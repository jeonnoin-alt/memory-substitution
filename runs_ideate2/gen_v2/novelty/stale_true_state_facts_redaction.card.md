=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: stale_true_state_facts_redaction — Stale-True, Not Wrong: Episode-Specific State Facts Carry the Natural Harm of Agent Experience Memory, and Fact-Level Redaction Beats Abstention

- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.58 · hf
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2608.25553 · 2026-08-28 · preprint · sim 0.53 · hf
  When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
  Provenance links keep the evidence behind an inherited belief reachable; an agent with a verification budget must still choose which links to inspect. We study a consolidated memory that states a decision constraint and whose source record has since been superseded by a record that withdraws it: provenance is immutable, the current record has changed, and the memory is stale. In a controlled six-memory scenario with a budget of two records, sixteen language models rarely re-verified a constraint
- arxiv:2605.29463 · 2026-05-31 · preprint · sim 0.52 · hf
  Honest Lying: Understanding Memory Confabulation in Reflexive Agents
  Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR
- arxiv:2602.14080 · 2026-02-15 · preprint · sim 0.51 · hf
  Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality
  Standard factuality evaluations of LLMs treat all errors alike, obscuring whether failures arise from missing knowledge (empty shelves) or from limited access to encoded facts (lost keys). We propose a behavioral framework that profiles factual knowledge at the level of facts rather than questions, characterizing each fact by whether it is encoded, and then by how accessible it is: cannot be recalled, can be directly recalled, or can only be recalled with inference-time computation (thinking). T
- arxiv:2605.12978 · 2026-05-13 · preprint · sim 0.50 · hf
  Useful Memories Become Faulty When Continuously Updated by LLMs
  Learning from past experience benefits from two complementary forms of memory: episodic traces -- raw trajectories of what happened -- and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising self-improving agents without parameter updates. Yet we find that such consolidated m
- arxiv:2608.11772 · 2026-08-12 · preprint · sim 0.50 · hf
  Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction
  Self-correction is particularly useful when a failure constrains the next repair. Coding agents benefit from this property because compilers, tests, and execution traces turn many failures into typed recovery signals, but broad language-agent tasks often expose only a coarse task failure. This creates a tension for generic recovery playbooks: they broaden the agent's context precisely when the system needs a narrower repair interface, mixing incompatible signals for invalid actions, missing proc
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.46 · hf
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2607.19749 · 2026-07-22 · preprint · sim 0.45 · hf
  The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL
  Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? Under never-clear replay, pre-registered component-level probes (n=3 seeds throughout) show that the world model retains essentially everything measurable about old tasks -- reward discrimi
- arxiv:2608.04574 · 2026-08-05 · preprint · sim 0.45 · hf
  When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs
- arxiv:2606.25852 · 2026-06-24 · preprint · sim 0.44 · hf
  Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
  Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress insi

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
