=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: aggregate_or_comply — headline P2 is **open**; open 2 / entailed 0 / near-entailed 3 / unresolvable 2; verdict revise

- P1 [open] falsifier: loss < 12 (the agent does not follow the wrong procedure); study stops and the poison is reported inert
  reason: Retrieved exemplars are advisory rather than mandatory, so the agent declining to imitate three replay-validated wrong procedures is a reachable outcome, and the 20-point margin sits above the +-12 floor.
  fix: State what happens when the loss exceeds 12 but the arm stays above k=0, since the conjunction 'loses >= 20 and lands at or below k=0' has no falsifier attached to its second clause.
- P2 [open] falsifier: loss < 12 (the reader outvotes one wrong item in three)
  reason: The falsifier is a genuine alternative hypothesis the design can produce, since majority-style resistance at k=3 would show up directly as a sub-floor loss.
  fix: None; note the effect is diluted by the ~58% exposure rate, so record realised per-episode exposure and report the loss conditional on at least one poisoned item retrieved.
- P3 [near_entailed] falsifier: R2_p.25 loses >= 12 across draws with the audit showing hedged or poisoned procedures; or R2_p.75 within +-12 of p=0 with the audit showing the compiler restored the clean procedure from its own knowledge
  reason: Both falsifiers are gated on a corroborating audit finding and the second is pre-labelled a compiler-prior confound to be reported as such, so a flat R2_p.75 is absorbed as a confound rather than counted against the hypothesis, and a p=.25 drop with a clean-looking audit triggers no falsification at all; the flat half is additionally confirmed by any undetected loss up to the +-12 floor.
  fix: Define both falsifiers on the success numbers alone with the audit reported separately as a descriptive covariate, and fund the R2 p=0 cell, which the 4 new p levels x 8 routes = 32 arm count does not contain.
- P4 [near_entailed] falsifier: R4_p.25 within +-12 of R4_p0 while R1_p.25 lost >= 12
  reason: The falsifier is written as a conjunction with P2's success, so if R1_p.25 does not lose >= 12 the prediction cannot be falsified by any R4 outcome; and the R4 p=0 comparison cell is not in the 32-arm count, which lists only 4 new p levels.
  fix: State the falsifier on R4 alone (R4_p.25 within +-12 of R4_p0) and add R4_p0 (and the other static p=0 cells) to the arm list and budget.
- P5 [near_entailed] falsifier: the wrong instruction damages less than the wrong exemplars by >= 12
  reason: At p=1 both arms deliver the same wrong procedure and P1's own gate requires R1_p1 to land at or below k=0, so both cells are compressed against the procedure-type floor and the near-zero difference that confirms the prediction is largely forced; the falsifier needs the agent to ignore an explicit instruction while obeying exemplars, a dissociation the design never isolates.
  fix: Run the contrast at p=.5 or p=.75 where neither arm is floored, report absolute success levels against the k=0 floor, and add a wrong-instruction-without-exemplars cell so instruction compliance is measured rather than inferred.
- P6 [unresolvable] falsifier: R5's draw mean differs from R1 by >= 12, or the between-draw spread at p=.5 is < 12
  reason: The spread claim is estimated from exactly two draws whose own cell noise is +-12, so an observed range of 12 points carries no information about draw-to-draw variance, and the first half is an equivalence claim whose margin equals the floor, i.e. confirmed by any failure to detect.
  fix: Run at least five R5 draws and report the spread with its own bootstrap CI, and set the equivalence margin above the cell's CI half-width (or enlarge the cell) so 'within +-12' is not satisfied by noise.
- P7 [unresolvable] falsifier: pick-type success moves by >= 12 at any p for any route
  reason: As written the control is a conjunction over roughly 32 route x p comparisons each carrying +-12 noise, so chance excursions are expected to trigger the falsifier regardless of true spillover, and the outcome cannot distinguish contamination leakage from multiplicity.
  fix: Replace the all-cells conjunction with one pre-registered pooled test (paired regression of pick-type success on p with route as a factor) and a multiplicity-controlled threshold.
- shared terms: P1-P2: both are R1 losses measured against the same R1_p0 cell, so a low or high R1_p0 moves both losses together.; P2-P4: P4's falsifier is written conditional on R1_p.25 having lost >= 12, so P2's outcome determines whether P4 can be falsified at all.; P1-P5: P5's contrast contains R1_p1, the same cell P1 requires to land at or below k=0, so P1's gate floors one term of P5's difference.; P2-P6: R1_p.25 is a measured term in both the compliance test and the static-versus-retrieved comparison.; P3-P4-P7: all rest on p=0 cells for R2, R4 and the pick types that the stated count (4 new p levels x 8 routes = 32 arms) does not include, so the same unfunded baseline determines three predictions.
