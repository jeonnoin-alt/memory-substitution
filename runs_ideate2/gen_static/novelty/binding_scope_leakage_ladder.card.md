=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: binding_scope_leakage_ladder — Global Fact, Scene Table, or Instance Replay: The Scope of Instance Bindings Sets How Much of a Memory Gain Is Near-Duplicate Leakage and Whether a Static Prompt Can Match It

- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.55 · hf · found via adjacent
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.55 · hf · found via adjacent
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2605.09611 · 2026-05-10 · preprint · sim 0.51 · hf · found via mechanism_home
  Byte-Exact Deduplication in Retrieval-Augmented Generation: A Three-Regime Empirical Analysis Across Public Benchmarks
  This preprint presents an empirical analysis of byte-exact chunk-level deduplication in Retrieval-Augmented Generation (RAG) pipelines. We measure context reduction across three distinct operating regimes: clean academic retrieval (0.16% byte reduction on 22.2M BeIR passages), constructed enterprise patterns (24.03% reduction), and multi-turn conversational AI (80.34% reduction). To validate quality preservation, we conducted a cross-vendor 5-judge calibrated panel evaluation across four product
- arxiv:2605.13941 · 2026-05-13 · preprint · sim 0.50 · hf · found via methods
  EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents
  Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full r
- arxiv:2511.20857 · 2025-11-25 · preprint · sim 0.50 · hf · found via methods
  Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
  Statefulness is essential for large language model (LLM) agents to perform long-term planning and problem-solving. This makes memory a critical component, yet its management and evolution remain largely underexplored. Existing evaluations mostly focus on static conversational settings, where memory is passively retrieved from dialogue to answer queries, overlooking the dynamic ability to accumulate and reuse experience across evolving task streams. In real-world environments such as interactive 
- arxiv:2608.05784 · 2026-08-06 · preprint · sim 0.49 · hf · found via agent
  Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay
  Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local capture stream into typed activity frames, bounded episodes carrying application, site, timing, input volume, and evidence pointers back to the raw rows, with no model in the loop, so th
- arxiv:2510.16809 · 2025-10-19 · preprint · sim 0.49 · hf · found via mechanism_home
  When Many-Shot Prompting Fails: An Empirical Study of LLM Code Translation
  Large Language Models (LLMs) with vast context windows offer new avenues for in-context learning (ICL), where providing many examples ("many-shot" prompting) is often assumed to enhance performance. We investigate this assumption for the complex task of code translation. Through a large-scale empirical study of over 90,000 translations, we systematically evaluate the impact of scaling in-context examples from zero-shot to many-shot configurations of up to 625 examples, with prompts spanning from
- arxiv:2609.01865 · 2026-09-01 · preprint · sim 0.49 · hf · found via agent
  ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval
  Embedding-based code retrieval is a core component of coding agents and retrieval-augmented code generation, where retrieving correct code matters more than retrieving lexically similar code. Existing code-retrieval benchmarks do not plant controlled, execution-verified single-edit variants of each query's canonical implementation in the search pool, leaving the question of whether embeddings can functionally discriminate correct from near-clone-but-incorrect code unanswered in a retrieval setti
- arxiv:2411.04257 · 2024-11-06 · preprint · sim 0.48 · hf · found via mechanism_home
  LSHBloom: Memory-efficient, Extreme-scale Document Deduplication
  Deduplication is a major focus for assembling and curating training datasets for large language models (LLM) -- detecting and eliminating additional instances of the same content -- in large collections of technical documents. Unrestrained, duplicates in the training dataset increase training costs and lead to undesirable properties such as memorization in trained models or cheating on evaluation. Contemporary approaches to document-level deduplication are often extremely expensive in both runti
- arxiv:2205.10487 · 2022-05-21 · preprint · sim 0.48 · hf · found via adjacent
  Scaling Laws and Interpretability of Learning from Repeated Data
  Recent large language models have been trained on vast datasets, but also often on repeated data, either intentionally for the purpose of upweighting higher quality data, or unintentionally because data deduplication is not perfect and the model is exposed to repeated data at the sentence, paragraph, or document level. Some works have reported substantial negative performance effects of this repeated data. In this paper we attempt to study repeated data systematically and to understand its effec

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2309.07900 · 2023-09-14 · sim 0.47 · via mechanism_home — Ambiguity-Aware In-Context Learning with Large Language Models
- arxiv:2608.03089 · 2026-08-04 · sim 0.47 · via mechanism_home — Scalable Frequency- and Length-Aware Subdocument Deduplication for Large Language Model Pretraining
- arxiv:2305.14907 · 2023-05-24 · sim 0.46 · via mechanism_home — Coverage-based Example Selection for In-Context Learning
- arxiv:2605.13511 · 2026-05-13 · sim 0.46 · via mechanism_home — Many-Shot CoT-ICL: Making In-Context Learning Truly Learn
- arxiv:2606.05633 · 2026-06-04 · sim 0.46 · via adjacent — Answer Presence Drives RAG Rewriting Gains

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
