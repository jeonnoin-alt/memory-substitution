=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: responsible_item_attribution_benchmark — Which Item Did It? A Seed-Replicated Intervention Benchmark for Attributing Agent Failures to Retrieved Memory Items

- arxiv:2606.25449 · 2026-07-21 · preprint · sim 0.53 · hf · found via agent
  Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One
  A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain. We call this brittle memory. The information loss is definitional; the finding is behavioral, and it turns on one thing, whether the memory kept a re-derivation basis (the source) rather than the answer. We
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.52 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2608.20627 · 2026-08-20 · preprint · sim 0.50 · hf · found via methods
  When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation
  Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the kno
- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.43 · hf · found via methods
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2509.10401 · 2025-09-12 · preprint · sim 0.43 · hf · found via agent/methods
  Abduct, Act, Predict: Scaffolding Causal Inference for Automated Failure Attribution in Multi-Agent Systems
  Failure attribution in multi-agent systems -- pinpointing the exact step where a decisive error occurs -- is a critical yet unsolved challenge. Current methods treat this as a pattern recognition task over long conversation logs, leading to critically low step-level accuracy (below 17\%), which renders them impractical for debugging complex systems. Their core weakness is a fundamental inability to perform robust counterfactual reasoning: to determine if correcting a single action would have act
- arxiv:2605.29463 · 2026-05-31 · preprint · sim 0.43 · hf · found via agent
  Honest Lying: Understanding Memory Confabulation in Reflexive Agents
  Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR
- arxiv:2605.25338 · 2026-05-25 · preprint · sim 0.41 · hf · found via agent/methods
  CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures
  Large language model (LLM) agents frequently fail on multi-step tasks involving reasoning, tool use, and environment interaction. While such failures are typically logged or retried heuristically, they contain structured signals about where execution broke down. We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision. CausalFlow models execution traces as sequential chains of dependent steps and computes 
- arxiv:2607.01480 · 2026-07-01 · preprint · sim 0.39 · hf · found via agent
  Procedural Memory Distillation: Online Reflection for Self-Improving Language Models
  Reinforcement learning with verifiable rewards (RLVR), along with recent selfdistillation variants such as SDPO, evaluates each rollout against a verifier and updates the policy from that episode-level signal. However, the richer procedural information in the rollout is rarely retained or reused. Across episodes and epochs, the model repeatedly encounters related problems under a changing policy, producing cross-episode signals that episode-local updates cannot capture: which strategies consiste
- arxiv:2509.08682 · 2025-09-10 · preprint · sim 0.38 · hf · found via agent/methods
  Automatic Failure Attribution and Critical Step Prediction Method for Multi-Agent Systems Based on Causal Inference
  Multi-agent systems (MAS) are critical for automating complex tasks, yet their practical deployment is severely hampered by the challenge of failure attribution. Current diagnostic tools, which rely on statistical correlations, are fundamentally inadequate; on challenging benchmarks like Who\&When, state-of-the-art methods achieve less than 15\% accuracy in locating the root-cause step of a failure. To address this critical gap, we introduce the first failure attribution framework for MAS ground
- arxiv:2605.24941 · 2026-05-24 · preprint · sim 0.37 · hf · found via agent
  Memory-Induced Tool-Drift in LLM Agents
  Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production systems. We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. We call this memory-induced tool-drift and operationalize it through MEMDRIFT,

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- s2:1a28d106c0b61d61d9804746ec45783ce40769bb · 2018-12-01 · sim 0.37 · via baseline — Single-Trial EEG Predicts Memory Retrieval Using Leave-One-Subject-Out Classification
- arxiv:2303.09962 · 2023-03-17 · sim 0.35 · via mechanism_home — Adversarial Counterfactual Visual Explanations
- arxiv:2007.12986 · 2020-08-24 · sim 0.33 · via mechanism_home — Counterfactual Evaluation of Slate Recommendations with Sequential Reward Interactions
- arxiv:2407.11867 · 2024-07-16 · sim 0.33 · via baseline — Single Layer Single Gradient Unlearning
- arxiv:2608.04509 · 2026-08-05 · sim 0.32 · via mechanism_home — CARGO-VL: Counterfactual Arbitration with Risk-Constrained Group Optimization for Vision-Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
