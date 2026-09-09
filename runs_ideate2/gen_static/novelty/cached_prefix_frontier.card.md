=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: cached_prefix_frontier — Prefix Caching Moves the Break-Even: Measured Accuracy–GPU-Second Frontiers for Static, Whole-Bank and Retrieved Experience Prefixes in a Multi-Turn Agent

- arxiv:2607.23159 · 2026-07-30 · preprint · sim 0.64 · hf · found via agent
  CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion
  Test-time search lets small video diffusion models rival larger ones, but costs 2-10x more. All candidates are fully denoised, although most are discarded. Training-free caching makes each rollout 2-3x faster at near-lossless quality. Composition is safe only if lossy caching preserves verifier rankings. We present the first study of whether caching corrupts candidate ranking in video test-time search. On Wan2.1-T2V-1.3B with an adaptive caching wrapper (~2x per-candidate speedup), ImageReward s
- arxiv:2607.12161 · 2026-07-15 · preprint · sim 0.59 · hf · found via agent
  Token Reduction Is Not Cost Reduction
  Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and API-boundary proxies, are commonly evaluated by how much context or tool output they remove. We ask a different question: which interventions actually reduce end-to-end billed cost while preserving task success? Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848 were analyzed, covering 103 tasks, seven repo
- arxiv:2606.20474 · 2026-06-19 · preprint · sim 0.58 · hf · found via mechanism_home
  UltraQuant: 4-bit KV Caching for Context-Heavy Agents
  Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized. We study 4-bit KV-cache compression for this setting, using TurboQuant-style rotation and codebook quantization as a quality anchor and vLLM FP8 KV caching as the deployment anchor. We report three contributions. First, we frame 4-bit KV caching around multi-round agent workloads where task quali
- arxiv:2606.01065 · 2026-05-31 · arXiv.org · sim 0.57 · s2 · found via mechanism_home
  Leyline: KV Cache Directives for Agentic Inference
  Modern KV cache management assumes the chatbot workload: prompts arrive once and the cache grows append-only, so prefix caching and forward-only eviction are correct by construction. Agentic LLMs break this assumption. Their conversations evolve through policy-driven editing: failed tool calls are retried, stale outputs dropped, trajectories pivoted. Two distinct cache problems result. First, identical content moves to new positions between turns, invalidating exact-prefix caches even though the
- arxiv:2605.22850 · 2026-05-16 · arXiv.org · sim 0.56 · s2 · found via mechanism_home
  ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse
  Prefix KV caching has become a key mechanism in LLM serving: it reduces time to first token (TTFT) by avoiding redundant computation across requests that share a prefix (i.e., the system prompt). However, the accumulated KV cache is often larger than what GPU memory and local DRAM can hold. To preserve latency, current systems keep the KV cache in remote DRAM pools, increasing serving-cluster size and cost. In this paper, we explore a different approach: storing the KV cache in S3-compatible obj
- arxiv:2606.21238 · 2026-06-19 · preprint · sim 0.55 · hf · found via methods
  Recency/Frequency Adaptive KV Caching for Large Language Model Serving
  Key-value (KV) caching is a powerful technique for accelerating large language model inference and generation. Inference workloads are large and diverse, which makes them difficult to cache effectively. Existing cache management strategies adopt the least-recently-used policy for evicting cache blocks. However, LRU leads to multiple unrelated workloads flushing each other's caches. To address this, we integrate adaptive caching that dynamically allocates cache space between recently and frequent
- arxiv:2507.07400 · 2025-07-10 · preprint · sim 0.53 · hf · found via agent/mechanism_home/methods
  KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows
  Large language model (LLM) based agentic workflows have become a popular paradigm for coordinating multiple specialized agents to solve complex tasks. To improve serving efficiency, existing LLM systems employ prefix caching to reuse key-value (KV) tensors corresponding to agents' fixed prompts, thereby avoiding redundant computation across repeated invocations. However, current systems typically evict KV caches using a Least Recently Used (LRU) policy, which fails to anticipate future agent usa
- arxiv:2604.03143 · 2026-04-03 · arXiv.org · sim 0.53 · s2 · found via mechanism_home
  TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing
  Multi-agent LLM applications organize execution in synchronized rounds where a central scheduler gathers outputs from all agents and redistributes the combined context. This All-Gather communication pattern creates massive KV Cache redundancy, because every agent's prompt contains the same shared output blocks, yet existing reuse methods fail to exploit it efficiently. We present TokenDance, a system that scales the number of concurrent agents by exploiting the All-Gather pattern for collective 
- s2:6db782df823d9da204a59180305aba81d47b3997 · 2026-09-02 · Proceedings of the 19th ACM International Systems and Storage Conference · sim 0.52 · s2 · found via mechanism_home
  To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems
  Disaggregated LLM serving separates prefill and decode into distinct node pools, interposing a network fabric between the moment a key-value (KV) cache is computed and the moment it is consumed. This architectural shift invalidates a core assumption of classical cache policies: that the cost of a miss is simply recomputation on the same device. In disaggregated systems, a miss triggers both recomputation on a prefill node and a network transfer of the resulting KV block to the decode node—costs 
- arxiv:2605.08441 · 2026-05-08 · preprint · sim 0.52 · hf · found via baseline
  DUET: Optimize Token-Budget Allocation for Reinforcement Learning with Verifiable Rewards
  Reinforcement learning with verifiable rewards (RLVR) generates hundreds of thousands of tokens per training step, with rollout generation dominating the computational cost. The overall token budget can be controlled along two main dimensions: (i) deciding which prompts to allocate rollouts to, and (ii) deciding how long each rollout should be. Prior work has generally controlled only one of these dimensions at a time. We show that jointly tuning both decisions under a shared compute budget impr

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2605.24022 · 2026-05-20 · sim 0.52 · via mechanism_home — Adaptive KV Cache Reuse for Fast Long-Context LLM Serving
- arxiv:2607.14952 · 2026-07-16 · sim 0.51 · via mechanism_home — LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
- s2:1ed0c295dfbc82ded770bdc458d18276f6d12a47 · 2026-06-15 · sim 0.49 · via mechanism_home — SW-SpeedDLM: Sliding Window Speculative Decoding for Diffusion Language Models Under Long Context Constraints
- arxiv:2607.10987 · 2026-07-13 · sim 0.49 · via mechanism_home — [AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows
- arxiv:2608.14624 · 2026-07-16 · sim 0.49 · via mechanism_home — Learning Agent Execution for KV-Cache Management in Agentic Serving

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
