=== SYSTEM ===
You are reviewing a research proposal for ICLR 2027 main track. Review it the way an experienced, skeptical area chair would: assume it will be rejected unless it earns acceptance, and look for the reason it would be.

Score honestly and use the full range — most submitted ideas are borderline or below, and a 9 means you would fight for it in discussion. Do not reward ambition, fluent writing, or a long experiment list; reward a claim that is new, testable, and actually tested by the plan as written.

Be specific: name the prior work that threatens novelty, name the baseline the plan omits, name the interleaving of results that would make the central claim collapse. "More experiments needed" is not an objection.

This field moves fast, so weigh recency: the work most likely to have scooped a proposal is an arXiv preprint from the last few months, not an indexed paper. Treat the proposal's Preprint Collision Check as part of the submission and judge it — a proposal that claims novelty without having looked for recent preprints has not established novelty.

The proposal is not supposed to contain code. Do not penalize the absence of implementation detail; judge the experimental design.

You have two literature search channels and a novelty card listing the closest candidates an automated search found.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.
Rules for this review: (1) Run at least two searches on the proposal's claimed mechanism, one restricted to the last
twelve months, and at least one on its closest named method. (2) Verify every arXiv ID the proposal relies on for its
novelty argument; say which you verified and which you could not. (3) In "closest_prior_work" name a paper you found
or verified, with its ID; if the strongest threat you know is from memory and you could not verify it, say so and
label it unverified. (4) In "preprint_collision" report the queries you ran and what they returned, with IDs; an empty
search is reported as empty, not as evidence of novelty. (5) If a search finds a paper that already makes the central
claim, say "VERIFIED COLLISION: <id>" as the first words of "preprint_collision"; the aggregate will cap novelty. Score
novelty on what you verified, not on what the proposal asserts.

=== OUTPUT SCHEMA (return ONLY JSON matching this) ===
{
 "type": "object",
 "properties": {
  "novelty": {
   "type": "integer",
   "description": "1-10"
  },
  "significance": {
   "type": "integer",
   "description": "1-10"
  },
  "soundness": {
   "type": "integer",
   "description": "1-10: would the proposed experiments actually test the claim?"
  },
  "feasibility": {
   "type": "integer",
   "description": "1-10: runnable on an academic budget as described"
  },
  "clarity": {
   "type": "integer",
   "description": "1-10"
  },
  "verdict": {
   "type": "string",
   "enum": [
    "accept-worthy",
    "borderline",
    "reject"
   ]
  },
  "one_line_contribution": {
   "type": "string",
   "description": "The new thing, in one sentence, in your own words. If you cannot state it, say so."
  },
  "closest_prior_work": {
   "type": "string",
   "description": "The work that most threatens novelty, and why it does or does not."
  },
  "strongest_objection": {
   "type": "string",
   "description": "The objection most likely to sink this in review."
  },
  "what_would_fix_it": {
   "type": "string"
  },
  "missing_baseline": {
   "type": "string",
   "description": "A baseline a reviewer would demand that the plan omits, or 'none'."
  },
  "preprint_collision": {
   "type": "string",
   "description": "Judge the proposal's Preprint Collision Check. Is there a recent arXiv preprint that already makes this claim? Name it if so. If the check is thin, vague, or reports no searches, say that \u2014 an unsearched claim of novelty is a weakness, not a neutral."
  }
 },
 "required": [
  "novelty",
  "significance",
  "soundness",
  "feasibility",
  "clarity",
  "verdict",
  "one_line_contribution",
  "closest_prior_work",
  "strongest_objection",
  "what_would_fix_it",
  "missing_baseline",
  "preprint_collision"
 ],
 "additionalProperties": false
}

=== USER ===
Proposal under review:

```json
{
 "Name": "coverage_limited_context_count_limited_weights",
 "Title": "Coverage-Limited Context, Count-Limited Weights: The Substrate Crossover Lives on the Experience-Collection Axis, Not the Deployment Horizon",
 "Short Hypothesis": "The in-context route's gain on ALFWorld is a same-type procedure copy that saturates once the bank holds a few items per task type (three per type, under twenty episodes, recovers >= 80 % of the full-bank gain), whereas the parametric route's memory-free retained fraction keeps rising with item count at matched optimizer steps (rho at 10 % of the pool <= 60 % of rho at 100 %); therefore which substrate is cheaper is decided by how many experiences have been collected, not by how many episodes will be deployed. A procedure absent from both bank and pool exposes the asymmetry: cross-type retrieval keeps under half of the same-type gain, while the student trained without that type keeps a type-general residual of at least a quarter of its in-pool gain.",
 "Related Work": "Measurement A in the brief established that the in-context gain is procedure-bound (unseen ~ seen, carried by the multi-step types) and flagged the near-duplicate-template concern, but used the full 1,465-item bank; no bank-size ladder exists. The substrate benchmark (2608.15008) finds regime-dependent trade-offs and calls for routing without naming the regime variable or testing a matched-cost ladder; UniMem (2607.26017) and COVE (2608.01234) route by recurrence or novelty without reporting what bank or pool size each substrate needs. Experience Distillation (2607.21051) claims sample efficiency for the weights route but has no context arm at the same sample counts; SKILL0 (2604.02268) and SIRI (2606.02355) internalize on fixed pools. Echo (2604.05533, In-Context Analogy Learning in Minecraft) is the nearest work on cross-type in-context transfer and has no weights arm or held-out procedure. Continual-memory work (2604.27003, 2606.02461) studies coverage over streams for non-parametric memory only (G24); 2512.02543's amortization treats collection as free. On the archived side, order_randomized_leakage_audit (5.7) observed that memory gains concentrate on tasks with a near-duplicate solved earlier, and query_agnostic_curation_ceiling (5.18) and coverage_currency_coupling (5.68) concern bank curation; none turns coverage into a scaling comparison across substrates. What none does: two ladders (bank size for context, pool size for weights at matched steps) on one backbone with a procedure-held-out boundary, and a cost frontier on the collection axis.",
 "Abstract": "Cost comparisons between in-context and parametric experience are framed on the deployment axis: how many episodes until training pays for itself. We argue the decisive axis is the collection axis: how many experiences you have. On ALFWorld with Qwen3-32B the in-context gain is a copy of a same-type procedure, so it should saturate once each task type is covered a few times; the parametric route learns from gradient signal over many items, so it should keep improving with count. We test both scaling curves from one partitioned expert pool: a bank-size ladder (1, 3, 10, 30 items per type and the full bank; type-stratified and type-blind; three subsample seeds) for retrieval at k=3, and a pool-size ladder (5, 10, 30, 100 % of the targets) for QLoRA at matched optimizer steps, each evaluated memory-free, with matched memory and with token-matched decoys. A procedure-held-out rotation across the three multi-step types (withheld from both bank and targets) separates the two mechanisms: cross-type retrieval of the nearest analogous procedure versus a student trained on the other types. We plot net gain against collected episodes plus training GPU-hours, locate the crossover pool size, and replicate on the own-rollout pool where collection has a measured cost per success. Pre-registered predictions: three items per type recover >= 80 % of the full-bank context gain; the student at 10 % of the pool retains <= 60 % of its full-pool retained fraction; on a held-out type cross-type retrieval keeps under half of the same-type gain while the student keeps at least a quarter of its in-pool gain. Either outcome of the second prediction has a cost consequence: if weights are coverage-limited too, the 2-GPU-hour full-pool training is ten times more than needed.",
 "Experiments": "E0 Partition stratified by type: targets T (55 %, ~806), bank B (30 %, ~440), evaluation-only train slice H (15 %, ~220). Gate 0: full-bank-B k=3 gain on valid >= 15 net points; per-type gains on clean/heat/cool >= 25 net points (Measurement A: +39 to +55). E1 Bank-size ladder (context): bank sizes {1, 3, 10, 30 per type, full B}, i.e. 6, 18, 60, 180 and ~440 items, type-stratified subsamples and type-blind uniform subsamples of the same totals, 3 subsample seeds each; base at k=3 (and k=1 for the two smallest banks) on valid + H, 2 evaluation seeds; decoy-3 at each size as the volume control. E2 Pool-size ladder (weights): QLoRA nf4 r32 SFT on {5, 10, 30, 100 %} of T (stratified), at matched optimizer steps (the full-pool one-epoch step count; smaller pools cycle more epochs) and, as an ablation, at one epoch; 2 LoRA seeds per size; evaluate at k=0 (absent), k=3 from B (matched) and decoy-3 (mismatched) on valid + H, 3 seeds; retained fraction rho(n) = student k=0 gain / base k=3 gain at Gate 0; CD at 100 % with its P-CD0 control as an optional check that the scaling is not SFT-specific. E3 Procedure-held-out rotation: for each of clean, heat, cool: remove the type from T and B; train SFT on T minus type (2 LoRA seeds, all of the remainder); evaluate on the withheld type in valid + H under base k=0, base k=3 same-type (reference, items from the withheld tasks in B), base k=3 cross-type (MiniLM nearest from B minus type), base k=3 best-analog (items from the hand-mapped sister type, e.g. heat for cool), student k=0, student k=3 cross-type; 3 seeds; step-level failure localization (search phase, appliance step, placement) for each condition. E4 Collection-cost frontier: x = collected episodes (expert walkthroughs counted as one episode each; own-rollout pool at measured k=0 GPU-seconds per success) plus training GPU-seconds; y = net gain; curves for context (k=3, bank of size n), weights (student on pool n, memory-free) and hybrid (student on pool n + k=3 from a 3-per-type bank); crossover n_c = smallest pool fraction where the memory-free student's gain reaches the 3-per-type context gain. E5 Own-rollout pool replication of E1-E2 when complete. Budget: E1 ~16,400 episodes; E2 16 GPU-hours training + ~11,900 episodes; E3 12 GPU-hours + ~4,000 episodes; training on one GPU while the other serves; about three days.",
 "Baselines and Ablations": "Context: type-stratified vs type-blind bank subsamples (coverage vs count within the context route); k=1 vs k=3 at small banks; decoy-3 at every bank size; retrieval by goal sentence (MiniLM) vs oracle same-type retrieval (upper bound on coverage). Weights: matched optimizer steps vs one epoch (is the small-pool deficit under-training or lack of items?); 2 LoRA seeds; CD with P-CD0 at 100 % as the objective check; direct SFT is the main weights arm. Held-out procedure: same-type reference, MiniLM cross-type, best-analog oracle, student trained without the type, student + cross-type items; failure localization by procedure phase. Frontier: cost with and without training GPU-hours; expert vs own-rollout collection cost. Finer-taxonomy ablation: coverage defined by type x object category x target receptacle, to test whether the saturation point moves when 'procedure' is defined more finely.",
 "Falsifiable Predictions": "P1 (context saturates at coverage): net gain with 3 stratified items per type >= 0.8 x gain with the full bank, and gain(full) - gain(18 items) <= 1/3 gain(full); falsified if the gain keeps rising from 18 to ~440 items by more than a third of the full gain. P2 (coverage, not count, within context): type-blind 6-item banks underperform stratified 6-item banks by at least the gain share of the types they miss and converge with stratified banks by 60 items; falsified if type-blind and stratified are indistinguishable at 6 items. P3 (weights are count-limited): at matched optimizer steps rho(10 %) <= 0.6 x rho(100 %); falsified if rho(10 %) >= 0.85 x rho(100 %), which would make weights coverage-limited too and the collection-axis crossover vanish (an informative null: full-pool training is ten times more than needed). P4 (held-out procedure asymmetry, pooled over the three rotations with a type random effect): cross-type retrieval gain <= 0.5 x same-type gain, and the student's residual gain >= 0.25 x its in-pool gain on that type with CI excluding 0; falsified if cross-type retrieval retains >= 0.5x (analogy works in context) or if the student's residual CI includes 0. P5 (crossover location): n_c > 30 % of the pool or does not exist at this retained fraction; falsified if n_c <= 10 %. P6 (placebo): decoy-3 gains are within the margin of k=0 at every bank size. All predictions are stated for the expert pool; on the own-rollout pool P1-P2 are expected to hold and P3 to hold with a smaller rho(100 %).",
 "Measurement and Noise Control": "Paired over identical (task, seed) across every bank size, pool size and probe; cluster bootstrap over tasks with seeds nested (2,000 resamples). Bank subsampling is a random factor: three subsample seeds per size, and the CI for each context cell includes subsample variance (reported separately from evaluation-seed variance). LoRA seed is a random factor with two levels per pool size. Noise floor: valid 274 x 2 seeds ~ +/-8 net points (measured); the weights ladder uses valid + H x 3 seeds (~+/-5); the bank ladder uses valid + H x 2 seeds x 3 subsamples (~+/-4 on the size-averaged contrast). Held-out-type contrasts pool three rotations (~80 tasks x 3 seeds x 3 types ~720 paired episodes, ~+/-8) with margins pre-registered as fractions of the per-type Gate-0 gains. Minimum detectable effects: 5 net points on the pool ladder, 4 on the bank ladder, 8 on the held-out contrasts, stated before the confirmatory run; P3's 0.6 vs 0.85 thresholds correspond to ~6-7 net points at an expected rho(100 %) of 0.5-0.7 x 27, so P3 is resolvable only if rho(100 %) >= 0.4 (Gate 1; otherwise P3 is declared untestable). Training curves (loss per step, examples seen) are logged so that matched-steps small-pool runs can be shown to have converged. Injected, total and cached tokens are logged for the frontier; training GPU-seconds measured per run. Thresholds, split seed, subsample seeds and the analog mapping are frozen in a pre-registration file before E1.",
 "Preprint Collision Check": "Literature command (S2 + HF, --recent, limit 8) for every query; WebSearch not used (quota exhausted); WebFetch never used. (1) 'experience pool size scaling agent memory retrieval saturates coverage versus fine-tuning data scaling' -> 2608.15008 (substrate benchmark), 2606.24775 and 2606.06448 (systems-level profiling of memory costs), 2605.12493 LongMemEval-V2, 2604.03295 (memory-enabled lifelong learning in multi-agent systems), 2602.19320 (anatomy of agentic memory: performance variability), 2602.03315 Memora; no bank-size ladder against a pool-size ladder. (2) 'held-out task type generalization ALFWorld fine-tuned agent versus retrieved demonstrations unseen procedure' -> only generic SFT/RL generalization papers (2501.17161 'SFT memorizes, RL generalizes', 2510.00237, 2501.01702 AgentRefine, 2502.18407 AgentRM); no per-procedure held-out comparison of substrates. (3) 'cross-task analogical transfer retrieved demonstration of a different task type embodied agent' -> 2604.05533 Echo (In-Context Analogy Learning for Minecraft agents; context route only, no held-out procedure or weights arm), 2511.20344 (analogical reasoning limits when transferring to new entities), 2507.06219 (task diversity beats quantity in robot-manipulation data, a count-vs-coverage result for weights in another field); nothing on the asymmetry claimed here. (4) 'context distillation agent interaction histories memory-free retained gain Experience Distillation' -> 2607.21051 (claims sample efficiency without a context arm at matched sample counts), 2608.07068, 2608.07169, 2609.02253 APEx (2026-09-02), 2607.29032; no scaling comparison. No preprint found that reports the two scaling curves on one backbone or the collection-axis crossover.",
 "Risk Factors and Limitations": "(1) ALFWorld has six task types, so type coverage is reached with a handful of items; the finer-taxonomy ablation tests whether the saturation point moves with a finer definition of 'procedure', and the claim is scoped to procedure-templated environments. (2) P3 may fail (weights also coverage-limited); the pre-registration treats this as an informative null with a stated cost consequence, but the headline then changes. (3) Cross-type retrieval may transfer well by analogy (Echo suggests it does in Minecraft); P4's falsification is then the finding and the asymmetry claim is dropped. (4) Matched optimizer steps on 5 % pools means ~20 epochs on ~40 tasks and can overfit; loss curves and the matched-memory evaluation detect this, and the one-epoch ablation bounds it. (5) Per-type held-out contrasts resolve only ~8 net points even pooled; smaller residuals are unresolved. (6) The own-rollout pool's collection cost depends on the k=0 success rate and the pool may be incomplete in time. (7) One backbone family; a Qwen3-8B check of P1 and P3 at two pool sizes is optional. (8) Bank subsampling interacts with MiniLM retrieval quality at tiny banks; the oracle same-type retrieval condition bounds this."
}
```

Research area this was proposed for:

# Title: The Same Experience Pool in Weights and in Context: What Transfers, What It Costs, and Where the Two Substrates Fail

Author: Fable 5.1, 2026-09-07. Stage-1 brief for the ideate2 pipeline, written after the Stage-0 pre-scan on this topic
(5 axes, 79 papers carded from S2 + HF, 26 gaps synthesized; see `digest.md`; no section-level reads this round, the
WebSearch quota was spent on the previous topic) and after Step 0, a measurement pass on this node that replaces the old
pilot's numbers with numbers from the backbone the experiments will actually use (`runs/STEP0_RESULTS.md`).

## Keywords
LLM agents, experience memory, in-context experience, parametric memory, context distillation, on-policy self-distillation,
privileged information, privilege illusion, LoRA, continual adaptation, amortization, cost-matched evaluation, ALFWorld

## TL;DR
An agent's past episodes can be reused two ways: retrieved into the prompt at inference, or trained into the weights. The
2026 literature has dozens of systems on each side and a growing family of hybrids, and the Stage-0 scan finds the same
hole under every axis: almost no paper builds both routes from the same experience pool on the same backbone and reports
them on one cost axis, almost none evaluates the trained student strictly without the memory it was trained with, and the
few memory-free margins that exist are 0.5–3 points without seeds. The program now has a measured starting position on
one node: with an expert pool, in-context retrieval on Qwen3-32B is worth +20 to +33 points on ALFWorld and does not turn
harmful up to k=7, and one epoch of QLoRA on the same pool costs about two GPU-hours. This track asks for the sharp,
falsifiable claim about what moves between the two substrates, at what cost, and where each one breaks.

## Starting position (measured here; not to be rediscovered)
**Measurement A, in-context retrieval on this node** (Qwen3-32B, thinking off, ReAct, expert bank of 1,465 replayed
walkthroughs, MiniLM retrieval on the goal sentence, paired over identical (game, seed), 274 games × 2 seeds per cell):

| split | k=0 | k=1 | k=3 | k=7 | net/100 at k=3 [95 % CI] |
|---|---|---|---|---|---|
| valid_seen | 0.536 | 0.739 | 0.807 | 0.846 | +27.1 [+18.6, +35.6] |
| valid_unseen | 0.549 | 0.776 | 0.869 | 0.877 | +32.1 [+22.9, +41.0] |

- The gain is procedure-bound, not scene-bound: unseen ≈ seen, and it is carried by the three multi-step types
  (clean/heat/cool then place: +39 to +55 net) whose procedure the k=0 agent fails to finish in 30 steps; most fixes
  convert timeouts. This is also the near-duplicate-template concern: same task type ⇒ near-identical procedure in the pool.
- No high-dose harm: k=7 ≥ k=3 ≥ k=1 on both splits, broken counts fall with k. The old pilot's one-sided harm (27B,
  self-built bank, "broke six or seven, fixed none") does not reproduce with an expert pool on this backbone.
- One type nets negative under retrieval: look-at-object-in-light (−4.8 net/100, n=62). It is the only natural harm regime
  on this node and it is small; any harm-side question needs a manufactured regime (see rules).
- Injected tokens: ~140 at k=1, ~430 at k=3, ~1,010 at k=7 per episode.

**Measurement B, parametric route cost** (QLoRA nf4 rank 32 on Qwen3-32B, step-level SFT on the same pool, 8,854 examples
of ~300 tokens): 385 tok/s at batch 4, 31.5 GB peak, 0.8 s per example, one epoch ≈ 2 GPU-hours on one A100; loss fits
the procedure within tens of steps. Serving a trained arm costs one vLLM restart (~3 min). Feasible; accuracy untested.

**In progress:** the agent's own k=0 successes on the 1,465 train tasks are being collected as a second, on-policy pool
(`runs/bank/own_rollouts_train.jsonl`). Every question below must be answerable on both pools, because the expert pool
is off-policy text and the literature's largest parametric gains come from self-generated data.

**Carried over from earlier rounds:** the 2026-08 pilot findings (memory can be one-sidedly harmful at high injection
volume; volume, not content, was the lever; noise of 0.05–0.14 on a headline metric swallowed most claims) and 51 archived
ideas (appendix). Three of the 51 already sit on this topic and were rejected or left borderline; their objections are
binding on the next round (appendix B).

## What the Stage-0 scan says, by axis
1. **Internalization objectives** (39 cards). The objective menu is now large and well studied on math: on-policy
   self-distillation from a privileged teacher (OPSD 2601.18734; π-Distill 2602.04942; OPCD 2602.12275), its repairs for
   multi-turn agents (HERO 2606.11559; SMRC-SD 2608.05219; Skill-SD 2604.10674; SGCD 2606.12634), skill and memory
   internalization on ALFWorld/WebShop (SKILL0 2604.02268; SIRI 2606.02355; PMD 2607.01480; Skill0.5 2605.28424; UCOB
   2606.29502), and context distillation of interaction histories (Experience Distillation 2607.21051: ≥64.8 % of the
   in-context gain retained memory-free, direct SFT 3.8 %). The gap named by every synth: none of them runs the
   keep-it-in-context arm at matched training compute and inference tokens, so "distilling beats RL/SFT" is established and
   "distilling beats context" is not. A multi-iteration study reports progressive collapse, not compounding (2606.04703).
2. **What survives internalization** (26 cards). Two literatures that do not talk to each other: the privilege-illusion
   family (DAPD 2608.01735; DOPD 2606.30626; OP²SD 2608.09228 shows OPSD gains come partly from context-induced teacher
   behaviour, not the reference) and the subliminal-transfer family (2507.14805; steering-vector account 2606.00995; LoRA
   artefact claim 2606.00831 vs natural-language transfer 2603.09517; corridor regularization 2609.01091; unsafe agent
   trajectories 2604.15559). Nobody has asked either question with retrieved agent memory as the privileged information, and
   nobody has run the paired condition "same material kept in context vs distilled" for harm, bias, or conflicting memory
   (compliance trap 2607.10608).
3. **Hybrids and routing** (26 cards). Routers exist (UniMem 2607.26017; COVE 2608.01234; Skill0.5; substrate benchmark
   2608.15008 concludes "no substrate dominates, routing is necessary") and memory-free deployment margins are reported
   (SESA 2607.29468: 1.8–2.2 memory-free, +0.5–1.0 with the bank back). The train-by-infer 2×2 (trained with/without memory
   × deployed with/without) is never reported with seeds; the information-abundance effect (abundant train-time context
   reduces what is encoded parametrically, 2608.12218) is shown only on documents and generic SFT, never on trajectories.
4. **Continual adaptation and shift** (27 cards). Erosion under self-evolution is documented across memory and model
   channels (2605.09315), stability–plasticity is re-framed as a retrieval problem (2604.27003), and benchmarks exist
   (AgentCL 2606.02461; OAKS 2603.07392; SWE-Bench-CL 2507.00014) but each evaluates only non-parametric memories; the
   parametric CL papers (FOREVER 2601.03938; Agent-Dice 2601.03641; self-generated replay 2605.26097) evaluate only weights.
   No paper puts both substrates on one stream with the same backbone and reports forgetting, transfer and recovery time.
5. **Evaluation and cost** (24 cards). Inference tokens of retrieval, reconstruction and guideline compilation are left out
   of accuracy comparisons (ReMe's 8B-with-memory > 14B-memoryless, 2512.10696; MemHarness 2607.28272); training compute of
   internalization is never amortized against memory-free inference; the one amortization analysis is for in-context
   distillation only (2512.02543: break-even after 843 episodes). Reported substrate differences are 1–5 points, usually
   single-seed.

## Rules for every proposal in this round (from 28 judge reviews of the previous round and the three archived objections)
- **Same pool, same backbone, one cost axis.** Every arm is built from one named experience pool (expert or self-rollout,
  both if possible) on Qwen3-32B and reported on a shared axis: training GPU-hours plus per-episode inference tokens, with
  a cumulative-cost curve or an explicit Pareto plot. "Weights beat context" without the context arm is not a finding.
- **Partition the pool.** No item that is an SFT/distillation target may also be a retrievable bank item at evaluation
  (bank pool ≠ target pool); otherwise own-bank vs swapped-bank contrasts measure memorization, not a read policy.
- **Self-distillation control (P-CD0).** Any context-distillation or on-policy arm needs the same objective run with an empty
  retrieval block, because self-training on ALFWorld train tasks is itself a large effect and generation format and
  on-policy-ness are confounded with the retrieved content.
- **Memory-free evaluation is mandatory** for every trained student, with three prompt conditions at test: memory absent,
  matched memory, mismatched memory (other task's items, token-matched). Report the privileged-vs-unprivileged gap.
- **Placebo arms for anything that injects less.** Token-matched and rate-matched decoys (relevance-destroyed, same length)
  at training time and at inference, since volume was the causal lever in the pilot.
- **Power gates tied to the measured effect.** Equivalence margins are pre-registered as a fraction of the effect measured at
  Gate 0, never a fixed 3 points; on this node a paired cell of 274 games × 2 seeds gives about ±8 net points at 95 %, so
  claims below ~6 points need more seeds, the held-out train split, or a manufactured regime. State the minimum detectable
  effect before the confirmatory run; if Gate 0 fails, the claim is declared untestable, not "confirmed by TOST".
- **Positive control for any dispositional claim.** A teacher context known to induce a disposition (e.g. a majority-action
  prior) must be shown to transfer under the same distillation before "X does not transfer" is asserted.
- **No prediction entailed by a definition.** An append-only bank cannot forget; a LoRA trained only on post-shift data
  cannot keep a renamed mapping. Stream designs need a bounded evicting bank, a reset-LoRA arm, and an off-stream capability
  probe that the shift did not relabel.
- **Procedure-held-out split.** Because the in-context gain is procedure-bound, at least one evaluation holds out an entire
  task type from both the bank and the training targets; scene-level "unseen" is not enough.
- **Public data, local models, days not weeks;** pre-registration of thresholds and amendments before the first
  confirmatory run; the noise floor of the setup (paired CI above) is part of the proposal.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Retained fraction and its cost.** For one pool, build (a) retrieval at k∈{1,3,7}, (b) QLoRA on the pool, (c) context
  distillation from the k=3-conditioned teacher, (d) P-CD0, and evaluate every trained arm memory-free and with memory back.
  What fraction of the +27/+32 in-context gain survives in weights, how does it scale with pool size (10 %, 30 %, 100 % of
  1,465 tasks) and with the procedure-held-out split, and where on the cumulative-cost curve do weights become cheaper
  than ~430 tokens per episode? Must go past `harm_does_not_distill` (asymmetric-filter framing, underpowered) and
  `amortization_horizon_ranking_flip` (8B-vs-14B, different backbones): same backbone, retained fraction as the estimand.
- **Q2 Which objective transfers what, and is the retrieved memory a privilege illusion?** With retrieved episodes as the
  privileged information, compare SFT on trajectories, off-policy context distillation, and on-policy self-distillation
  (reverse-KL to the memory-conditioned teacher) on the same pool; decompose the gain into reference-attributable and
  context-induced parts (OP²SD-style shuffled-memory teacher), and test whether the student's memory-free accuracy tracks
  the teacher's memory-conditioned accuracy or its memory-free one. Prediction must be stated per objective and per task type.
- **Q3 Training-time context dose and context reliance.** Vary k in the prompt during SFT/distillation (0, 1, 3, 7, decoy);
  evaluate with context present, absent, and misleading. Does abundant train-time experience reduce what is encoded
  (2608.12218's information-abundance effect) on agent trajectories, is the optimum intermediate, and does the effect
  reverse on the self-rollout pool? Must differ from `memory_in_the_loop_training_decomposition` by the dose ladder, the
  pool partition, and a training-time decoy arm (its named missing baseline).
- **Q4 Harm and dispositions across substrates.** Only in a manufactured high-harm regime (Gate 0: in-context harm ≥ 6 net
  points, e.g. planted wrong-procedure items or the compliance-trap construction) with a positive control: does the same
  harmful material harm more when distilled than when read, does the entry-propagation-recovery signature change form, and
  does the corridor-regularization defence (2609.01091) have an in-context analogue? Also the subliminal question the field
  left open: do agent-trajectory traits transfer under on-policy distillation, or only under SFT/LoRA?
- **Q5 Same stream, both substrates, symmetric design.** A stream with a mid-stream rule change; arms: bounded evicting bank,
  unbounded bank, continual LoRA, reset LoRA, LoRA with self-generated replay; a randomized dose ladder of pre-shift items in
  the retrieved set at fixed k and tokens; off-stream capability probe. The honest hypothesis is "both erode, at different
  rates and with different recovery times"; `opposite_sided_failure_under_shift` was rejected for asserting the definitional
  version.
- **Q6 The memory-free margin and the 2×2.** Trained with/without memory × deployed with/without memory, on both pools, with
  seeds and per-step tokens: is the in-context channel still additive after internalization (SESA's +0.5–1.0), is it
  substitutive, or does training with memory make the memory-free policy worse (the crutch)? Small margins are expected,
  so the proposal must show the design can resolve 2 points.

## In scope
- ALFWorld (primary; 1,465 train tasks, 274 validation games, expert and self-rollout pools already on disk); WebShop or a
  text-game second environment if the claim needs a second domain; public data only.
- Qwen3-32B as agent, teacher and student (QLoRA rank 32 fits one A100); other local models only as a robustness check.
- Reimplementation of one published objective per family (OPSD/OPCD, Experience Distillation, SIRI-style skill
  internalization) as named baselines; null results when the measurement makes the null informative.

## Out of scope
- Frontier-model training; anything with private or clinical data.
- "We routed between memory and weights and the number went up" without the single-substrate arms at matched cost.
- Effects the setup cannot resolve (below the paired CI without a stated plan to shrink it).
- Restating any of the 51 archived ideas (appendix); a proposal near one of them must name the archived idea and state what
  it fixes.

## Resource constraints
Two A100 80GB on one node (not four); vLLM serves one Qwen3-32B replica per GPU; both GPUs must stay busy (a training arm
runs on one GPU while the other serves). Budget per confirmatory cell: 274 games × 2–3 seeds ≈ 550–820 episodes;
one QLoRA epoch on the full pool ≈ 2 GPU-hours (0.2–0.6 h for 10–30 % pools); one distillation arm additionally needs one
teacher pass over the target pool (~1,465 episodes with memory). A full Q1 on one pool is roughly 6 trained arms plus 4
retrieval cells, i.e. two to three days; plan seeds and gates accordingly.

## Appendix A: the 51 ideas already generated in this program (do not restate; differentiate or move on)
Round 1 (27, 3-judge Opus mean, `reviews/ideation/RANKING.md`): memory_item_value_reliability 6.12,
provenance_gap_selection_not_authorship 6.07, compile_dont_retrieve 6.0, memory_or_instruction 5.92,
failure_signature_routing 5.87, collection_policy_coupling_collapse 5.85, instruction_conditioned_complementarity 5.82,
coadaptation_transplant_ccr 5.77, decorative_retriever 5.75, memory_induced_shortcutting 5.72,
memory_vetoes_instruction_slot 5.72, coverage_currency_coupling 5.68, memory_budget_confound 5.63,
substitutes_not_complements 5.47, counterfactual_memory_screening_under_selection_noise 5.45,
memory_dropout_coadaptation 5.45, coverage_selection_division_of_labour 5.4, clause_level_portability 5.38,
commit_then_consult_slot_discipline 5.38, breadth_routed_memory 5.35, playbook_transfer 5.33,
meta_prompt_generalization 5.3, action_prior_imprinting 5.27, optimizer_substitutes_for_memory_scaffold 5.22,
query_agnostic_curation_ceiling 5.18, memory_volume_amplifies_optimizer_curse 5.05, allocation_prior_transfer 5.0.

Round 2 (24, open-book Opus, `runs_ideate2/gen_v2/review/RANKING.md`):
- abstraction_discards_bindings_and_repairs 5.95: scene bindings and failure-to-repair pairs explain when distilled experience beats raw trajectories
- closer_beats_stronger 5.75: consumer-side policy proximity, not builder capability, predicts cross-backbone transfer of shared experience
- model_shaped_instruction_task_shaped_store 5.75: the memory–instruction substitution does not survive a backbone swap
- failure_memory_framing_drag 5.72: cross-episode failure notes induce contextual drag; positive rewriting removes it
- order_randomized_leakage_audit 5.7: memory gains concentrate on tasks with a near-duplicate solved earlier in the stream
- memory_in_the_loop_training_decomposition 5.65: train-by-infer 2×2 with bank swap (crutch / content / read skill)
- optimizer_writes_the_read_policy 5.6: joint instruction–memory gains are carried by evolved clauses governing memory use
- gate_reads_style_not_truth 5.55: planted-record audit of write-time validation
- dormant_is_not_dead 5.45; need_blind_compaction_audit 5.45; stall_triggered_injection 5.45
- amortization_horizon_ranking_flip 5.35: cost definition and horizon decide whether 8B+memory beats 14B
- harm_does_not_distill 5.35: context distillation as an asymmetric filter on agent experience
- stale_true_state_facts_redaction 5.3; state_load_not_length 5.2; memory_surrogate_validity 5.15
- opposite_sided_failure_under_shift 5.05: in-context and parametric experience fail on opposite sides of a shift
- utility_pruning_is_frequency_pruning 4.9; contributor_conflict_not_size 4.85; wrong_action_fraction_dose 4.85;
  cross_episode_drag_content_not_label 4.8; lineage_blast_radius 4.75; coupling_variance_components 4.65;
  retrieved_set_disagreement_gate 4.65

## Appendix B: why the three parametric-axis ideas did not pass (binding objections)
- **harm_does_not_distill.** The equivalence margin (3 points) exceeded the harm being probed (~1.3 points on the held-out
  set), so "harm does not distill" and "harm distills but is invisible" were not separated; the second half of the claim was a
  failure-to-reject read as a null. Missing baseline: P-CD0 (context distillation from an empty-retrieval teacher), without
  which the retained-value fraction is confounded with generation format and on-policy-ness. Closest work: Experience
  Distillation 2607.21051 for the retained-gain half; DAPD 2608.01735 / DOPD 2606.30626 / 2608.05219 for the mechanism half.
- **memory_in_the_loop_training_decomposition.** Bank A items were also SFT targets, so the own-bank vs swapped-bank drop
  measured memorization and the co-adaptation claim was pre-determined. Missing baseline: a training-time relevance-destroyed
  decoy block of matched length, without which "crutch" is confounded with "long irrelevant prefix hurts SFT"; the GRPO arm
  had to be a named published objective (MemHarness reconstruction reward or UCOB). Closest work: UCOB 2606.29502 (credit-aware
  bidirectional self-distillation between skill-conditioned and no-skill prompts, ALFWorld/WebShop) and SESA 2607.29468.
- **opposite_sided_failure_under_shift.** The headline was definitional (an append-only bank cannot forget; a LoRA trained
  only on post-shift data cannot retain a renamed mapping); the stale-fraction regression was observational and collinear with
  probe index and bank size; no probe of a capability the shift did not relabel. Fix demanded: randomized dose ladder of
  pre-shift items at fixed k and tokens, bounded evicting bank, reset-LoRA arm, off-stream probe. Closest work: UniMem
  2607.26017 (contents unverified on either channel) and Do Self-Evolving Agents Forget 2605.09315.


Review it now.

=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: coverage_limited_context_count_limited_weights — Coverage-Limited Context, Count-Limited Weights: The Substrate Crossover Lives on the Experience-Collection Axis, Not the Deployment Horizon

- arxiv:2606.17016 · 2026-06-15 · preprint · sim 0.55 · hf
  TokenPilot: Cache-Efficient Context Management for LLM Agents
  As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, 
- arxiv:2608.22695 · 2026-08-24 · preprint · sim 0.49 · hf
  Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing
  Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable pr
- arxiv:2602.11748 · 2026-02-12 · preprint · sim 0.45 · hf
  Think Longer to Explore Deeper: Learn to Explore In-Context via Length-Incentivized Reinforcement Learning
  Achieving effective test-time scaling requires models to engage in In-Context Exploration -- the intrinsic ability to generate, verify, and refine multiple reasoning hypotheses within a single continuous context. Grounded in State Coverage theory, our analysis identifies a critical bottleneck to enabling this capability: while broader state coverage requires longer reasoning trajectories, the probability of sampling such sequences decays exponentially during autoregressive generation, a phenomen
- arxiv:2407.21787 · 2024-07-31 · preprint · sim 0.43 · hf
  Large Language Monkeys: Scaling Inference Compute with Repeated Sampling
  Scaling the amount of compute used to train language models has dramatically improved their capabilities. However, when it comes to inference, we often limit the amount of compute to only one attempt per problem. Here, we explore inference compute as another axis for scaling by increasing the number of generated samples. Across multiple tasks and models, we observe that coverage - the fraction of problems solved by any attempt - scales with the number of samples over four orders of magnitude. In
- arxiv:2606.05633 · 2026-06-04 · preprint · sim 0.43 · hf
  Answer Presence Drives RAG Rewriting Gains
  Retrieval-augmented QA pipelines often route retrieved passages through an LLM rewriter before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compi
- arxiv:2605.25997 · 2026-05-25 · preprint · sim 0.42 · hf
  Deployment-complete benchmarking
  Benchmarks increasingly guide deployment, procurement and scientific screening, yet a score supports only the response it records, not necessarily the deployment action. We introduce deployment-complete benchmarking, which tests whether benchmark evidence determines a deployment action. A benchmark is complete for a claim exactly when the action is constant on each evidence fiber; mixed fibers expose missing deployment information, and completion curves quantify the evidence required to resolve 
- arxiv:2606.25852 · 2026-06-24 · preprint · sim 0.42 · hf
  Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
  Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress insi
- arxiv:2609.02217 · 2026-09-02 · preprint · sim 0.42 · hf
  SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams
  LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of 
- arxiv:2410.16848 · 2024-10-22 · preprint · sim 0.40 · hf
  ETHIC: Evaluating Large Language Models on Long-Context Tasks with High
  Information Coverage
  Recent advancements in large language models (LLM) capable of processing extremely long texts highlight the need for a dedicated evaluation benchmark to assess their long-context capabilities. However, existing methods, like the needle-in-a-haystack test, do not effectively assess whether these models fully utilize contextual information, raising concerns about the reliability of current evaluation techniques. To thoroughly examine the effectiveness of existing benchmarks, we introduce a new met
- arxiv:2505.23522 · 2025-05-29 · preprint · sim 0.39 · hf
  OmniEarth-Bench: Towards Holistic Evaluation of Earth's Six Spheres and
  Cross-Spheres Interactions with Multimodal Observational Earth Data
  Existing benchmarks for Earth science multimodal learning exhibit critical limitations in systematic coverage of geosystem components and cross-sphere interactions, often constrained to isolated subsystems (only in Human-activities sphere or atmosphere) with limited evaluation dimensions (less than 16 tasks). To address these gaps, we introduce OmniEarth-Bench, the first comprehensive multimodal benchmark spanning all six Earth science spheres (atmosphere, lithosphere, Oceansphere, cryosphere, b

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

