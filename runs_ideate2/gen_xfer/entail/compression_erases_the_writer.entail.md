=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: compression_erases_the_writer — headline P3 is **open**; open 1 / entailed 1 / near-entailed 0 / unresolvable 4; verdict revise

- P1 [unresolvable] falsifier: The 95% CI of D(self) lies entirely below +4 in either self cell (the writer's own procedures are at least as good as its raw trajectories).
  reason: The +4 margin sits inside the design's own noise (two-cell contrast half-width ~+-6, and the pre-registered seed escalation only triggers above +-6), so the natural anti-hypothesis outcome D(self)~0 gives a CI straddling +4 and falsifies nothing.
  fix: Restate the falsifier as 'CI excludes +4 from below' so a null falsifies, and pre-register 4+ seeds on both self L0/L2 cells until the contrast half-width is <= 2.
- P2 [unresolvable] falsifier: CI of D(foreign) entirely above -4 in BOTH foreign cells (raw foreign at least as good as compressed foreign).
  reason: -4 is inside the ~+-6 contrast noise and the falsifier is conjunctive over both foreign cells, so a flat D(foreign)~0, or one cell in which raw foreign wins, refutes nothing.
  fix: Make falsification per-cell with a CI that must exclude 0 in the predicted direction, and extend the seed escalation to the L1 cells so every contrast has half-width <= 2.
- P3 [open] falsifier: The 95% CI of I(r) includes 0, or I(r) is negative, for either reader.
  reason: Nothing in the design fixes the sign of D(self)-D(foreign): both readers, both self pools and both foreign pools are actually run, so a null or reversed interaction is a directly measurable outcome and the 'CI includes 0' falsifier is easy to reach at the stated power.
- P4 [unresolvable] falsifier: Reader-compressed exceeds writer-compressed by >= 4 net with CI excluding 0.
  reason: This is an equivalence claim with a 4-point bound tested against a ~+-6 contrast half-width, so any failure to detect confirms it, and the falsifier is one-sided: a reader-compressed version 4+ points WORSE also contradicts 'changes by less than 4' without falsifying.
  fix: Two-sided TOST at +-4 with seeds giving a contrast half-width <= 2, and count a large negative difference as falsifying too.
- P5 [unresolvable] falsifier: X-written or Q-written procedures beat the static prompt by >= 4 net with CI excluding 0.
  reason: Another 4-point bound against ~+-6 noise, stated as a universal null over several L2 cells, so non-detection confirms it and only an implausibly large single-cell effect could falsify.
  fix: Recast as an equivalence test with a pre-registered bound and power (half-width <= 2), or pre-register that any single L2 cell whose CI lies above 0 falsifies.
- P6 [entailed] falsifier: ratio(L2) <= ratio(L0) for some foreign writer x reader pair.
  reason: If P1 holds (g_self(L0) > g_self(L2)) and P2 holds (g_for(L2) > g_for(L0)), then ratio(L2)=g_for(L2)/g_self(L2) exceeds ratio(L0) by arithmetic on shared measured terms, so the falsifier is just the negation of P1/P2 and P6 tests nothing new.
  fix: Replace with an estimand not built from the same four means (e.g. absolute foreign gain against an independent expert or third-writer denominator) reported with its own bootstrap CI and a margin larger than that CI.
- shared terms: P1-P3: D(self) is one term of I(r)=D(self)-D(foreign); the same self-L0 and self-L2 means determine both.; P2-P3: D(foreign) is the other term of I(r), so P3 is fixed once P1 and P2 are measured on the same four cells.; P1-P2-P6: ratio(L)=g_foreign(L)/g_self(L) is a ratio of those same four cell means, so P6 is an arithmetic consequence of P1 and P2.; P4-P5: both are scored on the foreign L2 gain net of the static prompt, so a single cell mean moves both.
