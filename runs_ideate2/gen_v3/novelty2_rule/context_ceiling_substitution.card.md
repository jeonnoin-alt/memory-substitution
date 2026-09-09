=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_ceiling_substitution — Does Training Still Add Anything Once the Memory Is Back? Substitution at the In-Context Ceiling and Retention-Routed Memory After Internalization

- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.66 · hf · found via agent/methods
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2502.02046 · 2025-02-04 · preprint · sim 0.61 · hf · found via agent
  Contextual Memory Reweaving in Large Language Models Using Layered
  Latent State Reconstruction
  Memory retention challenges in deep neural architectures have ongoing limitations in the ability to process and recall extended contextual information. Token dependencies degrade as sequence length increases, leading to a decline in coherence and factual consistency across longer outputs. A structured approach is introduced to mitigate this issue through the reweaving of latent states captured at different processing layers, reinforcing token representations over extended sequences. The proposed
- arxiv:2604.27003 · 2026-04-29 · preprint · sim 0.60 · hf · found via agent
  When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents
  Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity dilemma of parametric learning. We show that this challenge does not disappear but resurfaces at the memory level. Under a limited context window, old and new experiences compete during retrieval, relocating the continual-learning bottleneck from parameter updates to memory access. To s
- arxiv:2601.19897 · 2026-01-27 · preprint · sim 0.59 · hf · found via methods
  Self-Distillation Enables Continual Learning
  Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple meth
- arxiv:2606.22844 · 2026-06-22 · preprint · sim 0.57 · hf · found via agent
  RaMem: Contextual Reinstatement for Long-term Agentic Memory
  Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We r
- arxiv:2609.01532 · 2026-09-01 · preprint · sim 0.57 · hf · found via methods
  Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
  Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while for
- arxiv:2606.03746 · 2026-06-02 · preprint · sim 0.57 · hf · found via agent/mechanism_home
  Qwen-Image-Flash: Beyond Objective Design
  Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspective, focusing on the training recipe that critically shapes student performance. Using Qwen-Image-2.0 as a representative case, we systematically investigate three factors in unified text-to-image generation and instruction-guided image editing distillat
- arxiv:2605.08374 · 2026-05-12 · preprint · sim 0.56 · hf · found via agent
  MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs
  Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency chains through which memories enable the creation of future memories. We introduce MemQ, which applies TD(λ) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. Credit wei
- arxiv:2607.17247 · 2026-07-19 · preprint · sim 0.56 · hf · found via mechanism_home
  Distilled Reinforcement Learning for LLM Post-training
  Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment. Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). However, RL relies on coarse-grained outcome supervision, resulting in difficult credit assignment and limited capability to acquire new knowledge. OPD, meanwhile, unconditionally matches teacher logits through KL divergence, which creates a dilemma: similar teachers provide little new
- arxiv:2606.11173 · 2026-06-09 · preprint · sim 0.55 · hf · found via methods
  The Role of Feedback Alignment in Self-Distillation
  Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this contex

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2605.10781 · 2026-05-11 · sim 0.53 · via mechanism_home — Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR
- arxiv:2603.18272 · 2026-03-18 · sim 0.51 · via baseline — Retrieval-Augmented LLM Agents: Learning to Learn from Experience
- arxiv:2605.22731 · 2026-05-21 · sim 0.50 · via mechanism_home — Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation
- arxiv:2510.19316 · 2025-10-22 · sim 0.50 · via mechanism_home — KORE: Enhancing Knowledge Injection for Large Multimodal Models via
  Knowledge-Oriented Augmentations and Constraints
- arxiv:2605.12419 · 2026-05-12 · sim 0.48 · via adjacent — ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
