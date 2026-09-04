# v2 re-judged under Opus — 2026-09-04 (calibration run, not a revival of v2 as a candidate)

Purpose: separate "the score fell because the design got worse" from "the score fell because the judge changed and
because later versions disclose their collisions". v2 (`reference/proposal_v2.md`, the version that scored **6.97**
with Sonnet in the ideation program) was re-judged with the **same** prompt template, schema and weights used for
v5.3, by three independent Opus judges. Verified before the run: the SYSTEM + SCHEMA blocks are byte-identical to
v5.3's, `reference/track_brief.md` is byte-identical to the ideation brief v2 was originally judged against, and no
prior score or "BEST" marker appears anywhere in the constructed prompt. The only variable is the judge model.

## Result
**6.02 — borderline** (nov 5.3 / sig 6.3 / snd 5.3 / fea 7.0 / cla 8.0). R1 6/7/6/7/8, R2 5/6/5/7/8, R3 5/6/5/7/8.

## The decomposition this buys
| | v2 Sonnet | v2 Opus | v5.3 Opus |
|---|---|---|---|
| total | 6.97 | 6.02 | 4.83 |
Judge substrate costs **0.95**. The remaining **1.19** is the design text itself, and it splits in a way that matters:

| criterion | v2 Opus | v5.3 Opus | Δ | weighted Δ |
|---|---|---|---|---|
| novelty | 5.3 | 4.0 | −1.3 | −0.39 |
| significance | 6.3 | 5.0 | −1.3 | −0.33 |
| **soundness** | 5.3 | **5.7** | **+0.4** | **+0.10** |
| feasibility | 7.0 | 4.7 | −2.3 | −0.23 |
| clarity | 8.0 | 5.0 | −3.0 | −0.30 |

**Soundness is the only criterion that improved across eight rounds of work.** Clarity and feasibility together
(−0.53 weighted) nearly equal the novelty loss (−0.39), and both are scope-and-presentation problems, not validity
problems: v5.3's judge prompt is 153 KB against v2's 36 KB, with 20 Tier-0 rows, six candidate titles and a 14-row
truth table.

## Novelty: v2's 5.3 is not clean either
All three Opus judges found collisions v2's own check missed, and every one is pre-cutoff and verifiable:
**Agent Workflow Memory (arXiv 2409.07429)**, whose offline variant is v2's compiled-block arm C under another name
and which already reports offline induction competitive with online retrieval; **ACE / Agentic Context Engineering
(arXiv 2510.04618)**, which benchmarks an accumulating natural-language playbook directly against GEPA and so
falsifies v2's sentence that nobody uses one as the control for the other; **Dynamic Cheatsheet (arXiv 2504.07952)**;
**MIPROv2's instruction-versus-demonstration ablations**; and **ExpeL's own insights-versus-retrieved-trajectories
ablation**. So v2 scores 1.3 novelty points higher while carrying *more* undisclosed collisions than v5.3, which
concedes its own in the first paragraph. The gap is largely the price of disclosure, not a difference in originality.

## Soundness: v2's objections are exactly what v4.2–v5.3 fixed
Saturation and headroom ("any stronger baseline shrinks a second intervention's marginal gain, and no arm separates
that from substitution" — R3), the precheck gate selecting the denominator on dev noise (R1, R2), equivalence claims
below the MDE with no TOST (R2), and optimization pressure applied to the instruction container but not the bank
(R1). The later versions' headroom controls, split-sample gating, TOST margins and null replicates are answers to
these, and the soundness number reflects it. The eight rounds bought a design that is more correct and much less
legible.

## The one control four independent judges have now named
A **retrieval-budget (k) arm**. v2's R2: "the track's own measured result is that injection volume, not memory
content, was the causal lever, so fixing k = 7 makes both the S denominator and the compiled-versus-retrieved verdict
functions of an untuned hyperparameter." v5.3's R1 and R3 said the same about k being tuned once under the
hand-written scaffold and then held fixed across instructions of very different lengths. That is four judges across
two rounds, on a confound this program measured in its own prior work. It is fixed in whatever version ships next.

## Reading
This is not an argument for reviving v2: its primary endpoint has the saturation confound the whole lineage was built
to remove, and its collision check is weaker. It is an argument that the remaining score gap is concentrated in
scope and legibility, which cutting fixes, and in disclosure, which should not be undone.
