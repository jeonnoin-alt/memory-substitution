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
 "Name": "student_side_abundance",
 "Title": "Information Abundance Is a Student-Side Effect: Training-Time Memory Dose Suppresses Parametric Encoding of Agent Experience Only When the Memory Sits in the Student's Own Prompt",
 "Short Hypothesis": "Putting k retrieved episodes in the student's prompt during step-level SFT lowers the action-token loss the student has to close, and the memory-free accuracy of the resulting agent falls with the loss that memory removes at training time (the information-abundance effect of 2608.12218 on trajectories); token-matched relevance-destroyed decoys at the same k do not produce the drop. The same dose given to the teacher instead of the student (on-policy reverse-KL from a k-conditioned self-teacher, student prompt empty) yields memory-free accuracy that is non-decreasing in k. The optimum train-time dose is therefore intermediate (k~1) for memory-in-prompt SFT and maximal for teacher-side distillation, and the SFT dose effect shrinks on the self-rollout pool where the k=0 loss is already low.",
 "Related Work": "The Information Abundance Paradox (arXiv:2608.12218) shows on documents and generic SFT that longer training contexts reduce parametric encoding and increase context reliance up to an intermediate optimum; it does not test agent trajectories, memory-conditioned distillation, decoy contexts or a teacher-side dose. Retrieval-augmented agent training (2603.18272) trains the agent to use retrieved trajectories in context with LoRA and reports generalisation, but never evaluates without retrieval and never varies the dose. 'Training Prompt Matters' (2606.01967) shows training prompts change learning dynamics and proposes prompt adaptation, without memory or agents. Experience Distillation (2607.21051) and OPCD (2602.12275) distil a context-conditioned teacher into an empty-prompt student at one fixed dose. The archived idea memory_in_the_loop_training_decomposition ran a 2x2 with a bank swap and was rejected for bank/target overlap and for lacking a training-time decoy; this design starts from those two fixes. Measurement B on this node gives the cost and loss behaviour of QLoRA on the expert pool at k=0 but no accuracy.",
 "Abstract": "Should an agent be fine-tuned with its retrieved experience in the prompt, so that training matches deployment, or without it, so that the experience is forced into the weights? The information-abundance paradox predicts the former suppresses parametric encoding, but the evidence is from documents and generic SFT. We test it on ALFWorld trajectories with Qwen3-32B and one partitioned experience pool. Student-side ladder: step-level QLoRA on target-pool walkthroughs with k in {0, 1, 3, 7} bank items in the prompt, plus token-matched relevance-destroyed decoys at k=3 and k=7 and a rate-matched arm (k=3 on half the examples). Teacher-side ladder: on-policy reverse-KL from a self-teacher conditioned on k in {1, 3, 7} or a k=7 decoy, with the student prompt empty (P-CD0 at k=0). Every student is evaluated with memory absent, matched (k=3 from the bank) and mismatched (token-matched other-type items). The mechanism is measured directly: for every training example we record the action-token NLL reduction that the memory affords before training (delta-NLL), per task type and dose. Predictions: memory-free accuracy decreases with k on the student-side ladder and is unchanged by decoys; reliance (matched minus absent) and mismatched-memory harm increase with k; the teacher-side ladder is non-decreasing so the two curves cross; per-type deficits scale with delta-NLL; on the self-rollout pool delta-NLL and the deficit both shrink. All arms are reported with training GPU-hours and per-episode tokens against the k=3 in-context arm, so the result decides whether internalisation at deployment-matched dose can beat context at all.",
 "Experiments": "(1) Partition: 1,465 expert walkthroughs split by task into bank B (40 %) and targets T (60 %), stratified by type and floorplan; 200 target tasks held out as evaluation set H; second partition with one multi-step type (heat-then-place) removed from B and T. (2) Student-side ladder (QLoRA nf4 rank 32, one epoch, step-level targets on T as in Measurement B, prompt = ReAct history plus a memory block): k_train in {0, 1, 3, 7} with items retrieved from B by goal similarity (~140/430/1,010 block tokens); DEC-3 and DEC-7 with other-type items token-matched to the same lengths; RATE-3 with k=3 on a random 50 % of examples. Seven arms; two training seeds for k=1 and k=7. (3) Teacher-side ladder: on-policy reverse-KL on student rollouts over T (student prompt has no block; teacher = same base weights with k_t in {1, 3, 7} matched items or DEC-7), plus P-CD0 (k_t = 0). Four arms, one epoch each. (4) Mechanism measure: before training, base-model action-token NLL on every target example with and without its k block; delta-NLL(k) per example, aggregated per type; the same for decoys (expected ~0). (5) Self-rollout pool: repeat the student-side ladder at k in {0, 3, 7} with own k=0 successes as targets and the expert bank B as memory. (6) Evaluation of all students on valid_seen, valid_unseen and H, test blocks absent / matched k=3 from B / mismatched token-matched, paired on identical (game, seed) sets; 2 seeds for the exploratory ladder, 3 seeds for the confirmatory pair (k=1 vs k=7 memory-free, all three sets). (7) Reliance index = matched minus absent; harm index = absent minus mismatched; per type. (8) Cost axis: training GPU-hours (k=7 prompts roughly triple the token count of Measurement B) plus per-episode inference tokens for each deployment condition; Pareto plot against the k=3 in-context agent. Budget: ~14 QLoRA runs (~25 GPU-hours), ~4 student-rollout passes over T (~3.5k episodes), ~20k evaluation episodes; three to four days on two A100s with training overlapping serving.",
 "Baselines and Ablations": "Base agent k=0 and the in-context k=1/3/7 arms of Measurement A as the cost reference. Measurement B's k_train=0 student is the origin of the ladder and the Gate-0 arm. P-CD0 (teacher k_t=0) for self-training format effects. Training-time decoys (DEC-3, DEC-7) as the named missing baseline of the archived idea; test-time mismatched blocks as inference placebos. RATE-3 separates dose-per-example from fraction-of-examples (the context-dropout recipe). Ablations: LoRA rank 16 vs 32 at k=7 (capacity is not the limiter); loss masking of the memory block tokens is already standard (targets are action tokens only), an arm that also trains on memory tokens checks whether copying pressure changes the effect; the procedure-held-out partition checks that the dose effect is about encoding of the procedures present in training, not general capability.",
 "Falsifiable Predictions": "P1: memory-free accuracy on the student-side ladder is monotone decreasing over k in {1, 3, 7} (linear contrast on paired differences across seeds) and the k=7 student is below the k=1 student by at least 0.4 x the Gate-0 gain (pre-registered fraction); falsified if k=7 >= k=1 memory-free, which would mean the abundance effect does not hold on trajectories and deployment-matched training dominates. P2: DEC-7 memory-free equals k=0 within the equivalence margin (0.25 x Gate-0 gain); falsified if DEC-7 drops as much as k=7, which would make the effect a long-prefix effect rather than information abundance. P3: reliance index and mismatched-memory harm both increase with k_train (k=7 student loses the most when memory is removed and is hurt the most by mismatched memory). P4: teacher-side ladder memory-free accuracy is non-decreasing in k_t (k_t=7 >= 3 >= 1 >= P-CD0 within CI), so the student-side and teacher-side curves cross between k=1 and k=7; falsified if the teacher-side ladder also declines, which would locate the effect in the information rather than the student's prompt. P5: per-type memory-free deficit relative to the k=0 student correlates with per-type delta-NLL(k) (Spearman >= 0.6 over 6 types x 3 doses) and delta-NLL of decoys is ~0; on the self-rollout pool both delta-NLL and the k=7 deficit are at least halved. P6: RATE-3 sits between k=0 and k=3 on memory-free accuracy and on reliance.",
 "Measurement and Noise Control": "Primary metric: net success per 100 games, paired on identical (game, seed) tuples across arms; bootstrap CI over games. Gate 0 before the ladder: the k_train=0 QLoRA student must show a memory-free gain >= 12 net/100 over the base agent pooled over valid_seen + valid_unseen + H at 3 seeds (about +/-4 net at 95 % with ~2,200 paired episodes); if it fails the dose claim is declared untestable on that pool (there is no encoded gain to suppress) and only the reliance/harm indices are reported. The predicted k=1 vs k=7 deficit (>= 0.4 x gain >= ~5 net) is above the pooled MDE of ~4 net; the exploratory ladder at 274 x 2 per split resolves only trends, and the trend test across four doses is the pre-registered exploratory statistic. Training-seed variance from the two-seed k=1 and k=7 arms is added to the confirmatory CI. Teacher-forced per-step action accuracy on H (~6,000 steps) is the low-noise secondary for P1 and P5; delta-NLL is computed once on the base model and is noise-free relative to the success metric. Per-type claims are exploratory unless the pooled per-type count exceeds 150 games.",
 "Preprint Collision Check": "Query 1 (mechanism, --recent, s2=ok hf=ok): 'abundant training context reduces parametric encoding increases context reliance fine-tuning' returned only 2608.12218 (the paradox paper, documents), 2608.05224 (cognitive models) and 2605.09932 (FocuSFT, long-context attention); no trajectory, memory or teacher-side dose study. Query 2 (closest method, all years, s2=ok hf=ok): 'fine-tuning with retrieved demonstrations in prompt dependence on retrieval at test time crutch' returned nothing relevant (2604.05467 CUE-R on RAG item utility, older ICL exemplar papers 2410.20482, 2405.16122, 2404.08865, 2309.07900). Query 3 (--recent, s2=ok hf=ok): 'supervised fine-tuning with retrieved experience in the prompt evaluated without retrieval at test agent memory reliance' returned 2606.05684 (AdaMEM, no updates), 2606.01967 (Training Prompt Matters), 2603.18272 (retrieval-augmented SFT, never evaluated retrieval-free), 2603.19313, 2602.16313, 2601.05107, 2504.13145. No hit varies the training-time memory dose, adds training-time decoys or contrasts student-side with teacher-side dose. WebSearch not used (quota exhausted).",
 "Risk Factors and Limitations": "If Gate 0 fails on the expert pool (QLoRA on off-policy walkthroughs may encode little; Experience Distillation reports direct SFT retaining 3.8 %), the ladder moves to the context-distillation targets (teacher rollouts at k=0) or the self-rollout pool, which changes the claim's scope and is pre-registered as amendment A1. Longer prompts change effective batch composition and optimisation; equal examples and epochs are held fixed and GPU-hours reported, but the decoy arm is the only defence against optimisation artefacts. Reverse-KL on-policy distillation of one epoch may under-train the teacher-side ladder, flattening P4 in either direction; P-CD0 and the CD variant at k_t=3 bound this. Retrieval from B for train and test is by goal similarity, so near-duplicate templates inflate the matched condition; the procedure-held-out partition is the check. One backbone, one environment; the self-rollout pool is still being collected."
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

Proposal: student_side_abundance — Information Abundance Is a Student-Side Effect: Training-Time Memory Dose Suppresses Parametric Encoding of Agent Experience Only When the Memory Sits in the Student's Own Prompt

- arxiv:2608.12218 · 2026-08-12 · preprint · sim 0.60 · hf
  Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge
  Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which 
- arxiv:2603.15994 · 2026-03-16 · preprint · sim 0.59 · hf
  Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving
  Retrieval-augmented generation stores all content indiscriminately, degrading accuracy as noise accumulates. Parametric approaches compress knowledge into weights, precluding selective updates. Neither mirrors biological memory, which gates encoding based on salience and archives rather than deletes superseded information. We introduce write-time gating that filters incoming knowledge objects using composite salience scores (source reputation, novelty, reliability) while maintaining version chai
- arxiv:2510.04454 · 2025-10-06 · preprint · sim 0.57 · hf
  Mitigating Forgetting Between Supervised and Reinforcement Learning Yields Stronger Reasoners
  Large Language Models (LLMs) show strong reasoning abilities, often amplified by Chain-of-Thought (CoT) prompting and reinforcement learning (RL). Although RL algorithms can substantially improve reasoning, they struggle to expand reasoning boundaries because they learn from their own reasoning trajectories rather than acquiring external knowledge. Supervised fine-tuning (SFT) offers complementary benefits but typically requires large-scale data and risks overfitting. Recent attempts to combine 
- arxiv:2410.21750 · 2024-10-29 · preprint · sim 0.57 · hf
  Learning and Unlearning of Fabricated Knowledge in Language Models
  What happens when a new piece of knowledge is introduced into the training data and how long does it last while a large language model (LM) continues to train? We investigate this question by injecting facts into LMs from a new probing dataset, "Outlandish", which is designed to permit the testing of a spectrum of different fact types. When studying how robust these memories are, there appears to be a sweet spot in the spectrum of fact novelty between consistency with world knowledge and total r
- arxiv:2410.01380 · 2024-10-02 · preprint · sim 0.55 · hf
  Knowledge Entropy Decay during Language Model Pretraining Hinders New Knowledge Acquisition
  In this work, we investigate how a model's tendency to broadly integrate its parametric knowledge evolves throughout pretraining, and how this behavior affects overall performance, particularly in terms of knowledge acquisition and forgetting. We introduce the concept of knowledge entropy, which quantifies the range of memory sources the model engages with; high knowledge entropy indicates that the model utilizes a wide range of memory sources, while low knowledge entropy suggests reliance on sp
- arxiv:2608.18852 · 2026-08-19 · preprint · sim 0.55 · hf
  SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
  Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve
- arxiv:2511.23271 · 2025-11-28 · preprint · sim 0.51 · hf
  Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs
  Carefully engineered system prompts play a critical role in guiding the behavior of LLM agents, but their considerable length introduces significant drawbacks, including increased inference latency, higher computational cost, and reduced effective context length. This raises the question of whether such lengthy prompts can be replaced by a drastically reduced number of tokens while preserving their behavioral effect on downstream tasks. To enable this, we propose a lightweight three-stage traini
- arxiv:2603.10359 · 2026-03-11 · preprint · sim 0.49 · hf
  HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation
  Distilling reasoning capabilities from Large Reasoning Models (LRMs) into smaller models is typically constrained by the limitation of rejection sampling. Standard methods treat the teacher as a static filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight Entropy-Assisted Learning (HEAL), an RL-free framework designed to bridge this re
- arxiv:2307.06948 · 2023-07-13 · preprint · sim 0.48 · hf
  Self-regulating Prompts: Foundational Model Adaptation without
  Forgetting
  Prompt learning has emerged as an efficient alternative for fine-tuning foundational models, such as CLIP, for various downstream tasks. Conventionally trained using the task-specific objective, i.e., cross-entropy loss, prompts tend to overfit downstream data distributions and find it challenging to capture task-agnostic general features from the frozen CLIP. This leads to the loss of the model's original generalization capability. To address this issue, our work introduces a self-regularizatio
- arxiv:2608.20965 · 2026-08-21 · preprint · sim 0.48 · hf
  Training, learning and inference: unified dynamics of neural systems
  We define an atomic generation fact f=(u,tau,omega,z;rho), recording the origin, realized transformation, concrete occurrence, generated result and relation role. Compiled into a Generation-Fact Graph (GFG), these facts provide an AI-native, compilable scientific fact substrate preserving generation histories. We establish a GFG-based recursive scientific process in which analysis, intervention, replay and validation form facts for later cycles. Using nanoGPT, we establish unified training-learn

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

