=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: stale_item_score_lag_after_rule_change — headline P2 is **open**; open 1 / entailed 0 / near-entailed 3 / unresolvable 1; verdict revise

- P1 [near_entailed] falsifier: The post-drift stale-only cell is within +/-5 of k=0 at both D1 and D2, i.e. the reader recovers from the rewritten admissible-command list.
  reason: The wrapper rejects exactly the action string the stale items encode and D0 explicitly escalates to D2 whenever stale harm is under 10 net, so severity is tuned until the predicted sign appears, and the +/-5 equivalence bound is inside the roughly +/-7 CI on a stale-only-minus-k=0 difference.
  fix: Fix the severity (D1) and pre-register thresholds before D0 runs, reporting D2 as a separate severity result rather than as a second chance at the same test.
- P2 [open] falsifier: The lag ratio's 95% CI lies below 1.5, which happens if one stale item sinks mixed sets as hard as three do.
  reason: Composition is randomly assigned and the compliance-trap outcome that would equalise the two lags is a real, uncontrolled property of the reader, so the stream can return a ratio near 1 even though the scorer's shared set-level credit pushes the other way.
- P3 [near_entailed] falsifier: The outcome-reinforced false-retain rate is 10% or lower at +1,000 games.
  reason: Above the scorer's pruning threshold is never defined, so the 30%/5%/10% split is not a pinned estimand, and score-weighted retrieval freezes a demoted item's score by starving it of further updates, a retention channel the proposal never names or separates from credit contamination.
  fix: Pre-register the pruning threshold (for example the bottom score quartile at each checkpoint) and log per-item retrieval counts so frozen-by-non-retrieval retention is reported separately from contamination-driven retention.
- P4 [near_entailed] falsifier: Post-drift confidence gain drops by 50% or more, i.e. the reader stops following the item after Nothing happens.
  reason: The post-drift D2 trajectories were generated with the stale item in context, so the item is scored on the very actions it induced and its likelihood advantage is largely self-fulfilling; falsification requires a mid-episode recovery large enough to dominate the trajectory average, a magnitude the design neither isolates nor powers.
  fix: Compute confidence gain on trajectories generated without the item in context (post-drift k=0 or stale-removed successful trajectories) and report the pre/post comparison on that held-out trajectory set.
- P5 [unresolvable] falsifier: The single and pairwise removal effects agree within +/-5 net.
  reason: The pairwise cell is a single seed (about +/-6) and the contrast of the two removal effects carries a CI near +/-8 to +/-9, so the +/-5 agreement bound sits inside the noise, and the quantity itself equals the fresh item's own removal effect plus the interaction, so an ordinary main effect can clear the >= 8 threshold without any non-additivity.
  fix: Define the estimand as the interaction (pairwise minus both single removals), run it on all 4 seeds, and state its MDE.
- shared terms: P2-P3: the D3 lag and the D4 false-retain rate are the same outcome-reinforced score path crossing a threshold, so a long mixed lag mechanically produces a high false-retain rate.; P1-P2: the stale-harm term P1 gates on is the same mixed-versus-stale-only success gap that sets the score separation speed and therefore the lag ratio in P2.; P1-P5: both are read off the single-REMOVE stale-item contrast in the D2 cells, so the harm magnitude established for P1 also sets the size of P5's single-versus-pairwise disagreement.
