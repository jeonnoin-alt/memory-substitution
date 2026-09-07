=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: coverage_limited_context_count_limited_weights — Coverage-Limited Context, Count-Limited Weights: The Substrate Crossover Lives on the Experience-Collection Axis, Not the Deployment Horizon

- arxiv:2606.17016 · 2026-06-15 · preprint · sim 0.55 · hf
  TokenPilot: Cache-Efficient Context Management for LLM Agents
  As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, 
- arxiv:2608.22695 · 2026-08-24 · preprint · sim 0.49 · hf
  Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing
  Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable pr
- arxiv:2602.11748 · 2026-02-12 · preprint · sim 0.45 · hf
  Think Longer to Explore Deeper: Learn to Explore In-Context via Length-Incentivized Reinforcement Learning
  Achieving effective test-time scaling requires models to engage in In-Context Exploration -- the intrinsic ability to generate, verify, and refine multiple reasoning hypotheses within a single continuous context. Grounded in State Coverage theory, our analysis identifies a critical bottleneck to enabling this capability: while broader state coverage requires longer reasoning trajectories, the probability of sampling such sequences decays exponentially during autoregressive generation, a phenomen
- arxiv:2407.21787 · 2024-07-31 · preprint · sim 0.43 · hf
  Large Language Monkeys: Scaling Inference Compute with Repeated Sampling
  Scaling the amount of compute used to train language models has dramatically improved their capabilities. However, when it comes to inference, we often limit the amount of compute to only one attempt per problem. Here, we explore inference compute as another axis for scaling by increasing the number of generated samples. Across multiple tasks and models, we observe that coverage - the fraction of problems solved by any attempt - scales with the number of samples over four orders of magnitude. In
- arxiv:2606.05633 · 2026-06-04 · preprint · sim 0.43 · hf
  Answer Presence Drives RAG Rewriting Gains
  Retrieval-augmented QA pipelines often route retrieved passages through an LLM rewriter before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compi
- arxiv:2605.25997 · 2026-05-25 · preprint · sim 0.42 · hf
  Deployment-complete benchmarking
  Benchmarks increasingly guide deployment, procurement and scientific screening, yet a score supports only the response it records, not necessarily the deployment action. We introduce deployment-complete benchmarking, which tests whether benchmark evidence determines a deployment action. A benchmark is complete for a claim exactly when the action is constant on each evidence fiber; mixed fibers expose missing deployment information, and completion curves quantify the evidence required to resolve 
- arxiv:2606.25852 · 2026-06-24 · preprint · sim 0.42 · hf
  Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
  Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress insi
- arxiv:2609.02217 · 2026-09-02 · preprint · sim 0.42 · hf
  SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams
  LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of 
- arxiv:2410.16848 · 2024-10-22 · preprint · sim 0.40 · hf
  ETHIC: Evaluating Large Language Models on Long-Context Tasks with High
  Information Coverage
  Recent advancements in large language models (LLM) capable of processing extremely long texts highlight the need for a dedicated evaluation benchmark to assess their long-context capabilities. However, existing methods, like the needle-in-a-haystack test, do not effectively assess whether these models fully utilize contextual information, raising concerns about the reliability of current evaluation techniques. To thoroughly examine the effectiveness of existing benchmarks, we introduce a new met
- arxiv:2505.23522 · 2025-05-29 · preprint · sim 0.39 · hf
  OmniEarth-Bench: Towards Holistic Evaluation of Earth's Six Spheres and
  Cross-Spheres Interactions with Multimodal Observational Earth Data
  Existing benchmarks for Earth science multimodal learning exhibit critical limitations in systematic coverage of geosystem components and cross-sphere interactions, often constrained to isolated subsystems (only in Human-activities sphere or atmosphere) with limited evaluation dimensions (less than 16 tasks). To address these gaps, we introduce OmniEarth-Bench, the first comprehensive multimodal benchmark spanning all six Earth science spheres (atmosphere, lithosphere, Oceansphere, cryosphere, b

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
