# Ideation pool re-judged under Opus — 2026-09-04

All 27 deduplicated ideas from the AI-Scientist-v2 ideation pools, re-scored with the **same** harness prompt,
schema and weights (novelty .3 / significance .25 / soundness .25 / feasibility .1 / clarity .1, worst verdict
wins) used for the v2 calibration and every v4/v5 round. Three independent Opus judges per idea, 81 reviews.
Each idea was judged against its own research-area brief. Prompts: `tools/ideation_prompts/<name>.md`;
fields: `reference/ideation/<name>.json`; reviews: `reviews/ideation/<name>_opus/`.

**Read this as a calibration of the recorded Sonnet scores, not as a shortlist.** The v2 control run showed
Sonnet scores the same text about a point higher than Opus, concentrated in soundness, and these are
undeveloped ideation texts: the measured decay from an ideation text to a developed, scanned, costed proposal
was another 1.2 points (v2 6.02 → v5.3 4.83, Opus against Opus).

| # | Opus | verdict | Sonnet | Δ | nov | sig | snd | fea | cla | idea | area |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **6.12** | borderline | 6.7 | -0.58 | 5.7 | 6.0 | 5.7 | 7.0 | 8.0 | `memory_item_value_reliability` | memory x optimizer |
| 2 | **6.07** | borderline | 6.17 | -0.10 | 5.7 | 6.0 | 5.3 | 7.3 | 8.0 | `provenance_gap_selection_not_authorship` | memory x optimizer |
| 3 | **6.00** | borderline | 6.77 | -0.77 | 5.3 | 6.0 | 6.0 | 6.0 | 8.0 | `compile_dont_retrieve` | memory x optimizer |
| 4 | **5.92** | borderline | 6.7 | -0.78 | 5.0 | 6.3 | 5.3 | 6.7 | 8.3 | `memory_or_instruction` | memory x optimizer |
| 5 | **5.87** | borderline | 5.8 | +0.07 | 5.3 | 5.7 | 5.7 | 6.3 | 8.0 | `failure_signature_routing` | transferable prompt opt |
| 6 | **5.85** | borderline | 6.3 | -0.45 | 5.3 | 5.7 | 5.3 | 7.0 | 8.0 | `collection_policy_coupling_collapse` | memory x optimizer |
| 7 | **5.82** | borderline | 6.58 | -0.76 | 5.0 | 5.7 | 5.3 | 8.0 | 7.7 | `instruction_conditioned_complementarity` | memory x optimizer |
| 8 | **5.77** | borderline | 6.15 | -0.38 | 5.0 | 6.0 | 5.3 | 6.3 | 8.0 | `coadaptation_transplant_ccr` | memory x optimizer |
| 9 | **5.75** | borderline | 5.73 | +0.02 | 5.0 | 6.0 | 5.0 | 7.0 | 8.0 | `decorative_retriever` | memory x optimizer |
| 10 | **5.72** | borderline | 6.88 | -1.16 | 5.0 | 6.0 | 5.0 | 6.7 | 8.0 | `memory_induced_shortcutting` | memory x optimizer |
| 11 | **5.72** | borderline | 6.4 | -0.68 | 5.3 | 6.0 | 5.0 | 7.0 | 6.7 | `memory_vetoes_instruction_slot` | memory x optimizer |
| 12 | **5.68** | borderline | 6.45 | -0.77 | 5.0 | 6.0 | 5.0 | 6.3 | 8.0 | `coverage_currency_coupling` | memory x optimizer |
| 13 | **5.63** | borderline | 6.58 | -0.95 | 5.0 | 5.7 | 5.0 | 6.7 | 8.0 | `memory_budget_confound` | memory x optimizer |
| 14 | **5.47** | borderline | 6.42 | -0.95 | 4.7 | 5.0 | 5.0 | 7.7 | 8.0 | `substitutes_not_complements` | memory x optimizer |
| 15 | **5.45** | reject | 6.0 | -0.55 | 5.0 | 5.3 | 4.3 | 7.3 | 8.0 | `counterfactual_memory_screening_under_selection_noise` | memory x optimizer |
| 16 | **5.45** | borderline | 5.95 | -0.50 | 4.0 | 5.0 | 6.0 | 7.0 | 8.0 | `memory_dropout_coadaptation` | memory x optimizer |
| 17 | **5.40** | borderline | 5.7 | -0.30 | 4.0 | 5.0 | 5.7 | 7.3 | 8.0 | `coverage_selection_division_of_labour` | memory x optimizer |
| 18 | **5.38** | borderline | 5.95 | -0.57 | 4.3 | 5.7 | 5.3 | 5.3 | 8.0 | `clause_level_portability` | transferable prompt opt |
| 19 | **5.38** | borderline | 6.45 | -1.07 | 4.7 | 5.3 | 5.0 | 6.0 | 8.0 | `commit_then_consult_slot_discipline` | memory x optimizer |
| 20 | **5.35** | borderline | 5.67 | -0.32 | 4.0 | 5.0 | 5.3 | 7.7 | 8.0 | `breadth_routed_memory` | memory x optimizer |
| 21 | **5.33** | borderline | 5.97 | -0.64 | 4.3 | 5.3 | 6.0 | 4.0 | 8.0 | `playbook_transfer` | transferable prompt opt |
| 22 | **5.30** | reject | 5.9 | -0.60 | 4.7 | 5.0 | 5.7 | 4.7 | 7.7 | `meta_prompt_generalization` | transferable prompt opt |
| 23 | **5.27** | borderline | 5.83 | -0.56 | 3.7 | 5.0 | 5.7 | 7.0 | 8.0 | `action_prior_imprinting` | memory x optimizer |
| 24 | **5.22** | borderline | 6.12 | -0.90 | 4.0 | 5.3 | 5.0 | 6.3 | 8.0 | `optimizer_substitutes_for_memory_scaffold` | memory x optimizer |
| 25 | **5.18** | borderline | 5.67 | -0.49 | 4.7 | 5.3 | 4.3 | 6.0 | 7.7 | `query_agnostic_curation_ceiling` | memory x optimizer |
| 26 | **5.05** | reject | 5.47 | -0.42 | 4.0 | 5.0 | 4.7 | 7.0 | 7.3 | `memory_volume_amplifies_optimizer_curse` | memory x optimizer |
| 27 | **5.00** | reject | 5.53 | -0.53 | 4.3 | 4.7 | 5.3 | 4.0 | 8.0 | `allocation_prior_transfer` | transferable prompt opt |

**Sonnet → Opus:** mean -0.58, median -0.57, range -1.16 to +0.07 over 27 ideas.
**Novelty under Opus:** mean 4.74, max 5.7. No idea in the pool clears 6 on novelty.
**Verdicts:** 4 reject, 23 borderline, 0 accept-worthy.

## Caveats that matter for using this table
- **Five ideas lack a Preprint Collision Check field** (`playbook_transfer`, `clause_level_portability`,
  `meta_prompt_generalization`, `failure_signature_routing`, `allocation_prior_transfer`): they come from an
  ideation run that predated that field, so their judges saw an empty collision section and penalized it. Their
  novelty scores are not comparable to the other 22.
- `memory_or_instruction` here is the **agent_memory_v2-pool variant** (Sonnet 6.7), not the top-4 text that
  scored 6.97 and is the basis of `reference/proposal_v2.md`; that one is scored separately in `reviews/v2_opus`
  (6.02) and `reviews/v2_sonnet` (7.10).
- `memory_induced_shortcutting` is proposal ①, already being executed by another session.
- Scores are for **undeveloped ideation texts**. Ranking by them selects for what a judge finds sound on a page,
  which the v4.2 round showed is not the same as a design that can detect its own effect.
