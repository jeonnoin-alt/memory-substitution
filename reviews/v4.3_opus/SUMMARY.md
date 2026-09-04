# v4.3 judging, Opus 5 round (round 3 of the freeze rule) — reviews delivered 2026-09-03, aggregated 2026-09-04

Same prompt/schema/weights (`tools/judge_prompt_v4.3.md`), three independent general-purpose subagents, model opus.
The previous session ended after saving R1; R2 and R3 were recovered on 2026-09-04 from the subagent transcripts
on the NAS (`claude/projects/-home-work/41db1bba-…/subagents/`) and saved verbatim.

## Aggregate
**6.05 — borderline** (nov 6.0 / sig 5.0 / snd 6.7 / fea 7.0 / cla 6.3). R1 6/5/6/7/7, R2 6/5/7/7/6, R3 6/5/7/7/6.
Opus trajectory: v4 5.93 → v4.2 6.40 → v4.3 6.05. Novelty and soundness held; **significance fell to 5.0 across all three**
and clarity dropped (25 arms, 16 predictions, five test families read as "a program, not a result").

## What all three say (the round-3 design-blocking finding)
**The confirmatory endpoint is placed where the phenomenon is least likely to exist, and the design is gated in the wrong place.**
- Δ_info is a difference of two small quantities. The proposal's own priors for 27–32B agents in BM25 multi-hop QA are +0.6pt
  (this program's pilot) to +3.6pt (EvoAgentBench, ReasoningBank on Qwen3.5-27B, at a hand-written prompt). G7 needs ≥4pt
  from an *unseen* bank at an *optimized* instruction; Δ_info then needs ≥2pt on top. Modal outcome: the fallback branch.
- Winner's curse: A1 is the argmax over six pairings on S_dev (SE ≈2.4pt), so its S_test gain regresses; Risk 8 covered the
  inflation of S_raw but not the deflation of Δ_info's power (R3).
- R1 adds the structural version: random stratified halves are exchangeable, so B_a and B_b carry near-identical generic
  content and Δ_info can be ≈0 whether or not substitution is real; there is no bank-divergence statistic and no crossover-specific
  positive control. (R1's proposed fix — split halves by task type — would confound provenance with relevance and is refused;
  the correct reading is that the crossover identifies *episode-specific* absorption only, and generic absorption needs the
  level-matched control. See v4.4.)
- Limitation 12 (E1 is not where procedural memory is expected to be valuable) is turned against the design by R2 and R3:
  screen the environment too, or promote ALFWorld and buy the n it needs.
- Equivalence margins of ±4pt on 4pt effects make the compile-once and full-data claims unfalsifiable (R1, R3).
- The Short Hypothesis bundles five claims; the brief asks for one (R2).

## Other objections
| Objection | Who | v4.4 |
|---|---|---|
| Iso-cost arm appears in budgets and cut order but is defined nowhere | R1 | Defined as the compute-matched inference control (below) or dropped |
| Compute-matched inference control missing: give the no-memory agent memory's token/prefill budget as extra search calls or best-of-2 | R1, R3 | Added as a numbered Tier-0 cell (I0+3 calls; I1+3 calls) |
| Shuffled / irrelevant-content bank has no cell, n, seeds | R2 | Numbered Tier-0 cell at I0 and I1 (token-matched random items) |
| Oracle-retrieval upper bound to bound retrieval quality | R2 | Tier 1 (best item per instance chosen post hoc, descriptive) |
| Informed hand-written instruction (a human reads the bank) | R2 | Refused: not reproducible, and the PI writing it would be an unblinded author arm; the compiled block C is the reproducible version |
| I2_ab — co-adaptation at full data; the track is about coupling | R3 | Added, Tier 0 (2 seeds) |
| Promote 18c (re-distilled bank) to Tier 0 at n=1000 | R2 | Tier 1 at n=1000, 2 seeds; it defends an interpretation, not the claim |
| Sign consistency across crossover directions as a condition | R2 | Reported per direction with the interaction; consistency is a pre-registered *interpretation* rule, not a claim condition (R1 showed the condition splits true effects) |
| Cut arms (15, 18d, 20, 21, 23, 25) and put compute into seeds | R3 | Grid cut from 25 rows to 14 Tier-0/1 rows; Tier 2 reduced to three descriptive arms |
| EvoAgentBench verified only via a PI-supplied PDF; 2608.14036 appendix unopened; provenance-crossover literature unsearched | 3/3 | PDF text is committed with SHA256; the PI is not an interested party in the paper's sense but the point is logged; a targeted scan for held-out-episode / provenance crossovers in prompt optimization is added to the pre-freeze re-scan list |

## Decision under the freeze rule
This was round 3. The unanimous finding changes arm definitions, the claim's wording and the test structure, so it is
design-blocking and must be resolved or descoped before freeze. v4.4 is the resolution text; no further judging round is
owed by the rule, but one confirmatory Opus round is run for the record before DESIGN.md, and only a *new* design-blocking
finding there reopens the loop.
