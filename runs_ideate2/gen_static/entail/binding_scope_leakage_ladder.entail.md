=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: binding_scope_leakage_ladder — headline P6 is **unresolvable**; open 5 / entailed 0 / near-entailed 0 / unresolvable 3; verdict revise

- P1 [open] falsifier: Residual < +8 net in that cell, in which case the ladder is not run and the failure is reported.
  reason: Reader application failure is a reachable outcome and a near-null reading's +-8 CI excludes the predicted +14, so the gate is decidable.
- P2 [open] falsifier: Sentence < retrieval - 8 net (the reader applies a concrete trajectory but not a stated rule).
  reason: The exemplar-over-rule application gap is a reachable, named mechanism and the falsifier needs a reportable 8-point gap, but without a global-scope positive control the prediction is confirmed vacuously whenever global-scope retrieval shows no gain at all.
  fix: Add a global-scope positive control (retrieval at s=1 minus type-agnostic static >= +14) as a precondition for reading P2.
- P3 [open] falsifier: 20-item < full - 8 net (a many-shot per-class requirement).
  reason: A thin 20-item bank can plausibly return wrong-class items and lose by a reportable margin, so the falsifier is reachable; only the one-sided direction is falsifying, which the proposal states.
- P4 [open] falsifier: Table < retrieval - 8 net in the scene-scope table cell.
  reason: A 274-row lookup can fail by a reportable margin and, unlike P2, the P1 gate guarantees a non-null retrieval level so the non-inferiority test is not vacuous.
- P5 [open] falsifier: Residual < +8 net (the reader does not exploit even an exact self-duplicate).
  reason: The falsifier is not merely reachable but close to forced by construction: duplicates exist only for games the type-agnostic prompt already solved, so the attainable residual is capped by first-pass/eval-seed disagreement rather than by whether the reader exploits the duplicate.
  fix: Source instance-scope duplicates independently of the baseline's outcome (regenerated expert trajectories of the same instance, or a first pass under a different arm) so failed games can also carry a duplicate.
- P6 [unresolvable] falsifier: residual(0.5) >= residual(1) - 8 (superlinear) or residual(0.5) <= +8 while residual(1) >= +14 (sublinear).
  reason: At the smallest residual(1) that P5 admits (+14 to +16) an exactly linear residual(0.5) of 7-8 trips both falsifiers at once, so the predicted outcome is auto-falsified, and the +-8 tolerance is as large as the half-residual under test; the s=0 intercept clause is additionally entailed by the split, since an instance-scope bank with no duplicate holds nothing keyed to the eval instance, as the proposal concedes.
  fix: Require residual(1) >= +32 before reading linearity (so half the residual clears the floor), or fit slope and intercept over s in {0, 0.25, 0.5, 0.75, 1} with a bootstrap CI on the intercept.
- P7 [unresolvable] falsifier: Whole-bank >= retrieval - 8 net (the reader finds its own trial among 80 items without a query).
  reason: Falsification requires establishing a difference smaller than the stated +-8 floor, which the cluster-bootstrap CI cannot separate from the predicted -8.
  fix: State it as whole-bank <= retrieval - 14, or power the comparison so an 8-point difference is excludable.
- P8 [unresolvable] falsifier: Goal-query residual within +-8 of the scene-query residual.
  reason: The falsifier is a sub-floor difference the stated CI cannot resolve, and it is close to forced anyway because the self-duplicate carries the eval game's goal string verbatim, so goal similarity retrieves the same item and the confirming direction is excluded by construction.
  fix: Predict goal-query <= scene-query - 14 and make the indexed duplicate's goal text differ from the eval query (index on the trajectory or a paraphrase) so goal similarity is not an exact match.
- shared terms: P5-P6-P7-P8: instance-scope retrieval at s=1 is a measured term in all four; its level sets P6's falsifier bands, P7's threshold and P8's comparison, so one arm decides four predictions.; P5-P6: P6's superlinear and sublinear bands are algebraic functions of residual(1) measured in P5, so P5's outcome determines whether P6 can pass at all.; P1-P4: the scene-scope retrieval (s=1) success is a shared term in the gate and in the table non-inferiority test.; P2-P3: global-scope retrieval at s=1 over the full relocated bank is a measured term in both.; P2-P4 (form): both are non-inferiority tests of a compiled static against retrieval and are auto-confirmed whenever the matching retrieval residual is null; P4 is protected by the P1 gate, P2 has no equivalent gate.
