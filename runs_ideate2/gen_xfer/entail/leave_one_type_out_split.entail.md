=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: leave_one_type_out_split — headline P1 is **unresolvable**; open 1 / entailed 0 / near-entailed 0 / unresolvable 4; verdict revise

- P1 [unresolvable] falsifier: Any LOTO cell shows at least +12 net with CI excluding +8.
  reason: The headline comparison is scored on valid_unseen only (about 134 of the 274 games), so the asserted +/-8 floor, justified by the claim that the LOTO composite keeps the full 274 x 2 cell, does not apply; at the unseen-half noise (roughly +/-11) confirmation needs a point estimate near or below zero and the falsifier needs about +20, leaving almost the whole plausible range unresolved.
  fix: Define the headline on the full 274 x 2 LOTO composite (or run 4 seeds on valid_unseen) and set the +8/+12 bands from the actual unseen-cell CI so the confirm and falsify regions are separated by more than the noise.
- P2 [unresolvable] falsifier: Expert LOTO at or above -2 net (no harm), or the two rankings disagree.
  reason: Both parts sit under the proposal's own +/-8 floor (a 6-net harm claim and a -2 net cut are inside cell noise), and exact tau=1 over three writers whose gains almost certainly differ by less than the floor is decided by noise, so rank disagreement fires near-certainly regardless of the mechanism.
  fix: Replace exact tau=1 with a pre-registered adjacent-writer gap at or above the resolvable margin, and add seeds so a 6-net LOTO harm lies outside the paired CI.
- P3 [open] falsifier: LOTO adapter at most +4, or LOTO retrieval at or above the LOTO adapter, or the all-type adapter at or above within-type retrieval.
  reason: The falsifier is a disjunction of three comparisons, two of them plain sign comparisons that any outcome resolves, and adapter overfitting to the trained types is a live outcome that full-size composite cells can show.
- P4 [unresolvable] falsifier: static-5 at or above adapter minus 4 net.
  reason: The confirm threshold (6 net) and the falsify threshold (4 net) both lie below the stated +/-8 cell noise floor and are only 2 net apart, so the comparison cannot come out either way at the stated power.
  fix: Add seeds to the adapter and static-5 cells until the paired MDE is under 4 net, and state one decision boundary instead of a 4-to-6 dead zone.
- P5 [unresolvable] falsifier: Seen minus unseen at most 2 net under LOTO for the self writer.
  reason: The estimand is a contrast between two non-overlapping half-cells (about 140 and 134 games at 4 seeds) whose difference carries roughly sqrt(2) times the half-cell noise, so a 2-net falsifier is deep inside that noise and 2-to-10 is a dead zone.
  fix: State the MDE for the seen-minus-unseen contrast itself and add seeds until 2 net lies outside its CI, or replace the split with a per-game room-overlap covariate regressed on the LOTO gain.
- shared terms: P1-P2: P2's within-type gain ranking is read off the same standard-bank cells P1 requires to reach +16, and its harm term is the same LOTO gain P1 bounds at +8, so one set of cells determines both.; P1-P3: P3's clause that the LOTO adapter exceeds LOTO retrieval by 8 uses the same LOTO expert retrieval cell P1 bounds, so a confirmed P1 supplies that conjunct as soon as the adapter clears +8.; P3-P4: both are differences against the same LOTO adapter composite cell, so an error in that single cell moves both.; P1-P5: P5's unseen term is the valid_unseen LOTO self cell that P1 already caps at +8, so P1 bounds the quantity P5 must exceed by 10.
