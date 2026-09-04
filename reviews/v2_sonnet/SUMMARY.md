# v2 re-judged under Sonnet — 2026-09-04 (the control for the Opus calibration run)

The PI asked whether the harness reproduces the original **6.97** when the judge is Sonnet, using the identical
prompt. Same `tools/judge_prompt_v2.md`, same schema, same weights as the v2 Opus run and the v5.3 run. Three
independent Sonnet judges. Predictions were written down before the run: ≥ 6.7 confirms the judge model is the cause,
≈ 6.0 falsifies it and points at harness-versus-API instead.

## Result
**7.10 — borderline** (nov 6.3 / sig 7.0 / snd 7.7 / fea 7.3 / cla 8.0). Per reviewer: 7.15, 6.95, 7.20 — a tight
spread. The original ideate.py API run gave **6.97**, so the harness reproduces it to within 0.13.

| same text, `proposal_v2.md` | score |
|---|---|
| Sonnet, original ideate.py API run | 6.97 |
| **Sonnet, this harness** | **7.10** |
| Opus, this harness | 6.02 |

**The judge model is the cause, and harness-versus-API is not.** The gap on this text is **1.08 points**, larger than
the 0.95 estimated from the API number, and well outside the reviewer spread (Sonnet SD ≈ 0.13, Opus ≈ 0.46).

## Where the gap lives, and the caveat that it is not a constant
| criterion | v2: Sonnet − Opus | v4: Sonnet − Opus |
|---|---|---|
| novelty | +1.0 | +0.3 |
| significance | +0.7 | +0.3 |
| **soundness** | **+2.4** | **+0.7** |
| feasibility | +0.3 | −1.3 |
| clarity | 0.0 | −1.3 |
| **total** | **+1.08** | **+0.09** |

The one direction that holds in both comparisons is **soundness: Sonnet scores it higher, by +2.4 and +0.7.** The v4
totals tie only because Opus happened to score v4's clarity 1.3 higher, which cancelled its lower soundness. So the
substrate correction is real but text-dependent, between 0.1 and 1.1, and it cannot be applied as a single offset.
The clean series is the Opus-only one: v2 6.02, v4 5.93, v4.2 6.40, v4.3 6.05, v4.4 5.83, v5 5.25, v5.1 5.57,
v5.2 5.12, v5.3 4.83.

## Why this matters more for idea selection than for this proposal
Sonnet gave v2 **soundness 7.7**. Opus gave the same text **5.3**, and its three judges named the reason: the primary
endpoint has a saturation confound, since any intervention that raises the baseline shrinks a second intervention's
marginal gain whether or not the two containers hold the same information. Sonnet did not raise it.

Every idea in the ideation pool (22 in this research area, plus 10 in the neighbouring one) carries a **Sonnet** score,
and the inflation is largest on exactly the criterion that would tell you whether a design can detect its own effect.
Ranking those ideas by their recorded scores therefore selects for texts Sonnet found sound, not for studies that will
resolve anything — which is the same error the v4.2 round exposed, where 6.40 was awarded to a design whose own judges
called the primary endpoint unreachable.

## What this does and does not change
It does **not** change the design decomposition, which was computed Opus-against-Opus: v2 6.02 → v5.3 4.83, with
soundness the only criterion that rose (5.3 → 5.7) while clarity fell 3.0 and feasibility fell 2.3. The recommendation
to cut rather than to keep adding is unaffected. It does mean the lineage's Sonnet-era numbers (v1 6.70, v2 6.97,
v3 5.73, v4 6.02) are not comparable to the Opus rounds and should not be quoted in the same series again.
