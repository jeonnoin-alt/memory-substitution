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
 "Name": "context_ceiling_substitution",
 "Title": "Does Training Still Add Anything Once the Memory Is Back? Substitution at the In-Context Ceiling and Retention-Routed Memory After Internalization",
 "Short Hypothesis": "After an experience pool is trained into Qwen3-32B (step-level QLoRA SFT or context distillation), putting the same pool back into context leaves the trained student no better than the untrained agent with that context: the marginal value of weights given context is about zero, so the residual value of context after internalization equals the un-retained part of the in-context gain, task type by task type (substitution, not additivity and not a crutch). Consequently a router that keeps memory in context only for task types whose gain the weights did not retain (chosen on a held-out train split) matches the full weights-plus-k=3 hybrid at a fraction of the injected tokens, whereas a random-type router and a decoy router at the same injection rate do not.",
 "Related Work": "Experience Distillation (arXiv:2607.21051) reports >=64.8% of the in-context gain retained memory-free but never evaluates the distilled student with the experience put back at matched tokens. SESA (arXiv:2607.29468) shows the bank retains +0.5-1.0 of value after internalization (QA/search, no seeds) but only measures the marginal value of context given weights, never the marginal value of weights given context. Skill0.5 (arXiv:2605.28424) keeps task-specific skills in context and internalizes general ones with a difficulty-aware router, uncosted and without single-substrate arms at matched tokens; SKILL0 (arXiv:2604.02268) withdraws skill context by curriculum without a keep-in-context arm; UniMem (arXiv:2607.26017), COVE (arXiv:2608.01234) and the substrate benchmark (arXiv:2608.15008) motivate routing but do not cost the decision or say where the residual value of context lives. Retrieval-augmented SFT (arXiv:2603.18272) trains the agent to use retrieved trajectories but does not test whether retrieval remains necessary. In-context distillation (arXiv:2512.02543) gives the only amortization analysis, for the frozen-student route only. DiSC (arXiv:2602.16093) and Doc-to-LoRA (arXiv:2602.15902) move context into parameters for documents, not agent trajectories. In this program, memory_in_the_loop_training_decomposition (round 2) attempted the train-by-infer 2x2 but its bank items were also SFT targets, so its own-bank-vs-swapped-bank drop measured memorization; substitutes_not_complements (round 1) concerned the memory-versus-instruction axis, not weights versus context; amortization_horizon_ranking_flip compared 8B and 14B backbones.",
 "Abstract": "Every internalization paper asks how much of the in-context gain survives in the weights; none asks the converse that a hybrid actually depends on: once the memory is back in context, do the trained weights add anything? We measure both marginals on one pool, one backbone and one cost axis. The 1,465 ALFWorld expert walkthroughs (and, as a replicate, the agent's own k=0 successes) are partitioned into disjoint target, bank and calibration sets. Students are trained on the target set by QLoRA SFT (at 10/30/100% of the targets), context distillation from a k=3-conditioned teacher, the P-CD0 empty-retrieval control, and SFT with k=3 memory in the prompt; two further arms hold one multi-step task type out of the targets (still in the bank) and out of both. Every student is evaluated memory-free, with matched k=3 memory from the bank, and with token-matched mismatched memory. The estimands are, per task type, the retained fraction r, the residual value of context given weights, and the value of weights given context. The substitution hypothesis predicts the hybrid sits on the untrained in-context ceiling (value of weights given context ~0, residual value = (1-r) x in-context gain, slope 1 across roughly 40 type-by-arm cells); additivity predicts a constant increment above it; the crutch predicts negative retention for memory-in-prompt training. We then cost the implied policy: a retention-informed type router built on the calibration split, against all-context (k=1,3,7), all-weights, full hybrid, random-type and decoy routers at the same injection rate, on a Pareto plot of accuracy versus training GPU-hours plus per-episode tokens with a cumulative-cost break-even.",
 "Experiments": "Setup: Qwen3-32B, thinking off, ReAct, vLLM one replica per GPU (QLoRA jobs run on the GPU not serving, so both A100s stay busy). Pool partition, stratified by task type over the 1,465 train tasks: T targets (55%, ~805 tasks; SFT/distillation targets), B bank (35%, ~510 tasks; the only retrievable items at train and test time), H calibration (10%, ~150 tasks; used for router selection and the low-noise NLL proxy, never for reporting). MiniLM retrieval on the goal sentence from B only. Step 1, Gate 0 (re-measure the in-context gain under the halved bank): untrained agent at k in {0,1,3,7} from B on valid_seen and valid_unseen (274 games x 3 seeds each, paired by (game, seed)); require pooled net gain at k=3 >= 15/100 and >= 25/100 on the three multi-step types, else the bank share is raised to 50% and Gate 0 re-run. Step 2, trained arms on the expert pool: (a) SFT-k0 on 10%, 30%, 100% of T (0.2-1.1 GPU-h per epoch, 2 epochs, checkpoint by held-out NLL on H); (b) CD-k3: one teacher pass at k=3 over T (~805 episodes), student trained on teacher outputs with an empty retrieval block; (c) P-CD0: identical with the teacher at k=0; (d) SFT-k3: SFT on T with k=3 items from B in the prompt (~2.7 GPU-h); (e) SFT-k0 with one multi-step type (pre-registered: cool-then-place) removed from T but kept in B (manufactured un-retained type); (f) SFT-k0 with the same type removed from T and from B (procedure-held-out generalization split). Step 3, evaluation of every trained arm in three prompt conditions: absent (k=0), matched (k=3 from B), mismatched (k=3 items of other task types, token-matched to within 5% of the matched injection); 274 x 2 splits x 3 seeds per condition at 100% pool, 2 seeds for the 10%/30% ladder, mismatched only at 100%. Step 4, estimands per (type t, arm a): g_t = untrained k=3 minus k=0; r_ta = (student k=0 minus untrained k=0)/g_t; residual value RV_ta = student matched minus student k=0; value of weights given context WV_ta = student matched minus untrained matched; slope and intercept of RV on (1-r)g across all cells by cluster bootstrap over games. Step 5, routers (untrained-agent cells are not needed; all routers deploy the SFT-k0 100% student and, as a second instance, the CD-k3 student): retention router injects k=3 from B only for types with r_t < 0.5 estimated on H (primary) or with the largest per-type memory-free NLL gap on H (secondary, low-noise); random-type router at the same injection fraction f; decoy router injecting relevance-destroyed items of the same length for the same types; full hybrid (k=3 for all types); all-weights; all-context k in {1,3,7}. Each router cell 274 x 2 x 3 seeds. Step 6, cost axis: training GPU-hours (measured), per-episode injected and generated tokens (measured), converted to GPU-seconds with the replica's measured prefill/decode throughput so both axes are GPU-hours; Pareto plot of pooled and per-type accuracy versus cost and the cumulative-cost curve with break-even episode count for each arm versus all-context k=3 (~430 injected tokens). Step 7, self-rollout pool replicate (runs/bank/own_rollouts_train.jsonl, same partition ratios): SFT-k0 100%, arm (e), and the retention router, 2 seeds; note that on this pool P-CD0 and SFT-k0 nearly coincide, which is reported rather than hidden. Budget: ~11 trained arms (~15 GPU-h training, overlapped with serving) and ~40k episodes; core claim (arms a-100%, b, c, e plus Gate 0 and routers) first, ladder and replicate second.",
 "Baselines and Ablations": "Single-substrate arms at matched cost: all-context k in {1,3,7} from B; all-weights SFT-k0 and CD-k3 memory-free. Controls: P-CD0 (empty-retrieval context distillation) to separate retained memory content from generation format and on-policy-ness; token-matched mismatched memory at test for every student; decoy router (same types, same tokens, relevance destroyed) and random-type router at the same injection fraction; SFT-k3 to check the crutch corner (r < 0 would flag it); procedure-held-out-from-both arm (f) versus held-out-from-targets arm (e) to separate generalization from substitution. Ablations: pool-size ladder (10/30/100%) as the retention manipulation; router threshold tau in {0.3,0.5,0.7} reported as a curve; item-level router variant (inject only when retrieval similarity to the top bank item exceeds a threshold, calibrated on H) reported as a secondary point on the Pareto plot and explicitly not a headline because stall_triggered_injection and failure_signature_routing are archived; k=7 hybrid to check that the ceiling is not a k=3 artefact.",
 "Falsifiable Predictions": "P1 (substitution slope): across the ~40 (type, arm) cells, the regression of residual context value RV on un-retained gain (1-r)g has slope in [0.7, 1.3] and intercept within +/-5 net points; additivity (slope < 0.3 with intercept > 5) or complementarity (RV > g on retained types, i.e. context worth more after training than before) falsifies it. P2 (weights given context): pooled WV = student-matched minus untrained-matched lies within +/-5 net points of zero for SFT-k0 100% and CD-k3; WV >= 8 falsifies substitution (headroom above the in-context ceiling is ~15-19 points on valid_seen, so this is not ceiling-forced). P3 (manufactured contrast): on the type held out from targets but present in the bank, RV >= 0.8 g_t, while on the fully trained multi-step types at 100% pool RV <= 0.5 g_t; difference >= 15 net points. P4 (router): the retention router at injection fraction f <= 0.5 is within 25% of the full hybrid's gain over memory-free (equivalence margin pre-registered as a fraction of the Gate-0 hybrid gain), the random-type router at the same f recovers <= 60% of it, the decoy router <= 20%; if the random router matches the retention router, the residual value is not type-localized and the substitution story is wrong in its useful part. P5 (cost): the retention router's break-even against all-context k=3 occurs at fewer episodes than the full hybrid's, by at least the factor 1/f in per-episode tokens; on the cumulative-cost curve all-weights beats all-context k=3 only after N* = training GPU-h / per-episode GPU-s saved, reported with its CI. P6 (self-rollout replicate): P1-P3 hold with the same sign; a reversal (WV >= 8 on the on-policy pool) is reported as a pool-dependent failure of substitution.",
 "Measurement and Noise Control": "Paired design over identical (game, seed) across all arms; net/100 per pair; 95% CIs by cluster bootstrap over games (1,000 replicates) re-fitting the slope in each replicate; 3 seeds for every 100%-pool and router cell (pooled over both validation splits, 548 games x 3 seeds, ~+/-4.6 net points for a pooled contrast, ~+/-13-15 for a single task type), 2 seeds for ladder cells. Minimum detectable effects stated before the confirmatory run: 5 net points pooled (P2, P4), 15 net points per-type difference (P3), slope SE ~0.08 (P1). Gate 0 as above; Gate 1 (retention heterogeneity): at least one cell with r <= 0.3 and one with r >= 0.6 whose 80% CIs do not overlap, else P1's regression is declared under-ranged and only P2-P4 are confirmatory. Low-noise proxy: memory-free action-token NLL of each student on H targets, reported alongside episode success and used for router calibration. Router selection uses H only; validation cells are never used for any choice. Decoding temperature, prompt template, vLLM version, retriever and truncation rules pinned and pre-registered; evaluation order randomized across arms so throughput drift is not confounded with arm; broken-episode counts and timeouts reported per cell. Thresholds and amendments are written to the pre-registration file before the first confirmatory episode.",
 "Preprint Collision Check": "All searches via the literature command (s2cli: Semantic Scholar + HuggingFace Papers; both channels answered 'ok' unless stated); WebSearch not used (quota exhausted this session); WebFetch never used. Q1 (mechanism, --recent): 'memory-free deployment after distilling retrieved experience residual value of in-context memory per task' -> 7 hits: 2608.26730 (conditional experience transfer in post-training), 2607.21051 (Experience Distillation), 2607.09493, 2606.22844, 2602.16093 (DiSC), 2512.10696 (ReMe), 2502.02046; none evaluates the trained student with memory back against the untrained agent with memory, none localizes residual value by task type, none builds a retention-based router. Q2 (closest method, --recent): 'internalize general skills into weights keep task-specific skills in context router agentic RL' -> 2606.23127, 2605.28424 (Skill0.5), 2604.02268 (SKILL0), 2603.29919, 2603.18743, 2601.04748, 2504.06821; Skill0.5 is the closest (weights for general, context for task-specific, difficulty router) but reports no token cost, no matched single-substrate arms and no per-type retention. Q3 (cost framing, --recent): 'context distillation versus in-context learning cost comparison' -> 2607.21051, 2512.02543 (in-context distillation cascades, 2.5x cost reduction on ALFWorld, frozen student only), 2602.15902 (Doc-to-LoRA), 2608.29897, plus off-topic hits; no agent paper reports both marginals on one cost axis. Q4 (--recent): 'keeping experience in context versus distilling into weights matched inference tokens training compute agent' -> no results on S2 or HF. Verdict: no collision found; the nearest is SESA 2607.29468 (already in the digest), which measures the opposite marginal.",
 "Risk Factors and Limitations": "The in-context ceiling on valid_seen (0.81 at k=3) leaves ~15-19 points of headroom, so additivity could be partly masked; mitigated by per-type analysis, the procedure-held-out-from-both split and timeouts/broken counts, and stated as a limitation. Halving the bank may shrink the in-context gain below Gate 0; the bank share is then raised, which shrinks the target set and retention. Near-duplicate templates within a task type mean the target set effectively teaches the bank's procedures; the partition prevents item memorization but not procedure overlap, which is precisely what the retention estimand measures. Six task types give few regression units; the pool-size ladder and the manufactured held-out type supply the range, and Gate 1 declares the regression under-ranged if they do not. Router calibration on ~150 H tasks is noisy; misestimated types make the router worse, which counts against P4 (conservative), and the NLL-proxy calibration is the fallback. Budget is 5-6 node-days if all arms run; the core claim needs ~half. ALFWorld-only; a WebShop check is out of budget for this round. Self-rollout pool is still being collected and may be too small for a 10/30/100% ladder."
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

Proposal: context_ceiling_substitution — Does Training Still Add Anything Once the Memory Is Back? Substitution at the In-Context Ceiling and Retention-Routed Memory After Internalization

- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.66 · hf
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2502.02046 · 2025-02-04 · preprint · sim 0.61 · hf
  Contextual Memory Reweaving in Large Language Models Using Layered
  Latent State Reconstruction
  Memory retention challenges in deep neural architectures have ongoing limitations in the ability to process and recall extended contextual information. Token dependencies degrade as sequence length increases, leading to a decline in coherence and factual consistency across longer outputs. A structured approach is introduced to mitigate this issue through the reweaving of latent states captured at different processing layers, reinforcing token representations over extended sequences. The proposed
- arxiv:2604.27003 · 2026-04-29 · preprint · sim 0.60 · hf
  When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents
  Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity dilemma of parametric learning. We show that this challenge does not disappear but resurfaces at the memory level. Under a limited context window, old and new experiences compete during retrieval, relocating the continual-learning bottleneck from parameter updates to memory access. To s
- arxiv:2601.19897 · 2026-01-27 · preprint · sim 0.59 · hf
  Self-Distillation Enables Continual Learning
  Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple meth
- arxiv:2606.22844 · 2026-06-22 · preprint · sim 0.57 · hf
  RaMem: Contextual Reinstatement for Long-term Agentic Memory
  Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We r
- arxiv:2609.01532 · 2026-09-01 · preprint · sim 0.57 · hf
  Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
  Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while for
- arxiv:2606.03746 · 2026-06-02 · preprint · sim 0.57 · hf
  Qwen-Image-Flash: Beyond Objective Design
  Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspective, focusing on the training recipe that critically shapes student performance. Using Qwen-Image-2.0 as a representative case, we systematically investigate three factors in unified text-to-image generation and instruction-guided image editing distillat
- arxiv:2605.08374 · 2026-05-12 · preprint · sim 0.56 · hf
  MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs
  Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency chains through which memories enable the creation of future memories. We introduce MemQ, which applies TD(λ) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. Credit wei
- arxiv:2606.11173 · 2026-06-09 · preprint · sim 0.55 · hf
  The Role of Feedback Alignment in Self-Distillation
  Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this contex
- arxiv:2412.15115 · 2024-12-19 · preprint · sim 0.54 · hf
  Qwen2.5 Technical Report
  In this report, we introduce Qwen2.5, a comprehensive series of large language models (LLMs) designed to meet diverse needs. Compared to previous iterations, Qwen 2.5 has been significantly improved during both the pre-training and post-training stages. In terms of pre-training, we have scaled the high-quality pre-training datasets from the previous 7 trillion tokens to 18 trillion tokens. This provides a strong foundation for common sense, expert knowledge, and reasoning capabilities. In terms 

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

