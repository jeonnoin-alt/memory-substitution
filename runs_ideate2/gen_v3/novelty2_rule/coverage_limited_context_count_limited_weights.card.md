=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: coverage_limited_context_count_limited_weights — Coverage-Limited Context, Count-Limited Weights: The Substrate Crossover Lives on the Experience-Collection Axis, Not the Deployment Horizon

- arxiv:2606.17016 · 2026-06-15 · preprint · sim 0.55 · hf · found via agent
  TokenPilot: Cache-Efficient Context Management for LLM Agents
  As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, 
- arxiv:2406.15334 · 2024-06-21 · preprint · sim 0.49 · hf · found via adjacent
  Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning
  The recent success of interleaved Large Multimodal Models (LMMs) in few-shot learning suggests that in-context learning (ICL) with many examples can be promising for learning new tasks. However, this many-shot multimodal ICL setting has one crucial problem: it is fundamentally limited by the model's context length set at pretraining. The problem is especially prominent in the multimodal domain, which processes both text and images, requiring additional tokens. This motivates the need for a multi
- arxiv:2503.08640 · 2025-03-11 · preprint · sim 0.49 · hf · found via adjacent
  Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse
  Attention
  Many-shot in-context learning has recently shown promise as an alternative to finetuning, with the major advantage that the same model can be served for multiple tasks. However, this shifts the computational burden from training-time to inference-time, making deployment of many-shot ICL challenging to justify in-practice. This cost is further increased if a custom demonstration set is retrieved for each inference example. We present Dynamic Block-Sparse Attention, a training-free framework for r
- arxiv:2608.22695 · 2026-08-24 · preprint · sim 0.49 · hf · found via agent
  Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing
  Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable pr
- arxiv:2404.11018 · 2024-04-17 · preprint · sim 0.48 · hf · found via adjacent
  Many-Shot In-Context Learning
  Large language models (LLMs) excel at few-shot in-context learning (ICL) -- learning from a few examples provided in context at inference, without any weight updates. Newly expanded context windows allow us to investigate ICL with hundreds or thousands of examples -- the many-shot regime. Going from few-shot to many-shot, we observe significant performance gains across a wide variety of generative and discriminative tasks. While promising, many-shot ICL can be bottlenecked by the available amoun
- arxiv:2506.04579 · 2025-06-05 · preprint · sim 0.47 · hf · found via adjacent
  Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching
  In-Context Learning (ICL) empowers Large Language Models (LLMs) for rapid task adaptation without Fine-Tuning (FT), but its reliance on demonstration selection remains a critical challenge. While many-shot ICL shows promising performance through scaled demonstrations, the selection method for many-shot demonstrations remains limited to random selection in existing work. Since the conventional instance-level retrieval is not suitable for many-shot scenarios, we hypothesize that the data requireme
- arxiv:2405.09798 · 2024-05-16 · preprint · sim 0.46 · hf · found via adjacent
  Many-Shot In-Context Learning in Multimodal Foundation Models
  Large language models are well-known to be effective at few-shot in-context learning (ICL). Recent advancements in multimodal foundation models have enabled unprecedentedly long context windows, presenting an opportunity to explore their capability to perform ICL with many more demonstrating examples. In this work, we evaluate the performance of multimodal foundation models scaling from few-shot to many-shot ICL. We benchmark GPT-4o and Gemini 1.5 Pro across 10 datasets spanning multiple domains
- arxiv:2602.11748 · 2026-02-12 · preprint · sim 0.45 · hf · found via agent
  Think Longer to Explore Deeper: Learn to Explore In-Context via Length-Incentivized Reinforcement Learning
  Achieving effective test-time scaling requires models to engage in In-Context Exploration -- the intrinsic ability to generate, verify, and refine multiple reasoning hypotheses within a single continuous context. Grounded in State Coverage theory, our analysis identifies a critical bottleneck to enabling this capability: while broader state coverage requires longer reasoning trajectories, the probability of sampling such sequences decays exponentially during autoregressive generation, a phenomen
- arxiv:2506.11103 · 2025-06-06 · preprint · sim 0.43 · hf · found via adjacent
  You Only Fine-tune Once: Many-Shot In-Context Fine-Tuning for Large
  Language Model
  Large language models (LLMs) possess a remarkable ability to perform in-context learning (ICL), which enables them to handle multiple downstream tasks simultaneously without requiring task-specific fine-tuning. Recent studies have shown that even moderately sized LLMs, such as Mistral 7B, Gemma 7B and Llama-3 8B, can achieve ICL through few-shot in-context fine-tuning of all tasks at once. However, this approach still lags behind dedicated fine-tuning, where a separate model is trained for each 
- arxiv:2407.21787 · 2024-07-31 · preprint · sim 0.43 · hf · found via agent
  Large Language Monkeys: Scaling Inference Compute with Repeated Sampling
  Scaling the amount of compute used to train language models has dramatically improved their capabilities. However, when it comes to inference, we often limit the amount of compute to only one attempt per problem. Here, we explore inference compute as another axis for scaling by increasing the number of generated samples. Across multiple tasks and models, we observe that coverage - the fraction of problems solved by any attempt - scales with the number of samples over four orders of magnitude. In

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2606.05633 · 2026-06-04 · sim 0.43 · via mechanism_home — Answer Presence Drives RAG Rewriting Gains
- arxiv:2204.03511 · 2022-04-07 · sim 0.42 · via baseline — Interval Bound Interpolation for Few-shot Learning with Few Tasks
- arxiv:2609.02217 · 2026-09-02 · sim 0.42 · via agent/mechanism_home — SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams
- arxiv:2201.06910 · 2022-01-18 · sim 0.41 · via baseline — ZeroPrompt: Scaling Prompt-Based Pretraining to 1,000 Tasks Improves
  Zero-Shot Generalization
- arxiv:2407.02880 · 2024-07-03 · sim 0.41 · via baseline — Knowledge Composition using Task Vectors with Learned Anisotropic
  Scaling

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
