# Entailment check report

| idea | headline | status | open | entailed | near | unresolvable | verdict |
|---|---|---|---|---|---|---|---|
| binding_scope_leakage_ladder | P6 | near_entailed | 8 | 0 | 1 | 0 | revise |
| many_shot_averages_detours | P2 | unresolvable | 7 | 0 | 0 | 1 | revise |
| near_duplicate_needle_crossover | P3 | open | 2 | 1 | 3 | 1 | revise |
| retrieval_timing_is_budgeting | P6 | near_entailed | 5 | 0 | 1 | 0 | revise |
| aggregate_or_comply | P2 | open | 6 | 0 | 2 | 1 | pass |
| bindings_need_a_query_only_when_untestable | P3 | open | 6 | 0 | 0 | 0 | pass |
| compile_the_statistics_not_the_trajectory | P1 | open | 5 | 0 | 2 | 1 | pass |
| recall_success_dissociation | P4 | open | 10 | 0 | 1 | 0 | pass |
| whole_bank_confusability_ladder | P4 | open | 7 | 0 | 0 | 0 | pass |

## Flagged predictions

- **aggregate_or_comply P4** [unresolvable]: The margin (12) equals the stated per-cell floor and the estimand is a difference of two such cells, so its propagated floor exceeds the margin and the confirming and falsifying outcomes cannot be told apart at the stated power.
- **aggregate_or_comply P6b** [near_entailed]: The two arms already differ on clean banks by the program's own retrieval-minus-static residual (about +17 net in Measurement C, and this proposal's Short Hypothesis concedes retrieval wins on accuracy), so a >=12 raw-level gap is delivered by that uncontrolled baseline route difference rather than 
- **aggregate_or_comply P7** [near_entailed]: Pick items are never poisoned and R1 selects by goal query while R5/R6 are type-conditioned, so spillover is structurally impossible in roughly half the 37 cells; averaging those forced zeros into one pooled slope halves any real spillover carried by the type-agnostic R2/R3/R4 arms and pushes it und
- **many_shot_averages_detours P2** [unresolvable]: The +9 margin is a four-cell difference-in-differences whose propagated paired floor is roughly 11-16 net, and larger again under the block-level bootstrap over 8 banks the design itself requires for WB cells, so a +9 interaction cannot be separated from equal losses at the stated noise; only the co
- **binding_scope_leakage_ladder P6** [near_entailed]: The discount branch is unreachable as stated because a duplicate-present game sees its own duplicate at rank 1 in both s=1 and s=0.5 and the split never shows the model the bank's duplicate rate, so the only channel that can move D(0.5) is the changed content of retrieved ranks 2-3, a mechanism the 
- **near_duplicate_needle_crossover P1** [near_entailed]: The needle is a completed purchase of the exact target product id delivered into a 2-item context, so a null requires the reader to ignore a demonstration that contains the answer - a compliance failure the design logs (needle-use rate) but never manipulates.
- **near_duplicate_needle_crossover P4** [near_entailed]: The retrieval half of the falsifier is excluded by construction - with an instruction-line-only index and identical templated lines the hit rate is designed to be about 0.05, capping any retained gain at roughly 0.05 x 15 = 0.8 points, far inside the +/-4.5 floor - so only the whole-bank half can co
- **near_duplicate_needle_crossover P5** [near_entailed]: By construction the r=0 bank contains only the material static3 already supplies (type-matched, binding-mismatched expert exemplars), so a +12 residual would have to come from per-game selection among items guaranteed to share no binding - a mechanism the design neither names nor isolates - and the 
- **near_duplicate_needle_crossover P6** [entailed]: Fillers are constructed to share zero attribute phrases with any cluster instruction while needles share the product id or at least two attribute phrases, so BM25 plus embedding cannot lose the needle as filler count grows; the stated hit-rate precondition is itself a construction fact, not a measur
- **near_duplicate_needle_crossover P7** [unresolvable]: At a 15-point gain and a +/-4.5 floor the r=0.5 gain of about 7.5 carries a ratio interval of roughly 0.2-0.8, so no plausible true value is distinguishable from 0.5, and the item is declared non-confirmatory with no decision rule attached.
- **compile_the_statistics_not_the_trajectory P3** [near_entailed]: cheatsheet - shuffled = (cheatsheet - k0) + (k0 - shuffled), so once P1 confirms at M1 the only way P3 fails is a deranged table beating no table at all, and a table that actively sends the agent to wrong receptacles is unlikely to clear k0 - a scaffold effect the proposal names but does not size in
- **compile_the_statistics_not_the_trajectory P7** [near_entailed]: The scoring rule puts failed episodes at their ceiling, so P1's predicted ~10-point success gain mechanically produces roughly the whole 0.5-0.6 reduction, and a null would require a large success gain to arrive with no change in search breadth whatsoever.
- **compile_the_statistics_not_the_trajectory P8** [unresolvable]: The acceptance band is set equal to the stated 268-cell floor, so a same-arm replication passes for any true drift up to 12 points, and every branch of the k3 - k0 outcome (at least +7, 0 to +7, CI covering 0) ends in 'proceed', so no result can count against the design.
- **retrieval_timing_is_budgeting P6** [near_entailed]: Substituting the estimand makes the upper falsifier equivalent to S(stall) > P(static3 succeeds OR always-distractor succeeds) - D0 + 8, i.e. the stall arm must beat the per-episode union oracle of static3 and always-distractor by 8 - D0 points, and because the shared always-distractor cell inflates
- **recall_success_dissociation P3b** [near_entailed]: Both sides are built from the same S cells and the same treatment (a same-product trajectory in the top-3), so the natural arm's gain is by construction the coverage-weighted average of the per-cell duplicate effect and equality with b_ws times E is an accounting identity up to effect heterogeneity 
