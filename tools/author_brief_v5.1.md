# Author brief — write proposal v5.1 (2026-09-04, final round before freeze)

Same role, same rules and same constraints as `tools/author_brief_v5.md` — read that file first, then this one.
You are revising **your own v5** (`reference/proposal_v5.md`) after its Opus round (`reviews/v5_opus/SUMMARY.md`,
`r1.json`, `r2.json`, `r3.json`). This is the **last round before the design freezes**: every finding below must
be resolved or explicitly descoped with a reason in the decision log and in Risk Factors. Direction A (ALFWorld
primary, no API key, local models only) is unchanged and not negotiable.

## Findings to answer (read the three review JSONs for the full arguments)

1. **Gate/threshold arithmetic (3/3).** G3 admits a 4pt relevance advantage while the confirmatory Δ_abs needs 5pt,
   which requires Inner(I_oth) > 5pt and near-total absorption at once; a real 60–70% absorption of a 4–6pt advantage
   (2–3pt) lands below the MDE. Make the **absorbed share** A = 1 − Inner(I_own)/Inner(I_oth) the confirmatory
   endpoint with a ratio threshold (e.g. A ≥ 0.5 with the 90% delta-method/bootstrap lower bound ≥ 0.2), raise G3 so
   the ratio is estimable (relevance advantage ≥ 8–10pt on S_dev2 with a lower CI ≥ 5pt), and add a **gate on the
   instruction-provenance main effect** (acc(I_own×M0) − acc(I_oth×M0) on own-type games, lower CI > 0). Show the
   arithmetic that the gate floor and the endpoint threshold are consistent, and state what a G3 failure means
   (the branch must not be "fall back to the level-ladder endpoint four rounds rejected").
2. **Ladder A is not information-free for the correction it makes (R2, R3).** Best-of-w resolves games lost to
   sampling noise and attenuates prompt sensitivity; the on-type instruction resolves the games the on-type bank
   exists to fix, so the correction under-corrects in the hypothesis's favour, and Ladder B cannot validate it. Fix:
   use a **targeted level control** — instructions from the on-type optimizer at *subsampled rollout budgets*
   (e.g. 50/100/200/350 rollouts) and/or an instruction optimized on a *disjoint* slice of the same types, titrated
   to bracket the level — and pre-register a **sensitivity analysis**: how much of A survives if the correction
   under-corrects by 25% and 50%. Keep best-of-w only as the compute-matched sampling control, not as the ladder.
   Alternatively, argue (with arithmetic) that the ratio endpoint at a fixed instruction needs no level correction at
   all — Inner(I) compares two banks at one instruction, so headroom is identical inside Inner; the level correction
   was only needed to compare Inner across two instructions. If you take that route, say what replaces it.
3. **Missing arms (Tier 0, or a reason):**
   (a) **I_own′** — an instruction optimized on a **P_train-disjoint** pool of the same three task types (there are
   3,553 training games; reserve a disjoint slice), run against B_own and B_oth. This separates "absorbed these
   episodes" from "learned this task type from any episodes"; without it the title's "same episodes, two containers"
   is untested (R2, R1). Its expected reading must be pre-registered.
   (b) **I_all × {M0, B_all} on S_test** — the practitioner's configuration (pooled instruction, pooled bank), at
   Tier 0 with enough seeds for the 3pt bounds predictions 5–6 use (R1, R3).
   (c) **Distractor-robustness control** — a token-matched, plausibly worded, task-irrelevant block at **both**
   I_own and I_oth (cell 24 promoted and run at both instructions), and a **break-deficit bucket** in the mechanism
   rule: a smaller Inner at I_own is also consistent with the optimized instruction being more robust to off-type
   text (R1, R3).
   (d) **A demonstration-bearing I0** — a 2-shot expert-trajectory ReAct scaffold as an alternative baseline
   instruction, because the published 5–15pt ALFWorld memory effects were obtained under such scaffolds and the
   thesis makes the choice of I0 outcome-determining (R3). Either run G1/G3 under both I0 variants on dev and
   pre-register which is primary, or explain why one suffices.
   (e) A direct **content check** that I_own contains the procedures B_own's items encode (textual overlap or item
   ablation), since the claim is about content moving between containers (R1).
4. **Compute arithmetic (R2, R3).** Recompute every cell in **LLM calls**, not episodes: best-of-w multiplies per-step
   calls by w; timeouts spend the full step budget; use the dev-measured timeout rate to set calls/episode (state the
   assumption: e.g. mean 12 steps solved / full 30 steps timed out, 25% timeouts → ≈16.5 calls). Then re-derive
   hours at a stated calls/hour per replica and cut until Tier 0 fits ≈3 days on 2×A100. Show the multipliers
   explicitly for the sampling cells.
5. **Partition (R2).** T_A/T_B currently splits near-isomorphic types. Either partition by procedural similarity
   ({pick_and_place, pick_two, look_in_light} vs {clean, cool, heat}) with a stated reason, or pre-register a dev
   measurement of cross-type transfer that chooses the partition, with the rule written down before any test cell.
6. **Reflector (R3).** Refused by constraint — no API key exists on this node. Keep the local reflector, state the
   bias direction (it makes absorption harder to find, so it is conservative for the claim) and keep the G2 branch.
7. **Novelty and scan (3/3).** Do not add citations. State plainly that EvoAgentBench publishes the qualitative
   headline and that ExpeL's prepended insight block already makes "memory as an instruction" a design pattern; the
   contribution is the identification and the number. Keep the three pre-freeze scan obligations and add that
   obligation (2) is now a **freeze-blocking** item that the PI runs before DESIGN.md is hashed.
8. **Clarity.** One confirmatory endpoint, ≤ 8 predictions, a grid a reader can hold in one screen. If a Tier-0 arm
   does not bear on the endpoint or on a named refutation, cut it.

## Output

Write `/home/work/neuro/memory-substitution/reference/proposal_v5.1.md` in exactly v5's structure: the cumulative
decision-log table (rows 1–67 verbatim from v5, then rows 68+ for this round, each naming the objection and the
answer or refusal), a `---` separator, then the 11 `## <field>` sections with complete prose. Lineage line: append
" → v5 5.25 (opus) → **v5.1 (this file)**". Name stays `memory_or_instruction`. Do not write code. When the file is
written, reply with a 10-line summary of what changed and what you refused — nothing else.
