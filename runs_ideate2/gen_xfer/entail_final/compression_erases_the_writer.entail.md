=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: compression_erases_the_writer — headline P3 is **open**; open 5 / entailed 0 / near-entailed 0 / unresolvable 1; verdict pass

- P1 [open] falsifier: Any of the four self contrasts whose 95% CI covers 0 or whose upper bound is below +6, i.e. writer-written summaries or six-procedure distillations matching or beating the writer's own raw traces.
  reason: Nothing in the construction forces raw above self-compressed - L2 injects all six type procedures at matched tokens and could beat k=3 raw - and a null D gives about [-3,+3], which the stated rule reads as falsified.
- P2 [open] falsifier: Any of the four foreign contrasts with a CI covering 0 or a lower bound above -6, and explicitly any single cell in which foreign raw beats foreign compressed.
  reason: Foreign raw trajectories could out-perform the foreign writer's own summaries (format mismatch is not guaranteed to be fatal), so the sign is not fixed by the design and a null falsifies at the stated noise.
- P3 [open] falsifier: I(r) with a 95% CI covering 0, or negative for either reader.
  reason: I(r) is arithmetic on P1's and P2's estimands (both at their margins force I >= +12), but its falsifier is reachable whenever either component fails, and +8 against +-4.2 keeps the null CI [-4.2,+4.2] clear of the boundary.
- P4 [open] falsifier: The compressor-identity difference with a 95% CI excluding 0 in either direction (reader wording helping or hurting).
  reason: This is an equivalence claim confirmed by a null, but the band (+-6) is twice the stated half-width (+-3), so a real 6-point wording effect gives about [3,9] and is read as falsifying.
- P5 [open] falsifier: Self-L2 differing from foreign-L2 with a CI excluding 0, or either L2 cell exceeding the static expert prompt with a CI entirely above 0.
  reason: The rival (writer identity as a main effect at every level) produces exactly this, and the trivial-by-construction case - near-identical L2 texts from the two writers - is caught by the pre-registered edit-distance rule that demotes clause 1 to a manipulation check.
- P6 [unresolvable] falsifier: S(r) with a CI covering 0 or a negative point estimate (thoughts are filler regardless of author).
  reason: The margin (+6) is only 1.4 times the four-cell half-width (+-4.2), violating the proposal's own 'twice the half-width' rule, so the predicted +6 gives about [1.8,10.2] and the null gives [-4.2,+4.2] - overlapping intervals that cannot separate the prediction from its falsifier.
  fix: Either raise S(r)'s margin to at least +8.4 (twice the stated four-cell half-width) or run the four L0/L0s cells at about 12 seeds so the four-cell half-width falls to about +-3.
- shared terms: P1-P3: I(r) is literally D(self,L2) minus D(foreign,L2); P1 and P2 at their stated margins force I >= +12, so P3 cannot fail once both hold.; P2-P3: same shared estimand D(foreign,L2), and P2's falsifier (foreign raw winning) is also the main route to P3's falsifier.; P3-P5: both read gain(self L2) and gain(foreign L2); under P5's null, I(r) collapses to the raw self-minus-foreign gap and stops being an interaction with compression.; P4-P5: P4's writer-compressed foreign L2 cell is the same measured cell as P5's foreign L2 term.; P1-P6 and P2-P6: S(r) reuses gain(self L0) and gain(foreign L0), the L0 terms of D(self) and D(foreign).
