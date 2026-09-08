=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: instance_share_is_the_illusion — The Privilege Illusion of Retrieved Agent Memory Is Its Instance-Bound Share: What a Memory-Conditioned Self-Teacher Can and Cannot Distil into a Memory-Free Student

- arxiv:2606.29476 · 2026-06-28 · arXiv.org · sim 0.52 · s2 · found via mechanism_home
  CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning
  Self-distilled agentic reinforcement learning augments trajectory-level reward with a token-level distillation loss, using as its teacher the same policy conditioned on privileged context. The prevailing recipe gates this loss by a single scalar, the teacher-student log-probability gap. This signal is doubly limited: it is retrospective, scoring only the realised rollout and never the counterfactual ones, and it is sign-blind, never signalling when a teacher-preferred action would have harmed th
- arxiv:2608.09228 · 2026-08-10 · preprint · sim 0.52 · hf/s2 · found via adjacent/mechanism_home
  Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
  On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with OP^{2}SD (On-Policy Se
- arxiv:2606.17628 · 2026-06-16 · preprint · sim 0.50 · hf · found via methods
  OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation
  Memory has become a standard substrate for self-evolving agents, yet retaining experience is not the same as learning how to evolve through it. Existing memory agents can store trajectories, retrieve reflections, or accumulate skills, but often lack the holistic competence to select useful experience, act on it, write reusable knowledge, and maintain a growing repository. We introduce OPD-Evolver, a slow-fast co-evolution framework that cultivates such an agent evolver through on-policy self-dis
- arxiv:2608.05987 · 2026-08-06 · preprint · sim 0.49 · hf · found via agent
  AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
  Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in 
- arxiv:2608.01837 · 2026-08-03 · preprint · sim 0.47 · hf · found via agent
  PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning
  Large language model agents have shown strong potential in complex interactive tasks, yet their reinforcement learning (RL) is often hindered by sparse rewards, as a long multi-turn trajectory may receive only a single outcome-level signal. On-policy self-distillation (OPSD) provides dense token-level supervision from a privileged teacher, but the teacher may not be reliable at every position. Existing methods commonly rely on isolated token-level discrepancies, which can be sensitive to noise, 
- arxiv:2608.13040 · 2026-08-13 · preprint · sim 0.47 · hf · found via agent/mechanism_home/methods
  Latent On-Policy Self-Distillation
  Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student's own trajectories; however, existing methods still rely heavily on designer-specified privileged artifacts (e.g., answers, feedback, skills, or trajectories), limiting the end-to-end learnability and scalability required for cont
- arxiv:2605.20643 · 2026-05-20 · preprint · sim 0.47 · hf · found via agent
  AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals
  Self-distillation enables language models to learn on-policy from their own trajectories by using the same model as both student and teacher, with the teacher being conditioned on privileged information unavailable to the student. Such information can come in different types or views, such as solutions, demonstrations, feedback, or final answers. This setup provides dense token-level feedback without relying on a separate external model, but creates a fundamental asymmetry: the teacher may rely 
- arxiv:2604.10674 · 2026-04-12 · preprint · sim 0.45 · hf · found via agent/mechanism_home
  Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents
  Reinforcement learning (RL) has been widely used to train LLM agents for multi-turn interactive tasks, but its sample efficiency is severely limited by sparse rewards and long horizons. On-policy self-distillation (OPSD) alleviates this by providing dense token-level supervision from a privileged teacher that has access to ground-truth answers. However, such fixed privileged information cannot capture the diverse valid strategies in agent tasks, and naively combining OPSD with RL often leads to 
- arxiv:2606.29340 · 2026-06-28 · arXiv.org · sim 0.44 · s2 · found via mechanism_home
  PHF: Privileged Hidden Flow for On-Policy Self-Distillation
  On-policy self-distillation (OPSD) trains a reasoning model on rollouts sampled from its own policy by matching a privileged teacher that also sees verified reference solutions. Existing OPSD objectives supervise only the output distribution, so privileged context affects training through a token-level divergence without directly supervising the internal computation that produced that distribution. We propose Privileged Hidden Flow (PHF), which additionally distills how a privileged teacher's hi
- arxiv:2602.04942 · 2026-02-04 · preprint · sim 0.43 · hf · found via agent/mechanism_home
  Privileged Information Distillation for Language Models
  Training-time privileged information (PI) can enable language models to succeed on tasks they would otherwise fail, making it a powerful tool for reinforcement learning in hard, long-horizon settings. However, transferring capabilities learned with PI to policies that must act without it at inference time remains a fundamental challenge. We study this problem in the context of distilling frontier models for multi-turn agentic environments, where closed-source systems typically hide their interna

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2608.27065 · 2026-08-27 · sim 0.41 · via mechanism_home — Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models
- arxiv:2608.01735 · 2026-08-03 · sim 0.41 · via adjacent/agent/mechanism_home/methods — DAPD: Dual-Anchored Policy Distillation
- arxiv:2607.21556 · 2026-07-23 · sim 0.41 · via mechanism_home — Visual Contrastive Self-Distillation
- arxiv:2608.14144 · 2026-08-14 · sim 0.41 · via adjacent/mechanism_home — Self-Supervised Visual On-Policy Distillation
- arxiv:2605.11609 · 2026-05-12 · sim 0.40 · via adjacent/agent — Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
