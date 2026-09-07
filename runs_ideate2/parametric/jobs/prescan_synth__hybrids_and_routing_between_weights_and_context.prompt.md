=== SYSTEM ===
You are given the index cards for one axis. Write the 3-5 open gaps these papers jointly expose: for each gap, one
sentence stating what is unresolved, the card IDs whose stated limitations or untested items point to it (at least
two), and one sentence on what evidence would settle it. Do not propose papers. Do not invent gaps that no card
supports. Return JSON: {"axis":"...","gaps":[{"gap","card_ids":[...],"evidence_needed"}]}.

=== USER ===
[
 {
  "id": "arxiv:2604.27003",
  "date": "2026-04-29",
  "claim": "External memory does not resolve the continual-learning problem for LLM agents; under a limited context window, old and new experiences compete during retrieval, relocating the stability-plasticity bottleneck from parameter updates to memory representation and retrieval design.",
  "method": "A (k,v) framework that disentangles how experience is represented and how it is organized for retrieval, evaluated in sequential-task experiments with memory-augmented agents.",
  "evidence": "Sequential-task experiments in ALFWorld and BabyAI; abstract procedural memories transfer more reliably than detailed trajectories; negative transfer disproportionately harms hard cases; finer-grained memory organization can yield strong forward transfer while inducing severe forgetting; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "No parametric (weight-update) continual-learning arm is described for a direct comparison against memory-based reuse; the abstract does not report seeds, noise floors or the cost of maintaining memory over long streams.",
  "axes": [
   "continual adaptation and shift",
   "hybrids and routing between weights and context"
  ],
  "title": "When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents"
 },
 {
  "id": "arxiv:2603.12056",
  "date": "2026-03-12",
  "claim": "Multimodal agents can continually improve without parameter updates by accumulating and reusing two complementary kinds of knowledge from past trajectories, action-level experiences and task-level skills.",
  "method": "XSkill, a dual-stream framework that distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique, then retrieves and adapts them to the current visual context while feeding usage history back into accumulation.",
  "evidence": "Five benchmarks across diverse domains with four backbone models; XSkill consistently and substantially outperforms tool-only and learning-based baselines; the two streams play complementary roles and show superior zero-shot generalization; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the accumulated context knowledge could be internalized into weights, or how it compares to parameter updates under matched compute, is not described; behaviour of the memory over long streams with distribution shift or staleness is not described.",
  "axes": [
   "continual adaptation and shift",
   "hybrids and routing between weights and context"
  ],
  "title": "XSkill: Continual Learning from Experience and Skills in Multimodal Agents"
 },
 {
  "claim": "Agent skills loaded at inference time can instead be internalized into model parameters via an in-context RL curriculum that progressively withdraws skill context, yielding zero-shot autonomous behaviour that outperforms standard RL at a much smaller context.",
  "method": "SKILL0 trains with full skill context initially, groups skills offline by category and renders them with interaction history into a compact visual context, then a Dynamic Curriculum evaluates each skill file's on-policy helpfulness and retains only beneficial files under a linearly decaying budget until the agent runs fully zero-shot.",
  "evidence": "Agentic experiments on ALFWorld and Search-QA; +9.7% on ALFWorld and +6.6% on Search-QA over the standard RL baseline, with fewer than 0.5k context tokens per step.",
  "stated_limitations": "not stated",
  "not_tested": "The abstract does not report a comparison against simply keeping skills in context at inference time at matched training compute, nor whether internalized skills survive distribution shift or new skill categories not seen during training.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-04-02",
  "id": "arxiv:2604.02268",
  "title": "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
 },
 {
  "claim": "Retrieval-augmented prompting with similar image-caption pairs can adapt a generalist VLM to stylistically coherent remote-sensing captioning without fine-tuning, reaching performance competitive with fine-tuning.",
  "method": "RAGCap uses SigLIP similarity-based retrieval to select relevant image-caption pairs from the training set and combines them with the target image in a designed prompt for Qwen2VL to generate captions matching the dataset's style.",
  "evidence": "Four remote-sensing captioning benchmark datasets with SigLIP retrieval and Qwen2VL as the base VLM; RAGCap achieves competitive performance compared to traditional fine-tuning approaches; no specific numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Inference token cost of retrieved examples versus the amortized cost of fine-tuning is not compared, and the retrieval approach is not evaluated on held-out or unseen-scene splits beyond the standard benchmarks.",
  "axes": [
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "date": "2025-10-28",
  "id": "s2:68c32642a3f48da49c4aebb65c9ab602ce2a4ac0",
  "title": "RAGCap: retrieval-augmented generation for style-aware remote sensing image captioning without fine-tuning"
 },
 {
  "claim": "Abstract skill cards used as privileged context for an on-policy self-teacher provide dense supervision where group-relative RL rewards become uninformative, and distilling them into weights beats both GRPO and in-context skill exposure.",
  "method": "SKALD: on-policy self-distillation with two context views of the same Qwen3-Base model (question-only student, teacher conditioned on an explicit-answer-filtered skill card), trained on the student's own prefixes with an annealed exponentially tilted objective and an empirical gate that activates distillation only when verified rollouts estimate positive teacher advantage.",
  "evidence": "Qwen3-Base at 0.6B, 1.7B and 4B on five held-out mathematics benchmarks; 63.0-68.0% of GRPO rollout groups are zero-variance; SKALD improves avg@8 over GRPO by +2.46, +4.85 and +12.01 respectively; at 1.7B, zero-variance-only distillation recovers 84.7% of the full gain, SKALD is +4.06 above FLOP-matched GRPO and +3.77 above contextual skill exposure.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the skill-induced advantage transfers beyond mathematics or beyond the Qwen3-Base family; long-horizon or continual settings where skill cards change or go stale; the token cost of composing skill cards is not compared against the inference savings of removing them at test time.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-08-10",
  "id": "arxiv:2608.09826",
  "title": "Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation"
 },
 {
  "claim": "A self-routing framework that keeps novel or sparse tasks in an episodic retrieval buffer and consolidates recurring, reliable execution patterns into expandable parametric memory resolves the stability-plasticity dilemma on boundary-agnostic task streams better than either substrate alone.",
  "method": "UniMem uses learnable routing tokens as memory controllers to decouple task identification from execution, routing tasks between an episodic buffer (retrieval-augmented execution) and expandable parametric memory blocks that grow on demand without task labels or uncontrolled parameter growth.",
  "evidence": "Long-horizon streaming task sequences across three backbone models; UniMem consistently outperforms baselines while maintaining execution fidelity, with an average gain of 4.0 EM points. Specific benchmarks and backbone names are not given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether parameter growth stays bounded over much longer streams and what the consolidation compute and retrieval-overhead trade-off is at matched cost; whether consolidated patterns erode or go stale when a recurring task's execution strategy later changes.",
  "axes": [
   "hybrids and routing between weights and context",
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-07-28",
  "id": "arxiv:2607.26017",
  "title": "UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams"
 },
 {
  "claim": "Making the self-teacher's privileged context learnable end-to-end from retrieved experience, rather than hand-specifying answers, feedback, skills or trajectories, yields stronger and more rollout-efficient on-policy self-distillation.",
  "method": "LOPD retrieves relevant experiences and composes them into continuous latent tokens conditioning a self-teacher, gives the student dense token-level supervision at every visited prefix of its own trajectories, and adds a privileged-margin objective to stabilize learning of the latent context.",
  "evidence": "Agentic tool use and code generation; LOPD outperforms RLVR and OPSD methods (OPSD, SDPO, Skill-SD) and surpasses GRPO and Skill-SD with less than 30% of their rollout budget; ablations indicate learnable privileged context is necessary for the gains. Model names and absolute numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the learned latent context transfers hidden or undesired traits along with task content; behavior over long continual streams where the retrieved experience pool shifts or goes stale; comparison against simply keeping the retrieved experiences in context at inference under matched token cost.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-08-13",
  "id": "arxiv:2608.13040",
  "title": "Latent On-Policy Self-Distillation"
 },
 {
  "claim": "Coordinating harness-based (editable memory/skills) and parameter-based (weight-internalized) self-evolution through task-aware routing outperforms either channel alone under changing environments.",
  "method": "COVE combines the two channels via task-aware routing, stage-aware scheduling and knowledge optimization, matching tasks and knowledge types to the appropriate learning mechanism instead of accumulating experience indiscriminately.",
  "evidence": "Experiments across multiple task categories in environments where tool interfaces, APIs and user requirements change; COVE outperforms single-channel evolution strategies with more robust and efficient improvement. No models, benchmarks or numbers are stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the routing decision is evaluated at matched training compute and inference token cost against each single channel; how internalized knowledge erodes or goes stale when the environment changes again after parameter updates.",
  "axes": [
   "hybrids and routing between weights and context",
   "continual adaptation and shift"
  ],
  "date": "2026-08-02",
  "id": "arxiv:2608.01234",
  "title": "Learning What to Remember and What to Internalize in LLM Self-Evolution via Adaptive Memory-Parameter Coordination"
 },
 {
  "claim": "Structured hierarchical memory built from a large teacher agent's successful trajectories can be transferred to small student agents without any training and substantially improves their tool use, outperforming existing memory-based baselines.",
  "method": "AMD constructs Workflow memory (task-level strategies), Subtask memory (intermediate-granularity behavioral examples) and Function memory (per-function calling conventions and pitfalls) from teacher trajectories; Workflow and Subtask memories are injected proactively at task start and Function memory is retrieved reactively on tool-calling errors.",
  "evidence": "Three tool-use benchmarks with four 4B-8B student models and GPT-5-mini as teacher; average accuracy gains of 27.2%p on AppWorld, 11.2%p on BFCL V3 and 3.4%p on ToolSandbox; Subtask memory contributes most, teacher effectiveness depends on teacher capability and student compatibility, and 4B students benefit most.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against fine-tuning or distilling the same teacher trajectories into the student's weights, and no report of the inference token cost of the proactively injected memory.",
  "axes": [
   "hybrids and routing between weights and context"
  ],
  "date": "2026-08-07",
  "id": "arxiv:2608.07169",
  "title": "Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory"
 },
 {
  "id": "arxiv:2608.04530",
  "date": "2026-08-05",
  "claim": "Effective latent memory for GUI agents depends on separating what is retained (role-aware episodic vs. working content), what is exposed (a state-conditioned readout), and what is allowed (a trust gate), rather than on compressing trajectories into one fixed memory block trained by next-action supervision.",
  "method": "FocusMem compresses multimodal trajectories into a few continuous latent tokens with a role-aware content basis (episodic memory for reusable experience, working memory for task progress), a state-conditioned readout that produces a decision-specific view of the stored evidence, and a lightweight trust gate that suppresses seemingly irrelevant memory blocks; all components are trained while the GUI policy stays frozen.",
  "evidence": "Five GUI-agent benchmarks; FocusMem consistently outperforms a fully matched action-only fixed-memory baseline and prior latent memory adaptations; analysis shows semantic and functional supervision preserve complementary information, state-conditioned readout is more robust as trajectory context grows, and the trust gate reduces harm from injected irrelevant episodic evidence; no numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not compare the frozen-policy latent memory against fine-tuning the policy on the same experience (weights vs. context substitution); does not report inference cost or behaviour over long streams of accumulating memory.",
  "axes": [
   "hybrids and routing between weights and context"
  ],
  "title": "FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory"
 },
 {
  "id": "arxiv:2603.18272",
  "date": "2026-03-18",
  "claim": "Combining supervised fine-tuning with experience retrieval, by training the agent to use retrieved trajectories in-context, significantly improves generalization to unseen tasks over either fine-tuning alone or training-free retrieval.",
  "method": "Establishes a LoRA-based SFT recipe, analyzes experience-retrieval design choices (storage, querying, trajectory selection), and proposes a pipeline that integrates experience retrieval into the fine-tuning process so the agent learns to leverage retrieved trajectories.",
  "evidence": "LoRA SFT recipe reported to outperform several state-of-the-art agent training pipelines; the combined retrieval-plus-fine-tuning approach significantly improves generalization to unseen tasks; benchmarks, models, and numbers not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report whether the retrieval component remains necessary at inference after training (i.e., whether context and weights add or substitute), nor the inference token cost of retrieval versus SFT-only.",
  "axes": [
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "title": "Retrieval-Augmented LLM Agents: Learning to Learn from Experience"
 },
 {
  "claim": "Agentic RL should internalize general skills into weights while keeping task-specific skills in context, and doing so with a difficulty-aware router outperforms both full externalization and full internalization on in- and out-of-distribution tasks.",
  "method": "Skill0.5 uses a dynamic difficulty-aware router to stream tasks into mastery tiers, internalizing general skills via privileged distillation on hard tasks and applying diagnostic probing on easy tasks to penalize shortcuts and enforce task-specific skill utilization.",
  "evidence": "Experiments on ALFWorld and WebShop; Skill0.5 outperforms memory-based and skill-based RL baselines on both in-distribution and out-of-distribution scenarios. Specific numbers and backbone models are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report the context-token or training-compute cost of the hybrid versus the full-externalization and full-internalization baselines; does not test whether the internalized general skills erode or conflict under continued training on new tasks.",
  "axes": [
   "hybrids and routing between weights and context",
   "internalization objectives"
  ],
  "date": "2026-05-27",
  "id": "arxiv:2605.28424",
  "title": "Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning"
 },
 {
  "claim": "Decomposing RAG into collaborating specialized agents (Planner, Step Definer, Extractor, QA) that share chain-of-thought reasoning improves accuracy and interpretability on multi-hop and ambiguous QA without end-to-end fine-tuning.",
  "method": "MA-RAG orchestrates a set of prompted agents that handle query disambiguation, evidence extraction and answer synthesis, communicating intermediate reasoning via chain-of-thought prompting to progressively refine retrieval and synthesis.",
  "evidence": "NQ, HotpotQA, 2WikimQA and TriviaQA with LLaMA3-8B, LLaMA3-70B and GPT-4o-mini; MA-RAG outperforms standalone LLMs and existing RAG methods at all scales, LLaMA3-8B with MA-RAG surpasses larger standalone LLMs, larger variants set state-of-the-art on multi-hop datasets; ablations show planner and extractor are critical; generalizes to medical QA without domain-specific fine-tuning. Specific numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report inference token cost or latency of the multi-agent pipeline versus single-pass RAG; does not compare against fine-tuning the same knowledge into weights.",
  "axes": [
   "hybrids and routing between weights and context"
  ],
  "date": "2025-05-26",
  "id": "arxiv:2505.20096",
  "title": "MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning"
 },
 {
  "claim": "No single memory substrate consistently dominates across agent operating regimes, so substrate routing is a necessary component of adaptive long-term memory for LLM agents.",
  "method": "A controlled harness evaluation of memory substrates (dense and sparse indices, text records, structural, hierarchical and refinement-based stores, parametric updates, and activation-compatible context mechanisms) instrumented with 26 performance and efficiency metrics.",
  "evidence": "Three backbone models and four benchmark suites spanning user-centric QA and agent-centric decision-making; broad retrieval helps long-context factual QA while excessive retrieval harms sequential decision-making; substrates strong at moderate history lengths become costly or brittle at longer horizons. Specific models and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not describe or evaluate an actual routing policy, only motivates one; does not report matched training compute for parametric updates versus the inference cost of retrieval substrates.",
  "axes": [
   "evaluation and cost of the two substrates",
   "hybrids and routing between weights and context",
   "continual adaptation and shift"
  ],
  "date": "2026-08-15",
  "id": "arxiv:2608.15008",
  "title": "Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents"
 },
 {
  "id": "arxiv:2606.29502",
  "date": "2026-07-17",
  "claim": "Retrieved skills are not oracular teachers, so treating a skill-conditioned prompt as a fixed privileged teacher is fragile; instead a credit-aware bidirectional self-distillation that picks the higher-return context view per task/state as the local teacher yields better skill utilization and evolution.",
  "method": "UCOB treats skill-conditioned and no-skill prompts as two on-policy context views of the same model, compares their return-to-go at the same task and anchor state, uses the higher-return view as the local teacher to distill and correct behavior, and uses the credit signal to drive skill memory updates, utility-aware retrieval, and reflection self-training.",
  "evidence": "Agentic tasks ALFWorld, WebShop, and Search-QA across model scales; UCOB outperforms skill-free RL, skill-memory baselines, and self-distillation methods, with up to 23.5 point gains on ALFWorld and 18.0 on WebShop over SOTA baselines; ablations report continual adaptation across environments and modest training overhead.",
  "stated_limitations": "not stated",
  "not_tested": "The abstract does not say whether the distilled policy is evaluated without the skill memory at deployment (memory-free) versus with it, nor does it report inference token cost of the skill-conditioned view or noise floors across seeds.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "continual adaptation and shift"
  ],
  "title": "UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation"
 },
 {
  "id": "arxiv:2607.29468",
  "date": "2026-07-31",
  "claim": "Making an external skill memory a co-evolving state of self-play changes both policy learning and the future training distribution, and its benefits partly enter the parameters (allowing memory-free deployment) while the bank retains additional value as optional inference-time memory.",
  "method": "SESA runs tool-augmented search self-play with a challenger that poses problems and a separately parameterized solver that retrieves skills; informative failures are distilled into reusable skills written back to memory, and because retrieved skills shape on-policy training trajectories, the model can be deployed with or without the skill bank.",
  "evidence": "Seven open-domain and multi-hop QA benchmarks, multiple backbones including Qwen3; SESA improves average accuracy over SSP by 1.2-3.2 points and beats SkillRL by 0.9 points under a unified protocol; on Qwen3, SESA-Off (memory-free) retains 1.8-2.2 points over SSP and the final skill bank adds a further 0.5-1.0 points.",
  "stated_limitations": "not stated",
  "not_tested": "The gains are small (0.9-3.2 points) and the abstract gives no seed variance or noise floor; only QA/search is tested, and the cost of retrieval tokens versus the memory-free variant is not reported.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "title": "Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember"
 },
 {
  "id": "arxiv:2512.02543",
  "date": "2025-12-02",
  "claim": "A frozen low-cost student model given retrieved teacher demonstrations in context at each agent step, combined with self-consistency cascades to decide when to trust the student, can match teacher-level accuracy at substantially lower cost without fine-tuning.",
  "method": "In-context distillation: retrieve relevant high-cost teacher demonstrations at each agent step and provide them as in-context examples to a cheaper student; a self-consistency cascade routes to the teacher when the student is unreliable.",
  "evidence": "ALFWorld: matches teacher accuracy at 2.5x lower cost, per-episode cost from $0.059 to $0.024, demonstration cost amortizes after 843 episodes with cumulative savings over $34,900 at 1M episodes; AppWorld: 2x cost reduction at iso-accuracy, shifting the Pareto frontier.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against actually fine-tuning the student on the same teacher demonstrations (the weight route) at matched cost; no evaluation of robustness when the deployment task distribution drifts from the collected demonstrations.",
  "axes": [
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "title": "In-Context Distillation with Self-Consistency Cascades: A Simple, Training-Free Way to Reduce LLM Agent Costs"
 },
 {
  "id": "arxiv:2606.08755",
  "date": "2026-06-07",
  "claim": "Skills generated by even frontier LLMs have highly mixed utility, so skills should be validated for context-dependent marginal utility before being stored, and this signal can also train the policy itself to generate skills and to rerank and prune the bank.",
  "method": "An online RL framework that splits the standard rollout budget into matched base rollouts (current retrieved skills) and skill-augmented rollouts (same skills plus one candidate skill induced from the base trajectories) under the same task and retrieval context, uses the reward gap as the candidate's marginal utility to admit or filter it, and trains the policy as a skill generator whose likelihood serves as a retrieval-time reranking and outdated-skill pruning score.",
  "evidence": "Setting is skill-augmented online RL for language agents; the abstract reports that many frontier-LLM-generated skills provide little benefit or degrade performance and that validation adds no additional rollout overhead, but names no benchmarks, models, or headline numbers.",
  "stated_limitations": "not stated",
  "not_tested": "No headline benchmark numbers or models appear in the abstract; the paper does not (per abstract) test whether validated skills become unnecessary at inference, i.e. whether their content transfers into weights.",
  "axes": [
   "hybrids and routing between weights and context",
   "continual adaptation and shift"
  ],
  "title": "Co-Evolving Skill Generation and Policy Optimization"
 },
 {
  "id": "arxiv:2607.01224",
  "date": "2026-07-01",
  "claim": "Memory management is an independently learnable skill: optimizing only how an agent manages its memory files, without changing task-action behavior, yields large gains on long-horizon tasks.",
  "method": "AutoMem promotes file-system operations to first-class memory actions and automates two loops: a strong LLM reviews full trajectories to iteratively revise the memory structure (prompts, file schemas, action vocabulary), and the agent's own good memory decisions are mined from many episodes as training signal to sharpen its memory proficiency.",
  "evidence": "Three procedurally generated long-horizon games (Crafter, MiniHack, NetHack); optimizing memory alone improved the base agent ~2x-4x and brought a 32B open-weight model competitive with Claude Opus 4.5 and Gemini 3.1 Pro Thinking.",
  "stated_limitations": "not stated",
  "not_tested": "Does not separate the contribution of the strong-LLM structure loop from the self-training proficiency loop in the abstract, and does not compare against internalizing the same experience into weights rather than keeping it in memory files.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context"
  ],
  "title": "AutoMem: Automated Learning of Memory as a Cognitive Skill"
 },
 {
  "id": "arxiv:2607.01480",
  "date": "2026-07-01",
  "claim": "Cross-episode procedural signals that episode-local RLVR/self-distillation updates cannot capture can be converted into a procedural memory and distilled into the policy's weights during training, yielding a memory-free model at inference that outperforms SDPO, with co-evolution of memory and policy driving the gains.",
  "method": "Procedural Memory Distillation organizes memory at three levels (raw trajectories, self-reflected strategies and lessons, recurring behavioral patterns) extracted online from the model's own rollouts, and a memory-conditioned self-teacher supervises the student on its own rollouts so it progressively internalizes the procedural knowledge; the policy updates the memory and the memory shapes the supervision.",
  "evidence": "Qwen3-8B and OLMo3-Instruct-7B; PMD improves over SDPO by 3.8-5.5% on SciKnowEval and 7.9-13.6% on LiveCodeBench; freezing either the memory or the policy trails PMD by more than 10% across SciKnowEval domains.",
  "stated_limitations": "not stated",
  "not_tested": "No direct comparison of the memory-free distilled model against simply keeping the procedural memory in context at inference, and no report of matched compute between PMD and SDPO or of seed variance.",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "title": "Procedural Memory Distillation: Online Reflection for Self-Improving Language Models"
 },
 {
  "id": "arxiv:2606.02355",
  "date": "2026-06-01",
  "claim": "Agents can discover, validate, and internalize skills from their own successful rollouts without external skill generators or inference-time skill banks, and self-mined skills distilled into the plain policy can match distillation from a closed-source large model.",
  "method": "Three phases: warm up with GiGPO and collect skill-free trajectories; self-skill mining where the policy summarizes compact skills from its own successful rollouts and validates them through paired skill-augmented versus skill-free rollouts; distill only beneficial skill-guided action tokens into the plain policy using trajectory-level utility and action-level advantage, then run with the original prompt at inference.",
  "evidence": "ALFWorld and WebShop with Qwen2.5-7B-Instruct; SIRI improves GiGPO from 0.908 to 0.930 on ALFWorld and from 0.728 to 0.813 on WebShop, outperforming prompt-based, RL-based, and memory-augmented baselines; self-mining performs comparably to distillation from a closed-source large model.",
  "stated_limitations": "not stated",
  "not_tested": "Only a single 7B backbone on two environments; the abstract does not report the extra rollout cost of paired validation or whether internalized skills persist under continued training or environment shift.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "hybrids and routing between weights and context"
  ],
  "title": "SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training"
 },
 {
  "id": "arxiv:2605.27762",
  "date": "2026-05-26",
  "claim": "Agent memory in Minecraft can be moved from inference-time retrieval into parameter-resident skills via failure-aware contrastive internalization, improving long-horizon performance, reducing forgetting of consolidated skills, and beating retrieval-based agents on parametric-versus-retrieval efficiency.",
  "method": "A slow deliberative LLM is paired with a fast multimodal Mixture-of-Experts LoRA module with per-category isolated adapters; failure-correction trajectory pairs are internalized with a joint behavioral-cloning plus contrastive objective, gated by a parameterization-worthiness score (what to internalize) and a scale-free self-triggered consolidation mechanism (when to internalize).",
  "evidence": "Minecraft embodied-agent experiments comparing PEAM against retrieval-based embodied agents and parametric memory variants; reports improved long-horizon task performance, mitigated forgetting on previously consolidated skills, and improved parametric-versus-retrieval efficiency; no specific numbers, base models, or benchmark names are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No headline numbers or base-model details are given, so the size of the gain over retrieval and whether it holds under matched training compute or inference token cost is unclear; transfer of the self-triggered consolidation beyond Minecraft task distributions is asserted but not evidenced in the abstract.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "hybrids and routing between weights and context",
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "title": "PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft"
 },
 {
  "id": "arxiv:2607.28272",
  "date": "2026-07-30",
  "claim": "Replaying retrieved experiences verbatim into context causes negative transfer, and training a policy to critique and reconstruct retrieved experience conditioned on the current state removes this failure and additionally improves the agent's intrinsic reasoning.",
  "method": "At each decision step a single policy model critiques and reconstructs the retrieved experience into context-grounded guidance before acting, with the reconstruction ability trained end-to-end via GRPO.",
  "evidence": "ALFWorld and WebShop; MemHarness substantially outperforms pure RL and static memory-augmented baselines and is robust in OOD scenarios; analyses indicate the reconstruction objective prevents negative transfer and acts as latent guidance during training; no numeric results or base models are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the reconstruction step's extra per-step inference tokens are accounted for when comparing against static-memory baselines; whether gains persist if memory is removed at test time (i.e., how much was internalized into weights versus still depending on retrieval).",
  "axes": [
   "internalization objectives",
   "hybrids and routing between weights and context",
   "evaluation and cost of the two substrates"
  ],
  "title": "MemHarness: Memory Is Reconstructed, Not Replayed"
 },
 {
  "id": "arxiv:2601.03192",
  "date": "2026-01-06",
  "claim": "Agents can self-evolve without weight updates by applying reinforcement learning to an episodic memory store, reconciling the stability-plasticity dilemma while avoiding the cost and forgetting of fine-tuning.",
  "method": "MemRL decouples stable reasoning from plastic memory and uses a Two-Phase Retrieval mechanism, tuned by environmental feedback, to filter noise and identify high-utility strategies in episodic memory at runtime.",
  "evidence": "HLE, BigCodeBench, ALFWorld, and Lifelong Agent Bench; MemRL significantly outperforms state-of-the-art baselines and shows continuous runtime improvement without weight updates; no numbers or base models are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No direct comparison against a fine-tuning route at matched compute or inference token cost, so the claim that fine-tuning is expensive and forgetting-prone is asserted rather than measured; staleness of stored episodic items under distribution shift is not addressed in the abstract.",
  "axes": [
   "hybrids and routing between weights and context",
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "title": "MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory"
 },
 {
  "id": "arxiv:2512.10696",
  "date": "2025-12-11",
  "claim": "Managing procedural memory dynamically across its lifecycle (distillation, context-adaptive reuse, utility-based refinement) rather than as an append-only archive yields state-of-the-art agent memory, and a smaller model with such memory outperforms a larger memoryless model.",
  "method": "ReMe combines multi-faceted distillation (success patterns, failure triggers, comparative insights), context-adaptive reuse via scenario-aware indexing, and utility-based refinement that adds valid memories and prunes outdated ones to keep a compact experience pool.",
  "evidence": "BFCL-V3 and AppWorld; ReMe establishes a new state of the art among agent memory systems, and Qwen3-8B with ReMe outperforms memoryless Qwen3-14B (memory-scaling effect); code and the reme.library dataset are released; no specific scores are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "The 8B-with-memory versus 14B-without comparison does not account for the extra inference tokens of retrieved memory, and no comparison against internalizing the same experiences into weights is reported; long-stream behavior under distribution shift and pruning errors is not addressed in the abstract.",
  "axes": [
   "hybrids and routing between weights and context",
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "title": "Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution"
 },
 {
  "id": "arxiv:2608.12218",
  "date": "2026-08-12",
  "claim": "Abundant relevant information in the training context reduces the incentive to encode that information parametrically and increases reliance on context, so scaling training context helps only up to an intermediate optimum and hurts robustness when context is absent or misleading at test time.",
  "method": "The paper varies context window length in long-document pretraining and the amount of task-relevant train-time context in supervised fine-tuning, analyzes gradient pressure across feed-forward versus attention modules, and uses causal interventions to test context reliance at inference.",
  "evidence": "In pretraining, language modeling, natural language understanding, and closed-book MCQA improve with context window only up to an intermediate optimum and then consistently decline; in SFT, more train-time context improves performance with supporting context but reduces robustness without or with misleading context; gradient pressure shifts from FFNs toward attention and causal interventions show increased context reliance; no model names or numbers are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the effect holds for agent trajectory data and memory-conditioned distillation rather than documents and generic SFT tasks; whether the intermediate optimum shifts with model scale or with total training tokens.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "hybrids and routing between weights and context"
  ],
  "title": "Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge"
 }
]
