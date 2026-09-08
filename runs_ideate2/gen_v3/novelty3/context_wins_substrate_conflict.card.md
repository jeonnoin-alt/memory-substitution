=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_wins_substrate_conflict — When Weights and Memory Disagree: Which Substrate an Agent Follows After a Rule Change, and What It Means for Hybrid Memory Under Shift

- arxiv:2608.04574 · 2026-08-05 · preprint · sim 0.59 · hf · found via agent
  When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.08716 · 2026-07-09 · preprint · sim 0.57 · hf · found via agent
  Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
  In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate me
- arxiv:2605.24941 · 2026-05-24 · preprint · sim 0.54 · hf · found via agent
  Memory-Induced Tool-Drift in LLM Agents
  Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production systems. We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. We call this memory-induced tool-drift and operationalize it through MEMDRIFT,
- arxiv:2605.30690 · 2026-05-29 · preprint · sim 0.53 · hf · found via agent
  ElasticMem: Latent Memory as a Learnable Resource for LLM Agents
  Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity to noisy evidence, while latent-space approaches reduce textual cost but still rely on rigid retrieval or fixed-capacity memory interfaces
- arxiv:2602.18628 · 2026-02-20 · preprint · sim 0.53 · hf · found via agent
  Non-Interfering Weight Fields: Treating Model Parameters as a Continuously Extensible Function
  Large language models store all learned knowledge in a single, fixed weight vector. Teaching a model new capabilities requires modifying those same weights, inevitably degrading previously acquired knowledge. This fundamental limitation, known as catastrophic forgetting, has resisted principled solutions for decades. Existing approaches treat weights as immutable artifacts that must be protected through techniques like regularization heuristics, replay buffers, or isolated adapter modules. The p
- arxiv:2603.04549 · 2026-03-04 · preprint · sim 0.53 · hf · found via agent
  Adaptive Memory Admission Control for LLM Agents
  LLM-based agents increasingly rely on long-term memory to support multi-session reasoning and interaction, yet current systems provide little control over what information is retained. In practice, agents either accumulate large volumes of conversational content, including hallucinated or obsolete facts, or depend on opaque, fully LLM-driven memory policies that are costly and difficult to audit. As a result, memory admission remains a poorly specified and weakly controlled component in agent ar
- arxiv:2606.13174 · 2026-06-11 · preprint · sim 0.51 · hf · found via agent
  Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents
  Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline
- arxiv:2605.26252 · 2026-05-25 · preprint · sim 0.51 · hf · found via agent
  Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory
  Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.51 · hf · found via agent/baseline
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2605.14473 · 2026-05-14 · sim 0.47 · via mechanism_home — Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict
- arxiv:2402.06262 · 2024-02-09 · sim 0.45 · via baseline — On the Efficacy of Eviction Policy for Key-Value Constrained Generative
  Language Model Inference
- arxiv:2410.05162 · 2024-10-07 · sim 0.44 · via adjacent — Deciphering the Interplay of Parametric and Non-parametric Memory in
  Retrieval-augmented Language Models
- arxiv:2605.25475 · 2026-05-25 · sim 0.43 · via baseline — IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference
- arxiv:2601.09445 · 2026-01-14 · sim 0.42 · via mechanism_home — Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
