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
  "id": "arxiv:2601.03938",
  "date": "2026-01-07",
  "claim": "Aligning memory-replay schedules with a model-centric notion of time based on optimizer update magnitude, following the Ebbinghaus forgetting curve, mitigates catastrophic forgetting in LLM continual learning better than fixed step-based heuristics.",
  "method": "FOREVER defines model time by the magnitude of optimizer updates, uses a forgetting curve-based replay scheduler to decide when to replay and an intensity-aware regularization mechanism to control how to replay.",
  "evidence": "Three continual-learning benchmarks and models ranging from 0.6B to 13B parameters; FOREVER consistently mitigates catastrophic forgetting; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "The replay compute overhead relative to step-based replay is not stated in the abstract; no comparison with a non-parametric (external memory) alternative is described.",
  "axes": [
   "continual adaptation and shift"
  ],
  "title": "FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning"
 },
 {
  "id": "arxiv:2601.03641",
  "date": "2026-01-07",
  "claim": "The stability-plasticity dilemma in agent continual learning arises from failing to distinguish common knowledge shared across tasks from conflicting task-specific knowledge, and disentangling them at the parameter-update level yields strong continual learning with minimal overhead.",
  "method": "Agent-Dice, a parameter fusion framework with two stages: geometric consensus filtering to prune conflicting gradients and curvature-based importance weighting to amplify shared semantics, supported by theoretical analysis.",
  "evidence": "Extensive experiments on GUI agents and tool-use agent domains; Agent-Dice exhibits outstanding continual-learning performance with minimal computational overhead and parameter updates; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against external-memory (non-parametric) experience reuse is described; behaviour under long streams with distribution shift or recovery time after a bad update is not described.",
  "axes": [
   "continual adaptation and shift"
  ],
  "title": "Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning"
 },
 {
  "claim": "OLieRA, a Lie-group-based fine-tuning framework using multiplicative updates with orthogonality across task subspaces, mitigates catastrophic forgetting in sequential multi-task learning of LLMs better than additive low-rank methods like O-LoRA and N-LoRA.",
  "method": "Fine-tune LLMs sequentially with multiplicative Lie-group parameter updates that preserve parameter geometry while enforcing orthogonality between low-rank task subspaces; inference is replay-free and task-ID free, inherited from O-LoRA.",
  "evidence": "Sequential multi-task continual learning of LLMs; the Standard CL benchmark and larger task sequences; claims state-of-the-art on the Standard CL benchmark and 'highly competitive' on large task sequences, with no numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against context-based (in-context or retrieval) alternatives to weight updates, and no report of training or inference cost relative to replay-based methods; only parameter-regularization baselines (O-LoRA, N-LoRA) are named.",
  "axes": [
   "continual adaptation and shift"
  ],
  "date": "2025-09-07",
  "id": "arxiv:2509.06100",
  "title": "Orthogonal Low-rank Adaptation in Lie Groups for Continual Learning of Large Language Models"
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
  "claim": "Retrieval alone does not make agent memory valid evidence for the current query because compressed memory fragments lose their surrounding context (\"context collapse\"), and reinstating each memory's original episodic conditions before retrieval and synthesis consistently improves long-term memory performance.",
  "method": "RaMem is a four-stage pipeline: evidence anchoring grounds each memory in its original episodic conditions (event time, mention time, session span, participants), recall condition induction derives the evidence conditions implied by the query, validity-aware retrieval prioritizes context-compatible memories while keeping content-relevant candidates as fallback, and context-preserved synthesis exposes the selected memories' structured context to the generator.",
  "evidence": "Long-term memory benchmarks (not named in the abstract) across several backbones (not named); average F1 gains of more than 10% over strong memory baselines.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against internalizing the same experience into weights, and no report of the latency or token cost of the four-stage pipeline relative to plain retrieval; benchmarks and backbones are not identified in the abstract.",
  "axes": [
   "continual adaptation and shift"
  ],
  "date": "2026-06-22",
  "id": "arxiv:2606.22844",
  "title": "RaMem: Contextual Reinstatement for Long-term Agentic Memory"
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
  "claim": "Generated memory updates in LLM agents omit, corrupt or hallucinate content that then persists as system-state failures, and verifying memory transitions for coverage, preservation and faithfulness and training the updater with preference-guided RL improves both memory utility and reliability.",
  "method": "TrustMem uses a Memory Transition Verifier to score candidate write/revise/delete updates from the same memory state on coverage, preservation and faithfulness, builds preference pairs among those candidates, and applies preference-guided reinforcement learning to optimize memory updating behavior.",
  "evidence": "State-of-the-art results on MemoryAgentBench, HaluMem and the Mem-alpha validation set; +12.14 F1 on HaluMem memory extraction; transition-level omission, corruption and hallucination reduced by 40.1%, 79.1% and 50.0% versus the strongest baseline for each error type. Models are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Behavior over very long streams with distribution shift or how errors accumulate after many consolidations, and the compute or latency cost of running the verifier during consolidation; models are not identified.",
  "axes": [
   "continual adaptation and shift"
  ],
  "date": "2026-06-23",
  "id": "arxiv:2606.25161",
  "title": "TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory"
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
  "id": "arxiv:2606.04703",
  "date": "2026-06-03",
  "claim": "Under multi-iteration experience internalization, existing methods show progressive capability collapse rather than compounding improvement, and stability depends on principle-level experience granularity, step-wise injection, and off-policy context distillation from high-quality teacher trajectories.",
  "method": "Systematically examines experience internalization along three dimensions (experience granularity: principle-level vs. instance-level; injection pattern: step-wise vs. global; internalization regime: off-policy vs. on-policy context distillation) across repeated iterations of experience learning, and derives a recipe for stable internalization.",
  "evidence": "Multi-iteration experience-learning setting on long-horizon tool-use tasks; findings that principle-level experience is more durable than instance-level, step-wise injection significantly outperforms global injection, and off-policy context distillation on high-quality teacher trajectories is more stable than on-policy context distillation; models, benchmarks, and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report whether keeping the experience in context (no internalization) matches or beats the stable recipe at equal cost; the number of iterations, models, and seeds behind the collapse finding are not stated.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "continual adaptation and shift"
  ],
  "title": "Rethinking Continual Experience Internalization for Self-Evolving LLM Agents"
 },
 {
  "id": "arxiv:2602.03315",
  "date": "2026-02-03",
  "claim": "A memory representation that structurally balances abstraction and specificity, with primary abstractions indexing concrete values and cue anchors expanding retrieval access, scales agent memory better than RAG or knowledge-graph memories, which are special cases of the framework.",
  "method": "Memora organizes memory as primary abstractions that index concrete memory values and consolidate related updates into unified entries, plus cue anchors that connect related memories; a retrieval policy exploits these connections to retrieve beyond direct semantic similarity, and the paper shows RAG and KG-based memory emerge as special cases.",
  "evidence": "New state-of-the-art on LoCoMo and LongMemEval, with better retrieval relevance and reasoning effectiveness as memory scales; no numbers or models stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Purely context/retrieval memory; no comparison against internalizing the same information into weights, and no report of retrieval or consolidation cost as memory grows.",
  "axes": [
   "continual adaptation and shift"
  ],
  "title": "Memora: A Harmonic Memory Representation Balancing Abstraction and Specificity"
 },
 {
  "claim": "Language models can nearly eliminate forgetting during continual finetuning by replaying their own self-generated samples, but forgetting persists when the model has little remaining capacity, and replay removes the tradeoff between low learning rates and training steps.",
  "method": "Finetune language models on new tasks using self-generated samples drawn from the model's own training distribution as replay data, and compare forgetting across pretraining saturation levels and learning-rate settings.",
  "evidence": "Continual-learning finetuning experiments on language models; self-generated replay reported to nearly eliminate forgetting; models pretrained close to saturation still forget; low learning rates reduce forgetting but require substantially more steps; replay enables fast high-learning-rate finetuning without forgetting. Specific models, benchmarks and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report the cost of generating replay samples or how much replay is needed relative to the new-task data; does not state whether self-generated replay preserves in-context or agentic behaviours as opposed to task accuracy on prior tasks.",
  "axes": [
   "continual adaptation and shift",
   "internalization objectives"
  ],
  "date": "2026-05-25",
  "id": "arxiv:2605.26097",
  "title": "Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay"
 },
 {
  "claim": "Hippocampus-inspired binding and separation mechanisms enable parameter-efficient continual learning for video-language models that mitigates forgetting and improves cross-task generalization.",
  "method": "Bisecle combines a multi-directional supervision module to capture cross-modal relationships with a contrastive prompt learning scheme that isolates task-specific knowledge, updating a small subset of parameters while the bulk of the VLM stays frozen.",
  "evidence": "Evaluated on several VideoQA benchmarks in a continual-learning setting; reported to mitigate forgetting and enhance cross-task generalization. Specific models, benchmark names and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not compare parametric continual learning against keeping past experiences in context or retrieval memory; does not report replay cost or recovery time on long streams.",
  "axes": [
   "continual adaptation and shift"
  ],
  "date": "2025-06-30",
  "id": "arxiv:2507.00469",
  "title": "Bisecle: Binding and Separation in Continual Learning for Video Language Understanding"
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
  "claim": "Language-agent memory is mainly semantic, and an explicit episodic memory built as a time-aware hybrid graph with agentic iterative retrieval substantially improves episodic recollection and reasoning.",
  "method": "REMem converts experiences offline into a hybrid memory graph linking time-aware gists and facts, then performs online inference with an agentic retriever using curated tools for iterative retrieval over the graph.",
  "evidence": "Four episodic memory benchmarks; REMem outperforms Mem0 and HippoRAG 2 by 3.4% and 13.4% absolute on episodic recollection and reasoning tasks respectively, and shows more robust refusal on unanswerable questions. Backbone models are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not compare against internalizing the episodes into weights via finetuning; does not report staleness or maintenance cost of the memory graph as the interaction stream grows.",
  "axes": [
   "continual adaptation and shift"
  ],
  "date": "2026-02-28",
  "id": "arxiv:2602.13530",
  "title": "REMem: Reasoning with Episodic Memory in Language Agent"
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
  "id": "arxiv:2606.30626",
  "date": "2026-06-29",
  "claim": "Injecting privileged information into on-policy distillation induces a privilege illusion that conflates the closable capability gap with an unreplicable information-asymmetry gap, and routing token-level supervision between privileged teacher and privileged student by advantage gap alleviates it.",
  "method": "DOPD is an advantage-aware dual distillation scheme that per token dynamically routes supervision of varying strength, objective, and strategy to either a privileged teacher or the privileged student itself based on their advantage gap and relative probabilities.",
  "evidence": "LLM and VLM settings; DOPD consistently outperforms vanilla OPD and other counterparts, with additional results on stability, robustness, continual learning, and out-of-distribution tasks; no models, benchmarks, or numbers are given in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No headline numbers are given, so effect sizes and noise floors are unknown; the abstract does not say whether the student was evaluated with privileged information fully absent at inference, which is the defining test for the privilege illusion.",
  "axes": [
   "internalization objectives",
   "what survives internalization",
   "continual adaptation and shift"
  ],
  "title": "DOPD: Dual On-policy Distillation"
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
 }
]
