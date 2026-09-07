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
 "Name": "reversal_savings_latent_retention",
 "Title": "Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory",
 "Short Hypothesis": "On an A -> B -> A rule stream in ALFWorld, a continual QLoRA whose rule-A accuracy has eroded to the reset-LoRA floor during phase B re-acquires rule A on reversal with at most half the post-return items and GPU-hours of a reset LoRA (savings ratio <= 0.5), because parametric interference silences rather than erases the earlier mapping. Retrieval memory has no latent state: a bounded FIFO bank is the no-retention reference, and the bank policies that do show savings (unbounded, failure-decayed) obtain them only by keeping rule-A items retrievable, which costs a stale tax during B that the continual LoRA does not pay. Both substrates erode; the claim is that the weights channel's erosion is partly reversible for free, the memory channel's only for a price.",
 "Related Work": "Closest: Do Self-Evolving Agents Forget (2605.09315) documents non-monotonic erosion across memory and model channels and adds a capability-preserving constraint, but measures erosion only, never relearning speed, and never the two channels head-to-head on one stream. When Continual Learning Moves to Memory (2604.27003) locates the bottleneck in retrieval competition without a weight-update arm. FOREVER (2601.03938) schedules replay by model-centric time; Forgetting in Language Models (2605.26097) removes forgetting with self-generated replay; neither reports reacquisition after reversal or a memory-based alternative. Spurious Forgetting (2501.13453) and Unlearning Isn't Deletion (2505.16831) show that performance loss after fine-tuning often reflects alignment shift rather than knowledge loss, on text tasks; this proposal is the agent-substrate version of that observation with a retrieval-memory foil. UniMem (2607.26017) and COVE (2608.01234) route between substrates but never ask whether consolidated knowledge survives a later change. Archived: opposite_sided_failure_under_shift asserted that a LoRA cannot keep a renamed mapping; this idea tests the opposite, empirically.",
 "Abstract": "Continual adaptation papers measure how much an agent loses when the environment changes; they do not measure how much of that loss is recoverable, or whether the answer depends on where the experience lives. We build an A -> B -> A rule stream in ALFWorld (heating works at the microwave under A and only at the stoveburner under B; cleaning verbs swap likewise; other task types are untouched, one type is held out entirely) and feed the same expert experience stream, split by item parity into a bank partition and a target partition, to six arms on Qwen3-32B: FIFO bank, unbounded bank, failure-decayed bank, continual QLoRA, reset QLoRA and QLoRA with a replay buffer. We probe the shifted types under the active rule through each phase, probe rule-A capability counterfactually at the end of B (erosion), and measure recovery time on reversal. The estimand is the savings ratio, recovery time of the continual arm divided by that of the reset arm, together with the stale tax each arm pays during B, an off-stream probe of unshifted and held-out types, and a cumulative cost curve in GPU-hours and injected tokens. The falsifiable content is that weights show large savings after behavioural erosion to the floor while retrieval memory shows savings only in proportion to the stale tax it paid; a rank-32 adapter that is simply overwritten during B would refute it.",
 "Experiments": "- E0 Gate 0: stale harm >= 15 net points on the shifted types (k=3 all-A items under rule B), and the positive control that a QLoRA trained on A-phase items scores >= 15 net points above the base model under rule A; failing either, the shift is strengthened or the claim declared untestable.\n- E1 Stream: phases A1 (400 expert items), B (400), A2 (400) sampled from train tasks excluding the held-out type and a 100-task shifted-type reserve; odd items feed the bank arms, even items feed the LoRA arms, so every substrate consumes 200 disjoint items per phase and no bank item is ever a training target. Arms: FIFO bank N=200 (N=600 ablation), unbounded bank, failure-decayed bank (item weight x0.5 when retrieved into a failed episode, x1.2 into a success; retrieval score = similarity x weight), continual QLoRA (chunk of 100 target items, one epoch, no replay), reset QLoRA (adapter re-initialized at each phase boundary, trained on the current phase only), QLoRA with replay buffer (all past target items replayed 1:1 with the chunk).\n- E2 Recovery curves: shifted-type probe (about 95 validation games plus the 100-task reserve) under the active rule after 50, 150 and 300 items of phases B and A2, 1 seed per intra-phase point (the curve fit pools points), 2 seeds at phase ends; recovery time = items until 90 % of the arm's own A1-end level, converted to GPU-hours and tokens.\n- E3 Erosion probe: at the end of B, all arms probed under rule A (counterfactual environment) on the shifted probe set; Gate 1 requires the continual LoRA to sit within 5 net points of the reset LoRA (behavioural erosion to the floor), else B is lengthened to 800 items before the confirmatory run.\n- E4 Phase-end full probes: 274 validation games x 2 seeds under the active rule; LoRA arms with memory absent, matched memory (k=3 from the bank partition of the current phase) and token-matched mismatched memory; bank arms with their own store; unshifted in-stream types and the held-out type reported as the off-stream probe.\n- E5 Cost axis: cumulative GPU-hours (chunk training, replay) and cumulative injected tokens per arm plotted against shifted-type accuracy through the stream; Pareto plot at the A2 recovery point.\n- E6 Own-rollout replication of the two headline arms (continual vs reset LoRA) and the FIFO bank, with successes collected on-stream under the active rule.",
 "Baselines and Ablations": "- Reset LoRA is the no-savings parametric control; FIFO bank is the no-retention memory reference (its savings ratio is expected near 1 by construction and is reported as a reference, not a finding).\n- Replay-buffer LoRA vs unbounded bank: the two explicit-retention arms, matched on what they retain, to compare stale tax and savings across substrates.\n- FIFO capacity ablation N=200 vs N=600: eviction share of unshifted-type items varies, giving a non-definitional erosion measurement on the memory side.\n- Rank ablation (16 vs 32) and learning-rate ablation for the continual LoRA: savings should shrink as B training becomes more destructive; reported as a boundary condition.\n- Self-generated replay (2605.26097 style, 1:1 with chunk) as an alternative retention arm on the weights side if the replay buffer arm shows stale tax.\n- Decoy k=3 (relevance-destroyed items of matched length) at phase ends for the bank arms so the bank-vs-LoRA accuracy differences are not attributable to prompt length.",
 "Falsifiable Predictions": "- P1 Continual LoRA savings ratio <= 0.5 while its rule-A probe at B end is within 5 net points of the reset LoRA; falsified by a ratio >= 0.8 (the adapter was overwritten) or by no erosion at B end (then savings are trivial).\n- P2 Unbounded bank and decayed bank recover on reversal faster than the FIFO bank, but their stale tax during B (drop on shifted types relative to FIFO at matched stream position) exceeds 10 net points, whereas the continual LoRA's stale tax relative to the reset LoRA is within 5 net points; falsified if the decayed bank obtains savings with a stale tax within noise (retrieval-side retention for free).\n- P3 Replay-buffer LoRA behaves like the unbounded bank (larger stale tax, larger savings), i.e. explicit retention costs the same in both substrates; the substrate difference lives in the implicit channel only.\n- P4 Off-stream: LoRA arms lose <= 5 net points on unshifted and held-out types over the stream; the FIFO bank's unshifted-type gain drops with eviction share (N=200 below N=600 by a measurable margin), showing type-selective erosion on the memory side; falsified if LoRA arms erode unshifted types by more than the bank does.\n- P5 Cost: the continual LoRA reaches its A2 recovery at <= 0.3 GPU-hours and zero injected tokens beyond the stream, while every bank arm pays about 430 tokens per episode throughout; on the two-axis plot no bank arm dominates the continual LoRA at the A2 recovery point.",
 "Measurement and Noise Control": "All arms see the identical task sequence and seeds (paired stream); probe games are paired across arms and phases. The shifted probe set (about 195 games) at 2 seeds gives roughly +/-9 net points for a paired difference, adequate for the >= 15-point Gate 0 harm and the 10-point stale-tax prediction; intra-phase points at 1 seed are used only through a monotone (isotonic) fit whose crossing time is bootstrapped over probe games and over the 2 stream seeds run for the headline pair. The savings ratio is reported with a bootstrap CI; the pre-registered success criterion is that the CI upper bound is below 0.7. Gate 1 (erosion to the floor) is checked before the confirmatory run; if the continual LoRA does not erode, B is lengthened and the gate re-run rather than the claim rewritten. Budget: about 20,000 episodes and under 10 GPU-hours of training, roughly five days on two A100s with one GPU serving while the other trains the next chunk.",
 "Preprint Collision Check": "- Q1 (mechanism, --recent, s2cli = S2 + HF): 'relearning savings after catastrophic forgetting LoRA continual fine-tuning reacquisition' -> 2602.03493 (intermediate principal components for LoRA forgetting trade-offs), 2510.15103 sparse memory finetuning, 2508.06202 LiLoRA, 2504.13407; none measures reacquisition speed after reversal or compares with a retrieval bank.\n- Q2 (mechanism, --recent, s2cli): 'task reversal relearning speed continual learning language model latent retention after forgetting' -> 2605.26097 (self-generated replay), 2603.06610 CapTrack, 2505.16831 (unlearning is reversible at the representation level), 2501.13453 (spurious forgetting: alignment shift, not knowledge loss); the last two are the closest mechanism precedents and are cited; none is an agent stream with a memory foil.\n- Q3 (closest method, --recent, s2cli): 'external memory stability plasticity retrieval competition continual learning LLM agents' -> 2608.07622 Controlled Memory Interference, 2604.27003, 2607.13591 MemCon, 2606.06448, 2603.18718, 2602.22406, 2601.14287; memory-only, no reversal design.\n- WebSearch unavailable in this session and not used. No result reports a savings measurement across substrates.",
 "Risk Factors and Limitations": "The savings effect may be small at rank 32 with 200 items per phase, in which case the result is a bounded null (savings ratio CI including 1) reported with the rank and learning-rate ablations. The failure-decayed bank is our own implementation of a Live-Evo-style policy, not the published system, so its stale tax reflects our decay constants; two constants are pre-registered. Counterfactual probing under rule A during phase B requires the wrapper to switch rules for evaluation only, which is straightforward but must be audited for leakage into the stream. Expert items make the stream exogenous; the own-rollout replication is limited to three arms for budget. Task repetition across phases (the same train task can appear under both rules) is intended, but near-duplicate goals mean bank retrieval cannot tell A from B items by similarity, which is the retrieval-competition regime we want and also a limitation of MiniLM retrieval specifically. Findings are for Qwen3-32B, QLoRA and ALFWorld; a second environment is out of budget this round."
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

Proposal: reversal_savings_latent_retention — Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory

- arxiv:2511.04228 · 2025-11-06 · preprint · sim 0.55 · hf
  REMIND: Input Loss Landscapes Reveal Residual Memorization in Post-Unlearning LLMs
  Machine unlearning aims to remove the influence of specific training data from a model without requiring full retraining. This capability is crucial for ensuring privacy, safety, and regulatory compliance. Therefore, verifying whether a model has truly forgotten target data is essential for maintaining reliability and trustworthiness. However, existing evaluation methods often assess forgetting at the level of individual inputs. This approach may overlook residual influence present in semantical
- arxiv:2606.26560 · 2026-06-25 · preprint · sim 0.55 · hf
  Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention
  Delta-rule linear attention improves recurrent memory updates by correcting what is already stored at the current write address before writing new content. However, the active correction is still anchored to that same write address. As a result, stale information stored at a different address cannot be actively removed before new content is written elsewhere. We propose Erase-then-Delta Attention (EDA), a memory update rule that decouples where to erase from where to write. The key insight is th
- arxiv:2511.17100 · 2025-11-21 · preprint · sim 0.53 · hf
  Geometric-Disentangelment Unlearning
  Machine unlearning, the removal of a training subset's influence from a deployed model, is critical for privacy preservation and model reliability, yet gradient ascent on forget samples often harms retained knowledge. Existing approaches face a persistent tradeoff between effective forgetting and preservation on the retain set. While previous methods provide useful heuristics, they often lack a formal analysis on how exactly forgetting updates harm retained knowledge, and whether the side effect
- arxiv:2509.05316 · 2025-08-29 · preprint · sim 0.53 · hf
  Standard vs. Modular Sampling: Best Practices for Reliable LLM Unlearning
  A conventional LLM Unlearning setting consists of two subsets -"forget" and "retain", with the objectives of removing the undesired knowledge from the forget set while preserving the remaining knowledge from the retain. In privacy-focused unlearning research, a retain set is often further divided into neighbor sets, containing either directly or indirectly connected to the forget targets; and augmented by a general-knowledge set. A common practice in existing benchmarks is to employ only a singl
- arxiv:2410.14713 · 2024-10-09 · preprint · sim 0.52 · hf
  QuAILoRA: Quantization-Aware Initialization for LoRA
  QLoRA reduces the memory-cost of fine-tuning a large language model (LLM) with LoRA by quantizing the base LLM. However, quantization introduces quantization errors that negatively impact model performance after fine-tuning. In this paper we introduce QuAILoRA, a quantization-aware initialization for LoRA that mitigates this negative impact by decreasing quantization errors at initialization. Our method spends a small amount of computational overhead to compute this quantization-aware initializa
- arxiv:2505.16831 · 2025-09-26 · preprint · sim 0.51 · hf
  Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs
  Unlearning in large language models (LLMs) aims to remove specified data, but its efficacy is typically assessed with task-level metrics like accuracy and perplexity. We demonstrate that these metrics are often misleading, as models can appear to forget while their original behavior is easily restored through minimal fine-tuning. This phenomenon of reversibility suggests that information is merely suppressed, not genuinely erased. To address this critical evaluation gap, we introduce a represent
- arxiv:2601.10566 · 2026-03-17 · preprint · sim 0.51 · hf
  Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure
  Selective knowledge erasure from LLMs is critical for GDPR compliance and model safety, yet current unlearning methods conflate behavioral suppression with true knowledge removal, allowing latent capabilities to persist beneath surface-level refusals. In this work, we address this challenge by introducing Knowledge Immunization Framework (KIF), a representation-aware architecture that distinguishes genuine erasure from obfuscation by targeting internal activation signatures rather than surface o
- arxiv:2509.14624 · 2025-09-18 · preprint · sim 0.50 · hf
  Reveal and Release: Iterative LLM Unlearning with Self-generated Data
  Large language model (LLM) unlearning has demonstrated effectiveness in removing the influence of undesirable data (also known as forget data). Existing approaches typically assume full access to the forget dataset, overlooking two key challenges: (1) Forget data is often privacy-sensitive, rare, or legally regulated, making it expensive or impractical to obtain (2) The distribution of available forget data may not align with how that information is represented within the model. To address these
- arxiv:2607.09236 · 2026-07-10 · preprint · sim 0.48 · hf
  Forget Narrowly, Retain Broadly: Unlearning as an Asymmetric Generalization Problem
  Machine unlearning in LLMs is the targeted removal of specific knowledge while preserving all other capabilities, critical for privacy and safety. Yet existing benchmarks measure it unreliably. They miss knowledge that resurfaces under paraphrased or indirect queries, a failure we call under-forgetting, and lack the semantic, syntactic, and lexical probes needed to verify that unrelated knowledge is preserved, a failure we call over-forgetting. Both failures reflect an asymmetric generalization 
- arxiv:2402.05445 · 2024-02-08 · preprint · sim 0.47 · hf
  Accurate LoRA-Finetuning Quantization of LLMs via Information Retention
  The LoRA-finetuning quantization of LLMs has been extensively studied to obtain accurate yet compact LLMs for deployment on resource-constrained hardware. However, existing methods cause the quantized LLM to severely degrade and even fail to benefit from the finetuning of LoRA. This paper proposes a novel IR-QLoRA for pushing quantized LLMs with LoRA to be highly accurate through information retention. The proposed IR-QLoRA mainly relies on two technologies derived from the perspective of unifie

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

