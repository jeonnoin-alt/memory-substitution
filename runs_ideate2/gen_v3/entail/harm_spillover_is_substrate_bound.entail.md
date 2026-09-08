=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: harm_spillover_is_substrate_bound — headline P1 is **unresolvable**; open 0 / entailed 0 / near-entailed 2 / unresolvable 5; verdict revise

- P1 [unresolvable] falsifier: rho_sft <= rho_context + margin.
  reason: With D gated at only about 10 net points, rho values of 0.1 versus 0.3 are sibling harms of 1 versus 3 net points against a +-7 sibling CI, so the claimed doubling is roughly an order of magnitude inside the stated noise, and no p on the {0,0.1,0.3,0.5} grid is guaranteed to match D across substrates.
  fix: Power the sibling cell to an MDE of 1-2 net points (or raise D with a stronger poison or higher p until 2x rho is several CI widths) and pre-register the interpolation used to match D across substrates.
- P2 [near_entailed] falsifier: Sp_context exceeds r_x x (direct harm per retrieved poisoned item).
  reason: For a frozen model the prompt is the only channel from bank to behaviour, so sibling harm without a cross-retrieved poisoned item is excluded by construction, and the falsifier survives only through per-item harm being larger on sibling types than on the poisoned types where it is estimated, a mechanism the design neither names nor measures.
  fix: Estimate per-retrieved-item harm separately on sibling-type episodes (an arm that forces a poisoned item into sibling prompts) so the inequality compares two independently measured terms rather than one term against itself.
- P3 [unresolvable] falsifier: Both substrates linear, or SFT harm super-linear at low p.
  reason: Under a 10-net-point harm ceiling every quantity in the prediction is a 1-4 net point contrast against +-5 (D_context(0.1) of 1-3.5, a 1.5x ratio between D_sft(0.5) and D_sft(0.3)), and the clause that D_sft(0.1) is within noise of zero is satisfied by low power alone.
  fix: Score dose shape on a continuous per-episode measure (entry-step rate or wrong-action rate) instead of net success points, and power the p grid to an MDE of about 2 net at p=0.1.
- P4 [unresolvable] falsifier: omega >= 0.9.
  reason: A ratio whose numerator and denominator each carry +-5 on a 10-point base has a bootstrap CI wide enough to cover both 0.7 and 0.9, so the compliance-trap alternative cannot be separated from the prediction.
  fix: State the MDE for omega and reach it (direct harm of about 25 net, or several times the episode count), and report D(clean) and D(absent) with their own CIs rather than only the ratio.
- P5 [unresolvable] falsifier: D_opsd >= D_sft, or the discount not tracking the measured c(p).
  reason: At p=0.1 the test is vacuous because P3 already predicts D_sft(0.1) is zero within noise, and at p=0.5 a predicted D_opsd of about c x 10 cannot be separated from D_sft of about 10 when both carry +-5.
  fix: Drop p=0.1, state the margin for the product test in net points, and power D_sft(0.5) to at least about 25 net so a compliance discount of 0.5 sits several CIs from unity.
- P6 [near_entailed] falsifier: Internalized harm recovers at least as often as in-context harm.
  reason: V1 and V2 put the divergence at a single fixed step of each type's procedure, so the KS coincidence of in-context entry steps with the retrieved item's divergence step is fixed by how the poison was built and has essentially one degree of freedom; only the recovery clause is contingent, and it rests on the few dozen harmed episodes per substrate that a 10-net-point harm yields.
  fix: Add a poison variant whose divergence step varies across items so the KS test can fail, and pre-register a powered MDE for the recovery-fraction halving on the harmed subsample.
- P7 [unresolvable] falsifier: Any arm moves a control type beyond margin.
  reason: The margin is never stated and the control cells are the smallest in the design, so no arm can be shown equivalent on the controls at the achievable precision and the reassignment-to-forgetting rule can never be triggered reliably.
  fix: Pre-register an equivalence margin in net points for the control types, power those cells to it, and state in advance how a control-type change is subtracted from D and Sp.
- shared terms: P1-P4: rho and omega both take the trained student's direct harm D(absent) as their base, so a mis-estimated D moves the spillover ratio and the override fraction together.; P3-P5: D_opsd(p) = c(p) x D_sft(p) contains D_sft(p), so P3's prediction that D_sft(0.1) is zero within noise turns P5's p=0.1 comparison into an identity between two zeros.; P1-P2: Sp_context is the numerator of rho_context in P1 and the estimand of P2, so P2's retrieval accounting bounds rho_context near zero and mechanically favours P1's ordering.; P3-P6: entry step and recovery are scored only on harmed episodes, whose count is set by D(p), so the P3 dose curve determines the sample available to P6.
