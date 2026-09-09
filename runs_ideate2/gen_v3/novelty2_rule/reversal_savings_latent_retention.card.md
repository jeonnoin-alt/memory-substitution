=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: reversal_savings_latent_retention — Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory

- arxiv:2511.04228 · 2025-11-06 · preprint · sim 0.55 · hf · found via agent
  REMIND: Input Loss Landscapes Reveal Residual Memorization in Post-Unlearning LLMs
  Machine unlearning aims to remove the influence of specific training data from a model without requiring full retraining. This capability is crucial for ensuring privacy, safety, and regulatory compliance. Therefore, verifying whether a model has truly forgotten target data is essential for maintaining reliability and trustworthiness. However, existing evaluation methods often assess forgetting at the level of individual inputs. This approach may overlook residual influence present in semantical
- arxiv:2606.26560 · 2026-06-25 · preprint · sim 0.55 · hf · found via agent
  Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention
  Delta-rule linear attention improves recurrent memory updates by correcting what is already stored at the current write address before writing new content. However, the active correction is still anchored to that same write address. As a result, stale information stored at a different address cannot be actively removed before new content is written elsewhere. We propose Erase-then-Delta Attention (EDA), a memory update rule that decouples where to erase from where to write. The key insight is th
- arxiv:2511.17100 · 2025-11-21 · preprint · sim 0.53 · hf · found via agent
  Geometric-Disentangelment Unlearning
  Machine unlearning, the removal of a training subset's influence from a deployed model, is critical for privacy preservation and model reliability, yet gradient ascent on forget samples often harms retained knowledge. Existing approaches face a persistent tradeoff between effective forgetting and preservation on the retain set. While previous methods provide useful heuristics, they often lack a formal analysis on how exactly forgetting updates harm retained knowledge, and whether the side effect
- arxiv:2509.05316 · 2025-08-29 · preprint · sim 0.53 · hf · found via agent
  Standard vs. Modular Sampling: Best Practices for Reliable LLM Unlearning
  A conventional LLM Unlearning setting consists of two subsets -"forget" and "retain", with the objectives of removing the undesired knowledge from the forget set while preserving the remaining knowledge from the retain. In privacy-focused unlearning research, a retain set is often further divided into neighbor sets, containing either directly or indirectly connected to the forget targets; and augmented by a general-knowledge set. A common practice in existing benchmarks is to employ only a singl
- arxiv:2410.14713 · 2024-10-09 · preprint · sim 0.52 · hf · found via agent/mechanism_home
  QuAILoRA: Quantization-Aware Initialization for LoRA
  QLoRA reduces the memory-cost of fine-tuning a large language model (LLM) with LoRA by quantizing the base LLM. However, quantization introduces quantization errors that negatively impact model performance after fine-tuning. In this paper we introduce QuAILoRA, a quantization-aware initialization for LoRA that mitigates this negative impact by decreasing quantization errors at initialization. Our method spends a small amount of computational overhead to compute this quantization-aware initializa
- arxiv:2402.08096 · 2024-02-12 · preprint · sim 0.51 · hf · found via mechanism_home
  An Efficient Rehearsal Scheme for Catastrophic Forgetting Mitigation
  during Multi-stage Fine-tuning
  Incrementally fine-tuning foundational models on new tasks or domains is now the de facto approach in NLP. A known pitfall of this approach is the catastrophic forgetting of prior knowledge that happens during fine-tuning. A common approach to alleviate such forgetting is to rehearse samples from prior tasks during fine-tuning. Several existing works assume a fixed memory buffer to store prior task examples, while relying on inferences (forward passes) with the model at hand for choosing example
- arxiv:2601.18699 · 2026-01-26 · preprint · sim 0.51 · hf · found via mechanism_home
  Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning
  Large language models exhibit remarkable performance across diverse tasks through pre-training and fine-tuning paradigms. However, continual fine-tuning on sequential tasks induces catastrophic forgetting, where newly acquired knowledge interferes with previously learned capabilities. Despite widespread observations of this phenomenon, the mechanistic understanding remains limited. Here, we present a comprehensive mechanistic analysis of catastrophic forgetting in transformer-based LLMs during s
- arxiv:2603.00624 · 2026-02-28 · preprint · sim 0.51 · hf · found via baseline
  IDER: IDempotent Experience Replay for Reliable Continual Learning
  Catastrophic forgetting, the tendency of neural networks to forget previously learned knowledge when learning new tasks, has been a major challenge in continual learning (CL). To tackle this challenge, CL methods have been proposed and shown to reduce forgetting. Furthermore, CL models deployed in mission-critical settings can benefit from uncertainty awareness by calibrating their predictions to reliably assess their confidences. However, existing uncertainty-aware continual learning methods su
- arxiv:2512.20634 · 2025-12-02 · arXiv.org · sim 0.51 · s2 · found via mechanism_home
  Real Time Detection and Quantitative Analysis of Spurious Forgetting in Continual Learning
  Catastrophic forgetting remains a fundamental challenge in continual learning for large language models. Recent work revealed that performance degradation may stem from spurious forgetting caused by task alignment disruption rather than true knowledge loss. However, this work only qualitatively describes alignment, relies on post-hoc analysis, and lacks automatic distinction mechanisms. We introduce the shallow versus deep alignment framework, providing the first quantitative characterization of
- arxiv:2401.05605 · 2024-01-11 · preprint · sim 0.51 · hf · found via mechanism_home
  Scaling Laws for Forgetting When Fine-Tuning Large Language Models
  We study and quantify the problem of forgetting when fine-tuning pre-trained large language models (LLMs) on a downstream task. We find that parameter-efficient fine-tuning (PEFT) strategies, such as Low-Rank Adapters (LoRA), still suffer from catastrophic forgetting. In particular, we identify a strong inverse linear relationship between the fine-tuning performance and the amount of forgetting when fine-tuning LLMs with LoRA. We further obtain precise scaling laws that show forgetting increases

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2406.06564 · 2024-06-03 · sim 0.48 · via mechanism_home — SwitchLoRA: Switched Low-Rank Adaptation Can Learn Full-Rank Information
- arxiv:2402.05445 · 2024-02-08 · sim 0.47 · via agent/mechanism_home — Accurate LoRA-Finetuning Quantization of LLMs via Information Retention
- arxiv:2411.05663 · 2024-11-08 · sim 0.47 · via mechanism_home — Online-LoRA: Task-free Online Continual Learning via Low Rank Adaptation
- arxiv:2402.10462 · 2024-02-16 · sim 0.46 · via agent/mechanism_home — QDyLoRA: Quantized Dynamic Low-Rank Adaptation for Efficient Large
  Language Model Tuning
- arxiv:2304.04158 · 2023-04-09 · sim 0.46 · via mechanism_home — Does Continual Learning Equally Forget All Parameters?

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
