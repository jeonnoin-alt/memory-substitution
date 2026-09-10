=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: hole_backfill_static_counterfactual — headline P3 is **open**; open 4 / entailed 0 / near-entailed 1 / unresolvable 0; verdict pass

- P1 [open] falsifier: g_1 = s(B1) - s(H1) <= 0 with the 95% CI excluding +8, i.e. the next-ranked item adds nothing to [2,3].
  reason: The backfill item enters at the bottom of a two-item prompt and the proposal's own nested-k prior puts its marginal value at +2 to +4, so a null gap is a fully reachable measurement and an observed 0 has CI [-5,+5] that excludes +8.
- P2 [open] falsifier: c_H(w1) = s(F_w1) - s(H1) >= 0 with the CI excluding -10, i.e. the correct co-items dominate and the wrong item is ignored.
  reason: An ignored or neutral w gives c_H(w1) near 0 with CI +/-5.7 that excludes -10, so the falsifier is reachable; the accompanying class-invariance claim is definitional rather than tested, since deleting w and backfilling reproduces exactly the B1 prompt [2,3,4].
- P3 [open] falsifier: D_H = s(F) + s(B12) - s(H1) - s(H2) <= 0 with the CI excluding +12, i.e. pruning two items costs at least the sum of their hole credits.
  reason: D_H = c_H(1) + [s(B12) - s(H2)], and with item 1 gated at >= +10 net the set [3,4,5] can easily fall 10 or more net below [1,3], so a non-positive D_H is reachable; an observed 0 has CI [-7,+7] excluding +12, though the 0-to-12 indeterminate zone is 1.7 half-widths wide.
- P4 [open] falsifier: c_S(1) = s(F) - s(S1) <= 0 with the CI excluding +8, i.e. the static exemplar substitutes fully once the co-items carry the procedure.
  reason: Falsification is reachable only as s(S1) >= s(F), i.e. sigma_1 = c_H(1) - c_S(1) >= 10 under the gate, which is a genuine possible measurement but means confirmation needs only sigma_1 <= 2 while falsification needs the static exemplar to close the entire gated hole.
- P5 [near_entailed] falsifier: g_1' = s(B1') - s(H1') <= -2 with the CI excluding +8.
  reason: The outcome the proposal itself calls falsifying, that the second reader gets nothing from the next-ranked item (g_1' about 0), does not meet the stated numeric falsifier, which demands the backfill actively hurt by 2 or more net through a harm mechanism the proposal never names or controls, leaving the whole band (-2,+8) undecided.
  fix: Set the falsifier at g_1' <= 0, or add a pre-registered TOST on g_1 - g_1' against +/-3, so a zero gap on the second backbone decides the prediction.
- shared terms: P1-P3: both rest on the same H1 arm; D_H = c_H(1) + s(B12) - s(H2), so the arm that sets g_1 also fixes half of the headline estimand and a low s(H1) inflates both.; P2-P1: c_B(w1) = c_H(w1) - g_1 is an algebraic identity (removing w and backfilling gives B1's [2,3,4] prompt), so P2 plus P1 determine the planted item's backfill credit with no further measurement, and the asserted class-invariance of the hole-backfill gap is definitional, not tested.; P4-P1 and the gate: sigma_1 = c_H(1) - c_S(1) and g_1 - sigma_1 are functions of arms already used by P1 and the c_H(1) gate, so the reported ordering s(H1) < s(S1) < s(B1) is fully determined once c_H(1), c_S(1) and g_1 are measured.; P3-P4: both share the F arm with c_H(1), so a high s(F) inflates D_H and c_S(1) together.
