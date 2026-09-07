=== SYSTEM ===
You are given the index cards for one axis. Write the 3-5 open gaps these papers jointly expose: for each gap, one
sentence stating what is unresolved, the card IDs whose stated limitations or untested items point to it (at least
two), and one sentence on what evidence would settle it. Do not propose papers. Do not invent gaps that no card
supports. Return JSON: {"axis":"...","gaps":[{"gap","card_ids":[...],"evidence_needed"}]}.

=== USER ===
[
 {
  "id": "arxiv:2602.04942",
  "date": "2026-02-04",
  "claim": "Capabilities learned with training-time privileged information (PI) can be transferred to a student that acts without PI at inference, and the proposed objectives outperform the standard SFT-then-RL pipeline even when that pipeline has full chain-of-thought supervision.",
  "method": "π-Distill, a joint teacher-student objective that trains a PI-conditioned teacher and an unconditioned student simultaneously in the same model, and On-Policy Self-Distillation (OPSD), which trains with RL plus a reverse-KL penalty between the student and the PI-conditioned teacher.",
  "evidence": "Distilling frontier agents in multi-turn agentic environments using action-only PI (teachers expose action trajectories but hide reasoning); evaluated across multiple agentic benchmarks, models and forms of PI; π-Distill and, in some cases, OPSD outperform SFT followed by RL that assumes full CoT supervision; no headline numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the distilled student retains context-dependent or teacher-specific behaviours beyond task success is not described; training compute and inference-cost comparisons against the SFT+RL baseline are not stated in the abstract.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "evaluation and cost of the two substrates"
  ],
  "title": "Privileged Information Distillation for Language Models"
 },
 {
  "claim": "Representing an agent's growing trajectory-indexed memory utilities with a fixed-dimensional per-task utility state concentrates sparse feedback and limits the 'memory-reward trap' in which irrelevant co-retrieved memories receive misleading utility updates.",
  "method": "RoMeRL factorizes memory utility into a fixed set of semantic coordinates per task, split by outcome polarity and memory dynamics, whose contents are updated or replaced over time so feedback is concentrated on a bounded support; a theoretical analysis of feedback density and steady-state occupancy of erroneous coordinates accompanies the empirical study.",
  "evidence": "ALFWorld and LifelongAgentBench with self-evolving LLM agents; improves task performance, reduces the Cold-Q ratio by 80.0%, increases feedback density about 6.0x, reduces maintained memory size by 84.4%, and cuts LLM calls by 21.1%.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against internalizing the accumulated experience into weights (fine-tuning) as an alternative to a learned external memory, and no report of behaviour under distribution shift beyond the two benchmarks or of how stale coordinates are handled over very long streams.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-08-10",
  "id": "arxiv:2608.02508",
  "title": "RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States"
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
  "claim": "Current LLMs and agentic memory systems fail to adapt robustly to continually updating knowledge streams, showing delays in state-tracking and susceptibility to distraction.",
  "method": "Introduce the OAKS benchmark, a sequence of fine-grained context chunks in which individual facts change multiple times over time intervals, with dense annotations for change-tracking, in two datasets (OAKS-BABI and OAKS-Novel).",
  "evidence": "14 models evaluated with varied inference approaches, including state-of-the-art models and agentic memory systems; all show significant limitations in tracking evolving facts. No headline numbers are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Parametric update routes (fine-tuning or distillation on the stream) are not among the evaluated inference approaches per the abstract; the streams are synthetic/annotated (BABI, novel-based) rather than real deployment streams.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-03-08",
  "id": "arxiv:2603.07392",
  "title": "Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams"
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
  "claim": "An online self-evolving external memory that separates stored experiences from compiled meta-guidelines and reweights experiences from continuous feedback (reinforcing helpful, decaying stale or misleading ones) is more robust under true distribution shift than pipelines built for static train/test splits.",
  "method": "Live-Evo maintains an Experience Bank and a Meta-Guideline Bank, compiles task-adaptive guidelines from retrieved experiences per task, and updates experience weights online from feedback so that consistently helpful experiences are retrieved more and misleading or stale ones are gradually forgotten.",
  "evidence": "Live Prophet Arena benchmark over a 10-week horizon: Brier score improved by 20.8% and market returns by 12.9%; consistent gains over strong baselines on deep-research benchmarks. Underlying LLMs are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No parametric or fine-tuning arm is compared, so whether in-context memory evolution substitutes for or adds to weight updates is untested; inference token cost of retrieving and compiling guidelines per task and the noise floor of a single 10-week live run are not reported.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-02-02",
  "id": "arxiv:2602.02369",
  "title": "Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback"
 },
 {
  "claim": "Existing benchmarks cannot rigorously evaluate continual learning in language agents; controlled compositional task streams with intentionally reusable sub-solutions separate memory designs by their plasticity far better than naive streams, while naive and held-out settings often show limited gains and can expose memory-induced degradation.",
  "method": "AgentCL builds compositional task streams where earlier sub-solutions, evidence or workflows are reusable later, contrasts them with naive streams, defines transfer-gain metrics, and uses MemProbe, a probing memory that stores interactions, insights and skills and filters unreliable experiences during consolidation, to diagnose non-parametric memory designs.",
  "evidence": "Coding, deep research, and language understanding/reasoning tasks; evaluation of non-parametric memory designs; qualitative findings that controlled streams distinguish designs while naive and held-out settings yield limited gains and sometimes degradation. No headline numbers or models are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Only non-parametric (in-context) memory designs are evaluated, so parametric or weight-update continual learning is not compared on the same streams; no accounting of the token or compute cost of memory is described.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-06-02",
  "id": "arxiv:2606.02461",
  "title": "AgentCL: Toward Rigorous Evaluation of Continual Learning in Language Agents"
 },
 {
  "id": "arxiv:2507.00014",
  "date": "2025-06-13",
  "claim": "A chronologically ordered continual-learning benchmark built on SWE-Bench Verified enables direct evaluation of a coding agent's ability to accumulate experience, transfer knowledge across tasks, and resist catastrophic forgetting.",
  "method": "Organizes SWE-Bench Verified GitHub issues into chronological per-repository sequences; provides an inter-task similarity and contextual-sensitivity analysis, a LangGraph-based evaluation framework with a FAISS-backed semantic memory module, and continual-learning metrics (average accuracy, forgetting, forward/backward transfer, tool-use efficiency, Composite Continual Learning Score, CL-F-beta), plus a protocol comparing memory-enabled and memory-disabled agents.",
  "evidence": "Benchmark and framework only; the abstract outlines a protocol comparing memory-enabled vs. memory-disabled agents across diverse Python repositories but reports no experimental results or numbers; code and data at github.com/thomasjoshi/agents-never-forget.",
  "stated_limitations": "not stated",
  "not_tested": "No empirical results are reported, so the benchmark's sensitivity to memory or to forgetting is unverified; no parametric (fine-tuned) agent arm is described alongside the retrieval-memory arm.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "title": "SWE-Bench-CL: Continual Learning for Coding Agents"
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
  "claim": "Letting an agent search the raw corpus directly with general-purpose terminal tools, without any embedding model, index or retrieval API, outperforms conventional sparse, dense and reranking retrievers for agentic search.",
  "method": "Direct corpus interaction (DCI): the agent uses grep, file reads, shell commands and lightweight scripts over the raw corpus, with no offline indexing, allowing multi-step clue combination and plan revision.",
  "evidence": "Several BRIGHT and BEIR datasets where DCI substantially outperforms strong sparse, dense and reranking baselines; strong accuracy on BrowseComp-Plus and multi-hop QA without any semantic retriever. Specific agent models and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report the token or latency cost of multi-step terminal interaction versus a single top-k retrieval; does not test scaling to very large corpora where grep-style search becomes expensive.",
  "axes": [
   "evaluation and cost of the two substrates"
  ],
  "date": "2026-05-03",
  "id": "arxiv:2605.05242",
  "title": "Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction"
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
  "id": "arxiv:2607.21051",
  "date": "2026-07-23",
  "claim": "In-context learning gains from agent interaction histories vanish when the experience leaves the context, but Experience Distillation (context distillation applied to those histories) retains most of the gains in the weights without any further environment interaction, whereas direct SFT on the same experience recovers almost none.",
  "method": "Experience Distillation: collect interaction histories, learn from them in context, then apply context distillation to internalize the context-conditioned behavior into model weights using no environment interaction beyond the collected experience.",
  "evidence": "749 curated software-engineering tasks and six text-adventure games; Experience Distillation retains at least 64.8% of in-context learning gains across both domains while direct SFT on the collected experience recovers only 3.8%; ICL plus Experience Distillation matches classical RL baselines with at least 9.6x fewer environment samples.",
  "stated_limitations": "not stated",
  "not_tested": "The abstract does not report training compute or token cost of distillation relative to keeping the experience in context, nor behavior under distribution shift or repeated distillation rounds over a long stream of experience.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "evaluation and cost of the two substrates"
  ],
  "title": "Sample-Efficient Learning from Agent Experience"
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
  "id": "arxiv:2605.09315",
  "date": "2026-05-10",
  "claim": "Self-evolution in LLM agents is often non-monotonic: adapting to new task distributions progressively erodes previously acquired capabilities across workflow, skill, model, and memory evolution channels, and an explicit capability-preserving constraint mitigates this.",
  "method": "The paper characterizes capability erosion under self-evolution across four evolution channels and proposes Capability-Preserving Evolution (CPE), a general stabilization principle that constrains destructive capability drift during continual adaptation.",
  "evidence": "Across workflow, skill, model, and memory evolution, CPE consistently improves retained capability stability while preserving adaptation performance; in workflow evolution under GPT-5.1 optimization, retained simple-task performance rises from 41.8% to 52.8% while complex-task adaptation also improves.",
  "stated_limitations": "not stated",
  "not_tested": "The abstract does not compare the size of erosion between the memory (context) channel and the model (weights) channel head-to-head under matched conditions; replay cost and recovery time after erosion are not quantified in the abstract.",
  "axes": [
   "continual adaptation and shift",
   "evaluation and cost of the two substrates"
  ],
  "title": "Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation"
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
  "id": "arxiv:2607.10608",
  "date": "2026-07-12",
  "claim": "Agents consuming conflicting retrieved memory fall into a compliance trap: they adopt task-wrong memory at the first exposed decision point, repeated exposure amplifies the error, recovery is weak, and once they comply success collapses to a low floor, so stronger agents suffer larger absolute damage.",
  "method": "The Entry-Propagation-Recovery (E-P-R) trajectory-level diagnostic framework asks where memory first changes an action, whether that change carries forward, and whether the agent recovers, instantiated on WebArena and on MemTrapBench, a controlled benchmark built to isolate the three phases.",
  "evidence": "WebArena and MemTrapBench across multiple models; conflicting memory induces similar compliance rates across models, and success rates collapse to a low floor after compliance; specific models and numeric rates are not given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the compliance trap persists or changes when the same conflicting experience is internalized into weights instead of injected into context; whether training the agent to critique retrieved memory reduces entry-point compliance.",
  "axes": [
   "what survives internalization",
   "evaluation and cost of the two substrates"
  ],
  "title": "The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory"
 }
]
