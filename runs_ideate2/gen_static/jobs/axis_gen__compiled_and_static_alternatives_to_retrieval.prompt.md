=== SYSTEM ===
You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
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
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.

Two further requirements, both checked mechanically before review:
- Falsifiable Predictions: for every prediction write the outcome that would falsify it AND the arm or cell that can
  produce that outcome. If no arm can produce it (the split never gives the model that information; an append-only
  store cannot forget; a warm-started adapter always relearns faster than a cold one; the estimand is an identity of
  another quantity you compare it to; the falsifier lies inside your stated confidence interval), the prediction is
  entailed by the design and must be removed or the design changed. A proposal whose headline prediction is entailed
  is sent back before any judge sees it.
- One of your literature searches must be phrased in the home vocabulary of the mechanism, with no agent, memory,
  retrieval, experience or benchmark words (e.g. "data poisoning number of poison samples threshold" rather than
  "stale items in the agent's memory bank"); label it `home:` in the Preprint Collision Check. Papers that pre-empt
  a claim are usually found there, not under the agent-memory phrasing.

Standard IDEA JSON fields: Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Baselines and Ablations,
Falsifiable Predictions, Measurement and Noise Control, Preprint Collision Check, Risk Factors and Limitations.

=== USER ===
# Title: When Does Experience Memory Need a Query: Retrieval Against Static Prompts, Compiled Playbooks and the Whole Bank in Context

Author: Fable 5.1, 2026-09-09. Stage-1 brief for the ideate2 pipeline, after the Stage-0 pre-scan on this topic (5 axes,
60 papers carded from S2 + HF, 25 gaps; `digest.md`; no section reads) and after Step 0 on this node
(`runs/STEP0_RESULTS.md`). Third topic of the program alongside `xfer` and `credit`; the 51 archived ideas are the prior,
and four of them (compile_dont_retrieve 6.0, memory_or_instruction 5.92, decorative_retriever 5.75,
optimizer_substitutes_for_memory_scaffold 5.22) sit on this exact question.

## Keywords
LLM agents, experience memory, retrieval, static prompt, few-shot exemplars, compiled instructions, playbooks, long context,
many-shot in-context learning, prompt caching, near-duplicate leakage, ALFWorld, WebShop

## TL;DR
Agent-memory papers report the gain of a retriever over no memory; almost none report the gain over the cheapest
alternative, a fixed prompt built once from the same experience: a per-type procedure sentence, a curated exemplar set, a
compiled playbook, or the whole bank in a long context. The scan finds this control missing under every axis (G2, G6, G11,
G22), the whole-bank long-context arm missing (G3, G12, G17, G21), retrieval gains scored on recall rather than task
success (G18, G23), and run-to-run variance unreported (G4, G8, G24). The one memory-vs-long-context cost study is
conversational QA with one model (2603.04814); the one corpus-size sweep finds crossovers but with one reader and on
documents, not trajectories (2607.26497). On this node the question is already half-measured: the retrieval gain on
ALFWorld is procedure-bound (unseen ≈ seen), which predicts that a static per-type procedure prompt captures most of it,
and Measurement C is testing exactly that. This track asks for the sharp claim about what property of a task
distribution makes a query necessary, and how to tell before building a retriever.

## Starting position (measured here; not to be rediscovered)
- **Retrieval on this node (Measurement A):** expert bank, Qwen3-32B, k=0 0.536/0.549 → k=1 0.739/0.776 → k=3 0.807/0.869
  → k=7 0.846/0.877 (valid_seen/valid_unseen); net +27/+32 at k=3; gain carried by clean/heat/cool procedures (+39 to +55),
  pick-and-place +15, pick-two +18, look-at-in-light −4.8; unseen ≈ seen, so the retrieved value is the type's procedure,
  not the scene. Injected tokens ~140/430/1,010 at k=1/3/7; ALFWorld has six task templates, so a bank of 1,465 items has
  at most six procedures in it.
- **Measurement C (running; appended before generation if finished, otherwise before review):** five static arms paired with
  the same games and seeds as A: one fixed expert exemplar of the task's type (token-matched to k=1), three fixed
  exemplars (matched to k=3), one fixed exemplar of a different type (length placebo), a one-paragraph hand-written
  procedure for the type in the instruction slot (~60 tokens), and all six procedures in one type-agnostic prompt
  (~400 tokens). The first two remove the retriever but keep type conditioning (the goal sentence reveals the type); the
  last removes even that. The comparison of interest is retrieval minus the best static arm, per type, with the ±8-net
  paired floor.
- **Two pools on disk** (expert 1,465; self 1,892 successes across all six types); the self pool contains the agent's own
  detours and is the on-policy counterpart of a curated playbook.
- **Noise floor:** ±8 net at 274 games × 2 seeds; per-type ±13–15; the previous round's judges rejected every claim below it.
- **Cost:** a static prefix is prefix-cached by vLLM; retrieval injects a different prefix per episode, so the token cost
  difference is measurable on this node (prefill tokens per episode are logged).

## What the Stage-0 scan says, by axis (gap ids as in `digest.md`)
1. **Compiled and static alternatives** (13 cards). Strategy graphs distilled from trajectories (2511.07800), skill graphs
   promoted by verifier replay (2512.23760), tool-graph memory (2604.07791), tutorials from screen recordings (2606.03951),
   ICAL insight exemplars (2406.14596), synthetic-task pre-built playbooks at 2–3× lower deployment cost (Preping
   2605.13880), MemAPO's argument that per-query retrieval beats one compiled prompt (2603.21520), CLEAR's argument that a
   generated context beats retrieved experience (2604.07487); SkillEvolBench finds raw-trajectory reuse often beats
   distilled skills (2605.24117). Gaps G1–G5: compiled vs retrieved never at matched tokens; retriever vs fixed exemplars
   never isolated; no whole-bank arm; no variance; no size scaling.
2. **Environment properties that make retrieval necessary** (13 cards). State-gated retrieval failures (SGR-Bench
   2605.22219), memory-dependent tool parameters (Mem2ActBench 2601.19935), interdependent sessions (MemoryArena
   2602.16313), related-task experience helps only when correctly selected (SWE-ContextBench 2602.08316), cue-anchored
   deterministic injection beats voluntary memory reads (2607.20972). Gaps G6–G10: retrieval vs knowledge never separated;
   deficits not split into retrieval vs application; no variance; recall vs action; relatedness threshold unmeasured.
3. **The query and the retriever** (37 cards). Utility-trained and trajectory-trained retrievers (2601.11888, 2604.04949,
   2605.04018), adaptive retrieval decisions (2607.07380, SPARKLE), direct corpus interaction without a retriever
   (2605.05242), retrieval dominates write strategy on LoCoMo (2603.02473), positional bias marginal in realistic RAG
   (2505.15561), compliance trap (2607.10608). Gaps G11–G15: retriever vs random/fixed/compiled at matched length;
   retrieval vs whole history; retriever metrics vs end-task success; adaptive policies vs always/never retrieve at cost;
   asymmetry of right vs wrong retrieved memory and near-duplicate dependence.
4. **Scaling both routes** (14 cards). Memory vs long-context break-even after ~10 turns at 100k tokens (2603.04814);
   BM25 overtakes agentic file-system search at ~10M corpus tokens (2607.26497); in-context routing collapses past ~500
   capabilities (2608.22695); many-shot saturation (2512.04106, 2603.24690); effective context shorter than advertised
   (2411.05000). Gaps G16–G20: crossovers measured with one reader; no matched-budget whole-corpus arm; recall not task
   success; shot saturation vs whole-bank untested; documents, not trajectories.
5. **Evaluation and cost** (33 cards). Cost models with prompt caching (2603.04814, AdaptiveScale), agent compute scaling
   (2506.04301), DOS RAG as the baseline complex pipelines must beat (2506.03989), retrieval planning as the bottleneck
   (2603.14468), fault propagation (2608.20627). Gaps G21–G25: same-budget static or full-context control; random/fixed
   selection control; recall vs task success; variance; accuracy–cost curves under caching.

## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **The static arm is the baseline, not an ablation.** Every retrieval claim is reported as retrieval minus the best
  static alternative built from the same experience at matched tokens (fixed exemplars, compiled procedure, whole bank
  in context where it fits), on the same (game, seed).
- **Type conditioning is controlled.** On template environments the goal sentence gives away the task type; a
  "no-retriever" arm that selects by type is a type-conditioned prompt, and a type-agnostic arm (all procedures, or a
  fixed exemplar of a random type) must also be run.
- **The environment property is manipulated, not named.** Claims of the form "retrieval is needed when X" require at least
  two levels of X built into the bank or the task set (near-duplicate rate, instance-specific bindings, procedure count,
  distractor items) on one environment, or the same manipulation on two environments.
- **Task success, not recall**, is the primary outcome; retriever metrics are secondary.
- **Whole-bank long-context arm** whenever the bank fits the 16k context (it does for ALFWorld at ~140 tokens per item up
  to ~80 items; larger banks need a stated truncation rule).
- **Cost accounting under caching.** Prefill tokens per episode for static (cached) and retrieved (uncached) prefixes are
  logged; accuracy–cost curves, not accuracy alone.
- **Variance:** paired cells, ±8 net floor at 274 × 2; margins as fractions of the Gate-0 retrieval gain; per-type claims
  on pooled cells or declared exploratory.
- **No prediction entailed by a definition** (a whole-bank arm that contains the retrieved items cannot lose information;
  a type-conditioned static arm on a six-template benchmark equals retrieval by construction unless bindings matter);
  per prediction, the falsifying outcome and the arm that can produce it.
- **Home-vocabulary search**: in-context example selection, demonstration retrieval vs random demonstrations, few-shot
  saturation, long-context vs RAG, prompt compression; one query without agent/memory/benchmark words.
- **Must pass the four archived ideas** on this question (appendix A) by manipulating what they only observed.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 What Measurement C leaves: the residual of retrieval over the best static prompt (G2, G6, G11, G22).** Per type, is
  the residual zero on procedure-bound types and positive only where bindings matter; does it survive a type-agnostic
  static prompt; what is its token cost under caching.
- **Q2 Manipulating the property (G10, G15).** Build banks with controlled near-duplicate rates, controlled procedure
  counts, or planted instance-specific bindings (object–receptacle pairs that vary within a type), and show where the
  retrieval residual appears; predict the threshold and test it on a second environment (WebShop) with different
  template structure.
- **Q3 Whole bank in context vs retrieval (G3, G12, G17, G19).** As the bank grows from 6 to 80 to 1,465 items, where does
  many-shot context stop matching top-k retrieval on success and on cost; does the crossover move with the reader.
- **Q4 Compiled vs retrieved at matched tokens (G1, G5).** Procedures, playbooks and distilled skills compiled once from the
  expert pool vs raw retrieval, with the self pool as the on-policy variant; SkillEvolBench's raw-beats-skills result
  as the prior to overturn or bound.
- **Q5 The query (G13, G14).** Goal-sentence retrieval vs state-conditioned retrieval vs stall-triggered retrieval against
  the static arm and against random selection; is any retriever more than decorative on this environment, and at what
  per-episode cost.
- **Q6 Cross-environment generality (G16, G20, G23).** The same design on ALFWorld and WebShop: does the static-prompt
  residual change sign with environment structure, and can a bank statistic (template count, binding entropy) predict it.

## In scope
- ALFWorld primary (Measurement C on disk), WebShop as the second environment when a claim needs it; public data only.
- Qwen3-32B reader; a second backbone only for the crossover-moves-with-reader question.
- Compiled artifacts written by rule or by Qwen3-32B from the pools; prompt optimization (MIPRO/GEPA-style) as a compiler
  is in scope but its own value was the first topic; here it is one static arm among others.

## Out of scope
- Frontier-model compilers at experiment time; clinical or private data.
- New retrievers whose contribution is a higher recall number.
- Restating the four archived ideas (appendix A) or the first topic's substitution ideas.

## Resource constraints
Two A100 80GB, ~20 episodes/min. A 5-arm static measurement is 2,740 episodes (~2.5 h, running); each additional arm at
274 × 2 seeds is ~30 min; a bank-size ladder (6 sizes × 2 routes) is ~6 h; WebShop needs its own environment install (not
yet on this node) and is a day of setup. Static prefixes are cached across a whole arm, so cost differences are measured,
not modelled. Pre-registration before the first confirmatory cell.

## Appendix A: archived ideas on this question (do not restate; the gate compares against all 51)
- compile_dont_retrieve (6.0, round 1): the query-conditioned read in agentic experience memory is inert. Judges: observed
  on one environment with no manipulation of the property that would make the read non-inert.
- memory_or_instruction (5.92): is your agent's memory just an un-optimized prompt; residual value of retrieved experience
  after instruction optimization. Judges: the residual was below the noise floor; no static exemplar arm.
- decorative_retriever (5.75): retrieval-set overlap predicts whether procedural memory must be retrieved or can be frozen.
  Judges: overlap was observed, not manipulated.
- optimizer_substitutes_for_memory_scaffold (5.22): instructions substitute for memory's scaffold and leave only its content
  harm. Judges: scaffold vs content was not separable in the design.
- Adjacent: memory_budget_confound (5.63), abstraction_discards_bindings_and_repairs (5.95), order_randomized_leakage_audit
  (5.7), coverage_limited_context_count_limited_weights (5.35, round 3), first_item_additive_rest_substitutive (5.4).

## Appendix B: what the previous rounds' judges demanded (binding)
Same pool / same backbone / one cost axis; static-prompt baseline first; token- and rate-matched placebos; margins tied to the
measured effect; positive controls before any null; no prediction entailed by a definition; manipulate, do not observe;
searches in the mechanism's home literature.


## Your axis
compiled and static alternatives to retrieval: instructions, cheatsheets, playbooks and fixed exemplar sets compiled from experience once and reused without a retriever, versus query-time retrieval; prompt optimizers as compilers

## Digest gaps on your axis (cite by ID)
- G1: No card establishes whether distilling trajectories into compiled skills, strategies, or tutorials beats query-time retrieval of the raw trajectories at matched prompt length, and SkillEvolBench's finding that raw reuse often wins leaves the source of any compilation gain (distillation, weighting, auditability, or simply extra context) unresolved. (cards arxiv:2511.07800, arxiv:2512.23760, arxiv:2604.07791, arxiv:2605.24117, arxiv:2606.03951, arxiv:2509.16189)
- G2: Whether a retriever contributes anything beyond a fixed curated exemplar set or a static playbook is not isolated: several systems build memory but do not state whether it is consumed via per-query retrieval or supplied statically, and none compares against random or fixed exemplars. (cards arxiv:2605.13880, arxiv:2406.14596, arxiv:2604.07487, arxiv:2512.04106, arxiv:2606.03951)
- G3: No card tests a long-context condition that places the entire memory bank (all trajectories, all strategies, or all exemplars) in the prompt at once, so whether retrieval is necessary or merely a substitute for context length is open. (cards arxiv:2605.24117, arxiv:2512.04106, arxiv:2603.21520, s2:f2b0e4a048464616619a85b86f61df77ac4ac6b0)
- G4: The run-to-run variance of memory-induced gains is unreported across the axis, even where gains are described as unstable under frozen deployment, so it is unknown which reported deltas exceed seed noise. (cards arxiv:2511.07800, arxiv:2605.24117, arxiv:2605.13880, s2:f2b0e4a048464616619a85b86f61df77ac4ac6b0)
- G5: How gains scale with memory or bank size, and what the memory route costs per step (extra generation calls, retrieval, injected tokens, clutter as the store grows), is not reported, so the cost-normalized value of retrieval versus compiled memory is unknown. (cards arxiv:2603.21520, arxiv:2406.14596, arxiv:2607.20972, arxiv:2604.07791, arxiv:2604.07487)

## Digest cards for your axis and the cross-axis papers
- arxiv:2511.07800 (2025-11-11): A trainable, multi-layered graph memory that distills agent trajectories into weighted, human-interpretable strategic meta-cognitions improves LLM agents' strategic reasoning and generalization and provides consistent benefits during RL training. | limitations: not stated | not tested: The abstract does not compare the distilled strategy memory against a static compiled instruction set or fixed exemplars, nor against raw-trajectory retrieval at matched prompt length, so the source of the gain (distillation, weighting, or simply extra context) is unclear; run-to-run variance of the memory gain is not mentioned.
- arxiv:2512.23760 (2025-12-28): Agent self-improvement can be reframed as iterative compilation of successful trajectories into an auditable skill graph whose entries are promoted only after verifier-backed replay and contract checks, yielding reusable, verifiable capabilities rather than opaque parameter updates. | limitations: not stated | not tested: The abstract reports no comparison of the compiled skill graph against query-time retrieval of raw trajectories or against a static instruction set, so whether compilation matters beyond auditability is not established; no evaluation on standard agent benchmarks or across environments is described.
- arxiv:2604.07791 (2026-04-09): A structured tool-graph experience memory that integrates planning with execution lets resource-constrained agents self-evolve from their trajectories, generalize across analogous contexts through tool reuse, and densify sparse outcome-based rewards. | limitations: not stated | not tested: No comparison against directly retrieving raw interaction experiences or a static compiled tool set is stated; no ablation isolating the memory from the policy RL, and no report of memory size or per-step retrieval cost.
- arxiv:2603.21520 (2026-03-23): Prompt optimization should accumulate a reusable, self-evolving memory of strategies and error patterns retrieved per query, rather than compile one prompt specialized to a fixed task, improving generalization across heterogeneous queries while cutting optimization cost. | limitations: not stated | not tested: Whether a single compiled prompt containing the whole strategy memory would match per-query retrieval, and the sensitivity of gains to memory size or to random retrieval, are not stated.
- arxiv:2604.07487 (2026-04-08): Generating task-specific context with a trained context augmentation model beats retrieving and reusing past-experience context, because retrieved context must otherwise be adapted by the execution agent at extra reasoning cost. | limitations: not stated | not tested: Only two environments, with the WebShop result on a subset; the abstract does not say whether generated context is compared against a fixed compiled playbook or random exemplars, nor report the token cost of the extra CAM call.
- arxiv:2512.04106 (2025-11-25): Retrieval-augmented few-shot prompting with semantically similar examples consistently beats random-example few-shot prompting, zero-shot prompting and fine-tuned Gemini on code vulnerability detection, though a fine-tuned CodeBERT still scores higher. | limitations: not stated | not tested: Only one prompting model (Gemini-1.5-Flash) and one task, so generality of the retrieval advantage is untested; a fixed curated exemplar set and shot counts beyond 20 (saturation or a whole-bank long-context prompt) are not reported in the abstract.
- arxiv:2607.20972 (2026-07-23): The load-bearing memory for long-running coding agents is situationally cued operational facts that must be delivered deterministically by the harness, because agents almost never voluntarily read or write document-style memory. | limitations: not stated | not tested: The evaluation is a single coding task with a small set of seeded facts, so cross-task generality and effect on task success rate are not shown; the model does not measure whether cue-triggered injection adds noise or cost when the memory store grows large.
- s2:f2b0e4a048464616619a85b86f61df77ac4ac6b0 (2025-11-02): An agentic long-context RAG pipeline that combines chunk retrieval with cached ground-truth MCQs and a one-million-token context yields the most accurate context-specific quiz generation for engineering education. | limitations: not stated | not tested: Does not isolate a 1M-context-without-cache or cache-without-retrieval condition, so the retriever's contribution beyond the cached exemplars and long context is unclear; does not report token cost or run-to-run variance on the 150-question set.
- arxiv:2605.24117 (2026-05-22): Current LLM agents rarely distill episodic experience into robust reusable procedural skills: raw-trajectory reuse frequently outperforms distilled skills, skill gains are unstable under frozen deployment, and writing more skills or larger resource libraries adds coverage but also episode-specific drift and procedural clutter. | limitations: not stated | not tested: The abstract does not say how raw trajectories are selected for reuse (retrieved versus fixed), so the retriever's contribution to the raw-trajectory advantage is unclear; it also does not report run-to-run noise of the skill-condition gains that it calls unstable, or a long-context condition that supplies all trajectories at once.
- arxiv:2605.13880 (2026-05-11): An agent can build useful procedural memory before seeing any target-environment tasks by practising on proposer-controlled synthetic tasks with validated trajectory insertion, reaching performance competitive with playbook methods built from real offline or online experience at lower deployment cost. | limitations: not stated | not tested: The abstract does not state whether the pre-built memory is consumed via a retriever or as a static playbook at deployment, so the retrieval component's contribution is not isolated; it also does not report how the gain scales with synthetic bank size or how noisy the gains are across runs.
- arxiv:2509.16189 (2025-09-19): Machine learning systems generalize poorly in part because they lack latent learning (acquiring task-irrelevant information for future use), and episodic memory via retrieval can complement parametric learning to enable more flexible reuse of experiences. | limitations: not stated | not tested: Whether a realistic, non-oracle retriever recovers the gains, and whether the same experiences compiled once into parameters or a static prompt would match query-time retrieval.
- arxiv:2606.03951 (2026-06-02): Structured multimodal tutorials distilled from human screen recordings and interaction logs are effective knowledge representations that improve both human learning and GUI-agent planning and generalization, surpassing human-authored tutorials. | limitations: not stated | not tested: Whether tutorials are supplied statically or retrieved per task, how the gain compares to giving the agent raw or retrieved demonstrations, and how well tutorials generalize across applications beyond the documented software.
- arxiv:2406.14596 (2024-06-20): LLMs and VLMs can abstract sub-optimal demonstrations plus human feedback into a memory of insight-annotated exemplars that, when used as prompt examples in retrieval-augmented agents, substantially improve decision-making and reduce reliance on expert-crafted examples. | limitations: not stated | not tested: Whether the abstracted insights work as a fixed exemplar set without a retriever, how gains vary with memory size or number of exemplars, and retrieval versus random exemplars is not reported in the abstract.
- arxiv:2603.04814 (2026-03-05): A fact-based memory system (Mem0) and long-context LLM inference have structurally different accuracy-cost profiles: long context wins on factual recall for most benchmarks, but the memory system becomes cheaper after roughly ten turns at 100k-token context, with the break-even point falling as context grows. | limitations: not stated | not tested: Only a single long-context model (GPT-5-mini) and a single memory framework (Mem0) are compared, so the accuracy gap may not generalize across models or memory designs; the evaluation is conversational QA rather than agentic task-solving, so it says nothing about whether retrieved facts help action selection.
- arxiv:2603.18272 (2026-03-18): Training LLM agents (via LoRA SFT) to use retrieved experience trajectories in-context combines the strengths of fine-tuning and training-free experience retrieval and significantly improves generalization to unseen tasks. | limitations: not stated | not tested: The abstract does not say whether retrieval is compared against a random or fixed exemplar set at matched prompt length, so it is unclear how much of the gain depends on retrieval quality versus simply having trajectories in context; it also does not indicate whether the retrieval advantage holds across environments with different task-template structure.
- arxiv:2506.03989 (2025-06-04): Under matched token budgets with long-context LMs, a simple retrieve-then-read pipeline that preserves original document order (DOS RAG) consistently matches or beats more complex multi-stage RAG pipelines, so added pipeline complexity must justify itself against this baseline. | limitations: not stated | not tested: The comparison is among RAG pipelines for document QA and does not include a no-retrieval full-document long-context arm at the same budget in the abstract's description, nor retrieval of agent experience or exemplars; the retriever is treated as given rather than compared against random or fixed passage selection.
- arxiv:2509.24183 (2025-09-29): A lightweight VLM that retrieves web tutorials at inference time and is trained with SFT plus self-guided rejection-sampling fine-tuning acts as a model-agnostic plug-in that consistently improves GUI agents. | limitations: not stated | not tested: The abstract does not report a control in which the same tutorial guidance is compiled once into a static prompt or a fixed tutorial set is used without a retriever, so the contribution of query-time retrieval versus tutorial content is not isolated; the query used for retrieval (goal versus current screen state) is not specified.
- arxiv:2508.14817 (2025-08-20): Targeted retrieval over EHR notes remains a competitive and more token-efficient alternative to long-context prompting for clinical reasoning, even as newer models handle longer inputs. | limitations: Missing information in the clinical notes, often due to inter-hospital transfers, limited performance to some extent; diagnosis generation suggests ceiling effects imposed by documentation variability and evaluation constraints. | not tested: Single health system and three tasks, so cross-site generality is untested; run-to-run variance and the retriever's quality against a random or fixed note selection are not reported.
- arxiv:2601.19935 (2026-01-13): Existing memory benchmarks test passive fact retrieval, and current memory frameworks are inadequate at actively applying long-term memory to ground tool-call parameters in task execution. | limitations: not stated | not tested: No comparison against a no-memory or full-history long-context baseline is reported in the abstract, so it is unclear how much of the deficit is retrieval versus application; the sessions and tasks are synthetic, so robustness to real interrupted user histories is untested.
- arxiv:2605.22219 (2026-05-21): Search agents fail on specialized data-retrieval websites mainly because they establish the wrong site-specific retrieval state (filters, views, scopes), not because they cannot compose answers. | limitations: not stated | not tested: Whether providing agents with stored site-specific procedures (e.g., a playbook of how to configure each site) or prior successful trajectories would fix scope drift is not tested; run-to-run variance of the agents is not reported in the abstract.
- arxiv:2605.05242 (2026-05-03): For agentic search, letting the agent interact with the raw corpus directly through general-purpose terminal tools outperforms fixed top-k lexical, dense and reranking retrievers, because retrieval quality depends on the resolution of the corpus interface, not only on reasoning. | limitations: not stated | not tested: Token and latency cost of multi-step terminal search versus a single top-k call is not quantified in the abstract; the approach is not tested on corpora too large for grep-style scanning, and the dependence of gains on agent strength is asserted rather than measured across model sizes.
- arxiv:2602.08316 (2026-02-09): Correctly selected summarized experience from related tasks improves programming-agent resolution accuracy and substantially reduces runtime and token cost, while unfiltered or incorrectly selected experience gives limited or negative benefit. | limitations: not stated | not tested: The abstract does not state which agents or models were evaluated or the run-to-run variance of the gains; the related tasks are drawn from explicit dependency links, so gains on unrelated or diverse task sequences are not measured.
- arxiv:2605.12493 (2026-05-12): Memory systems should be evaluated on whether they internalize environment-specific experience, and a coding agent that gathers evidence from stored trajectories substantially outperforms RAG-based memory on this, at a high latency cost. | limitations: Despite the strong performance gains, coding agent based methods have high latency costs; substantial room for improvement remains. | not tested: The benchmark scores evidence gathering for question answering rather than downstream task success, so whether recalled experience improves action-taking is not shown; a whole-history long-context baseline is not mentioned, and token cost is only characterized as latency.
- arxiv:2509.21035 (2025-09-25): Treating knowledge-graph context construction as a budgeted sequential decision process yields higher multi-hop QA accuracy with smaller, provenance-preserving contexts and lower, more predictable latency than static k-hop expansion or GraphRAG. | limitations: not stated | not tested: Training cost of LC-MAPPO and transfer of the learned policies to new knowledge graphs are not described in the abstract; the comparison excludes a long-context baseline that simply includes a large static subgraph, and variance across runs is not reported.
- arxiv:2509.16442 (2025-09-19): LLM-based data augmentation improves compact dual-encoder retrieval, but the benefit saturates beyond a certain augmentation scale even with diverse strategies, smaller augmentation LLMs are competitive with larger ones, and the gain is largest for poorly pre-trained retrievers. | limitations: not stated | not tested: The study concerns training-data augmentation for retrievers, not retrieval at inference time for agents, so nothing is shown about how retrieved items affect downstream LLM task performance; the abstract does not name the OOD benchmarks or quantify the saturation point.
- arxiv:2510.01353 (2025-10-01): Long-term memory and state tracking in dynamic, multi-platform enterprise agent environments is largely unsolved: the best model (GPT-5) reaches only 60% Correctness on MEMTRACK, with failures in long-horizon memory use, cross-platform dependencies and contradiction resolution. | limitations: not stated | not tested: Does not compare query-time retrieval against a static compiled summary of the timeline or against placing the whole timeline in a long context; does not report run-to-run variance of memory-backend gains or token cost per backend.
- arxiv:2604.04949 (2026-03-30): Retrievers for agentic search should be trained from agent interaction trajectories rather than human click logs, and doing so improves evidence recall, task success and execution efficiency across agent architectures and scales. | limitations: not stated | not tested: Does not compare the learned retriever against random or fixed exemplar/document sets to show the retriever is not decorative; does not test whether gains transfer to experience/trajectory memory banks rather than document corpora, or quantify token cost.
- s2:ed199025da9dc8cd2a6daea44970d50977bac11b (2026-06-23): Retrieval quality is the main determinant of end-to-end RAG quality in knowledge-management QA, and 256-token chunking with overlap, top-1 retrieval and grounded prompting are robust design choices, while abstention-oriented prompting is a separate operating point rather than a default. | limitations: The design narrows practical claims to what is supported by multi-dataset evidence, error analysis and long-context testing. | not tested: Does not test a no-retrieval or fixed-context baseline against retrieval on the same generators; does not report run-to-run variance or prompt caching/token accounting for the long-context stress condition.
- arxiv:2511.20857 (2025-11-25): Agent memory should be evaluated as test-time evolution over sequential task streams rather than static conversational recall, and the proposed ReMem action-think-memory pipeline enables continual improvement over an ExpRAG experience-retrieval baseline. | limitations: not stated | not tested: Does not compare experience retrieval against a fixed exemplar set or compiled instructions built once from the stream; does not report run-to-run noise of memory gains or how much of the gain comes from near-duplicate tasks within a stream.
- arxiv:2603.24690 (2026-03-25): In-context learning in unified multimodal models is non-monotonic and task-dependent, and a capability-oriented taxonomy plus a lightweight Context-Adaptive Prototype Modulator stabilizes few-shot adaptation and outperforms larger multimodal baselines on most understanding ICL tasks. | limitations: not stated | not tested: Does not test retrieved versus fixed or random demonstration sets, nor scaling beyond 8 shots to assess saturation with the number of exemplars.
- arxiv:2602.16313 (2026-02-18): Existing memory benchmarks decouple memorization from action, and agents that near-saturate long-context memory benchmarks like LoCoMo perform poorly when memory must be acquired through interaction and used to guide later interdependent subtasks. | limitations: not_stated | not tested: Does not compare retrieval-based memory against a static compiled summary or full long-context replay of earlier sessions; does not report run-to-run noise or token cost of memory mechanisms.
- arxiv:2602.12192 (2026-02-12): Attention scores of selected retrieval heads can be trained into a lightweight listwise reranker that outperforms state-of-the-art pointwise and listwise rerankers and sets a new state of the art on LoCoMo. | limitations: not stated | not tested: Does not compare the reranker against feeding the full long context without reranking or against random/fixed passage selection; does not report end-to-end token cost or run-to-run variance.
- arxiv:2606.24775 (2026-06-23): No single agent-memory architecture dominates across workloads; effectiveness depends on aligning memory structure with the workload bottleneck, and localized maintenance is more cost-efficient than global reorganization. | limitations: not stated | not tested: Does not report whether the two reference baselines include a static compiled context or full long-context replay, nor run-to-run noise of the reported differences; cross-environment generality beyond the five workloads is not addressed.
- arxiv:2502.18017 (2025-02-25): A multi-agent RAG framework with a GMM-based hybrid multi-modal retrieval strategy and an iterative exploration-summarization-reflection agent workflow substantially improves retrieval-augmented reasoning over visually rich documents. | limitations: not stated | not tested: Whether the >10% gain comes from the hybrid retrieval versus the extra reasoning tokens of the agent workflow is not separated in the abstract; no evaluation on benchmarks other than the authors' own ViDoSeek, and no token/latency cost accounting for the iterative agent loop is reported.
- arxiv:2602.02007 (2026-02-02): Because agent memory is a bounded, highly correlated and often duplicated dialogue stream rather than a heterogeneous corpus, fixed top-k similarity retrieval returns redundant context, and retrieval should instead operate over a hierarchy of decoupled semantic components with expansion to raw episodes only when it reduces reader uncertainty. | limitations: not stated | not tested: Only long-conversation QA benchmarks are used, so whether the decoupling-aggregation advantage transfers to agentic task environments is untested; the abstract does not compare against a long-context baseline that simply includes the whole dialogue stream, nor report construction cost of the hierarchy.
- arxiv:2607.26497 (2026-07-30): Across a controlled corpus-size sweep, no RAG paradigm wins unconditionally: an agentic file-system search leads at small corpora, but BM25 lexical retrieval overtakes it around 10 million corpus tokens and leads at every larger tier, making global candidate ranking the strongest scalable default with agentic reasoning best applied after ranked discovery. | limitations: not stated | not tested: Only one reader model and one question set are used, so whether the crossover point shifts with reader capability or task type is untested; the study covers document corpora, not experience or trajectory banks, so the scaling conclusions for agent memory are not established.
- arxiv:2608.22695 (2026-08-24): In-context routing over a capability registry collapses as the registry grows, whereas an offline-enriched retrieve-then-rank pipeline degrades gracefully and is both more accurate and far cheaper at scale. | limitations: not stated | not tested: Match@1 measures whether the right capability is selected, not end-task success after invoking it; the retrieve-then-rank pipeline's own accuracy still falls to 0.39 at full scale, and the abstract does not report how much of that is retrieval recall failure versus reranking error or how the sweep behaves with stronger routing LLMs than Nova Micro.
- arxiv:2603.02473 (2026-04-12): In memory-augmented LLM agents, the retrieval method dominates performance far more than the write strategy, raw chunked storage matches or beats expensive lossy write pipelines, and failures manifest mostly at the retrieval stage rather than at utilization. | limitations: not stated | not tested: Only the LoCoMo conversational QA benchmark is used, so whether retrieval dominance holds for procedural or task-oriented agent memory is untested; the abstract reports no run-to-run variance and no comparison against putting the full history in a long context without retrieval.
- arxiv:2608.20627 (2026-08-20): In multi-hop agentic RAG, post-hoc trace-based diagnosis loses the signal needed to identify an injected retrieval fault once the downstream trajectory changes, so propagation depth must be an explicit evaluation axis for failure attribution. | limitations: Depth-3 content estimates are descriptive only because they contain three failed cases; the depth-2 counterfactual comparison is an exploratory pooled comparison distinguished from broad evidence of post-hoc signal loss as a small-sample method comparison. | not tested: Only one agent model (Claude Haiku 4.5) and one dataset (80 MuSiQue questions) are used, so generality across models and retrieval settings is untested; the benchmark evaluates fault attribution, not whether the agent's later retrieval actually repairs trajectories at a measurable rate.
- arxiv:2603.14468 (2026-03-15): Multi-hop evidence retrieval planning, not answer generation, is the primary bottleneck for agentic long-video QA, with frontier agents scoring below 50% under enforced retrieval necessity but near-perfect with gold evidence clips. | limitations: not stated | not tested: Only one agent design (VideoAgent-style) is varied over backbones, so whether different retrieval-planning strategies close the gap is untested; the fixed retrieval backend means retriever quality itself is not varied, and run-to-run variance of the accuracy numbers is not reported.
- arxiv:2607.10608 (2026-07-12): Agents adopt conflicting retrieved memory at the first exposed decision point even when it is task-wrong, repeated exposure amplifies the error and recovery is weak, so once agents comply their success collapses to a low floor and stronger agents suffer larger absolute damage. | limitations: not stated | not tested: Whether correct or non-conflicting memory yields the symmetric benefit (how much retrieved memory helps when it is right), and whether compiled/static instructions or random exemplars induce the same compliance behavior as retrieved entries.
- arxiv:2505.12065 (2025-05-17): Both exact and overly approximate retrieval degrade search-agent efficiency, and scheduling and retrieval stalls cause cascading latency; high-recall approximate retrieval with priority-aware scheduling and non-stall retrieval removes these bottlenecks without hurting generation quality. | limitations: not stated | not tested: Token or cost accounting of the retrieved content itself rather than latency and throughput, and whether the efficiency gains hold for agent memory retrieval over trajectories rather than document search.

Propose 3 proposals on this axis, each as a complete IDEA JSON with the two extra fields. Return JSON:
{"proposals":[{...}, ...]}.
