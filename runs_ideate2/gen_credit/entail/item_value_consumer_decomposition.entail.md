=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: item_value_consumer_decomposition — headline P2 is **open**; open 1 / entailed 0 / near-entailed 2 / unresolvable 2; verdict revise

- P1 [near_entailed] falsifier: Under reader B all classes lie within +/-5 of each other, or the ordering C2 < C3 < C1 inverts.
  reason: E0 screens reader B for a k=3 net of at least +10 and swaps in Qwen3-14B otherwise, so the exact mechanism the prediction names as its escape (a weaker reader that ignores item content) is filtered out before E3 ever runs, and the residual equivalence bound of +/-5 is tighter than the roughly +/-7 CI on a difference of two +/-5 class cells.
  fix: Keep the screened-out reader as a reported arm and run E3 on it rather than replacing it, and size the class cells so the equivalence bound (+/-5) exceeds the difference CI.
- P2 [open] falsifier: Disattenuated rho_AB at or above 0.8 (residuals transfer), or rho_AA below 0.3 (residuals are estimator noise).
  reason: Both branches are reachable on the same items and same frozen sets: a shared procedural component surviving the static subtraction would push the disattenuated ratio above 0.8, and per-item residuals built from as few as 8 binary paired contrasts can plausibly fail the rho_AA >= 0.3 floor, which the proposal names as a falsifier rather than as an excuse.
- P3 [unresolvable] falsifier: The C5-C4 difference is within +/-5 under both readers, or is more negative under A than under B.
  reason: C5-C4 is a difference of two +/-5 class cells (CI about +/-7) and the reader contrast is a difference of differences (CI about +/-10), so the predicted -8 under B versus -3 under A split and the +/-5 equivalence bound both lie inside the stated noise.
  fix: Size the C4/C5 cells for a +/-3 net margin (roughly four times the episodes) or recast the estimand as a per-item paired A-minus-B difference with a stated MDE.
- P4 [unresolvable] falsifier: A-values under B gain as much as B-values under B, or B-values under B gain nothing over similarity top-3.
  reason: Every threshold in the claim (a +/-5 equivalence band and a >= +5 gain) is at or below the stated +/-5.7 per-cell precision, so neither the predicted split nor either falsifying branch can be separated from noise.
  fix: Enlarge the E4 cells or pair the selections game-by-game and report the paired difference CI so the MDE is 3 net or better, and pre-register a winner's-curse correction for values estimated from 8 contrasts.
- P5 [near_entailed] falsifier: rho_AC no greater than rho_AB + 0.1.
  reason: Reader C shares A's backbone, tokenizer and capability while B differs in both family and scale, so rho_AC exceeding rho_AB follows from a confound this contrast leaves uncontrolled (the same-family 8B ablation is not used here), and the 0.1-to-0.2 dead band is narrower than the propagated error of a disattenuated ratio at 150-250 items.
  fix: Add a capability-matched cross-family 32B reader, or anchor rho_AC against an A-versus-A-with-different-seed ceiling, and state the SE of the disattenuated ratio instead of that of a raw Spearman.
- shared terms: P2-P4: the A-values-under-B arm of E4 is the operational image of the same cross-reader agreement rho_AB that P2 estimates, so a low rho_AB determines P4's within-+/-5-of-similarity half.; P2-P5: P5's statistic is rho_AC minus rho_AB using the same rho_AB and the same rho_AA disattenuation denominator, so P2's estimate moves P5's test.; P1-P3: every E3 class is scored against the same natural k=3 without-baseline on the same reader-B episodes, so one baseline error shifts C1-C2 and C5-C4 together.
