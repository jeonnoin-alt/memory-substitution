# memory-substitution

**Is Your Agent's Memory Just an Un-Optimized Prompt?** — measuring how much of a retrieved-experience
memory bank's value survives once a prompt optimizer is given the same training episodes.

This repo executes **proposal ③ v2** (`memory_or_instruction`, score 6.97) from the agent-memory ×
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
- 2026-09-03: repo created. Stage 1 (reproduce) done earlier (see `reference/REPRO_stage1_2026-08-24.md`);
  Stage 2 (fresh literature scan → v4 text answering the objections → ≥3-reviewer judging) next.
- Constraint discovered before design: proposal ① measured the ExpeL bank's effect on this node's agents —
  **+0.6pt (equivalent to none) for Qwen3.5-27B, +7.7pt for gpt-oss-120b**. v2's precheck gate requires
  ≥10pt. Agent choice and gate threshold must be settled in DESIGN.md before anything runs.

## House rules (from HANDOFF)
Paired within-instance comparisons · exact McNemar + Holm with fix/break decomposition · TOST for every
"no difference" claim · null replicates at a different seed · MDE stated before running · pre-registered
drop order · unrun arms are "unrun", never nulls · every arXiv ID in a verification appendix ·
no keys in chat or commits · public data only.
