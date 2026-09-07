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
 "Name": "train_dose_sets_substrate",
 "Title": "Training-Time Memory Dose Chooses the Substrate: The Information-Abundance Effect on Agent Trajectories and Its Context-Explained-Loss Signature",
 "Short Hypothesis": "When an agent is fine-tuned or distilled on experience with retrieved episodes in its training prompt, the amount of memory present at training time (k_train) decides where the experience ends up: relevant context in the prompt reduces what is encoded parametrically in proportion to how much of the action-token loss that context already explains at initialization, so memory-free retention peaks at a low intermediate dose and falls at k=7, fragility to mismatched memory rises monotonically with k_train, a token-matched relevance-destroyed decoy at training time produces neither effect, the effect is smaller on the on-policy self-rollout pool (where the base loss is already low), and no single dose is optimal for both memory-free and memory-present deployment.",
 "Related Work": "The information-abundance paradox (arXiv:2608.12218) shows on documents and generic SFT that abundant relevant training context reduces parametric encoding and raises context reliance with an intermediate optimum; it has no agent-trajectory data, no memory-conditioned distillation and no relevance-destroyed control. Retrieval-augmented SFT for agents (arXiv:2603.18272) trains with retrieved trajectories in the prompt and reports better unseen-task generalization but never varies the dose or evaluates memory-free or misleading-memory deployment. MemHarness (arXiv:2607.28272) trains a policy to reconstruct retrieved experience; PMD (arXiv:2607.01480) distills procedural memory into a memory-free policy; UCOB (arXiv:2606.29502) self-distills between skill-conditioned and no-skill prompts; OPSD (arXiv:2601.18734), OPCD (arXiv:2602.12275), Skill-SD (arXiv:2604.10674) and learned privileged context (arXiv:2608.13040) put memory-like context on the teacher side; none reports how the student's own training-time context dose changes what is encoded. The privilege-illusion family (DAPD arXiv:2608.01735, DOPD arXiv:2606.30626, OP2SD arXiv:2608.09228) studies asymmetry between teacher and student contexts, not the dose in the student prompt. Latent learning (arXiv:2509.16189) argues episodic memory complements parametric learning without a dose manipulation. In this program, memory_in_the_loop_training_decomposition (round 2) had one training dose, bank items that were also targets and no training-time decoy; memory_dropout_coadaptation (round 1) proposed dropout as a mitigation, not a dose ladder with a mechanism.",
 "Abstract": "Hybrid systems train agents with memory in the prompt and then deploy them with more, less or no memory. Whether the training-time dose helps or hurts the weights is unknown for agent trajectories: the information-abundance paradox predicts that relevant context in the training prompt lowers the gradient pressure to encode the procedure, so memory-free performance should peak at an intermediate dose and reliance on (and fragility to) context should grow with dose; the retrieval-augmented-SFT literature reports only that training with retrieval generalizes better. We run a pre-registered dose ladder on Qwen3-32B and ALFWorld with a partitioned pool: step-level QLoRA SFT on the target partition with k_train in {0,1,3,7} matched items retrieved from the bank partition, a token-matched relevance-destroyed decoy at k=3 (the control that separates 'relevant context reduces encoding' from 'a long prefix hurts SFT'), and context distillation from a k=3 teacher into a student prompted at k=0 or k=3, plus P-CD0. Every student is evaluated memory-free, with matched memory and with token-matched mismatched memory, with per-type retention, reliance and fragility as estimands. The mechanism is measured directly: the context-explained action-token loss at initialization, per example and per task type, should predict the per-type encoding deficit, and its smaller size on the on-policy self-rollout pool should predict a smaller dose effect there. The routing consequence is stated as a Pareto claim: the dose that maximizes memory-free accuracy and the dose that maximizes with-memory accuracy differ, so a single hybrid checkpoint cannot be optimal for both deployments.",
 "Experiments": "Setup and partition as in the program's rules: Qwen3-32B, thinking off, ReAct, vLLM one replica per GPU with QLoRA on the idle GPU; train tasks split by type into T targets (55%), B bank (35%), H calibration/proxy (10%); retrieval by MiniLM on the goal sentence from B only. Step 1, mechanism pre-measurement (cheap, deterministic): for every step-level example in T, action-token NLL under the base model with the prompt at k=0, k=1, k=3, k=7 and decoy-3; record dl_i(k) = NLL(k=0) - NLL(k) and its per-type mean, on both the expert and self-rollout pools (a forward pass over ~8.9k examples x 5 prompts). Step 2, Gate 0 on the untrained agent (274 x 2 splits x 3 seeds): in-context gain at k=3 from B (require pooled >= 15 net) and the mismatched-memory penalty (k=3 token-matched other-type items versus absent) to establish the baseline fragility F0. Step 3, trained arms on the expert pool: SFT with k_train in {0,1,3,7} (per-epoch cost ~1.1, 1.6, 2.7, 4.8 GPU-h on T; 2 epochs, checkpoint by memory-free NLL on H); SFT-decoy3 (three relevance-destroyed items: other-type items with goal sentence and object tokens replaced, length matched to within 5%); CD-k3 with student prompt k_s=0 and k_s=3 (teacher pass at k=3 over T, ~805 episodes; student trained on teacher outputs); P-CD0 (teacher k=0, student k=0). Step 4, evaluation of each arm in three prompt conditions (absent; matched k=3 from B; mismatched token-matched), 274 x 2 x 3 seeds, plus matched at the training dose for the k=1 and k=7 arms (the diagonal). Estimands per arm and type: retention r = (A0_student - A0_base)/g; reliance R = A+ - A0; fragility F = A0 - A-; encoding deficit D(k) = r(0) - r(k); proxy: memory-free NLL on H. Step 5, self-rollout replicate: SFT k_train in {0,3,7} and decoy3, 2 seeds, same three conditions. Step 6, misleading-memory extension only if Gate 0b passes: planted wrong-procedure items (swap the appliance in heat/cool items) must harm the untrained agent by >= 6 net; then evaluate the k_train ladder under misleading items. Step 7, Pareto: for each deployment condition (absent, matched k=3, mismatched) report accuracy versus training GPU-hours plus per-episode tokens across doses; identify the memory-free-optimal and with-memory-optimal doses with bootstrap CIs on the argmax. Budget: 8 arms on the expert pool (~20 GPU-h training) and 4 on the self-rollout pool, ~35k episodes; core = k in {0,3,7}, decoy3, CD k_s=0, P-CD0 first.",
 "Baselines and Ablations": "P-CD0 (empty-retrieval distillation) and SFT-k0 as the no-dose references; SFT-decoy3 as the training-time placebo (length without relevance); mismatched token-matched memory at test as the inference-time placebo; CD with k_s=0 versus k_s=3 to test the effect on the distillation side; matched-at-training-dose evaluation for the diagonal; per-type analysis with the three multi-step types as the high-gain regime; the low-noise NLL proxy on H as an ablation of the episode metric. Optional ablation (not a headline, because memory_dropout_coadaptation is archived): k_train=3 with the memory block dropped on 50% of examples, to check whether intermittent dose recovers k=0 retention. Positive control for the mechanism: a task type whose procedure the k=0 model already nails (pick-and-place, dl ~0) should show no dose effect; the three multi-step types (large dl) should show the largest.",
 "Falsifiable Predictions": "P1 (intermediate optimum): memory-free retention r(k_train) is non-monotone, with r(1) or r(3) > r(0) and r(7) < r(0) by at least 0.15 g (about 4-5 net points pooled); monotone increase (co-training story) or a flat ladder falsifies the abundance effect on trajectories. P2 (decoy separates relevance from length): r(decoy3) is within 0.1 g of r(0) and above r(3); if r(decoy3) ~ r(3) the effect is a long-prefix SFT artefact, not information abundance. P3 (fragility): F rises monotonically with k_train, F(7) - F(0) >= 6 net points, F(decoy3) - F(0) <= 2. P4 (mechanism): across (type, dose) cells on both pools the encoding deficit D_t(k) correlates with the mean context-explained loss dl_t(k) with rho >= 0.5 (bootstrap CI excluding 0); on the self-rollout pool mean dl is at most half of the expert pool's and the pooled dose effect on r shrinks by a comparable factor; a self-rollout reversal (r rising monotonically while dl > 0) falsifies the loss-explained account. P5 (distillation side): r(CD, k_s=3) < r(CD, k_s=0) by >= 0.15 g; equality means the effect is SFT-specific. P6 (no dominant dose): the dose maximizing memory-free accuracy and the dose maximizing matched-memory accuracy differ by >= 2 rungs with non-overlapping bootstrap argmax sets; if k=1 or k=3 dominates all conditions a single hybrid checkpoint suffices and the routing implication is void.",
 "Measurement and Noise Control": "Paired (game, seed) design across all arms and conditions, net/100 per pair, cluster bootstrap over games; 3 seeds on expert-pool arms (pooled contrast ~+/-4.6 net points over 548 games x 3 seeds), 2 seeds on the self-rollout replicate; per-type contrasts reported with their ~+/-13-15 point floors and used only for the correlation in P4, where the unit is the cell and the CI comes from bootstrap over games. MDE stated before the confirmatory run: 5 net points pooled for P1/P3, 0.1 g for P2 via the NLL proxy (deterministic, per-token) plus episodes. Gate 0a (in-context gain >= 15 net under the partition) and Gate 0b (mismatched penalty measured; misleading extension only if >= 6 net). Checkpoint selection by memory-free NLL on H for all arms, so dose arms are not advantaged by with-memory selection. Prompt, retriever, truncation, decoding temperature and vLLM version pinned; the decoy generator and token-matching tolerance (5%) pre-registered; evaluation order interleaved across arms. Training-loss curves and per-step gradient norms on action tokens logged per dose as mechanism evidence.",
 "Preprint Collision Check": "All searches via the literature command (s2cli: Semantic Scholar + HuggingFace Papers, both 'ok'); WebSearch not used (quota exhausted this session); WebFetch never used. Q1 (mechanism, --recent): 'training context abundance reduces parametric encoding context reliance fine-tuning with retrieved context robustness absent misleading' -> a single hit, 2608.12218 (Information Abundance Paradox), documents and generic SFT only. Q2 (closest method, --recent): 'retrieval-augmented fine-tuning agent trajectories context dependence at inference misleading retrieved experience' -> 2607.10608 (compliance trap), 2604.04949 (learning to retrieve from trajectories), 2603.27813, 2603.18272 (retrieval-augmented SFT with LoRA; the closest, no dose ladder, no memory-free evaluation), 2603.10600, 2509.16189 (latent learning); none varies training-time memory dose or measures memory-free retention against it. Q3 (--recent): 'context distillation versus in-context learning cost comparison' -> 2607.21051, 2512.02543, 2602.15902 and off-topic hits; nothing on training-dose effects. Verdict: no collision; 2608.12218 is the mechanism source and explicitly leaves trajectories and memory-conditioned distillation untested.",
 "Risk Factors and Limitations": "The k=7 arm quadruples training tokens (~4.8 GPU-h per epoch on T) and may be under-trained at equal epochs; we report both equal-epoch and equal-token-budget checkpoints. Near-duplicate templates in the pool make matched items unusually predictive, so dl may be large and the effect exaggerated relative to natural pools; stated as a limitation and partly addressed by the self-rollout replicate. Per-type cells are noisy; P4 relies on the correlation across cells and the NLL proxy. Ceiling effects at k=3 matched deployment (0.81-0.87 success) can compress with-memory differences and blunt P6; reported with timeouts and per-type breakdown. The self-rollout pool is still being collected and may be small or type-skewed. ALFWorld only; the effect could differ in environments where memory carries bindings rather than procedures. Distinct from Q3's literal phrasing only by the mechanism measurement, the decoy, the distillation-side arm and the Pareto claim; if the dose effect is absent the null is informative for hybrid design and is reported as such."
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

Proposal: train_dose_sets_substrate — Training-Time Memory Dose Chooses the Substrate: The Information-Abundance Effect on Agent Trajectories and Its Context-Explained-Loss Signature

- arxiv:2607.21051 · 2026-07-23 · preprint · sim 0.67 · hf
  Sample-Efficient Learning from Agent Experience
  Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interacti
- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.64 · hf
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2603.13017 · 2026-03-13 · preprint · sim 0.62 · hf
  Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation
  Long conversations with an AI agent create a simple problem for one user: the history is useful, but carrying it verbatim is expensive. We study personalized agent memory: one user's conversation history with an agent, distilled into a compact retrieval layer for later search. Each exchange is compressed into a compound object with four fields (exchange_core, specific_context, thematic room_assignments, and regex-extracted files_touched). The searchable distilled text averages 38 tokens per exch
- arxiv:2603.18272 · 2026-03-18 · preprint · sim 0.61 · hf
  Retrieval-Augmented LLM Agents: Learning to Learn from Experience
  While large language models (LLMs) have advanced the development of general-purpose agents, achieving robust generalization to unseen tasks remains a significant challenge. Current approaches typically rely on either fine-tuning or training-free memory-augmented generation using retrieved experience; yet both have limitations: fine-tuning often fails to extrapolate to new tasks, while experience retrieval often underperforms compared to supervised baselines. In this work, we propose to combine t
- arxiv:2603.15666 · 2026-03-12 · arXiv.org · sim 0.61 · s2
  Compiled Memory: Not More Information, but More Precise Instructions for Language Agents
  Existing memory systems for language agents address memory management: how to retrieve and page more information within a context budget. We address a complementary problem -- memory utility: what experience is worth keeping, and how it should change agent behavior. We present Atlas, a memory kernel that compiles accumulated task experience into an agent's instruction structure -- without fine-tuning, RAG, or human intervention. Memory is distillation, not storage; delivery is instruction rewrit
- arxiv:2608.07169 · 2026-08-07 · preprint · sim 0.60 · hf
  Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory
  Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow m
- arxiv:2305.16338 · 2023-05-24 · preprint · sim 0.60 · hf
  Think Before You Act: Decision Transformers with Internal Working Memory
  Large language model (LLM)-based decision-making agents have shown the ability to generalize across multiple tasks. However, their performance relies on massive data and compute. We argue that this inefficiency stems from the forgetting phenomenon, in which a model memorizes its behaviors in parameters throughout training. As a result, training on a new task may deteriorate the model's performance on previous tasks. In contrast to LLMs' implicit memory mechanism, the human brain utilizes distrib
- arxiv:2607.08716 · 2026-07-09 · preprint · sim 0.60 · hf
  Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
  In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate me
- arxiv:2403.02757 · 2024-03-05 · preprint · sim 0.60 · hf
  In-Memory Learning: A Declarative Learning Framework for Large Language
  Models
  The exploration of whether agents can align with their environment without relying on human-labeled data presents an intriguing research topic. Drawing inspiration from the alignment process observed in intelligent organisms, where declarative memory plays a pivotal role in summarizing past experiences, we propose a novel learning framework. The agents adeptly distill insights from past experiences, refining and updating existing notes to enhance their performance in the environment. This entire
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.59 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

