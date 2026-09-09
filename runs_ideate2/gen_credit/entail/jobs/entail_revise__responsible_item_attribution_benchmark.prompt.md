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
 "Name": "responsible_item_attribution_benchmark",
 "Title": "Which Item Did It? A Seed-Replicated Intervention Benchmark for Attributing Agent Failures to Retrieved Memory Items",
 "Short Hypothesis": "A failed ALFWorld episode can be attributed to a specific retrieved memory item only by seed-replicated intervention (removing or token-replacing each item and re-running the same game under m seeds); against that ground truth, the cheap attributions current systems rely on - the reader's self-report, teacher-forced confidence gain over the failed trajectory, position priors, single-seed leave-one-out - identify the responsible item at accuracies we predict below 70%, which fall further when a redundant helpful item is co-retrieved, and most natural failures are not attributable to any single item at all.",
 "Related Work": "Agentic memory benchmarks score end-to-end outcomes only (Evo-Memory arXiv:2511.20857, MemoryArena arXiv:2602.16313, MemoryAgentBench arXiv:2507.05257, MINTEval arXiv:2605.18565, Memora arXiv:2604.20006) and never attribute a failure to an item (G21). CUE-R (arXiv:2604.05467) and Shapley source attribution (arXiv:2507.04480) intervene per document but in single-shot RAG, without seed replication or cost accounting. Failure attribution for agents exists at the step or agent level: CausalFlow (arXiv:2605.25338, causal responsibility scoring of failure-inducing steps plus counterfactual repair), A2P (arXiv:2509.10401) and ErrorProbe (arXiv:2604.17658) for multi-agent systems, and root-cause benchmarks (arXiv:2509.23735); the retrieved memory item is never the unit. The compliance trap (arXiv:2607.10608) diagnoses adoption of conflicting memory at trajectory level without item-level ground truth or composition arms. Self-explanation faithfulness work (arXiv:2401.07927, arXiv:2307.08678, CC-SHAP arXiv:2311.07466, arXiv:2602.02639) shows self-reports are often unfaithful in classification; nobody has tested self-reported memory use against counterfactual re-runs. Archived retrieved_set_disagreement_gate made a set-level harm claim without item-level ground truth.",
 "Abstract": "When a memory-augmented agent fails, which retrieved item, if any, is responsible? No agent-memory benchmark answers this, and the systems that reinforce or demote items on failure use attributions whose accuracy has never been measured. We define item responsibility by intervention: for each failed (game, seed, retrieved set) we re-run the same game with the set intact, with each item removed, and with each item token-replaced, under m = 6 seeds, and call an item responsible when its removal raises the success rate by at least 0.5 with a one-sided 90% interval excluding zero. On about 250 natural failures of Qwen3-32B at k=3 (valid splits plus a train-stream pool) and about 270 manufactured failures with a known culprit (a planted wrong-procedure item at position 1 or 3, with and without a duplicated helpful item), this costs 42 re-runs per failure. We score attribution methods by top-1 identification accuracy on attributable episodes, abstention on non-attributable ones, rank correlation with the responsibility score, own-seed stability and LLM-call cost: position prior, self-report elicited from the reader after the episode, teacher-forced confidence gain of the failed action sequence with and without each item, a semantic-overlap heuristic, single- and few-seed leave-one-out, and exact Shapley over the eight subsets. Static-procedure, second-reader and composition arms are separate cells. The benchmark releases per-episode responsibility labels with intervals, the accuracy-versus-seeds curve that says how many re-runs a label needs, and the cost frontier of the estimators.",
 "Experiments": "E0 (free): position prior from the k-sweep logs (which position's items co-occur with failure), and a 500-episode seed-variance pilot at the pre-registered temperature. E1 natural failure pool: 274 valid games x 2 seeds plus 500 train games x 2 seeds at k=3 (1,548 episodes); expected about 250 failures; each failure gets 6 base re-runs, 3 x 6 LOO re-runs and 3 x 6 token-matched REPLACE re-runs (42 per failure, about 10,500 episodes, about 9 h). Responsibility r_i = p(S minus i) - p(S) with Wilson/Newcombe intervals; attributable if max_i r_i >= 0.5 with one-sided 90% CI excluding 0; multi-responsible if two items each have r_i >= 0.4. E2 manufactured compositions (positive control with known culprit): 300 episodes with a planted wrong-procedure item inserted at position 1 or 3 into the natural set (expected about 60% failures, about 180 x 42 = 7,560 episodes), and 150 episodes with the planted item plus a paraphrased duplicate of the top helpful item (two partial supports; about 90 x 42 = 3,780 episodes). E3 attribution methods on every failed episode, with cost logged: position prior (0 calls); self-report (one extra call, forced choice over the k items plus 'none', two prompt variants, repeated over 3 seeds for own-stability); teacher-forced confidence gain of the failed action sequence with vs without each item (3 forward passes, no environment steps); semantic overlap between item text and the failing action (0 calls); single-seed LOO and m-seed LOO for m in {2,3,4} subsampled from E1 (no extra cost); exact Shapley over 2^3 subsets on 100 attributable episodes x 6 seeds (4 extra subset re-runs per seed, 2,400 episodes). E4 static-procedure net: 150 natural failures re-measured with the type procedure sentence present (6,300 episodes): fraction that remain attributable to an item. E5 consumer swap: 100 attributable episodes re-measured under the second local backbone (4,200 episodes, faster on a smaller model): overlap of responsible items across readers and method accuracies under reader 2. Total about 35,000 episodes, about 29 h on two replicas with E5 on the second replica in parallel; pre-registration after E0.",
 "Baselines and Ablations": "Position prior and random choice as floors; oracle (planted culprit) as ceiling in E2; m in {1,2,3,4,6} seeds for the accuracy-versus-seeds curve; REMOVE vs REPLACE ground truth; planting at position 1 vs 3; natural vs planted vs planted-plus-duplicate compositions; Shapley vs LOO top-1 disagreement as the additivity test; self-report with two elicitation prompts; confidence gain computed on the failed actions vs on the expert action sequence; gross vs static-procedure-net attributability; reader swap.",
 "Falsifiable Predictions": "P1 Self-report: top-1 accuracy on attributable natural failures is <= position prior + 10 points; falsified if >= prior + 20 with a bootstrap CI excluding prior + 10 (E3 self-report on the E1 attributable set). Positive control: on E2 planted failures self-report must exceed 60%, otherwise the elicitation is judged broken and P1 is reported as uninterpretable. P2 Confidence gain: the teacher-forced confidence-gain method ranks the responsible item first in < 50% of attributable natural failures; falsified if >= 65% (E3 on E1). P3 Seeds: single-seed LOO agrees with the 6-seed label in < 70% of attributable episodes and the accuracy-versus-m curve first exceeds 85% at m >= 4; falsified if single-seed agreement is >= 85% (E3 subsampling of E1; no extra cost). P4 Attributability: at most 40% of natural failures are attributable to a single item; falsified if >= 60% are (E1). P5 Composition: in the planted-plus-duplicate composition the multi-responsible fraction is >= 25% and every single-output method loses >= 15 points relative to the planted-only composition; falsified if the multi-responsible fraction is < 10% or the loss is < 5 points (E2 vs E2-duplicate); Shapley and LOO disagree on the top-1 item in >= 20% of those episodes; falsified if < 5% (E3 Shapley cell). P6 Consumer swap: the responsible item is the same under reader 2 in < 50% of attributable episodes; falsified if >= 70% (E5). P7 Static net: >= 50% of natural attributable failures become non-attributable or succeed at base when the type procedure sentence is present; falsified if < 25% (E4).",
 "Measurement and Noise Control": "Responsibility scores are differences of two 6-seed success proportions (SE 0.2-0.29), so the attributable threshold (0.5 with a one-sided 90% interval excluding zero) deliberately labels only large effects; the full r_i distribution is released so users can re-threshold. Accuracies are compared on the same episodes (paired; McNemar) with bootstrap CIs over episodes; with about 100 attributable natural episodes the accuracy CI is about +/-9 points, so every method margin above is >= 10 points and the benchmark's headline numbers are reported with that width; E2 provides about 180 known-culprit episodes (+/-7 points). Sampling temperature is fixed and reported; the seed component is measured in the pilot; own-stability of each method is reported over 3 seeds; thresholds and margins are pre-registered; both replicas busy with throughput logged per cell.",
 "Preprint Collision Check": "All queries answered by the literature command (Semantic Scholar + HF Papers, both ok); WebSearch not used. (1) mechanism, --recent: 'attribute agent failure to a specific retrieved memory item counterfactual re-run responsible item': CausalFlow arXiv:2605.25338 (verified with s2cli paper: step-level causal responsibility scoring and counterfactual repair of failed agent traces; not item-level, no seed-replication or cost report), ErrorProbe arXiv:2604.17658 and A2P arXiv:2509.10401 (agent/step-level attribution in multi-agent systems), root-cause benchmark arXiv:2509.23735, Compliance Trap arXiv:2607.10608 (trajectory-level diagnosis), Phantom Guardrails arXiv:2607.13083 (invented failures). None attributes failures to retrieved memory items with intervention ground truth. (2) home: 'faithfulness of self-explanations counterfactual test which input feature was used language model': arXiv:2401.07927, arXiv:2307.08678, CC-SHAP arXiv:2311.07466, arXiv:2502.18156, arXiv:2602.02639 - self-report faithfulness is tested for classification and reasoning, never for which retrieved item an agent followed. (3) closest named method: 'Shapley attribution retrieved documents RAG LLM calls approximation redundancy evidence utility intervention': only arXiv:2507.04480 (Source Attribution in RAG, PKDD/ECML workshops, 7 citations); single-shot, no stability across calls. (4) 's2cli paper 2605.25338' confirmed the CausalFlow abstract. No preprint provides item-level responsibility labels with seed replication, a seeds-to-label curve, or an accuracy-cost frontier of attribution methods.",
 "Risk Factors and Limitations": "Failures at k=3 are about 15% of episodes, so the natural pool depends on the train-stream games; if the failure rate is lower, E1 is extended (each extra 100 failures cost 4,200 episodes). The responsibility threshold is a design choice; the released r_i distribution mitigates it. Negative results for self-report depend on elicitation; two prompts and the planted positive control guard this. Ground truth costs 42 re-runs per failure, so the benchmark is a fixed labelled set rather than a live evaluator. Teacher-forced confidence gain needs local forward passes outside vLLM (feasible on one GPU, slower). Multiplicity across seven predictions is handled by pre-registration and reporting all of them. The second-backbone serving must be verified before E5.",
 "Addresses gap": "G21 (no benchmark attributes a failure to a specific retrieved item in multi-step persistent-memory agents); secondarily G24 (seeds and LLM-call cost of a per-item label) and G25 (composition arm with a duplicated support).",
 "Not a restatement of": "Nearest brief bullet: 'Retrieval logs hold per episode the retrieved item ids in rank order, so a nested-k design gives one crude per-position counterfactual for free' - a per-position aggregate cannot name the item responsible for a given failure; this idea produces per-episode item responsibility labels with seed replication and scores attribution methods by accuracy and cost. Nearest digest card: arXiv:2604.05467 (CUE-R measures per-evidence utility by intervention in single-shot RAG; cost and variance unreported) - this idea works on multi-step trajectories, measures how many seeds a label needs, and defines attributability and multi-responsibility as reported quantities. Nearest archived idea: retrieved_set_disagreement_gate claimed harm lives in the set without item-level ground truth; here the item-level ground truth exists and the set-versus-item question is answered by the multi-responsible fraction."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "responsible_item_attribution_benchmark",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "E3 self-report (forced choice over the k items plus 'none', two prompt variants) scored against E1's argmax-r_i label on about 100 attributable natural failures, compared with the E0 position prior under paired McNemar.",
   "falsifier": "Self-report top-1 accuracy >= prior + 20 points with a bootstrap CI excluding prior + 10.",
   "label": "near_entailed",
   "reason": "The ground-truth label is the argmax of three r_i, each a difference of two 6-seed proportions with SE 0.2-0.29 and selected at max r_i >= 0.5, so a substantial share of labels is selection noise that caps any method's attainable accuracy; the label's own test-retest is never measured, and the falsifier additionally needs about a 20-point margin against a +/-9-point accuracy CI.",
   "fix": "Add an independent second 6-seed replication of the same interventions to measure label test-retest, and state P1's margin relative to that measured ceiling."
  },
  {
   "id": "P2",
   "depends_on": "E3 teacher-forced confidence gain of the failed action sequence with vs without each item, ranked against the same E1 argmax label on attributable natural failures.",
   "falsifier": "Confidence gain ranks the responsible item first in >= 65% of attributable natural failures.",
   "label": "near_entailed",
   "reason": "The mechanism actually favours the method (a culprit item by definition raises the probability of the failed actions it induced), so the falsifier is mechanically plausible, but 65% is scored against an unreplicated argmax label whose instability the proposal never measures and whose magnitude P3 implies is large, so the threshold may sit above the label's ceiling rather than above the method's ability.",
   "fix": "Measure the 6-seed label's test-retest agreement on a disjoint seed block and express P2's threshold as a fraction of that ceiling."
  },
  {
   "id": "P3",
   "depends_on": "E3 subsampling of m in {1,2,3,4,6} seeds from the SAME six E1 seeds that define the 6-seed ground-truth label, with agreement measured as argmax match over 3 items.",
   "falsifier": "Single-seed LOO agrees with the 6-seed label in >= 85% of attributable episodes.",
   "label": "entailed",
   "reason": "A single binary re-run per item yields deltas in {-1,0,1} with pervasive three-way ties, so an argmax over 3 items cannot match a 6-seed label at 85%, and the accuracy-versus-m curve is nested inside the very seeds that define the label (agreement is 1.0 at m=6 by construction and inflated at m=4 by four shared seeds), so both clauses are artifacts of subsampling rather than evidence about replication.",
   "fix": "Build the m-seed curve from a disjoint block of fresh seeds against a label defined by the original six, and pre-register the tie-breaking rule for the single-seed argmax."
  },
  {
   "id": "P4",
   "depends_on": "E1's attributability rule (max_i r_i >= 0.5 with a one-sided 90% CI excluding 0), where r_i is a difference of two 6-seed proportions with SE 0.2-0.29, over about 250 natural failures.",
   "falsifier": ">= 60% of natural failures are attributable to a single item.",
   "label": "entailed",
   "reason": "At SE 0.2-0.29 the CI condition is nearly implied by the 0.5 threshold and a true effect of exactly 0.5 is detected only about half the time, so the observed attributable fraction is roughly half the true decisive-item rate plus about 7% per-episode false positives - reaching 60% would require essentially every natural failure to contain a decisive item, and no arm varies m or the threshold to distinguish a low rate from low power.",
   "fix": "Raise m to >= 12 seeds for the labelling pass, or calibrate the attributability threshold to 80% detection power on the E2 known-culprit episodes and state P4 at that calibrated threshold."
  },
  {
   "id": "P5",
   "depends_on": "E2-duplicate (150 episodes, about 90 failures x 42 re-runs) with a planted wrong-procedure item plus a paraphrased duplicate of the top helpful item, versus the planted-only composition; multi-responsible defined as two items each with r_i >= 0.4; plus the E3 Shapley cell.",
   "falsifier": "Multi-responsible fraction < 10%, or single-output methods lose < 5 points, or Shapley-LOO top-1 disagreement < 5%.",
   "label": "open",
   "reason": "The falsifier is disjunctive and its first branch is what the construction should actually produce - r_i >= 0.4 requires a HARMFUL item, but the duplicated pair is helpful and mutually redundant, so removing either copy leaves the other in place and drives each copy's r_i toward zero - making the falsifying outcome not merely reachable but the expected one.",
   "fix": ""
  },
  {
   "id": "P6",
   "depends_on": "E5 re-measurement of 100 attributable episodes under a second local backbone (4,200 episodes, same 6-seed LOO design), compared item-by-item with reader 1's argmax label.",
   "falsifier": "The same responsible item is identified under reader 2 in >= 70% of attributable episodes.",
   "label": "near_entailed",
   "reason": "Two independently noisy argmax labels can agree at most at about the product of their own reliabilities, and no same-reader replication arm ever establishes that ceiling, so agreement below 70% follows from label noise alone and needs no reader difference at all.",
   "fix": "Add a reader-1 replication arm (fresh six seeds, same backbone, same episodes) as the agreement ceiling and report cross-reader agreement normalized by it."
  },
  {
   "id": "P7",
   "depends_on": "E4 re-measurement of 150 natural failures previously SELECTED as attributable, now with the type procedure sentence present (6,300 episodes), compared with their original E1 selecting measurement.",
   "falsifier": "< 25% of attributable natural failures become non-attributable or succeed at base.",
   "label": "entailed",
   "reason": "The 150 episodes were selected on max r_i >= 0.5 from estimates with SE 0.2-0.29, so regression to the mean alone drops a large fraction below the threshold on any re-measurement, and the design contains no procedure-sentence-absent re-measurement arm to net that out - the >= 50% loss can be produced with the intervention doing nothing.",
   "fix": "Re-run the same 150 selected failures with fresh seeds and NO procedure sentence as a control arm, and define P7 as the difference between the two re-measurements."
  }
 ],
 "shared_terms": [
  "P3-P4: the m-seed agreement curve and the attributable-set definition are computed from the same six E1 seeds, and the m-seed estimates are nested subsets of the seeds defining the label, so agreement is 1.0 at m=6 by construction.",
  "P1-P2: both accuracies are scored against the same argmax label on the same ~100 attributable episodes, so the label's unmeasured error rate caps and co-moves both.",
  "P1-P6 and P2-P6: reader-2 method accuracies and the cross-reader item agreement rest on the same reader-1 label, so a noisy label depresses all three simultaneously.",
  "P4-P5: the multi-responsible criterion (r_i >= 0.4) is the same statistic as P4's attributability rule (0.5) at a nested threshold on the same r_i estimates.",
  "P4-P7: P7's 'become non-attributable' is P4's threshold statistic re-applied to the very sample P4's threshold selected."
 ],
 "headline": "P3",
 "headline_status": "entailed",
 "n_open": 1,
 "n_entailed": 3,
 "n_near": 3,
 "n_unresolvable": 0,
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
