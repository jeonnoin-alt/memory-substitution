# THRESHOLDS — pre-registered stopping criteria (proposal ③; fixed 2026-09-04 before implementation)

## T-A. Design-freeze threshold
Applied to the proposal loop (v4 → v5.2, `reviews/`): a finding is design-blocking iff acting on it changes an arm, a
claim's wording, a test or margin, or the split/seed structure. **Freeze when a round yields 0 blocking findings twice in
a row, or after round 3 (blockers resolved-or-descoped, logged).** Applied 2026-09-04: v5.1's one new blocking finding
(non-neutral denominator) resolved in v5.2 (decision-log rows 82–91); frozen. DESIGN.md is hashed into FREEZE.sha256
after the PI's freeze-blocking literature obligation (v5.2 collision check, item 1). After the hash: DEVIATIONS.md.

## T-B. Worth-running gates (go/no-go before the main grid) — numeric definitions in DESIGN.md §6
G-P0 smoke · G-P1 throughput ≥ 400 eps/h per replica · G0 dynamic range · K read-depth · G1 memory effect ≥ 5pt ·
G2 optimizer ≥ 3pt · G3 relevance ≥ 9pt (lower CI ≥ 5) · G3b provenance direction · G4 ladder brackets · G5 hygiene,
throughput ≥ 11,000 calls/h, DEFF/ICC republish · G6 denominator sufficiency + neutrality (S_test, pre-unblinding).
**Any gate fail → STOP, log numbers in GATES_LOG.md, take the pre-registered branch (DESIGN §6), report to the PI.**

## T-C. Experiment-complete threshold
DONE when: all Tier-0 rows (DESIGN §4) complete on S_test with the seed schedule; nulls complete; analyses A1–A8 computed
with the pre-registered tests; every claim labelled supported / refuted / inconclusive-by-MDE. Tier 1/2 and contingency
cuts follow DESIGN §4's orders; dropped = reported as unrun. Kill: any T-B gate fail; engine instability (>10% episode
failure after retry) persisting after one debugging pass — stop, checkpoint, report.

## T-D. Reproducibility checklist (must be TRUE at report time)
[ ] data: SHA256SUMS + PROVENANCE.md committed   [ ] splits: seeded script, task-closed, IDs in prereg/
[ ] partition: criterion values for all candidate splits in prereg/partition.json, computed before any episode
[ ] configs: every arm = one JSON in code/arms/, no CLI-only params   [ ] seeds: {11,23,37} logged per episode
[ ] episode logs: JSONL per arm with instruction/bank hashes + provenance tags, trace, tokens, outcome; append-only
[ ] serving: vllm 0.13.0 + launch flags logged   [ ] instruction/prompt texts: verbatim + sha256 in prereg/
[ ] artifacts: sha256 + P_train identity hash checked at load   [ ] analysis: single script → all tables
[ ] deviations: DEVIATIONS.md append-only   [ ] unrun arms listed as unrun
