=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: recall_success_dissociation — headline P4 is **open**; open 10 / entailed 0 / near-entailed 1 / unresolvable 0; verdict pass

- P1a [open] falsifier: Random-type within +/-8 of the comparator.
  reason: A k=3 uniform draw contains at least one same-type item on about 42 percent of cells, so the arm is not pinned to blind1's measured -15.4 and could in principle reach the comparator, though the outcome is close to settled in advance by Measurement C.
  fix: none required
- P1b [open] falsifier: The residual is +8 or less.
  reason: A fresh-seed, single-split replication can fall short of +8, although E0 deliberately supplements the bank so every valid_seen game has same-type same-scene successes, which loads the retrieval arm in the direction that makes this control pass.
  fix: none required
- P1c [open] falsifier: BM25 at least +8 over static3-bank.
  reason: The static arm shows three fixed items per type while BM25 selects per episode over the whole bank, so a per-episode selection advantage can survive the source swap; the only leakage is that type medoids are high-centrality items BM25 sometimes returns, which shrinks but does not close the contrast.
  fix: none required
- P1d [open] falsifier: same-type-random at least 8 below BM25.
  reason: Object-class and scene matching above type is a live channel that BM25 exploits and the within-type random arm does not, so the falsifier is reachable on the stated arms.
  fix: none required
- P2 [open] falsifier: Either difference at or above +8.
  reason: Placing the game's own successful trajectory at rank 1 is a strong intervention with ample headroom (static3 +12.4 and k3 +17.2 over k0 leave no ceiling), and c=1 also raises type recall relative to c=0's other-scene BM25 fills, a confound that pushes toward the falsifier rather than away from it; the only caveat is that the +/-8 floor was calibrated at about 548-560 cells while the oracle-game clause runs on roughly 320.
  fix: pre-register the floor for the |G| x 4 cell count of the oracle-game clause instead of importing the 560-cell +/-8.
- P3a [open] falsifier: The difference is below +8 (outcomes in [8, 16) fall in a declared dead band and confirm nothing).
  reason: A same-product trajectory placed at rank 1 can fail to transfer the attribute-to-product binding through a ReAct rollout, so the falsifier is reachable and lies about two floor units below the predicted +16.
  fix: none required
- P3b [near_entailed] falsifier: The BM25 effect is at least 8 net above or below b_ws times the P3a effect.
  reason: Both sides are built from the same S cells and the same treatment (a same-product trajectory in the top-3), so the natural arm's gain is by construction the coverage-weighted average of the per-cell duplicate effect and equality with b_ws times E is an accounting identity up to effect heterogeneity and retrieval rank, neither of which the design manipulates; worse, at b_ws around 0.3-0.5 the predicted value is only about 5-10 net, smaller than the +/-8 tolerance itself, so almost any observed BM25 gain confirms.
  fix: add a rank-matched oracle arm (the same-product item planted at the rank BM25 naturally gives it), estimate b_ws and the P3a effect on disjoint seed sets so the two sides do not share measured terms, and state the tolerance as a fraction of b_ws times E rather than a fixed +/-8.
- P3c [open] falsifier: Any c=0 retriever at or above +8 over the comparator.
  reason: Transfer of category search strategy without duplicates is a real channel, and the 'any retriever' quantifier over several arms plus the regression of a max-selected comparator on fresh evaluation cells both make the falsifier easier rather than harder to reach.
  fix: none required
- P3d [open] falsifier: The difference is below +8.
  reason: Reachable on the stated arms, but |X| carries no pre-registered minimum or fallback (unlike |S|'s 150-250 with two named fallbacks), so the floor for this contrast, and hence whether a value between +8 and +16 resolves anything, is not fixed before the run.
  fix: pre-register a minimum |X| with its own floor at that cell count and a stated fallback if X falls short.
- P4 [open] falsifier: ALFWorld slope at or above +16 with 95% CI excluding +8; WebShop slope below +8; or both slopes landing in the same band (both at or above +16, or both within +/-8), which falsifies the dissociation itself.
  reason: Both environment clauses can come out against the hypothesis on the stated arms, but on an equally spaced three-level coverage grid the OLS slope reduces to the c=1 minus c=0 endpoint difference (the c=0.5 cell has zero leverage), so P4 is largely an algebraic restatement of P2 on ALFWorld and of P3a on WebShop perturbed only by the natural BM25 point, and its thresholds sit exactly at the stated MDE, giving about 80 percent power at the boundary.
  fix: give the middle coverage level leverage (add an unequally spaced rung such as c=0.25 or 0.75) so the slope is not the endpoint difference, and report P4's power separately from P2 and P3a since they share the same cells.
- P5 [open] falsifier: The gain fails to clear the estimated WebShop floor.
  reason: WebShop retrieval can genuinely fail to clear a roughly +/-6 to +/-8 floor, and the proposal pre-registers exactly which claims are withdrawn and which comparator-free ones survive, so either outcome is informative.
  fix: none required
- shared terms: P2-P4 (ALFWorld): with equally spaced coverage levels the fitted slope equals the oracle-scene c=1 minus c=0 difference that P2 scores, so P2 determines P4's ALFWorld clause up to the natural BM25 point.; P3a-P4 (WebShop): the same identity holds on S, so P3a's c=1 minus c=0 effect is the WebShop slope's endpoint difference and one determines the other.; P3a-P3b: P3b's target value is b_ws times P3a's own effect, and both contrasts are built on the same c=0 arm and the same S cells.; P1b-P1c-P1d: all three are scored against the single ALFWorld BM25 k=3 cell, so its noise moves them together (a high BM25 draw pushes P1b away from its falsifier while pushing P1c and P1d toward theirs).; P3c-P5: both rest on the natural BM25 arm on T, so the gate outcome and the c=0 residual claim share a cell.; P1a-P3c: both are residuals over the out-of-sample-selected comparator, so comparator selection noise moves the ALFWorld and WebShop residual claims together.
