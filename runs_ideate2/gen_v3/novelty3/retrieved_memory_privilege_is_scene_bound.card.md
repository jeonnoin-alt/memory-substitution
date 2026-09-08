=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: retrieved_memory_privilege_is_scene_bound — Which Part of the Memory-Conditioned Teacher Reaches the Memory-Free Student? Decomposing the Privilege Illusion When the Privileged Information Is Retrieved Agent Memory

- arxiv:2608.09228 · 2026-08-10 · preprint · sim 0.61 · hf · found via adjacent/mechanism_home/methods
  Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
  On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with OP^{2}SD (On-Policy Se
- arxiv:2606.29502 · 2026-06-28 · arXiv.org · sim 0.58 · s2 · found via agent
  UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation
  Skill memories can improve agentic reinforcement learning by reusing past experience as textual guidance, but retrieved skills are not oracular: they may help in one state while misleading the same policy in another. This makes the common privileged-teacher assumption fragile, namely that a skill-conditioned prompt can be treated as a fixed teacher for the no-skill prompt. We introduce UCOB, a framework for learning to utilize and evolve agentic skills via credit-aware on-policy bidirectional se
- arxiv:2608.05219 · 2026-08-05 · preprint · sim 0.56 · hf · found via agent
  When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents
  Privileged on-policy distillation provides dense supervision for multi-turn agents by allowing a synchronized teacher to re-score the student's response at every turn with access to training-only references, such as successful trajectories. In interactive environments, however, the student's preceding actions continually change the execution state. As the student takes different actions or completes subgoals in a different order, its rollout may reach states not covered by the reference, making 
- arxiv:2606.26790 · 2026-06-25 · arXiv.org · sim 0.56 · s2 · found via agent
  OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning
  Outcome-based reinforcement learning provides a stable optimization backbone for language agents, but its sparse trajectory-level rewards provide little guidance on which intermediate decisions should be reinforced or suppressed. On-policy self-distillation offers dense token-level supervision, yet existing skill-conditioned variants often rely on external skill memories or retrieved privileged context, which are costly to maintain and can be mismatched with the state distribution induced by the
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
- arxiv:2606.29863 · 2026-06-29 · arXiv.org · sim 0.49 · s2 · found via agent
  KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search
  Agentic search equips large language models with dynamic retrieval abilities, but existing reinforcement learning methods remain limited by reward sparsity in knowledge boundary calibration -- deciding when to trust parametric memory, when to rely on retrieved evidence, and when to abstain. Binary rewards can penalize undesirable outcomes, but provide little guidance on the reasoning process required to make calibrated decisions across different knowledge states. To address this, we propose KbSD

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2602.04942 · 2026-02-04 · sim 0.49 · via agent/mechanism_home/methods — Privileged Information Distillation for Language Models
- arxiv:2607.21556 · 2026-07-23 · sim 0.48 · via baseline/methods — Visual Contrastive Self-Distillation
- arxiv:2608.01735 · 2026-08-03 · sim 0.48 · via mechanism_home/methods — DAPD: Dual-Anchored Policy Distillation
- arxiv:2604.10674 · 2026-04-12 · sim 0.48 · via agent/mechanism_home — Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents
- arxiv:2606.30626 · 2026-06-29 · sim 0.47 · via mechanism_home — DOPD: Dual On-policy Distillation

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
