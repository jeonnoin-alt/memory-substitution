=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_ceiling_substitution — Does Training Still Add Anything Once the Memory Is Back? Substitution at the In-Context Ceiling and Retention-Routed Memory After Internalization

- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.66 · hf
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2502.02046 · 2025-02-04 · preprint · sim 0.61 · hf
  Contextual Memory Reweaving in Large Language Models Using Layered
  Latent State Reconstruction
  Memory retention challenges in deep neural architectures have ongoing limitations in the ability to process and recall extended contextual information. Token dependencies degrade as sequence length increases, leading to a decline in coherence and factual consistency across longer outputs. A structured approach is introduced to mitigate this issue through the reweaving of latent states captured at different processing layers, reinforcing token representations over extended sequences. The proposed
- arxiv:2604.27003 · 2026-04-29 · preprint · sim 0.60 · hf
  When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents
  Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity dilemma of parametric learning. We show that this challenge does not disappear but resurfaces at the memory level. Under a limited context window, old and new experiences compete during retrieval, relocating the continual-learning bottleneck from parameter updates to memory access. To s
- arxiv:2601.19897 · 2026-01-27 · preprint · sim 0.59 · hf
  Self-Distillation Enables Continual Learning
  Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple meth
- arxiv:2606.22844 · 2026-06-22 · preprint · sim 0.57 · hf
  RaMem: Contextual Reinstatement for Long-term Agentic Memory
  Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We r
- arxiv:2609.01532 · 2026-09-01 · preprint · sim 0.57 · hf
  Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
  Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while for
- arxiv:2606.03746 · 2026-06-02 · preprint · sim 0.57 · hf
  Qwen-Image-Flash: Beyond Objective Design
  Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspective, focusing on the training recipe that critically shapes student performance. Using Qwen-Image-2.0 as a representative case, we systematically investigate three factors in unified text-to-image generation and instruction-guided image editing distillat
- arxiv:2605.08374 · 2026-05-12 · preprint · sim 0.56 · hf
  MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs
  Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency chains through which memories enable the creation of future memories. We introduce MemQ, which applies TD(λ) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. Credit wei
- arxiv:2606.11173 · 2026-06-09 · preprint · sim 0.55 · hf
  The Role of Feedback Alignment in Self-Distillation
  Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this contex
- arxiv:2412.15115 · 2024-12-19 · preprint · sim 0.54 · hf
  Qwen2.5 Technical Report
  In this report, we introduce Qwen2.5, a comprehensive series of large language models (LLMs) designed to meet diverse needs. Compared to previous iterations, Qwen 2.5 has been significantly improved during both the pre-training and post-training stages. In terms of pre-training, we have scaled the high-quality pre-training datasets from the previous 7 trillion tokens to 18 trillion tokens. This provides a strong foundation for common sense, expert knowledge, and reasoning capabilities. In terms 

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
