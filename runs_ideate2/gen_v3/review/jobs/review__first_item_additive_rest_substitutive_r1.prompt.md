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
 "Name": "first_item_additive_rest_substitutive",
 "Title": "Additive at One Item, Substitutive at Seven: The Dose-Response of Retrieved Experience After Memory-Free Internalization",
 "Short Hypothesis": "After memory-free internalization of an experience pool (QLoRA SFT or context distillation on Qwen3-32B), retrieved experience keeps its first-item value but loses its marginal value beyond one item: the student's k=0->k=1 gain stays at least half of the base model's, while its k=1->k=7 slope falls to at most one third of the base's, because the student has internalized the procedures and needs only a cue to select one. Consequently the token-optimal deployment is student+k=1 at ~15 % of base+k=7's injected tokens, and memory-free training does not damage the read skill: on a task type withheld from the training targets but present in the bank, the student's dose-response equals the base's.",
 "Related Work": "SESA (2607.29468) is the closest result: skill-memory benefits partly enter the parameters (1.8-2.2 memory-free) and the bank retains +0.5-1.0 as optional inference-time memory -- one dose, QA/search, no seeds, no token cost. Retrieval-augmented SFT (2603.18272) trains the agent to use retrieved trajectories and does not test whether retrieval is still needed afterwards. Experience Distillation (2607.21051), PMD (2607.01480), SKILL0 (2604.02268) and Skill0.5 (2605.28424) evaluate memory-free or with a fixed context and never trace the dose after internalization. The information-abundance paradox (2608.12218) predicts that abundant training-time context increases context reliance, on documents; New News (2505.01812) reports contextual shadowing for knowledge; neither has a post-training dose ladder on trajectories. UCOB (2606.29502) picks the higher-return context view as a local teacher but does not report the memory-free student. The substrate benchmark (2608.15008) concludes that no substrate dominates, without a dose axis. The archived memory_in_the_loop_training_decomposition (5.65) proposed the train-by-infer 2x2 with a bank swap but had bank items as SFT targets and no training-time decoy; the archived substitutes_not_complements (5.47) asked the additive-vs-substitutive question for memory vs instructions, not for weights vs context. None reports the shape of the dose-response after internalization, the token-optimal hybrid point, or a crutch test on a type the student never saw.",
 "Abstract": "Internalization papers report the memory-free accuracy of a student and, at most, one number for 'with the memory back'. That single number cannot distinguish three regimes that have different cost implications: the retrieved channel stays additive (deploy with the full k), it becomes substitutive (deploy memory-free), or training has made the policy dependent on it (the crutch). We measure the full dose-response after internalization on ALFWorld with Qwen3-32B: a base ladder k in {0,1,3,7} plus token-matched decoys from a bank disjoint from the training targets, then the same ladder for students trained memory-free by SFT, by context distillation from the k=3 teacher, and by the P-CD0 control, on the expert pool and on the own-rollout pool, with a type withheld from the targets but kept in the bank as a crutch probe and a type withheld from both as the procedure-held-out probe. The pre-registered claim is a specific shape -- first-item gain preserved, slope beyond it collapsed -- which implies that student+k=1 (~140 injected tokens) matches base+k=7 (~1,010 tokens) and that the hybrid, not the memory-free student, sits on the token-accuracy frontier. A secondary memory-in-the-loop arm with a decoy-trained twin tests whether training with memory in the prompt steepens the slope (reliance) on trajectory data. Every contrast is paired over (task, seed) with three evaluation seeds and two LoRA seeds; the design resolves a slope difference of about 5 net points.",
 "Experiments": "E0 Partition (stratified by type): targets T (55 %, ~806), bank B (30 %, ~440), evaluation-only train slice H (15 %, ~220). Gate 0: base ladder on bank B, valid 274 x 2 seeds; require k=1->k=7 slope >= 6 net points and k=0->k=1 gain >= 10 net points (Measurement A with the full bank: ~+10 and ~+20). E1 Base ladder: k in {0,1,3,7}, decoy-3, decoy-7 (same length, relevance destroyed by cross-type items with swapped object names), on valid + H, 3 seeds. E2 Main students on full T (QLoRA nf4 r32, one epoch, 2 LoRA seeds): SFT-E on expert step targets; CD-E = Experience Distillation from the base at k=3 with bank B (teacher pass over T, memory block removed from the student prompt); P-CD0-E (teacher at k=0, same recipe); evaluated at k=0, 1, 3, 7 and decoy-3 (absent / matched / mismatched) on valid + H, 3 seeds. E3 Own-rollout pool: SFT-O and CD-O when the pool is complete, same ladder. E4 Probe students: SFT-E trained on T minus pick_heat_then_place and minus pick_cool_then_place (2 LoRA seeds). Crutch probe: on the heat type (kept in B; valid + H, ~80 tasks x 3 seeds) compare the probe student's and base's dose-response at k=0, 1, 3. Procedure-held-out probe: on the cool type with B minus cool (cross-type retrieval only), base and probe student at k=0 and k=3. E5 Iso-token cell: student+k=1 vs base+k=7 with a fourth seed. E6 Secondary memory-in-the-loop: SFT-E trained with k=3 items from B in the prompt, and its twin trained with decoy-3 in the prompt, 1 LoRA seed each, same ladder at test. Costs logged per episode (injected tokens, total tokens, steps). Budget: ~8,900 base episodes; core students 4 (SFT-E, CD-E x 2 seeds) x 5 conditions x 3 seeds x 494 tasks ~29,600; P-CD0 at k=0/1 ~5,900; probes ~1,500; memory-in-loop 2 x 4 x 3 x 494 ~11,900; ~20 GPU-hours of QLoRA plus ~2,000 teacher-pass episodes; training on one GPU while the other serves; about three days for the core, four with E3 and E6.",
 "Baselines and Ablations": "Base ladder with the matched bank B (the base is never scored with the full 1,465 bank, so both substrates see the same items); decoy-3/decoy-7 placebos at inference for base and students (volume control); direct SFT vs context distillation vs P-CD0 (objective ablation: is the shape objective-specific?); expert vs own-rollout pool; full-T students vs probe students trained without two types; memory-in-the-loop arm with a decoy-trained twin (the training-time placebo the brief requires) as the secondary axis; retrieval order shuffled at k=7 to check that a flat slope is not a position effect; a one-seed Qwen3-8B replication of the shape.",
 "Falsifiable Predictions": "P1 (first item preserved): for SFT-E and CD-E, (student k=1 - student k=0) >= 0.5 x (base k=1 - base k=0); falsified if <= 0.25x for both objectives. P2 (slope collapse): (student k=7 - student k=1) <= 1/3 x (base k=7 - base k=1); falsified if >= 2/3x, which would mean the channel is fully additive after internalization. P3 (token-optimal point): student+k=1 is at least as accurate as base+k=7 minus the pre-registered margin (one half of the Gate-0 slope, about 5 net points) with 4 seeds; falsified if base+k=7 exceeds student+k=1 by more than the margin. P4 (no crutch): on the heat type withheld from T but kept in B, the probe student's k=3 gain is not below the base's k=3 gain on that type by more than one third of the base's gain; falsified otherwise (powered only for a crutch >= 15 net points on the ~40-55-point in-context gain of that type). P5 (procedure-held-out): on the cool type withheld from both, base and probe-student dose-responses are both flat within the per-type CI and the student's k=0 is within the CI of base k=0; falsified if either substrate carries a gain there, which would also refute the procedure-bound account in the brief. P6 (volume placebo): student + decoy-3 is within the margin of student k=0; falsified if decoy items raise the student's accuracy, in which case P1's first-item effect is a length effect. P7 (secondary, the 2608.12218 direction): the memory-in-the-loop student has lower memory-free accuracy than SFT-E and a k=1->k=7 slope >= 2/3 of the base's; the decoy-trained twin must not show the same drop, otherwise the drop is a long-prefix SFT artefact. Objective-specific expectation: CD-E has a higher k=0 than SFT-E but the same shape; P-CD0-E shows the shape only if self-training alone internalizes the procedures.",
 "Measurement and Noise Control": "All arms run on identical (task, seed) pairs, so the dose-response is a within-task design: for every task and seed we record success at each k, and the slope contrasts (k=1 - k=0, k=7 - k=1) are paired differences whose difference between base and student is tested with a cluster bootstrap over tasks (2,000 resamples, seeds nested). Noise floor: 274 x 2 seeds ~ +/-8 net points (measured); 494 tasks (valid + H) x 3 seeds ~ +/-5 net points; the iso-token cell uses 4 seeds (~+/-4). Minimum detectable slope difference ~5 net points, stated before the confirmatory run; Gate 0 requires the base slope k=1->k=7 to be >= 6 net points with bank B, otherwise P2 is declared untestable at this bank and the study reports only P1 and P3. Per-type probes (heat, cool) have ~80 tasks x 3 seeds and about +/-12 net points; their margins are pre-registered as one third of the base's per-type gain measured at Gate 0. Two LoRA seeds per objective; LoRA-seed SD reported as a variance component, and a third seed added if it exceeds 3 net points. Decoys are drawn with a fixed random seed and token-matched within 5 % of the real items. Injected, total and cached tokens per episode are logged for the frontier plot. Thresholds, split seed and margins are frozen in a pre-registration file before E2.",
 "Preprint Collision Check": "Literature command (S2 + HF, --recent, limit 8) for all queries; WebSearch not used (quota exhausted); WebFetch never used. (1) 'retrieval-augmented agent after fine-tuning memory still additive memory-free deployment skill bank re-added inference' -> 2603.18272 (retrieval-augmented SFT with LoRA; no memory-free test after training), 2604.27003, AdaMEM 2606.05684, Auto-Dreamer 2605.20616, MRAgent 2606.06036, Mem-pi 2605.21463, MINTEval 2605.18565, 2604.24594; none traces the retrieval dose after internalization. (2) 'number of in-context examples dose after fine-tuning context reliance substitution weights versus context' -> 2608.12218 (information-abundance paradox, documents and generic SFT), 2505.01812 New News (contextual shadowing for knowledge), 2605.09665 (data selection); no post-training dose ladder on agent trajectories. (3) 'context distillation agent interaction histories memory-free retained gain Experience Distillation' -> 2607.21051, 2608.07068 MemOPD, 2608.07169 Agent Memory Distillation (memory handed to a small model without training), 2609.02253 APEx (2026-09-02, hierarchical procedural-experience memory for deep-research QA; a memory system, no weights arm), 2607.29032 TransMem; none evaluates a trained student across k. (4) 'seed variance LoRA fine-tuning agent benchmark noise floor run-to-run variability' -> 2602.09492 (batch-size bias in LoRA evaluation; motivates fixed hyperparameters across arms), 2602.00084, 2509.12229; nothing on agent-benchmark seed floors. No preprint found claiming the additive-then-substitutive shape or the student+k=1 iso-token result.",
 "Risk Factors and Limitations": "(1) The shape may be objective-specific (SFT flat from k=0, CD additive at k=1); the per-objective predictions make this an outcome rather than a failure, but the headline then needs qualification. (2) Bank B is 30 % of the pool; Gate 0 protects against a base slope too small to resolve, at the price of a possibly untestable P2. (3) Per-type probes are underpowered below ~15 net points; smaller crutches remain unresolved and are reported as such. (4) The own-rollout pool may be incomplete; the expert-pool result is primary. (5) Retrieval by MiniLM on the goal sentence returns same-type items when available, so a flat slope could reflect item redundancy (near-duplicate templates) rather than internalization; the base ladder at the same bank is the control, since redundancy would flatten the base too, and the k=7 order-shuffle ablation checks position effects. (6) ALFWorld's six task types limit how far 'cue' generalizes; a WebShop replication is optional. (7) One backbone family; the 8B check is single-seed."
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

Proposal: first_item_additive_rest_substitutive — Additive at One Item, Substitutive at Seven: The Dose-Response of Retrieved Experience After Memory-Free Internalization

- arxiv:2606.05633 · 2026-06-04 · preprint · sim 0.58 · hf
  Answer Presence Drives RAG Rewriting Gains
  Retrieval-augmented QA pipelines often route retrieved passages through an LLM rewriter before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compi
- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.51 · hf
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2608.03796 · 2026-08-04 · preprint · sim 0.47 · hf
  Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss
  Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-K l
- arxiv:2209.15189 · 2022-09-30 · preprint · sim 0.46 · hf
  Learning by Distilling Context
  Language models significantly benefit from context tokens, such as prompts or scratchpads. They perform better when prompted with informative instructions, and they acquire new reasoning capabilities by generating a scratch-pad before predicting the final answers. However, they do not internalize these performance gains, which disappear when the context tokens are gone. Our work proposes to apply context distillation so that a language model can improve itself by internalizing these gains. Concr
- arxiv:2512.10696 · 2025-12-11 · preprint · sim 0.45 · hf
  Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
  Procedural memory enables large language model (LLM) agents to internalize "how-to" knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a "passive accumulation" paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose ReMe (Remember Me, Refine Me), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle vi
- arxiv:2606.04703 · 2026-06-03 · preprint · sim 0.44 · hf
  Rethinking Continual Experience Internalization for Self-Evolving LLM Agents
  Experience internalization converts contextual experience from past interactions into reusable parametric capability, offering a promising path toward continual learning in large language models (LLMs). While prior work has predominantly focused on single-iteration transfer, we discover that under multi-iteration experience learning, existing methods suffer from a progressive capability collapse rather than compounding improvement. We systematically examine this failure through three vital dimen
- arxiv:2505.24850 · 2025-05-30 · preprint · sim 0.43 · hf
  Harnessing Negative Signals: Reinforcement Distillation from Teacher
  Data for LLM Reasoning
  Recent advances in model distillation demonstrate that data from advanced reasoning models (e.g., DeepSeek-R1, OpenAI's o1) can effectively transfer complex reasoning abilities to smaller, efficient student models. However, standard practices employ rejection sampling, discarding incorrect reasoning examples -- valuable, yet often underutilized data. This paper addresses the critical question: How can both positive and negative distilled reasoning traces be effectively leveraged to maximize LLM 
- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.43 · hf
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2607.25659 · 2026-07-28 · preprint · sim 0.41 · hf
  CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization
  Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria. Yet in GRPO-style pipelines, these structured judgments are reduced to a scalar response-level reward and converted into a response-level advantage, which is broadcast uniformly to all generated tokens. This leaves no explicit mechanism for allocating credit within a response, even when different criteria are grounded in different spans, formatting decisions, or semantic ch
- arxiv:2207.05080 · 2022-07-11 · preprint · sim 0.39 · hf
  Learning an evolved mixture model for task-free continual learning
  Recently, continual learning (CL) has gained significant interest because it enables deep learning models to acquire new knowledge without forgetting previously learnt information. However, most existing works require knowing the task identities and boundaries, which is not realistic in a real context. In this paper, we address a more challenging and realistic setting in CL, namely the Task-Free Continual Learning (TFCL) in which a model is trained on non-stationary data streams with no explicit

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

