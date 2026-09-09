=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: aggregate_or_comply — headline P2 is **open**; open 6 / entailed 0 / near-entailed 2 / unresolvable 1; verdict pass

- P1 [open] falsifier: R1_p1 loses <12 points vs R1_p0, i.e. the agent does not follow the replay-verified wrong procedure and the poison is reported inert.
  reason: Nothing in the construction forces compliance (the k=0 reference shows the agent can succeed without exemplars), and an inert-poison outcome near 0 sits about 1.7 floors from the 20-point margin with the ambiguous [12,20) band pre-declared inconclusive.
- P2 [open] falsifier: Loss <12, i.e. the reader outvotes one wrong item in three (the 2202.12837 prior).
  reason: Outvoting is a live, named prior and poisoned items are equally retrievable (goal sentences unchanged), so both signs are reachable, though the 12-point margin is only ~1.4 floors and a true loss near 12 falls in noise with no inconclusive band declared for this prediction.
- P3a [open] falsifier: Point loss >=12 with the CI excluding 0, i.e. the compiler hedges or carries the minority item into the playbook.
  reason: The LLM artifact is explicitly not majority-determined (unlike R3), so a poisoned or hedged one-in-three playbook is reachable and a large loss is detectable; the cost is that with a ~10-point half-width, confirmation requires a point loss under ~2, leaving a wide inconclusive strip.
- P3b [open] falsifier: Loss <12, counted as falsified even when the audit shows the compiler restored the clean procedure from pretraining.
  reason: The obvious escape hatch (compiler prior overrides the sample) is pre-committed as falsifying rather than excused, and a ~0 loss lies two floors from the 20-point margin.
- P4 [unresolvable] falsifier: Loss <12, i.e. the long-context reader aggregates and the minority wrong items are outvoted.
  reason: The margin (12) equals the stated per-cell floor and the estimand is a difference of two such cells, so its propagated floor exceeds the margin and the confirming and falsifying outcomes cannot be told apart at the stated power.
  fix: Run R4_p0 and R4_p1/3 at 4 seeds (or score on the full 274-game cell, floor +-8) so the paired-difference floor falls below 12, or raise the margin to 20 as in P1.
- P5 [open] falsifier: R6a - R6b >= 12, i.e. clean exemplars override a wrong instruction more than a clean instruction overrides wrong exemplars.
  reason: Both cells are unfloored by construction (wrong+wrong is the only floored cell and is not run) and the asymmetry can go either way, but the falsifier sits exactly at the stated difference floor and every outcome below +12, including an exact null, is scored as confirmation.
- P6a [open] falsifier: Pooled loss <12, i.e. a single fixed wrong exemplar is outvoted by the two clean ones.
  reason: Outvoting one of three fixed exemplars is a reachable outcome and the pooled difference floor (~10) leaves the 12-point margin marginally resolvable.
- P6b [near_entailed] falsifier: Point difference >=12 with the CI excluding 0, read as a retrieved wrong item being treated differently from a fixed one.
  reason: The two arms already differ on clean banks by the program's own retrieval-minus-static residual (about +17 net in Measurement C, and this proposal's Short Hypothesis concedes retrieval wins on accuracy), so a >=12 raw-level gap is delivered by that uncontrolled baseline route difference rather than by any differential treatment of the wrong item, and the equivalence the prediction claims is the outcome that is excluded.
  fix: State P6b as a difference-in-differences, (R5_j1 - R5_j0) versus (R1_p1/3 - R1_p0), so the clean-bank route gap cancels and only the poison response is compared.
- P7 [near_entailed] falsifier: |fitted p=0 to p=1 change| >= 8 with the 95% bootstrap CI excluding 0, i.e. spillover from the contaminated procedure types.
  reason: Pick items are never poisoned and R1 selects by goal query while R5/R6 are type-conditioned, so spillover is structurally impossible in roughly half the 37 cells; averaging those forced zeros into one pooled slope halves any real spillover carried by the type-agnostic R2/R3/R4 arms and pushes it under the 8-point falsification bar.
  fix: Pre-register the p slope inside the type-agnostic routes (R2/R3/R4), or a p x route interaction, instead of a single slope pooled over routes whose pick-type context cannot contain poison.
- shared terms: P1-P2: both are losses measured against the same R1_p0 procedure-type cell (2 vs 4 seeds), so a high or low clean retrieval baseline moves both verdicts together.; P2-P6b: R1_p1/3 is a measured term in both estimands, so the compliance loss and the fixed-vs-retrieved equivalence cannot fail independently.; P3a-P3b: both are draw-pooled losses against the same R2_p0 draw-pooled cell.; P6a-P6b: both use the same pooled R5_j1 cell, so a low j=1 mean simultaneously confirms P6a and pushes P6b toward its falsifier.; P7-P1..P6: P7's pooled regression is run on the pick-type halves of the same episodes whose procedure-type halves carry P1-P6, so any run-level artefact enters both the control and the tests.
