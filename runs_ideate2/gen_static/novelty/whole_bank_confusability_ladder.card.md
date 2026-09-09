=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: whole_bank_confusability_ladder — Confusable, Not Long: The Whole-Bank-in-Context Route Loses to Top-k Retrieval Only as Near-Miss Trajectories Accumulate

- arxiv:2402.07440 · 2024-02-12 · preprint · sim 0.67 · hf · found via methods
  Benchmarking and Building Long-Context Retrieval Models with LoCo and
  M2-BERT
  Retrieval pipelines-an integral component of many machine learning systems-perform poorly in domains where documents are long (e.g., 10K tokens or more) and where identifying the relevant document requires synthesizing information across the entire text. Developing long-context retrieval encoders suitable for these domains raises three challenges: (1) how to evaluate long-context retrieval performance, (2) how to pretrain a base language model to represent both short contexts (corresponding to q
- arxiv:2606.22778 · 2026-06-22 · preprint · sim 0.62 · hf · found via baseline
  HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions
  With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. Large retrieval benchmarks are comprehensive but too heavy to rerun during development, and there is little infrastructure for comparing production settings--dimensionality reduction, quantization, reranking--across many models under identical conditions. We present HAKARI-Bench, a lightweight benchmark that reconstructs existing retrieval su
- arxiv:1406.3170 · 2014-06-12 · Annual Symposium on Combinatorial Pattern Matching · sim 0.61 · s2 · found via baseline
  Compact Indexes for Flexible Top- k k Retrieval
  We design and engineer a self-index based retrieval system capable of rank-safe evaluation of top-\(k\) queries. The framework generalizes the GREEDY approach of Culpepper et al. (ESA 2010) to handle multi-term queries, including over phrases. We propose two techniques which significantly reduce the ranking time for a wide range of popular Information Retrieval (IR) relevance measures, such as \({\textsc {TF}\times \textsc {IDF}} \) and \({\textsc {BM25}} \). First, we reorder elements in the do
- arxiv:2608.06305 · 2026-08-06 · preprint · sim 0.61 · s2 · found via baseline
  Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations
  Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important class of documents -- financial statements, audit reports, regulatory returns -- this design is structurally unsound, and we make the argument measurable. On a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding spa
- arxiv:2607.00394 · 2026-07-01 · preprint · sim 0.60 · hf · found via agent
  When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers
  LLM agents increasingly rely on retrieval buffers to store and reuse past experience, yet the cache management policies governing these buffers remain largely ad-hoc. We formalize this as an online semantic cache replacement problem with switching costs, where items are matched by embedding similarity and hit quality is continuous rather than binary. Through experiments on two datasets from MemoryBench-Full (LoCoMo, DialSim) with 8 replacement policies, we reveal a surprising finding: classic he
- arxiv:2502.13542 · 2025-02-19 · preprint · sim 0.57 · hf · found via methods
  Activation-aware Probe-Query: Effective Key-Value Retrieval for
  Long-Context LLMs Inference
  Recent advances in large language models (LLMs) have showcased exceptional performance in long-context tasks, while facing significant inference efficiency challenges with limited GPU memory. Existing solutions first proposed the sliding-window approach to accumulate a set of historical key-value (KV) pairs for reuse, then further improvements selectively retain its subsets at each step. However, due to the sparse attention distribution across a long context, it is hard to identify and recall re
- arxiv:2602.20732 · 2026-02-24 · preprint · sim 0.52 · hf · found via agent
  CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
  Long-context LLMs demand accurate inference at low latency, yet decoding becomes primarily constrained by KV cache as context grows. Prior pruning methods are largely context-agnostic: their token selection ignores step-wise relevance and local semantics, which undermines quality. Moreover, their irregular accesses and selection overheads yield only limited wall-clock speedups. To address this, we propose CHESS, an algorithm-system co-design KV-cache management system. Algorithmically, CHESS int
- arxiv:2603.04238 · 2026-03-04 · preprint · sim 0.51 · hf · found via baseline
  Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG
  Retrieval-augmented generation (RAG) is a common way to ground language models in external documents and up-to-date information. Classical retrieval systems relied on lexical methods such as BM25, which rank documents by term overlap with corpus-level weighting. End-to-end multimodal retrievers trained on large query-document datasets claim substantial improvements over these approaches, especially for multilingual documents with complex visual layouts. We demonstrate that better document repres
- arxiv:2608.21450 · 2026-08-19 · preprint · sim 0.51 · hf · found via baseline
  Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering
  Knowledge-Based Visual Question Answering (KB-VQA) relies on retrieving external information to answer queries involving long-tail entities. However, existing retrieval pipelines predominantly employ CLIP-style dual encoders, which prioritize surface-level visual similarity over entity-level semantic alignment. This paradigm often fails when semantically identical concepts exhibit large visual variations or when distinct entities appear visually similar. To address this, we propose KBMR, the fir
- s2:db7348b987400b62504a338018ce352588312202 · 2025 · Fire · sim 0.49 · s2 · found via baseline
  LexiSemIR: A Two-Stage Re-ranking Framework with BM25 and Zero-Shot Bi-Encoder
  LexiSemIR, a two-stage re-ranking-based model developed for the CMIR-2025 (Code-Mixed Information Retrieval) shared task on Bengali-English code-mixed text, secures 3rd place and highlights the model’s ability to effectively combine lexical and semantic retrieval strategies for robust performance in code-mixed IR settings.

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2411.18947 · 2024-11-28 · sim 0.47 · via adjacent — ICLERB: In-Context Learning Embedding and Reranker Benchmark
- arxiv:2603.05697 · 2026-03-05 · sim 0.46 · via baseline — MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents
- arxiv:2308.04028 · 2023-08-08 · sim 0.46 · via baseline — Top K Relevant Passage Retrieval for Biomedical Question Answering
- s2:bbb8c2ebdf262e176150a2ea37ab6dffdcf0e415 · 2023 · sim 0.46 · via baseline — Passage-based BM25 Hard Negatives: A Simple and Effective Negative Sampling Strategy For Dense Retrieval
- s2:6ceacb27d78a284e6cb278977ee930cf27b299a1 · 2013 · sim 0.45 · via mechanism_home — The Role of Contextual Repetition During Fast Mapping on Word Learning

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
