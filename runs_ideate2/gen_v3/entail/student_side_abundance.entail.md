=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: student_side_abundance — headline P4 is **near_entailed**; open 1 / entailed 0 / near-entailed 3 / unresolvable 2; verdict revise

- P1 [open] falsifier: k=7 memory-free accuracy at or above k=1 memory-free accuracy.
  reason: The sign flip is a directional outcome the design can genuinely produce, the length confound is separately controlled by the DEC arms, and 0.4 x 12 = ~5 net sits just above the stated ~4-net pooled MDE, though the four-dose monotonicity clause is only a 2-seed trend by the proposal's own admission.
- P2 [unresolvable] falsifier: DEC-7 dropping as much as k=7, i.e. a long-prefix effect rather than information abundance.
  reason: DEC-7 sits in the exploratory ladder that the proposal itself says resolves only trends (+/-8 net at 274 x 2 per split), so a ~3-net equivalence margin and the distinction between a 0-net and a ~5-net drop both fall inside its CI.
  fix: Promote DEC-7 (and DEC-3) into the confirmatory set at 3 seeds pooled over all three evaluation sets, so the half-width is below the 0.25 x Gate-0-gain margin.
- P3 [near_entailed] falsifier: reliance and/or mismatched-memory harm flat or decreasing in k_train.
  reason: Both indices contain the memory-free (absent) accuracy with a negative sign, so P1's predicted decline in that same measured term mechanically raises both unless the matched and mismatched accuracies fall in lockstep with it, a case the proposal neither predicts nor controls.
  fix: Pre-register the matched-block and mismatched-block accuracies as separate estimands (or use a ratio-form reliance index) so P3 can fail while P1 holds.
- P4 [near_entailed] falsifier: a decline in memory-free accuracy across the teacher-side ladder.
  reason: No teacher-side arm puts a block in the student's prompt, so the train/test prompt mismatch that drives the student-side decline is removed by construction and a decline could only arise from a teacher-student distribution gap the proposal never names or measures; the 'within CI' acceptance rule additionally lets any 2-seed null confirm non-decrease, so the crossing of the two curves is largely built in.
  fix: Add a teacher-side arm whose student prompt also carries a token-matched block (or a length-matched empty-content prefix) to separate prompt mismatch from information, and pre-register a decline magnitude above the ladder CI as the falsifier instead of 'within CI'.
- P5 [near_entailed] falsifier: Spearman below 0.6, non-zero decoy delta-NLL, or an undiminished self-rollout effect.
  reason: Both variables rise with the dose k by construction (more context lowers action-token NLL; P1 predicts the deficit grows with k), so pooling 18 type-dose points makes a positive rank correlation follow from the shared dose factor rather than from any type-level correspondence, and decoy delta-NLL ~ 0 restates how the decoy pool was built (other-type items chosen to be irrelevant).
  fix: Compute the correlation within each dose across the six types (or partial out the dose main effect) and pre-register that within-dose statistic, with per-type counts above the stated 150-game rule.
- P6 [unresolvable] falsifier: RATE-3 landing outside the k=0 to k=3 interval on either measure.
  reason: RATE-3 is a 50/50 mixture of the two endpoint training distributions so an interior value is expected by construction, and the whole k=0-to-k=3 interval is only a few net points, well inside the +/-8-net 2-seed ladder CI.
  fix: Run RATE-3 and both endpoints at 3 seeds pooled over the three sets and pre-register a non-inferiority margin smaller than the measured k=0 minus k=3 gap.
- shared terms: P1-P3: memory-free (absent) accuracy is P1's estimand and a negative term in both of P3's indices, so P1's decline determines P3 unless matched accuracy moves with it.; P1-P5: P5's per-type deficit is the per-type decomposition of P1's pooled ladder difference, and both are indexed by the same dose k, which also drives delta-NLL.; P1-P6: RATE-3 is scored against the same k=0 and k=3 memory-free cells that anchor the P1 ladder.; P1-P2: P1's required deficit and P2's equivalence margin are both fractions of the same Gate-0 k_train=0 gain, so a barely-passing gate shrinks them together.
