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
 "Name": "surrogate_endpoints_for_item_credit",
 "Title": "Cheaper Per-Item Credit from Process Endpoints: Variance Reduction and Class-Specific Bias of Surrogate Outcomes for Leave-One-Out Memory Value",
 "Short Hypothesis": "Per-item leave-one-out value measured on the binary success flag wastes most of each re-run; process endpoints logged in the same re-runs (goal-condition progress, steps-to-success, first-divergence step) give per-item estimates with at least three times lower noise and hence at least three times fewer re-runs for the same rank reliability, but they are biased for identifiable item classes (location-stale items lengthen the path without changing success; redundant duplicates change nothing), a cross-fitted surrogate index calibrated on success removes most of that bias, and zero-re-run offline surrogates (teacher-forced log-probability change, DIG-style confidence gain) do not track counterfactual value.",
 "Related Work": "DIG (arXiv:2509.12765) scores a document by generation-confidence change one document at a time, never checked against counterfactual removal (G22); MERIT (arXiv:2606.00547) and SLATE (arXiv:2602.23440) use PRM or LLM-judge step rewards as proxies whose agreement with counterfactual item value is untested; AttriMem (arXiv:2607.21106) derives local rewards from token attribution with unreported noise. Progress rewards (ProgRM arXiv:2505.18121; Progress Advantage arXiv:2606.26080) and EarlyEval (arXiv:2609.02783, halting evaluation runs early by predicting outcomes from intermediate behaviour) use process signals to cut cost but for policy training or aggregate evaluation, not per-item counterfactuals, and without class-bias tests. Surrogate-outcome methodology in trials (arXiv:2412.14129) and control variates (arXiv:2109.08944) supply the bias-variance framing; CUE-R (arXiv:2604.05467) and Shapley source attribution (arXiv:2507.04480) measure per-item effects on the answer only. Archived memory_item_value_reliability lacked an intervention arm; this idea keeps success-LOO as the anchor and asks what each re-run can additionally measure.",
 "Abstract": "Ground-truth per-item value in a memory-augmented agent is a leave-one-out re-run scored by a 0/1 success flag, so each re-run yields one bit and per-item ranks need tens of retrievals to stabilise. We ask whether the same re-runs, scored by process endpoints - fraction of PDDL goal conditions satisfied at episode end, steps-to-success, the step at which the trajectory first diverges from the intact-set run, and invalid-action counts - deliver per-item estimates that are cheaper to stabilise, and where they are biased. On the ALFWorld expert bank with Qwen3-32B at k=3 we run leave-one-out re-runs on 1,000 train-stream games x 2 seeds with three manufactured item classes forced into position 3 (location-stale: a correct procedure whose object location is true in its source game but wrong here; redundant duplicate: a paraphrase of the top-1 item; planted wrong-procedure), each with about 400 forced retrievals. For every endpoint we estimate the retrievals needed for rank reliability 0.7, the disattenuated rank correlation with success-LOO on natural items, and the class-wise bias in net points; a logistic surrogate index of success on the process endpoints is cross-fitted across game halves and tested for residual bias; offline surrogates that need no re-runs are scored the same way. Composition (natural versus forced sets, pairwise removal), a static-procedure prompt, a second reader and a halved store are separate arms. About 19,000 episodes (16 h) yield a re-run savings factor per endpoint, a bias map by item class, and a calibrated estimator whose cost and bias are both stated.",
 "Experiments": "E0 (free of environment steps, run first): offline surrogates for every item in the k=3 logs - teacher-forced log-probability of the expert action sequence under the prompt with vs without the item, and DIG-style confidence gain on the base trajectory - about 3 forward passes per episode on 2,000 episodes on one GPU while E1 starts on the other. E1 main cell: 1,000 train-stream games x 2 seeds x k=3, base plus 3 single-item removals = 8,000 episodes (about 7 h); in 60% of episodes position 3 is a forced class item (30 location-stale, 30 redundant-duplicate, 30 planted wrong-procedure items; about 400 forced retrievals per class, about 13 per item), the other 40% carry the natural top-3; every run logs success, goal-condition fraction (satisfied PDDL goal predicates at the end), steps to success or max, first-divergence step relative to the intact-set run under the same seed, and invalid or repeated action counts. E2 composition: natural-only vs forced-composition subsets of E1, plus pairwise removals (items 1+3 and 2+3) on 300 games x 2 seeds = 1,200 episodes for non-additivity under each endpoint. E3 replace ground truth: 300 games x 2 seeds x 4 = 2,400 episodes with token-matched cross-type replacement. E4 static-procedure net: 300 games x 2 seeds x 4 = 2,400 episodes with the Measurement C procedure sentence present. E5 consumer swap: 300 games x 2 seeds x 4 = 2,400 episodes under the second local backbone. E6 store size: 50% random bank, 300 games x 2 seeds x 4 = 2,400 episodes. E7 surrogate index: logistic regression of success on the process endpoints fit on intact-set runs of one half of games and applied to the LOO re-runs of the other half, and vice versa; no extra episodes. Analyses per endpoint Z: delta_Z per (item, game, seed); crossed variance components; reliability curve R_Z(n) by retrieval subsampling; n_Z(0.7) and savings = n_success(0.7) / n_Z(0.7); disattenuated Spearman between item means under Z and under success on natural items with >= 20 retrievals; class means under Z (in SD of natural-item values) against class means under success (net points). Total about 19,000 episodes, about 16 h with both replicas busy; pre-registration after E0 and a 500-episode seed-variance pilot.",
 "Baselines and Ablations": "Success-LOO as the reference estimator; each raw process endpoint; the cross-fitted surrogate index; offline surrogates (teacher-forced expert log-probability change; DIG-style confidence gain); an early-halt variant (re-runs truncated at 50% of the step limit and scored by progress) as the cheapest process surrogate; REMOVE vs REPLACE; three manufactured classes against natural items; natural vs forced composition; single vs pairwise removal; gross vs static-procedure net; two readers; two store sizes; index fitted with and without the first-divergence feature to see which endpoint carries the bias.",
 "Falsifiable Predictions": "P1 Savings: goal-condition-progress LOO reaches reliability 0.7 with at most one third of the retrievals success-LOO needs (savings >= 3x); falsified if savings < 1.5x (E1, the same re-runs scored under both endpoints); not entailed because progress may be as bimodal as success. P2 Class bias: steps-to-success and first-divergence endpoints assign the location-stale class a value <= -0.3 SD of natural-item values while the class's success-LOO is within +/-3 net of zero; falsified if the stale class's success-LOO is <= -5 net (the surrogate would then be right, not biased) or if the step endpoint puts the stale class within +/-0.1 SD of zero (E1 stale cell); the redundant-duplicate class is a negative control expected within +/-3 net and +/-0.1 SD under every endpoint, and any endpoint assigning it |value| > 0.3 SD is reported as a false positive of that endpoint. P3 Calibrated index: the cross-fitted surrogate index keeps disattenuated Spearman >= 0.8 with success-LOO on natural items, class means within +/-3 net of success-LOO for all three classes, and savings >= 2x; falsified if Spearman < 0.6, any class bias > 5 net, or savings < 1.5x (E7). P4 Offline surrogates: teacher-forced expert log-probability change has disattenuated Spearman < 0.4 with success-LOO on natural items and separates planted-wrong from location-stale items with AUC < 0.7; falsified if Spearman >= 0.6 or AUC >= 0.85 (E0 vs E1). P5 Non-additivity detection: pair-minus-sum-of-singles is detected with CI excluding zero for at least twice as many pairs under the progress endpoint as under success; falsified if the ratio is <= 1.2 (E2 pairs scored under both endpoints); not entailed because interactions may live only in the success endpoint. P6 Consumer swap and store size: the sign pattern of P2 (stale class negative under step endpoints, near zero under success) replicates under reader 2, falsified if reader 2's step endpoint gives the stale class >= -0.1 SD or its success-LOO <= -5 net (E5); the progress-endpoint savings factor changes by less than 2x between full and half bank, falsified if it changes by >= 2x (E6). P7 Static net: with the procedure sentence present the stale class keeps a step-endpoint value <= -0.3 SD (location information is not captured by a type-level procedure) while the planted-wrong class's success-LOO harm shrinks by >= 50%; falsified if the stale value moves within +/-0.1 SD or the planted harm shrinks by < 20% (E4).",
 "Measurement and Noise Control": "Every endpoint is computed on the same re-runs, so comparisons between endpoints are within-episode paired and their reliability differences are bootstrapped over games and items with the pairing preserved; disattenuation uses each endpoint's own measured reliability. Class cells are sized to +/-5 net on the success endpoint (about 400 forced retrievals per class at within-class SD about 0.45, confirmed in the pilot); natural-item statements use >= 100 items with >= 20 retrievals. The surrogate index is cross-fitted across game halves to avoid in-sample optimism; the goal-condition metric is validated against the environment success flag (fraction 1 if and only if success) before use. Sampling temperature fixed and reported; seed component measured first; all thresholds pre-registered; both replicas busy (E0 on one GPU while E1 runs on the other) with throughput logged per cell.",
 "Preprint Collision Check": "All queries answered by the literature command (Semantic Scholar + HF Papers, both ok); WebSearch not used. (1) home: 'surrogate index variance reduction control variates online experiments CUPED long-term outcome': no CUPED or surrogate-index paper returned (Deng et al. 2013 and Athey et al. 2019 are cited from memory); nearest returned items are a model-free surrogate for survival endpoints arXiv:2412.14129 and control-variate papers arXiv:2109.08944, arXiv:2305.00402, arXiv:2212.00517; nothing applies surrogate endpoints to per-item counterfactual valuation. (2) mechanism, --recent: 'progress-based surrogate outcome instead of binary success variance reduction LLM agent evaluation fewer rollouts': EarlyEval arXiv:2609.02783 (2026-09-02; early outcome prediction to halt evaluation runs; aggregate accuracy, not per-item counterfactuals, no class bias), VIGOR arXiv:2607.22002 (rollout allocation by reward variance), Progress Advantage arXiv:2606.26080 and ProgRM arXiv:2505.18121 (progress rewards for training), SEAGym arXiv:2606.17546; none estimates per-item value. (3) closest named method: DIG (digest card arXiv:2509.12765) and the RAG Shapley query 'Shapley attribution retrieved documents RAG LLM calls approximation redundancy evidence utility intervention', which returned only arXiv:2507.04480 (answer-level attribution, single-shot). (4) --recent 'per-item value of retrieved memory leave-one-out noise seeds sample size LLM agent' returned nothing on surrogate endpoints (Echo Gap arXiv:2608.00017, MEMPROBE arXiv:2606.24595 unrelated). No preprint reports a re-run savings factor or a class-bias map for process-endpoint estimates of memory item value.",
 "Risk Factors and Limitations": "Goal-condition fraction may require a custom PDDL predicate check in the ALFWorld text engine (implementation risk; fallback is subgoal completion inferred from the expert plan's object states). Items that induce short failing episodes (early done) can game step-based endpoints; the first-divergence and progress endpoints and the index are expected to expose this, and it is reported if not. The surrogate index's bias correction assumes surrogacy holds across classes, which P3 tests and may reject. Results depend on ALFWorld's procedural structure with clear subgoals and may not transfer to tasks without decomposable progress. Location-stale items are an ALFWorld analogue of staleness, not temporal drift. The second-backbone serving must be verified before E5; total compute is about 16 h on two A100s.",
 "Addresses gap": "G24 (sample and compute cost of per-item estimates: the re-run savings factor is the estimand) and G22 (offline proxy signals such as DIG-style confidence gain are checked against counterfactual removal of the same item).",
 "Not a restatement of": "Nearest brief bullet: 'Cost: a leave-one-out re-run of one episode costs one episode; Shapley over a k=3 set costs 7 re-runs per episode' - the brief prices ground truth per re-run on the binary outcome; this idea claims the same re-run carries a lower-variance endpoint whose class-specific bias can be measured and corrected, and measures both the savings and the bias. Nearest digest card: arXiv:2509.12765 (DIG scores one document by confidence change, never checked against counterfactual removal, interactions and transfer untested) - this idea checks DIG-style and teacher-forced offline surrogates plus three process endpoints against success-LOO in a multi-step agent, under two compositions, two readers and two store sizes, with class-level bias as a reported quantity. Nearest archived idea: memory_item_value_reliability had no intervention arm; here success-LOO remains the anchor and the question is what else each intervention re-run measures."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "surrogate_endpoints_for_item_credit",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "E1's 8,000 re-runs scored under both the binary success flag and goal-condition progress, with R_Z(n) from retrieval subsampling and savings = n_success(0.7) / n_progress(0.7).",
   "falsifier": "Savings < 1.5x.",
   "label": "open",
   "reason": "Nothing in the design forces the variance ratio - progress may be as bimodal as success (its validation that progress = 1 iff success even pins its top mass to the binary) - and the 3x versus 1.5x gap is wide relative to a paired bootstrap over 1,000 games and items; the residual weakness is that n(0.7) is extrapolated well beyond the 13-20 retrievals per item actually observed.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "E1's 30 forced location-stale items (about 400 forced retrievals for the class), class means under steps-to-success and first-divergence in SD of natural-item values versus the class's success-LOO in net points, with class cells sized to +/-5 net on success.",
   "falsifier": "The stale class's success-LOO is <= -5 net, or the step endpoint puts the stale class within +/-0.1 SD of zero.",
   "label": "unresolvable",
   "reason": "The prediction asserts the stale class's success-LOO lies within +/-3 net of zero while its own falsifier sits at -5 net, yet the class cell is explicitly sized to a +/-5 net CI, so 'no success effect' and 'the surrogate was right, not biased' cannot be told apart; the step-endpoint branch meanwhile restates how the stale class was manufactured (a wrong location lengthens the path by construction).",
   "fix": "Size the stale class to +/-2 net on the success endpoint (roughly 2.5x the forced retrievals) and pre-register the null as an equivalence test with bounds outside the resulting CI."
  },
  {
   "id": "P3",
   "depends_on": "E7's cross-fitted logistic regression of success on the process endpoints (fit on intact runs of one game half, applied to the other half's LOO re-runs), disattenuated Spearman against success-LOO on natural items with >= 20 retrievals, plus class means and savings.",
   "falsifier": "Disattenuated Spearman < 0.6, any class bias > 5 net, or savings < 1.5x.",
   "label": "near_entailed",
   "reason": "Disattenuation divides by the square root of each arm's own measured reliability, and success-LOO's reliability at 20 retrievals is the low value this whole program predicts, so the divisor inflates the estimate two- to threefold and a raw correlation near 0.3 already clears 0.8; the index is moreover fitted to predict success, so 'class means within +/-3 net of success-LOO' largely restates that the regression is calibrated rather than testing it.",
   "fix": "Pre-register the raw un-disattenuated Spearman with a bootstrap CI and a floor on each arm's reliability, and hold the three manufactured classes entirely out of the index fit."
  },
  {
   "id": "P4",
   "depends_on": "E0's teacher-forced expert log-probability change on 2,000 k=3 episodes against E1 success-LOO item means (disattenuated Spearman on natural items), and its separation of the 30 planted-wrong from the 30 location-stale items.",
   "falsifier": "Disattenuated Spearman >= 0.6, or planted-versus-stale AUC >= 0.85.",
   "label": "open",
   "reason": "Here the same disattenuation inflation pushes against the prediction rather than for it, and the mechanism makes the falsifier plausible - a wrong-procedure item contradicts the expert action tokens while a stale-location item need not - with the 0.7-to-0.85 AUC gap running about two SE at 30 versus 30 items.",
   "fix": ""
  },
  {
   "id": "P5",
   "depends_on": "E2's pairwise removals of position pairs 1+3 and 2+3 on 300 games x 2 seeds (about 600 paired episodes per pair), with pair-minus-sum-of-singles scored under progress and under success.",
   "falsifier": "The ratio of pairs detected under progress to pairs detected under success is <= 1.2.",
   "label": "unresolvable",
   "reason": "Only two position-pairs are run, so 'at least twice as many pairs' is a ratio over a denominator of at most 2 and undefined at 0 versus 0; read instead at the item-pair level each pair carries only a handful of episodes so neither endpoint's CI excludes zero, and the ratio is in any case a monotone restatement of the P1 variance ratio rather than an independent test.",
   "fix": "Define the estimand over >= 30 named item pairs with >= 20 paired episodes each and report the detection RATE with a paired bootstrap CI under both endpoints."
  },
  {
   "id": "P6",
   "depends_on": "E5 (300 games x 2 seeds x 4 under a second local backbone) for the P2 sign pattern, and E6 (50% random bank, same size) for the progress-endpoint savings factor.",
   "falsifier": "Reader 2's step endpoint gives the stale class >= -0.1 SD or its success-LOO <= -5 net; or the savings factor changes by >= 2x between full and half bank.",
   "label": "unresolvable",
   "reason": "E5 and E6 are 2,400-episode cells, so each forced class receives roughly a quarter of E1's ~400 forced retrievals (CI nearer +/-9-10 net than the +/-5 net E1 was sized for), putting the -5 net branch inside the noise, while the savings factor is a ratio of extrapolated n(0.7) values whose CI on a cell that small easily spans a 2x change in either direction.",
   "fix": "Size E5 and E6 to E1's ~400 forced retrievals per class and pre-register a bootstrap CI on the savings ratio so that the 2x boundary lies outside it."
  },
  {
   "id": "P7",
   "depends_on": "E4 (300 games x 2 seeds x 4) with the Measurement C type procedure sentence present: the stale class's step-endpoint value in SD, and the planted-wrong class's success-LOO harm relative to its E1 value.",
   "falsifier": "The stale class's step value moves within +/-0.1 SD, or the planted-wrong harm shrinks by < 20%.",
   "label": "unresolvable",
   "reason": "The stale branch is excluded by construction - a type-level procedure sentence cannot carry instance-level location information, which is exactly the reason the proposal gives for the penalty persisting - and the surviving branch is a ratio of two class means (E4 at roughly +/-9-10 net against E1 at +/-5 net, on largely different games), so a 50% shrink cannot be separated from a 20% one.",
   "fix": "Add an instance-location control sentence so the stale branch can actually fail, and run the procedure-sentence arm paired on the same forced-class episodes at E1's class size."
  }
 ],
 "shared_terms": [
  "P1-P3: P3's savings >= 2x is the same n_Z(0.7) ratio as P1's savings >= 3x computed from the same reliability curves on the same re-runs, so P1 largely implies P3's savings clause.",
  "P1-P5: P5's detection-count ratio between endpoints is a monotone function of the very variance ratio P1 asserts, so the two cannot fail independently.",
  "P2-P6: P6's first clause is P2's estimand (stale class negative under step endpoints, near zero under success) re-measured under reader 2 with the same class definition and thresholds.",
  "P2-P7: P7's stale-class step value and planted-harm shrinkage are ratios taken against the same E1 class means that P2 reports, so a mis-estimated E1 class mean moves both.",
  "P3-P4: both are disattenuated Spearmans against the same success-LOO item means, so the shared reliability divisor inflates P3 toward its >= 0.8 threshold and P4 toward its >= 0.6 falsifier at the same time."
 ],
 "headline": "P1",
 "headline_status": "open",
 "n_open": 2,
 "n_entailed": 0,
 "n_near": 1,
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
