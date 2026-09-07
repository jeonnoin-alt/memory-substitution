=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: first_item_additive_rest_substitutive — Additive at One Item, Substitutive at Seven: The Dose-Response of Retrieved Experience After Memory-Free Internalization

- arxiv:2606.05633 · 2026-06-04 · preprint · sim 0.58 · hf
  Answer Presence Drives RAG Rewriting Gains
  Retrieval-augmented QA pipelines often route retrieved passages through an LLM rewriter before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compi
- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.51 · hf
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2608.03796 · 2026-08-04 · preprint · sim 0.47 · hf
  Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss
  Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-K l
- arxiv:2209.15189 · 2022-09-30 · preprint · sim 0.46 · hf
  Learning by Distilling Context
  Language models significantly benefit from context tokens, such as prompts or scratchpads. They perform better when prompted with informative instructions, and they acquire new reasoning capabilities by generating a scratch-pad before predicting the final answers. However, they do not internalize these performance gains, which disappear when the context tokens are gone. Our work proposes to apply context distillation so that a language model can improve itself by internalizing these gains. Concr
- arxiv:2512.10696 · 2025-12-11 · preprint · sim 0.45 · hf
  Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
  Procedural memory enables large language model (LLM) agents to internalize "how-to" knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a "passive accumulation" paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose ReMe (Remember Me, Refine Me), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle vi
- arxiv:2606.04703 · 2026-06-03 · preprint · sim 0.44 · hf
  Rethinking Continual Experience Internalization for Self-Evolving LLM Agents
  Experience internalization converts contextual experience from past interactions into reusable parametric capability, offering a promising path toward continual learning in large language models (LLMs). While prior work has predominantly focused on single-iteration transfer, we discover that under multi-iteration experience learning, existing methods suffer from a progressive capability collapse rather than compounding improvement. We systematically examine this failure through three vital dimen
- arxiv:2505.24850 · 2025-05-30 · preprint · sim 0.43 · hf
  Harnessing Negative Signals: Reinforcement Distillation from Teacher
  Data for LLM Reasoning
  Recent advances in model distillation demonstrate that data from advanced reasoning models (e.g., DeepSeek-R1, OpenAI's o1) can effectively transfer complex reasoning abilities to smaller, efficient student models. However, standard practices employ rejection sampling, discarding incorrect reasoning examples -- valuable, yet often underutilized data. This paper addresses the critical question: How can both positive and negative distilled reasoning traces be effectively leveraged to maximize LLM 
- arxiv:2602.16093 · 2026-02-17 · preprint · sim 0.43 · hf
  Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities
  Post-training endows pretrained LLMs with a variety of desirable skills, including instruction-following, reasoning, and others. However, these post-trained LLMs only encode knowledge up to a cut-off date, necessitating continual adaptation. Unfortunately, existing solutions cannot simultaneously learn new knowledge from an adaptation document corpora and mitigate the forgetting of earlier learned capabilities. To address this, we introduce Distillation via Split Contexts (DiSC), a simple contex
- arxiv:2607.25659 · 2026-07-28 · preprint · sim 0.41 · hf
  CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization
  Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria. Yet in GRPO-style pipelines, these structured judgments are reduced to a scalar response-level reward and converted into a response-level advantage, which is broadcast uniformly to all generated tokens. This leaves no explicit mechanism for allocating credit within a response, even when different criteria are grounded in different spans, formatting decisions, or semantic ch
- arxiv:2207.05080 · 2022-07-11 · preprint · sim 0.39 · hf
  Learning an evolved mixture model for task-free continual learning
  Recently, continual learning (CL) has gained significant interest because it enables deep learning models to acquire new knowledge without forgetting previously learnt information. However, most existing works require knowing the task identities and boundaries, which is not realistic in a real context. In this paper, we address a more challenging and realistic setting in CL, namely the Task-Free Continual Learning (TFCL) in which a model is trained on non-stationary data streams with no explicit

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
