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
 "Name": "success_filter_lockin_under_shift",
 "Title": "Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights",
 "Short Hypothesis": "When an agent stores only its own successes, a hidden rule change couples the read and write sides of its memory: stale items suppress post-shift successes on the shifted task types, fewer successes mean fewer fresh items, and the stale share of the store stays high. We claim that this loop produces a practical lock-in for an unbounded retrieval bank (no recovery within 400 post-shift episodes in most stream seeds), because top-k retrieval is winner-take-all over the stale share, whereas a continual QLoRA fed by the same success filter recovers without help in every seed, because a single chunk of fresh successes flips its graded prior; the loop disappears in both substrates when the writer is an exogenous expert, and the exogenous refresh dose needed to break it is larger for the bank than for the LoRA.",
 "Related Work": "Closest: Live-Evo (2602.02369) keeps an online memory robust under true shift by decaying stale experiences from feedback, but has no parametric arm and a single live run, and does not ask what happens to a success-only writer without decay. RoMeRL (2608.02508) names a memory-reward trap in which co-retrieved memories receive misleading utility updates, on stationary benchmarks. Escaping the Self-Confirmation Trap (2606.24428) fixes self-confirmatory experience construction with heterogeneous agents, without a rule change or a weights arm. Zombie Agents (2602.15654) shows self-reinforcing memory content persisting, framed as an attack. When Continual Learning Moves to Memory (2604.27003) supplies the retrieval-competition mechanism without a write-policy loop. HarnessEvolve (2609.00829) gates self-evolution with reference trajectories, which is one form of the exogenous refresh we dose. Archived: collection_policy_coupling_collapse (round 1) concerns coupling between what is collected and what is read on a stationary task set; opposite_sided_failure_under_shift asserted a definitional failure side.",
 "Abstract": "Self-evolving agents write their successes into a store and read from it on the next task; the literature treats staleness as an item-level property to be detected or decayed. We argue and test that under a hidden rule change staleness becomes a dynamical property of the whole loop: stale items lower the success rate on the shifted types, which starves the store of the fresh items that would displace them. On Qwen3-32B in ALFWorld with a manufactured hidden rule change (heating moves from microwave to stoveburner, cleaning to a new verb, other types untouched, one type held out), we run paired streams of 150 pre-shift and 400 post-shift episodes in which each arm collects its own successes: unbounded bank, FIFO bank, failure-decayed bank, continual QLoRA, replay QLoRA, and a memory-free explorer that writes but never reads. We measure on-stream recovery of shifted-type success, the stale share of the retrieved set, lock-in frequency across stream seeds, and the minimum dose of exogenous expert post-shift items (with a relevance-destroyed placebo at the same rate) that breaks the loop in each substrate. An expert-writer control removes the success filter and is predicted to remove lock-in in every arm. Costs are reported as cumulative injected tokens and chunk-training GPU-hours, and every trained arm is evaluated memory-free, with matched and with mismatched memory at the end of the stream.",
 "Experiments": "- E0 Gate 0 (expert pool, rule B): success rate on shifted types with k=3 all-stale items (s_stale) vs k=0 (s_0) vs k=3 all-fresh; the loop is only testable if s_stale is at least 15 net points below s_0; the required fresh-item count for a stale share <= 1/3 in the top-3 is computed from the pre-shift store size and pre-registered as the lock-in prediction.\n- E1 Paired self-collection streams: 150 pre-shift episodes under rule A (one shared collection copied into every arm's store or training set), then 400 post-shift episodes under rule B with 50 % shifted-type sampling, identical task order and sampling seeds across arms, 3 stream seeds. Arms: unbounded bank (k=3), FIFO bank N=150, failure-decayed bank, continual QLoRA (chunk update after every 50 new successes), replay QLoRA (all past successes replayed 1:1), explorer (k=0, writes successes to a store nobody reads).\n- E2 Metrics on-stream: shifted-type success per 100-episode window (paired by task sequence), stale share of the top-3 retrieved (bank arms) or fresh fraction of the last training chunk (LoRA arms), time to recovery (first window at or above s_0 plus half the all-fresh k=3 gain), and lock-in indicator (no recovery by episode 400).\n- E3 Exogenous refresh ladder: expert post-shift items appended to the store or chunk at 1 % and 10 % of stream episodes, with a relevance-destroyed placebo at the same rate; arms: unbounded bank, decayed bank, continual QLoRA; 3 seeds; escape dose = smallest rate with recovery in >= 2 of 3 seeds.\n- E4 Expert-writer control: the same streams with the expert supplying every post-shift item (no success filter) for the unbounded bank and the continual QLoRA, 2 seeds: predicted to recover by displacement arithmetic and by one fresh chunk respectively.\n- E5 End probes: 274 validation games x 2 seeds under rule B; LoRA arms with memory absent, matched memory (successes from the explorer's store, disjoint items) and token-matched mismatched memory; bank arms with their own store; unshifted in-stream types and the held-out type as the off-stream probe; positive control that a QLoRA trained on the pre-shift successes exhibits the stale procedure under rule B.\n- E6 Cost curves: cumulative injected tokens (about 430 per k=3 episode) and chunk-training GPU-hours per arm against shifted-type success through the stream; Pareto plot at recovery.",
 "Baselines and Ablations": "- Explorer (k=0 writer) is the write-side reference: what the store would receive without read-side harm; a decoy-k=3 explorer (irrelevant items of matched length) checks that its base rate is not a prompt-length effect.\n- FIFO bank N=150 is the eviction reference (escape by volume) and N=450 the ablation.\n- Failure-decayed bank tests whether a read-side utility rule (Live-Evo style) breaks the loop without exogenous items; two decay constants pre-registered.\n- Replay QLoRA vs continual QLoRA: does parametric retention of pre-shift successes reintroduce lock-in on the weights side.\n- Expert-writer control isolates the success filter as the cause of lock-in versus pure retrieval competition.\n- Placebo refresh (relevance-destroyed items at 1 % and 10 %) separates content from volume; in FIFO it is expected to help by eviction and is reported as such.\n- Bank-vs-target partition: LoRA arms never train on items that any bank arm retrieves; the matched-memory end probe uses the explorer's store, whose items are disjoint from every LoRA's training set.",
 "Falsifiable Predictions": "- P1 Unbounded bank locks in (no recovery by episode 400) in >= 2 of 3 seeds and its top-3 stale share stays >= 0.66 throughout in those seeds; falsified if it recovers in >= 2 seeds (the agent self-corrects enough to refresh the store).\n- P2 Continual QLoRA recovers in 3 of 3 seeds within 400 episodes and within 2x the FIFO bank's recovery time; falsified if it also locks in (then lock-in is a property of the success filter regardless of substrate, itself reportable).\n- P3 Expert-writer control shows no lock-in in any arm: the unbounded bank recovers within the displacement count computed at E0 and the LoRA within two chunks; falsified if the unbounded bank still locks in with an exogenous writer (cause is retrieval competition alone).\n- P4 Escape dose: the unbounded bank needs >= 10 % exogenous items, the continual QLoRA escapes at 1 %; placebo items do not release the unbounded bank.\n- P5 Failure-decayed bank escapes without exogenous items in >= 2 of 3 seeds; otherwise the decay constants are reported as insufficient for this shift.\n- P6 At stream end, the recovered LoRA's memory-free success on shifted types is within 10 net points of the all-fresh k=3 reference, and unshifted and held-out types are within 5 net points of the pre-shift level for every arm except the FIFO bank, whose unshifted gain drops with eviction share.",
 "Measurement and Noise Control": "All arms run the identical post-shift task sequence and sampling seeds, so window-level success differences are paired by episode; with 50 % shifted-type sampling a 100-episode window holds about 50 shifted episodes, giving about +/-14 points per window per seed, which resolves the lock-in contrast (s_stale near 0.1-0.2 vs recovered near 0.7) but not fine differences, so recovery time is estimated from a monotone fit over windows and bootstrapped over episodes and the 3 stream seeds. Gate 0 fixes the effect size the design must resolve: s_0 minus s_stale >= 15 net points on the 95 validation shifted games plus a 100-task reserve at 2 seeds (about +/-9). Lock-in is a binary per-seed outcome and is reported as counts with the recovery curves as the primary quantitative evidence; the pre-registered decision rule for P1/P2 is the sign of the paired difference in mean window success over the last 200 episodes, with CI. End probes use the paired 274-game x 2-seed cell (+/-8). Budget: about 23,000 episodes plus under 5 GPU-hours of chunk training, about five days on two A100s, staged so that E3 and E4 run only if Gate 0 passes.",
 "Preprint Collision Check": "- Q1 (mechanism, --recent, s2cli = S2 + HF): 'self-evolving agent memory distribution shift success-only writes feedback loop stale experience lock-in' -> 2609.00829 HarnessEvolve, 2608.02508 RoMeRL (memory-reward trap, stationary), 2606.24428 EDV (self-confirmation trap in experience construction, no shift, no weights arm), 2606.17628 OPD-Evolver, 2606.00619 MemPro, 2602.02369 Live-Evo, 2601.18226, 2512.18746 MemEvolve; none constructs a shift-triggered write-starvation loop or compares substrates.\n- Q2 (closest method, --recent, s2cli): 'online self-evolving memory experience reweighting decay distribution shift agent' -> 2602.02369 Live-Evo confirmed (decay of stale experiences from feedback, no parametric arm), 2607.29468 SESA, 2606.17628, 2602.15654 Zombie Agents (self-reinforcing stored content, security framing), 2608.02508, 2512.18746; none doses exogenous refresh or reports lock-in frequency.\n- Q3 (--recent, s2cli): 'nonstationary environment rule change LLM agent memory adaptation ALFWorld TextWorld' -> 2606.30639 WorldEvolver, 2606.05684 AdaMEM, 2603.07392 OAKS, 2602.02369, 2508.16153 AgentFly, surveys 2507.21046 and 2501.07278; no hidden rule change on ALFWorld with both substrates.\n- WebSearch unavailable in this session and not used. No collision with the success-filter lock-in claim, the expert-writer control or the escape-dose estimand.",
 "Risk Factors and Limitations": "If the agent explores after a failed heat attempt and succeeds often enough (s_stale close to s_0), the loop is weak and the study reports a bounded null; the fallback is the stronger hidden shift (inert receptacle echoes success). Lock-in frequency is estimated from only 3 stream seeds per arm, so the binary claims are coarse and the recovery curves carry the evidence. The stale prior in the LoRA may be too weak after 150 pre-shift episodes (few shifted successes) to produce any harm, which the positive control detects; then pre-shift phases are lengthened. Chunked continual QLoRA with vLLM re-serving costs about 3 minutes per chunk; with 8 chunks per seed and 3 seeds this is manageable but serializes the LoRA arms. The 50 % shifted-type sampling makes the stream unrepresentative of ALFWorld's natural mix and is a power choice, stated as such. The failure-decayed bank is our implementation, not Live-Evo. Results are for Qwen3-32B, MiniLM goal-sentence retrieval and one manufactured shift; a second environment is out of budget."
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

Proposal: success_filter_lockin_under_shift — Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights

- arxiv:2608.04003 · 2026-08-04 · preprint · sim 0.65 · hf
  PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-
- arxiv:2607.10526 · 2026-07-14 · preprint · sim 0.63 · hf
  Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents
  Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills. This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original conversation is gone. We call this persistent sycophancy and introduce the Personal Agent Sycophancy Benchmark (PASB), a 1,600-task benchmark that traces whether a conversa
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.13396 · 2026-07-15 · preprint · sim 0.57 · hf
  Set-shifting Behavioral Test for Harnessed Agents
  What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. Our benchmark mounts tool-skill libraries with redundancies, where many tools solve the same task but differ in hidden reliability. In our evaluation framework, a branched schedule shifts the reliable tool group at hidden boundaries and pairs every shift with a no-shift control. 
- arxiv:2606.06448 · 2026-06-04 · preprint · sim 0.56 · hf
  Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
  LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza
- arxiv:2606.17591 · 2026-06-16 · preprint · sim 0.55 · hf
  Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning
  Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic for
- arxiv:2608.18852 · 2026-08-19 · preprint · sim 0.54 · hf
  SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
  Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve
- arxiv:2605.26252 · 2026-05-25 · preprint · sim 0.53 · hf
  Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory
  Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and
- arxiv:2608.26730 · 2026-08-27 · preprint · sim 0.51 · hf
  Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training
  Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, 
- arxiv:2412.17256 · 2024-12-23 · preprint · sim 0.49 · hf
  B-STaR: Monitoring and Balancing Exploration and Exploitation in
  Self-Taught Reasoners
  In the absence of extensive human-annotated data for complex reasoning tasks, self-improvement -- where models are trained on their own outputs -- has emerged as a primary method for enhancing performance. However, the critical factors underlying the mechanism of these iterative self-improving methods remain poorly understood, such as under what conditions self-improvement is effective, and what are the bottlenecks in the current iterations. In this work, we identify and propose methods to monit

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

