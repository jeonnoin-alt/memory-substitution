# v6 judging, Opus 5 round — 2026-09-07 (author = Fable 5.1 directly; judges web-enabled for the first time)

Protocol: one judge first, two more after it came back borderline. All three had WebSearch (≤6 searches) and were
told to verify the cited IDs and hunt collisions; the previous rounds were closed-book.

## Aggregate
**5.23 — reject** (worst-verdict-wins; nov 4.0 / sig 5.0 / snd 5.7 / fea 6.7 / cla 7.0).
R1 4/5/6/7/7 = 5.35 borderline · R2 4/5/5/5/7 = 4.90 **reject** · R3 4/5/6/8/7 = 5.45 borderline.
Against v5.3 (4.83): feasibility +2.0, clarity +2.0, soundness 0, novelty 0, significance 0. The cut bought exactly
what the calibration predicted and nothing else.

## What the web-enabled judges verified
All three confirmed the load-bearing IDs exist and say what v6 says: ExpeL 2308.10144 (R2 confirmed the 59/55/50
ALFWorld table; R3 saw the ablation but not the numbers), GEPA 2507.19457 (ICLR 2026 oral), Coin Flip 2604.14585
(49% below zero-shot), MemHarness 2607.28272 (70.1 vs 76.4), MemDelta, 2511.21730, 2608.14036. **None found a
collision on the surviving contribution** (residual at a search-optimized same-episode instruction; episode-disjoint
level-matched control). EvoAgentBench 2607.05202 exists but its Table 3 numbers were not visible to their searches;
ours come from the PI-supplied PDF and the exact table must be cited.

## The finding that reframes the thesis (R2)
**ExpeL's own table already contains the joint cell.** Full (insights + retrieval) 59 vs insights-only 50 on ALFWorld
is the residual value of the retrieval container at an instruction-shaped container written from the same pool:
**+9 points, not ≈ 0.** v6's "unpublished number" is published, and its published value contradicts the hypothesis.
The paper as written is therefore a bet that replacing ExpeL's extraction routine with a search optimizer closes a
9-point gap, and it places that bet with the weakest version of the mechanism the novelty rests on: 350 rollouts on
300 games (one sweep plus 50, i.e. about one mutation actually evaluated) and a local 32B reflector.

## Design-blocking findings
1. **The confirmatory family is arithmetically unlikely to fire (3/3).** E declarable only at |ĝ| ≤ 0.9pt; D powered
   at 4pt, thresholded at 3pt; every prior in the proposal's own text (ExpeL +9, this program +0.6–2.4, MemHarness)
   puts the true residual in the 1–4pt band where neither equivalence nor superiority can be declared. Modal outcome:
   two intervals and no claim. Fix (R2, R3): make the **retention ratio R = g(I_P)/g(I0\*)** with a cluster-bootstrap
   CI the primary; it is always declarable and is the quantity Experience Distillation reports.
2. **I′_match is confounded with optimizer maturity (R2, R3) and length/specificity (3/3).** An early snapshot of a
   P′ run matched only on no-memory accuracy is thinner and less specific than the converged I_P; a larger residual
   there is explained by "less instruction leaves more for the bank to say". Fix: a **same-episode early snapshot of
   I_P** at the same level as the comparator (row 3b), plus token- and budget-matching of I′_match, plus the mirror
   cell I′ × B′ so the estimand is a 2×2 provenance interaction, not a difference across unmatched instructions.
3. **Selection on S_dev at sample sizes where the selection is noise (R1, R3).** k\*(I) chosen over 75 games per k
   (paired-gain SE ≈ 5–6pt), I′ snapshot chosen on S_dev, agent×format screened on 50 games at a 5pt bar. Winner's
   curse feeds straight into E and D. Fix: a selection-only partition from the reserve, or one shared k with the
   k-curve as sensitivity, or full k-curves as the reported surface.
4. **Row 9 is not a null (R3).** I_P × {M0, B} at seed 37 is the treatment contrast at another seed; pooling it into
   the null floor contaminates the floor with the effect. Fix: I_P × M0 at two seeds and B × B at two seeds.
5. **Missing arms (3/3 on the first):** a **raw-trajectory retrieval bank** at I_P, k- and token-matched — ExpeL shows
   it is the *stronger* container on ALFWorld (55 vs 50), so v6 measures the residual of the weaker, more
   instruction-like container and biases toward its own null; the **compiled/extraction instruction C** at Tier 0
   (without it "search-based" is untested against AutoManual/AutoGuide); the **coupling arm I2** at Tier 0 (the track's
   question); a **gold-trajectory upper bound** at I_P (separates "absorbed" from "does not read the slot"); official
   `valid_unseen` at Tier 0 (R2).
6. **New 2026 adjacencies surfaced by the judges' searches:** arXiv **2609.00549** "Skill Following: Evaluating Actual
   Skill Use in Retrieval-Enabled LLM Agents" (Sep 2026) — collides with the item-following-rate instrument f(I) and
   must be cited/adopted; 2603.21520 (MemAPO, prompt optimization as accumulated memory); 2606.00619 (MemPro, argues
   prompt-level optimization cannot substitute for memory-pipeline evolution — the thesis's counterparty); 2606.23127
   (AFTER, holds skill annotations fixed to separate skill quality from retrieval); 2606.03083 (DeltaMem, ALFWorld
   per-component ablations); 2608.09096 (Evo-Bench); 2604.18206 (applicability control: when to trigger a
   memory-assisted pass, confidence-gated acceptance, bank governance — abstract read 2026-09-07).
7. **Novelty 4.0, unanimous, for the reasons v6 itself concedes.** The judges' words: "a measurement, not a claim";
   "an interval on top of an accepted qualitative result"; "not scooped, but thin".

## Reading
Feasibility and clarity recovered fully; soundness did not move because the new identification arm has a real
confound and the null replicate was mis-specified. The scientifically important output of this round is R2's point:
the only published data point for the residual is +9pt, so the honest question is *how much a search optimizer
reduces ExpeL's residual*, a retention-ratio question, not an equivalence-to-zero question. That is a major
reframing, not a decimal fix. Per the PI's instruction the loop now **waits**; the next version, if any, is v7.
