=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: stage_conditional_item_value — headline P3 is **near_entailed**; open 0 / entailed 0 / near-entailed 2 / unresolvable 3; verdict revise

- P1 [unresolvable] falsifier: The 95% CI of the ratio v_S1/v_S0 lies entirely below 0.6.
  reason: v_S0 for a single item class is a single-digit net carrying a +/-5.7 CI, so a ratio built on that denominator cannot have a CI bounded entirely below 0.6, and the intersection subset additionally conditions on games where the k=0 policy already reached pickup unaided, selecting out the pre-procedure value whose absence the falsifier requires.
  fix: Test a pre-registered absolute margin (v_S0 minus v_S1) with a stated MDE instead of a ratio, and stratify by whether the k=0 run reached pickup so games that need navigation help stay in the comparison.
- P2 [unresolvable] falsifier: I2 and I3 lie within +/-5 of each other at S2, or the S0 gap is at least as large as the S2 gap.
  reason: At about 650 contrasts the I3-I2 gap carries a CI near +/-10 and the cross-stage 2x comparison is a ratio of two such gaps, so the <= -5 and >= +5 thresholds and the +/-5 equivalence bound all sit inside the stated noise.
  fix: Raise the S2 cells to at least the 1,096-contrast size (more seeds or a broader stuck-point definition) and pre-register the cross-stage comparison as an absolute difference of differences with its MDE.
- P3 [near_entailed] falsifier: The bootstrap CI of (stage + interaction) minus class includes zero or is negative.
  reason: The comparison is asymmetric by construction, putting two components (stage main plus interaction) against one whose levels are three same-type expert items further deflated by subtracting I4, while the stage levels are made maximally different (full episode versus stuck-prefix continuation), so a class-dominant result is close to excluded before any data are collected.
  fix: Compare stage main against class main symmetrically with the interaction reported separately, and widen the class factor to span I1-I5 including the static and cross-type placebo arms.
- P4 [near_entailed] falsifier: The Spearman difference's CI includes zero for the outcome-reinforced scorer.
  reason: S2 per-item values come from about 650 partial episodes with fewer contrasts per item than the 1,096-contrast S0 values, so the S2 correlation is attenuated by measurement noise alone and the predicted sign is forced by differential reliability rather than by stage-conditionality, a channel P4 never disattenuates.
  fix: Disattenuate both correlations by their split-half reliabilities, or subsample the S0 contrasts per item to match S2, before taking the paired difference.
- P5 [unresolvable] falsifier: The single and pairwise removal effects agree within +/-5 net.
  reason: At about 325 contrasts each cell is roughly +/-10.5 and the contrast of two removal effects is near +/-15, so a +/-5 agreement bound is far inside the noise, and the quantity also absorbs I3's own removal effect instead of isolating the buffering interaction it claims.
  fix: Define the estimand as the interaction (pairwise minus both single removals), run T4 at the full 1,096-contrast size, and state its MDE.
- shared terms: P1-P3: the v_S0 and v_S1 cells for I1/I4 are the same quantities that form the stage main effect in P3's decomposition, so P1's ratio and P3's stage component move together.; P2-P3: the S2 I3-I2 gap is the class x stage interaction cell that P3 counts on the stage-plus-interaction side, so P2 holding largely determines P3's sign.; P3-P4: both are functions of the same S0 and S2 per-item value tables, so noise in the S2 table simultaneously lowers P4's S2 correlation and inflates P3's interaction component.; P2-P5: the I2 harm term at S2 appears both in P2's I2-versus-no-item contrast and in P5's single removal of I2 from the k=3 set.
