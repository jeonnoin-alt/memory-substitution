# ideate2 — literature-grounded, axial, open-book ideation pipeline

Redesign of the AI-Scientist-v2 ideation stage along three directions: (1) literature
infrastructure + Stage-0 pre-scan, (2) parallel axial generation + repackaging gate,
(3) open-book review with a mandatory novelty check. Design and prompts: `DESIGN.md`.

## Environment

```
python : /home/work/neuro/alfworld-env/bin/python   (sentence-transformers for gate/rerank/novelty)
key    : /home/work/.s2_env   (S2_API_KEY=...; chmod 600; never commit)
network: export S2_PIN_IP=18.244.60.91               (only DNS answer for api.semanticscholar.org that is not black-holed)
```

Reachability from this node (checked 2026-09-07): S2 (key + pinned IP) ✓, HF papers API ✓,
Claude Code WebSearch (server-side) ✓; arXiv/ar5iv/OpenAlex/alphaXiv/openreview/WebFetch ✗.
Full text therefore comes only through WebSearch subagents (`SectionReader.websearch_job`).

## Model policy (PI, 2026-09-07)

Generation (Stage 2 `axis_gen`) = **Fable 5.1**; every other LLM role (pre-scan cards/synth, gate adjudication, novelty keys, section reads, judges) = **Opus**. **Sonnet is prohibited.** The 2026-09-07 validation runs below predate this rule and used Sonnet for cards/gate/section reads.

## Backends

`--backend harness` (default; no Anthropic key needed): every LLM step is written as a job
(`<jobs_dir>/<kind>__<name>.prompt.md` + `.json`) which the Claude Code session launches as a
subagent; results are read back from the subagent transcript by `run.py collect`, `gate_collect.py`,
`ingest_sections.py`. `--backend api` calls the Messages API directly when a key exists.

## Stage 0 — pre-scan (`prescan.py`)

```
prescan.py plan    --slug S --brief brief.md --out W          # 1 job: axes + queries (PRESCAN_AXES)
prescan.py collect --slug S --axes W/axes.json --out W --rerank --top 32 --sections 8
                                                              # S2/HF/(OpenAlex/arXiv if reachable) → papers.jsonl
                                                              # + web_queries.json + jobs_sections/*.json
ingest_sections.py W/papers.jsonl mapping.json                # after the section-read subagents finish
prescan.py cards   --slug S --axes W/axes.json --out W --batch 8 --model opus     # card jobs (PRESCAN_CARD)
   → concatenate the card arrays into W/cards.jsonl (one card per line)
prescan.py synth   --slug S --out W --model opus              # 1 job per axis (PRESCAN_SYNTH) → W/gaps.json
prescan.py digest  --slug S --out W --brief brief.md          # digest.md + brief_with_digest.md
```

Ranking: 0.4·recency + 0.2·log-citations + 0.4·MiniLM relevance to the axis text (`--rerank`);
without `--rerank`, citation-heavy off-topic benchmarks dominate.

## Stage 2 — axial generation (`axes.py`)

```
axes.py emit  --axes W/axes.json --brief W/brief_with_digest.md --cards W/cards.jsonl --gaps W/gaps.json --n 3 --out G
axes.py merge --out G                                          # → G/ideas.json
```
One generator per axis with a fresh context; each gets the digest gaps/cards for its axis and the
multi-axis cards; WebSearch enabled; output = `{"proposals":[<11-field idea>...]}`.

## Stage 2.5 — repackaging gate (`gate.py`, `gate_collect.py`)

```
gate.py --ideas G/ideas.json --brief brief.md --cards W/cards.jsonl --out G/gate --backend harness
   thresholds default to mean + 1.5·SD of the pairwise cosine (absolute 0.55 put 27/27 ideas in one cluster)
   → gate_report.{md,json}; adjudication jobs batched 10 pairs each (GATE_ADJUDICATE, opus)
gate_collect.py G/gate mapping.json           # flatten batches → adjudications.json → gate_decisions.json
```
Labels: `distinct` / `same_mechanism_new_measurement` (keep, note) / `same_claim_reworded`
(idea–idea: send the later one back to differentiate; idea–prior: withdraw unless a new claim).

## Stage 2.7 — novelty card (`novelty_check.py`, `novelty_keys_collect.py`)

```
novelty_check.py --ideas G/ideas.json --out G/novelty --backend harness --model fable --batch 5   # key-extraction jobs (Fable)
#   one Fable subagent per novelty_keys__batchNN job → novelty_keys_collect.py G/novelty <map.json> → keys.json
novelty_check.py --ideas G/ideas.json --out G/novelty --keys G/novelty/keys.json --s2-queries 3
   → <name>.card.md/.json + candidates.jsonl; each candidate says which query CLASS found it
```
Queries come in classes, and the order matters because S2 (rate-limited) only sees the first `--s2-queries`:
`mechanism_home` (the phenomenon in the vocabulary of the field it came from, no agent/memory/benchmark words),
`agent` (the proposal's own phrasing), `adjacent` (the published result direction in a neighbouring field),
`baseline` (the cheapest intervention the proposal must beat), `methods`. Without LLM keys, `rule_keys` builds the
home queries by stripping the agent vocabulary and by keyword templates (`HOME_TEMPLATES`). Rationale (2026-09-08):
in two review rounds every paper that pre-empted a claim was found under the home vocabulary, never under the
agent-memory phrasing; the old cards recalled 6 of 57 judge-found papers.
Every arXiv id returned by a WebSearch subagent is re-resolved through S2 and HF before it may be
cited (`s2_resolves` / `hf_resolves`); unverified ids stay on the card but are marked.
The card is evidence for the reviewers; it carries no verdict.

## Stage 2.8 — entailment check (`entail.py`)

```
entail.py emit    --ideas G/ideas.json --out G/entail --batch 3 --model opus     # one Opus subagent per entail__batchNN job
entail.py collect --out G/entail --mapping <map.json>                            # entail_report.json, ENTAIL_REPORT.md, <name>.entail.md
entail.py revise  --ideas G/ideas.json --out G/entail --brief brief.md            # Fable revision jobs for verdict == revise
review_batch.py emit ... --entail G/entail                                        # attaches <name>.entail.md after the novelty card
```
For every prediction: the arms it rests on, the outcome that would falsify it, whether that outcome is reachable
under the stated design (split, retriever, update rule, estimand identity, ceiling, deleted tokens, absent arm) and
whether it is distinguishable at the stated noise. Labels `open / entailed / near_entailed / unresolvable`; an idea
whose headline prediction is not open goes back to the generator before any judge sees it. Rationale (2026-09-08):
in 28 reviews across two topics the most frequent fatal objection was a prediction entailed by the design, and the
gate cannot catch it because it is not a restatement.

## Stage 3 — open-book review (`review.py`)

```
review.py emit --idea idea.json --card G/novelty/<name>.card.md --out R --judges 1   # 1 → +2 on escalation
review.py aggregate --out R
```
Judges get WebSearch and must run ≥2 mechanism searches; `VERIFIED COLLISION:` in the novelty
field caps novelty at 4; weights nov .3 / sig .25 / snd .25 / fea .1 / cla .1; worst verdict wins.

## Validation runs (2026-09-07)

- `runs_ideate2/agent_memory/` — pre-scan on the memory-vs-instruction brief: 4 hand axes,
  32 papers kept after rerank, 8 section reads via WebSearch (2 verbatim, 4 paraphrased, 2 empty),
  cards + gaps + digest.
- `runs_ideate2/pool27/` — gate over the 27 archived AI-Scientist-v2 ideas: 2 clusters, 93 pairs,
  adjudications in `gate/adjudications.json`, decisions in `gate/gate_decisions.json`.
- `runs_ideate2/v6_novelty/` — novelty card for proposal v6 (API candidates + 12 web adjacents, 7 S2-verified).

## Search policy (PI, 2026-09-07)

Subagents search Semantic Scholar first through `s2cli.py` (keyed, IP-pinned, cross-process throttled at ~1 req/s) and
use WebSearch only when S2 returns nothing, for papers newer than S2's indexing lag, or for section text. WebFetch is
blocked on this node and must not be used. `S2_FIRST` in `prompts.py` carries this rule into the generator and judge prompts.
