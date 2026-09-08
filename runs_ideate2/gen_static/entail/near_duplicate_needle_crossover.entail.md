=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: near_duplicate_needle_crossover — headline P3 is **unresolvable**; open 0 / entailed 3 / near-entailed 1 / unresolvable 2; verdict revise

- P1 [entailed] falsifier: RET r=1 minus RET r=0 within the measured floor.
  reason: The r=0 bank deletes every same-category item while the r=1 bank guarantees a retrievable trajectory naming the target product id and its buy action, so the contrast re-describes how the two banks were built and a 10-point gap is forced unless the retriever fails on an item constructed to be its top instruction-text match.
  fix: Make r=0 a same-category, different-product bank (shared category, zero shared attribute phrases) so the contrast isolates near-duplication rather than the mere presence of category-relevant material.
- P2 [near_entailed] falsifier: RET exceeds WB-40 or fixed-2 by more than the floor at r=0.
  reason: With every same-category item removed from the r=0 bank the retriever has nothing selectable to exploit, so the residual can only appear through a cross-category wording transfer the design neither varies nor measures, and the claim is a three-way equivalence asserted exactly at the floor.
  fix: Add a same-category-but-non-duplicate cell (shared category, zero shared attributes) so the retriever has selectable non-duplicate material and a category-level residual is producible.
- P3 [unresolvable] falsifier: WB-40's recovery within the floor of RET's gain, or WB-12 and WB-40 recovering the same fraction.
  reason: With the gate fixing RET's gain at about 10 points and the paired floor at 4-5 points, the half-recovery cut sits at roughly 5 points, i.e. inside the stated noise, so the bootstrap upper bound can only fall below 0.5 when WB recovery is essentially nil, and the WB-12 versus WB-40 clause has no stated margin while those two cells differ in distractor type (same-category siblings versus other-category items) as well as haystack size.
  fix: Gate on a much larger measured RET gain, or add episodes/seeds until the floor is 1-2 points so the 0.5 cut sits outside noise; state a margin for the WB-12 versus WB-40 comparison and hold distractor composition fixed while varying only haystack size.
- P4 [entailed] falsifier: RET's r=0.5 gain exceeds the hit-rate-scaled prediction by more than the floor, or random fixed selection matches RET at r=1.
  reason: Given P2's no-residual-without-near-duplicates claim, gain can accrue only on instructions whose needle was retrieved, so gain equals hit rate times per-hit gain as an arithmetic identity of already-measured terms, and a single fixed pair shared by twelve instructions cannot carry more than two of the twelve needles, so the random-fixed cell cannot match RET by construction.
  fix: Decouple needle presence from retrievability with an arm where the near-duplicate's instruction text is paraphrased so BM25/embedding misses it, and estimate the gain among instructions whose top-2 missed the needle as a separate quantity with a stated MDE.
- P5 [unresolvable] falsifier: RET r=1 exceeds RET r=0 by at least 9 net on valid_seen.
  reason: The falsifying margin (9 net) and the asserted equivalence band (+/-8 net) both lie inside the +/-11 net floor the proposal itself states for 140 games x 2 seeds, so neither the prediction nor its falsifier can be resolved by the stated design.
  fix: Run the r=1/r=0 manipulation on all 274 games or add seeds until the floor is below 8 net, or restate the margins above the +/-11 net floor of the valid_seen subset.
- P6 [entailed] falsifier: fixed-2 below RET by more than the floor at r=0.
  reason: The fixed-2 arm does not change with rate, so P6 is exactly P2's RET r=0 equals fixed-2 clause plus P1's forced 10-point r=1 gain on the identical cells, and its stated falsifier is P2's falsifier restated, so the advertised ordering flip cannot fail once P1 and P2 hold.
  fix: Make the static arm rate-dependent (two fixed exemplars drawn from the same r=1 cluster bank, so some clusters receive a near-duplicate) or drop P6 as a restatement of P1 plus P2.
- shared terms: P1-P3: RET r=1 minus RET r=0 at size 40 is P1's estimand and the denominator of P3's recovery fraction, so the gate that sets its size also sets P3's resolvability.; P1-P6 and P2-P6: P6 is P2's RET r=0 versus fixed-2 contrast combined with P1's r=1 gain, measured on the identical cells.; P1-P4: P4's hit-rate-scaled prediction is constructed from P1's r=1 gain and the logged top-2 near-duplicate hit rate.; P2-P3: WB-40 r=0 and RET r=0 serve simultaneously as P2's equivalence cells and P3's recovery baselines.
