=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: binding_scope_leakage_ladder — headline P6 is **near_entailed**; open 8 / entailed 0 / near-entailed 1 / unresolvable 0; verdict revise

- P0 [open] falsifier: Table - k3 < -8, i.e. the +17.2 is scene-family information a per-class sentence cannot carry.
  reason: A class-level table can genuinely fail to carry scene-family information, the falsifier region is one-sided and unbounded so a real shortfall is detectable well beyond the -8 threshold, and the anchor cells are re-paired on the same games.
- P1 [open] falsifier: The difference is < +8, in which case the ladder is not run and the failure is reported.
  reason: Even with scene-matched relocation information in the retrieved items the reader can fail to exploit it within 25 steps, so an inert gate is reachable, and the [8,14) band is pre-declared inconclusive.
- P2a [open] falsifier: The difference is < +8, i.e. the reader does not carry a class rule out of other-scene trajectories; P2 and P3 are then reported as not testable.
  reason: Cross-scene rule transfer is exactly the thing that can fail, and the proposal pre-commits to disabling the two dependent predictions rather than reinterpreting them.
- P2b [open] falsifier: Sentence < retrieval - 8, i.e. the reader applies a concrete trajectory but not a stated rule.
  reason: A rule-versus-trajectory gap would show up far beyond the floor and the falsifier is one-sided and unbounded, though the non-inferiority bound is set at exactly the +-8 floor so any underpowered null counts as confirmation.
- P3 [open] falsifier: 20-item < full - 8, read as a many-shot per-class requirement.
  reason: A shortfall is reachable, but shrinking the pool to 20 items also degrades the similarity of the top-3 to the query, so the falsifier can be produced by retrieval quality rather than by the per-class item count the prediction names.
- P4 [open] falsifier: Table < retrieval - 8, i.e. the reader cannot look up its scene's row among <=274.
  reason: Look-up failure in a <=274-row prefix is a live outcome and the falsifier is unbounded below, although like P2b the non-inferiority bound sits at the floor so an underpowered null confirms.
- P5 [open] falsifier: Residual < +20, i.e. the reader does not follow its own instance's expert trajectory within 25 steps, or k=3 does not rank it first.
  reason: Both named failure routes are reachable and separately logged, and static3-relocated should be low enough under relocation that no ceiling forces the +28.
- P6 [near_entailed] falsifier: D(0.5) <= residual(1) - 14 (discounting: the reader trusts a duplicate less when half the bank's retrievals are non-duplicates) or N(0.5) >= residual(0) + 14 (spillover).
  reason: The discount branch is unreachable as stated because a duplicate-present game sees its own duplicate at rank 1 in both s=1 and s=0.5 and the split never shows the model the bank's duplicate rate, so the only channel that can move D(0.5) is the changed content of retrieved ranks 2-3, a mechanism the proposal neither names nor controls; only the spillover branch is genuinely open.
  fix: Hold the retrieved context comparable across s (fill ranks 2-3 from the same train items at s=1 and s=0.5, or condition D(s) on the logged per-episode retrieval composition), or restate the discount claim as one about retrieved-neighbour content rather than about the global duplicate rate.
- P7 [open] falsifier: Whole-bank >= retrieval - 8, i.e. the reader finds its own instance among <=80 same-scene trajectories without a query.
  reason: The duplicate is genuinely present in the prefix so the reader can in principle locate it, both outcomes are reachable, and the two thresholds sit at and above the +-8 floor.
- shared terms: P5-P6-P7: all three read the same instance-scope s=1 retrieval cell, so residual(1) simultaneously decides P5, supplies P6's D-branch reference, gates whether P6 is read at all, and sets P7's baseline.; P6 internal: pooled residual(s) = s x D(s) + (1 - s) x N(s) is an algebraic identity of the two measured terms, so the 'linear-in-s law' adds no test beyond the D and N comparisons.; P1-P4: both read the scene-scope s=1 retrieval cell, so a weak gate directly deflates the table's non-inferiority target.; P2a-P2b-P3: all three read the global-scope full-bank retrieval cell, so one anomalous cell moves the positive control, the sentence claim and the 20-item claim together.; P0: 'table - k3 >= -8' and 'recovers at least +9 of the +17.2' are the same measured quantity re-expressed through the fixed Measurement C rows, not two checks.
