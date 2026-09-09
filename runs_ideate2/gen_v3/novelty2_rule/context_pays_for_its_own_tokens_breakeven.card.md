=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_pays_for_its_own_tokens_breakeven — Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.60 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.21503 · 2026-07-23 · preprint · sim 0.56 · hf · found via agent
  Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
  Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. The incumbent response treats this as a storage-and-retrieval problem. We argue that framing i
- arxiv:2602.16313 · 2026-02-18 · preprint · sim 0.54 · hf · found via agent
  MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
  Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment,
- arxiv:2601.11969 · 2026-01-17 · preprint · sim 0.52 · hf · found via agent
  MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models
  Existing works increasingly adopt memory-centric mechanisms to process long contexts in a segment manner, and effective memory management is one of the key capabilities that enables large language models to effectively propagate information across the entire sequence. Therefore, leveraging reward models (RMs) to automatically and reliably evaluate memory quality is critical. In this work, we introduce MemoryRewardBench, the first benchmark to systematically study the ability of RMs to evaluate l
- arxiv:2606.03329 · 2026-06-02 · preprint · sim 0.51 · hf · found via agent
  InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain
  Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts. Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory. However, existing RL-based chunk-wise agents either rely on sparse final-answer rewards or use lexical intermediate rewards for memory and retrieval actions. These signals supervise task success or local overlap, but do n
- arxiv:2105.14039 · 2021-05-28 · preprint · sim 0.48 · hf · found via agent
  Towards mental time travel: a hierarchical memory for reinforcement
  learning agents
  Reinforcement learning agents often forget details of the past, especially after delays or distractor tasks. Agents with common memory architectures struggle to recall and integrate across multiple timesteps of a past event, or even to recall the details of a single timestep that is followed by distractor tasks. To address these limitations, we propose a Hierarchical Chunk Attention Memory (HCAM), which helps agents to remember the past in detail. HCAM stores memories by dividing the past into c
- arxiv:2607.00725 · 2026-07-01 · preprint · sim 0.45 · hf · found via mechanism_home
  What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It
  Retrieval-augmented generation (RAG) under a fixed reader-context budget forces a selection problem: of the evidence retrieved, only a fraction can be shown to the reader. We argue that document recall -- the standard retrieval metric -- is the wrong quantity to optimize in this regime, and we make two contributions. First, as a general contribution, we introduce answer-in-context, a diagnostic that measures whether a gold answer survives as a contiguous span in the packed reader context (not th
- arxiv:2608.26175 · 2026-07-27 · preprint · sim 0.44 · hf · found via baseline
  Lost in Compression: A Controlled Cross-Lingual Audit of Extractive Prompt Compressors
  Extractive prompt compression promises to cut LLM inference costs by removing low-information tokens, and learned compressors such as LLMLingua-2 report strong results on English benchmarks. Most other languages already pay a token premium: the same content costs 1.3-1.8x more tokens than in English. We ask whether compression closes or widens this gap. Using fully parallel data in ten languages spanning five scripts, with controls budget-matched in the target model's tokenizer, we audit four le
- arxiv:2605.29341 · 2026-05-28 · preprint · sim 0.44 · hf · found via agent
  WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction
  Multimodal large language models are increasingly deployed as long-horizon agents, where memory must do more than recall: it must track an evolving world, revise what has gone stale, and surface the right evidence at decision time. Existing benchmarks measure recall over static dialogue, collapse memory into a single end-of-task accuracy, and reduce visual observations to captions, leaving us unable to localize failures to writing, maintenance, retrieval, or use. The rise of agent harnesses that
- arxiv:2603.23971 · 2026-03-25 · preprint · sim 0.43 · hf · found via agent/mechanism_home
  The Price Reversal Phenomenon: When Cheaper Reasoning Models End Up Costing More
  Developers and consumers increasingly choose reasoning language models (RLMs) based on their listed API prices. However, how accurately do these prices reflect actual inference costs? We conduct the first systematic study of this question, evaluating 8 frontier RLMs across 9 diverse tasks covering competition math, science QA, code generation, and multi-domain reasoning. We uncover the pricing reversal phenomenon: in 21.8% of model-pair comparisons, the model with a lower listed price actually i

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2604.16890 · 2026-04-18 · sim 0.43 · via mechanism_home — Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning
- arxiv:2511.23271 · 2025-11-28 · sim 0.42 · via baseline — Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs
- arxiv:2509.09677 · 2025-09-11 · sim 0.42 · via mechanism_home — The Illusion of Diminishing Returns: Measuring Long Horizon Execution in
  LLMs
- arxiv:2510.16439 · 2025-10-18 · sim 0.41 · via agent/baseline — FrugalPrompt: Reducing Contextual Overhead in Large Language Models via Token Attribution
- arxiv:2606.02643 · 2026-04-13 · sim 0.40 · via mechanism_home — Inference Cost Attacks for Retrieval-Augmented Large Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
