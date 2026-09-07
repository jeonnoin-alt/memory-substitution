=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: memory_surrogate_validity — Good Memory, Wrong Endpoint: Retrieval Recall, LLM-Judge Quality and Admission F1 Do Not Rank Agent Experience Memories by Execution Success

- arxiv:2605.06132 · 2026-05-07 · preprint · sim 0.66 · hf
  MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval
  In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory. Most systems adopt the "retrieve-then-rerank" two-stage paradigm, but generic reranking models rely on semantic similarity matching and lack genuine reasoning capabilities, leading to a problem where recalled results are semantically highly relevant yet do not contain the key information needed to answer the question. This deficiency manifests in memory scenarios as three spe
- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.65 · hf
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2603.02473 · 2026-04-12 · preprint · sim 0.65 · hf
  Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
  Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval
- arxiv:2607.17621 · 2026-07-20 · preprint · sim 0.63 · hf
  Mechanistic Attention Guidance for Agent Memory Refinement
  Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections. However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored. This limitation can lead to unreliable error attribution and hallucinated memory modifications. In this work, we show that retrieval-head attention provides a mechanistic signal for revealing se
- arxiv:2604.20006 · 2026-04-21 · preprint · sim 0.61 · hf
  From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents
  Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change. However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent knowledge updates. We introduce Memora, a long-term memory benchmark spanning weeks to months long user conversations. The benchmark
- arxiv:2512.20237 · 2025-12-23 · preprint · sim 0.60 · hf
  MemR^3: Memory Retrieval via Reflective Reasoning for LLM Agents
  Memory systems have been designed to leverage past experiences in Large Language Model (LLM) agents. However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. From this observation, we build memory retrieval as an autonomous, accurate, and compatible agent system, named MemR^3, which has two core mechanisms: 1) a router that selects among retrieve, reflect, and answer actions to optimiz
- arxiv:2607.12893 · 2026-07-14 · preprint · sim 0.59 · hf
  MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations
  Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values
- arxiv:2605.12493 · 2026-05-12 · preprint · sim 0.59 · hf
  LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for 
- arxiv:2602.16313 · 2026-02-18 · preprint · sim 0.59 · hf
  MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
  Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment,
- arxiv:2607.24097 · 2026-07-27 · preprint · sim 0.59 · hf
  MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents
  Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. We propose MemChain, a trainable post-retrieval memory policy that transforms retrieved candidates into answer-facing ac

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
