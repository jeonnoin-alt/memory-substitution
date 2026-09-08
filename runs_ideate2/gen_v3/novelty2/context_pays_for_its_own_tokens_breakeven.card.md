=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_pays_for_its_own_tokens_breakeven — Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.60 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2608.28044 · 2026-08-28 · preprint · sim 0.53 · s2 · found via mechanism_home
  Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms
  Large language model (LLM) inference serving is priced by tokens, but GPU energy is consumed over inference windows. This accounting mismatch makes token-normalized metrics incomplete, since average output-token energy can decrease even when total request energy increases. We characterize this behavior with a decomposed energy model: a fixed one-time prefill with a fixed generation setup cost, while each output-token generation step adds marginal step energy. We evaluate this LLM inference energ
- arxiv:2605.12493 · 2026-05-12 · preprint · sim 0.50 · hf · found via agent
  LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for 
- arxiv:2609.02737 · 2026-09-02 · preprint · sim 0.48 · s2 · found via mechanism_home
  Language Models Can Control Their Own Attention
  Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motiva
- arxiv:2607.21051 · 2026-07-23 · preprint · sim 0.46 · hf · found via agent
  Sample-Efficient Learning from Agent Experience
  Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interacti
- arxiv:2511.23271 · 2025-11-28 · preprint · sim 0.42 · hf · found via mechanism_home
  Behavior-Equivalent Token: Single-Token Replacement for Long Prompts in LLMs
  Carefully engineered system prompts play a critical role in guiding the behavior of LLM agents, but their considerable length introduces significant drawbacks, including increased inference latency, higher computational cost, and reduced effective context length. This raises the question of whether such lengthy prompts can be replaced by a drastically reduced number of tokens while preserving their behavioral effect on downstream tasks. To enable this, we propose a lightweight three-stage traini
- arxiv:2603.18272 · 2026-03-18 · preprint · sim 0.41 · hf · found via agent
  Retrieval-Augmented LLM Agents: Learning to Learn from Experience
  While large language models (LLMs) have advanced the development of general-purpose agents, achieving robust generalization to unseen tasks remains a significant challenge. Current approaches typically rely on either fine-tuning or training-free memory-augmented generation using retrieved experience; yet both have limitations: fine-tuning often fails to extrapolate to new tasks, while experience retrieval often underperforms compared to supervised baselines. In this work, we propose to combine t
- arxiv:2503.08640 · 2025-03-11 · preprint · sim 0.41 · hf · found via mechanism_home
  Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse
  Attention
  Many-shot in-context learning has recently shown promise as an alternative to finetuning, with the major advantage that the same model can be served for multiple tasks. However, this shifts the computational burden from training-time to inference-time, making deployment of many-shot ICL challenging to justify in-practice. This cost is further increased if a custom demonstration set is retrieved for each inference example. We present Dynamic Block-Sparse Attention, a training-free framework for r
- arxiv:2606.05684 · 2026-06-04 · preprint · sim 0.41 · hf · found via agent
  AdaMEM: Test-Time Adaptive Memory for Language Agents
  A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions. While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation. Consequently, agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. To address this rigidity, we propose the Adaptive Memory Agent (AdaMEM), a novel framework for agent test-time adaptation. Without upda
- arxiv:2603.04257 · 2026-03-04 · preprint · sim 0.39 · hf · found via agent
  Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory
  Large language model (LLM) agents are fundamentally bottlenecked by finite context windows on long-horizon tasks. As trajectories grow, retaining tool outputs and intermediate reasoning in-context quickly becomes infeasible: the working context becomes prohibitively long, eventually exceeds the context budget, and makes distant evidence harder to use even when it is still present. Existing solutions typically shorten context through truncation or running summaries, but these methods are fundamen

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2506.06266 · 2025-06-06 · sim 0.39 · via mechanism_home — Cartridges: Lightweight and general-purpose long context representations
  via self-study
- arxiv:2405.00200 · 2024-04-30 · sim 0.39 · via mechanism_home — In-Context Learning with Long-Context Models: An In-Depth Exploration
- arxiv:2602.23200 · 2026-02-26 · sim 0.39 · via mechanism_home — InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models
- arxiv:2311.06102 · 2023-11-10 · sim 0.37 · via mechanism_home — Making LLMs Worth Every Penny: Resource-Limited Text Classification in
  Banking
- arxiv:2410.05563 · 2024-10-07 · sim 0.36 · via mechanism_home — Rational Metareasoning for Large Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
