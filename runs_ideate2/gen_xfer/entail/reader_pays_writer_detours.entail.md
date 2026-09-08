=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: reader_pays_writer_detours — headline P1 is **unresolvable**; open 1 / entailed 0 / near-entailed 0 / unresolvable 4; verdict revise

- P1 [unresolvable] falsifier: The slope's 95% CI upper bound is at most 0.1 in both pairs.
  reason: A cell is 274 games x 2 seeds = 548 episodes, so about 500 paired successful episodes would require over 90% joint success in both arms, which no stated number supports; at the attainable count the slope SE is far too large for a CI upper bound of 0.1, so even a true zero slope cannot reach the falsifier, and conditioning on success drops exactly the cap-hitting detour-copying episodes that carry the effect.
  fix: Run the manipulation pairs at enough seeds or games to actually deliver about 500 paired successful episodes, or estimate the slope over all episodes with step-cap censoring modeled, and state the achieved SE rather than a pilot assumption.
- P2 [unresolvable] falsifier: Pruned at least 6 net below raw with CI excluding 0.
  reason: The 6-net neutrality margin is set below the proposal's own stated +/-8 cell noise floor, so the falsifier lies inside the stated noise and within-6-net is confirmed by insensitivity rather than by evidence.
  fix: State the paired (not cell) success MDE and add seeds or games until it is below 6 net, or raise the neutrality margin to the resolvable floor.
- P3 [unresolvable] falsifier: Padded at least 6 net below expert.
  reason: Same 6-net threshold under the stated +/-8 floor, and the padding is replay-verified benign and token-matched, so item content is preserved by construction and only a distraction effect smaller than the cell noise could produce the falsifier.
  fix: Set the neutrality margin at or above the resolvable paired MDE (more seeds), and add a deliberately non-benign padding arm (replay-failing detours) as the sensitivity control showing the cell can detect content damage at all.
- P4 [open] falsifier: self-raw's gain per consumer token is at least the expert's, or the success gap is at least 8 net.
  reason: The second falsifier disjunct is a plain 8-net success comparison at the stated cell floor and is genuinely reachable, although the 25% confirm threshold carries no CI for a ratio whose numerator inherits the +/-8 net noise (about 30% of the +27 reference effect).
- P5 [unresolvable] falsifier: Slope CI upper bound at most 0.1 for the foreign reader while at least 0.3 for the self reader.
  reason: It inherits P1's paired-successful-episode shortfall on a cell with no more episodes and adds a conjunction on the self-reader slope, so if P1 is itself unresolved, or both slopes are null, the falsifier can never be triggered.
  fix: Power the EXAONE manipulation pair to the same paired-success count as the self reader and restate the falsifier as a stated difference between the two slopes with its own CI, instead of a conjunction of two one-sided bounds.
- shared terms: P1-P5: P5 is the same length-inheritance slope on a second reader and its falsifier is defined relative to P1's slope, so P1's estimate decides whether P5 can resolve at all.; P1-P4: reader steps in P1's slope and consumer tokens in P4's denominator are the same measured episode length (tokens are generated per step), so a positive P1 mechanically produces P4's token gap.; P2-P4: P4's 'success gaps within 8 net' clause and the neutrality tests share the same self-raw and expert net-gain terms, so the pruning and padding cells fix the numerator of the cost ratio.
