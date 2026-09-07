=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: memory_or_instruction_v6 — Is Your Agent's Memory Just an Un-Optimized Prompt? Residual Memory Value at an Episode-Disjoint, Level-Matched Optimized Instruction in ALFWorld

- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.63 · hf
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2605.29463 · 2026-05-31 · preprint · sim 0.58 · hf
  Honest Lying: Understanding Memory Confabulation in Reflexive Agents
  Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR
- arxiv:2605.18421 · 2026-05-18 · preprint · sim 0.57 · hf
  EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective
  Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution. However, memory is also essential for agents, as it enables them to store, update, and retrieve information over time. This ability remains under-evaluated, largely because existing benchmarks do not provide a systematic way to assess memory mechanisms. In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two a
- arxiv:2607.05202 · 2026-07-06 · preprint · sim 0.54 · hf
  EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer
  Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domai
- arxiv:2608.13546 · 2026-08-13 · preprint · sim 0.53 · hf
  Alaya-EVOKE: From Linear-Scaling Supervision to Endless World
  Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state
- arxiv:2605.13880 · 2026-05-11 · preprint · sim 0.53 · hf
  PREPING: Building Agent Memory without Tasks
  Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions. However, regardless of how it is built, an agent faces a cold-start gap when first introduced to a new environment without any task-specific experience available. In this paper, we study pre-task memory construction: whether an agent can build procedural memory before observing any target-environment tasks, using only self-generated synthetic practice. Yet, synthetic inte
- arxiv:2606.05684 · 2026-06-04 · preprint · sim 0.52 · hf
  AdaMEM: Test-Time Adaptive Memory for Language Agents
  A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions. While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation. Consequently, agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. To address this rigidity, we propose the Adaptive Memory Agent (AdaMEM), a novel framework for agent test-time adaptation. Without upda
- arxiv:2605.13941 · 2026-05-13 · preprint · sim 0.52 · hf
  EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents
  Long-term memory is essential for LLM agents that operate across multiple sessions, yet existing memory systems treat retrieval infrastructure as fixed: stored content evolves while scoring functions, fusion strategies, and answer-generation policies remain frozen at deployment. We argue that truly adaptive memory requires co-evolution at two levels: the stored knowledge and the retrieval mechanism that queries it. We present EvolveMem, a self-evolving memory architecture that exposes its full r
- arxiv:2607.21273 · 2026-07-23 · preprint · sim 0.52 · hf
  The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works
  Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4B/8B on ALFWorld, a potential-based prediction reward drives every run into a degenerate absorbing state (prediction accuracy -> 1.0, task success -> 0,episode length pinned at the horizon): the "dark
- arxiv:2605.12978 · 2026-05-13 · preprint · sim 0.51 · hf
  Useful Memories Become Faulty When Continuously Updated by LLMs
  Learning from past experience benefits from two complementary forms of memory: episodic traces -- raw trajectories of what happened -- and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising self-improving agents without parameter updates. Yet we find that such consolidated m

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

## Web search adjacents (server-side WebSearch subagent, 7 queries)

Each arXiv id was re-resolved through the S2 API (id lookup, then title search) and the HF papers API. Unverified ids must not be cited.

- 2507.19457 · 2025-07 · verified
  GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
  why close: This is the GEPA-style reflective prompt optimizer itself, the mechanism the claim says can absorb a procedural memory bank's value into a single instruction.
- 2603.15666 · 2026-03 · verified
  Compiled Memory: Not More Information, but More Precise Instructions for Language Agents
  why close: Proposes Atlas, a memory kernel that compiles accumulated task experience directly into an agent's instruction (rather than retrieved context), matching the claim's mechanism of memory being distilled into an optimized instruction.
- 2603.21520 · 2026-03 · verified
  Generalizable Self-Evolving Memory for Automatic Prompt Optimization (MemAPO)
  why close: Directly reframes prompt optimization as self-evolving memory accumulation, the same coupling of memory-bank content and optimized prompts the claim examines for redundancy/absorption.
- 2606.29178 · 2026-06 · UNVERIFIED id
  Selective Memory Retention for Long-Horizon LLM Agents
  why close: Evaluates memory-augmented policies under a train-on-100/held-out-50 split, the same held-out-vs-training-episode control structure the claim uses to isolate residual memory value.
- 2609.00549 · 2026-09 · verified
  Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents
  why close: Introduces the Retrieval-Invoked Actual-Use Effect (RAE) showing retrieved skills/memory often add zero or negative same-task value once a policy already performs well, mirroring the claim's near-zero residual-value finding.
- 2603.18272 · 2026-03 · verified
  Retrieval-Augmented LLM Agents: Learning to Learn from Experience
  why close: Directly compares ExpeL-style extracted insights against retrieved trajectories on ALFWorld, the same benchmark and insight-vs-retrieval framing central to the claim.
- 2605.07164 · 2026-05 · verified
  Rethinking Experience Utilization in Self-Evolving Language Model Agents
  why close: Examines redundancy and diminishing marginal value of accumulated experience/trajectories as agents self-evolve, relevant to why a memory bank's residual value can shrink once its content is folded into the policy or instruction.
- 2606.04536 · 2026-06 · verified
  Scaling Self-Evolving Agents via Parametric Memory (TMEM)
  why close: Argues prompt-space memory agents cannot truly learn from experience unless it alters the policy, framing the same absorption-vs-residual-value question the claim raises about instructions versus a memory bank.
- 2603.07670 · 2026-03 · verified
  Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
  why close: Survey covering mechanisms and evaluation of agent memory systems.
- 2606.10616 · 2026-06 · verified
  Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents
  why close: Studies constrained optimization of what an agent retains in memory relative to task performance.
- 2607.03726 · 2026-07 · verified
  SelfMem: Self-Optimizing Memory for AI Agents
  why close: Treats the memory-writing procedure itself as something optimized from training feedback.
- 2604.24594 · 2026-04 · verified
  Skill Retrieval Augmentation for Agentic AI
  why close: Investigates whether retrieved skills provide genuine additional benefit beyond baseline competence.
