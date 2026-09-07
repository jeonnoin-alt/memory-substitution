=== SYSTEM ===
You are given the index cards for one axis. Write the 3-5 open gaps these papers jointly expose: for each gap, one
sentence stating what is unresolved, the card IDs whose stated limitations or untested items point to it (at least
two), and one sentence on what evidence would settle it. Do not propose papers. Do not invent gaps that no card
supports. Return JSON: {"axis":"...","gaps":[{"gap","card_ids":[...],"evidence_needed"}]}.

=== USER ===
[
 {
  "claim": "For agentic long-context reasoning with a streaming memory, skipping intermediate retrieval and instead triggering question decomposition and rereading when the final memory is insufficient recovers prematurely discarded indirect facts and outperforms retrieval-augmented memorize-while-reading baselines while keeping linear time complexity.",
  "method": "MemReread reads document chunks in a stream while updating memory, triggers decomposition and rereading passes when the final memory cannot answer, and uses a reinforcement learning framework to improve length extrapolation and to decide the number of rereading passes according to task complexity.",
  "evidence": "Long-context reasoning tasks (benchmarks and models not named in the abstract); described as consistently outperforming baseline frameworks with linear time complexity in context length. No headline numbers are stated.",
  "stated_limitations": "not stated",
  "not_tested": "No quantified comparison of total tokens or wall-clock cost of rereading passes against retrieval baselines, and no numbers, models or benchmark names appear in the abstract.",
  "axes": [],
  "date": "2026-05-11",
  "id": "arxiv:2605.10268",
  "title": "MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading"
 },
 {
  "id": "arxiv:2109.00527",
  "date": "2021-09-01",
  "claim": "Search agents can learn meta-strategies for iterative query refinement that match recent neural retrieval methods while using only a BM25 ranker and interpretable discrete actions.",
  "method": "Machine reading guides selection of refinement terms from aggregated results, agents use simple search operators for fine-grained query control, synthetic search sessions are generated via (self-)supervised transformer language models, and an RL agent with dynamically constrained actions learns interactive search strategies from scratch.",
  "evidence": "Information-seeking tasks; retrieval and answer quality comparable to recent neural methods using a traditional BM25 ranking function with discrete reranking and filtering actions; no numeric headline figures in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No treatment of experience memory or of moving experience into weights versus context; the paper predates LLM agents and does not address cost comparisons between substrates.",
  "axes": [],
  "title": "Boosting Search Engines with Interactive Agents"
 }
]
