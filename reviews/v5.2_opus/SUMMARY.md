# v5.2 judging, Opus 5 round — 2026-09-04 (the round the freeze decision skipped, then ran; author = Opus agent)

Same prompt/schema/weights (`tools/judge_prompt_v5.2.md`, 108 KB), three independent Opus judges. **v5.2 had been
declared frozen without judging** on the T-A round-3 clause; the PI challenged that, the round was run, and it did not
pass. Judging costs no API credits here, so the earlier decision was wrong on its own terms.

## Aggregate
**5.12 — reject** (worst-verdict-wins; nov 4.0 / sig 5.3 / snd 5.7 / fea 5.7 / cla 6.0). R1 4/5/6/5/6 borderline,
R2 5/6/6/6/7 borderline, R3 3/5/5/6/5 **reject**.
Trajectory (Opus): v4 5.93 → v4.2 6.40 → v4.3 6.05 → v4.4 5.83 → v5 5.25 → v5.1 5.57 → **v5.2 5.12**.
Novelty is now the binding ceiling (4.0): the conceded collisions cap it and no further design round moves it.

## Design-blocking findings
1. **The confirmatory endpoint does not test the title (3/3).** Inner(I) = acc(I×B_own) − acc(I×B_oth) is the bank's
   task-type *discriminability*, not its value. A ≥ 0.5 is fully compatible with the bank still adding 4–6pt over no
   memory at I_own, in which case the answer to "is your agent's memory just an un-optimized prompt" is **no** while the
   pre-registered bar reads *pass*. The quantity that would decide it — the residual gain at the optimized instruction —
   is free from Tier-0 rows 1–3 at n = 1,200 and is thresholded nowhere; its weaker n = 800 pooled cousin g(I_all, B_all)
   carries the entire deployment claim under a ±3pt TOST the proposal itself computes as declarable only within ≈0.2pt
   of zero. Fixes demanded: promote g(I_own, B_own) and/or the retention ratio R = g(I_own,B_own)/g(I0\*,B_own) into the
   confirmatory family as a conjunction, and title the paper after an endpoint the design can establish.
2. **The pre-registration contradicts itself (R1, R3).** Experiments says of A and A0 "Both must pass; nothing else gates
   the confirmatory claim", while Rule M says "absorption is claimed only if the help term carries ≥ 2/3 of ΔInner" and
   prediction 7 restates Rule M as required. In the live case where both ratios clear threshold and the off term carries
   the shrinkage, the document says both that absorption is claimed and that the reading is distractor-robustness.
3. **G6 conditions the denominator on the test set that computes the endpoint (R1).** G3 is correctly on S_dev2; G6's
   Inner(I_oth) ≥ 5pt and Inner(I0\*) ≥ 5pt are checked on the same 1,200 S_test games from which A and A0 are computed.
   A ratio conditioned on its own denominator exceeding a floor in the same sample is biased upward in the hypothesis's
   direction, and the one-sided bootstrap lower bound loses nominal coverage. Fix: move the floor to S_dev2 or an
   independent slice, or simulate and report the conditioning bias.
4. **A0 trades one bias for another, uncomputed (R2).** A0's denominator sits at the short hand-written scaffold, so the
   I0\*-to-I_own level gap is ≈8–11pt by the design's own gates, giving a headroom floor A_h(A0) ≈ 0.16–0.22 — at or above
   the 0.2 lower bound A0 must clear. Prediction 3's "A_h ≤ 0.15" is defined only for A's denominator, and the ladder-level
   null spans two adjacent rungs, a much smaller gap, so it does not price A0's floor. The intersection–union test also
   assumes unbiased marginals; here both marginals are biased toward passing by different mechanisms (mis-specification
   repair for A, context competition and headroom for A0), and they share a numerator.
5. **Missing arms (3/3 for I_type between R1 and R3; R_raw at I_own from all three).** I_type — a hand-written
   instruction naming only the three task types and their skeleton, no episodes — is the rival explanation for the whole
   result and costs ≈25,500 calls, yet sits at Tier 1 while a graded planted control, a compile-once arm whose novelty is
   disclaimed, and a two-seed J arm hold Tier 0. R_raw / M_all read at I_own is the cheapest rival container and is
   fourth on the cut list.
6. **ExpeL is still not confronted (R2, R3).** Its published ablation separates the distilled-insight container from the
   retrieved-trajectory container built from the same training pool, in ALFWorld. The proposal cites ExpeL five times for
   the framing concession and never engages that table, while claiming "nobody has reported the number".
7. **Scan recall (3/3).** The 2024 ALFWorld precedents were supplied by a reviewer, not found by the scan; the pre-2026
   re-sweep and the freeze-blocking provenance-crossover search are still unrun.
8. **Resources (R3).** The refusals (third seed, coupling arm, step control, I_type) are justified by an 84-hour ceiling
   that R3 reads as an artifact of using half the hardware the track brief grants. Partly correct and partly not: this
   node has **two** A100s, not four, and there is no API key. The record needs correcting either way.

## Decision
v5.2 is **not frozen**. Findings 1–4 change a test or a claim's wording, so they are design-blocking, and 1, 3 and 4 are
free or nearly free to fix from cells already in Tier 0. Under T-A's round-cap clause these are resolved-or-descoped in a
resolution text: the author agent writes **v5.3** from `tools/author_brief_v5.3.md`, it is judged once, and the design
freezes on that round's outcome regardless — with the novelty ceiling (4.0, from conceded collisions) recorded as a
limitation that no further round can move.
