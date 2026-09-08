=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: success_filter_lockin_under_shift — Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights

- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.62 · hf · found via agent/baseline
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2608.02508 · 2026-08-10 · preprint · sim 0.62 · hf · found via agent/baseline/methods
  RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
  Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory R
- arxiv:2607.03702 · 2026-07-04 · preprint · sim 0.60 · hf · found via agent
  Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry
  Large language model (LLM) agents have shown strong decision-making capabilities in long-horizon interactive tasks, yet they still struggle to effectively leverage failed trajectories: full retries incur high interaction costs, while experience retrieval tends to dilute critical experience signals. To address this, we propose PivoARL, a self-feedback retry framework for experience exploitation in LLM agents. PivoARL identifies the pivotal erroneous turn through structured reflection and performs
- arxiv:2606.24428 · 2026-06-23 · preprint · sim 0.60 · hf · found via agent/methods
  Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning
  Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. However, existing experience learning methods mostly rely on single-agent loops, where the same agent executes tasks, summarizes outcomes, and determines memory content. This setup makes agents vulnerable to the Self-Confirmation Trap: wrong-but-self-consistent trajectories are misidentified as successful experience, leading to cumulative errors during retrieval and reuse
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf · found via agent/baseline/methods
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2606.24595 · 2026-06-23 · preprint · sim 0.56 · hf · found via agent
  MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
  Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interac
- arxiv:2603.02473 · 2026-04-12 · preprint · sim 0.55 · hf · found via baseline
  Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
  Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval
- arxiv:2607.08716 · 2026-07-09 · preprint · sim 0.53 · hf · found via baseline
  Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
  In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate me
- arxiv:2607.29468 · 2026-07-31 · preprint · sim 0.52 · hf · found via agent
  Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember
  Self-play agents can generate training problems without questions from target benchmarks, but their curricula lack persistent state: failures affect gradients yet do not explicitly shape future practice. External skill memories preserve procedural experience but are typically learned from fixed task distributions. We introduce SESA (Self-Evolving Skill-Augmented Agent), which makes procedural memory an evolving state of tool-augmented search self-play. A challenger poses problems, while a separa
- arxiv:2607.07663 · 2026-07-08 · preprint · sim 0.49 · hf · found via mechanism_home
  Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops
  AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI research itself. This literature is described under a vocabulary ("self-refine," "self-reward," "self-play," "self-evolve") that conflates fundamentally different ambitions. We survey 1,250 arXiv papers (2024-2026) along two axes: what the system improves -- its behavior in deployment, its policy thr

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2602.16493 · 2026-02-18 · sim 0.48 · via baseline — MMA: Multimodal Memory Agent
- arxiv:2607.12893 · 2026-07-14 · sim 0.46 · via baseline — MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations
- arxiv:2507.06419 · 2026-04-08 · sim 0.46 · via baseline — Reward Models Can Improve Themselves: Reward-Guided Adversarial Failure Mode Discovery for Robust Reward Modeling
- arxiv:2404.01413 · 2024-04-01 · sim 0.46 · via adjacent — Is Model Collapse Inevitable? Breaking the Curse of Recursion by
  Accumulating Real and Synthetic Data
- arxiv:2211.13585 · 2022-11-24 · sim 0.45 · via mechanism_home — Learning to Suggest Breaks: Sustainable Optimization of Long-Term User
  Engagement

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
