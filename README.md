# memory-substitution

**Is Your Agent's Memory Just an Un-Optimized Prompt?** — measuring how much of a retrieved-experience
memory bank's value survives once a prompt optimizer is given the same training episodes.

This repo executes **proposal ③** (`memory_or_instruction`; frozen text: `reference/proposal_v5.2.md`, lineage from v2 6.97) from the agent-memory ×
prompt-optimization ideation program run in `AI-Scientist-v2`. Lineage: v1 6.73 → **v2 6.97** → v3 5.73
("When Is a Retriever Decorative?", superseded). The HANDOFF that started this work is `HANDOFF.md`.

## Core question
A memory bank B (ExpeL-style, distilled from training episodes, retrieved top-k per query) and an
instruction I1 (GEPA-optimized on the *same* episodes, never seeing the bank) are two containers for the
same information. Primary endpoint — the substitution ratio:

    S = 1 − [acc(I1×M1) − acc(I1×M0)] / [acc(I0×M1) − acc(I0×M0)]

plus a frozen offline-compiled instruction C (no retrieval), a raw few-shot control R, a length control I3,
and a non-compilable positive-control bank B-dup that must show S < 0.25. Full text: `reference/proposal_v2.md`.

## Layout
| Path | What |
|---|---|
| `HANDOFF.md` | Mission (reproduce → refine → run), reviewer objections to answer, lab measurement rules |
| `reference/proposal_v{1,2,3}.md` | Proposal texts (11 IDEA_FIELDS). v2 is the one being executed |
| `reference/reviews_v{1,3}.md` | Reviewer objections (v2's own reviews were not persisted) |
| `reference/REPRO_stage1_2026-08-24.md` | Stage-1 reproduction notes and artifact-integrity findings |
| `reference/track_brief.md` | The research-track brief (scope, resource constraints) |
| `reference/judging_constants.md` | REVIEW_SCHEMA / REVIEW_SYSTEM / SCORE_WEIGHTS verbatim from `ideate.py` |
| `reference/shortcutting_v4/` | Frozen snapshot of proposal ①'s design, code, prereg logs, bank, abstract — the reusable infrastructure and the prior result that constrains this design |
| `DESIGN.md` | (Stage 2/3) the single design authority, frozen by hash before any test-set episode |
| `prereg/` | Splits, instruction texts + SHA256, thresholds, gates log, deviations log, amendments |
| `code/` | (Stage 3) agent, env, memory, bank builder, optimizer driver, stats — adapted from `reference/shortcutting_v4/code` |
| `data/`, `runs/` | Not committed (see their READMEs) |
| `analysis/` | Tables/figures produced by a single script from `runs/` JSONL |
| `tools/` | Harness-side helpers (zero-credit judging, literature scan) |

## Status
- 2026-09-03: repo created. Stage 1 (reproduce) done earlier (see `reference/REPRO_stage1_2026-08-24.md`).
  Stage 2 run the same day: literature scan (`reference/litscan_2026-09-03.md`, 32 verified IDs, EvoAgentBench
  PDF read), then v4 → v4.1 → v4.2 → v4.3 with harness judging after each round
  (`reviews/`: v4 sonnet 6.02, v4 opus 5.93, v4.2 opus 6.40, v4.3 opus 6.05; every round's objections and the
  answers are in the decision log at the top of each `reference/proposal_v4.x.md`).
- 2026-09-04: v4.3's round-3 finding (the confirmatory endpoint was placed where the phenomenon is least likely
  to exist, gated in the wrong place, and equivalence margins wider than the effects) resolved in
  **`reference/proposal_v4.4.md`** — the resolution text under the freeze rule: primary endpoint is now
  *absorption beyond headroom* (memory's gain at the optimized instruction vs. at an accuracy-matched
  information-free instruction, full data), the provenance crossover is the specificity probe with a planted
  control, environment joins agent and bank format as a split-sample screening axis, completion mechanics are
  held fixed across all arms (proposal ①'s 2026-09-04 finding), and the grid is cut to 11 must-ship rows.
- Constraints carried into DESIGN.md: proposal ① measured the ExpeL bank at **+0.6pt bare / +2.4pt with fair
  completion mechanics on Qwen3.5-27B** and +7.7pt on gpt-oss-120b; EvoAgentBench reports +3.6 (ReasoningBank)
  and +1.2 (GEPA) on Qwen3.5-27B. Gates are set from these numbers, not from the literature's ≥10pt.
- 2026-09-04, confirmatory Opus round on v4.4: **5.83** (`reviews/v4.4_opus/`). New design-blocking findings — the
  hand-written headroom family does not identify Δ_abs, the bank is off-policy at the optimized instruction (distilled
  under I0), and the 2pt threshold sits below the MDE and the null floor. **Not frozen.** The reviewers' third-round-in-a-row
  point stands: on 27–32B agents in multi-hop QA the memory effect is 0–4pt, so any decomposition is at the noise floor.
  `reviews/v4.4_opus/SUMMARY.md` lays out the three ways forward (A: move the confirmatory environment to one with
  recurring procedural structure, e.g. ALFWorld with held-out training games; B: re-scope to the memory-null/headroom
  report; C: v4.5 in E1 with the instrument fixes) and recommends A pending an ALFWorld feasibility check. Awaiting the PI.
- 2026-09-04 (later): the PI chose **direction A** (ALFWorld primary, no API key, local models only) and asked for the
  loop to run automatically: an Opus author agent writes each version from a brief (`tools/author_brief_v5*.md`), three
  Opus judges score it. v5 5.25 → **v5.1 5.57** (`reviews/v5.1_opus/`). The v5.1 round's one new design-blocking
  finding (the ratio endpoint's denominator Inner(I_oth) is not neutral: a mis-specified off-type instruction is
  repaired by the on-type bank, inflating A) is answered in **`reference/proposal_v5.2.md`, the frozen proposal text**
  (rows 82–91 of its decision log): A0 with the I0\* denominator is co-primary, I_all × {B_own, B_oth} and B′_own join
  Tier 0, M_shuf is promoted, the reserve is spent in a stated order, prediction 6 becomes a TOST, AutoManual/AutoGuide
  are cited as the pre-2026 ALFWorld precedents. v5.2 is not re-judged (THRESHOLDS T-A: round-3 blockers resolved or
  descoped, logged, then freeze). ALFWorld feasibility on this node: `reference/alfworld_feasibility_2026-09-04.md`.
- **Stage 3 next:** `DESIGN.md` from v5.2, with two data-forced amendments found on 2026-09-04 — ALFWorld's 3,553
  training games are trials of **1,465 unique tasks** (allocate and cluster by task), and clean/cool/heat exist only in
  kitchens (the type partition also partitions rooms) — then code adapted from `reference/shortcutting_v4/code`.
  DESIGN.md is hashed only after the PI runs the freeze-blocking literature obligation (provenance-crossover search).
- The GitHub repo was renamed to `memory-substitution`; the old `experiments-mem` URL redirects.

## House rules (from HANDOFF)
Paired within-instance comparisons · exact McNemar + Holm with fix/break decomposition · TOST for every
"no difference" claim · null replicates at a different seed · MDE stated before running · pre-registered
drop order · unrun arms are "unrun", never nulls · every arXiv ID in a verification appendix ·
no keys in chat or commits · public data only.
