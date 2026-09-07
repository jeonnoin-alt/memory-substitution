=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: need_blind_compaction_audit — Need-Blind by Construction: A Counterfactual Audit of What Agent Context Compaction Drops, and Why Summary Fidelity Does Not Predict Task Success

- arxiv:2607.05378 · 2026-07-06 · preprint · sim 0.70 · hf
  CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents
  Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs wi
- arxiv:2606.17016 · 2026-06-15 · preprint · sim 0.69 · hf
  TokenPilot: Cache-Efficient Context Management for LLM Agents
  As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, 
- arxiv:2605.05191 · 2026-05-06 · preprint · sim 0.66 · hf
  LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents
  Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information. Naively accumulating all intermediate content can overwhelm the agent, increasing costs and the risk of errors. We propose that effective context management should be adaptive: parts of the agent's trajectory are maintained at different levels of detail depending on their current relevance to the task. To operationalize this principle, we introduce Context-ReAct, a genera
- arxiv:2608.09290 · 2026-08-11 · preprint · sim 0.64 · hf
  OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review
  LLM-based code review agents promise scalable, always-on review, yet current systems suffer from two intertwined weaknesses: (1) non-determinism--unbounded tool use makes review outcomes unstable, and (2) context locality--the reviewer's access remains bounded to the diff, capping discoverable issue depth. Both give rise to three challenges: misaligned context retrieval, a coherence-efficiency trade-off in multi-file pull requests, and hallucinated comments that erode trust. To address these, we
- arxiv:2606.11213 · 2026-05-01 · preprint · sim 0.64 · hf
  Beyond Compaction: Structured Context Eviction for Long-Horizon Agents
  We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon. As a session accumulates history, CWL keeps the context within budget through graduated, semantically-aware eviction: the agent annotates its trajectory as typed, dependency-linked episodes as work proceeds, and a deterministic, LLM-free policy evicts content in priority order within that structure when a token budget is exceeded. CWL preserves user 
- arxiv:2606.30005 · 2026-06-29 · preprint · sim 0.64 · hf
  LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard
  Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window. Recent systems make context management agent- or system-controlled, but they either learn a compression policy that discards evidence or manage context in a layer the agent never sees. We argue both leave a more basic gap unaddressed. Frontier language models are proprioceptively blind to their own context. From the prompt alone they cannot see how large, how old, or how used each block 
- arxiv:2510.00615 · 2025-10-01 · preprint · sim 0.63 · hf
  ACON: Optimizing Context Compression for Long-horizon LLM Agents
  Large language models (LLMs) are increasingly deployed as agents in dynamic, real-world environments, where success requires both reasoning and effective tool use. A central challenge for agentic tasks is the growing context length, as agents must accumulate long histories of actions and observations. This expansion raises costs and reduces efficiency in long-horizon tasks, yet prior work on context compression has mostly focused on single-step tasks or narrow applications. We introduce Agent Co
- arxiv:2607.27250 · 2026-07-28 · preprint · sim 0.63 · hf
  Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories
  Persistent context files (AGENTS.md, CLAUDE.md) are standard practice for guiding AI coding agents, yet evidence for their effectiveness is contradictory. We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation. Context strategy does not measurably move correctness on either agent (bounded to <=10-15pp via equivalence testing). 
- arxiv:2603.00822 · 2026-05-04 · preprint · sim 0.63 · hf
  ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files
  As Large Language Model (LLM) agents increasingly execute complex, autonomous software engineering tasks, developers rely on natural language instruction files such as AGENTS.md to express project-specific coding conventions, tooling restrictions, and architectural boundaries. However, because these instructions remain passive text, agents frequently violate documented constraints due to context window saturation or conflicting local context. In autonomous settings without real-time human superv
- arxiv:2606.23525 · 2026-06-22 · preprint · sim 0.62 · hf
  Self-Compacting Language Model Agents
  Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. We propose SelfCompact, a scaffold that allows the model itself to decide when and how to compact. Specifically, it pairs t

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
