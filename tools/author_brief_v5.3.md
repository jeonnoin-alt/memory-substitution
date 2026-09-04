# Author brief — write proposal v5.3 (2026-09-04, the resolution text; one judged round, then freeze)

Same role, rules and constraints as `tools/author_brief_v5.md`, `_v5.1.md` and `_v5.2.md` — read all three first.
You are amending **your own v5.2** (`reference/proposal_v5.2.md`) after its Opus round, which came back **5.12, reject**
(`reviews/v5.2_opus/SUMMARY.md`, `r1.json`, `r2.json`, `r3.json`). v5.2 had been declared frozen without judging; that
was wrong and the round was run. This is the resolution text: it is judged once and the design then freezes on that
outcome. Direction A (ALFWorld primary, no API key, local models only) is unchanged. Keep every sentence v5.2 already
has unless an item below requires the change, and keep Tier 0 inside the compute ceiling you state.

## Items

1. **The endpoint must test the title, or the title must change (3/3, the decisive finding).** Inner is the bank's
   task-type *discriminability*; A ≥ 0.5 is compatible with the bank still paying several points at I_own, in which
   case the paper's own question is answered "no" while the bar reads pass. Do all of:
   (a) Add the residual-value quantity to the **confirmatory family**, computed free from Tier-0 rows 1–3 at n = 1,200:
   **g(I_own, B_own) = acc(I_own×B_own) − acc(I_own×M0)** and the **retention ratio R = g(I_own,B_own)/g(I0\*,B_own)**.
   (b) Pre-register the **conjunction** that licenses the headline: absorbed share above threshold **and** the residual
   gain equivalent to zero within a stated margin. State the margin the n supports; if ±3pt is the smallest the design
   holds, say so and accept that only a near-zero residual can license the strong claim.
   (c) Pre-register, in both directions, the outcome where A and A0 pass but the residual gain survives: that is
   **"the type-specific content is absorbed, the generic content is not"**, it gets a different title, and it is
   reported as the finding rather than as a pass. Say which title each branch takes.
   (d) Revisit the **Title** field accordingly so the claim in the title is the claim the confirmatory family tests.
2. **Remove the self-contradiction (R1, R3).** "Both must pass; nothing else gates the confirmatory claim" (Experiments)
   versus "absorption is claimed only if the help term carries ≥ 2/3 of ΔInner" (Rule M, restated in prediction 7).
   Replace both with a single **truth table** over the outcome space {A, A0, residual-gain equivalence, Rule M bucket,
   Rule R verdict}, giving for every combination the claim that is made and the title that goes with it. No cell may be
   left to interpretation.
3. **G6 must not condition the endpoint's denominator on the endpoint's own sample (R1).** Move the Inner(I_oth) ≥ 5pt
   and Inner(I0\*) ≥ 5pt floors to **S_dev2** (where G3 already lives) or to an independent reserve slice named here. If
   any floor must be re-checked on S_test, it becomes a **reported diagnostic, not a gate**, and you state that the
   published CI is conditional and quantify the conditioning bias by simulation. Say explicitly which coverage claim
   survives.
4. **Compute A_h for each denominator and null-replicate the gap that matters (R2).** A0's denominator sits at I0\*, so
   its headroom floor spans the I0\*-to-I_own gap: by your own gates that is ≈8–11pt, i.e. A_h(A0) ≈ 0.16–0.22, at or
   above the 0.2 bound A0 must clear. Report A_h separately for A, A0 and A_all; add a **matched-gap null replicate** —
   A computed between two instructions separated by that level gap with **no** provenance difference (a Ladder T rung
   pair chosen to span it, or best-of-w titrated to it) — and either raise A0's threshold to its own null's 95th
   percentile plus a margin, or state that A0's bound is read against that null and not against 0.2. Also address the
   intersection–union assumption directly: the two marginals are biased toward passing by different mechanisms and share
   a numerator, so say what the joint rule does and does not control.
5. **Arms.** Promote **I_type** to Tier 0 (≈25,500 calls; it is the rival explanation for the headline and it is already
   written and hashed) and **R_raw / M_all read at I_own** to Tier 0 (the cheapest rival container; three reviewers now
   name it). Pay for both by cutting row 12 (J) to one seed, the 25% arm of row 9, and row 11 to one seed — or state a
   different funding order. Keep Tier 0 inside the ceiling and republish the totals in episodes, calls and hours.
6. **Confront ExpeL numerically (R2, R3).** Its published ablation separates a distilled-insight container from the
   retrieved-trajectory container built from the same training pool, in ALFWorld. Engage that table in Related Work:
   state what it reports, what it does not manipulate (episode provenance, the crossover, token matching, paired
   statistics), and revise "nobody has reported the number" to a claim that survives it. No other new citations except
   as item 7 requires.
7. **Scan obligations.** Record that the 2024 ALFWorld precedents were supplied by a reviewer rather than found by the
   scan, that the scan was recency-weighted, and that a **pre-2026 re-sweep** is now a fourth obligation. Obligation (1),
   the provenance-crossover search in the contamination and data-attribution literatures, stays freeze-blocking.
8. **Correct the resource record (R3).** This node has **two** A100-80GB, not the four the track brief describes, and
   there is no API key. State both plainly where the refusals are justified, so the 84-hour ceiling is read as a hardware
   fact rather than a self-imposed limit; keep the reflector refusal with its bias direction; and note that the
   throughput band is transferred from a 6-call multi-hop-QA setting and is measured by G5 before anything depends on it.
9. **Novelty ceiling, stated once.** Judges have converged at novelty 4–5 because of collisions the proposal itself
   concedes. Do not argue with it; state in Related Work and Risk Factors that the contribution is identification and a
   number on top of an accepted qualitative result, that this caps the venue expectation, and that the design's value is
   the pre-registration and the interval rather than the surprise.

## Output

Write `/home/work/neuro/memory-substitution/reference/proposal_v5.3.md` in exactly v5.2's structure: the cumulative
decision-log table (rows 1–91 verbatim from v5.2, then rows 92+ for this round), a `---` separator, then the 11
`## <field>` sections. Lineage line: append " → v5.2 5.12 (opus, reject) → **v5.3 (this file)**". Name stays
`memory_or_instruction`. Do not write code. When the file is written, reply with a 10-line summary of what changed and
what you refused — nothing else.
