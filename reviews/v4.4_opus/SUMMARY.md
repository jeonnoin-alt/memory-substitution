# v4.4 judging, Opus 5 round (the "confirmatory" round after the freeze-rule resolution) — 2026-09-04

Same prompt/schema/weights (`tools/judge_prompt_v4.4.md`), three independent general-purpose subagents, model opus.

## Aggregate
**5.83 — borderline** (nov 5.7 / sig 5.7 / snd 5.7 / fea 7.0 / cla 6.0). R1 6/5/6/7/6, R2 6/6/5/7/6, R3 5/6/6/7/6.
Opus trajectory: v4 5.93 → v4.2 6.40 → v4.3 6.05 → v4.4 5.83. The score has plateaued around 6 for four rounds; each
round removes the previous round's objection and the reviewers find the next identification gap. That pattern is itself
a finding about the proposal (see "Assessment").

## What all three say — new design-blocking findings (the loop reopens under T-A)
1. **The headroom curve does not identify Δ_abs.** Three information-free points (H1, H2, I0+3) are three different
   interventions, not one curve indexed by accuracy: H2 is content-identical to the modal multi-hop insight (biases the
   comparator conservative), I0+3 changes memory's marginal value through a different channel (search budget), and the
   pre-registered comparator is the single nearest member chosen on a 300-instance dev sample (SE ≈2.4pt). Two prompts at
   equal accuracy leave different residual unsolved sets, so g_H(ℓ₁) is not the counterfactual the test needs. (3/3)
2. **Off-policy bank confound (missing baseline).** Every bank is distilled from episodes run under bare I0, then injected
   under I1_ab. Memory's gain shrinking at I1_ab is equally explained by bank staleness (the items describe another
   policy's traces) as by absorption. Nothing in the grid separates them. Fix: an on-policy bank B^{I1} distilled from
   episodes generated under I1_ab. (R2, R3; R1 implicitly via the residual-set argument)
3. **The claim threshold (2pt) sits below the MDE (≤2.9pt) and at the expected null floor (≈2pt at n=1,500), and there is no
   null replicate of Δ_abs itself** — the confirmatory result is inconclusive at its own threshold by construction. (R1, R3)
4. **The specificity probe is pre-declared to return the uninformative value in E1** (Δ_info ∈ [−1, +1]) and that value is
   then read as "generic absorption" — circular; and the planted control certifies sensitivity at 15–30pt, not at the
   1–2pt natural content whose absence the null is meant to license. (R2)
5. **E1 remains the wrong confirmatory environment** for a procedural-memory claim; E2 or a web/tool agent should carry it,
   with E1 as replication. (R2, R3 — third round in a row)
6. **D_opt / J (the demonstration container's optimized representative) still cuttable**; if J×M0 matches I1_ab×M_ab the
   headline is about the demonstration slot, not about memory being redundant with instructions. (R1)
7. **The provenance crossover has never been searched for** in the contamination / data-attribution literature; the
   2608.14036 appendix is still unopened. (3/3)

## Assessment (for the PI)
The round-3 resolution moved the claim from "substitution" to "absorption beyond headroom" and the reviewers accepted the
move but rejected the instrument: a level-matched control built from a handful of hand-written prompts cannot carry a
confirmatory claim, and the off-policy bank is a real confound this program's own proposal ① also carried (its bank was
distilled under M0 and injected under instruction arms).

Underneath the instrument objections is one fact that has not changed since v4: on 27–32B agents in tool-augmented
multi-hop QA the memory effect is 0–4pt (proposal ①: +0.6 bare, +2.4 with fair mechanics; EvoAgentBench: +3.6 RB, +1.2 GEPA).
Any decomposition of a ≤4pt effect into headroom / generic absorption / specific absorption is at the noise floor of a
1,500-instance study, and no amount of design will change that. There are three coherent ways forward, and they are the
PI's choice, not the harness's:

A. **Move the confirmatory environment to one with recurring procedural structure** (ALFWorld with held-out training games,
   or a web/tool agent benchmark), where published memory effects are 5–15pt (MemHarness, EvoMemBench, Memp), so the
   quantities being decomposed are several times the floor. Cost: ALFWorld must be installable on this node (package via
   PyPI works; game data lives behind GitHub release assets, which this network has blocked before), and E2 episodes are
   ≈4× the calls of E1. E1 becomes the replication.
B. **Keep E1 and re-scope the paper to what E1 can support**: the memory-null / headroom report (outcome B in v4.4) with
   the fair-mechanics finding from proposal ① as its centre — "on strong 27–32B agents, procedural memory's headline gain
   is answerless-episode rescue plus headroom, and an evidence-citation line does the same job". This is publishable as a
   measurement note and is essentially what proposal ① already found; it does not need a new 70k-episode study.
C. **v4.5 in E1 with the instrument fixes** (search-budget sweep as a monotone headroom control, on-policy bank, null
   replicate of Δ_abs, structure-split crossover as an extra probe, J at Tier 0, threshold above the floor). This answers
   the reviewers but keeps the claim at the noise floor; expect the same ≈6 score and a fifth round of objections.

Recommendation: A, with a feasibility check of ALFWorld on this node as the very first Stage-3 step, and v4.4's E1 grid
retained as the replication. If ALFWorld cannot be installed, B.

## Freeze status
Not frozen. Under T-A the confirmatory round produced new design-blocking findings (items 1–3), so the loop is reopened
and the next text (v4.5) is written only after the PI chooses between A, B and C.
