=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: many_shot_averages_detours — headline P2 is **open**; open 3 / entailed 0 / near-entailed 4 / unresolvable 0; verdict revise

- P1 [open] falsifier: RET S within +/-8 of RET E with no step increase.
  reason: Self-pool successes could be as effective as expert ones on both success and steps, and both outcomes are measured on paired cells, so the null is a reachable and visible result.
- P2 [open] falsifier: both routes lose the same within 8 net, or WB48 S loses more than RET S (the most-similar-copying outcome).
  reason: The WB cells are measured independently of the RET cells and the copying outcome is explicitly available, so the interaction can come out at or below zero; the S-vs-E token and item-count mismatch pushes toward falsification rather than away from it.
- P3 [open] falsifier: WB6 S within 8 net of WB48 S or above it.
  reason: A flat or declining S ladder is reachable and the acknowledged 0.87 success ceiling makes failure to gain 9 net more likely rather than less.
- P4 [near_entailed] falsifier: RET P still at least 8 net below RET E.
  reason: P is S with exactly the detour tokens removed and then filtered to the items whose pruned replay still succeeds, so it is near-expert by construction and selection-biased toward easier games; the falsifier requires a residual phrasing or length deficit for which the design supplies no arm and no measurement.
  fix: Add a length-matched sham-prune arm (delete an equal number of non-detour steps, replay-verified) and report P's game/type coverage against S, so a phrasing or length residual can actually be produced and detected.
- P5 [near_entailed] falsifier: RET A within +/-8 of RET E.
  reason: A is selected on the very quantity the prediction is about (and on the harder, longer source episodes that produce it), so A below S with the longest episodes largely re-describes the selection, while the stated falsifier is written against RET E rather than RET S, so a genuine null (A equal to S) never trips the gate.
  fix: State the falsifier against RET S (RET A within +/-8 of RET S falsifies) and match A to S on game difficulty and type so the contrast varies detour steps rather than which games produced long episodes.
- P6 [near_entailed] falsifier: WB48 S episodes track the most-similar item's detours as strongly as RET episodes track theirs.
  reason: The WB prefix is a single fixed 48-item bank per arm, so the most-similar-item regressor draws on only 48 values and the bank-mean regressor has zero within-arm variance, attenuating or removing the slope regardless of whether consensus is the mechanism, and no MDE is stated for the asserted slope null.
  fix: Draw a different randomized bank per game or per block so the most-similar-item and bank-mean detour regressors vary within an arm, and pre-register an equivalence bound (a slope MDE) for the WB null.
- P7 [near_entailed] falsifier: WB48 M at least 8 net below WB48 E.
  reason: M is a 50/50 interpolation of banks already measured in P2, so its value is pinned by those cells unless the response to detour rate is non-monotone (a mechanism the proposal never names or models), and the RET M clause (between RET E and RET S) carries no margin so it cannot fail outside the floor.
  fix: Pre-register a quantitative interpolation test with an MDE (WB48 M within a stated band of the E-S midpoint) and attach explicit thresholds to the RET M ordering clause.
- shared terms: P1-P2: RET S minus RET E is P1's estimand and the subtracted half of P2's interaction, so a null P1 leaves P2 resting entirely on the WB cells.; P2-P3: WB48 S and WB48 E are two of P2's four cells and the top rungs of both of P3's ladders.; P2-P7: WB48 E and WB48 S are measured once and jointly pin the expected value of WB48 M.; P1-P4-P5: RET E and RET S are the single measured comparators for the pruned and amplified bank predictions and for the design's stop gate.; P1-P6: the RET S versus RET E step difference asserted in P1 is the same step data whose within-arm slope P6 regresses on detour steps.
