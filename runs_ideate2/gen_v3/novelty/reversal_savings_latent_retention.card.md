=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: reversal_savings_latent_retention — Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory

- arxiv:2511.04228 · 2025-11-06 · preprint · sim 0.55 · hf
  REMIND: Input Loss Landscapes Reveal Residual Memorization in Post-Unlearning LLMs
  Machine unlearning aims to remove the influence of specific training data from a model without requiring full retraining. This capability is crucial for ensuring privacy, safety, and regulatory compliance. Therefore, verifying whether a model has truly forgotten target data is essential for maintaining reliability and trustworthiness. However, existing evaluation methods often assess forgetting at the level of individual inputs. This approach may overlook residual influence present in semantical
- arxiv:2606.26560 · 2026-06-25 · preprint · sim 0.55 · hf
  Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention
  Delta-rule linear attention improves recurrent memory updates by correcting what is already stored at the current write address before writing new content. However, the active correction is still anchored to that same write address. As a result, stale information stored at a different address cannot be actively removed before new content is written elsewhere. We propose Erase-then-Delta Attention (EDA), a memory update rule that decouples where to erase from where to write. The key insight is th
- arxiv:2511.17100 · 2025-11-21 · preprint · sim 0.53 · hf
  Geometric-Disentangelment Unlearning
  Machine unlearning, the removal of a training subset's influence from a deployed model, is critical for privacy preservation and model reliability, yet gradient ascent on forget samples often harms retained knowledge. Existing approaches face a persistent tradeoff between effective forgetting and preservation on the retain set. While previous methods provide useful heuristics, they often lack a formal analysis on how exactly forgetting updates harm retained knowledge, and whether the side effect
- arxiv:2509.05316 · 2025-08-29 · preprint · sim 0.53 · hf
  Standard vs. Modular Sampling: Best Practices for Reliable LLM Unlearning
  A conventional LLM Unlearning setting consists of two subsets -"forget" and "retain", with the objectives of removing the undesired knowledge from the forget set while preserving the remaining knowledge from the retain. In privacy-focused unlearning research, a retain set is often further divided into neighbor sets, containing either directly or indirectly connected to the forget targets; and augmented by a general-knowledge set. A common practice in existing benchmarks is to employ only a singl
- arxiv:2410.14713 · 2024-10-09 · preprint · sim 0.52 · hf
  QuAILoRA: Quantization-Aware Initialization for LoRA
  QLoRA reduces the memory-cost of fine-tuning a large language model (LLM) with LoRA by quantizing the base LLM. However, quantization introduces quantization errors that negatively impact model performance after fine-tuning. In this paper we introduce QuAILoRA, a quantization-aware initialization for LoRA that mitigates this negative impact by decreasing quantization errors at initialization. Our method spends a small amount of computational overhead to compute this quantization-aware initializa
- arxiv:2505.16831 · 2025-09-26 · preprint · sim 0.51 · hf
  Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs
  Unlearning in large language models (LLMs) aims to remove specified data, but its efficacy is typically assessed with task-level metrics like accuracy and perplexity. We demonstrate that these metrics are often misleading, as models can appear to forget while their original behavior is easily restored through minimal fine-tuning. This phenomenon of reversibility suggests that information is merely suppressed, not genuinely erased. To address this critical evaluation gap, we introduce a represent
- arxiv:2601.10566 · 2026-03-17 · preprint · sim 0.51 · hf
  Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure
  Selective knowledge erasure from LLMs is critical for GDPR compliance and model safety, yet current unlearning methods conflate behavioral suppression with true knowledge removal, allowing latent capabilities to persist beneath surface-level refusals. In this work, we address this challenge by introducing Knowledge Immunization Framework (KIF), a representation-aware architecture that distinguishes genuine erasure from obfuscation by targeting internal activation signatures rather than surface o
- arxiv:2509.14624 · 2025-09-18 · preprint · sim 0.50 · hf
  Reveal and Release: Iterative LLM Unlearning with Self-generated Data
  Large language model (LLM) unlearning has demonstrated effectiveness in removing the influence of undesirable data (also known as forget data). Existing approaches typically assume full access to the forget dataset, overlooking two key challenges: (1) Forget data is often privacy-sensitive, rare, or legally regulated, making it expensive or impractical to obtain (2) The distribution of available forget data may not align with how that information is represented within the model. To address these
- arxiv:2607.09236 · 2026-07-10 · preprint · sim 0.48 · hf
  Forget Narrowly, Retain Broadly: Unlearning as an Asymmetric Generalization Problem
  Machine unlearning in LLMs is the targeted removal of specific knowledge while preserving all other capabilities, critical for privacy and safety. Yet existing benchmarks measure it unreliably. They miss knowledge that resurfaces under paraphrased or indirect queries, a failure we call under-forgetting, and lack the semantic, syntactic, and lexical probes needed to verify that unrelated knowledge is preserved, a failure we call over-forgetting. Both failures reflect an asymmetric generalization 
- arxiv:2402.05445 · 2024-02-08 · preprint · sim 0.47 · hf
  Accurate LoRA-Finetuning Quantization of LLMs via Information Retention
  The LoRA-finetuning quantization of LLMs has been extensively studied to obtain accurate yet compact LLMs for deployment on resource-constrained hardware. However, existing methods cause the quantized LLM to severely degrade and even fail to benefit from the finetuning of LoRA. This paper proposes a novel IR-QLoRA for pushing quantized LLMs with LoRA to be highly accurate through information retention. The proposed IR-QLoRA mainly relies on two technologies derived from the perspective of unifie

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
