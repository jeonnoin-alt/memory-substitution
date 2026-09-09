=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: many_shot_averages_detours — Reading the Whole Bank Averages Out Detours: Many-Shot Context Is Robust to Per-Item Noise Where Top-k Retrieval Commits to It

- arxiv:2608.15797 · 2026-08-16 · preprint · sim 0.49 · hf · found via methods
  KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving
  KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tokens until reaching the length limit. We characterize much of this loss as an information gapf caused by missing context, rather than a capability gap caused by limited model capacity. An evicted 7B mo
- arxiv:2603.02473 · 2026-04-12 · preprint · sim 0.49 · hf · found via agent
  Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
  Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval
- arxiv:2503.08640 · 2025-03-11 · preprint · sim 0.48 · hf · found via mechanism_home
  Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse
  Attention
  Many-shot in-context learning has recently shown promise as an alternative to finetuning, with the major advantage that the same model can be served for multiple tasks. However, this shifts the computational burden from training-time to inference-time, making deployment of many-shot ICL challenging to justify in-practice. This cost is further increased if a custom demonstration set is retrieved for each inference example. We present Dynamic Block-Sparse Attention, a training-free framework for r
- arxiv:2501.08248 · 2025-01-14 · preprint · sim 0.47 · hf · found via methods
  Eliciting In-context Retrieval and Reasoning for Long-context Large
  Language Models
  Recent advancements in long-context language models (LCLMs) promise to transform Retrieval-Augmented Generation (RAG) by simplifying pipelines. With their expanded context windows, LCLMs can process entire knowledge bases and perform retrieval and reasoning directly -- a capability we define as In-Context Retrieval and Reasoning (ICR^2). However, existing benchmarks like LOFT often overestimate LCLM performance by providing overly simplified contexts. To address this, we introduce ICR^2, a bench
- arxiv:2405.00200 · 2024-04-30 · preprint · sim 0.46 · hf · found via adjacent/mechanism_home/methods
  In-Context Learning with Long-Context Models: An In-Depth Exploration
  As model context lengths continue to increase, the number of demonstrations that can be provided in-context approaches the size of entire training datasets. We study the behavior of in-context learning (ICL) at this extreme scale on multiple datasets and models. We show that, for many datasets with large label spaces, performance continues to increase with hundreds or thousands of demonstrations. We contrast this with example retrieval and finetuning: example retrieval shows excellent performanc
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.43 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2307.08771 · 2023-07-17 · preprint · sim 0.42 · hf · found via baseline
  UPSCALE: Unconstrained Channel Pruning
  As neural networks grow in size and complexity, inference speeds decline. To combat this, one of the most effective compression techniques -- channel pruning -- removes channels from weights. However, for multi-branch segments of a model, channel removal can introduce inference-time memory copies. In turn, these copies increase inference latency -- so much so that the pruned model can be slower than the unpruned model. As a workaround, pruners conventionally constrain certain channels to be prun
- arxiv:2605.07804 · 2026-06-01 · preprint · sim 0.41 · hf · found via baseline
  Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning
  On-policy distillation (OPD) leverages dense teacher rewards to enhance reasoning models. However, scaling OPD to long-horizon tasks exposes a critical flaw: as the student's generated prefix inevitably diverges from the teacher's thought process, the teacher's dense reward loses local exploitability. Continuing to generate and evaluate tokens on these ``drifted'' trajectories not only degrades reward quality but also incurs massive computational waste. To address this, we introduce Prune-OPD, a
- arxiv:2603.24690 · 2026-03-25 · preprint · sim 0.40 · hf · found via mechanism_home
  UniICL: Systematizing Unified Multimodal In-context Learning through a Capability-Oriented Taxonomy
  In-context Learning enables training-free adaptation via demonstrations but remains highly sensitive to example selection and formatting. In unified multimodal models spanning understanding and generation, this sensitivity is exacerbated by cross-modal interference and varying cognitive demands. Consequently, In-context Learning efficacy is often non-monotonic and highly task-dependent. To diagnose these behaviors, we introduce a six-level capability-oriented taxonomy that categorizes the functi
- arxiv:2301.11321 · 2023-01-26 · preprint · sim 0.39 · hf · found via agent
  Trajectory-Aware Eligibility Traces for Off-Policy Reinforcement
  Learning
  Off-policy learning from multistep returns is crucial for sample-efficient reinforcement learning, but counteracting off-policy bias without exacerbating variance is challenging. Classically, off-policy bias is corrected in a per-decision manner: past temporal-difference errors are re-weighted by the instantaneous Importance Sampling (IS) ratio after each action via eligibility traces. Many off-policy algorithms rely on this mechanism, along with differing protocols for cutting the IS ratios to 

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2506.04579 · 2025-06-05 · sim 0.39 · via mechanism_home — Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching
- arxiv:2309.07900 · 2023-09-14 · sim 0.38 · via mechanism_home — Ambiguity-Aware In-Context Learning with Large Language Models
- arxiv:2202.12837 · 2022-02-25 · sim 0.38 · via mechanism_home — Rethinking the Role of Demonstrations: What Makes In-Context Learning
  Work?
- arxiv:2605.13511 · 2026-05-13 · sim 0.36 · via adjacent/mechanism_home — Many-Shot CoT-ICL: Making In-Context Learning Truly Learn
- arxiv:2406.15334 · 2024-06-21 · sim 0.36 · via mechanism_home — Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
