=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: retrieved_memory_privilege_is_scene_bound — Which Part of the Memory-Conditioned Teacher Reaches the Memory-Free Student? Decomposing the Privilege Illusion When the Privileged Information Is Retrieved Agent Memory

- arxiv:2608.09228 · 2026-08-10 · preprint · sim 0.61 · hf · found via adjacent/mechanism_home/methods
  Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
  On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with OP^{2}SD (On-Policy Se
- arxiv:2608.05219 · 2026-08-05 · preprint · sim 0.56 · hf · found via agent
  When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents
  Privileged on-policy distillation provides dense supervision for multi-turn agents by allowing a synchronized teacher to re-score the student's response at every turn with access to training-only references, such as successful trajectories. In interactive environments, however, the student's preceding actions continually change the execution state. As the student takes different actions or completes subgoals in a different order, its rollout may reach states not covered by the reference, making 
- arxiv:2608.14144 · 2026-08-14 · preprint · sim 0.54 · hf · found via mechanism_home
  Self-Supervised Visual On-Policy Distillation
  Visual on-policy distillation relies heavily on an informative teacher-student asymmetry, through either a larger, stronger teacher or privileged supervision, such as reference answers or ground-truth regions of interest. This raises a fundamental question: where can informative asymmetry come from when nothing privileged is available? We answer this by inverting where the asymmetry comes from. Rather than adding privileged information to the teacher, we subtract information from the student. Th
- arxiv:2608.01837 · 2026-08-03 · preprint · sim 0.54 · hf · found via agent
  PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning
  Large language model agents have shown strong potential in complex interactive tasks, yet their reinforcement learning (RL) is often hindered by sparse rewards, as a long multi-turn trajectory may receive only a single outcome-level signal. On-policy self-distillation (OPSD) provides dense token-level supervision from a privileged teacher, but the teacher may not be reliable at every position. Existing methods commonly rely on isolated token-level discrepancies, which can be sensitive to noise, 
- arxiv:2605.21606 · 2026-05-20 · preprint · sim 0.54 · hf · found via methods
  When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning
  On-policy self-distillation (OPSD) trains a student on its own rollouts using a privileged teacher, but its standard objective weights all generated tokens equally, implicitly treating the privileged teacher target as equally reliable at every student-visited prefix. Existing entropy-based OPD methods relax this uniformity by modulating token-level supervision with teacher entropy, but high teacher entropy in reasoning has an ambiguous reliability meaning: it can reflect either non-viable uncert
- arxiv:2605.20643 · 2026-05-20 · preprint · sim 0.51 · hf · found via agent/baseline
  AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals
  Self-distillation enables language models to learn on-policy from their own trajectories by using the same model as both student and teacher, with the teacher being conditioned on privileged information unavailable to the student. Such information can come in different types or views, such as solutions, demonstrations, feedback, or final answers. This setup provides dense token-level feedback without relying on a separate external model, but creates a fundamental asymmetry: the teacher may rely 
- arxiv:2608.05987 · 2026-08-06 · preprint · sim 0.51 · hf · found via agent
  AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
  Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in 
- arxiv:2602.04942 · 2026-02-04 · preprint · sim 0.49 · hf · found via agent/mechanism_home/methods
  Privileged Information Distillation for Language Models
  Training-time privileged information (PI) can enable language models to succeed on tasks they would otherwise fail, making it a powerful tool for reinforcement learning in hard, long-horizon settings. However, transferring capabilities learned with PI to policies that must act without it at inference time remains a fundamental challenge. We study this problem in the context of distilling frontier models for multi-turn agentic environments, where closed-source systems typically hide their interna
- arxiv:2607.21556 · 2026-07-23 · preprint · sim 0.48 · hf · found via baseline/methods
  Visual Contrastive Self-Distillation
  On-policy self-distillation (OPSD) is promising as it removes the external teacher required by on-policy distillation (OPD), yet it still needs asymmetric information between teacher and student to ensure that the self-teacher provides a stronger learning signal than the student. Existing methods create this asymmetry either through privileged answers or visual evidence. We ask whether both can be removed, yielding a simpler form of OPSD driven purely by input conditioning. For this purpose, we 
- arxiv:2608.01735 · 2026-08-03 · preprint · sim 0.48 · hf · found via mechanism_home/methods
  DAPD: Dual-Anchored Policy Distillation
  On-policy (self) distillation (OPSD) is increasingly adopted for language-model post-training. It strengthens the teacher with privileged information but can induce a privilege illusion: the student learns privilege-dependent behavior it cannot reproduce from its inference-time context, yet behaves as if the training-time privileged information remained available, ultimately degrading performance. In this paper, we identify information asymmetry between the privileged teacher and the student at 

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2604.10674 · 2026-04-12 · sim 0.48 · via agent/mechanism_home — Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents
- arxiv:2606.30626 · 2026-06-29 · sim 0.47 · via mechanism_home — DOPD: Dual On-policy Distillation
- arxiv:2605.11609 · 2026-05-12 · sim 0.46 · via adjacent/baseline — Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information
- arxiv:2604.12002 · 2026-04-13 · sim 0.44 · via baseline — Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision
- arxiv:2606.11173 · 2026-06-09 · sim 0.44 · via adjacent/mechanism_home — The Role of Feedback Alignment in Self-Distillation

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
