=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: style_outruns_content — headline P1 is **near_entailed**; open 1 / entailed 2 / near-entailed 3 / unresolvable 1; verdict revise

- P1 [near_entailed] falsifier: Either marker type-confined (gamma_marker <= 0.4), or content reaching the held-out type (gamma_content >= 0.5).
  reason: The content half re-describes the pool filter (pick_two is removed from B and T, so its content gain can only be nonzero through compositional transfer no arm supplies), and a fixed phrase prefixed to every thought of every marked item is the low-complexity unconditional habit for a LoRA to learn, so type-confinement requires a type-conditioning pressure the design never applies.
  fix: Plant the marker on only part of the marked-type items, or use a different phrase per type so type-conditioning is learnable, and keep a held-out-type slice in T as a positive control that lets gamma_content exceed 0.5.
- P2 [open] falsifier: S_opsd marker adoption within margin of the k=0 baseline while it still shows a content gain.
  reason: Both outcomes are mechanically reachable (on-policy reverse-KL can transmit or filter a surface habit) and the 20-plus point gap between 0.5 x teacher adoption and the k=0 baseline is far outside the +-3 pp marker CI.
  fix: Pre-register the content-gain threshold that makes the conjunctive falsifier binding, so an S_opsd arm that simply fails to learn cannot dodge it.
- P3 [entailed] falsifier: S_sanit adoption >= 0.3 x S_sft adoption.
  reason: The sanitizer deletes exactly the tokens the outcome is scored on, and an arbitrary fixed five-token string has a near-zero natural rate, so the trajectory-dynamics channel has no way to express itself in this metric whatever its true strength.
  fix: Score a channel the sanitizer does not delete (paraphrase-level or semantic adoption, thought-length or entropy signature, or a marker with a measurable natural base rate) so the 2604.15559 account has a reachable positive outcome.
- P4 [near_entailed] falsifier: Either marker outlives the content, or both decay together.
  reason: The continuation set is direct negative evidence against both markers (clean thoughts, no leading look) but carries no evidence at all about marked-type procedures, so faster marker decay follows from the update rule rather than from any style/content distinction, and 0.25 epoch is also the shortest half-life the checkpoint schedule can resolve.
  fix: Add a continuation arm containing clean marked-type items so both channels face the same contradiction (or a neutral continuation that contradicts neither), and add checkpoints below 0.25 epoch.
- P5 [unresolvable] falsifier: r=32 exceeds both r=8 and r=128 by more than the margin (an inverted-U).
  reason: The quoted +-3 pp is evaluation noise only and each rank arm has a single LoRA seed, so an apparent inverted-U cannot be separated from training-seed variation, which the design bounds nowhere for these arms.
  fix: Run at least three LoRA seeds per rank and pre-register the inverted-U margin in adoption points relative to the measured seed spread.
- P6 [entailed] falsifier: In-context marker adoption on unmarked types departs from the k=0 baseline with no marked item retrieved.
  reason: For an untrained model the prompt is the only route by which a planted phrase or leading look can appear, so conditioning on no cross-retrieval leaves nothing but sampling noise, and the proposal itself declines to count the result as a confirmation.
  fix: Test induction rather than presence, e.g. in-context items marked on a different task type, so cross-type marker generalization has a route into the metric.
- P7 [near_entailed] falsifier: Mismatched context suppresses adoption to the k=0 baseline.
  reason: The mismatched condition is only token-matched other-type items and is never required to be marker-free or marker-contradicting, so items drawn from the marked bank carry M1/M2 and reinforce the habit, leaving suppression reachable only through an interference mechanism the design does not construct.
  fix: Draw the mismatched items from an explicitly marker-free or counter-marked bank (different fixed phrase, no leading look) and report the injected items' marker rate in every prompt condition.
- shared terms: P1-P2: gamma_marker for S_sft and for S_opsd share A_M on marked types as the denominator, so low marked-type adoption inflates both generalization ratios.; P1-P3: S_sanit adoption is normalized by S_sft adoption, the same quantity that is P1's denominator, so confirming P1 raises the bar P3 must clear.; P3-P4: both are scored on emission of the same fixed phrase, so the sanitizer's deletion and the clean continuation's suppression act on the same measured term.; P1-P6: gamma_marker's numerator is marker adoption on unmarked types, the same quantity P6 predicts equals the k=0 baseline in context, and both subtract the same baseline rate.
