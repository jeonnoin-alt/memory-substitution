=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: compile_the_statistics_not_the_trajectory — headline P1 is **unresolvable**; open 6 / entailed 0 / near-entailed 1 / unresolvable 1; verdict revise

- P1 [unresolvable] falsifier: paired net gain below +12, i.e. indistinguishable from zero at this n
  reason: The decision margin (12) is exactly the stated noise floor (+-12) and the proposal anchors the true expected effect to the Gate-0 gain on those types (~+12..+15), so the predicted effect sits at the detection limit and a real effect of the anticipated size will read as falsified about half the time.
  fix: Shrink the floor below the margin on the search-bound cell (more seeds or all 274 games per type group, or a pre-registered TOST with margin > CI half-width) so that +12 and 0 are separable.
- P2 [near_entailed] falsifier: cheatsheet_6 within +-12 of cheatsheet_1465, or means not ordered 6 < 20 < 80 < 1465
  reason: The rule compiler emits one take-receptacle row per trajectory, so cheatsheet_6 covers at most 6 of ~30 object classes while cheatsheet_1465 covers all of them; if P1's effect exists at all the gap is forced by row coverage rather than by aggregation, and the falsifier is reachable only through the scaffold-driven mechanism P3's placebo is built to exclude.
  fix: Add a coverage-matched rung (all ~30 object classes, each estimated from a single sampled trajectory) so sample depth is varied at fixed coverage, and give the monotone ordering its own power statement, since 20 vs 80 vs 1465 differences are far inside the +-12 floor.
- P3 [open] falsifier: shuffled within +-12 of the true table
  reason: The falsifier is reachable if the reader treats the table as a search-anything scaffold and ignores its content, and nothing in the design forces the two arms apart.
  fix: Also report shuffled minus k=0, since the contrast as written cannot separate 'the true table helps' from 'the permuted table actively hurts'.
- P4 [open] falsifier: the no-bank table within +-12 of the compiled one
  reason: ALFWorld object-receptacle placements are stereotyped enough that the model's own prior table could match the compiled one, so the falsifying outcome is plainly reachable and would in fact be the likely result.
  fix: None needed for openness; pre-register the row-level agreement between the prior and compiled tables as a covariate so a null is interpretable rather than merely negative.
- P5 [open] falsifier: residual in favour of retrieval >= +8
  reason: Gate-0 puts k=3 about +27 over k=0 overall, so a residual well above the +-8 floor is entirely reachable if the static combo recovers less than that.
  fix: Close the dead band between the stated prediction (<= 0) and the stated falsifier (>= +8), which currently leaves residuals of +1..+7 neither confirming nor falsifying.
- P6 [open] falsifier: whole-bank_80 within +-12 of or above cheatsheet_80, or the added table worth < 12 on top of the same 80 items
  reason: The information is by construction present in the 80 raw items and the whole-bank arm also carries procedure content the cheatsheet lacks, so a long-context reader matching or beating the table is a reachable outcome.
  fix: None for openness; note that cheatsheet_80 is simultaneously an n-ladder rung, so a single bad draw of it moves P2 and P6 together.
- P7 [open] falsifier: the 95% CI of the paired difference includes 0
  reason: A null reduction is reachable if the reader does not act on the table, though the estimand is conditioned on a post-treatment event (the target being taken), which only episodes that get that far contribute to.
  fix: Restrict the paired comparison to games where the target is taken in both arms (or impute the max search length for failures), and reconcile the stated threshold (>= 1.0) with the stated falsifier (CI includes 0), which currently leaves reductions of 0.1..0.9 undecided.
- P8 [open] falsifier: k=3 minus k=0 below +19 on the fresh seeds
  reason: It is a re-measurement of an already observed +27 with a 30% discount and an +-8 floor, so failure is unlikely but empirically reachable rather than excluded by construction.
  fix: None; state explicitly whether a result between +8 and +19 stops the study or only flags it, since the stopping rule and the floor disagree in that band.
- shared terms: P1-P3-P4: all three are cheatsheet_1465 minus X on the identical search-bound cell, so they share one measured minuend and are one measurement with three subtrahends, not three independent tests.; P1-P2: cheatsheet_1465 is a measured term in both; if it fails against k=0, P2 can only survive by cheatsheet_6 falling below k=0.; P2-P6: cheatsheet_80 is both a rung of the n ladder and the explicit-aggregation arm of P6, so the ordering claim and the reader-is-not-an-aggregator claim rest on the same cell.; P1-P5: the combo arm of P5 contains cheatsheet_1465, so P5's residual inherits whatever P1 measures.; P1-P7: on search-bound types taking the target object is close to necessary for success, so the process measure of P7 and the success measure of P1 are scored on the same episodes and largely the same event.; P5-P8: k=3 on the fresh cells is the same measured arm in the gate and in the gap-closing test.
