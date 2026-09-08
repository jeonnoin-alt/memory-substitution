=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: train_dose_sets_substrate — headline P1 is **unresolvable**; open 0 / entailed 0 / near-entailed 2 / unresolvable 4; verdict revise

- P1 [unresolvable] falsifier: A monotone increasing r ladder (co-training) or a flat ladder.
  reason: The predicted down-leg is 0.15 g (about 4-5 net points) against a stated 5-point pooled MDE and a +/-4.6 CI, and the up-leg clause (r(1) or r(3) > r(0)) carries no margin at all, so a flat ladder plus noise satisfies the disjunction and cannot be told apart from the prediction.
  fix: Attach a pre-registered margin above the pooled CI to the up-leg, make the deterministic H NLL ladder the primary estimand with its own MDE, and raise seeds so 0.15 g clears the CI.
- P2 [unresolvable] falsifier: r(decoy3) close to r(3) rather than to r(0), i.e. a long-prefix SFT artefact.
  reason: Both halves are equivalence claims at 0.1 g (about 3 net points) against a +/-4.6 pooled episode CI, and the fallback proxy is declared at exactly that same 0.1 g resolution and in NLL units with no stated mapping onto r, so neither the confirming nor the falsifying pattern can be resolved.
  fix: Pre-register the memory-free NLL gap in NLL units as P2's primary estimand with an equivalence margin strictly above its measured noise, and add seeds so the accuracy version clears +/-4.6.
- P3 [unresolvable] falsifier: F flat or falling in k_train, F(7) - F(0) < 6 net, or F(decoy3) - F(0) > 2.
  reason: Monotonicity across four doses requires adjacent gaps of roughly 2 net points against a +/-4.6 pooled CI, the 6-point span is a difference of differences whose CI exceeds the stated 5-point MDE, and the 2-point decoy clause is far inside the noise.
  fix: State the CI for the F difference-of-differences, drop the monotonicity clause in favour of the single pre-registered F(7) - F(0) contrast with a margin above that CI, and raise the decoy equivalence margin above it too.
- P4 [near_entailed] falsifier: rho(D, dl) < 0.5, mean dl on the self-rollout pool above half the expert pool's, or r rising monotonically on the self-rollout pool while dl > 0.
  reason: The self-rollout pool consists of the model's own successful trajectories, so its base action-token loss and hence dl are low by construction and the halving clause cannot come out false; what remains is a correlation over per-type cells whose +/-13-15 point accuracy noise attenuates rho toward zero through a measurement mechanism the design neither names nor controls.
  fix: Demote dl-halving to a manipulation check, compute D from the deterministic H NLL proxy so cell noise is bounded, and pre-register the rho threshold against a null simulated from the actual cell CIs.
- P5 [near_entailed] falsifier: r(CD, k_s=3) equal to r(CD, k_s=0), making the effect SFT-specific.
  reason: A student trained with a filled k=3 block and then scored with an empty one is off its own training prompt distribution, so the predicted drop is delivered by format mismatch rather than by information abundance, and unlike the SFT side there is no CD-decoy student to separate the two.
  fix: Add a CD student trained on token-matched decoy items (k_s=decoy3) and evaluate the k_s=3 student at its training dose, so the prompt-mismatch component is measured rather than attributed.
- P6 [unresolvable] falsifier: k=1 or k=3 dominating both deployment conditions, or overlapping bootstrap argmax sets.
  reason: Adjacent doses are predicted to differ by the same 4-5 net points as the pooled CI, so a bootstrap argmax over four noisy cells is close to uniform and neither a 2-rung separation nor non-overlapping argmax sets can be established either way.
  fix: Replace the argmax with a pre-registered pair of contrasts (for example r(1) - r(7) memory-free and A+(7) - A+(1) matched), each with a margin above the pooled CI.
- shared terms: P1-P4: D_t(k) = r(0) - r(k) is built from the same r ladder P1 predicts, so P4's correlation is P1's ladder re-plotted against a fixed dl.; P1-P6: P6's memory-free argmax is simply the maximum of P1's r(k_train) ladder.; P2-P4: r(decoy3) is both the placebo comparison in P2 and the decoy-3 cell of P4's correlation.; P3-P6: F = A0 - A- and the matched-memory optimum share the measured A0(k) of each arm, so any shift in A0 moves both.
