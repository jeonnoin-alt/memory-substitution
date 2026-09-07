=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: wrong_action_fraction_dose — Not How Many, But How Many Are Wrong: The Dose-Response of Injected Experience on Agent Traces Follows the Wrong-Action Fraction, Not Token Load or Item Count

- arxiv:2607.07474 · 2026-07-08 · preprint · sim 0.68 · hf
  Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents
  Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another 
- arxiv:2607.13988 · 2026-07-15 · preprint · sim 0.56 · hf
  TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents
  Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many useful actions that move the agent closer to the goal, yet outcome-only training 
- arxiv:2603.23806 · 2026-05-08 · preprint · sim 0.54 · hf
  Willful Disobedience: Automatically Detecting Failures in Agentic Traces
  AI agents are increasingly embedded in real software systems, where they execute multi-step workflows through multi-turn dialogue, tool invocations, and intermediate decisions. These long execution histories, called agentic traces, make validation difficult. Outcome-only benchmarks can miss critical procedural failures, such as incorrect workflow routing, unsafe tool usage, or violations of prompt-specified rules. This paper presents AgentPex, an AI-powered tool designed to systematically evalua
- arxiv:2608.02276 · 2026-08-03 · preprint · sim 0.51 · hf
  Harness-R1: Learning to Edit Executable Runtime Harnesses from Agent Failure Trajectories
  Agents built around large language models continually accumulate interaction trajectories during deployment, yet their behavior typically remains fixed. Beyond updating model weights, these trajectories can improve the agent harness that constructs context, mediates tools, validates actions, and recovers execution. We introduce Harness-R1, the first method, to our knowledge, that makes failure-conditioned, lifecycle-wide editing of an existing executable runtime a learned capability. It post-tra
- arxiv:2608.20627 · 2026-08-20 · preprint · sim 0.51 · hf
  When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation
  Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the kno
- arxiv:2604.22708 · 2026-04-24 · preprint · sim 0.50 · hf
  Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems
  Failure attribution, i.e., identifying the responsible agent and decisive step of a failure, is particularly challenging in LLM-based multi-agent systems (MAS) due to their natural-language reasoning, nondeterministic outputs, and intricate interaction dynamics. A reliable benchmark is therefore essential to guide and evaluate attribution techniques. Yet existing benchmarks rely on partially observable traces that capture only agent outputs, omitting the inputs and context that developers actual
- arxiv:2606.13174 · 2026-06-11 · preprint · sim 0.50 · hf
  Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents
  Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline
- arxiv:2607.07702 · 2026-07-08 · preprint · sim 0.47 · hf
  From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization
  The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, 
- arxiv:2604.16706 · 2026-04-17 · preprint · sim 0.47 · hf
  Evaluating Tool-Using Language Agents: Judge Reliability, Propagation Cascades, and Runtime Mitigation in AgentProp-Bench
  Automated evaluation of tool-using large language model (LLM) agents is widely assumed to be reliable, but this assumption has rarely been validated against human annotation. We introduce AgentProp-Bench, a 2,000-task benchmark with 2,300 traces across four domains, nine production LLMs, and a 100-label human-validated subset. We quantify judge reliability, characterize error propagation, and evaluate a runtime mitigation. Substring-based judging agrees with human annotation at kappa=0.049 (chan
- arxiv:2606.25852 · 2026-06-24 · preprint · sim 0.46 · hf
  Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
  Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress insi

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
