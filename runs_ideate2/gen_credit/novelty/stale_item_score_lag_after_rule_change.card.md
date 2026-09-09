=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: stale_item_score_lag_after_rule_change — How Long Does a Stale Item Stay Valuable? Score Lag and Co-Retrieval Contamination After a Manufactured Rule Change

- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.53 · hf · found via agent/methods
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2608.25553 · 2026-08-28 · preprint · sim 0.51 · hf · found via agent
  When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
  Provenance links keep the evidence behind an inherited belief reachable; an agent with a verification budget must still choose which links to inspect. We study a consolidated memory that states a decision constraint and whose source record has since been superseded by a record that withdraws it: provenance is immutable, the current record has changed, and the memory is stale. In a controlled six-memory scenario with a budget of two records, sixteen language models rarely re-verified a constraint
- arxiv:2605.17639 · 2026-05-17 · preprint · sim 0.50 · hf · found via agent
  Temporal Decay of Co-Citation Predictability: A 20-Year Statute Retrieval Benchmark from 396M Ukrainian Court Citations
  Co-citation structure is widely assumed to provide stable retrieval signal in legal information systems. We test this assumption longitudinally by constructing UA-StatuteRetrieval, a benchmark that measures co-citation predictability across 20 annual snapshots (2007-2026) of 396 million codex citations from 101 million Ukrainian court decisions. Using a leave-one-out protocol over the full bipartite citation graph, we find that Adamic-Adar MRR declines 33% on a fixed set of articles (from 0.43 t
- arxiv:2607.18722 · 2026-07-21 · preprint · sim 0.46 · hf · found via agent/mechanism_home/methods
  Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning
  Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but staleness is an inevitable byproduct compounded by policy lag, engine delays, and mixture-of-experts routing. From a trust-region perspective, this mismatch is critical: training-inference divergence governs approximation error in finite-horizon bounds, whereas PPO clipping only gates sampled outward updates, acting as a sampled surrogate rather than a full-policy constraint. As a resu
- arxiv:2603.02473 · 2026-04-12 · preprint · sim 0.42 · hf · found via agent
  Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
  Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval
- arxiv:2605.06132 · 2026-05-07 · preprint · sim 0.42 · hf · found via agent
  MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval
  In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory. Most systems adopt the "retrieve-then-rerank" two-stage paradigm, but generic reranking models rely on semantic similarity matching and lack genuine reasoning capabilities, leading to a problem where recalled results are semantically highly relevant yet do not contain the key information needed to answer the question. This deficiency manifests in memory scenarios as three spe
- arxiv:2604.27306 · 2026-04-30 · Annual International ACM SIGIR Conference on Research and Development in Information Retrieval · sim 0.42 · s2 · found via baseline
  NuggetIndex: Governed Atomic Retrieval for Maintainable RAG
  Retrieval-augmented generation (RAG) systems are frequently evaluated via fact-based metrics, yet standard implementations retrieve passages or static propositions. This unit mismatch between evaluation and retrieval objects hinders maintenance when corpora evolve and fails to capture superseded facts or source disagreements. We propose NuggetIndex, a retrieval system that stores atomic information units as managed records, so called nuggets. Each record maintains links to evidence, a temporal v
- arxiv:2607.12893 · 2026-07-14 · preprint · sim 0.41 · hf · found via agent
  MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations
  Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values
- arxiv:1811.11043 · 2018-11-27 · preprint · sim 0.41 · hf · found via mechanism_home
  Rotting bandits are not harder than stochastic ones
  In stochastic multi-armed bandits, the reward distribution of each arm is assumed to be stationary. This assumption is often violated in practice (e.g., in recommendation systems), where the reward of an arm may change whenever is selected, i.e., rested bandit setting. In this paper, we consider the non-parametric rotting bandit setting, where rewards can only decrease. We introduce the filtering on expanding window average (FEWA) algorithm that constructs moving averages of increasing windows t
- arxiv:2510.08109 · 2025-10-09 · arXiv.org · sim 0.40 · s2 · found via baseline
  VersionRAG: Version-Aware Retrieval-Augmented Generation for Evolving Documents
  Retrieval-Augmented Generation (RAG) systems fail when documents evolve through versioning-a ubiquitous characteristic of technical documentation. Existing approaches achieve only 58-64% accuracy on version-sensitive questions, retrieving semantically similar content without temporal validity checks. We present VersionRAG, a version-aware RAG framework that explicitly models document evolution through a hierarchical graph structure capturing version sequences, content boundaries, and changes bet

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2606.17664 · 2026-06-16 · sim 0.40 · via baseline — Temporal Preference Optimization for Unsupervised Retrieval
- arxiv:2604.21432 · 2026-04-23 · sim 0.38 · via agent/mechanism_home — A single algorithm for both restless and rested rotting bandits
- arxiv:2601.03715 · 2026-01-07 · sim 0.38 · via mechanism_home — R^3L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification
- arxiv:2605.23497 · 2026-05-22 · sim 0.37 · via baseline — Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering
- arxiv:2305.19036 · 2023-05-30 · sim 0.37 · via mechanism_home — Delayed Bandits: When Do Intermediate Observations Help?

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
