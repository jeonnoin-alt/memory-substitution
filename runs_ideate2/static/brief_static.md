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

**Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. Binding: any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.

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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.

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
