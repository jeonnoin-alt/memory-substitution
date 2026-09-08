=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: self_pool_break_even — headline P1 is **open**; open 3 / entailed 0 / near-entailed 1 / unresolvable 1; verdict pass

- P1 [open] falsifier: Either 10% draw is at least 8 net below the full self pool with the paired CI excluding 0.
  reason: At b=10% the low-p_t low-f_t types can fall below three same-type items, so an 8-net aggregate deficit is reachable through the near-duplicate/coverage channel the proposal names, and the mandatory b=0.5%/m=1 control shows the sweep can resolve an 8-net drop; the equivalence margin does equal the stated +/-8 cell noise floor, so a true 7-net deficit still scores as confirmation.
- P2 [near_entailed] falsifier: m=3 is at least 8 net below m=all in either bank.
  reason: With k=3 the retriever can inject at most three same-type items, so a cap at m=3 removes no item the reader would otherwise have seen and the count channel the prediction calls saturation is fixed by construction; only within-type match quality can produce the falsifier, and no arm separates that channel.
  fix: Cross the coverage cap with retrieval depth (m=3 at k=7, or m=3 vs m=all at k=1), or add an m=3 cell whose three retained items are the worst-matched same-type items, so the item-count axis is testable apart from which three items the retriever returns.
- P3 [open] falsifier: Expert minus self at least 8 net with CI excluding 0 (the reverse, self beating expert by 8, is also reported).
  reason: Nothing in the construction ties the 1,465 replayed walkthroughs to the 1,892 on-policy successes and both directions are reported, so an 8-net separation at the stated floor is reachable; note the two stated criteria can disagree, since self +10 vs expert +17 satisfies the 8-net clause while breaking the 1.3 ratio bound.
- P4 [unresolvable] falsifier: Spearman rho at most 0.2, or heat not among the two largest per-type deficits.
  reason: rho is computed over six points from per-type deficits whose cells are roughly 45 games (per-type noise far exceeds the deficits being ranked), so 0.6 and 0.2 are not separable and 0.2-0.6 is a dead zone; the stated pooling is also unavailable because b=2.5% cells exist only for the Qwen3 reader at k=3 (arm E has only 100%/10% at k=1, arm F only 100%/10% for EXAONE).
  fix: Add b=2.5% cells for the EXAONE reader and for k=1, and attach a paired-bootstrap CI to rho (or replace the rank test with a per-type regression of deficit on 1/(p_t f_t) with a stated MDE).
- P5 [open] falsifier: Own minus other at least 8 net with CI excluding 0 in either reader.
  reason: Both pools and both swap directions are actually run, so an own-pool proximity advantage above the stated floor is reachable; the falsifier is one-sided, so the other backbone's pool beating the reader's own by 10 net would break the literal within-8 claim without triggering the stated falsifier.
- shared terms: P1-P2: both deficits are scored against the same self-100% (m=all) full-bank cell, so a mis-estimate of that single cell moves both.; P1-P4: P4's per-type deficits are the per-type decomposition of the same self-b vs self-100% difference P1 aggregates, so a confirmed P1 bounds the deficits P4 then has to rank.; P3-P5: both are differences taken against the same Qwen3 self-100% cell (expert minus self; other minus own), so that shared term determines both.
