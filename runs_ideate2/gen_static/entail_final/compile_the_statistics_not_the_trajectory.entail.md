=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: compile_the_statistics_not_the_trajectory — headline P1 is **open**; open 5 / entailed 0 / near-entailed 2 / unresolvable 1; verdict pass

- P1 [open] falsifier: Paired 95% bootstrap CI upper bound below +10.
  reason: Nothing in the design forces the reader to consult a 300-token frequency table, and M1 sits well above the +/-6 floor under a stated three-way decision rule.
- P2 [open] falsifier: CI upper bound below +7, i.e. one sampled placement per object class already carries the usable content.
  reason: ALFWorld placements are stereotyped enough that a single draw often recovers the modal receptacle, so both outcomes are reachable; the 150-vs-300 token gap is a confound the proposal acknowledges but does not remove.
- P3 [near_entailed] falsifier: CI upper bound below +10, i.e. the reader treats the table as a search scaffold and ignores its rows.
  reason: cheatsheet - shuffled = (cheatsheet - k0) + (k0 - shuffled), so once P1 confirms at M1 the only way P3 fails is a deranged table beating no table at all, and a table that actively sends the agent to wrong receptacles is unlikely to clear k0 - a scaffold effect the proposal names but does not size in advance.
  fix: Score P3 on shuffled_all - k0 as an equivalence-to-k0 test, or set P3's margin at M1 plus the measured shuffled - k0 gap, so it can come out against 'content, not scaffold' independently of P1.
- P4 [open] falsifier: CI upper bound below +7, i.e. a no-experience static table recovers the search-bound gain.
  reason: Reachable and by the authors' own account plausible, with a pre-registered reading that distinguishes redundancy from the reader ignoring content.
- P5 [open] falsifier: Residual CI upper bound at or above R_S, or point residual above R_S/2.
  reason: The estimand equals R_S minus the cheatsheet's increment over static3, so the real test is whether that increment is additive rather than redundant with type-conditioned exemplars - reachable either way - though R_S serves both as the threshold and as a component of the estimand, so the two move together.
- P6 [open] falsifier: CI upper bound below +7, i.e. the long-context reader extracts the placement statistic from the raw items itself.
  reason: Reachable in both directions, but the 80-item pool is selected to cover each object class only about twice, so cheatsheet_80 sits near the shallow end of the depth ladder and confirming P2 (depth, not coverage, carries the value) predicts this table adds little.
- P7 [near_entailed] falsifier: The 95% CI of the paired reduction is not entirely above 0.5.
  reason: The scoring rule puts failed episodes at their ceiling, so P1's predicted ~10-point success gain mechanically produces roughly the whole 0.5-0.6 reduction, and a null would require a large success gain to arrive with no change in search breadth whatsoever.
  fix: Make the both-arms-take restricted version primary, or report the reduction within the succeeded-in-both stratum, so the process claim is not a re-expression of P1's success gain.
- P8 [unresolvable] falsifier: A fresh-versus-stored difference beyond the +/-12 floor stops the run before any confirmatory arm.
  reason: The acceptance band is set equal to the stated 268-cell floor, so a same-arm replication passes for any true drift up to 12 points, and every branch of the k3 - k0 outcome (at least +7, 0 to +7, CI covering 0) ends in 'proceed', so no result can count against the design.
  fix: Test drift as a paired equivalence on the same (game, seed) cells with a band derived from that paired re-run noise (about +/-6), and state which k3 - k0 outcome stops the run rather than only rescaling M1.
- shared terms: P1-P3-P4: cheatsheet_all is the shared minuend (self-declared); with shuffled_all at or below k0, P1 algebraically implies P3 at the same margin M1.; P1-P7: scored on the same episodes, and the ceiling scoring of no-take episodes converts P1's success gain directly into P7's receptacle-count reduction.; P5-P8: R_S = k3 - static3 is both P5's threshold and a component of its estimand, and P8's fresh k3/k0 cells are what fix M1 and R_S.; P2-P6: cheatsheet_80 is compiled from a pool holding only about two trajectories per object class, so P2's depth claim and P6's redundancy claim are statements about the same aggregation-depth axis measured in different cells.
