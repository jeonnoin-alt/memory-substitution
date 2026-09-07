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
 "Name": "context_wins_substrate_conflict",
 "Title": "When Weights and Memory Disagree: Which Substrate an Agent Follows After a Rule Change, and What It Means for Hybrid Memory Under Shift",
 "Short Hypothesis": "In a hybrid, conflicts between a procedure trained into the weights and a procedure retrieved into context are resolved in favour of the context item regardless of which substrate is stale: after a manufactured procedure change, weights freshly trained on the new procedure do not reduce entry-point compliance with stale retrieved items, and fresh retrieved items fully repair stale weights; therefore the staleness of a hybrid under shift is governed by the bank's eviction policy, not by retraining, and recovery time in a post-shift stream is set by the bank's stale fraction rather than by the LoRA arm.",
 "Related Work": "The compliance trap (arXiv:2607.10608) shows untrained agents adopt task-wrong retrieved memory at the first exposed decision point with weak recovery, but never trains the correct procedure into the weights to see whether that changes compliance. STALE (arXiv:2605.06527) benchmarks whether agents notice invalid personal memories; knowledge-conflict work (arXiv:2506.06485) and CK-PLUG (arXiv:2503.15888) measure parametric-versus-contextual reliance in RAG QA with pretrained facts, not with procedures the experimenter trained in. UniMem (arXiv:2607.26017) consolidates recurring patterns into parametric memory and keeps sparse tasks episodic, and COVE (arXiv:2608.01234) routes between harness and parameter channels under changing environments; neither tests what happens when the consolidated pattern and a fresh episodic item disagree, nor costs it. Continual-learning-as-retrieval (arXiv:2604.27003), AgentCL (arXiv:2606.02461) and OAKS (arXiv:2603.07392) evaluate only non-parametric memories on streams; FOREVER (arXiv:2601.03938), Agent-Dice (arXiv:2601.03641) and self-generated replay (arXiv:2605.26097) only weights; Do Self-Evolving Agents Forget (arXiv:2605.09315) documents erosion across channels without a head-to-head; faulty consolidation (arXiv:2605.12978) and insight governance (arXiv:2606.17591) report negative transfer of updated memories. In this program, opposite_sided_failure_under_shift (round 2) asserted the definitional version (append-only banks cannot forget, post-shift-only LoRAs cannot retain) and was rejected; stale_true_state_facts_redaction and coverage_currency_coupling concern stale facts and currency within the context channel only.",
 "Abstract": "Hybrid memory systems assume that consolidating experience into weights buys robustness and that keeping items in context buys currency. Neither assumption has been tested at the point where they collide: the moment weights and retrieved memory prescribe different procedures for the same task. We manufacture that collision on ALFWorld with a wrapper-level rule change that inserts a new precondition step (an 'activate' action before heat, cool and clean), regenerate the expert pool under the new rule, and build the four combinations of stale/fresh weights (QLoRA on pre- or post-rule targets) and stale/fresh context (k=3 items from the pre- or post-rule bank), plus no-weights, no-context and decoy cells, with a randomized stale-dose ladder inside the retrieved set at fixed k and tokens. The estimands are entry-point compliance, recovery and success on the shifted task types, with pick-and-place types as an off-stream probe. The claim is behavioural, not definitional: fresh weights could override stale context (prior imprinting) or stale context could override fresh weights (context dominance), and Gate 0 requires that stale context harms the untrained agent by at least 6 net points and that post-rule weights alone recover at least 15. A secondary symmetric stream (bounded evicting bank, unbounded bank, continual LoRA, reset LoRA, LoRA with self-generated replay) measures recovery time and off-stream erosion under each arm at accounted GPU-hours and tokens. The result decides a routing question no hybrid paper has costed: whether, after a shift, the useful lever is retraining or eviction.",
 "Experiments": "Environment: ALFWorld train/valid games behind a command wrapper. Pre-rule = standard game. Post-rule: heat, cool and clean commands return 'Nothing happens.' unless the agent has issued 'activate <receptacle>' for that appliance earlier in the episode; 'activate' is added to the admissible commands; pick_and_place_simple and pick_two_obj types are untouched (off-stream probe). The three shifted types are the multi-step types where in-context gain is +39 to +55. Pools: E_pre = the 1,465 expert walkthroughs; E_post = the same walkthroughs with 'activate <receptacle>' inserted before each heat/cool/clean step (programmatic edit, verified by replay to success under the post rule). Partition both identically by task id into T targets (55%), B bank (35%), H (10%). Weights: W_none; W_pre = QLoRA SFT on T of E_pre; W_post = QLoRA SFT on T of E_post (~1.1 GPU-h each, 2 epochs); W_reset is W_post by construction; W_cont = W_pre further trained on T of E_post (continual). Context: C_none; C_pre = k=3 from B of E_pre; C_post = k=3 from B of E_post; C_decoy = relevance-destroyed, length matched. All post-rule evaluation. Step 1, Gate 0 (untrained agent, shifted types, both splits, ~270 games x 3 seeds per cell): (a) success(C_pre) <= success(C_none) - 6 net (stale context harms); (b) success(C_post) >= success(C_none) + 15 (fresh context helps); (c) success(W_post, C_none) >= success(W_none, C_none) + 15 (weights encode the new step); (d) k=0 discovery rate of 'activate' <= 20% success (the shift is real). If (a) fails, strengthen the rule (activation required after the object is placed in the appliance) and re-gate once; if still failing, declare the conflict claim untestable here and report Gate 0. Step 2, conflict factorial: W in {none, pre, post, cont} x C in {none, pre, post, decoy} on shifted types, ~270 games x 3 seeds per cell (16 cells, ~13k episodes), off-stream probe types in every cell at 2 seeds. Per episode log: entry-point action at the first heat/cool/clean decision (follows context procedure, follows weights procedure, other), recovery (activate issued after a failed attempt) and steps to recovery, success, tokens. Step 3, stale-dose ladder: for W in {none, post} at k=3 with s in {0,1,2,3} stale items among the three (randomized per episode, items length matched), ~270 x 3 seeds per rung; estimand: slope of entry-point compliance and success in s, by weights arm. Step 4, symmetric stream (secondary): 600 post-rule train tasks from T of E_post and H in three blocks of 200, agent's own successes appended to its bank as they occur (seeded with 20 post-rule expert items if the k=0 discovery rate at Gate 0d is below 5%); arms: unbounded bank with W_pre; bounded FIFO bank (capacity 200) with W_pre; continual LoRA (retrained on own post-rule successes at the end of each block, ~0.3 GPU-h) with bounded bank; reset LoRA (post-only) with bounded bank; continual LoRA with self-generated replay of off-stream types with bounded bank; W_none with bounded bank. Measure per block: shifted-type success, off-stream probe success, stale fraction of the retrieved set, block of recovery to 80% of the (W_post, C_post) ceiling, cumulative GPU-hours and tokens. Both A100s: one serves, the other trains the next LoRA; stream arms interleaved.",
 "Baselines and Ablations": "Single-substrate arms at matched cost: (W_none, C_post) all-context fresh; (W_post, C_none) all-weights fresh; and their stale counterparts. Placebo: C_decoy (length without relevance) crossed with every weights arm, to show that any protective effect of weights is not simply ignoring a long prefix. Manipulation checks as Gate 0 (a)-(d). Positive control for the dispositional reading: C_post with W_none must induce the new step (entry-point 'activate' rate >= 60%) so that 'context is followed' is demonstrated before 'context is followed even against weights' is claimed. Ablations: W_cont versus W_post (does a residue of the old procedure in the weights raise compliance with stale context?); stale-dose slope by weights arm; k=1 conflict cells (single stale item) to check that dominance is not a majority-of-items effect; a critique-prompt variant (instruct the agent to verify memory against observations) as an in-context defence, reported for cost. Off-stream probe types in every cell separate erosion from relabeling.",
 "Falsifiable Predictions": "P1 (context dominance): entry-point compliance with stale context under fresh weights is not lower than under no weights by more than 10 points, CDI(W_post, C_pre) >= CDI(W_none, C_pre) - 10, and success(W_post, C_pre) <= success(W_post, C_none) - 6 net (fresh weights do not protect against stale context); prior imprinting, CDI falling by >= 25 points and success(W_post, C_pre) within 5 of success(W_post, C_none), falsifies it. P2 (fresh context repairs stale weights): success(W_pre, C_post) >= success(W_none, C_post) - 5 and >= success(W_pre, C_none) + 15. P3 (dose ladder): the slope of success in stale fraction s is negative for both W_none and W_post and the two slopes differ by less than 40% of the W_none slope; if W_post flattens the slope by more than 60%, weights are a defence. P4 (residue): W_cont shows compliance with stale context at least as high as W_post; if W_cont > W_post by >= 10 points, old-procedure residue in the weights amplifies stale-context compliance (co-dominance), reported as a partial falsification. P5 (stream): recovery block is determined by the bank arm: bounded bank arms recover by block 2 regardless of LoRA arm, the unbounded bank lags by >= 1 block even with continual LoRA; reversal (LoRA arm decides recovery) falsifies. P6 (erosion, symmetric): continual LoRA without replay loses >= 5 net on the off-stream probe by block 3 while reset LoRA and bank arms do not; replay removes the loss; if no arm erodes, the 'both erode' hypothesis is rejected on this stream and reported. P7 (cost): the eviction lever costs zero GPU-hours and the same tokens as the unbounded bank; retraining costs >= 0.3 GPU-h per block; the Pareto plot shows whether any retraining arm beats eviction at any stream length.",
 "Measurement and Noise Control": "Paired (game, seed) design across all cells on the same shifted-type games; net/100 per pair; cluster bootstrap over games; 3 seeds on every conflict and ladder cell (shifted types pooled over both splits, ~270 games x 3 seeds, ~+/-6.5 net points for a paired contrast; per-type ~+/-13), 2 seeds for off-stream probes and stream blocks. Entry-point compliance is a per-episode binary with a deterministic detector (first heat/cool/clean decision without a preceding activate); detector validated on 100 hand-checked episodes before the confirmatory run. MDE stated before confirmation: 6 net points for success contrasts, 10 points for compliance contrasts, 40% slope ratio for P3. Gate 0 thresholds (6/15/15/20) are pre-registered as fractions of the measured in-context gain on multi-step types (about 0.15 and 0.35 of +40). Equivalence margins are fractions of the Gate-0 effect, never a fixed 3 points. Stale-dose assignment randomized per episode with the seed logged; item lengths matched within 5%; retrieval by the same MiniLM query in all cells; wrapper, prompt, decoding temperature and vLLM version pinned; evaluation order interleaved across cells. Stream arms use identical task order and seeds; recovery block reported with bootstrap CI over games within block.",
 "Preprint Collision Check": "All searches via the literature command (s2cli: Semantic Scholar + HuggingFace Papers, both 'ok'); WebSearch not used (quota exhausted this session); WebFetch never used. Q1 (mechanism, --recent): 'agent follows stale retrieved memory over fine-tuned knowledge conflict parametric versus contextual after environment rule change' -> 2607.10608 (compliance trap), 2606.17591 (insight governance in verbal RL), 2605.18565 (MINTEval), 2605.06527 (STALE), 2601.11653, 2506.06485 (knowledge conflict), 2503.15888 (CK-PLUG); the QA papers measure parametric-versus-contextual reliance for pretrained facts and none trains a procedure into an agent and then conflicts it with retrieved memory. Q2 (closest method, --recent): 'self-routing episodic buffer parametric memory consolidation recurring tasks stability plasticity agent stream' -> 2607.26017 (UniMem), 2607.03726 (SelfMem), 2606.02461 (AgentCL), 2605.31557, 2605.12978 (faulty consolidation), 2605.13438 (Cognifold), 2604.27003, 2605.20189 (SOLAR); none evaluates consolidated-versus-episodic conflict or a stale-dose ladder, and none costs eviction against retraining. Q3 (--recent): 'knowledge conflict fine-tuned agent versus retrieved memory which wins' -> 2607.10608, 2603.07670 (survey), 2601.02151 (entropy-adaptive fine-tuning), 2506.06485; no agent-level result. Verdict: no collision; the compliance trap (in the digest) is the mechanism source and leaves the trained-weights arm explicitly untested.",
 "Risk Factors and Limitations": "The manufactured rule is a wrapper-level precondition, so the shift is synthetic; a stronger variant is pre-registered but if Gate 0 fails twice the claim is declared untestable on ALFWorld rather than weakened. The k=0 agent might discover 'activate' from the admissible-command list, shrinking the stale-context harm; Gate 0d checks this, and the admissible list can be withheld from the prompt as a pre-registered amendment. Ceiling on fresh-fresh cells limits P2's upper contrast; reported with timeouts. The stream is short (600 tasks) and the LoRA retraining cadence coarse, so recovery times are block-resolved only; longer streams are out of this round's budget. Context dominance, if found, may be specific to procedures that appear as explicit action sequences in the items; abstract or compiled memories (guidelines) could behave differently and are not tested. Only one shift type is manufactured; an object-renaming shift is a possible second regime but not budgeted. Off-stream probe types are few (two), so erosion below ~7 net points is not resolvable. Self-rollout post-rule successes may be too sparse to build the stream bank without the 20-item seed, which is reported as part of the design."
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

Proposal: context_wins_substrate_conflict — When Weights and Memory Disagree: Which Substrate an Agent Follows After a Rule Change, and What It Means for Hybrid Memory Under Shift

- arxiv:2608.02508 · 2026-08-10 · preprint · sim 0.61 · hf
  RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
  Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory R
- arxiv:2608.04574 · 2026-08-05 · preprint · sim 0.59 · hf
  When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs
- arxiv:2608.15008 · 2026-08-15 · preprint · sim 0.58 · hf
  Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents
  Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and ac
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2601.11653 · 2026-01-15 · preprint · sim 0.55 · hf
  AI Agents Need Memory Control Over More Context
  AI agents are increasingly used in long, multi-turn workflows in both research and enterprise settings. As interactions grow, agent behavior often degrades due to loss of constraint focus, error accumulation, and memory-induced drift. This problem is especially visible in real-world deployments where context evolves, distractions are introduced, and decisions must remain consistent over time. A common practice is to equip agents with persistent memory through transcript replay or retrieval-based
- arxiv:2606.25449 · 2026-07-21 · preprint · sim 0.53 · hf
  Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One
  A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain. We call this brittle memory. The information loss is definitional; the finding is behavioral, and it turns on one thing, whether the memory kept a re-derivation basis (the source) rather than the answer. We
- arxiv:2601.07470 · 2026-01-12 · preprint · sim 0.53 · hf
  Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
  Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed desi
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.51 · hf
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2605.06527 · 2026-05-07 · preprint · sim 0.49 · hf
  STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?
  Large Language Model (LLM) agents are increasingly expected to maintain coherent, long-term personalized memory, yet current benchmarks primarily measure static fact retrieval, overlooking the ability to revise stored beliefs when new evidence emerges. We identify a critical and underexplored failure mode, Implicit Conflict: a later observation invalidates an earlier memory without explicit negation, requiring contextual inference and commonsense reasoning to detect. To rigorously evaluate this 
- arxiv:2606.25161 · 2026-06-23 · preprint · sim 0.49 · hf
  TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory
  Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content. Once stored, such errors become persistent system-state failures that can affect future reasoning and generation. In

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

