# Title: Which Memory Item Did It: Credit Assignment for Retrieved Experience in LLM Agents

Author: Fable 5.1, 2026-09-09. Stage-1 brief for the ideate2 pipeline, after the Stage-0 pre-scan on this topic (5 axes,
60 papers carded from S2 + HF, 25 gaps; `digest.md`; no section reads) and after Step 0 on this node
(`runs/STEP0_RESULTS.md`). Third topic of the program alongside `xfer` and `static`; the 51 archived ideas are the prior.

## Keywords
LLM agents, experience memory, credit assignment, counterfactual attribution, leave-one-out, Shapley, memory utility,
reinforcement over memory, retrieved-set interference, utility drift, data valuation, ALFWorld

## TL;DR
Every self-evolving memory system now scores its items: Q-values propagated over a provenance DAG (MemQ 2605.08374),
reduced-order utility coordinates (RoMeRL 2608.02508), critic-gated surprise and utility (2603.14597), survival importance
(2607.22562), attribution-derived local rewards (AttriMem 2607.21106), outcome-calibrated attribution distilled into the
policy (OPD-Evolver 2606.17628), admission scores (A-MAC 2603.04549). The scan finds the same hole under all five axes:
not one of these scores has been checked against the counterfactual effect of removing or adding the item it scores.
Credit is assigned to the retrieved set, the prompt, the agent or the write action, never to the item; the noise and sample
cost of any per-item estimate is unreported; interactions among co-retrieved items are measured only in single-shot RAG
(CUE-R 2604.05467, Shapley 2507.04480) or at the scaffolding-component level (2605.05716); and whether an item's value
survives a change of query, consumer or time is asserted. The program's own best-scored idea (memory_item_value_reliability,
6.12) lived here and did not pass, so the bar is known: a proposal must say what per-item credit is for, show that it can be
estimated at a cost the program can pay, and predict where it fails.

## Starting position (measured here; not to be rediscovered)
- **Expert bank, Qwen3-32B reader, ALFWorld:** k=0 0.536/0.549 → k=1 0.739/0.776 → k=3 0.807/0.869 → k=7 0.846/0.877
  (valid_seen/valid_unseen); net at k=3 +27.1 [+18.6, +35.6] / +32.1 [+22.9, +41.0]. Marginal value of items 2–3 over
  item 1 ≈ +7 net; of items 4–7 ≈ +4. The gain is procedure-bound (clean/heat/cool +39 to +55) and unseen ≈ seen; one type
  (look-at-in-light, n=62) nets −4.8. Retrieval logs (`runs/sweep/k_sweep_final.jsonl`) hold, per episode, the retrieved
  item ids in rank order, so a nested-k design (k=1 ⊂ k=3 ⊂ k=7 on the same games) already gives one crude per-position
  counterfactual for free.
- **Self pool:** 1,892 on-policy successes over all six types (0.533), success-filtered; useful for items whose value is
  expected to differ from expert items.
- **Noise floor:** a paired 274-game × 2-seed cell ≈ ±8 net; per-type cells ±13–15. Per-item estimates will be far noisier
  than per-arm ones: an item is retrieved for a handful of games, so any item-level claim must be about a distribution of
  items or a manufactured item class, not about individual items.
- **Measurement C (running):** static per-type procedure prompts vs retrieval; a retrieved item whose value is fully captured
  by the type's procedure has no item-specific credit to assign.
- **Cost:** ~20 episodes/min on two replicas; a leave-one-out re-run of one episode costs one episode; Shapley over a k=3 set
  costs 7 re-runs per episode.

## What the Stage-0 scan says, by axis (gap ids as in `digest.md`)
1. **Counterfactual attribution** (12 cards). Intervention-based per-item measurement exists for single-shot RAG (CUE-R
   REMOVE/REPLACE/DUPLICATE 2604.05467; document-level Shapley 2507.04480; DIG confidence gain 2509.12765) and at the
   component level for agent scaffolds (2^5 factorial with exact Shapley, 56 % submodularity violations, 2605.05716);
   agent-side credit is set-level (UCOB 2606.29502), agent-level (TreeMem 2605.04811), write-action-level (HiMPO
   2606.16285) or step-level (SLATE 2602.23440; Harness-G SNC 2607.27652). Gaps G1–G5.
2. **Learned utility and reinforcement over memory** (33 cards). MemRL two-phase retrieval (2601.03192), REMEMBERER
   (2306.07929), MemQ TD(λ) over a provenance DAG (2605.08374), RoMeRL's memory-reward trap and fixed-dimensional utility
   state (2608.02508), Oblivion's contribution-based reinforcement (2604.00131), MERIT's PRM proxy rewards (2606.00547),
   ExpSuite's with/without-set feedback (2605.30712), utility-aware pruning (ReMe 2512.10696, SF-AMS 2607.22562), admission
   (A-MAC 2603.04549, critic router 2603.14597). Gaps G6–G10: no score is checked against counterfactual item value; credit
   splitting among co-retrieved items unresolved; noise and sample cost unreported; validity under drift untested; pruning
   and admission error rates unmeasured.
3. **Set-level effects** (14 cards). Compliance trap (2607.10608), controlled memory interference (2608.07622), interference
   under updates (MINTEval 2605.18565; Memora 2604.20006), RaMem validity-aware retrieval (2606.22844), steerable memory
   dependence (2601.05107). Gaps G11–G15: per-item scores never validated against leave-one-out; harm's dependence on set
   composition untested in multi-step agents; failures never attributed to the responsible item; interference shown only on
   synthetic relationships; variance of per-item estimates unreported.
4. **Generalization and drift of item value** (31 cards). Gaps G16–G20: utility estimates never re-measured over a drifting
   stream; transfer of item value across consumers or query distributions untested; admission-time predictions never
   checked against realized utility (and false-negative cost unmeasured); forgetting rules validated only by aggregate
   accuracy; item value is state- and stage-conditional yet never measured per context.
5. **Measurement of per-item estimates** (22 cards). Benchmarks score end-to-end outcomes only (Evo-Memory 2511.20857,
   MemoryArena 2602.16313, MemoryAgentBench 2507.05257); no benchmark attributes a failure to an item. Gaps G21–G25.

## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **Ground truth is an intervention, not a score.** Any per-item value claim is anchored to re-runs with the item removed,
  replaced (token-matched) or added, on the same (game, seed); learned or proxy scores are evaluated by their rank
  correlation with that ground truth, not by downstream success alone.
- **Items are manufactured in classes when individual power is impossible.** Item-level CIs are wide; claims are about item
  classes (planted wrong-procedure items, stale-true items, same-type vs cross-type items, expert vs self-written items)
  with enough retrievals per class, or about the distribution of item values, with the sample size stated.
- **Set composition is a manipulated variable.** Any per-item estimate is reported under at least two co-retrieved-set
  compositions; additivity is tested, not assumed (pairwise removal vs single removal).
- **Noise and cost of the estimator are estimands.** Report variance across seeds and repeated runs, the number of episodes
  or re-runs needed for a stable per-item rank, and the LLM-call cost at that reliability; a method whose estimate needs
  more re-runs than a leave-one-out baseline must say so.
- **Static-procedure baseline (Measurement C).** Credit that a type-level procedure sentence already captures is not item
  credit; report item value net of the static-prompt arm.
- **Drift and consumer swap are separate arms**, not extrapolations: an item's value is re-measured after the query
  distribution, the store size or the reader changes.
- **No prediction entailed by a definition** (an append-only score cannot decrease; a leave-one-out on a k=1 set equals the
  k=0 contrast; a score defined from the outcome correlates with the outcome); per prediction, state the falsifying outcome
  and the arm that can produce it.
- **Home-vocabulary search**: data valuation, influence functions, Shapley attribution, credit assignment in RL, replay
  prioritization, off-policy evaluation; one query with no agent/memory/benchmark words.
- **Power and budget**: paired cells; per-class cells sized to ±5 net; re-run budgets stated cell by cell; both GPUs busy.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Do learned utilities track counterfactual item value (G6, G11, G22)?** Implement one published scorer per family
  (Q-value over provenance, utility coordinates, usage-decay survival, confidence gain) on the ALFWorld bank, then measure
  leave-one-out and replace effects for the same items; predict which scorer fails where (co-retrieval contamination,
  position, rarity) and by how much.
- **Q2 The unit of credit (G1, G7, G23).** Set-level, position-level, item-level: which unit predicts the outcome change of
  the next retrieval best, at what re-run cost; the nested-k logs give the first position-level estimate for free.
- **Q3 Interference and non-additivity (G4, G12, G25).** Pairwise vs single removal on manufactured sets (helpful +
  conflicting, helpful + redundant, two partial supports); how often single-item scores mis-rank when interactions exist.
- **Q4 Estimator noise and sample cost (G3, G8, G15, G24).** Convergence of per-item rank with re-runs and seeds; the
  winner's-curse of selecting top-scored items; how many episodes per item a pruning decision needs to beat random pruning.
- **Q5 Drift and consumer swap (G9, G17, G20, G16).** Re-measure item value after a rule change, after the store grows, after
  the reader is swapped (Qwen3-32B → a second backbone); fraction of items whose value sign flips; whether stage-conditional
  value (item helps at entry, hurts on recovery) exists.
- **Q6 Admission and pruning audits (G10, G18, G19).** Admit a random held-out sample regardless of score; correlate
  admission score with realized counterfactual utility; false-prune and false-bypass rates; whether frequency
  reinforcement entrenches wrong items.

## In scope
- ALFWorld primary (bank and logs on disk); a second environment only if the claim needs it; public data only.
- Qwen3-32B as reader; a second local backbone for the consumer-swap arm (serving to be verified).
- Reimplementation of one scorer per family as a named baseline (MemQ-style TD(λ), RoMeRL-style coordinates, usage-decay,
  DIG-style confidence gain); leave-one-out and Shapley as ground-truth estimators.

## Out of scope
- Frontier-model judges at experiment time; clinical or private data.
- New memory systems whose contribution is a better aggregate score; the contribution here is what the score means.
- Restating the archived ideas (appendix); a proposal near one must name it and state what it fixes.

## Resource constraints
Two A100 80GB, one replica per GPU, ~20 episodes/min. A leave-one-out ground truth over 274 games × 2 seeds × k=3 costs
about 1,650 re-runs (~1.5 h); Shapley over k=3 sets costs ~7× that; a scorer family needs one pass of the stream to learn
its scores (the 3,553-game train stream, ~3 h) before ground truth is measured. A full Q1 (four scorers, one ground truth,
two set compositions) is roughly two days. Pre-registration before the first confirmatory cell.

## Appendix A: archived ideas nearest this topic (do not restate; the gate compares against all 51)
- memory_item_value_reliability (6.12, round 1, the program's best score): item value is not an item property; a
  generalizability audit of per-item utility estimates in self-editing memory. Judges: no ground-truth intervention arm,
  effect sizes below the noise floor.
- counterfactual_memory_screening_under_selection_noise (5.45): does counterfactual screening survive its own noise;
  neighborhood-conditional utility, winner's curse, interference. Judges: the noise model was assumed, not measured.
- utility_pruning_is_frequency_pruning (4.9): outcome-based refinement deletes rare-task coverage. Judges: entailed by the
  pruning rule.
- retrieved_set_disagreement_gate (4.65): harm lives in the retrieved set, not the item; a disagreement gate. Judges:
  set-level claim without item-level ground truth.
- dormant_is_not_dead (5.45), action_prior_imprinting (5.27), memory_budget_confound (5.63), wrong_action_fraction_dose
  (4.85): adjacent on pruning, priors, volume and dose.

## Appendix B: what the previous rounds' judges demanded (binding)
Same pool / same backbone / one cost axis; bank–target partition; self-pool and self-distillation controls; memory-absent,
matched and mismatched evaluation; token- and rate-matched placebos; margins tied to the measured effect; positive controls
before any null; no prediction entailed by a definition; the cheapest baseline run first; searches in the mechanism's home
literature.
