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
 "Name": "masked_harm_pairwise_removal",
 "Title": "Masked Harm, Masked Help: Single-Item Removal Mis-scores Conflicting and Redundant Co-retrieved Experience, and the Pairwise Correction Costs Three Re-runs, Not Seven",
 "Short Hypothesis": "In a multi-step agent, the leave-one-out credit of a retrieved item is masked by its co-retrieved neighbour in a sign-predictable way: a planted wrong-procedure item's harm shrinks when a correct item is co-retrieved (unless the compliance trap makes the agent adopt it regardless), and a correct item's help shrinks when a twin is co-retrieved (unless duplication has a dose effect). A pruner scoring by single removal therefore keeps the wrong item and deletes the redundant one; the pairwise-removal interaction term, obtained with one extra re-run per pair, recovers the decision at less than half the cost of exact Shapley on k=3.",
 "Related Work": "Shapley source attribution in RAG (arxiv:2507.04480) reports redundancy, complementarity and synergy among retrieved documents in single-shot QA but does not measure how much a single-removal score is masked or what decision error results. Cross-component interference in agent scaffolds (arxiv:2605.05716) finds 56% submodularity violations with exact Shapley at the component level, not for retrieved items. CUE-R (arxiv:2604.05467) shows non-additive multi-hop supports in single-shot RAG. The compliance trap (arxiv:2607.10608) shows agents adopt conflicting memory at the first exposed decision point and that repeated exposure amplifies the error, but leaves untested whether the harm depends on co-retrieved correct entries; controlled memory interference (arxiv:2608.07622) uses synthetic relationships without per-item counterfactuals. RoMeRL's memory-reward trap (arxiv:2608.02508) is the training-side symptom of the same masking. Interaction indices (shapiq arxiv:2410.01649; Shapley-Taylor arxiv:2403.13106) supply the estimand; the archived retrieved_set_disagreement_gate proposed a set-level gate without item-level ground truth.",
 "Abstract": "Per-item credit is computed one item at a time, but items are consumed as a set. We manufacture k=3 retrieved sets for ALFWorld (Qwen3-32B reader) whose pairwise structure is known: correct expert item E plus a planted wrong-procedure item W (conflict), E plus a token-matched paraphrase E' (redundancy), the navigation and procedure halves of E as two items (complementarity), and E plus its natural second neighbour (natural sets), each with a cross-type filler F in the third slot and, for conflict, a second composition with a natural correct item in the third slot and a third with W in first position. For each set we run FULL, minus-i, minus-j and minus-both on the same (game, seed), giving single credits, pair credit and the interaction term; exact Shapley (7 re-runs) is run on the conflict and redundancy cells to check that pairwise removal recovers its ranking. We report the masking ratio per class, the fraction of sets in which a single-removal pruner deletes the wrong item, the recovery by the two-player Shapley within the pair, and the re-run cost of each. The compliance trap and the duplication dose effect are the published mechanisms that would falsify masking, so the experiment adjudicates between them.",
 "Experiments": "Sets on 274 valid games; items: E = natural rank-1 expert item, W = E with its procedure action swapped (heat<->cool, clean->heat, receptacle swapped for pick-and-place), E' = paraphrase of E token-matched within 10%, E_nav / E_proc = E split at the first procedure action, N2 = natural rank-2 expert item, F = token-matched cross-type expert trajectory. Compositions: A = (E1, X2, F3); B = (X1, E2, F3) (position swap); C (conflict only) = (E1, W2, N2_3) (natural correct third slot). Arms per set: v(FULL), v(-i), v(-j), v(-ij) with holes (k reduced), paired by (game, seed). Shared arms v(E,F) and v(F) serve all classes, so per composition the distinct arms are about 11 (conflict: v(EWF), v(WF); redundancy: v(EE'F), v(E'F); complementarity: v(E_nav E_proc F), v(E_nav F), v(E_proc F); natural: v(E N2 F), v(N2 F); shared: v(EF), v(F)). Budget: composition A headline cells (conflict, redundancy, shared) at 4 seeds (6 arms x 1,096 = 6,576), remaining A arms and all of B at 2 seeds (about 16 arms x 548 = 8,768), composition C (4 arms x 548 = 2,192), exact Shapley completion on A conflict and redundancy (v(EW), v(EE'), v(E), v(W), v(E'); k=0 from logs) 5 x 548 = 2,740, consumer-swap arm (conflict A, 4 arms x 548 = 2,192 on the second backbone): about 22,500 episodes, about 19 h at 20 episodes/min on two replicas. Order: the W-alone positive control v(WF) - v(F) runs first; if |harm| < 15 net, W is strengthened (wrong object and wrong procedure) before any confirmatory cell, per pre-registration. Analyses: masking ratio = credit with neighbour / credit without neighbour; interaction I = v(FULL) - v(-i) - v(-j) + v(-ij); per-set decision: single-removal pruner deletes argmin single credit (seed-averaged), pairwise pruner deletes argmin of the two-player Shapley phi_i = 0.5[(v(FULL) - v(-i)) + (v(-j) - v(-ij))]; Spearman between pairwise phi and exact Shapley on the completed cells. Exploratory on natural sets: does first-procedure-action disagreement between E and N2 predict |I| >= 10 (AUROC reported, no headline claim).",
 "Baselines and Ablations": "Single removal (1 re-run per item) vs pairwise removal (3 re-runs per set) vs exact Shapley (7 re-runs per set) as the cost axis; additive prediction (sum of single credits) vs measured pair credit as the additivity test; position swap (A vs B) and third-slot identity (F vs N2) as set-composition manipulations; natural sets as the realism control for manufactured ones; W-alone and E-alone cells as the unmasked references; paraphrase redundancy vs natural-neighbour redundancy; second backbone as a separate consumer-swap arm; seeds as a factor.",
 "Falsifiable Predictions": "- P1 (masked harm): |harm of W with E present| = |v(EWF) - v(EF)| is at most 0.5 x |v(WF) - v(F)|. Falsified if the ratio is >= 0.8 with its 95% CI excluding 0.5, which is what the compliance trap (adoption of the conflicting item at first exposure) predicts. Arm: composition A conflict and shared cells, 4 seeds (1,096 paired each).\n- P2 (masked help): help of E with the twin present, v(EE'F) - v(E'F), is at most 0.25 x help of E alone, v(EF) - v(F). Falsified if the ratio is >= 0.75 (duplication dose effect as in CUE-R DUPLICATE and the compliance trap's repeated-exposure amplification). Arm: composition A redundancy and shared cells, 4 seeds.\n- P3 (complementarity): the interaction of the navigation and procedure halves, v(E_nav E_proc F) - v(E_nav F) - v(E_proc F) + v(F), is at least +10 net. Falsified if it is <= +3 net, i.e. the procedure half alone carries the item's value (the procedure-bound result of the starting position points this way). Arm: composition A complementarity cells (548 paired).\n- P4 (decision error): a single-removal pruner deletes W in at most 55% of conflict sets, while the two-player Shapley within the pair deletes W in at least 80%. Falsified if single removal deletes W in >= 75% of sets (its masking is too small to change the decision). Arm: composition A conflict cell, per-set credits averaged over 4 seeds, rate over 274 sets (+/-6 points).\n- P5 (position dependence of masking): the P1 masking ratio in composition B (W first) exceeds that in composition A by at least 0.3 (earlier exposure makes W adopted before E is read). Falsified if the difference is <= 0.1 in either direction. Arm: composition A vs B conflict cells.\n- P6 (pairwise recovers Shapley): Spearman between the two-player phi and exact Shapley across conflict and redundancy sets is >= 0.8. Falsified if <= 0.5 (the third item's interactions matter, so pairwise removal does not suffice). Arm: the Shapley-completed cells.",
 "Measurement and Noise Control": "All contrasts paired by (game, seed); +/-8 net per 548-episode cell and +/-5.7 per 1,096-cell; ratio predictions are differences of two cells (about +/-8 at 4 seeds), so P1/P2 thresholds are set 0.3 apart on bases the positive control must show to be >= 15 net (W-alone harm) and >= 20 net (E-alone help, expected from k=1 vs k=0 = +20); cluster bootstrap over games with seed as a factor; per-set decision rates use seed-averaged credits and are reported with the per-set noise (binary outcomes over 4 seeds) so that the rate under pure noise (50%) is the explicit null; prompt hashes, token counts and item ids logged; retrieval frozen from the logs; both GPUs busy, workers tuned to the vLLM running queue; pre-registration of thresholds after the positive-control cell and before confirmatory cells.",
 "Preprint Collision Check": "- mechanism (last 12 months): query 'conflicting retrieved memory compliance trap agent success collapse' --recent, channel s2cli (S2+HF, both ok): arxiv:2607.10608 (compliance trap, trajectory-level, no co-retrieved composition test), arxiv:2608.04574 (stale spatial memory in VLM agents), TrustMem arxiv:2606.25161, StateFuse arxiv:2607.05844, arxiv:2605.30087 (conflicting personal memory QA); none measures masking of a single-item counterfactual by a co-retrieved item.\n- closest named method: query 'Shapley value attribution of retrieved documents in retrieval-augmented generation', channel s2cli: arxiv:2507.04480 (SHAP approximations, redundancy/synergy noted, single-shot), RAG-E (S2, no arXiv id), arxiv:2605.27105 (position effects); no decision-error or masking measurement.\n- closest named method: query 'intervention-based per-evidence utility remove replace duplicate retrieval-augmented generation' --recent, channel s2cli: CUE-R arxiv:2604.05467, CoRM-RAG arxiv:2605.01302; single-shot only.\n- home: query 'pairwise interaction index Shapley additivity violation redundancy synergy', channel s2cli: shapiq arxiv:2410.01649, Shapley-Taylor interactions in LMs arxiv:2403.13106, arxiv:2605.05716 (component-level interference in agents), FL-I2MoE arxiv:2603.13326 (unique/synergistic/redundant evidence in multimodal models), OddSHAP arxiv:2602.01399; interaction indices exist, none applied to co-retrieved items with manufactured ground truth or to a pruning decision. No pre-emption found; WebSearch not used.",
 "Risk Factors and Limitations": "Manufactured W may be too weak (the reader ignores an implausible procedure) or too strong (any exposure collapses success), in which case the masking ratio is undefined or saturated; the positive-control-first rule and the pre-registered strengthening step address this. The filler F makes two thirds of the set synthetic; composition C and the natural class bound the realism cost. Per-set decision rates at 4 seeds carry binary noise, so the 50% null is stated. Paraphrase redundancy is cleaner than natural redundancy but less realistic; both are run. The exploratory disagreement detector is not a headline claim because on manufactured sets it is true by construction. Second-backbone serving unverified.",
 "Addresses gap": "G4 (per-item attribution computed one item at a time misses redundancy, conflict and complementarity among co-retrieved items; no item-level estimator captures it or reports the decision error it causes).",
 "Not a restatement of": "Brief bullet 'The gain is procedure-bound (clean/heat/cool +39 to +55) and unseen = seen': that bullet measures set-level value; this idea claims how that value is split among co-retrieved items is non-additive with a predictable sign, and P3 tests whether the navigation and procedure halves interact at all. Digest card arxiv:2605.05716 (component-level exact Shapley, 56% submodularity violations): that card scores scaffold components; this idea scores retrieved items with manufactured ground truth, measures the pruning decision a single-removal score gets wrong and the cost of the pairwise fix. Digest card arxiv:2607.10608 (compliance trap): that card shows harm from conflicting memory but leaves its dependence on co-retrieved correct items untested; here that dependence is the headline prediction and the compliance trap is the named falsifier. Archived retrieved_set_disagreement_gate (4.65) made a set-level claim without item-level ground truth; here every set has single, pairwise and Shapley counterfactuals."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "masked_harm_pairwise_removal",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "Composition A conflict cells v(EWF), v(WF) and shared cells v(EF), v(F) at 4 seeds (1,096 paired, +/-5.7 each; differences about +/-8), with a W-alone positive control required only to reach 15 net.",
   "falsifier": "|v(EWF) - v(EF)| / |v(WF) - v(F)| >= 0.8 with a 95% CI excluding 0.5 (compliance trap: W is adopted regardless of E).",
   "label": "unresolvable",
   "reason": "On the control's guaranteed base of 15 net the 0.5-vs-0.8 gap is 4.5 net against a stated +/-8 on each difference, so the ratio CI (numerator 12 +/- 8 over denominator 15 +/- 8) spans roughly 0.2 to 2.5 and cannot exclude 0.5 in either direction.",
   "fix": "Require the W-alone control to reach about 30 net (stronger W) or raise the conflict and shared cells to enough seeds that each difference CI is under 3 net, and restate the claim as a net-point difference (harm_alone - harm_with_E >= 10 net)."
  },
  {
   "id": "P2",
   "depends_on": "Composition A redundancy cells v(EE'F), v(E'F) and shared v(EF), v(F) at 4 seeds, with E' a paraphrase of E token-matched within 10%.",
   "falsifier": "Help of E with the twin present is >= 0.75 x help of E alone (a duplication dose effect).",
   "label": "near_entailed",
   "reason": "E' is by construction informationally identical to E, so the only route to the falsifier is a pure repetition/dose effect that the design has no arm to produce or isolate (no literal-duplicate or 3-copy cell, no partial-content twin), and the ratio's 0.25-vs-0.75 band (10 net on a 20-net base) sits at the stated +/-8 difference noise.",
   "fix": "Add a dose arm (v(EEF) literal duplicate, and a 3-copy set) and a partial-overlap twin so repetition strength is manipulated rather than assumed, and power the redundancy cells so the 10-net band exceeds the difference CI."
  },
  {
   "id": "P3",
   "depends_on": "Composition A complementarity cells v(E_nav E_proc F), v(E_nav F), v(E_proc F), v(F) at 2 seeds (548 paired, +/-8 per cell) with E split at its first procedure action.",
   "falsifier": "The four-term interaction is <= +3 net, i.e. the procedure half alone carries the item's value.",
   "label": "unresolvable",
   "reason": "A four-term interaction built from 548-episode cells carries roughly +/-11 to +/-16, far wider than the 7-net band between the predicted +10 and the falsifying +3.",
   "fix": "Run the complementarity cells at the 4-seed (or higher) budget used for the headline cells so the interaction CI is under 3.5 net, and state that interaction MDE explicitly rather than reusing the single-cell +/-8 floor."
  },
  {
   "id": "P4",
   "depends_on": "Per-set argmin of single-removal credits over the three items of composition A conflict, credits seed-averaged over 4 binary paired contrasts per set, rate across 274 sets (+/-6 points).",
   "falsifier": "Single removal deletes W in >= 75% of conflict sets (its masking is too small to change the decision).",
   "label": "entailed",
   "reason": "A per-set credit from 4 paired binary re-runs is quantized in 25-point steps with an SD near 25 net, so a true W-vs-E separation of 15-30 net gives an argmin that picks W only around half the time even with zero masking - the >= 75% falsifier is unreachable at this per-set estimator, and the paired >= 80% claim for the pairwise pruner has no falsification clause at all.",
   "fix": "Raise seeds per set to >= 16 (or use hierarchical shrinkage of per-set credits) so per-set SE is well below the true harm, state the correct three-item argmin null (33%, not 50%), and give the pairwise-pruner >= 80% clause its own falsifier."
  },
  {
   "id": "P5",
   "depends_on": "Composition B conflict cells, which the budget runs at 2 seeds (548, +/-8), compared with the composition A masking ratio from P1's 4-seed cells.",
   "falsifier": "The B-minus-A masking-ratio difference is <= 0.1 in either direction.",
   "label": "unresolvable",
   "reason": "Each masking ratio is a ratio of 548- or 1,096-episode differences on a 15-net base, giving per-ratio CIs of order 0.5-1.0, so a 0.3 difference between two such ratios - and a 0.1 falsification band - lies entirely inside the stated noise.",
   "fix": "Run composition B conflict at the same 4-seed budget and restate the position effect as a difference of harms in net points (harm_B - harm_A >= 10 net) with a bootstrap CI, not as a difference of ratios."
  },
  {
   "id": "P6",
   "depends_on": "Shapley-completion cells v(EW), v(EE'), v(E), v(W), v(E') at 2 seeds plus k=0 from logs, correlated across conflict and redundancy sets against the two-player phi computed from v(FULL), v(-i), v(-j), v(-ij).",
   "falsifier": "Spearman between two-player phi and exact Shapley is <= 0.5 (the third item's interactions matter).",
   "label": "entailed",
   "reason": "The pairwise phi's two terms, v(FULL) - v(-i) and v(-j) - v(-ij), are literally two of the exact three-player Shapley's four terms and carry half of its weight, measured on the very same episodes, so shared measurement noise forces a high across-set Spearman and puts <= 0.5 out of reach.",
   "fix": "Estimate the exact Shapley from disjoint seeds (independent re-runs) so the shared-term correlation is broken, and additionally correlate only the residual the pairwise estimator omits (the v(i) - v(empty) and v(ij) - v(j) terms)."
  }
 ],
 "shared_terms": [
  "P1-P5: composition A's masking ratio in P5 is exactly P1's estimand computed on the same cells, so P1 determines half of P5's contrast.",
  "P1-P4: P4's per-set decision is built from the same v(EWF) - v(EF) and v(EWF) - v(WF) contrasts as P1, only seed-averaged per set instead of pooled.",
  "P2-P6: the redundancy phi entering P6's Spearman is assembled from v(EE'F), v(E'F), v(EF) and v(F) - the same four cells as P2's two help terms.",
  "P6-P1/P2: the two-player phi shares two measured terms (weight 1/2) with the exact Shapley it is correlated against, and those terms are P1's and P2's numerators.",
  "P1-P2-P3: all three rest on the single shared v(F) arm as the common subtracted baseline, so an error in that one cell moves all three estimands together."
 ],
 "headline": "P1",
 "headline_status": "unresolvable",
 "n_open": 0,
 "n_entailed": 2,
 "n_near": 1,
 "n_unresolvable": 3,
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
