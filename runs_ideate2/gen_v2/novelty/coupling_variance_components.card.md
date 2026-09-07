=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: coupling_variance_components — Whose Variance Is It? A Seed-Crossed Decomposition and Cost-Matched Audit of Memory-Coupled Prompt Optimization on Long-Horizon Agent Tasks

- arxiv:2606.16285 · 2026-06-15 · preprint · sim 0.57 · hf
  HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents
  Long-horizon agents rely on memory mechanisms to compress interaction history, but optimizing memory writing faces a distinct credit assignment challenge: a memory update may be rewarded or penalized due to downstream tool failures, noisy observations, or reasoning errors rather than its own contribution. This causally entangled credit can lead agents to discard useful evidence or preserve irrelevant information. We propose HiMPO, a Hindsight-Informed Memory Policy Optimization framework for ass
- arxiv:2602.16313 · 2026-02-18 · preprint · sim 0.57 · hf
  MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
  Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment,
- arxiv:2605.27140 · 2026-05-26 · preprint · sim 0.56 · hf
  StepOPSD: Step-Aware Online Preference Distillation for Agent Reinforcement Learning
  Reinforcement learning for multi-turn agents suffers from a credit-assignment mismatch: rewards are sparse and trajectory-level, while success often hinges on a few local decisions. Existing online policy distillation (OPD) provides denser token-level supervision, but typically treats heterogeneous agent trajectories as monolithic strings rather than causal interaction units. We present StepOPSD, a post-rollout preference self-distillation framework that takes the agent step as the unit of credi
- arxiv:2603.09022 · 2026-03-09 · arXiv.org · sim 0.56 · hf/s2
  MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games
  Multi-turn, multi-agent LLM game evaluations often exhibit substantial run-to-run variance. In long-horizon interactions, small early deviations compound across turns and are amplified by multi-agent coupling. This biases win rate estimates and makes rankings unreliable across repeated tournaments. Prompt choice worsens this further by producing different effective policies. We address both instability and underperformance with MEMO (Memory-augmented MOdel context optimization), a self-play fram
- arxiv:2607.13884 · 2026-07-15 · preprint · sim 0.56 · hf
  Experience Memory Graph: One-Shot Error Correction for Agents
  Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations. However, in complex, long-horizon tasks, these agents frequently suffer from compounding errors and struggle to recover from failures. Existing self-correction mechanisms rely on prompt-based reflection, which is inherently brittle, incurs heavy time and API costs due to iterative trial-and-error loops, and produces task-sp
- arxiv:2606.24595 · 2026-06-23 · preprint · sim 0.53 · hf
  MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
  Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interac
- arxiv:2601.08816 · 2026-01-13 · preprint · sim 0.53 · hf
  MemRec: Collaborative Memory-Augmented Agentic Recommender System
  The evolution of recommender systems has shifted preference storage from rating matrices and dense embeddings to semantic memory in the agentic era. Yet existing agents rely on isolated memory, overlooking crucial collaborative signals. Bridging this gap is hindered by the dual challenges of distilling vast graph contexts without overwhelming reasoning agents with cognitive load, and evolving the collaborative memory efficiently without incurring prohibitive computational costs. To address this,
- arxiv:2607.07702 · 2026-07-08 · preprint · sim 0.53 · hf
  From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization
  The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, 
- arxiv:2603.20667 · 2026-03-21 · preprint · sim 0.52 · hf
  REVERE: Reflective Evolving Research Engineer for Scientific Workflows
  Existing prompt-optimization techniques rely on local signals to update behavior, often neglecting broader and recurring patterns across tasks, leading to poor generalization; they further rely on full-prompt rewrites or unstructured merges, resulting in knowledge loss. These limitations are magnified in research-coding workflows, which involve heterogeneous repositories, underspecified environments, and weak feedback, where reproducing results from public codebases is an established evaluation 
- arxiv:2605.12493 · 2026-05-12 · preprint · sim 0.52 · hf
  LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for 

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
