=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_ceiling_substitution — Does Training Still Add Anything Once the Memory Is Back? Substitution at the In-Context Ceiling and Retention-Routed Memory After Internalization

- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.66 · hf · found via methods
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2608.12218 · 2026-08-12 · preprint · sim 0.57 · hf · found via mechanism_home
  Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge
  Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which 
- arxiv:2605.08374 · 2026-05-12 · preprint · sim 0.56 · hf · found via agent
  MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs
  Episodic memory allows LLM agents to accumulate and retrieve experience, but current methods treat each memory independently, i.e., evaluating retrieval quality in isolation without accounting for the dependency chains through which memories enable the creation of future memories. We introduce MemQ, which applies TD(λ) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. Credit wei
- arxiv:2607.17247 · 2026-07-19 · preprint · sim 0.56 · hf · found via agent
  Distilled Reinforcement Learning for LLM Post-training
  Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment. Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). However, RL relies on coarse-grained outcome supervision, resulting in difficult credit assignment and limited capability to acquire new knowledge. OPD, meanwhile, unconditionally matches teacher logits through KL divergence, which creates a dilemma: similar teachers provide little new
- arxiv:2402.02868 · 2024-02-05 · preprint · sim 0.56 · hf · found via mechanism_home
  Fine-tuning Reinforcement Learning Models is Secretly a Forgetting
  Mitigation Problem
  Fine-tuning is a widespread technique that allows practitioners to transfer pre-trained capabilities, as recently showcased by the successful applications of foundation models. However, fine-tuning reinforcement learning (RL) models remains a challenge. This work conceptualizes one specific cause of poor transfer, accentuated in the RL setting by the interplay between actions and observations: forgetting of pre-trained capabilities. Namely, a model deteriorates on the state subspace of the downs
- arxiv:2306.10480 · 2023-06-18 · preprint · sim 0.54 · hf · found via agent
  IF2Net: Innately Forgetting-Free Networks for Continual Learning
  Continual learning can incrementally absorb new concepts without interfering with previously learned knowledge. Motivated by the characteristics of neural networks, in which information is stored in weights on connections, we investigated how to design an Innately Forgetting-Free Network (IF2Net) for continual learning context. This study proposed a straightforward yet effective learning paradigm by ingeniously keeping the weights relative to each seen task untouched before and after learning a 
- arxiv:2504.05571 · 2025-04-08 · preprint · sim 0.52 · hf · found via mechanism_home
  Knowledge-Instruct: Effective Continual Pre-training from Limited Data
  using Instructions
  While Large Language Models (LLMs) acquire vast knowledge during pre-training, they often lack domain-specific, new, or niche information. Continual pre-training (CPT) attempts to address this gap but suffers from catastrophic forgetting and inefficiencies in low-data regimes. We introduce Knowledge-Instruct, a novel approach to efficiently inject knowledge from limited corpora through pure instruction-tuning. By generating information-dense synthetic instruction data, it effectively integrates 
- arxiv:2607.13591 · 2026-07-15 · preprint · sim 0.51 · hf · found via agent
  Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents
  Large Language Model (LLM) agents increasingly rely on external memory systems to accumulate experience across tasks. Yet nearly all existing approaches, from graph-structured memories to reflective insight stores, access memory through fixed, hand-designed heuristics. We argue that this static view of memory is a core bottleneck for agentic learning because optimal memory behavior is fundamentally context-dependent. The early stages of the tasks, benefit from minimal retrieval because memory is
- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.50 · hf · found via agent
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2510.19316 · 2025-10-22 · preprint · sim 0.50 · hf · found via adjacent/mechanism_home
  KORE: Enhancing Knowledge Injection for Large Multimodal Models via
  Knowledge-Oriented Augmentations and Constraints
  Large Multimodal Models encode extensive factual knowledge in their pre-trained weights. However, its knowledge remains static and limited, unable to keep pace with real-world developments, which hinders continuous knowledge acquisition. Effective knowledge injection thus becomes critical, involving two goals: knowledge adaptation (injecting new knowledge) and knowledge retention (preserving old knowledge). Existing methods often struggle to learn new knowledge and suffer from catastrophic forge

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2410.01380 · 2024-10-02 · sim 0.48 · via mechanism_home — Knowledge Entropy Decay during Language Model Pretraining Hinders New Knowledge Acquisition
- arxiv:2606.01967 · 2026-06-01 · sim 0.48 · via mechanism_home — Training Prompt Matters: State-Adaptive Optimization for Robust Fine-Tuning
- arxiv:2412.14964 · 2024-12-19 · sim 0.47 · via adjacent — Knowledge Injection via Prompt Distillation
- arxiv:2607.08393 · 2026-07-09 · sim 0.47 · via mechanism_home — Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning
- arxiv:2405.05904 · 2024-05-09 · sim 0.46 · via mechanism_home — Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
