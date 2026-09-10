# Entailment check report

| idea | headline | status | open | entailed | near | unresolvable | verdict |
|---|---|---|---|---|---|---|---|
| complementarity_not_proximity | P2 | open | 4 | 0 | 1 | 0 | pass |
| compression_erases_the_writer | P3 | open | 5 | 0 | 0 | 1 | pass |
| coverage_not_headcount | P2 | open | 5 | 0 | 0 | 1 | pass |
| leave_one_type_out_split | P1 | open | 8 | 0 | 1 | 1 | pass |
| one_bad_apple_population_vote | P2 | open | 8 | 0 | 0 | 0 | pass |
| own_errors_pass_the_gate | P2 | open | 4 | 0 | 1 | 1 | pass |
| reader_pays_writer_detours | P1 | open | 3 | 0 | 1 | 1 | pass |
| reconstruction_pays_only_across_the_writer_gap | P1 | open | 8 | 0 | 0 | 0 | pass |
| rewriter_trained_against_one_reader_matched_cost | P1 | open | 5 | 0 | 1 | 2 | pass |
| shared_blind_spot | P1 | open | 4 | 0 | 1 | 1 | pass |
| thoughts_do_not_travel | P1 | open | 5 | 0 | 1 | 0 | pass |

## Flagged predictions

- **compression_erases_the_writer P6** [unresolvable]: The margin (+6) is only 1.4 times the four-cell half-width (+-4.2), violating the proposal's own 'twice the half-width' rule, so the predicted +6 gives about [1.8,10.2] and the null gives [-4.2,+4.2] - overlapping intervals that cannot separate the prediction from its falsifier.
- **leave_one_type_out_split P3** [unresolvable]: The hypothesis's own predicted +9 lies only about half an MDE above the +6 boundary, so a true +9 reads as falsified a sizeable fraction of runs and the proposal's stated 'each value at least one MDE from the boundary' rule fails for this clause.
- **leave_one_type_out_split P8** [near_entailed]: cell12 - cell3 = (cell12 - cell2) + (cell2 - cell1) - (cell3 - cell1), so P7 at +6 and P5 at -4 already deliver +12 once the five-procedure prompt reaches its predicted +2 gain; the only route to the falsifier is a static-5 gain below +2, a quantity the proposal predicts but neither controls nor mak
- **own_errors_pass_the_gate P3** [unresolvable]: Clause (a) is decidable, but the mediation clause (b) - the one that separates familiarity from paraphrasing as such - sets a +5 margin against a +-4 half-width and falsifies only when the estimate falls below about +1, so a true zero difference escapes falsification roughly a third of the time and 
- **own_errors_pass_the_gate P6** [near_entailed]: On a clean store the gate can only swap a flagged item for the next-ranked clean item of the same type, so at the sub-10% (or even 15%) flag rate about 0.3 of 3 retrieved items change per episode and a >= 6 net cost is reachable only through a steep retrieval-rank-to-value falloff the design never m
- **coverage_not_headcount P4** [unresolvable]: Falsification requires the CI on (num - 0.6*den) to clear 0, which at the stated ~+/-6 subset noise needs an expert-minus-self gain gap of roughly 35 net; the proposal states expert gains of +39..+55 but never states or gates gain_SELF on these types, and for any plausible denominator of 10-20 net t
- **reader_pays_writer_detours P4** [near_entailed]: The per-token half is largely fixed by how the pools were rendered - self-raw items are longer, so served tokens are larger by construction and, at matched success, the ratio exceeds 1 without any reader behaviour being involved - so the only live falsifying route is the auxiliary success-gap clause
- **reader_pays_writer_detours P5** [unresolvable]: Clause (a) is resolvable (a true slope of 0 gives an upper bound of about 0.24), but the distinctive no-self-recognition claim in (b) is affirmed by noise - with SE 0.17 the 95% half-width is 0.33, so a real self-recognition gap of 0.2 yields a CI including 0 and counts as confirmation, and only an 
- **rewriter_trained_against_one_reader_matched_cost P2a** [unresolvable]: The margin (6) exceeds the stated half-width (5.7) by 0.3 net, so under the decision rule falsification requires a point estimate below 0.3: a genuinely falsifying world of full retention lands there only about half the time, and the substantively falsifying middle (the rewriter retaining 60-70% on 
- **rewriter_trained_against_one_reader_matched_cost P2b** [unresolvable]: Same knife edge as P2a (margin 6 against a 5.7 half-width forces the falsifying point estimate to lie below 0.3), and here the reduced headroom of A'' pushes the estimate toward the falsifier through a compression-of-headroom route the ceiling guard bounds only loosely, so most outcomes are reported
- **rewriter_trained_against_one_reader_matched_cost P4** [near_entailed]: Delta is algebraically [S(B,C_selfcost) - S(B,C_vtok)] - I(R_A,B), and the proposal's own Measurement-C numbers put the first bracket near +8, so falsification requires I(R_A,B) >= ~13 net on the held-out backbone, above the >= 10 that Gate 0 demands of the training reader itself, a transfer surplus
- **shared_blind_spot P3** [near_entailed]: A diagonal deficit is exactly what a judge's ordinary leniency toward its own backbone's text produces at an operating point calibrated only on clean expert items, and the covariate removes a judge's overall recall (a main effect) rather than that self-text leniency, so the falsifier is reachable on
- **shared_blind_spot P4** [unresolvable]: With a paired 95% half-width of ~0.063, an upper bound below 0.05 requires a point estimate below -0.013, and the falsifier demands this for both judges at once, so a world where the deficit truly vanishes at L1 is classified as falsifying only about one time in eight; the monotonicity clause adds n
- **thoughts_do_not_travel P6** [near_entailed]: The two F6 cells are selected on the outcome-correlated criterion of largest verbatim deficit, i.e. the pairings where the writer's material transfers worst, and the arm most likely to show thoughts carrying procedure (own thoughts read by their own backbone) is absent, so the placebo's falsifier su
- **complementarity_not_proximity P5** [near_entailed]: static3 already supplies the type-correct exemplar and the ReAct format, so the only channel left to a deliberately wrong-type pool is raw context length, a mechanism the design neither names as plausible nor equips with an arm, and the same measurement family already put the placebo at -3; the fals
