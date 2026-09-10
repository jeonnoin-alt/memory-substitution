=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: exemplar_lottery — headline P1 is **open**; open 3 / entailed 0 / near-entailed 0 / unresolvable 2; verdict pass

- P1 [open] falsifier: Draw SD at or below the seed SD, or a draw range below half the mean gap.
  reason: The falsifier is disjunctive and its first branch is exactly the null outcome, since with draws scored on 548 episodes and seed cells on 274 pure sampling puts the draw SD near 0.7x the seed SD and the stated +-35% chi-square CI on 16 draws separates that from the 2x claim, although the range branch is close to self-confirming because an observed 16-draw range is inflated by sampling noise (about 7 net) while the mean gap it must exceed is small by hypothesis.
- P2 [unresolvable] falsifier: R_full minus F_best-heldout above 8 net.
  reason: The evaluation cell is a quarter of the grid (about 134 episodes, per-arm SE near 4 net) while the +-8 floor was calibrated on 548-episode paired cells, so the falsifying value sits inside that cell's noise and confirming or falsifying under a CI rule would demand an observed gap near 1 or near 15 net respectively.
  fix: Cross-fit rather than quarter: select the best draw on all seed-1 cells (both splits, 274 games), evaluate R_full vs F_best on all seed-2 cells, average with the mirror, or restate the floor scaled to the E5 cell (about +-16).
- P3 [unresolvable] falsifier: SD_self at or below SD_expert.
  reason: An SD estimated from 8 draws carries roughly a +-50-60% chi-square CI and the variance ratio needed to separate 1.5x from 1.0x at df 7 vs 15 is about a 1.65x SD ratio, so the falsifying and confirming regions overlap under the proposal's own SD-precision argument, which it stated only for the 16-draw case.
  fix: Run 16 self-pool draws to match the expert arm and pre-register the SD-ratio threshold from an F-test at df 15,15 (about 2x), or test the variance difference directly by bootstrap over games against a stated MDE.
- P4 [open] falsifier: C_short at least 8 net below R_full, or C_worst within +-8 of R_full.
  reason: Both branches sit on full-size paired cells and both are live outcomes - a one-time length rule may fail to recover retrieval, and the negative control may fail to lose - and the proposal itself concedes the second branch would also remove P1's premise.
- P5 [open] falsifier: Mean paired residual above 8 net (retrieval beats a same-bank fixed draw on average).
  reason: The mean residual rests on 8 paired same-bank comparisons totalling 4,384 episodes per side, so a genuine 8-net retrieval advantage would be plainly visible, although the second clause (across-sample SD larger than across-seed SD) is given no falsifier and is weakly estimated from 8 samples.
- shared terms: P1-P2: both read the same 16 F_d arm-level scores, and if the draws cluster (P1's falsifier) the held-out best draw collapses to the draw mean, mechanically enlarging R_full minus F_best and pushing P2 toward its own falsifier.; P1-P3: SD_expert is the quantity P1 tests and the denominator of P3's 1.5x ratio, so one estimate fixes the other.; P2-P4: both are residuals against the same R_full mean net score, so a high or low R_full shifts them together.; P1-P4: P4's second falsifier (C_worst within +-8 of R_full) asserts exemplar choice does not matter, which is the direct negation of P1's premise.
