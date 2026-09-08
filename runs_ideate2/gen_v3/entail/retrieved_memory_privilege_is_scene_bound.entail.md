=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: retrieved_memory_privilege_is_scene_bound — headline P1 is **entailed**; open 0 / entailed 3 / near-entailed 0 / unresolvable 4; verdict revise

- P1 [entailed] falsifier: R = S_match - S_proc > 0.25 G0 (about +8 net) on valid_unseen.
  reason: The audit strips scene/object/receptacle overlap between every training target and its retrieved MATCH exemplar, and valid_unseen shares no scenes with B either, so the item-specific binding channel that is the only route to a large R is deleted before any student is trained.
  fix: Add a MATCH+ arm whose retrieved exemplars deliberately share (scene, object, receptacle) with the target task, so binding transfer has a route to appear in R.
- P2 [unresolvable] falsifier: R_seen - R_unseen < 0.15 G0 (about 4.8 net), i.e. equal within margin.
  reason: A difference of two arm differences across two unpaired splits carries roughly +-13 net at the stated cell sizes, so the 4.8-net threshold sits deep inside the noise, and R is already pushed toward zero by the P1 audit.
  fix: Make the seen-vs-unseen difference-in-differences the primary contrast and power it to an MDE below 0.15 G0 (far more games/seeds, or a within-split matched-scene manipulation that is paired).
- P3 [unresolvable] falsifier: U flat across types, or largest on the procedure-bound (high s_type) types.
  reason: With about five ranked types and per-type cells of 40-60 games the per-type CI on U swamps the between-type spread, a permutation over five items floors at p~0.008 only for a perfect ordering, and U and 1-s_type share the per-type teacher MATCH term so any correlation is partly mechanical.
  fix: Increase the number of ranked units (sub-type strata or a second environment), pre-register an MDE for the rank statistic, and define U so it does not share MATCH with s_type.
- P4 [unresolvable] falsifier: Retained fraction uniform across types.
  reason: Retained fraction and s_type share the denominator MATCH-EMPTY, so a type with a small in-context gain inflates both, and the per-type ratio of two small noisy quantities has CIs far wider than the gap between the 0.6 threshold and uniformity, with no guarantee that any type populates the >=0.7 or <=0.3 bins.
  fix: Require both bins to be populated with Gate-0 CIs excluding 0.7/0.3, report the retained fraction only for types whose MATCH-EMPTY CI excludes zero, and state the MDE for a between-type difference in retained fraction.
- P5 [entailed] falsifier: None stated: a significantly negative F is absorbed by recomputing every later margin after subtracting it, and no outcome for O is named as refuting.
  reason: Both branches of the F clause are accommodated by design (F near zero confirms it, F negative becomes a nuisance correction), so no result of the long-prefix test can come out against the hypothesis.
  fix: State a refuting magnitude for F (e.g. |F| >= 0.25 G0 breaks the decomposition), fix the subtraction rule before unblinding, and name O <= 0 as a falsifier of the self-training term.
- P6 [entailed] falsifier: Some student beats base on the held-out type, or gains more from matched memory there than base does.
  reason: Removing the type from both B and T means no arm was trained on it and the retriever has no same-type item to deliver, so the prediction re-describes the pool filter rather than testing type-boundness, and the near-floor 36-game cell could not support the equivalence claim in any case.
  fix: Keep a held-out-type slice in B as retrievable-only (never trained) so matched memory is deliverable, add one arm trained on that type as a positive control, and power the held-out cell.
- P7 [unresolvable] falsifier: The reference-attributable part R becomes the majority on the self-rollout pool.
  reason: Majority has no defined denominator, and a smaller G0 shrinks every fraction-of-G0 margin below the fixed +-6.5 net measurement floor, so neither the pattern nor its falsifier can be resolved on that pool.
  fix: Define majority explicitly (e.g. R > 0.5(R+C+F)) with a stated MDE, and impose a Gate-0 floor on the self-rollout G0 (e.g. >= 20 net) below which the replication is declared untestable.
- shared terms: P1-P5: R + C + F = S_match - S_empty identically, so fixing C >= 0.5 G0 and F within margin of zero determines R once the retained gain is measured.; P1-P2: P2 is the same R contrast re-split by scene familiarity, so the audit that drives R toward zero in P1 also bounds P2's difference.; P3-P4: U = teacher_MATCH - S_match and s_type = (PROC-EMPTY)/(MATCH-EMPTY) share the per-type teacher MATCH score, and P4's retained fraction shares the denominator MATCH-EMPTY with s_type.; P1-P4: retained fraction = (S_match - base)/(MATCH - EMPTY) and R both contain S_match, so a low-retention student simultaneously shrinks R and the retained fraction.
