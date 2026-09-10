=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: protocol_bindings_procedure_count — headline P3 is **open**; open 5 / entailed 0 / near-entailed 0 / unresolvable 2; verdict pass

- P1 [unresolvable] falsifier: The drop is < 8 net (the reader discovers the precondition by trial within the budget), and still < 8 under the stricter wrapper.
  reason: The threshold sits exactly at the stated +-8 minimum reportable margin, so a null drop's CI still covers 8; the falsifier is genuinely reachable because the prerequisite menu (examine, open-then-close, look, inventory, visit) consists of actions ALFWorld readers take incidentally, which puts the outcome right in the unresolvable band.
  fix: State the manipulation check at +14 net like the confirmatory cells, or add seeds/games so a null reading's CI excludes the threshold.
- P2 [open] falsifier: Retrieval minus all-P compiled >= +8 net at R=4 (the reader already fails to route among 24 procedures).
  reason: Routing among 24 code-keyed procedures can plausibly fail by a reportable margin so the falsifier is reachable; note that the R=1 half of the claim carries no stated falsifier and is untested prose.
- P3 [open] falsifier: Retrieval minus all-P < +8 net at R=48 (the reader routes among 288 cached procedures as well as the retriever).
  reason: A 32B reader can plausibly find its randomly-coded row inside a 10k-token prompt, so the falsifier is reachable and a near-null reading's +-8 CI excludes the predicted +14; the 'non-decreasing in R' clause, however, has no stated falsifier and cannot be resolved when each R's residual carries a +-8 CI.
- P4 [open] falsifier: Placebo <= all-P - 8 net (the degradation is context length, not routing).
  reason: Long-context degradation is reachable and reportable; in fact the placebo presents the reader with the same 288 code-keyed rows as the R=48 all-P prompt, so if P3 is confirmed because routing among 288 rows fails, P4 is falsified by the same mechanism and the two cannot both pass.
- P5 [open] falsifier: Factorized < retrieval - 8 net at R=48 (the reader cannot index 48 rows either).
  reason: A 48-row lookup can fail by a reportable margin, so the falsifier is reachable, though the test is auto-confirmed whenever the R=48 retrieval arm is not itself elevated.
- P6 [open] falsifier: Retrieval minus oracle-routed static >= +8 net at any R (retrieved trajectories carry value beyond the (type, protocol) procedure).
  reason: Full retrieved trajectories can carry concrete action strings the procedure text lacks, so the falsifier is reachable; if anything it is too easy, since 'at any R' tests four cells at the +-8 floor with no multiplicity control.
- P7 [unresolvable] falsifier: The 8B ladder shows no residual through R=48, or its threshold equals the 32B threshold.
  reason: The threshold is a step function of per-cell residuals each carrying a +-8 CI on a three- or four-point grid, with no CI stated for the threshold itself, so a one-step difference lies inside the stated noise; the 8B grid also omits R=1, so a smaller-than-32B threshold cannot be observed if the 32B threshold is already R=4.
  fix: Predict the reader-to-reader residual difference at a fixed R (e.g. R=16) with a cluster-bootstrap CI, or bootstrap the threshold itself over games, and run the 8B ladder on the same R grid.
- shared terms: P2-P4: both rest on the R=4 all-P compiled arm's success, so that one arm's level moves P2's residual and P4's placebo comparison together.; P3-P5, P3-P6: retrieval at R=48 is a measured term in all three; a null R=48 retrieval arm falsifies P3 and confirms P5 and P6 automatically.; P3-P4 (logical, not merely shared): the R=4 placebo and the R=48 all-P prompt are both 288 code-keyed rows with one match, so P3's confirming outcome entails P4's falsifier unless degradation depends on which codes are in force.; P7-P3: the 8B threshold is defined by the same >= +14 residual criterion against the same all-P arms that P3 tests.
