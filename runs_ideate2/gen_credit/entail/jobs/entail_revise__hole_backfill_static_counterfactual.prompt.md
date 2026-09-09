=== SYSTEM ===
You are revising your own research proposal after review.

The reviewers' objections are the specification. Answer each one concretely — not by adding reassuring prose, but by changing the design: cut experiments that do not carry a claim, drop target tasks, shrink the grid, narrow the claim to what the sample size can actually detect, add the baseline they named.

Two rules:

- **Do not abandon the core hypothesis.** A proposal that answers every objection by becoming   generic is worse than one that keeps a sharp claim and scopes it honestly. If an objection   can only be answered by giving up the contribution, keep the contribution and say in   changes_made why you refused.
- **Novelty is the thing you are most likely to lose.** Measured across revision rounds,   answering reviewers reliably raises soundness and feasibility and *lowers* novelty: the   claim gets hedged, the scope narrows, and what was surprising becomes safe. Guard against   that. Do not soften the central claim into something a reviewer could not disagree with, do   not replace a sharp mechanism with a measurement study, and do not add qualifiers that make   the prediction unfalsifiable. If a reviewer's objection is really "this is risky", the right   answer is a better test of the risky claim, not a smaller claim. State in changes_made what   you did to keep the claim as sharp as it was.
- **The resource envelope is hard.** Every experiment must fit the stated compute and budget.   If the full matrix does not fit, cut it to a primary experiment that decides the main claim   plus the minimum ablations that isolate the mechanism, and state the arithmetic: number of   runs x rollouts per run, and why that fits. A smaller study that can be run beats a large   one that cannot.

=== USER ===
=== PROPOSAL ===
{
 "Name": "hole_backfill_static_counterfactual",
 "Title": "Which Counterfactual Is Item Credit? Hole, Backfill and Static-Procedure Replacement Give Different Per-Item Values for Retrieved Experience, and Only Backfill Predicts What Pruning Realizes",
 "Short Hypothesis": "For the same retrieved item on the same (game, seed), the leave-one-out value with an empty slot (hole: what CUE-R REMOVE, Shapley-RAG marginal contributions and DIG estimate) is neither the value that pruning realizes (backfill: the retriever serves its next-ranked bank item) nor the item-specific value beyond the type's procedure (replacement by a token-matched placebo carrying the static procedure sentence). For expert same-type items backfill credit is a fraction of hole credit and item-specific credit is smaller still; for planted wrong-procedure items the references coincide; and the realized loss from pruning the bank is predicted by summed backfill credit while summed hole credit over-predicts it.",
 "Related Work": "CUE-R (arxiv:2604.05467) measures per-evidence utility by REMOVE/REPLACE/DUPLICATE in single-shot RAG, replacing with distractors rather than the retriever's own next candidate, and reports no cost or variance. Shapley source attribution in RAG (arxiv:2507.04480) and DIG confidence gain (arxiv:2509.12765) are hole-based marginal contributions in single-shot QA. The local additive attribution taxonomy (arxiv:2607.14271) names the reference (what replaces the removed input) as a specification choice but does not evaluate references against a downstream decision; semantic-missingness baselines (arxiv:2508.14482) argue the reference must be a plausible state, which for a memory bank is the next-ranked item. On the agent side credit is set-level (UCOB arxiv:2606.29502; ExpSuite arxiv:2605.30712), agent-level (TreeMem arxiv:2605.04811) or write-action-level (HiMPO arxiv:2606.16285); utility-refining systems that prune (ReMe arxiv:2512.10696; SF-AMS arxiv:2607.22562) never state which counterfactual their score is meant to track. The program's nested-k logs give hole credit per slot for free; nothing gives the backfill counterfactual.",
 "Abstract": "Every memory system that prunes or admits items acts on a per-item score, but the score is validated (when at all) against removing the item and leaving a hole, whereas pruning realizes a different counterfactual: the retriever fills the slot with its next-ranked item. We measure, for the same retrieved item on the same ALFWorld (game, seed) with a Qwen3-32B reader over k=3 expert-bank sets, four references for the same slot: hole (k=2), backfill (rank-4 item from the same retrieval log), a token-matched cross-type placebo, and the placebo with the type's static procedure sentence prepended (Measurement C at item level). Credits are estimated per item class (natural expert, planted wrong-procedure, self-written, cross-type) at positions 1-3 with cells sized to +/-5 net, and additivity of each reference is tested by pruning 50% and 75% of the bank at random and comparing the realized loss with the loss each reference predicts. The contribution is a statement of what per-item credit is for: the reference that predicts the pruning outcome, its magnitude relative to hole credit per class, and its cost (one re-run per item-episode, the same as hole).",
 "Experiments": "Unit: (game, seed, position p in {1,2,3}) over 274 valid_seen+valid_unseen games, 2 seeds, k=3 sets taken from runs/sweep/k_sweep_final.jsonl (item ids in rank order). Arms per unit: FULL (natural k=3); H (item p removed, k=2); B (item p replaced at the same position by the rank-4 item of that log); P (item p replaced by a token-matched, within 10%, expert trajectory of a different task type); S (P with the type's static procedure sentence prepended, tokens matched by trimming P). Credits: c_X = success(FULL) - success(X), paired by (game, seed). Classes: natural expert (all three positions: FULL 548 + 4 arms x 1,644 = 7,124 episodes, about 6 h); planted classes are inserted at positions 1 and 3 in place of the natural item, and their H, B, P, S arms are identical to the natural class's arms at that position, so each planted class needs only its FULL-with-plant arm: wrong-procedure (procedure action swapped, e.g. heat->cool, clean->heat, receptacle swapped for pick-and-place), self-written (self-pool success nearest to the game), cross-type (nearest expert item of another type): 3 x 2 x 548 = 3,288 episodes, about 2.7 h. Pruning-realization cell: prune 50% and 75% of the expert bank uniformly at random, re-retrieve, run 274 games x 4 seeds each plus 2 extra seeds of the unpruned baseline: 2,740 episodes, about 2.3 h; compare the realized loss with f x sum_p c_H(p) and f x sum_p c_B(p). Consumer-swap arm (separate): natural class at position 1, arms FULL/H/B on the second local backbone (serving verified first): 1,644 episodes. Total about 14,800 episodes, about 12.5 h at 20 episodes/min on two replicas; both GPUs busy throughout; pre-registration before the first confirmatory cell; the natural-class position-1 H cell is run first as the positive control (must show c_H >= +10 net, expected from the k=1 vs k=0 contrast of +20).",
 "Baselines and Ablations": "Nested-k slot credit from the existing logs (k=1 vs k=3 vs k=7) as the free position-level baseline; k=1 leave-one-out excluded because it equals the k=0 contrast; hole vs backfill vs placebo vs placebo+static as a within-unit factorial; position (1-3) and set composition (natural vs planted at rank 1 vs rank 3) as manipulated factors; per-type breakdown (clean/heat/cool vs pick-two vs look-in-light); set-level static-procedure arm (Measurement C) as the reference for S; random-pruning realization at two fractions as the additivity test of each reference; backfill item similarity to the removed item (embedding cosine and same-object flag) as a covariate; second backbone as a separate consumer-swap arm; seeds as a factor.",
 "Falsifiable Predictions": "- P1 (backfill is a fraction of hole): for natural expert items pooled over positions, mean c_B <= 0.4 x mean c_H. Falsified if c_B >= 0.8 x c_H with the 95% CI of the ratio excluding 0.4 (the rank-4 item is not a near-substitute). Arm: natural-class H and B cells (1,644 paired episodes each).\n- P2 (class x reference interaction): the gap c_H - c_B is at least 5 net larger for natural expert items than for planted wrong-procedure items (where H, B and S should agree because any correct replacement fixes the harm). Falsified if the gap for wrong items is >= the gap for expert items minus 5, or reversed. Arm: the 2 x 2 (class x reference) cells at positions 1 and 3.\n- P3 (which reference predicts the realized pruning loss): at f=0.75 the realized loss lies within +/-5 net of f x sum_p c_B(p) and at least 8 net below f x sum_p c_H(p). Falsified if the realized loss lies within +/-5 of the hole prediction or exceeds it. Arm: the 75%-pruned bank cell (274 x 4 seeds) against the unpruned baseline.\n- P4 (item-specific credit beyond the procedure): for expert items in clean/heat/cool types, S recovers at least two thirds of hole credit (c_S <= 1/3 x c_H), i.e. most item credit is type-procedure credit; falsified if c_S >= 2/3 x c_H in those types (the trajectory carries object- or scene-specific value the static sentence lacks). Arm: S and H cells per type.\n- P5 (consumer swap, separate arm): the c_B/c_H ratio for expert items at position 1 on the second backbone is within +/-0.2 of the Qwen3-32B ratio; falsified if it differs by >= 0.3. Arm: swap cell (FULL/H/B, 1,644 episodes).",
 "Measurement and Noise Control": "All contrasts paired by (game, seed); cluster bootstrap over games with seed as a factor for CIs; the known floor is +/-8 net at 548 paired episodes and +/-5 at about 1,400, so natural-class cells pool positions (1,644) and planted classes report +/-8 per position and +/-5.7 pooled; ratios reported with bootstrap CIs and only interpreted when the positive control (c_H at position 1 >= +10) holds; pruning cell uses 4 seeds (1,096 paired, +/-5.7) because P3 is a difference of two predictions; prompt hashes and token counts of every replacement logged so that H/B/P/S sets are reproducible; retrieval is frozen from the logs so no arm re-retrieves except the pruning cell, whose re-retrieval is the manipulated variable; per-type results reported but only pooled claims are confirmatory; vLLM prefix caching on for both replicas, workers tuned to the running queue (>= 8 per replica).",
 "Preprint Collision Check": "- mechanism (last 12 months): query 'leave-one-out counterfactual attribution of individual retrieved memory items in LLM agents' --recent, channel s2cli (S2+HF, both ok): 7 results, none on per-item counterfactuals in agent memory (BeliefMem arxiv:2605.05583, Mandela-effect multi-agent memory arxiv:2602.00428, the rest are counterfactual-reasoning benchmarks).\n- closest named method: query 'intervention-based per-evidence utility remove replace duplicate retrieval-augmented generation' --recent, channel s2cli: CUE-R arxiv:2604.05467 (single-shot RAG, distractor replacement, no cost/variance), CoRM-RAG arxiv:2605.01302 (counterfactual risk minimization for retrieval robustness, single-shot); neither uses the retriever's next candidate or a static-procedure reference, nor multi-step agents.\n- closest named method: query 'Shapley value attribution of retrieved documents in retrieval-augmented generation', channel s2cli: arxiv:2507.04480 (SHAP approximations vs exact, RAG), RAG-E (S2, no arXiv id; attribution-relevance gap metric), arxiv:2605.27105 (position/context-size effects reproduction); all hole-based, single-shot.\n- home: query 'feature attribution baseline reference value choice counterfactual replacement', channel s2cli: arxiv:2607.14271 (taxonomy naming reference as a specification choice), arxiv:2508.14482 (semantic missingness baselines), arxiv:2603.05093 (transport-geodesic baselines); none evaluates a reference against a downstream decision or in a sequential decision setting. No pre-emption found; WebSearch not used.",
 "Risk Factors and Limitations": "Hole credit at positions 2-3 may be near the noise floor (+7 net for items 2-3 combined), making ratios unstable there; the confirmatory ratio is therefore pooled and anchored on position 1. Backfill items can be near-duplicates of the removed item, which is the point but makes c_B small and its CI relatively wide. Static-sentence padding by trimming the placebo is an approximation of token matching. The pruning cell changes the retrieval distribution, which the archived memory_budget_confound idea warns about; it is used here only as the realization check of an estimand, not as a volume claim. Second-backbone serving is unverified. Results are ALFWorld-specific: procedure-bound value may make S recover more credit than in environments where trajectories carry instance-specific content.",
 "Addresses gap": "G5 (single-shot RAG intervention attribution has not been extended to multi-step agents with a persistent bank, and whether item credit transfers to the decision that uses it is untested); secondarily G1 (no per-item counterfactual exists inside an agentic memory system).",
 "Not a restatement of": "Brief bullet 'Marginal value of items 2-3 over item 1 = +7 net; of items 4-7 = +4' (nested-k slot credit): that bullet measures the value of a slot under hole removal; this idea claims the value of a specific item relative to its backfill is a different and smaller quantity, and that only the backfill quantity predicts a realized pruning loss. Digest card arxiv:2604.05467 (CUE-R REMOVE/REPLACE/DUPLICATE): that card replaces with distractors in single-shot RAG; this idea replaces with the retriever's own next candidate and with the type's static procedure in a multi-step agent and tests which reference predicts what pruning realizes, with cost and noise reported. Archived memory_item_value_reliability (6.12) claimed item value is context-dependent without an intervention arm; here every value is an intervention on the same (game, seed) and the dependence is on the counterfactual's reference, not on context."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "hole_backfill_static_counterfactual",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "Natural-expert H (item p removed, k=2) and B (rank-4 backfill at same position) arms, 1,644 paired episodes each, c_X = s(FULL) - s(X) paired by (game, seed); positive control c_H(pos 1) >= +10.",
   "falsifier": "c_B >= 0.8 x c_H with the 95% CI of the ratio excluding 0.4, i.e. the rank-4 item is not a near-substitute for the removed item.",
   "label": "open",
   "reason": "Both outcomes are reachable (rank-4 can be a near-twin or near-useless) and, at the stated expected c_H of about +20, the 0.4-vs-0.8 band is 8 net against a paired s(B)-s(H) floor of +/-5, so it resolves - though only barely, since at the design's own gate value c_H = +10 the band shrinks to 4 net and falls inside that floor.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "The 2x2 class x reference cells at positions 1 and 3, where the Experiments section states the planted classes' H, B, P, S arms are identical to the natural class's arms at that position and only the FULL-with-plant arm is new.",
   "falsifier": "The gap c_H - c_B for wrong-procedure items is >= the expert gap minus 5, or reversed.",
   "label": "unresolvable",
   "reason": "Because the planted class reuses the natural class's H and B episodes, c_H - c_B = s(FULL_plant) - s(H) - s(FULL_plant) + s(B) = s(B) - s(H) for both classes - the same measured number - so the class x reference interaction is identically zero and always lands inside the +/-5 falsification band regardless of the data.",
   "fix": "Run class-specific H and B arms (remove and rank-4-backfill the planted item within the planted set) so the two gaps are estimated from different episodes rather than sharing arms that cancel the FULL term."
  },
  {
   "id": "P3",
   "depends_on": "75%-pruned-bank cell (274 games x 4 seeds, +/-5.7) against the unpruned baseline, compared with f x sum_p c_B(p) and f x sum_p c_H(p) built from the position-level natural-class credits.",
   "falsifier": "Realized loss within +/-5 of the hole prediction, or exceeding it.",
   "label": "unresolvable",
   "reason": "Both the +/-5 confirmation window and the +/-5 falsification window are narrower than the combined error of the comparison - +/-5.7 on the realized loss plus roughly +/-6 on the three-position summed credit prediction - so noise alone can put the point estimate in either window.",
   "fix": "State an equivalence margin larger than the combined CI (or add seeds until the realized-loss-minus-prediction CI is under 5 net), and pre-register that the additivity test only covers items whose measured positions survive re-retrieval after pruning."
  },
  {
   "id": "P4",
   "depends_on": "Per-type S (placebo + static procedure sentence) and H cells for clean/heat/cool only, carved out of the natural-class 1,644-episode arms; Measurement says per-type results are reported but only pooled claims are confirmatory.",
   "falsifier": "c_S >= 2/3 x c_H within those types, i.e. the trajectory carries object- or scene-specific value the static sentence lacks.",
   "label": "unresolvable",
   "reason": "Splitting the natural cells to three of six types leaves roughly 800 paired episodes per arm (+/-7 or worse), while the 1/3-vs-2/3 decision band is only about 1/3 of c_H (3-7 net), and the proposal itself declares per-type cells non-confirmatory.",
   "fix": "Pool clean/heat/cool into one pre-registered confirmatory cell powered to a CI under 3 net on c_S - c_H/3, and gate it on a c_H of at least +20 rather than +10."
  },
  {
   "id": "P5",
   "depends_on": "Second-backbone swap cell of 1,644 episodes split across FULL/H/B (about 548 per arm, +/-8), position 1 only, compared with the primary-backbone ratio which P1 computes pooled over positions.",
   "falsifier": "The c_B/c_H ratio on the second backbone differs from the Qwen3-32B ratio by >= 0.3.",
   "label": "unresolvable",
   "reason": "A ratio of two contrasts each carrying +/-8 on a base of 10-20 net has a bootstrap CI spanning well over 1.0, so a 0.2/0.3 discrimination is far inside the stated noise, and the two ratios are additionally non-comparable (position 1 vs pooled positions).",
   "fix": "Match the swap cell to the primary cell's 1,644 paired episodes per arm at the same positions and restate the prediction as a difference of credits in net points with a stated MDE instead of a ratio-of-ratios."
  }
 ],
 "shared_terms": [
  "P1-P2: both reduce to s(B) - s(H) measured on the identical natural-class H and B arms; because the planted classes reuse those arms, P2's interaction is P1's numerator differenced against itself and is identically zero.",
  "P1-P3: f x (sum_p c_H - sum_p c_B) is the position-summed s(B) - s(H) of P1, so P1's ratio mechanically fixes how far apart P3's two competing predictions can be.",
  "P1-P5: P5's estimand is P1's ratio recomputed on a second backbone, sharing the estimand definition and the same FULL-arm subtraction.",
  "P4-P1: c_S and c_H share the FULL arm and the identical H cell, so P4's ratio moves with P1's denominator.",
  "P2-P4: the planted-class and per-type claims are both scored against the one shared H/B/P/S arm block at each position, so their errors are the same episodes."
 ],
 "headline": "P3",
 "headline_status": "unresolvable",
 "n_open": 1,
 "n_entailed": 0,
 "n_near": 0,
 "n_unresolvable": 4,
 "verdict": "revise"
}

=== BINDING RULES FROM THE BRIEF ===
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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
