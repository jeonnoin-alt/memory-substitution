# Author brief — write proposal v5 (2026-09-04)

You are the **author** of a research proposal in an automated ideation loop (the harness re-implementation of
`ideate.py`'s revise round: author → three independent reviewers → aggregate). You revise; you do not judge.
Read everything listed under *Inputs* before writing a word. Then write **one file**,
`/home/work/neuro/memory-substitution/reference/proposal_v5.md`, in the exact format under *Output*.

## The decision that frames this revision (made by the PI, not negotiable)

**Direction A.** The confirmatory environment moves to **ALFWorld** (text-only, `AlfredTWEnv`), where task templates
recur and procedural memory has real content to carry; tool-augmented multi-hop QA (E1) becomes the replication
environment. ALFWorld is verified to run on this node (read `reference/alfworld_feasibility_2026-09-04.md`): all
3,553 training games plus the 140/134 eval games are on disk, the engine and the bundled expert work, and the test
pool can be **held-out training games** (n up to 1,500, stratified over the six task types), so the old n=274 ceiling
is gone. Human goal annotations are unavailable; games use ALFWorld's default templated goals.

**No API key.** There is no frontier API. Every model role — the agent, the GEPA reflector, the distiller, the
compiler, any judge — is a local open-weight model on 2×A100-80GB: Qwen3.5-27B and Qwen3-32B (dense), gpt-oss-120b
(MoE, out of the track's 7B–32B scope, usable only as a check), medgemma-27b-it. The reflector/distiller/compiler is
Qwen3-32B; say so and state the consequence (a weaker reflector than the literature's frontier reflectors).

## Rules for this revision (verbatim from `ideate.py`'s REVISE_SYSTEM; they are the specification)

You are revising your own research proposal after review. The reviewers' objections are the specification. Answer
each one concretely — not by adding reassuring prose, but by changing the design: cut experiments that do not carry a
claim, drop target tasks, shrink the grid, narrow the claim to what the sample size can actually detect, add the
baseline they named.

- **Do not abandon the core hypothesis.** A proposal that answers every objection by becoming generic is worse than
  one that keeps a sharp claim and scopes it honestly. If an objection can only be answered by giving up the
  contribution, keep the contribution and say in changes_made why you refused.
- **Novelty is the thing you are most likely to lose.** Answering reviewers reliably raises soundness and feasibility
  and *lowers* novelty. Do not soften the central claim into something a reviewer could not disagree with, do not
  replace a sharp mechanism with a measurement study, and do not add qualifiers that make the prediction
  unfalsifiable. If a reviewer's objection is really "this is risky", the right answer is a better test of the risky
  claim, not a smaller claim.
- **The resource envelope is hard.** Every experiment must fit the stated compute and budget. If the full matrix does
  not fit, cut it to a primary experiment that decides the main claim plus the minimum ablations that isolate the
  mechanism, and state the arithmetic: number of runs × rollouts per run, and why that fits. A smaller study that can
  be run beats a large one that cannot.

Do **not** use the "deepen" mode of thinking (raise the ceiling, pivot the claim): that is what produced v3's
scope drift. Keep the lineage's claim — memory bank and optimized instruction as two containers for the same
training episodes; how much of memory's value the instruction absorbs beyond headroom — and make it testable where
the phenomenon exists.

## What the four Opus rounds found (you must answer every item; read the SUMMARY files for the full text)

v4 (5.93): S not identified vs headroom compression. v4.2 (6.40): crossover accepted; power, full-data arms, joint
optimizer missing. v4.3 (6.05): endpoint placed where the effect is 0–4pt; gated at I0; ±4pt margins. **v4.4 (5.83),
the round you are answering:**
1. The hand-written "headroom curve" (H1, H2, I0+3) does not identify Δ_abs: three different interventions, not one
   curve indexed by accuracy; nearest-member comparator chosen on n=300; extrapolation allowed. Reviewers asked for a
   monotone, single-knob level control with ≥5 levels bracketing the optimized instruction's level, the residual
   scatter of memory's gain around that curve as the null distribution, and a null replicate of Δ_abs itself.
2. **Off-policy bank confound:** every bank was distilled from episodes run under I0 and injected under I1. Add an
   on-policy bank (distilled from episodes generated under the optimized instruction) — or explain why not.
3. Claim threshold (2pt) below the MDE (≤2.9pt) and at the null floor; power the confirmatory test properly.
4. The crossover's expected null was pre-declared and then read as "generic absorption" (circular); the planted
   control certified sensitivity at 15–30pt, not at the 1–2pt scale that matters. In ALFWorld, task types give you a
   *structured* provenance manipulation (a Latin square over task-type sets for instruction provenance × bank
   provenance × test type) that separates relevance from provenance instead of confounding them — consider it.
5. D_opt / the jointly optimized prompt (J) must not be cuttable if the compile/deployment claim is made.
6. A compute-matched sampling control (best-of-n / self-consistency at memory's token budget) in addition to the
   extra-step-budget control.
7. Re-scan obligations: the appendix of arXiv 2608.14036; provenance / held-out-episode crossovers in the
   prompt-optimization and contamination literature. You cannot search from here; state them as pre-freeze
   obligations and do not claim novelty for the crossover primitive beyond what the scan supports.
8. Completion mechanics: proposal ①'s 2026-09-04 finding (bare arms hid answerless episodes; memory raised
   indecision; fair mechanics +2.4pt vs +0.6pt) — keep the mechanics fixed across arms and state the ALFWorld analogue
   (episodes end at success or step limit; report timeout rates per cell).

## Constraints you must honour

- Track brief (`reference/track_brief.md`): 7B–32B open-weight agents; public data; days, not weeks; one claim.
- Two A100-80GB, one vLLM replica per GPU. Measured in this program: 985–1,380 multi-hop-QA episodes/hour per replica
  for a 27B agent (≈6 calls/episode). ALFWorld episodes take ≈5–36 agent turns (expert: 5–12 on train, 7–36 on
  unseen); budget ≈15 calls/episode and derive episodes/hour from that. Give the arithmetic per tier.
- The pilot's numbers (proposal ①, `reference/shortcutting_v4/`): ExpeL bank on Qwen3.5-27B in multi-hop QA +0.6pt
  bare / +2.4pt with fair mechanics; +7.7pt on gpt-oss-120b; between-seed spread of optimized instructions 1.0–1.6pt;
  treatment-free decoding spread 2.8–3.4pt at n=500. Published ALFWorld memory effects for reference: ExpeL,
  Memp, MemHarness (raw memory 70.1 vs no-memory RL 76.4; reconstruction 85.2), "When Continual Learning Moves to
  Memory" (2604.27003). Cite only IDs that are in `reference/litscan_2026-09-03.md`; do not invent citations.
- Judging: `reference/judging_constants.md` (REVIEW_SCHEMA, weights). The reviewers will be three independent
  Opus instances with the same prompt as before.
- House rules (HANDOFF §measurement): paired within-instance comparisons, exact McNemar + Holm with fix/break
  decomposition, TOST or bounded-loss CIs for every "no difference" claim, null replicates, MDE stated before running,
  pre-registered drop order, unrun arms reported as unrun.

## Inputs (read all, in this order)

1. `reference/track_brief.md`
2. `reference/proposal_v4.4.md` (the text you are revising; its decision log has 49 rows — continue the numbering)
3. `reviews/v4.4_opus/SUMMARY.md`, then `reviews/v4.4_opus/r1.json`, `r2.json`, `r3.json`
4. `reviews/v4.3_opus/SUMMARY.md`, `reviews/v4.2_opus/SUMMARY.md`, `reviews/v4_opus/SUMMARY.md`
5. `reference/alfworld_feasibility_2026-09-04.md`
6. `reference/litscan_2026-09-03.md` (citation table; the only IDs you may cite)
7. `reference/shortcutting_v4/DESIGN.md` (design-document precedent and the pilot's measured quantities)
8. `reference/judging_constants.md`
9. `HANDOFF.md` (mission and house rules)

## Output

Write `/home/work/neuro/memory-substitution/reference/proposal_v5.md` with exactly this structure:

```
# Proposal v5 — memory_or_instruction (2026-09-04; v4.4 revised under direction A after the fourth Opus round, see reviews/v4.4_opus/SUMMARY.md)

Lineage: <copy v4.4's lineage line and append " → v4.4 5.83 (opus) → **v5 (this file)**">

## Decision log (cumulative; rows 50–NN are new in v5)

<copy v4.4's table verbatim, then append one row per objection answered or refused, numbered from 50>

---

## Name
## Title
## Short Hypothesis
## Related Work
## Abstract
## Experiments
## Baselines and Ablations
## Falsifiable Predictions
## Measurement and Noise Control
## Preprint Collision Check
## Risk Factors and Limitations
```

Each of the 11 field sections is complete prose (the judges see only these 11 fields, not the decision log).
Field guidance: Experiments carries the full design (screening, splits, artifacts, gates with branches, the
condition grid as a table with n/seeds/tier, primary and secondary endpoints, compute arithmetic, ordered cuts);
Measurement and Noise Control carries the variance components and the MDE derived from the pilot's numbers;
Preprint Collision Check keeps v4.4's verified content, adds the pre-freeze obligations, and does not add unverified
IDs; Risk Factors includes every refusal with its reason. Name stays `memory_or_instruction`. The Short Hypothesis
is one claim. Do not write code. When the file is written, reply with a 10-line summary of what changed and what you
refused; nothing else.
