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
 "Name": "item_credit_variance_decomposition",
 "Title": "Is There an Item to Credit? Between-Item Variance, Re-run Cost and the Winner's Curse of Per-Item Counterfactual Credit in an ALFWorld Experience Bank",
 "Short Hypothesis": "Within a class of same-type expert items the true between-item variance of leave-one-out credit is indistinguishable from zero (item ICC < 0.1), so per-item scores over an expert bank fit re-run noise; item-level signal exists only between classes (expert vs self-written vs planted-wrong) and within self-written items, whose between-item spread is at least twice that of expert items. Consequently a stable per-item rank needs on the order of 16 retrieval-controlled re-runs per item, selection on fewer shows winner's-curse shrinkage of at least half, and pruning by per-item credit beats random pruning only when planted-wrong items are present and only above about 8 re-runs per item.",
 "Related Work": "Data Shapley (arxiv:1904.02868) and Data Banzhaf (arxiv:2205.15466, verified) show that leave-one-out and Shapley data values are unstable under stochastic training and that the Banzhaf value is the noise-robust semivalue; SCARV (arxiv:2605.00944) studies stable sample ranking under redundancy; FreeShap (arxiv:2406.04606) and amortized Shapley (arxiv:2305.19998) cut the cost of instance attribution. None decomposes item value into a between-item component and a re-run noise component, and none concerns retrieved experience consumed by an agent. On the agent side, TreeMem (arxiv:2605.04811) Monte-Carlo-averages branches without stating how many are needed, Shapley-RAG (arxiv:2507.04480) does not report attribution stability across repeated calls, HiMPO (arxiv:2606.16285) and AttriMem (arxiv:2607.21106) do not report the sample cost of their local utilities, and every scorer family (MemQ arxiv:2605.08374, RoMeRL arxiv:2608.02508, SF-AMS arxiv:2607.22562) presumes that items within a bank differ in value. The archived counterfactual_memory_screening_under_selection_noise assumed a noise model; the archived memory_item_value_reliability had no intervention arm.",
 "Abstract": "Per-item utility scores are the target of every self-evolving memory system, yet no one has asked whether same-class items in a bank differ in counterfactual value by more than the noise of measuring it. We take 100 items from the ALFWorld bank (40 expert, 40 self-pool successes, 20 planted wrong-procedure derivatives, stratified by task type) and force each into k=3 retrieved sets on 16 games of its type with 2 seeds, running FULL and minus-item on each (game, seed) with a Qwen3-32B reader; a 50-item subset is repeated with the item at position 3, a backfill arm is run for expert items, and a 60-item subset is re-measured on a second backbone. A mixed model decomposes per-item credit into class mean, item random effect, game effect and residual, giving the item ICC per class with bootstrap CIs. Subsampling the games yields split-half rank reliability versus re-runs per item, the winner's-curse shrinkage of top-decile items on the held-out half, and the number of re-runs at which bottom-decile pruning finds genuinely worse items. A confidence-gain proxy (first-action log-probability shift, one forward pass) is placed on the same reliability-cost curve. The result is the prerequisite every scorer paper skips: whether there is an item-level quantity to learn, and what it costs to measure.",
 "Experiments": "Items: 40 expert (about 7 per type over 6 types), 40 self-pool successes (same types, success-filtered on-policy), 20 planted-wrong (procedure action swapped in 20 of the expert items); for each item, 16 games of its type from valid_seen+valid_unseen where the item's retrieval rank is <= 20 (plausible retrieval), 2 seeds. Set = item at position 1 plus the game's top-2 natural expert items (excluding the item); arms FULL and HOLE (item removed, k=2), paired: 100 x 16 x 2 x 2 = 6,400 episodes, about 5.3 h. Composition arm: 50 items (25 expert, 15 self, 10 wrong) with the item at position 3: 3,200 episodes, about 2.7 h. Backfill arm for the 40 expert items at position 1 (rank-4 replacement): 1,280 episodes. Consumer-swap arm: 40 expert + 20 wrong at 8 games x 2 seeds x 2 arms on the second backbone: 1,920 episodes. Proxy: log-probability of the first procedure action with vs without the item from the same prompts, no rollout. Total about 12,800 episodes, about 11 h at 20 episodes/min on two replicas. Analyses: mixed model credit_{i,g,s} = mu_class + a_i + b_g + e with item ICC = var(a)/(var(a)+var(e)) per class, CIs by parametric bootstrap over items and games; split-half Spearman across items between disjoint halves of games at n in {2,4,8,16} games per half; winner's curse: top decile by half A, credit on half B, shrinkage = 1 - credit_B/credit_A; pruning: bottom 20% by half-A credit at n re-runs, mean half-B credit vs the pool mean; reliability-cost curve for HOLE, proxy and (from existing logs) nested-k slot credit. Order: the planted-wrong vs expert class contrast is run first as the positive control (must separate by >= 15 net at 40/20 items x 32 paired), before any ICC or reliability claim.",
 "Baselines and Ablations": "Class-mean model (no item effect) vs item random-effect model as the likelihood-ratio test of P1; expert vs self-written vs planted-wrong classes; position 1 vs position 3 composition; hole vs backfill for expert items; confidence-gain proxy and nested-k slot credit as cheaper estimators on the reliability-cost curve; Banzhaf-style robustness check on the position-1/position-3 pair as two coalitions; seeds as a factor; second backbone as a separate consumer-swap arm; random pruning as the decision baseline.",
 "Falsifiable Predictions": "- P1 (no within-class item signal for expert items): item ICC for same-type expert items < 0.1 with 95% CI upper bound < 0.2. Falsified if ICC >= 0.3 with CI lower bound > 0.1 (expert items differ in value by more than re-run noise). Arm: 40 expert items x 16 games x 2 seeds, FULL vs HOLE.\n- P2 (self-written items carry item signal): the between-item SD of self-pool items is at least 2x that of expert items. Falsified if the ratio is <= 1.2 with CI excluding 2. Arm: 40 self-pool items, same design.\n- P3 (positive control, run first): planted-wrong items separate from expert items by >= 15 net in class mean. Falsified if < 8 net; then the design is underpowered and stronger W items are pre-registered before any other claim. Arm: 20 wrong vs 40 expert items.\n- P4 (re-runs for a stable rank): split-half Spearman over all 100 items reaches 0.8 only at n >= 16 games per half (about 32 paired re-runs). Falsified if Spearman >= 0.8 at n = 4 games per half. Arm: subsampled halves of the position-1 cell.\n- P5 (winner's curse): top-decile items selected on half A at n = 4 games retain <= 50% of their half-A credit on half B. Falsified if they retain >= 75% (true between-item variance is large enough that selection is mostly real). Arm: split-half selection on the position-1 cell.\n- P6 (re-runs a pruning decision needs): pruning the bottom 20% by half-A credit finds items whose half-B credit is >= 5 net below the pool mean at n >= 8 games per half but not at n = 2 (<= 2 net); among expert items only, at n = 16 the pruned set is within +/-3 net of the expert mean. Falsified if the rule beats the pool mean by >= 5 at n = 2, fails at n = 16, or beats the expert mean by >= 5 within expert items. Arm: split-half pruning on the position-1 cell.\n- P7 (consumer swap, separate arm): the class separation of P3 reproduces on the second backbone within +/-8 net, while the cross-backbone Spearman of per-item credit among expert items is <= 0.3. Falsified if the class separation vanishes (< 5 net) or the expert cross-backbone Spearman is >= 0.6. Arm: the 60-item swap cell.",
 "Measurement and Noise Control": "Each (item, game, seed) contributes one paired binary contrast; per-item credit at 32 paired re-runs has SE about 9 points (+/-17 net), which is why item-level claims are never made and the estimands are variance components, split-half correlations and class means (40 items x 32 = 1,280 paired, +/-2.7 net); parametric bootstrap over items and games for ICC CIs; split-half statistics averaged over 200 random halvings; seeds nested in games; retrieval controlled so that every item has exactly the stated number of retrievals, removing the natural confound between retrieval frequency and credit; prompt hashes and item ids logged; the proxy is computed on the identical prompts; both GPUs busy with workers tuned to the vLLM running queue; pre-registration of P1-P7 thresholds after the positive-control cell.",
 "Preprint Collision Check": "- mechanism (last 12 months): query 'leave-one-out counterfactual attribution of individual retrieved memory items in LLM agents' --recent, channel s2cli (S2+HF, both ok): 7 results, none on per-item counterfactual variance in agent memory (BeliefMem arxiv:2605.05583, arxiv:2602.00428, counterfactual-reasoning benchmarks).\n- mechanism (last 12 months): query 'shared-prefix truncated re-run first divergence step counterfactual trajectory comparison LLM agent' --recent, channel s2cli: arxiv:2607.06503 (early abort of agent episodes via probes), arxiv:2601.20090 (counterfactual generation for LLM control with conformal guarantees), the rest unrelated; nothing on re-run cost of per-item credit.\n- closest named method: query 'Monte Carlo permutation sampling Shapley estimation variance number of samples convergence', channel s2cli: OddSHAP arxiv:2602.01399, amortized Shapley for text arxiv:2305.19998, Data Shapley arxiv:1904.02868, MARL Shapley arxiv:2110.01307; estimator-variance work on fixed value functions, none with a stochastic LLM-agent value function or an ICC of item value.\n- home: query 'data valuation leave-one-out versus Shapley value rank agreement under retraining noise', channel s2cli: Data Shapley arxiv:1904.02868, FreeShap arxiv:2406.04606, Joint Shapley arxiv:2107.11357, OddSHAP arxiv:2602.01399, federated Shapley variants; none reports a between-item variance component or a re-run count for stable ranks.\n- home: query 'Banzhaf value robust data valuation under stochastic training noise ranking stability', channel s2cli: did not return Data Banzhaf; returned SCARV arxiv:2605.00944 (stable sample ranking under redundancy) and unrelated robustness papers; Data Banzhaf verified directly with the paper command as arxiv:2205.15466 (AISTATS, 195 citations): it shows LOO/Shapley rank instability under training stochasticity for supervised data, which motivates but does not pre-empt an ICC measurement for retrieved experience in agents. No pre-emption found; WebSearch not used.",
 "Risk Factors and Limitations": "Retrieval-controlled sets are not the natural retrieval distribution (items are forced into sets on games where they rank <= 20), so ICC estimates are for plausible rather than realized retrievals; the position-3 composition and the backfill arm bound this. With 40 items per class the ICC CI is wide, so P1 is stated with an upper-bound criterion and could be inconclusive if the CI spans 0.1-0.3. Self-pool items may be systematically longer, confounding class with token count; token counts are covariates and a length-matched subset is reported. A null ICC for expert items would be ALFWorld-specific (near-optimal expert trajectories); the self-pool result is the internal check that the method can detect item signal when it exists. Second-backbone serving unverified. The proxy is one specific confidence-gain variant, not a scorer-family comparison (that is axis 2's task).",
 "Addresses gap": "G3 (no card reports the variance across seeds and repeated calls, the number of episodes or re-runs needed for reliable per-item credit, or its compute cost).",
 "Not a restatement of": "Brief bullet 'Noise floor: ... per-item estimates will be far noisier than per-arm ones; any item-level claim must be about a distribution of items': that bullet states a design rule; this idea measures the distribution's between-item variance component itself, asks whether it is non-zero within a class, and gives the re-run count at which selection beats noise. Digest card arxiv:2507.04480 (SHAP approximations in RAG, stability across repeated calls untested): that card compares approximate to exact attributions on a fixed generator; this idea decomposes per-item credit into item and noise components under a stochastic multi-step agent and reports the winner's-curse and pruning consequences. Archived counterfactual_memory_screening_under_selection_noise (5.45) assumed the noise model; here the noise and the between-item variance are both estimated from retrieval-controlled re-runs. Archived memory_item_value_reliability (6.12) lacked an intervention arm and worked below the noise floor; here every value is an intervention and class cells are sized to +/-3 net."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "item_credit_variance_decomposition",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "Mixed model credit_{i,g,s} = mu_class + a_i + b_g + e over 40 expert items x 16 games x 2 seeds, FULL vs HOLE paired binary contrasts, ICC = var(a)/(var(a)+var(e)) with parametric-bootstrap CIs.",
   "falsifier": "ICC >= 0.3 with CI lower bound > 0.1 (expert items differ in value by more than re-run noise).",
   "label": "entailed",
   "reason": "The ICC denominator uses the per-observation residual of a paired binary contrast (values in {-1,0,+1}, SD roughly 45-70 net points, consistent with the proposal's own +/-17 net at 32 re-runs), so ICC >= 0.3 would require a true between-item SD of 30-45 net points inside a class whose mean credit is only 10-20 net - arithmetically unreachable whatever the items are.",
   "fix": "Define the estimand at item-mean level (reliability at the design's n, or between-item SD in net points with a pre-registered MDE) and add a class with known real spread - e.g. expert plus planted-wrong pooled into one nominal class - as the positive control that the variance-component estimator can detect signal at all."
  },
  {
   "id": "P2",
   "depends_on": "Between-item SD from the same mixed model for 40 self-pool items divided by the expert between-item SD of P1, same 16 games x 2 seeds design.",
   "falsifier": "The SD ratio is <= 1.2 with its CI excluding 2.",
   "label": "unresolvable",
   "reason": "The denominator is the expert between-item SD that P1 asserts (and the estimator forces) to be indistinguishable from zero, so the ratio is unstable by construction and its bootstrap CI spans orders of magnitude, making both the >= 2 confirmation and the <= 1.2-with-CI-excluding-2 falsification undecidable.",
   "fix": "State the self-pool prediction as an absolute between-item SD in net points (e.g. SD >= 12 net with CI excluding 5) rather than a ratio to a component predicted to be zero."
  },
  {
   "id": "P3",
   "depends_on": "Class means of credit for 20 planted-wrong vs 40 expert items at 32 paired re-runs each (640 and 1,280 paired; +/-3.9 and +/-2.7), run first as the positive control.",
   "falsifier": "Class separation < 8 net, triggering a pre-registered strengthening of W.",
   "label": "open",
   "reason": "The outcome genuinely depends on whether the agent uses retrieved procedures - an agent that ignores the bank gives a near-zero separation - and the 15-vs-8 net band exceeds the roughly +/-5 CI on the class-mean difference.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "Split-half Spearman of per-item credit across all 100 items (three classes pooled) at n in {2,4,8,16} games per half, averaged over 200 random halvings of the position-1 cell.",
   "falsifier": "Split-half Spearman >= 0.8 already at n = 4 games per half.",
   "label": "entailed",
   "reason": "At n = 4 (8 paired binary re-runs) the per-item SE is about 18 points (+/-35 net) against a between-item spread that is essentially only the 15-net class separation, so the attainable Spearman is well under 0.5 - and by the same arithmetic (+/-17 net at 32 re-runs, the proposal's own figure) the 0.8 target is unreachable even at n = 16, so the prediction cannot come out either way as stated.",
   "fix": "Derive the reliability curve from the stated per-item SE and pre-register an attainable target (e.g. >= 0.5 at n = 16, < 0.3 at n = 4), and report the curve within class as well as across classes so class membership does not carry the correlation."
  },
  {
   "id": "P5",
   "depends_on": "Top-decile selection on half A at n = 4 games, retention measured as credit_B/credit_A on the position-1 cell, over 200 halvings.",
   "falsifier": "Top-decile items retain >= 75% of their half-A credit on half B (selection is mostly real).",
   "label": "entailed",
   "reason": "Retention >= 75% requires true between-item variance comparable to the selection noise, but at n = 4 the per-item SE is about +/-35 net while P1's design forces within-class true spread to about zero, so near-total regression to the mean is arithmetically guaranteed and the falsifier cannot occur.",
   "fix": "Predict retention against the value implied by the measured variance components (a quantitative shrinkage prediction, not a fixed 50/75% split) and include a selection pool with a planted, known between-item spread so the retention estimator has a case where high retention is possible."
  },
  {
   "id": "P6",
   "depends_on": "Bottom-20%-by-half-A-credit pruning of a 100-item pool that contains exactly 20 planted-wrong items, half-B credit of the pruned set vs pool mean at n in {2,8,16}, plus the expert-only sub-case.",
   "falsifier": "The rule beats the pool mean by >= 5 net at n = 2, or fails at n = 16, or beats the expert mean by >= 5 net within expert items.",
   "label": "unresolvable",
   "reason": "Two of the three falsifying clauses restate the design - the bottom 20% is the same 20% of the pool that was planted wrong, and the expert-only clause is P1's zero within-class variance re-asked - while the surviving clause turns on 5-net and 2-net margins that sit at or inside the +/-5.5 CI of a 20-item x 16-game half-B mean.",
   "fix": "Power the pruning cell so the pruned-set mean CI is under 2 net, and pre-register the enrichment expected purely from the 20% planted-wrong pool composition as the null against which the rule must improve."
  },
  {
   "id": "P7",
   "depends_on": "Second-backbone swap cell: 40 expert + 20 wrong items at 8 games x 2 seeds x 2 arms (16 paired per item), giving class means at +/-3.9/+/-5.5 and per-item credit at about +/-25 net.",
   "falsifier": "Class separation vanishes (< 5 net) on the second backbone, or the expert cross-backbone Spearman is >= 0.6.",
   "label": "near_entailed",
   "reason": "The Spearman clause is dead on arrival - 16 paired re-runs per item give +/-25 net per item against a within-class true spread P1 forces to about zero, so >= 0.6 is unreachable - leaving only the vanishing-separation clause, which is reachable solely if the second backbone ignores retrieval entirely, a mechanism the design cannot distinguish from a serving or prompt-format failure and for which it runs no per-backbone control.",
   "fix": "Add a per-backbone positive control (k=1 vs k=0 on the second backbone) so a vanished separation is attributable, and either drop the cross-backbone Spearman clause or disattenuate it using the measured per-item reliability."
  }
 ],
 "shared_terms": [
  "P1-P4: the split-half Spearman is a monotone function of the same variance components var(a)/var(e) that P1's ICC reports, computed on the identical position-1 cell, so P1's value fixes P4's curve.",
  "P1-P5: winner's-curse retention equals the reliability var(a)/(var(a)+var(e)/n) implied by P1, so a near-zero ICC determines P5's shrinkage before any selection is run.",
  "P2-P1: the SD ratio's denominator is P1's expert between-item SD, so P1's estimand determines whether P2's is even defined.",
  "P3-P7: P7's first clause is P3's class separation re-measured on the second backbone - the same estimand with a different consumer.",
  "P4-P5-P6: all three are computed from the same 200 random half-splits of the same position-1 cell, so their sampling errors are the same draws, not independent tests.",
  "P1-P6: the expert-only clause of P6 (pruned set within +/-3 net of the expert mean) is P1's zero within-class item variance restated as a decision outcome."
 ],
 "headline": "P1",
 "headline_status": "entailed",
 "n_open": 1,
 "n_entailed": 3,
 "n_near": 1,
 "n_unresolvable": 2,
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



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
