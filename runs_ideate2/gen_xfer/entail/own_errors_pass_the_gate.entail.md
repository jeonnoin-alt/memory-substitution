=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: own_errors_pass_the_gate — headline P2 is **open**; open 2 / entailed 0 / near-entailed 3 / unresolvable 1; verdict revise

- P1 [open] falsifier: Harm < 6 net at 50% and also at 100%.
  reason: A reader that ignores or repairs grafted wrong procedures (1.5 expected contaminated items among k=3) simply shows no success loss, and the 100% backstop roughly doubles the effect, so the no-harm world is separable from the >=6 world at the stated half-width.
- P2 [open] falsifier: recall(self host) >= recall(foreign host) for either reader, or both readers showing the same host ordering (pool-difficulty main effect, no interaction).
  reason: Both readers are crossed with both host pools on identically edited, game-paired items and the ceiling/floor rule keeps recall off the rails, so a null, a reversal, or a pure pool main effect are all measurable against the 10-point margin at a 4-point interaction SE.
- P3 [near_entailed] falsifier: Recall within +-4 of the unparaphrased original ALTHOUGH NLL falls by the amount seen for self hosts.
  reason: The falsifier is gated on the paraphrase actually driving NLL down to self-host levels - an outcome the design neither guarantees, measures against a tolerance, nor controls - and the +-4 equivalence band is inside the ~+-5.6 half-width of a recall difference at SE ~2 per arm.
  fix: Pre-register an NLL-matching criterion (retain only paraphrases within a stated NLL distance of self-host items and report the qualifying fraction) plus a two-sided equivalence bound with item counts giving half-width <= 3.
- P4 [near_entailed] falsifier: D1 self-host recall within +-4 of D0.
  reason: Only the first clause carries a falsifier: the gap-halving clause the hypothesis rests on can fail (D1 lifting foreign-host recall equally, leaving the gap intact) with no stated falsifying outcome, and the +-4 band is inside the recall-difference noise.
  fix: Add an explicit falsifier on the gap estimand (gap_D1 > 0.5 x gap_D0 with CI excluding), score D0 and D1 on identical paired items, and size the cells for a half-width <= 3.
- P5 [unresolvable] falsifier: leverage(foreign) >= leverage(self) with CI excluding the 0.15 margin.
  reason: Leverage is a ratio whose denominator is itself a +-5 gain that differs between self and foreign pools, so the CI on the 0.15 difference is far wider than the margin (and the normalisation actually pushes against the prediction whenever the foreign clean gain is the smaller denominator).
  fix: Score absolute harm (clean minus contaminated net points) per host with a paired cluster bootstrap and a margin at least twice the reported half-width, or add seeds until the leverage CI is under 0.15.
- P6 [near_entailed] falsifier: D0 gate false-positive rate on clean foreign items >= 20%, or its cost >= 6 net.
  reason: The second clause is true by construction - the writer-identity gate deletes every foreign item, so its cost IS the mixed-store minus self-store gain, the same quantity it is compared with - and the <3 vs >=6 cost band lies inside the +-5 per-cell noise, leaving only the FPR clause genuinely able to fail.
  fix: Drop or restate the identity-gate clause as a measured quantity with its own CI, and set the cost falsifier at a margin at least twice the +-5 half-width (or add seeds on the gated cells).
- shared terms: P2-P3: the unparaphrased foreign-host D0 recall is the same measurement in both, so P3's baseline is P2's foreign-host cell.; P2-P4: P4's self-foreign recall gap IS P2's estimand, so a null in P2 leaves P4's halving clause undefined.; P1-P5: P5's leverage numerator and denominator are built from the same clean-bank and C1-contaminated Q->Qwen3 cells that produce P1's Gate-0 harm.; P5-P6: both rest on the clean self vs clean foreign gains (P6's 'foreign excess over the self pool', P5's clean denominators).
