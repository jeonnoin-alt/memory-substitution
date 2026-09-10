=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: leave_one_type_out_split — headline P1 is **open**; open 8 / entailed 0 / near-entailed 1 / unresolvable 1; verdict pass

- P1 [open] falsifier: cell 3 minus cell 1 at or above +8 net, i.e. other-type expert items still carrying a large gain.
  reason: Wrong-type demonstrations can still supply format, navigation and action-validity priming, so a >= +8 LOTO gain is reachable, and at +-4 both the predicted -8 and the rival +16 sit several MDE from the boundary.
- P2 [open] falsifier: Any qualifying LOTO cell at or above +8 net.
  reason: Reachable in every listed cell, though the >= +16 qualification filter can silently drop a writer that shows a positive LOTO gain, and the 2-seed cell 22 carries an +-8 MDE equal to the decision boundary.
- P3 [unresolvable] falsifier: cell 6 minus cell 7 below +6.
  reason: The hypothesis's own predicted +9 lies only about half an MDE above the +6 boundary, so a true +9 reads as falsified a sizeable fraction of runs and the proposal's stated 'each value at least one MDE from the boundary' rule fails for this clause.
  fix: Run cells 6 and 7 at 8 seeds (MDE +-4) and move the boundary to +4, or restate the predicted separation so it sits at least one MDE above the boundary.
- P4 [open] falsifier: cell 3 minus cell 4 above -6, i.e. self-pool wrong-type items harming as much as expert wrong-type items.
  reason: Writer-independent wrong-type harm is a real and named outcome that the same two cells can show, and the predicted -10 sits one MDE below the boundary with the rival 0 one and a half MDE above.
- P5 [open] falsifier: cell 3 minus cell 1 above -4 (wrong-type expert items merely ignored).
  reason: A reader that ignores out-of-type items yields exactly 0 and is one MDE above the boundary, so the falsifier is reachable - but this is the identical estimand as P1 under a stricter boundary, so P1 follows from it.
- P6 [open] falsifier: Harm below 6 net, which voids the harm predictions rather than confirming them.
  reason: A reader insensitive to retrieved content produces this outcome directly, and the predicted -15 is far outside the +-5.7 MDE around the 6-point gate.
- P7 [open] falsifier: cell 12 minus cell 2 below +6 (adapter overfits the trained types, or five procedures carry the same generic gain).
  reason: Adapter and static-5 prompt carry the same five types' information in two substrates, so either ordering is reachable, and the predicted +10 and the rival 0 are one and one and a half MDE from the boundary.
- P8 [near_entailed] falsifier: cell 12 minus cell 3 below +12.
  reason: cell12 - cell3 = (cell12 - cell2) + (cell2 - cell1) - (cell3 - cell1), so P7 at +6 and P5 at -4 already deliver +12 once the five-procedure prompt reaches its predicted +2 gain; the only route to the falsifier is a static-5 gain below +2, a quantity the proposal predicts but neither controls nor makes a claim on, and the proposal's own note credits only P1a, not P5.
  fix: Predict the static-5 prompt's gain over k=0 as its own clause with its own boundary, or restate P8 net of the static-5 prompt so its boundary is not the arithmetic sum of P7's and P5's margins.
- P9 [open] falsifier: cell 6 minus cell 13 below +8 (weights matching retrieval within-type).
  reason: The all-type adapter is trained on the same expert pool that the standard bank retrieves, so it could match or beat retrieval within-type, and predicted +15 and rival 0 lie about 1.2 and 1.4 MDE from the boundary.
- P10 [open] falsifier: cell 14 minus cell 12 above -4, i.e. weights making the reader robust to, or willing to ignore, wrong-type items.
  reason: The robustness rival is a genuine outcome of the same paired cells and sits one MDE above the boundary; nothing in the adapter training forces the reader to keep following retrieved wrong-type procedures.
- shared terms: P1-P5: identical estimand (cell 3 minus cell 1); P5's boundary of -4 logically implies P1's < +8, so P1 cannot fail if P5 holds.; P4-P5: both read cell 3, so a noisy LOTO expert cell moves the two clauses together.; P7-P5-P8: P8 is the algebraic sum of P7's margin, P5's margin and the measured static-5 gain (cell 2 minus cell 1).; P1-P3-P9: cell 6 (standard expert) supplies P1's +16 premise, P3's minuend and P9's minuend.; P7-P8-P10: the same LOTO adapter cell 12 is the reference in all three, so one adapter cell decides the whole substrate-flip block.
