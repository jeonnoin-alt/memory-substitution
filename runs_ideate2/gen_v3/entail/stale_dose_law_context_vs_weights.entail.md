=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: stale_dose_law_context_vs_weights — headline P1 is **unresolvable**; open 0 / entailed 3 / near-entailed 1 / unresolvable 2; verdict revise

- P1 [unresolvable] falsifier: f1 = H(d=1)/H(d=3) at or below 0.4, or stale-first minus stale-last below the 8-point position margin (the agent averages over items).
  reason: Gate 0 only guarantees H(d=3) >= 15 net points, so the 0.6-vs-0.4 boundary is a 3-net-point gap on a ratio of two noisy paired differences whose stated MDE between dose levels is about 8 points, and the position margin is set exactly at that MDE, so the falsifying region lies inside the stated noise.
  fix: Raise the Gate 0 harm requirement to about 40 net points (or add games/seeds until the dose-difference MDE is under 3 points) and pre-register the position contrast as its own powered test with an equivalence bound for 'no position effect'.
- P2 [entailed] falsifier: a linear dose curve, or a jump concentrated at p <= 0.25.
  reason: A perfectly linear curve gives exactly H(0.25)/H(1)=0.25, exactly H(0.75)/H(1)=0.75 and exactly 50 percent of the harm inside the 0.25-0.75 interval, so it satisfies all three acceptance thresholds while being the named falsifier; the only remaining falsifier needs a ratio excursion worth a few net points against an 8-point MDE.
  fix: Move the thresholds strictly inside the linear values (e.g. <= 0.10 and >= 0.90 with more than 70 percent of harm in the middle interval), add seeds per student, and pre-register a step-vs-line model comparison so linearity lands in the falsifying region.
- P3 [entailed] falsifier: the in-context curve linearizes at temperature as well.
  reason: The temperature arm omits the d=0 and d=3 in-context cells, so neither H(d) nor the shape statistic f1 is defined at temperature 0.7 and the in-context curve cannot be shown to linearize; the arm that would show the opposite is absent.
  fix: Run d in {0,1,2,3} plus the k=0 reference at temperature 0.7 so f1 and the step statistic are computable on both sides, and pre-register the 'step statistic halves' criterion with a bootstrap CI.
- P4 [entailed] falsifier: none stated - a rescue below 50 percent of the gap is pre-labelled 'a crutch-like prior dominating context' and reported as a result.
  reason: Both branches are declared findings, so no outcome comes out against the hypothesis, and the 10-net-point equivalence bound is itself inside the stated +/-8 paired CI.
  fix: Pre-register one directional criterion with a falsifying region (e.g. rescue >= 70 percent of the gap, otherwise the context-dominance claim fails) and power the cell so a 10-point bound sits outside the CI.
- P5 [unresolvable] falsifier: decoy harm at or above one third of the stale-item harm at d=1 (harm is volume or irrelevance, not conflict).
  reason: With H(d=3) only guaranteed at 15 net points, H(d=1) is about 9 and the one-third threshold is about 3 net points, several times smaller than the stated ~8-point MDE for a difference between two cells.
  fix: Power the decoy contrast separately (more games/seeds, or a strengthened shift) so that one third of the measured H(d=1) exceeds the paired MDE, and report the decoy CI rather than a point ratio.
- P6 [near_entailed] falsifier: the bank recovers as fast as the LoRA, or the observed recovery curves fall outside the predicted band.
  reason: The 2x ordering is forced by the update rules - an append-only bank cannot forget the 300 rule-A items and can only dilute them, while a no-replay chunk LoRA trains on an all-fresh chunk from its first post-shift update - so falsification is reachable only through the uncontrolled route of the fitted laws mispredicting, on a band bootstrapped from 2 stream seeds.
  fix: Add arms that break the forced ordering (a bounded/FIFO or failure-decayed bank, and a replay LoRA matched on retained items) and pre-register the band width plus the number of stream seeds required to declare a miss.
- shared terms: P1-P5: both are computed from the same measured H(d=1) and the same d=0 anchor, so the decoy ratio moves with f1's numerator.; P2-P3: the step statistic in P3 is computed from the same H(p) points whose ratios define P2, so the greedy fit fixes the baseline of the temperature contrast.; P2-P4: both rest on the p=0 and p=1 student accuracies - P4's 'gap' is H(p=1), the denominator of P2's ratios.; P1-P6 and P2-P6: P6's predicted band is a deterministic function of the laws fitted in P1 and P2 plus the stale-share arithmetic, so it contributes no independent measured term.
