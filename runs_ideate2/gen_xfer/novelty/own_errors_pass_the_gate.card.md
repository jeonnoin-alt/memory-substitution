=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: own_errors_pass_the_gate — The Reader Cannot Grade Its Own Homework: Self-Authored Contamination Evades Read-Time Detection in Agent Experience Stores

- arxiv:2606.24428 · 2026-06-23 · preprint · sim 0.55 · hf · found via agent
  Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning
  Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. However, existing experience learning methods mostly rely on single-agent loops, where the same agent executes tasks, summarizes outcomes, and determines memory content. This setup makes agents vulnerable to the Self-Confirmation Trap: wrong-but-self-consistent trajectories are misidentified as successful experience, leading to cumulative errors during retrieval and reuse
- arxiv:2605.21856 · 2026-05-21 · preprint · sim 0.54 · hf · found via agent
  The Illusion of Reasoning: Exposing Evasive Data Contamination in LLMs via Zero-CoT Truncation
  Large language models (LLMs) have demonstrated impressive reasoning abilities across a wide range of tasks, but data contamination undermines the objective evaluation of these capabilities. This problem is further exacerbated by malicious model publishers who use evasive, or indirect, contamination strategies, such as paraphrasing benchmark data to evade existing detection methods and artificially boost leaderboard performance. Current approaches struggle to reliably detect such stealthy contami
- arxiv:2605.24216 · 2026-05-22 · preprint · sim 0.51 · hf · found via agent
  Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning
  Monitoring autonomous large language model (LLM) agents for covert malicious behavior is challenging due to delayed, context-dependent, and long-horizon attack patterns. Agents may pursue hidden objectives while maintaining superficially benign behavior, making detection difficult even with full trajectory access. Prior monitoring approaches improve scaffolding or ensemble aggregation, but treat each trajectory independently and do not learn from prior monitoring experience. Moreover, standard r
- arxiv:2606.21884 · 2026-06-20 · preprint · sim 0.50 · hf · found via baseline
  A Verifiable Search Is Not a Learnable Chain-of-Thought
  It is tempting to assume any task solvable by a short program can be taught to a model as its chain-of-thought: write the steps out, fine-tune, and the model follows. This paper shows the assumption fails for an identifiable class of procedures. The testbed is nine reasoning tasks, each from a deterministic generator; public and hidden splits share generators, so held-out data proxies test accuracy. I reverse-engineer the generators into Python solvers, render them as chain-of-thought, and disti
- arxiv:2512.16962 · 2025-12-18 · preprint · sim 0.50 · hf · found via agent
  MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval
  Large Language Model (LLM) agents increasingly rely on long-term memory and Retrieval-Augmented Generation (RAG) to persist experiences and refine future performance. While this experience learning capability enhances agentic autonomy, it introduces a critical, unexplored attack surface, i.e., the trust boundary between an agent's reasoning core and its own past. In this paper, we introduce MemoryGraft. It is a novel indirect injection attack that compromises agent behavior not through immediate
- arxiv:2604.27586 · 2026-04-30 · preprint · sim 0.50 · hf · found via agent
  Trace-Level Analysis of Information Contamination in Multi-Agent Systems
  Reasoning over heterogeneous artifacts (PDFs, spreadsheets, slide decks, etc.) increasingly occurs within structured agent workflows that iteratively extract, transform, and reference external information. In these workflows, uncertainty is not merely an input-quality issue: it can redirect decomposition and routing decisions, reshape intermediate state, and produce qualitatively different execution trajectories. We study this phenomenon by treating uncertainty as a controlled variable: we injec
- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.49 · hf · found via agent
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2603.27148 · 2026-03-28 · preprint · sim 0.49 · hf · found via agent
  SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do
  When an LLM agent reads a confidential file, then writes a summary, then emails it externally, no single step is unsafe, but the sequence is a data leak. We call this safety drift: individually safe actions compounding into violations. Prior work has measured this problem; we predict it. SafetyDrift models agent safety trajectories as absorbing Markov chains, computing the probability that a trajectory will reach a violation within a given number of steps via closed form absorption analysis. A c
- arxiv:2608.03509 · 2026-08-04 · preprint · sim 0.48 · hf · found via methods
  SkillJack: Persistent Skill Backdoors in Self-Evolving Agents
  Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present SkillJack, the first attack that exploits the experience-to-skill pipeline of self-evolvin
- arxiv:2602.09383 · 2026-02-10 · preprint · sim 0.48 · hf · found via mechanism_home
  BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation
  LLM-as-a-Judge has been widely adopted across various research and practical applications, yet the robustness and reliability of its evaluation remain a critical issue. A core challenge it faces is bias, which has primarily been studied in terms of known biases and their impact on evaluation outcomes, while automated and systematic exploration of potential unknown biases is still lacking. Nevertheless, such exploration is crucial for enhancing the robustness and reliability of evaluations. To br

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2507.02778 · 2025-07-03 · sim 0.47 · via mechanism_home — Self-Correction Bench: Revealing and Addressing the Self-Correction
  Blind Spot in LLMs
- arxiv:2608.26295 · 2026-08-26 · sim 0.45 · via baseline — MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models
- arxiv:2505.17100 · 2025-05-21 · sim 0.43 · via mechanism_home — Any Large Language Model Can Be a Reliable Judge: Debiasing with a
  Reasoning-based Bias Detector
- arxiv:2410.13640 · 2025-03-13 · sim 0.42 · via adjacent — Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation
- arxiv:2602.16802 · 2026-02-18 · sim 0.39 · via adjacent — References Improve LLM Alignment in Non-Verifiable Domains

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
