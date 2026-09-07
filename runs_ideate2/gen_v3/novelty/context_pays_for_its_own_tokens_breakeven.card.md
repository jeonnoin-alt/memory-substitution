=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_pays_for_its_own_tokens_breakeven — Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.60 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.21503 · 2026-07-23 · preprint · sim 0.56 · hf
  Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
  Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. The incumbent response treats this as a storage-and-retrieval problem. We argue that framing i
- arxiv:2602.16313 · 2026-02-18 · preprint · sim 0.54 · hf
  MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
  Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment,
- arxiv:2601.11969 · 2026-01-17 · preprint · sim 0.52 · hf
  MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models
  Existing works increasingly adopt memory-centric mechanisms to process long contexts in a segment manner, and effective memory management is one of the key capabilities that enables large language models to effectively propagate information across the entire sequence. Therefore, leveraging reward models (RMs) to automatically and reliably evaluate memory quality is critical. In this work, we introduce MemoryRewardBench, the first benchmark to systematically study the ability of RMs to evaluate l
- arxiv:2606.03329 · 2026-06-02 · preprint · sim 0.51 · hf
  InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain
  Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts. Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory. However, existing RL-based chunk-wise agents either rely on sparse final-answer rewards or use lexical intermediate rewards for memory and retrieval actions. These signals supervise task success or local overlap, but do n
- arxiv:2105.14039 · 2021-05-28 · preprint · sim 0.48 · hf
  Towards mental time travel: a hierarchical memory for reinforcement
  learning agents
  Reinforcement learning agents often forget details of the past, especially after delays or distractor tasks. Agents with common memory architectures struggle to recall and integrate across multiple timesteps of a past event, or even to recall the details of a single timestep that is followed by distractor tasks. To address these limitations, we propose a Hierarchical Chunk Attention Memory (HCAM), which helps agents to remember the past in detail. HCAM stores memories by dividing the past into c
- arxiv:2608.04003 · 2026-08-04 · preprint · sim 0.45 · hf
  PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-
- arxiv:2605.29341 · 2026-05-28 · preprint · sim 0.44 · hf
  WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction
  Multimodal large language models are increasingly deployed as long-horizon agents, where memory must do more than recall: it must track an evolving world, revise what has gone stale, and surface the right evidence at decision time. Existing benchmarks measure recall over static dialogue, collapse memory into a single end-of-task accuracy, and reduce visual observations to captions, leaving us unable to localize failures to writing, maintenance, retrieval, or use. The rise of agent harnesses that
- arxiv:2603.23971 · 2026-03-25 · preprint · sim 0.43 · hf
  The Price Reversal Phenomenon: When Cheaper Reasoning Models End Up Costing More
  Developers and consumers increasingly choose reasoning language models (RLMs) based on their listed API prices. However, how accurately do these prices reflect actual inference costs? We conduct the first systematic study of this question, evaluating 8 frontier RLMs across 9 diverse tasks covering competition math, science QA, code generation, and multi-domain reasoning. We uncover the pricing reversal phenomenon: in 21.8% of model-pair comparisons, the model with a lower listed price actually i
- arxiv:2608.18852 · 2026-08-19 · preprint · sim 0.43 · hf
  SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
  Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
