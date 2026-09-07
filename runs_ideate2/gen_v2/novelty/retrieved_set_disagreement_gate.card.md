=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: retrieved_set_disagreement_gate — Abstain When They Disagree: Harm from Organically Accumulated Agent Memory Lives in the Retrieved Set, Not the Item, and a Disagreement Gate Beats Item-Level Utility Filtering at Zero Clean-Setting Cost

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.65 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2605.05583 · 2026-05-08 · preprint · sim 0.58 · hf
  Belief Memory: Agent Memory Under Partial Observability
  LLM agents that operate over long context depend on external memory to accumulate knowledge over time. However, existing methods typically store each observation as a single deterministic conclusion (e.g., inferring "API~X failed" from temporary errors), even though such observations are inherently partial and potentially ambiguous. By committing to one conclusion and discarding uncertainty, these methods introduce self-reinforcing error: the agent acts on the stored conclusion, never revisits a
- arxiv:2607.05844 · 2026-07-07 · preprint · sim 0.56 · hf
  StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems
  Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (
- arxiv:2602.07398 · 2026-02-07 · preprint · sim 0.53 · hf
  AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management
  Indirect prompt injection threatens LLM agents by embedding malicious instructions in external content, enabling unauthorized actions and data theft. LLM agents maintain working memory through their context window, which stores interaction history for decision-making. Conventional agents indiscriminately accumulate all tool outputs and reasoning traces in this memory, creating two critical vulnerabilities: (1) injected instructions persist throughout the workflow, granting attackers multiple opp
- arxiv:2608.04574 · 2026-08-05 · preprint · sim 0.52 · hf
  When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs
- arxiv:2605.14133 · 2026-05-13 · preprint · sim 0.50 · hf
  ClawForge: Generating Executable Interactive Benchmarks for Command-Line Agents
  Interactive agent benchmarks face a tension between scalable construction and realistic workflow evaluation. Hand-authored tasks are expensive to extend and revise, while static prompt evaluation misses failures that only appear when agents operate over persistent state. Existing interactive benchmarks have advanced agent evaluation significantly, but most initialize tasks from clean state and do not systematically test how agents handle pre-existing partial, stale, or conflicting artifacts. We 
- arxiv:2601.11653 · 2026-01-15 · preprint · sim 0.50 · hf
  AI Agents Need Memory Control Over More Context
  AI agents are increasingly used in long, multi-turn workflows in both research and enterprise settings. As interactions grow, agent behavior often degrades due to loss of constraint focus, error accumulation, and memory-induced drift. This problem is especially visible in real-world deployments where context evolves, distractions are introduced, and decisions must remain consistent over time. A common practice is to equip agents with persistent memory through transcript replay or retrieval-based
- arxiv:2606.28733 · 2026-06-27 · preprint · sim 0.50 · hf
  Agentic Abstention: Do Agents Know When to Stop Instead of Act?
  LLM agents are expected to act over multiple turns, using search, browsing interfaces, and terminal tools to complete user goals. Yet not every goal is well specified or achievable in the available environment. In such cases, a reliable agent should recognize that further interaction is unlikely to help and abstain from additional tool calls. We define Agentic Abstention, the problem of deciding when an agent should stop acting under uncertainty. Unlike standard LLM abstention, which is usually 
- arxiv:2604.18419 · 2026-06-12 · preprint · sim 0.49 · hf
  Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning
  LLMs utilizing chain-of-thought reasoning often waste substantial compute by producing long, incorrect responses. Abstention can mitigate this by withholding outputs unlikely to be correct. While most abstention methods decide to withhold outputs before or after generation, dynamic mid-generation abstention considers early termination of unpromising reasoning traces at each token position. Prior work has explored empirical variants of this idea, but principled guidance for the abstention rule re
- arxiv:2607.10059 · 2026-07-11 · preprint · sim 0.47 · hf
  AgentAbstain: Do LLM Agents Know When Not to Act?
  Agent systems based on large language models (LLMs) are increasingly deployed for autonomous tasks, yet existing evaluations mostly focus on task success rather than whether agents know when to abstain. This gap poses real risks: under ambiguity, conflicting constraints, or tool failures, agents may execute unintended and irreversible actions. To close this gap, we present the first systematic evaluation framework for agentic abstention: the calibrated ability of tool-using LLM agents to recogni

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
