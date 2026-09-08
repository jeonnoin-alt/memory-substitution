# Repackaging gate report
thresholds: idea-idea ≥ 0.6324006393551826, idea-prior ≥ 0.5505036413669586

## Idea clusters (3)
- hole_backfill_static_counterfactual | masked_harm_pairwise_removal | item_value_consumer_decomposition | stage_conditional_item_value | guilt_by_coretrieval | pairwise_removal_interaction_audit
- stale_item_score_lag_after_rule_change | per_item_loo_reliability_and_winners_curse
- responsible_item_attribution_benchmark | memory_failure_blame_item_vs_set

## Ideas whose nearest prior text is above threshold (23)
- **hole_backfill_static_counterfactual** sim 0.597 ← archive: archive:memory_item_value_reliability: Item Value Is Not an Item Property: A Generalizability Audit of Per-Item Utility 
- **masked_harm_pairwise_removal** sim 0.632 ← archive: archive:retrieved_set_disagreement_gate: Abstain When They Disagree: Harm from Organically Accumulated Agent Memory Live
- **masked_harm_pairwise_removal** sim 0.576 ← digest: arxiv:2607.10608: Agents consuming retrieved memory fall into a compliance trap: they adopt conflicting memory at the fi
- **item_value_consumer_decomposition** sim 0.622 ← archive: archive:instruction_conditioned_complementarity: What Does the Prompt Already Say? Instruction-Conditioned Complementari
- **item_value_consumer_decomposition** sim 0.558 ← brief: Measurement C (running): static per-type procedure prompts vs retrieval; a retrieved item whose value is fully captured
- **stale_item_score_lag_after_rule_change** sim 0.613 ← archive: archive:stall_triggered_injection: Retrieve When Stuck, Not When Starting: Injection Timing Sets the Sign of Experience 
- **stage_conditional_item_value** sim 0.674 ← archive: archive:stall_triggered_injection: Retrieve When Stuck, Not When Starting: Injection Timing Sets the Sign of Experience 
- **stage_conditional_item_value** sim 0.652 ← digest: arxiv:2607.10608: Agents consuming retrieved memory fall into a compliance trap: they adopt conflicting memory at the fi
- **guilt_by_coretrieval** sim 0.679 ← digest: arxiv:2608.02508: Trajectory-indexed memory utilities disperse feedback over a growing state space and jointly assigned 
- **guilt_by_coretrieval** sim 0.671 ← archive: archive:memory_budget_confound: One Item Is the Budget: Token Volume, Not Memory Content, Explains Both the Harm and the
- **admission_pruning_audit_random_holdout** sim 0.643 ← digest: arxiv:2606.03329: Rewarding a chunk-wise memory agent by how much its final memory raises the per-token log-likelihood o
- **admission_pruning_audit_random_holdout** sim 0.632 ← archive: archive:memory_surrogate_validity: Good Memory, Wrong Endpoint: Retrieval Recall, LLM-Judge Quality and Admission F1 Do 
- **admission_pruning_audit_random_holdout** sim 0.613 ← brief: 5. Measurement of per-item estimates (22 cards). Benchmarks score end-to-end outcomes only (Evo-Memory 2511.20857,
- **utility_half_life_consumer_swap** sim 0.562 ← archive: archive:memory_budget_confound: One Item Is the Budget: Token Volume, Not Memory Content, Explains Both the Harm and the
- **per_item_loo_reliability_and_winners_curse** sim 0.619 ← archive: archive:memory_item_value_reliability: Item Value Is Not an Item Property: A Generalizability Audit of Per-Item Utility 
- **per_item_loo_reliability_and_winners_curse** sim 0.605 ← digest: arxiv:2606.22844: Retrieval alone does not make a memory valid evidence for the current query, and restoring each fragme
- **responsible_item_attribution_benchmark** sim 0.7 ← archive: archive:stale_true_state_facts_redaction: Stale-True, Not Wrong: Episode-Specific State Facts Carry the Natural Harm of 
- **surrogate_endpoints_for_item_credit** sim 0.623 ← digest: s2:05c14833b7cee3408bf72d25cf0bee2c4b0d70b0: Scoring replay-buffer transitions by a weighted combination of reward magni
- **surrogate_endpoints_for_item_credit** sim 0.582 ← brief: 5. Measurement of per-item estimates (22 cards). Benchmarks score end-to-end outcomes only (Evo-Memory 2511.20857,
- **surrogate_endpoints_for_item_credit** sim 0.576 ← archive: archive:substitutes_not_complements: Substitutes, Not Complements: Clause-Level Evidence That Optimized Instructions Shr
- **pairwise_removal_interaction_audit** sim 0.605 ← archive: archive:retrieved_set_disagreement_gate: Abstain When They Disagree: Harm from Organically Accumulated Agent Memory Live
- **memory_failure_blame_item_vs_set** sim 0.664 ← digest: arxiv:2607.10608: Agents consuming retrieved memory fall into a compliance trap: they adopt conflicting memory at the fi
- **memory_failure_blame_item_vs_set** sim 0.661 ← archive: archive:stale_true_state_facts_redaction: Stale-True, Not Wrong: Episode-Specific State Facts Carry the Natural Harm of 

## Nearest neighbours (all ideas)
- hole_backfill_static_counterfactual: item_value_consumer_decomposition (0.654), slot_vs_item_credit_permutation (0.598), stage_conditional_item_value (0.595)
- masked_harm_pairwise_removal: stage_conditional_item_value (0.668), pairwise_removal_interaction_audit (0.644), guilt_by_coretrieval (0.595)
- item_credit_variance_decomposition: hole_backfill_static_counterfactual (0.569), surrogate_endpoints_for_item_credit (0.563), admission_pruning_audit_random_holdout (0.529)
- item_value_consumer_decomposition: hole_backfill_static_counterfactual (0.654), guilt_by_coretrieval (0.633), pairwise_removal_interaction_audit (0.61)
- stale_item_score_lag_after_rule_change: per_item_loo_reliability_and_winners_curse (0.7), hole_backfill_static_counterfactual (0.586), item_value_consumer_decomposition (0.562)
- stage_conditional_item_value: pairwise_removal_interaction_audit (0.674), masked_harm_pairwise_removal (0.668), guilt_by_coretrieval (0.637)
- guilt_by_coretrieval: stage_conditional_item_value (0.637), item_value_consumer_decomposition (0.633), masked_harm_pairwise_removal (0.595)
- admission_pruning_audit_random_holdout: surrogate_endpoints_for_item_credit (0.605), guilt_by_coretrieval (0.576), hole_backfill_static_counterfactual (0.57)
- utility_half_life_consumer_swap: guilt_by_coretrieval (0.574), item_value_consumer_decomposition (0.555), masked_harm_pairwise_removal (0.543)
- per_item_loo_reliability_and_winners_curse: stale_item_score_lag_after_rule_change (0.7), pairwise_removal_interaction_audit (0.618), guilt_by_coretrieval (0.593)
- responsible_item_attribution_benchmark: memory_failure_blame_item_vs_set (0.751), stage_conditional_item_value (0.578), per_item_loo_reliability_and_winners_curse (0.569)
- surrogate_endpoints_for_item_credit: admission_pruning_audit_random_holdout (0.605), guilt_by_coretrieval (0.573), item_credit_variance_decomposition (0.563)
- pairwise_removal_interaction_audit: stage_conditional_item_value (0.674), masked_harm_pairwise_removal (0.644), per_item_loo_reliability_and_winners_curse (0.618)
- memory_failure_blame_item_vs_set: responsible_item_attribution_benchmark (0.751), stage_conditional_item_value (0.591), pairwise_removal_interaction_audit (0.583)
- slot_vs_item_credit_permutation: hole_backfill_static_counterfactual (0.598), per_item_loo_reliability_and_winners_curse (0.582), guilt_by_coretrieval (0.546)
