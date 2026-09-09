=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: guilt_by_coretrieval — Guilt by Co-retrieval: Measuring Reward Contamination of Learned Memory Utilities Against Leave-One-Out Ground Truth

- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.58 · hf · found via agent
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.56 · hf · found via agent
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2211.08714 · 2022-11-16 · preprint · sim 0.51 · hf · found via agent/mechanism_home
  Reward Gaming in Conditional Text Generation
  To align conditional text generation model outputs with desired behaviors, there has been an increasing focus on training the model using reinforcement learning (RL) with reward functions learned from human annotations. Under this framework, we identify three common cases where high rewards are incorrectly assigned to undesirable patterns: noise-induced spurious correlation, naturally occurring spurious correlation, and covariate shift. We show that even though learned metrics achieve high perfo
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.49 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2608.02508 · 2026-08-10 · preprint · sim 0.48 · hf · found via agent/methods
  RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
  Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory R
- arxiv:2606.06475 · 2026-06-04 · preprint · sim 0.48 · hf · found via mechanism_home
  RREDCoT: Segment-Level Reward Redistribution for Reasoning Models
  Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modifications thereof to steer the models to produce Chain-of-Thought (CoT) traces. The final answer can only be verified, and the reward assigned, after the CoT trace is complete, making it a delayed reward problem. GRPO and its modifications correspond to Monte Carlo methods in standard RL, which are k
- arxiv:2601.03468 · 2026-01-06 · preprint · sim 0.47 · hf · found via agent
  Understanding Reward Hacking in Text-to-Image Reinforcement Learning
  Reinforcement learning (RL) has become a standard approach for post-training large language models and, more recently, for improving image generation models, which uses reward functions to enhance generation quality and human preference alignment. However, existing reward designs are often imperfect proxies for true human judgment, making models prone to reward hacking--producing unrealistic or low-quality images that nevertheless achieve high reward scores. In this work, we systematically analy
- arxiv:2506.16507 · 2025-06-19 · preprint · sim 0.47 · hf · found via mechanism_home
  Robust Reward Modeling via Causal Rubrics
  Reward models (RMs) are fundamental to aligning Large Language Models (LLMs) via human feedback, yet they often suffer from reward hacking. They tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality (e.g., factuality, relevance). This occurs because standard training objectives struggle to disentangle these factors, leading to brittle RMs and misaligned 
- arxiv:2607.21106 · 2026-07-23 · preprint · sim 0.47 · hf · found via agent
  AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning
  Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals 
- arxiv:2601.08435 · 2026-01-13 · preprint · sim 0.44 · hf · found via agent
  Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management
  Effective memory management is essential for large language model agents to navigate long-horizon tasks. Recent research has explored using Reinforcement Learning to develop specialized memory manager agents. However, existing approaches rely on final task performance as the primary reward, which results in severe reward sparsity and ineffective credit assignment, providing insufficient guidance for individual memory operations. To this end, we propose Fine-Mem, a unified framework designed for 

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2105.03287 · 2021-05-07 · sim 0.41 · via mechanism_home — Order in the Court: Explainable AI Methods Prone to Disagreement
- arxiv:2501.09620 · 2025-01-16 · sim 0.40 · via mechanism_home — Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment
- arxiv:1907.09701 · 2019-07-23 · sim 0.40 · via mechanism_home — Benchmarking Attribution Methods with Relative Feature Importance
- arxiv:2503.02269 · 2025-03-04 · sim 0.40 · via baseline — Experience Replay with Random Reshuffling
- s2:2b43db82f61a80f375a24564205814c7fc8fb368 · 2020-04-29 · sim 0.39 · via mechanism_home — Co-Learning Non-Negative Correlated and Uncorrelated Features for Multi-View Data

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
