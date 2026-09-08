=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_pays_for_its_own_tokens_breakeven — Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.60 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2603.13017 · 2026-03-13 · preprint · sim 0.57 · hf · found via agent
  Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation
  Long conversations with an AI agent create a simple problem for one user: the history is useful, but carrying it verbatim is expensive. We study personalized agent memory: one user's conversation history with an agent, distilled into a compact retrieval layer for later search. Each exchange is compressed into a compound object with four fields (exchange_core, specific_context, thematic room_assignments, and regex-extracted files_touched). The searchable distilled text averages 38 tokens per exch
- arxiv:2608.28044 · 2026-08-28 · preprint · sim 0.53 · s2 · found via mechanism_home
  Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms
  Large language model (LLM) inference serving is priced by tokens, but GPU energy is consumed over inference windows. This accounting mismatch makes token-normalized metrics incomplete, since average output-token energy can decrease even when total request energy increases. We characterize this behavior with a decomposed energy model: a fixed one-time prefill with a fixed generation setup cost, while each output-token generation step adds marginal step energy. We evaluate this LLM inference energ
- arxiv:2606.06448 · 2026-06-04 · preprint · sim 0.52 · hf · found via agent
  Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
  LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza
- arxiv:2607.13157 · 2026-07-14 · preprint · sim 0.51 · hf · found via agent
  Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents
  Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. These requirements extend beyond document retrieval: a memory layer must determine which interactions become durable state, how that state is scoped, how it is retrieved under latency constraints, and how it is revised or removed
- arxiv:2605.30690 · 2026-05-29 · preprint · sim 0.51 · hf · found via agent
  ElasticMem: Latent Memory as a Learnable Resource for LLM Agents
  Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity to noisy evidence, while latent-space approaches reduce textual cost but still rely on rigid retrieval or fixed-capacity memory interfaces
- arxiv:2605.12493 · 2026-05-12 · preprint · sim 0.50 · hf · found via agent
  LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for 
- arxiv:2609.02737 · 2026-09-02 · preprint · sim 0.48 · s2 · found via mechanism_home
  Language Models Can Control Their Own Attention
  Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motiva
- arxiv:2607.21051 · 2026-07-23 · preprint · sim 0.46 · hf · found via agent/methods
  Sample-Efficient Learning from Agent Experience
  Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interacti
- arxiv:2606.24428 · 2026-06-23 · preprint · sim 0.45 · hf · found via methods
  Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning
  Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. However, existing experience learning methods mostly rely on single-agent loops, where the same agent executes tasks, summarizes outcomes, and determines memory content. This setup makes agents vulnerable to the Self-Confirmation Trap: wrong-but-self-consistent trajectories are misidentified as successful experience, leading to cumulative errors during retrieval and reuse

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2511.23271 · 2025-11-28 · sim 0.42 · via mechanism_home — Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs
- arxiv:2503.08640 · 2025-03-11 · sim 0.41 · via mechanism_home — Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse
  Attention
- arxiv:2506.06266 · 2025-06-06 · sim 0.39 · via mechanism_home — Cartridges: Lightweight and general-purpose long context representations
  via self-study
- arxiv:2405.00200 · 2024-04-30 · sim 0.39 · via adjacent/mechanism_home — In-Context Learning with Long-Context Models: An In-Depth Exploration
- arxiv:2602.23200 · 2026-02-26 · sim 0.39 · via mechanism_home — InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
