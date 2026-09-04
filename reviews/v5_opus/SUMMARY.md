# v5 judging, Opus 5 round — 2026-09-04 (first round of the direction-A loop; author = Opus agent, not Claude Code)

Same prompt/schema/weights (`tools/judge_prompt_v5.md`), three independent Opus judges. v5 was written by an Opus
author agent from `tools/author_brief_v5.md` (direction A: ALFWorld primary, no API key) after reading v4.4, all
four review rounds, the scan and the ALFWorld feasibility report.

## Aggregate
**5.25 — borderline** (nov 4.7 / sig 5.0 / snd 5.3 / fea 6.0 / cla 6.7). R1 5/5/6/6/6, R2 4/5/5/6/7, R3 5/5/5/6/7.
Trajectory (Opus): v4 5.93 → v4.2 6.40 → v4.3 6.05 → v4.4 5.83 → v5 5.25. The move to ALFWorld and the task-type
provenance square were accepted as the right instrument ("identification-and-quantification on top of a published
qualitative result"); the score fell on novelty (EvoAgentBench's table is conceded as the headline; ExpeL's insight
block is "an instruction in all but name") and on two design errors the reviewers found in the new text.

## Design-blocking findings (3/3 unless noted)
1. **Gate and threshold are arithmetically incompatible.** G3 admits a pairing on a 4pt on-type-minus-off-type
   relevance advantage, but Δ_abs ≥ 5pt requires Inner(I_oth) > 5pt *and* near-total absorption *and* a near-zero
   ladder correction. A true 60–70% absorption of a 4–6pt advantage is 2–3pt, below the 4.6–4.8pt MDE, and would be
   reported as inconclusive. Fix demanded: make the **absorbed share** 1 − Inner(I_own)/Inner(I_oth) the confirmatory
   endpoint (threshold on the ratio, powered for its delta-method CI) and raise G3 to ≈8–10pt; add a gate on the
   instruction-provenance main effect (an instruction that learned nothing type-specific cannot have absorbed anything).
2. **Ladder A (best-of-w) is not information-free with respect to the correction it makes.** Best-of-w resolves games
   lost to sampling noise and attenuates prompt sensitivity; an on-type instruction resolves the games the on-type
   bank exists to fix. At matched level the ladder leaves those games unsolved and I_own has removed them, so the
   correction under-corrects in the hypothesis's favour. Ladder B (step budget) shares no mechanism, so agreement
   validates nothing. Fix demanded: a targeted level control (instructions from a subsampled on-type rollout budget,
   or an instruction optimized on a disjoint slice of the same types, titrated to matched accuracy) and a pre-registered
   sensitivity analysis for under-correction. (R2, R3; R1 via the "distractor-robustness" reading)
3. **Missing arms that the framing needs:** (a) **I_own′** — an instruction optimized on a P_train-*disjoint* pool of
   the same task types, to separate "absorbed these episodes" from "learned this task type from any episodes"; the
   title's "same episodes, two containers" cannot be tested without it (R2, R1). (b) **I_all × {M0, B_all} on S_test at
   Tier 0** — every square cell uses a half-space instruction no practitioner would deploy, yet predictions 5–6 are the
   practitioner's numbers (R1, R3). (c) A **distractor-robustness control** (token-matched irrelevant block at *both*
   I_own and I_oth) and a break-deficit bucket in the mechanism rule: a shrinking Inner at I_own is equally consistent
   with the optimized instruction being more robust to off-type text (R1, R3). (d) A **demonstration-bearing I0**
   (2-shot expert-trajectory ReAct scaffold), because the published 5–15pt ALFWorld memory effects were obtained under
   such scaffolds and the thesis makes the choice of I0 outcome-determining (R3).
4. **Compute arithmetic is wrong by 2–3×.** Best-of-w multiplies per-step calls (w ∈ {2,4,8} → cell 10 alone ≈315k
   calls, a quarter of Tier 0), timeouts spend the full step budget, and ≈15 calls/episode is inconsistent with a
   20–60% timeout rate at 20–30 steps. (R2, R3)
5. **Partition.** T_A/T_B splits the near-isomorphic types (clean/cool/heat share one skeleton; pick_two ≈
   pick_and_place), maximizing cross-type transfer and minimizing the relevance advantage G3 needs. Measure cross-type
   transfer on dev first or partition by procedural similarity ({pick, pick_two, look} vs {clean, cool, heat}). (R2)
6. **Reflector.** R3: the track grants a few hundred dollars for the reflector role; a local 32B reflector minimizes
   absorption by construction. **Refused by constraint:** there is no API key; stated as a limitation.
7. **Novelty/scan.** Unchanged: the provenance-crossover primitive is unsearched (pre-freeze obligation 2); the
   2608.14036 appendix is unopened; ExpeL's prepended insight block is already "memory as an instruction". (3/3)

## Decision
This is round 1 of the two-round direction-A loop. The findings are design-blocking (endpoint/gate arithmetic, the
level control's validity, missing arms, compute), so the author gets **one more round (v5.1)**; the judging of v5.1 is
for the record and the design then freezes under T-A with any remaining findings resolved-or-descoped and logged.
The author brief for v5.1 lists items 1–7 as the specification.
