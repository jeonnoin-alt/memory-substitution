=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: aggregate_or_comply — Aggregate or Comply: Compiled Playbooks, Whole-Bank Context and Top-k Retrieval Under a Manipulated Contamination Rate of the Experience Bank

- arxiv:2602.02579 · 2026-02-05 · preprint · sim 0.53 · hf · found via agent
  ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation
  The prefill stage of long-context Retrieval-Augmented Generation (RAG) is severely bottlenecked by computational overhead. To mitigate this, recent methods assemble pre-calculated KV caches of retrieved RAG documents (by a user query) and reprocess selected tokens to recover cross-attention between these pre-calculated KV caches. However, we identify a fundamental "crowding-out effect" in current token selection criteria: globally salient but user-query-irrelevant tokens saturate the limited rec
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.53 · hf · found via agent/methods
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2608.20202 · 2026-08-20 · preprint · sim 0.51 · hf · found via methods
  MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use
  Memory has become a key component of large language models, enabling them to retain information and learn from long-term interactions. However, existing memory benchmarks mainly evaluate whether information is correctly extracted, stored, and retrieved, while largely overlooking how retrieved memories reshape model reasoning and affect performance on the current task. We identify memory-induced cognitive traps: even faithfully recorded and semantically relevant memories can distort model reasoni
- arxiv:2407.10670 · 2024-07-15 · preprint · sim 0.50 · hf · found via agent
  Enhancing Retrieval and Managing Retrieval: A Four-Module Synergy for
  Improved Quality and Efficiency in RAG Systems
  Retrieval-augmented generation (RAG) techniques leverage the in-context learning capabilities of large language models (LLMs) to produce more accurate and relevant responses. Originating from the simple 'retrieve-then-read' approach, the RAG framework has evolved into a highly flexible and modular paradigm. A critical component, the Query Rewriter module, enhances knowledge retrieval by generating a search-friendly query. This method aligns input questions more closely with the knowledge base. O
- arxiv:2605.13941 · 2026-05-13 · preprint · sim 0.50 · hf · found via methods
  EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents
  Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full r
- arxiv:2505.17206 · 2025-05-22 · preprint · sim 0.50 · hf · found via agent
  FB-RAG: Improving RAG with Forward and Backward Lookup
  The performance of Retrieval Augmented Generation (RAG) systems relies heavily on the retriever quality and the size of the retrieved context. A large enough context ensures that the relevant information is present in the input context for the LLM, but also incorporates irrelevant content that has been shown to confuse the models. On the other hand, a smaller context reduces the irrelevant information, but it often comes at the risk of losing important information necessary to answer the input q
- arxiv:2606.24595 · 2026-06-23 · preprint · sim 0.49 · hf · found via methods
  MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
  Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interac
- arxiv:2603.18718 · 2026-03-19 · preprint · sim 0.48 · hf · found via methods
  MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution
  Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines. This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse, delayed supervision on the backward path, where downstream failures rarely translate into 
- arxiv:2601.10681 · 2026-01-15 · preprint · sim 0.47 · hf · found via agent
  Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems
  Large language model (LLM) contexts are typically constructed using retrieval-augmented generation (RAG), which involves ranking and selecting the top-k passages. The approach causes fragmentation in information graphs in document structures, over-retrieval, and duplication of content alongside insufficient query context, including 2nd and 3rd order facets. In this paper, a structure-informed and diversity-constrained context bubble construction framework is proposed that assembles coherent, cit
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.47 · hf · found via baseline
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2505.12574 · 2025-05-18 · sim 0.44 · via mechanism_home — PoisonArena: Uncovering Competing Poisoning Attacks in
  Retrieval-Augmented Generation
- arxiv:2604.20006 · 2026-04-21 · sim 0.44 · via baseline — From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents
- arxiv:2607.12893 · 2026-07-14 · sim 0.44 · via agent/baseline — MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations
- arxiv:2607.21447 · 2026-07-23 · sim 0.43 · via baseline — RUMBA: Russian User Memory Benchmark
- arxiv:2608.09043 · 2026-08-10 · sim 0.40 · via baseline — Don't Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
