#!/usr/bin/env python3
"""Every ideate2 prompt, verbatim, plus the unchanged constants imported from ideate.py so that
review scores stay comparable with the v2–v6 rounds."""
import os, sys
sys.path.insert(0, "/home/work/neuro/AI-Scientist-v2")
os.environ.setdefault("ANTHROPIC_API_KEY", "dummy-key-for-import-only")
try:
    import ideate as _ideate  # noqa: E402
    REVIEW_SYSTEM = _ideate.REVIEW_SYSTEM
    REVIEW_SCHEMA = _ideate.REVIEW_SCHEMA
    REVIEW_USER = _ideate.REVIEW_USER
    REVISE_SYSTEM = _ideate.REVISE_SYSTEM
    BRIEF_SYSTEM = _ideate.BRIEF_SYSTEM
    IDEA_FIELDS = _ideate.IDEA_FIELDS
    SCORE_WEIGHTS = _ideate.SCORE_WEIGHTS
except Exception as e:  # tiktoken etc. missing in a bare interpreter → use the frozen snapshot of the same constants
    import json as _json
    _snap = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ideate_constants.json")
    if os.path.exists(_snap):
        _c = _json.load(open(_snap))
        REVIEW_SYSTEM, REVIEW_SCHEMA, REVIEW_USER = _c["REVIEW_SYSTEM"], _c["REVIEW_SCHEMA"], _c["REVIEW_USER"]
        REVISE_SYSTEM, BRIEF_SYSTEM, IDEA_FIELDS, SCORE_WEIGHTS = _c["REVISE_SYSTEM"], _c["BRIEF_SYSTEM"], _c["IDEA_FIELDS"], _c["SCORE_WEIGHTS"]
    else:
        REVIEW_SYSTEM = REVIEW_USER = REVISE_SYSTEM = BRIEF_SYSTEM = ""
        REVIEW_SCHEMA = {}
        IDEA_FIELDS = ["Name", "Title", "Short Hypothesis", "Related Work", "Abstract", "Experiments",
                       "Baselines and Ablations", "Falsifiable Predictions", "Measurement and Noise Control",
                       "Preprint Collision Check", "Risk Factors and Limitations"]
        SCORE_WEIGHTS = {"novelty": .3, "significance": .25, "soundness": .25, "feasibility": .1, "clarity": .1}
    IMPORT_ERROR = repr(e)

PRESCAN_AXES_SYSTEM = """You are planning a literature pre-scan for a research area. Read the seed brief. Propose 4-7 orthogonal AXES along
which the area's design space varies (examples for an agent-memory area: memory structure; write/curation policy;
retrieval mechanism and injection budget; coupling with prompt optimization; evaluation methodology). An axis is a
dimension a paper takes a position on, not a topic. For each axis give: name, one-sentence definition, three search
queries phrased as a researcher would (mechanism phrasing, application phrasing, closest-method phrasing), and one
foundational query for the pre-2024 origin of the idea. Return JSON: {"axes":[{"name","definition","queries":[...],
"foundational":"..."}]}."""

PRESCAN_CARD_SYSTEM = """You are writing an index card for one paper from its title, abstract, TL;DR and, when available, its limitations or
conclusion text. Do not add anything the text does not support. Return JSON with exactly these keys:
"claim" (one sentence: what the paper asserts), "method" (one sentence), "evidence" (the setting, models, benchmarks
and the headline numbers if stated), "stated_limitations" (verbatim or near-verbatim, or "not stated"),
"not_tested" (one or two things a skeptical reader would note the paper does not test), "axes" (which of the
provided axes it takes a position on), "date", "id"."""

PRESCAN_SYNTH_SYSTEM = """You are given the index cards for one axis. Write the 3-5 open gaps these papers jointly expose: for each gap, one
sentence stating what is unresolved, the card IDs whose stated limitations or untested items point to it (at least
two), and one sentence on what evidence would settle it. Do not propose papers. Do not invent gaps that no card
supports. Return JSON: {"axis":"...","gaps":[{"gap","card_ids":[...],"evidence_needed"}]}."""

S2_FIRST = """Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it."""

AXIS_GENERATION_SYSTEM = """You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
axis of the research area below; propose ideas that take a position on that axis. You will not see ideas from other
axes; do not try to cover the whole area.

Bar to clear: contribution stateable in one sentence; positioning that names the closest prior work and what it does
not do; a central claim with an experiment that could come out against it; a measurement plan that separates an
effect from run-to-run noise; feasibility on small open models and single-node compute.

Use the literature digest you were given. Two fields are mandatory in your IDEA JSON in addition to the standard
ones: "Addresses gap": the digest gap ID this idea attacks, or "none" with one sentence on why the digest missed it;
"Not a restatement of": the nearest prior-result bullet in the brief and the nearest digest card, each with one
sentence on what this idea claims that they do not. If you cannot write those sentences, the idea is a restatement
and you must change it.

Before finalizing you must run at least two literature searches: one on the mechanism you are claiming, restricted
to the last twelve months, and one on the closest named method. Report what came back in "Preprint Collision Check",
including empty results, the query strings and the channel that answered. Do not write experiment code.
""" + S2_FIRST + """

Standard IDEA JSON fields: Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Baselines and Ablations,
Falsifiable Predictions, Measurement and Noise Control, Preprint Collision Check, Risk Factors and Limitations."""

AXIS_GENERATION_USER = """{brief}

## Your axis
{axis_name}: {axis_definition}

## Digest gaps on your axis (cite by ID)
{gaps}

## Digest cards for your axis and the cross-axis papers
{cards}

Propose {n} proposals on this axis, each as a complete IDEA JSON with the two extra fields. Return JSON:
{{"proposals":[{{...}}, ...]}}."""

GATE_ADJUDICATE_SYSTEM = """You are judging whether two research proposals (or a proposal and a prior finding) make the same claim. Read both.
Answer with exactly one label and one sentence: "same_claim_reworded" (the central claim and mechanism are the same;
differences are wording, setting or metric), "same_mechanism_new_measurement" (same mechanism, but the second
measures a quantity or runs a control the first does not, and that difference would change a reader's conclusion),
or "distinct". Return JSON {"label","reason"}."""

GATE_ADJUDICATE_USER = """A:
{a}

B:
{b}"""

NOVELTY_KEYS_SYSTEM = """Extract from this proposal, as short phrases, the search keys a reviewer would use to find prior work that already
makes its claim: "mechanism" (what causes what), "estimand" (the quantity measured), "controls" (named control arms),
"environment" (benchmarks/models). Return JSON with those four keys, each a list of 1-3 phrases."""

REVIEW_SYSTEM_OPENBOOK_SUFFIX = """

You have two literature search channels and a novelty card listing the closest candidates an automated search found.
""" + S2_FIRST + """
Rules for this review: (1) Run at least two searches on the proposal's claimed mechanism, one restricted to the last
twelve months, and at least one on its closest named method. (2) Verify every arXiv ID the proposal relies on for its
novelty argument; say which you verified and which you could not. (3) In "closest_prior_work" name a paper you found
or verified, with its ID; if the strongest threat you know is from memory and you could not verify it, say so and
label it unverified. (4) In "preprint_collision" report the queries you ran and what they returned, with IDs; an empty
search is reported as empty, not as evidence of novelty. (5) If a search finds a paper that already makes the central
claim, say "VERIFIED COLLISION: <id>" as the first words of "preprint_collision"; the aggregate will cap novelty. Score
novelty on what you verified, not on what the proposal asserts."""

NOVELTY_CARD_HEADER = """=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.
"""
