# DESIGN v2 — Proposal ① v4.1 (consolidated; supersedes DESIGN_v1.md)
# Incorporates round-1 review: validity V1–V7, statistics S1–S8. This file is the single authority.

## 0. Claims
C1 CAUSE: outcome-bearing memory items trigger premature commitment; answer-redacted token/keyword-matched items do not.
C2 ANCHOR: pre-registered branch on whether a provenance-free candidate answer reproduces the truncation
   (≥60% → candidate-answer reframe; <30% → provenance-authority; else partial mediation).
C3 REPAIR LOCUS: hard floor Fh removes ≥50% of breaks preserving fixes; the same requirement via instruction slot
   (Fs; GEPA and MIPROv2 seeded with I*) recovers <1/3, with the citation audit separating say from do.
   Scoped to search-based in-context optimization.

## 1. Infrastructure (all local; network-forced amendments in prereg/AMENDMENTS.md)
Agent: Qwen3.5-27B bf16, thinking disabled, vLLM TP=1 per GPU, temp 0.7, max 8 calls/episode.
Distiller/redactor: Qwen3-32B (port 8001). Echo/compliance/citation annotator: EXAONE-4.0-32B (V2 role separation).
Replication model (decisive subset): EXAONE-4.0-32B (S6). Frontier probe + gold validation: deferred ≥09-01.
Corpus search tool: BM25 over the question's own dataset corpus. Memory retriever: MiniLM dense (gate G-7; BM25 fallback).

## 2. Data and splits (S8-corrected)
Pool = HippoRAG benchmark subsets: 1,000 questions per dataset (HotpotQA/MuSiQue/2Wiki; equal thirds), with
per-dataset retrieval corpora (9,811 / 11,656 / 6,119 passages). Provenance + SHA256 in data/.
Splits (seeded script make_splits.py, seed 20260824; **each split stratified 50% HotpotQA / 30% MuSiQue / 20% 2Wiki — the registered v4.1 environment weighting; the equal-thirds pool makes this feasible with a 1,700-question reserve**):
S_bank 400 · S_opt 150 · S_dev1 150 · S_dev2 100 · S_test 500 (total 1,300; IDs in prereg/splits.json).
The remaining 1,700 questions are a pre-registered RESERVE, untouched except for gate-triggered rebuilds (logged).

## 3. Bank
ExpeL-style distillation of solved S_bank episodes (agent runs bare M0 config on S_bank; Qwen3-32B distills
INSIGHT/PROCEDURE/OUTCOME items). Dedup. V7 decontamination: drop items whose source question's gold docs
title-match any S_test gold doc (count reported). M2 = per-item answer redaction (Qwen3-32B), token ±5%,
keyword-parity audited. M2i = answer swapped for an equally informative non-answer fact.

## 4. Arms — SINGLE AUTHORITATIVE TABLE (S4; supersedes every earlier bucket list)
| # | Arm | Memory | Instruction | Floor | Seeds | Split | Episodes |
|---|-----|--------|-------------|-------|-------|-------|----------|
| 1 | M0 | none | none | none | 11,23 | S_test | 1000 |
| 2 | M1 | bank-A top7 | none | none | 11,23 | S_test | 1000 |
| 3 | M2 | redacted top7 | none | none | 11,23 | S_test | 1000 |
| 4 | ANCHOR | own-guess answer | none | none | 11,23 | S_test | 1000 |
| 5 | M0+Fs | none | I* | soft | 11,23 | S_test | 1000 |
| 6 | M1+Fs | bank-A | I* | soft | 11,23 | S_test | 1000 |
| 7 | M2+Fs | redacted | I* | soft | 11,23 | S_test | 1000 |
| 8 | ANCHOR+Fs | own-guess | I* | soft | 11,23 | S_test | 1000 |
| 9 | M0+Fh | none | I* | hard | 11,23 | S_test | 1000 |
| 10 | M1+Fh | bank-A | I* | hard | 11,23 | S_test | 1000 |
| 11 | G1@M1 | bank-A | GEPA-evolved | soft | 11,23 | S_test | 1000 |
| 12 | G0@M0 | none | GEPA-evolved | soft | 11,23 | S_test | 1000 |
| 13 | M5 | bank-A top3 | none | none | 11,23 | S_test | 1000 |
| 14 | M5r | redacted top3 | none | none | 11,23 | S_test | 1000 |
| 15 | M8 | curated top7 | none | none | 11,23 | S_test | 1000 |
| 16 | M8+Fh | curated | I* | hard | 11,23 | S_test | 1000 |
| 17 | MIPROv2@M1 | bank-A | MIPRO-evolved | soft | 11,23 | S_test | 1000 |
| 18 | M2+Fh | redacted | I* | hard | 11 | S_test | 500 |
| 19 | ANCHOR+Fh | own-guess | I* | hard | 11 | S_test | 500 |
| 20 | M2i | info-matched top7 | none | none | 11 | S_test | 500 |
| 21 | ANCHOR-nh | no-hedge guess | none | none | 11 | S_test | 500 |
| 22 | M3 | answer-only top7 | none | none | 11 | S_test | 500 |
| 23 | M4 | decoy top7 | none | none | 11 | S_test | 500 |
| 24 | M6 | bank-A, +budget | none | none | 11 | S_test | 500 |
| 25 | G1+Fh | bank-A | GEPA-evolved | hard | 11 | S_test | 500 |
| 26 | I_B@M0 | none | I_B | soft | 11 | S_test | 500 |
| 27 | I_B@M1 | bank-A | I_B | soft | 11 | S_test | 500 |
| 28 | M0-CB (V1) | none, NO TOOLS | none | none | 11 | S_test | 500 |
| 29 | NULL: M0 seed 37 | none | none | none | 37 | S_test | 500 |
| 30 | NULL: M1 seed 37 | bank-A | none | none | 37 | S_test | 500 |
| 31 | NULL: M1+Fs seed 37 | bank-A | I* | soft | 37 | S_test | 500 |
| 32 | NULL: M1+Fh seed 37 | bank-A | I* | hard | 37 | S_test | 500 |
| 33 | EXAONE repl: M0,M1,M2,M1+Fs,M1+Fh | — | — | — | 11 | S_test[:300] | 1500 |
Bank-gen (S_bank, M0 cfg, seed 11): 400. Precheck (S_dev1/S_dev2 arms as gates require): ≤900.
Optimizer rollouts (GEPA×2 + MIPRO×1, 350 each on S_opt): 1,050.
**Grand total ≈ 28,350 agent episodes** (26,000 table rows + 400 bank-gen + ≤900 precheck + 1,050 optimizer; + deferred frontier probe 480).

## 5. Prompts and enforcement
I*, I_B verbatim + SHA256 in prereg/instructions.json|.sha256. Floor mechanics: agent must emit
`Evidence: "<quote>" | ...`; hard floor rejects unsupported finishes, forces ≥1 further search, cap +3 calls.
Optimizers seeded with I* verbatim; reflector = Qwen3-32B; training curves published; V5 semantic-fidelity check
on final instructions (discovery-loss vs compliance-gap interpretation pre-registered).

## 6. Gates (all numeric; measured before dependent arms; any fail → STOP and report)
G-P0 smoke 20 eps parse-clean · G-P1 throughput ≥400 eps/hr · G-P2 M0 EM ∈ [15,85]% on S_dev1(150, seed 11)
G-1 bank effect on S_dev1 (paired M0 vs M1, seed 11, n=150): fixes ≥6 AND breaks ≥6 (counts, no CI)
G-2 compliance headroom on S_dev2 (M0+Fs, n=100): ≥65 compliant
G-3 non-echo errors on S_dev1 M1 breaks: ≥20% non-echo AND ≥10 absolute
G-4 stored-record audit: ≥70% of items retrieved on S_dev1 breaks are truthful, no verification claims
G-5 parametric rate (M0-CB on S_test) ≤60% · G-6 M2 leakage ≤10% (human check on 150 items sampled uniformly from S_bank's redacted bank items)
G-7 memory-retriever relevance ≥60% (S_dev2, 100-question audit) · G-8 Fh unparseable rate <5% (S_dev2 WITH Fh engaged, full reject/retry loop)

## 7. Statistics (S1–S3, S7 fixed)
METRIC: EM is the gated/primary metric for every claim; F1 descriptive.
SUPERIORITY: exact McNemar on paired fix/break tables. EQUIVALENCE: TOST = 90% instance-level bootstrap CI
(10k resamples) of the paired EM difference within ±4pt (stats.py::tost). Deltas always with fix/break decomposition.
PRIMARY ENDPOINT (S2 fix): M0 vs M1 (arms 1 vs 2) is the single pre-registered primary test at alpha=.05,
outside all Holm families. HOLM FAMILIES (fixed now): F-A2 {comp under Fs: M0−M1, M2−M1, ANCHOR−M1, I_B@M0−I_B@M1}
· F-A4 {break-reduction vs M1: Fs, G1, MIPROv2, M8, Fh, G1+Fh, M6} · F-A5 {vs M1: M2, M2i, M3, M4, M5, M5r}
· F-A6 {the single interaction} · F-slice {pre-registered slices}. ORPHAN ARMS declared descriptive-only, no
formal claim: G0@M0, M2+Fh, ANCHOR+Fh, M8+Fh; ANCHOR-nh serves only the pre-registered C2 branch-guard rule;
M0-CB serves only gate G-5. Each family Holm-corrected separately.
NULL FLOOR (S1): the treatment-free reference = same-arm cross-seed aggregate |ΔEM| for the four replicated arms
(#29–32 vs their seed-11 runs), plus M0 seed 23 vs 11. An effect is claimable only if its |Δ| exceeds BOTH its
test threshold AND the maximum of these five treatment-free deltas on the same endpoint.
MDE (S7): headline MDEs at n=500 stand; A3/A6 subgroup MDEs are recomputed at PILOT-observed subgroup n
(breaks, non-echo counts from S_dev1) with difference-of-proportions formulas, and every subgroup claim reports
achieved-MDE alongside. Pre-declared: subgroup effects below achieved-MDE are inconclusive, not null.

## 8. Analyses A1–A6, branch logic, drop order, partial-completion — unchanged from v4.1 spec
(see ai_scientist/ideas/memory_shortcutting_v4.md and DESIGN_v1.md §8–§10; drop order: M8+Fh → I_B@M0 → M6 →
ANCHOR-nh → EXAONE repl; never drop arms 1–14.)

## 9. Round-2 validity fixes (2026-08-24; six blocking, all adopted)
R2-V1 Minimal-pair selection pinning: top-k selection is computed ONCE per question on bank-A original embeddings
      and held identical across M1/M2/M2i/M5/M5r/ANCHOR; only payload text varies (implemented in memory.py::_swap_payload).
R2-V2 G-8 is measured WITH Fh engaged on S_dev2 (full reject/retry loop), not under Fs.
R2-V3 ANCHOR items are format/length-matched to bank OUTCOME lines ("The answer was '<X>'." → hypothesis phrasing),
      differing only in source attribution; guess correctness rate is reported and the C2 branch analysis is
      additionally reported conditioned on guess-correct instances.
R2-V4 Arm 33's n=300 subset is a stratified 50/30/20 draw from S_test, IDs appended to prereg/splits.json.
R2-V5 V7-style gold-doc decontamination extended to S_opt vs S_test (overlap counts reported; overlapping S_opt
      questions replaced from RESERVE before optimizer rollouts).
R2-V6 Arm 33 (EXAONE replication) claims are restricted to EM/F1 outcomes; say-vs-do mechanism conclusions are NOT
      drawn for the replication subset (annotator would be self-grading there).

## 10. Round-3 (final) fixes — resolved before freeze per THRESHOLDS T-A cap rule
F1a M3 construction (§3 addition): Qwen3-32B keeps each item's OUTCOME line verbatim, deletes INSIGHT and
    PROCEDURE, pads with neutral task-generic filler to ±5% tokens (mirror of M2's operation).
F1b Selection pinning extended: the computed-once bank-A top-k selection is shared by M1/M2/M2i/M3/M5/M5r and the
    top-1 selection by ANCHOR/ANCHOR-nh. **M4 is intentionally NOT pinned**: its manipulated factor IS selection
    relevance (items retrieved for a different query, token-matched) — stated here so the exclusion is by design.
F2  G-8 protocol: single wording everywhere — measured on S_dev2 with Fh engaged (full reject/retry loop).
F3  C2 branch metric (formula): R_A = [mean paired per-instance (calls(M0) − calls(ANCHOR))] /
    [mean paired per-instance (calls(M0) − calls(M1))], computed on S_test, seeds 11+23 pooled, full paired set;
    branch thresholds ≥0.60 / <0.30 apply to R_A. Secondary consistency readout (reported, not branch-deciding):
    break-overlap ratio |breaks(M1) ∩ breaks(ANCHOR)| / |breaks(M1)|. The ANCHOR-nh guard applies to R_A: if
    |R_A − R_A(nh)| > 0.15, the branch is decided on R_A(nh).
