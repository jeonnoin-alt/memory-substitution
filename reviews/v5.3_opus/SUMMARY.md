# v5.3 judging, Opus 5 round — 2026-09-04 (the resolution round; author = Opus agent)

Same prompt/schema/weights (`tools/judge_prompt_v5.3.md`, 151 KB), three independent Opus judges.

## Aggregate
**4.83 — reject** (nov 4.0 / sig 5.0 / snd 5.7 / fea 4.7 / cla 5.0). R1 4/5/5/5/4 **reject**, R2 4/5/6/5/5 borderline,
R3 4/5/6/4/6 borderline. Trajectory: v4.2 6.40 → v4.3 6.05 → v4.4 5.83 → v5 5.25 → v5.1 5.57 → v5.2 5.12 → **v5.3 4.83**.

## What v5.3 fixed and no judge re-raised
The truth table (all three read it and none found an unhandled cell), G6 moved off S_test, the per-denominator A_h
numbers, the residual gain in the confirmatory family, ExpeL conceded, the resource record. Soundness held at 5.7.

## Why the score still fell: feasibility 4.7 and clarity 5.0, both the lowest in the lineage
The document is now 452 lines with 20 Tier-0 rows, six pre-registered titles and a 14-row truth table. Two judges say
in almost the same words that the modal deliverable of 990,000 calls is one of the fallback papers, not the headline,
and one adds that the version-history scaffolding ("v5.2 said X, withdrawn") should not be in a submission.

## Design-blocking findings
1. **Powered where it is not novel, under-powered where it is (R1, echoed by R2).** Rows 1–3 carry at n = 1,200 with
   two seeds exactly what ExpeL and EvoAgentBench already publish qualitatively. The three arms that carry the *new*
   identification — Ladder T's A_epi (n = 500, one seed, SE ≈ 0.30, de-thresholded), I_type (n = 500, SE ≈ 2.6pt, so
   only a ≥ 4.3pt gap is distinguishable) and B′_own (which risk 26 concedes answers the bank-side question) — are all
   descriptive. Strip them and the study is ExpeL's ablation with paired statistics; keep them and they cannot bear a
   claim. Fix demanded: put the identification arms at n = 1,200 with two seeds and pay for it by deleting the arms the
   proposal itself calls replication (compile-once, row 11), the ceiling arm (J, row 12) and the third denominator
   (A_all, row 16).
2. **The retrieval budget k is pinned across instructions of very different lengths (R1, R3).** k is tuned once on dev
   under the hand-written scaffold and then HELD FIXED THROUGHOUT, including in the residual-gain cells. **The research
   track's own headline prior is that injection volume, not memory content, was the causal lever** — cutting seven
   retrieved items to three eliminated the harm from the same bank — and the ALFWorld literature this proposal cites
   says excessive retrieval harms sequential decision-making specifically. If the optimal k under the longer, procedure-
   bearing I_own is smaller, then g(I_own, B_own) is depressed by context competition rather than by absorption, which
   pushes endpoint E toward passing and inflates A0 at the same time. The study would print its headline title for a
   budget artifact. Neither X_dist nor M_shuf covers it: both are token-matched at the same fixed k.
3. **A flat 0.5 threshold across denominators with different floors (R3).** A_h is 0.06–0.12 for A, **0.16–0.22 for the
   co-primary A0**, 0.04–0.08 for A_all, and the same nominal bar is applied to all three. A0 = 0.50 at its own floor is
   ≈0.3 of real absorption; A = 0.50 at its floor is ≈0.4. The abstract's "at least half is absorbed" is false on the A0
   branch at its floor. v5.1 had the right instrument — the floor-adjusted (A − A_h) — and the v5.2/v5.3 briefs deleted
   it. Fix: require (Â − A_h)/(1 − A_h) ≥ 0.5 per denominator.
4. **Rule M's help/off 2/3 bucket has no standard error and selects between the headline and its negation (R2).**
   help(I) and off(I) are paired differences with SE ≈ 1.4pt each, so a 2/3 share of a 4–6pt ΔInner is not estimable at
   n = 1,200, yet truth-table rows 1 and 3 differ only by that bucket and carry titles T1 and T4. Either power it or
   demote it to a diagnostic alongside Rules F and C.
5. **Missing controls.** A length-matched instruction control (R2): every memory container is token-matched to every
   other, but the instruction containers are never matched to each other, so part of A0 can be prompt mass rather than
   absorbed content. {C_own, C_oth} × {B_own, B_oth}, the non-GEPA prose summary (R3): without it a positive result
   licenses only "a GEPA instruction absorbs the bank", and AutoManual makes "any prose written from these episodes"
   the likelier reading.
6. **Novelty 4.0, unanimously, for the same reason each time.** ExpeL's ablation table has still not been read; arXiv is
   unreachable from this node. R1 adds a precedent the scan never had: the instruction-induction / APE line
   (Honovich et al. 2022; Zhou et al. 2022), which is "compile demonstrations into an instruction" in its original form.

## Decision
Three consecutive rounds have now traded one blocker for another while feasibility and clarity fall, so more of the same
loop is not the fix. The convergent instruction from the reviewers is the opposite of what the last three briefs did:
**cut**. Two of three independently propose collapsing to one denominator and one primary pair, powering the
identification arms, and deleting the replication arms. That is a scope decision for the PI, not a wording fix, so the
loop stops here and the PI chooses between:
(A) freeze v5.3 and run it, accepting that the modal deliverable is a pre-registered fallback paper;
(B) one **cutting** round (v6): single denominator A0, primary = residual gain g and retention ratio R, identification
    arms at n = 1,200, per-instruction k re-tuning added, compile-once / J / A_all / the six-title apparatus deleted;
(C) stop judging, run the experiment, and let the data decide the paper.
Finding 2 (the k artifact) must be fixed under any of the three, because it is a validity threat this program has
already measured once in its own prior work.
