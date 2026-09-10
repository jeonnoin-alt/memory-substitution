=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: relocated_bindings_demand — headline P3 is **open**; open 4 / entailed 0 / near-entailed 0 / unresolvable 4; verdict pass

- P1 [unresolvable] falsifier: The k=0 success drop at relocated x 25 is < 8 net (and still < 8 after escalation, at which point the demand lever is reported inert).
  reason: The decision threshold is exactly the stated +-8-net minimum reportable margin, so an observed near-zero drop still has a CI covering 8 and cannot exclude the prediction; escalation strengthens the lever but does not shrink the CI, and prerequisite-free relocation can also be defeated by incidental search, so the boundary case is likely rather than rare.
  fix: State the positive control at +14 net like the confirmatory cells (or add seeds/games) so a null reading's CI excludes the predicted drop.
- P2 [open] falsifier: A scene-query minus type-agnostic-static residual >= +8 net in either the canonical x 25 or the relocated x 50 cell.
  reason: Both cells exist, the fresh sibling still carries the new location at 50 steps and retrieved trajectories can help at canonical x 25 through non-binding content, so a residual is reachable and a >= +8 residual is at the stated reportable margin; the loose-budget half is nonetheless partly confirmed by reduced headroom at 50 steps rather than by demand-gating alone.
- P3 [open] falsifier: Residual < +8 net in that cell, i.e. the reader cannot apply a location carried by a retrieved trajectory even when it is required (application failure, G7).
  reason: Confirmation is close to built in because the retrieved sibling literally contains the answer, but the falsifying outcome is a named, reachable reader failure and a near-null reading's +-8 CI excludes the predicted +14.
- P4 [open] falsifier: Residual >= +8 net with a scene-disjoint bank, i.e. the gain comes from non-binding content such as a search heuristic.
  reason: Relocated expert trajectories from other scenes demonstrate off-canonical search that the six-procedure static prompt does not contain, so a non-binding gain is reachable and would be at the reportable margin.
- P5 [unresolvable] falsifier: Scene-query minus goal-query < +8 net in the relocated cell (goal similarity already keys the sibling), or >= +8 in the canonical cell.
  reason: The confirmatory margin is stated at +8, equal to the proposal's own minimum reportable margin, so a zero difference cannot be told from the predicted +8 in the relocated cell and the canonical half is confirmed by noise; unlike P1 there is no escalation to enlarge the effect.
  fix: Raise the scene-minus-goal margin to +14 (the proposal's declared confirmatory margin) or add seeds/games so the paired-difference floor drops below 8.
- P6 [open] falsifier: Table < retrieval - 8 net in that cell, i.e. the reader uses a 430-token trajectory but not a 3k-token table.
  reason: A 274-row table can plausibly lose to an exemplar by a reportable margin (lost-in-the-middle), so the falsifier is reachable, but the test is auto-confirmed whenever P3's residual is null because both arms then collapse onto the static level.
- P7 [unresolvable] falsifier: Whole-bank >= retrieval - 8 net (the sibling is found among 80 items without a query).
  reason: Falsification requires establishing a difference smaller than the stated +-8 floor, which the cluster-bootstrap CI cannot separate from the predicted -8.
  fix: State it as whole-bank <= retrieval - 14, or power the comparison so an 8-point difference is excludable.
- P8 [unresolvable] falsifier: Retrieval >= static - 8 net in the stale cell (no compliance trap).
  reason: Same structure as P7: the falsifier is 'no reportable harm', a sub-floor difference the stated CI cannot distinguish from the predicted -8.
  fix: Predict retrieval <= static - 14 in the stale cell, or add seeds/games to lower the floor.
- shared terms: P2-P3-P4: one estimand (scene-query minus type-agnostic static) read in three cells, each sharing its cell's static arm, so an unexpectedly strong static prompt moves all three toward their nulls together.; P3-P5: the relocated x 25 x fresh scene-query success is a measured term in both; a null scene-query arm falsifies P3 and simultaneously drives P5's relocated half below +8.; P3-P6: P6 compares the table against the same scene-query term, so P3's failure confirms P6 automatically.; P3-P7: the whole-bank prediction is stated as a difference from the same scene-query term that P3 tests.; P2-P5: the canonical x 25 scene-query arm is a measured term in both predictions.
