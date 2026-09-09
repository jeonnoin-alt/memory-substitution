=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: memory_failure_blame_item_vs_set — Who Is to Blame: Attributing Memory-Induced Failures of a Multi-Step Agent to a Single Retrieved Item or to the Set

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.56 · hf · found via agent/methods
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2608.11772 · 2026-08-12 · preprint · sim 0.55 · hf · found via agent
  Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction
  Self-correction is particularly useful when a failure constrains the next repair. Coding agents benefit from this property because compilers, tests, and execution traces turn many failures into typed recovery signals, but broad language-agent tasks often expose only a coarse task failure. This creates a tension for generic recovery playbooks: they broaden the agent's context precisely when the system needs a narrower repair interface, mixing incompatible signals for invalid actions, missing proc
- arxiv:2608.20627 · 2026-08-20 · preprint · sim 0.54 · hf · found via mechanism_home
  When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation
  Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the kno
- arxiv:2509.10401 · 2025-09-12 · preprint · sim 0.54 · hf · found via mechanism_home
  Abduct, Act, Predict: Scaffolding Causal Inference for Automated Failure Attribution in Multi-Agent Systems
  Failure attribution in multi-agent systems -- pinpointing the exact step where a decisive error occurs -- is a critical yet unsolved challenge. Current methods treat this as a pattern recognition task over long conversation logs, leading to critically low step-level accuracy (below 17\%), which renders them impractical for debugging complex systems. Their core weakness is a fundamental inability to perform robust counterfactual reasoning: to determine if correcting a single action would have act
- arxiv:2606.08275 · 2026-06-06 · arXiv.org · sim 0.50 · s2 · found via mechanism_home
  Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures
  When an LLM agent fails -- issues a refund it should not have, calls the wrong tool, leaks data -- existing tooling answers what happened (observability) or whether it passed (evaluation), but not which step caused the failure. The obvious heuristics are wrong: the step that executes the harmful action is usually not the step that decided on it, and LLM-judge attribution is correlational and unreliable (state-of-the-art step-level accuracy on the Who&When benchmark is about 14%). We present Caus
- arxiv:2605.29463 · 2026-05-31 · preprint · sim 0.49 · hf · found via agent
  Honest Lying: Understanding Memory Confabulation in Reflexive Agents
  Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR
- arxiv:2607.24368 · 2026-07-27 · preprint · sim 0.49 · hf · found via agent
  Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory
  Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives. This interface rests on an assumption so natural that it is rarely stated: a memory that is needed will resemble the query that needs it. World knowledge breaks the assumption. A tree-nut allergy should change the answer to a macaron request through their almond-flour ingredient, yet the two texts share no cue a retriever can see. We call this failure mode the implicit-association b
- arxiv:2509.08682 · 2025-09-10 · preprint · sim 0.47 · hf · found via mechanism_home
  Automatic Failure Attribution and Critical Step Prediction Method for Multi-Agent Systems Based on Causal Inference
  Multi-agent systems (MAS) are critical for automating complex tasks, yet their practical deployment is severely hampered by the challenge of failure attribution. Current diagnostic tools, which rely on statistical correlations, are fundamentally inadequate; on challenging benchmarks like Who\&When, state-of-the-art methods achieve less than 15\% accuracy in locating the root-cause step of a failure. To address this critical gap, we introduce the first failure attribution framework for MAS ground
- arxiv:2603.02473 · 2026-04-12 · preprint · sim 0.46 · hf · found via agent
  Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
  Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval
- arxiv:2601.05504 · 2026-01-12 · preprint · sim 0.44 · hf · found via agent/methods
  Memory Poisoning Attack and Defense on Memory Based LLM-Agents
  Large language model agents equipped with persistent memory are vulnerable to memory poisoning attacks, where adversaries inject malicious instructions through query only interactions that corrupt the agents long term memory and influence future responses. Recent work demonstrated that the MINJA (Memory Injection Attack) achieves over 95 % injection success rate and 70 % attack success rate under idealized conditions. However, the robustness of these attacks in realistic deployments and effectiv

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2608.23252 · 2026-08-24 · sim 0.37 · via mechanism_home — The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search
- arxiv:2608.18852 · 2026-08-19 · sim 0.35 · via baseline — SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
- arxiv:2605.01302 · 2026-05-02 · sim 0.34 · via mechanism_home — Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation
- arxiv:2602.00344 · 2026-01-30 · sim 0.33 · via adjacent — When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs
- arxiv:2605.15138 · 2026-05-14 · sim 0.33 · via agent/mechanism_home — Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
