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
 "Name": "stale_dose_law_context_vs_weights",
 "Title": "Entry-Gated or Majority-Gated: The Dose Law of Outdated Experience Read from Context versus Trained into Weights",
 "Short Hypothesis": "After a hidden rule change in ALFWorld, the same outdated experience items harm the agent under two different dose laws. Read from context at fixed k=3 and fixed injected tokens, harm is entry-gated: one stale item among three realizes at least 60 % of the all-stale harm and the harm depends on the stale item's position. Trained into a QLoRA from a p-stale mix of fixed size, harm is majority-gated under greedy decoding (at most 25 % of the all-stale harm at p=0.25, at least 75 % at p=0.75) and becomes proportional to p under temperature sampling. The stream consequence is that a retrieval bank recovers only when stale items are displaced from the top-k almost entirely, whereas a LoRA recovers as soon as fresh data is the majority of what it was last trained on; the two fitted laws must predict, within CI, the recovery times of an unbounded bank and a continual LoRA on a 400-episode expert stream.",
 "Related Work": "Closest: The Compliance Trap (2607.10608) shows agents adopt conflicting retrieved memory at the first exposed decision point with weak recovery, but only in context, without a dose ladder at fixed tokens, without position manipulation, and without the arm that trains the same conflicting material into weights (its own stated open question). When Continual Learning Moves to Memory (2604.27003) re-frames stability-plasticity as retrieval competition between old and new items but has no weight-update arm. Controlled Memory Interference (2608.07622) is a memory-only diagnostic of interactions among accumulated experiences. STALE (2605.06527) and When Memory Lies (2608.04574) study whether agents detect stale personalized or spatial memories, not the harm-per-item law or its parametric counterpart. Information abundance (2608.12218) concerns train-time context volume on documents, not conflicting items in trajectories. Live-Evo (2602.02369) decays stale experiences from feedback without measuring how much one stale item costs. Archived program ideas: opposite_sided_failure_under_shift (definitional headline, rejected), harm_does_not_distill (equivalence margin larger than the harm; asymmetric-filter framing).",
 "Abstract": "Experience stored by an agent goes stale when the environment's rules change, and the two places that experience can live, the prompt and the weights, are assumed to fail differently, but the assumption has never been measured with the same stale material on the same backbone. We manufacture a hidden rule change in ALFWorld (heating works only at the stoveburner and cleaning only via a new verb; the rule is not announced and is learnable only from experience) so that every pre-shift expert item for the heat and clean procedures becomes a wrong procedure. We then measure two dose-response curves on Qwen3-32B with one partitioned expert pool: the in-context curve, where d of k=3 retrieved items are stale at fixed injected tokens, with stale-item position and a relevance-destroyed decoy as controls; and the parametric curve, where five QLoRA students of identical data size are trained on p-stale mixes and evaluated memory-free, with matched fresh memory, and with token-matched mismatched memory. We test a specific pair of laws, entry gating in context and majority gating in weights under greedy decoding, with a temperature ablation that distinguishes a mixture-policy account from an attention account, and we test whether the fitted laws predict recovery times on a single-shift expert stream for an unbounded bank and a continual LoRA. All arms are reported on one cost axis (GPU-hours plus per-episode tokens) with pre-registered gates tied to the measured stale harm.",
 "Experiments": "- E0 Gate 0 (expert pool, rule B active on the 274 validation games plus a 200-task reserve of shifted-type train tasks held out of every bank and target partition): k=3 with 3/3 pre-shift items vs 3/3 post-shift items on the heat and clean types must differ by >= 15 net points, else the shift is strengthened (inert receptacle echoes a success message so no in-episode cue exists) and Gate 0 is re-run; if it still fails the claim is declared untestable.\n- E1 In-context dose ladder: k=3, d in {0,1,2,3} stale items of matched length drawn from the bank partition (odd task indices), position arms for d=1 (stale first vs last) and d=2, decoy arm (d=1 with the stale item replaced by a relevance-destroyed item of the same length), k=0 reference; 2 seeds on all cells, 3 seeds on d in {0,1,3}.\n- E2 Parametric dose ladder: five QLoRA students (nf4, rank 32, one epoch, identical data size = 30 % of the target partition, even task indices, about 2,700 step examples, ~0.6 GPU-h each) at p in {0, 0.25, 0.5, 0.75, 1} stale; evaluated under rule B with memory absent, matched fresh memory (k=3 post-shift items from the bank partition), and mismatched memory (token-matched items from other task types); greedy decoding as in Step 0.\n- E3 Decoding ablation: temperature 0.7 for the p in {0.25,0.5,0.75} students (memory absent) and for the in-context d in {1,2} cells; the mixture-policy account predicts linearization of the parametric curve only.\n- E4 Stream validation: 300 rule-A expert episodes then 400 rule-B expert episodes on train tasks; arms: unbounded bank at k=3 and continual LoRA (chunk update every 100 target-partition items, no replay); shifted-type probe on the reserve every 100 items; recovery times compared with the values predicted from the E1/E2 laws plus the stale-share arithmetic (hypergeometric draw of d stale among top-3 given counts; fresh fraction of the last chunk for the LoRA).\n- E5 Own-rollout pool replication of E1 (d in {0,1,3}) and E2 (p in {0,0.5,1}) once the on-policy pool is complete; post-shift own items are collected under rule B by the k=0 agent.\n- E6 Reporting: shifted types (heat, clean), unshifted in-stream types (cool, pick_and_place, look_at) as the off-stream erosion probe for the students, and pick_two_obj_and_place held out of every bank and target partition as the procedure-held-out probe; cumulative cost (GPU-hours, tokens) and a Pareto plot for every arm.",
 "Baselines and Ablations": "- k=0 under rule B and k=3 all-fresh (d=0): the two anchors of the in-context curve.\n- Decoy at d=1 (irrelevant item, same length): separates conflict harm from irrelevance harm; volume is constant across the ladder by construction.\n- Fresh student (p=0) and base model: anchors of the parametric curve; stale student (p=1) is the positive control and must show the stale procedure (harm >= Gate 0 threshold) before any weights-side claim is made.\n- Data-size ablation at p=0.5 (10 % vs 30 % of the target partition) to check the majority threshold is not a data-size artefact.\n- Bank-partition swap (items from the other half) to check the in-context law is not item-specific.\n- Visible lexical relabel (microwave shown and addressed as heatingunit) as a secondary shift: the entry-gating prediction is expected to weaken when the observation contradicts the item, which is reported as a boundary condition.\n- No context-distillation arm is used, so P-CD0 is not required; SFT on trajectories is the only objective.",
 "Falsifiable Predictions": "- P1 In context, f1 = H(d=1)/H(d=3) >= 0.6 and stale-first exceeds stale-last by >= 8 net points on the shifted types; falsified by f1 <= 0.4 or no position effect (the agent averages over items).\n- P2 In weights under greedy decoding, H(p=0.25)/H(1) <= 0.25 and H(p=0.75)/H(1) >= 0.75, with the 0.25-to-0.75 interval carrying >= 50 % of the total harm; falsified by a linear curve or by a jump concentrated at p <= 0.25 (weights as brittle as context).\n- P3 At temperature 0.7 the parametric curve's linear fit improves and its step statistic halves, while the in-context curve keeps its shape; falsified if the in-context curve linearizes as well.\n- P4 Matched fresh memory (k=3) rescues the p=1 student to within 10 net points of the fresh student; a rescue below 50 % of the gap is reported as a crutch-like prior dominating context.\n- P5 Decoy harm at d=1 is less than one third of the stale-item harm at d=1.\n- P6 On the stream, the unbounded bank's time to 90 % of the all-fresh k=3 accuracy on shifted types exceeds the continual LoRA's by at least 2x, and both observed recovery curves fall inside the bootstrap band predicted from the fitted laws; falsified if the bank recovers as fast as the LoRA or the predictions miss by more than the band.",
 "Measurement and Noise Control": "Every cell is paired over identical (game, seed) across arms; the primary metric is net fixed-minus-broken per 100 on the shifted types with paired bootstrap CIs over games. Power: the Step-0 paired cell of 274 games x 2 seeds gives about +/-8 net points; the shifted-type subset of the validation games (about 95 games) plus the 200-task reserve gives about 300 games x 2 seeds = 600 pairs, i.e. roughly +/-7.5 net points, and 3 seeds on the shape-defining cells bring the MDE for a difference between two dose levels to about 8 net points. Gate 0 requires total stale harm >= 15 net points so that a 60 % vs 40 % split of the harm (P1) and the quartile thresholds (P2) are resolvable; shape statistics (f1, quartile ratios, step statistic) are pre-registered with their thresholds and computed by paired bootstrap. Decoding is fixed at the Step-0 setting for the confirmatory cells; the temperature ablation is a separate pre-registered contrast. The stream validation uses two stream seeds and reports recovery times by isotonic-fit crossing with bootstrap over probe games. If the positive control (p=1 student) does not exhibit the stale procedure, the weights-side law is declared unmeasurable at this data scale rather than flat.",
 "Preprint Collision Check": "- Q1 (mechanism, --recent, s2cli = Semantic Scholar + HF Papers): 'stale outdated retrieved memory harm LLM agent after rule change in-context versus fine-tuned dose' -> 2608.04574 When Memory Lies (spatial staleness in VLM navigation, no weights arm), 2605.06527 STALE (validity detection of personalized memories, QA), 2607.12893 MemOps, 2606.22844 RaMem, 2605.24941 tool drift, 2603.04549 A-MAC, 2308.08747 forgetting under continual FT; none runs a stale dose ladder at fixed tokens or the paired in-weights condition.\n- Q2 (closest method, --recent, s2cli): 'compliance trap conflicting retrieved memory LLM agent' -> 2607.10608 The Compliance Trap confirmed (trajectory-level diagnosis, in-context only), plus 2609.01836, 2606.25161 TrustMem, 2602.07398 AgentSys, 2603.04549; no parametric counterpart, no dose or position manipulation.\n- Q3 (--recent, s2cli): 'external memory stability plasticity retrieval competition continual learning LLM agents' -> 2608.07622 Controlled Memory Interference (memory-only diagnostic; id verified with s2cli paper), 2604.27003, 2607.13591 MemCon, 2606.06448, 2603.18718; none with a weight-update arm on the same stream.\n- WebSearch was not available in this session and was not used; no result matches the two-substrate dose law or the stream prediction test.",
 "Risk Factors and Limitations": "The agent may self-correct after 'Nothing happens' at the inert receptacle, making stale harm small; the fallback shift removes the cue by echoing success messages, at the cost of a less natural regime. Mixed-label SFT (p near 0.5) may degrade format adherence rather than express a mixture policy; unshifted-type accuracy is monitored to catch this. The majority-gating claim is tied to greedy decoding; the temperature ablation is essential and results are stated per decoding regime. The parametric ladder uses 30 % of the target partition to keep five students at about 3 GPU-hours total, so absolute harm sizes are not those of a full-pool student. On the own-rollout pool stale items are on-policy text and may be more persuasive, which is why the replication is reported separately. The stream validation is a single expert stream with one shift; laws fitted on validation games are applied to train-task probes, so the reserve split is the load-bearing safeguard. Results are specific to Qwen3-32B and ALFWorld's short procedures."
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

Proposal: stale_dose_law_context_vs_weights — Entry-Gated or Majority-Gated: The Dose Law of Outdated Experience Read from Context versus Trained into Weights

- arxiv:2606.02540 · 2026-06-01 · preprint · sim 0.46 · hf
  SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction
  Agent skills occupy a privileged position in the agent workflow, as agents are expected to implicitly follow and execute them, rendering third-party skills a vulnerable attack surface. Existing studies have revealed unsafe agent behaviors induced by skill-based attacks, but they primarily evaluate poisoned skills within a single task execution and enumerate harms through ad-hoc risk lists. To bridge these gaps, we introduce SkillHarm, a benchmark of skill-based attacks across the skill-use lifec
- arxiv:2410.13886 · 2024-10-11 · preprint · sim 0.39 · hf
  Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents
  For safety reasons, large language models (LLMs) are trained to refuse harmful user instructions, such as assisting dangerous activities. We study an open question in this work: does the desired safety refusal, typically enforced in chat contexts, generalize to non-chat and agentic use cases? Unlike chatbots, LLM agents equipped with general-purpose tools, such as web browsers and mobile devices, can directly influence the real world, making it even more crucial to refuse harmful instructions. I
- arxiv:2603.15994 · 2026-03-16 · preprint · sim 0.39 · hf
  Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving
  Retrieval-augmented generation stores all content indiscriminately, degrading accuracy as noise accumulates. Parametric approaches compress knowledge into weights, precluding selective updates. Neither mirrors biological memory, which gates encoding based on salience and archives rather than deletes superseded information. We introduce write-time gating that filters incoming knowledge objects using composite salience scores (source reputation, novelty, reliability) while maintaining version chai
- arxiv:2608.02276 · 2026-08-03 · preprint · sim 0.38 · hf
  Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories
  Agents built around large language models continually accumulate interaction trajectories during deployment, yet their behavior typically remains fixed. Beyond updating model weights, these trajectories can improve the agent harness that constructs context, mediates tools, validates actions, and recovers execution. We introduce Harness-R1, the first method, to our knowledge, that makes failure-conditioned, lifecycle-wide editing of an existing executable runtime a learned capability. It post-tra
- arxiv:2506.00641 · 2026-01-31 · preprint · sim 0.37 · hf
  AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents
  Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents' step-by-step actions, overlook subtle meanings, fail to see how small issues compound, and get confused by unclear safety or security rules. To overcome this evaluation crisis, we introduce AgentAuditor, a universal, training-free, memory-augmented reasoning framework that empowers LLM ev
- arxiv:2605.05413 · 2026-05-06 · preprint · sim 0.36 · hf
  From History to State: Constant-Context Skill Learning for LLM Agents
  Large language model (LLM) agents are increasingly used to operate browsers, files, code and tools, making personal assistants a natural deployment target. Yet personal agents face a privacy-cost-capability tension: cloud models execute multi-step workflows well but expose sensitive intermediate context to external APIs, while local models preserve privacy but remain less reliable. Both settings also pay repeatedly for long skill prompts and growing histories. We propose constant-context skill l
- arxiv:2605.10663 · 2026-05-11 · preprint · sim 0.35 · hf
  Evolving-RL: End-to-End Optimization of Experience-Driven Self-Evolving Capability within Agents
  Experience-driven self-evolving agents aim to overcome the static nature of large language models by distilling reusable experience from past interactions, thus enabling adaptation to novel tasks at deployment time. This process places substantial demands on the foundation model's capacities for abstraction, generalization, and in-context learning. However, most existing studies focus primarily on system-level design choices, such as how experience is represented and managed, neglecting the inhe
- arxiv:2412.14470 · 2024-12-19 · preprint · sim 0.35 · hf
  Agent-SafetyBench: Evaluating the Safety of LLM Agents
  As large language models (LLMs) are increasingly deployed as agents, their integration into interactive environments and tool use introduce new safety challenges beyond those associated with the models themselves. However, the absence of comprehensive benchmarks for evaluating agent safety presents a significant barrier to effective assessment and further improvement. In this paper, we introduce Agent-SafetyBench, a comprehensive benchmark designed to evaluate the safety of LLM agents. Agent-Saf
- arxiv:2503.04957 · 2025-03-06 · preprint · sim 0.34 · hf
  SafeArena: Evaluating the Safety of Autonomous Web Agents
  LLM-based agents are becoming increasingly proficient at solving web-based tasks. With this capability comes a greater risk of misuse for malicious purposes, such as posting misinformation in an online forum or selling illicit substances on a website. To evaluate these risks, we propose SafeArena, the first benchmark to focus on the deliberate misuse of web agents. SafeArena comprises 250 safe and 250 harmful tasks across four websites. We classify the harmful tasks into five harm categories -- 
- arxiv:2607.21419 · 2026-07-23 · preprint · sim 0.33 · hf
  PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning
  In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. However, they remain centered on the skills themselves rather than being designed as adaptive training-time support for the evolving policy. To address this, we propose a policy-centric training paradigm t

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

