# v5.1 judging, Opus 5 round — 2026-09-04 (round 2 of the direction-A loop, for the record; author = Opus agent)

Same prompt/schema/weights (`tools/judge_prompt_v5.1.md`, 82 KB), three independent Opus judges. v5.1 was written by
the Opus author agent from `tools/author_brief_v5.1.md` after reading v5 and its three reviews.

## Aggregate
**5.57 — borderline** (nov 4.7 / sig 5.7 / snd 5.7 / fea 6.7 / cla 6.7). R1 5/6/6/7/6, R2 4/5/6/7/7, R3 5/6/5/6/7.
Trajectory (Opus): v4 5.93 → v4.2 6.40 → v4.3 6.05 → v4.4 5.83 → v5 5.25 → **v5.1 5.57**. Feasibility and clarity
rose (compute re-costed in calls, one endpoint, 15-row grid); soundness rose from 5.3 to 5.7; novelty is pinned at
4–5 by the conceded collisions (EvoAgentBench's shared-trajectory table, ExpeL's prepended insight block) and by the
unrun provenance-crossover search, which all three judges again count as a weakness rather than a neutral.

## What v5.1 settled (no judge re-raised it)
The ratio endpoint A = 1 − Inner(I_own)/Inner(I_oth) is accepted as the instrument; the collision check is called
"a model of the practice" (R1), "unusually strong" (R2), "well above the norm" (R3); Ladder T, the compute arithmetic,
X_dist at all three instructions, I0^demo and the item-level dose-response were not objected to as such.

## New design-blocking finding (3/3) — the denominator is not neutral
Inner(I_oth) is measured at an instruction that was optimized on the *other* type set and is then run on own-type
games. That instruction is not merely lower-level, it is **mis-specified**: it pushes the wrong procedure, B_own
repairs the damage, and the repair is scored as relevance advantage in the denominator — inflating A with zero
content transfer. G3b makes it worse by *requiring* I_oth to be ≥ 3pt worse on own-type games, i.e. the design gates
on the mis-specification that inflates its own denominator. Neither correction reaches this channel: A_h is a scalar
level correction and mis-specification is a shape effect concentrated on the games the on-type bank fixes; Ladder T is
same-type by construction, so it titrates level without ever instantiating wrong-type procedure. **Row 1 already
measures Inner(I0\*)** — the clean denominator exists in the Tier-0 grid and is not used. Fix demanded: pre-register
**A0 = 1 − Inner(I_own)/Inner(I0\*)** as co-primary; add **I_all × {B_own, B_oth}** at Tier 0 as a third,
optimizer-exposed but provenance-neutral denominator; pre-register a denominator-inflation check (Inner(I_oth)
materially above Inner(I0\*) ⇒ A is not interpretable as absorption) and an item-level diagnostic (does B_own at I_oth
mostly recover games I0\* already solves). R2 adds the internal edge: G3 (Inner(I0\*) ≥ 9pt) with G1 (help ≥ 5pt)
essentially requires the off-type bank to *harm* by several points, and a large off term is exactly what Rule M routes
to distractor-robustness — the power requirement and the mechanism rule pull in opposite directions.

## Other findings
1. **Which bar gates publication (R3, R1).** "A − A_h ≥ 0.30" and "A_epi ≥ 0.2" (prediction 4) are different
   requirements and the text never says which is confirmatory. A_epi comes from row 4 (n = 500, one optimizer seed,
   interpolated between two ladder levels): SE(A_epi) ≈ 0.3, so a 90% lower bound ≥ 0.2 needs Â_epi ≈ 0.6, and the MDE
   table stops exactly where A_epi/A_type begin. The treatment-free null floor of A (0.12–0.21, risk 8) overlaps the
   0.2 decision threshold, and the promised remedy — raise n from the reserve — is over-committed (see 3).
2. **Missing arms.** I_all × {B_own, B_oth} (3/3); **B′_own**, the episode-disjoint bank mirroring I′, without which
   "same episodes, two containers" is tested only on the instruction side (R3); {C_own, C_oth} × {B_own, B_oth} to
   separate "GEPA absorbed the bank" from "any prose summary of these episodes absorbs it" (R2); I_type promoted, since
   the pre-registered A_epi ≈ 0 / A_type ≥ 0.4 branch is uninterpretable without it (R2); M_shuf promoted as the
   within-domain distractor control, because X_dist (reformatted QA text) is out-of-domain and trivially ignorable
   while B_oth is topically plausible ALFWorld procedure (R3); R_raw at I_own (R1).
3. **Reserve arithmetic (R1).** The allocation table lists S_screen as its own 150-per-set line while the screening
   text draws it from the reserve; the ≈230-game balanced reserve (T_B binds at 116) is promised to the G3
   re-measurement, null-floor remediation and S_test shortfall at once.
4. **Partition rationale (R2).** look_at_obj_in_light toggles a lamp — a device operation, the stated defining feature
   of T_B — so the "no object state change" story is wrong; keep the retrieval-overlap criterion and drop the story.
5. **Third optimizer seed (R2, R3).** With two seeds the crossed optimizer-run effect is not estimable and the 0.8pt
   variance component is transferred from E1; both propose cutting rows 13 (coupling) and 15 (step control) to fund it.
6. **Prediction 6 (R1).** At n = 800 the "90% CI below 3pt" bound is satisfied by a true 2.5pt gain; use an equivalence
   test against a pre-specified margin. Official valid_seen/valid_unseen should leave Tier 1 because the 5–15pt prior
   was measured there (R2). "Same episodes" should be enforced by episode-set identity, not a 350-rollout cap, while
   Ladder T gets 500–750 (R3).
7. **Novelty/scan.** Obligation (2) still unrun (3/3, counted as a weakness). R1 adds two pre-2026 ALFWorld collisions
   the recency-weighted scan could not catch: **AutoManual (arXiv 2405.16247)** compiles interaction-derived rules into
   one manual that replaces experience lookup, and **AutoGuide (arXiv 2403.08978)** extracts and retrieves state-aware
   guidelines — most of the conceptual content of the compile-once arm (row 11) and prediction 6. Appendix of
   2608.14036 still unopened.
8. **Reflector (3/3).** Refused by constraint (no API key on this node); all three call the refusal self-inflicted.

## Decision — freeze with a minimal v5.2 amendment
This was the for-the-record round; under THRESHOLDS T-A the design now freezes with remaining findings resolved or
descoped and logged. The denominator finding is genuinely new (it could only arise once the ratio endpoint existed),
unanimous, and nearly free to fix (the I0\* cells are already Tier 0; I_all × {B_own, B_oth} is two cells), so the
author agent writes **v5.2 as a minimal amendment** — decision-log rows 82+, text changes limited to the items in
`tools/author_brief_v5.2.md` — and **v5.2 is the frozen proposal text**. v5.2 is not re-judged as part of the loop.
Next artifact: `DESIGN.md` (Stage 3), hashed only after the PI runs the freeze-blocking literature obligation.
