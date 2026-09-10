=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: whole_bank_confusability_ladder — headline P4 is **open**; open 7 / entailed 0 / near-entailed 0 / unresolvable 0; verdict pass

- P1 [open] falsifier: Either difference at or below -9 (plain long-context degradation); under the stated global rule a difference at or above +9 also breaks flatness.
  reason: An 80-item near-16k cached prefix can degrade, and the opposite breach is at least as live because Measurement C's k-sweep shows k7 at +19.5 over a 3-item static prompt, so adding 74 same-type items could push WB(R-80) above the +9 edge of the flatness band.
  fix: state explicitly that a gain at or above +9 also falsifies P1, since the stated falsifier names only the decline while the global threshold rule falsifies flatness in both directions.
- P2 [open] falsifier: WB(N-80) - WB(R-80) above -9, or a decline unaccompanied by a >=10-point rise in the twin-procedure error fraction from N-12 to N-80.
  reason: blind1 costs only 3 net against k0, so a 32B reader that disambiguates on the goal sentence leaves WB(N-80) flat and either limb of the conjunction can fail; the monotonicity clause is stated but not scored as a falsifier and its N-12 to N-24 step lies inside the +/-9 noise, and N vs R also differ in item identity rather than twin share alone.
  fix: score the monotonic decline with a pre-registered trend test or drop the clause, and define the twin-procedure signature by a bank-independent rule so the rise cannot follow mechanically from there being more twins in the larger bank to match against.
- P3a [open] falsifier: Cross-type-in-top-3 below 0.4 on N-48; or the rate reached yet RET(N-48) - RET(R-48) above -9; or RET-T(N-48) at or below -9 against RET(R-48).
  reason: The exposure limb is near-forced by construction because goal-sentence BM25 ties a twin with its original whenever the goal's combo is covered, but the adoption limb and the RET-T limb are genuinely reachable (a wrong-type item beside a right-type one may be disambiguated, as blind1 nearly is against k0), so the conjunction can still come out against the hypothesis.
  fix: report the cross-type-in-top-3 rate as a measured precondition rather than as a falsifiable limb, so the prediction rests only on the reader-adoption and RET-T contrasts.
- P3b [open] falsifier: RET(N-80) - RET(N-12) at or below -9.
  reason: The falsifier is reachable and arguably likely, because coverage grows from 6 twin pairs at N-12 to 40 at N-80 so per-episode twin exposure is coverage-bound rather than share-bound, and the proposal's own logging of the per-size exposure rate will show whether the fixed-share premise survives.
  fix: none required
- P4 [open] falsifier: The replicate interaction is above -9, or the two draws disagree in sign.
  reason: Both routes can lose the same amount to twins (P3a itself predicts retrieval is hurt) or whole-bank reading can absorb twins as well as retrieval does, so the falsifier is reachable; the caveat is that this double difference carries roughly 1.4 to 2 times the noise of the single contrasts the 9-net threshold was calibrated on, so the confirming condition is underpowered even though the falsifier region reaches well outside the noise.
  fix: state the interaction's own MDE and either raise its threshold above the single-contrast 9 net or add seeds, so a -9 interaction can separate from -5 at the stated 90% CI.
- P5 [open] falsifier: D_8B - D_32B above -9.
  reason: A weaker reader compressed toward the ALFWorld floor can show smaller, not larger, route gaps and can be hurt equally on both routes, so the falsifier is reachable; the quadruple contrast again carries about twice the single-contrast SE while being judged at the same 9-net threshold, so only a true effect near -12 or beyond would confirm.
  fix: state the MDE for the reader triple difference and add a floor-compression check on the weaker reader's absolute success rates, rather than importing the single-contrast 9-net threshold.
- P6 [open] falsifier: WB(U-80) - k3 at or below -9, or at or above +9.
  reason: Both breaches are reachable on paired cells with about a 5-point CI half-width, but the comparison arm retrieves from a different bank (the whole pool, not U-80), so any breach confounds route with bank size and the measured near-miss share of U-80 is the only thing tying it to the ladder's count axis.
  fix: add RET k=3 over U-80 itself so the whole-bank arm is compared against retrieval over exactly the same 80 items.
- shared terms: P1 internal: WB(S6) is the common reference for both the R-80 and F-80 clauses, so its noise moves the two together and one cell decides both.; P2-P5: WB N-80 and WB N-12 at 32B enter both the ladder decline and the 32B half of D_reader.; P3b-P5: RET N-80 and RET N-12 at 32B enter both the fixed-share flatness test and the 32B half of D_reader.; P2-P4: WB N-80 and WB R-80 on the primary draw appear in P2's matched-length contrast and in P4's primary-draw interaction (reported as exploratory); only the replicate arms are exclusive to P4.; P3a-P6: the measured k3 - static3 residual (+17.2) anchors both the reachability argument for the twin-adoption limb and P6's target value.
