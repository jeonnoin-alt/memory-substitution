=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: reversal_savings_latent_retention — Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory

- arxiv:2505.22310 · 2025-05-28 · preprint · sim 0.55 · hf · found via mechanism_home
  From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization
  Recent unlearning methods for LLMs are vulnerable to relearning attacks: knowledge believed-to-be-unlearned re-emerges by fine-tuning on a small set of (even seemingly-unrelated) examples. We study this phenomenon in a controlled setting for example-level unlearning in vision classifiers. We make the surprising discovery that forget-set accuracy can recover from around 50% post-unlearning to nearly 100% with fine-tuning on just the retain set -- i.e., zero examples of the forget set. We observe 
- arxiv:2608.11233 · 2026-07-31 · preprint · sim 0.51 · hf · found via baseline
  Retrofitting Recurrent Depth into a Pretrained Language Model: Installation, Extrapolation, Transfer, and Retention at Two Parameter Budgets
  A dense, pretrained language model can be retrofitted with recurrent depth and learn an iterative latent transition that persists after outcome-only annealing. Qwen2.5-0.5B-Instruct is split into a Prelude, a weight-tied Recurrent Block, and a Coda, with an identity-preserving one-loop path and a re-entry bridge on later loops. At loop 1 the retrofit remains non-inferior to its base on a preregistered ARC battery. Three findings. First, the mechanism is a reusable procedure rather than terminal-
- arxiv:2402.08096 · 2024-02-12 · preprint · sim 0.51 · hf · found via mechanism_home
  An Efficient Rehearsal Scheme for Catastrophic Forgetting Mitigation
  during Multi-stage Fine-tuning
  Incrementally fine-tuning foundational models on new tasks or domains is now the de facto approach in NLP. A known pitfall of this approach is the catastrophic forgetting of prior knowledge that happens during fine-tuning. A common approach to alleviate such forgetting is to rehearse samples from prior tasks during fine-tuning. Several existing works assume a fixed memory buffer to store prior task examples, while relying on inferences (forward passes) with the model at hand for choosing example
- arxiv:2601.18699 · 2026-01-26 · preprint · sim 0.51 · hf · found via adjacent/mechanism_home
  Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning
  Large language models exhibit remarkable performance across diverse tasks through pre-training and fine-tuning paradigms. However, continual fine-tuning on sequential tasks induces catastrophic forgetting, where newly acquired knowledge interferes with previously learned capabilities. Despite widespread observations of this phenomenon, the mechanistic understanding remains limited. Here, we present a comprehensive mechanistic analysis of catastrophic forgetting in transformer-based LLMs during s
- arxiv:2607.19749 · 2026-07-22 · preprint · sim 0.49 · hf · found via methods
  The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL
  Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? Under never-clear replay, pre-registered component-level probes (n=3 seeds throughout) show that the world model retains essentially everything measurable about old tasks -- reward discrimi
- arxiv:2604.20006 · 2026-04-21 · preprint · sim 0.49 · hf · found via agent
  From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents
  Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change. However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent knowledge updates. We introduce Memora, a long-term memory benchmark spanning weeks to months long user conversations. The benchmark
- arxiv:2410.06606 · 2024-10-15 · preprint · sim 0.48 · hf · found via mechanism_home
  Dissecting Fine-Tuning Unlearning in Large Language Models
  Fine-tuning-based unlearning methods prevail for preventing targeted harmful, sensitive, or copyrighted information within large language models while preserving overall capabilities. However, the true effectiveness of these methods is unclear. In this work, we delve into the limitations of fine-tuning-based unlearning through activation patching and parameter restoration experiments. Our findings reveal that these methods alter the model's knowledge retrieval process, providing further evidence
- arxiv:2406.06564 · 2024-06-03 · preprint · sim 0.48 · hf · found via agent
  SwitchLoRA: Switched Low-Rank Adaptation Can Learn Full-Rank Information
  In the training of large language models, parameter-efficient techniques such as LoRA optimize memory usage and reduce communication overhead and memory usage during the fine-tuning phase. However, applying such techniques directly during the pre-training phase results in poor performance, primarily because the premature implementation of low-rank training significantly reduces model accuracy. Existing methods like ReLoRA and GaLore have attempted to address this challenge by updating the low-ra
- arxiv:2601.15086 · 2026-01-21 · preprint · sim 0.48 · hf · found via agent/methods
  Memory Retention Is Not Enough to Master Memory Tasks in Reinforcement Learning
  Effective decision-making in the real world depends on memory that is both stable and adaptive: environments change over time, and agents must retain relevant information over long horizons while also updating or overwriting outdated content when circumstances shift. Existing Reinforcement Learning (RL) benchmarks and memory-augmented agents focus primarily on retention, leaving the equally critical ability of memory rewriting largely unexplored. To address this gap, we introduce a benchmark tha
- arxiv:2401.16650 · 2024-01-30 · preprint · sim 0.48 · hf · found via methods
  Augmenting Replay in World Models for Continual Reinforcement Learning
  Continual RL requires an agent to learn new tasks without forgetting previous ones, while improving on both past and future tasks. The most common approaches use model-free algorithms and replay buffers can help to mitigate catastrophic forgetting, but often struggle with scalability due to large memory requirements. Biologically inspired replay suggests replay to a world model, aligning with model-based RL; as opposed to the common setting of replay in model-free algorithms. Model-based RL offe

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2604.03114 · 2026-04-03 · sim 0.48 · via mechanism_home — Can VLMs Truly Forget? Benchmarking Training-Free Visual Concept Unlearning
- arxiv:2501.15377 · 2025-01-26 · sim 0.47 · via adjacent — Fine Tuning without Catastrophic Forgetting via Selective Low Rank
  Adaptation
- arxiv:2602.03379 · 2026-02-03 · sim 0.46 · via mechanism_home — Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures
- arxiv:2510.15103 · 2025-10-16 · sim 0.44 · via mechanism_home — Continual Learning via Sparse Memory Finetuning
- arxiv:2509.24675 · 2025-09-29 · sim 0.44 · via mechanism_home — Understanding the Dilemma of Unlearning for Large Language Models

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
