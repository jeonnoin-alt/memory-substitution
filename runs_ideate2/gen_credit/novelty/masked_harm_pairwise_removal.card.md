=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: masked_harm_pairwise_removal — Masked Harm, Masked Help: Single-Item Removal Mis-scores Conflicting and Redundant Co-retrieved Experience, and the Pairwise Correction Costs Three Re-runs, Not Seven

- arxiv:2607.05274 · 2026-07-06 · preprint · sim 0.51 · hf · found via agent
  Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models
  Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We intro
- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.45 · hf · found via adjacent/baseline
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.43 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2605.05716 · 2026-05-07 · preprint · sim 0.43 · hf · found via mechanism_home
  More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding
  LLM agent systems are built by stacking scaffolding components (planning, tools, memory, self-reflection, retrieval) assuming more is better. We study cross-component interference (CCI): degradation when components interact destructively. We run a full factorial experiment over all 2^5=32 subsets of five components on HotpotQA and GSM8K with Llama-3.1-8B/70B (96 conditions, up to 10 seeds). The All-In system is consistently suboptimal: on HotpotQA, a single-tool agent surpasses All-In by 32% (F1
- arxiv:2606.25449 · 2026-07-21 · preprint · sim 0.43 · hf · found via agent
  Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One
  A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain. We call this brittle memory. The information loss is definitional; the finding is behavioral, and it turns on one thing, whether the memory kept a re-derivation basis (the source) rather than the answer. We
- arxiv:2508.11733 · 2026-03-25 · preprint · sim 0.42 · hf · found via agent
  SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication
  LLM-based multi-agent systems exhibit strong collaborative capabilities but often suffer from redundant communication and excessive token overhead. Existing methods typically enhance efficiency through pretrained GNNs or greedy algorithms, but often isolate pre- and post-task optimization, lacking a unified strategy. To this end, we present SafeSieve, a progressive and adaptive multi-agent pruning algorithm that dynamically refines the inter-agent communication through a novel dual-mechanism. Sa
- arxiv:2606.23581 · 2026-06-22 · preprint · sim 0.42 · hf · found via agent
  Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse
  Multimodal agents repeatedly re-examine the same video frames, UI screenshots, and rendered artifacts as their context window slides and reasoning iterates, yet every look-back re-encodes from scratch, because prefix caches serve reuse only at a fixed leading position. We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. This loss is asymmetric. The direct readout of a cached chunk is recovered exac
- arxiv:2605.30087 · 2026-05-28 · preprint · sim 0.41 · hf · found via agent
  Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison
  Emerging personal AI agents are moving toward persistent, multi-source memory. This creates an evaluation problem: systems must decide how to use conflicting or incomplete evidence; they cannot just retrieve facts from one clean history. Existing benchmarks rarely show whether an error came from the evidence given to a method or from the method's conflict-resolution step. We study this as selective QA over conflicting multi-source personal memory: systems answer based on conflicting, sometimes i
- arxiv:2608.08389 · 2026-08-09 · preprint · sim 0.41 · hf · found via agent
  Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research Agents
  Long-horizon research agents solve open-ended tasks through iterative retrieval, aggregation, and synthesis, but context grows rapidly while the marginal value of additional evidence often declines. This leads to unnecessary token cost, higher latency, and noisier inputs for final report generation. We study marginal value estimation for context management in deep research agents and present the first systematic stage-aware comparison of pruning strategies across the pipeline. We evaluate lightw
- arxiv:2602.02007 · 2026-02-02 · preprint · sim 0.40 · hf · found via agent
  Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation
  Agent memory systems often adopt the standard Retrieval-Augmented Generation (RAG) pipeline, yet its underlying assumptions differ in this setting. RAG targets large, heterogeneous corpora where retrieved passages are diverse, whereas agent memory is a bounded, coherent dialogue stream with highly correlated spans that are often duplicates. Under this shift, fixed top-k similarity retrieval tends to return redundant context, and post-hoc pruning can delete temporally linked prerequisites needed 

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2607.26371 · 2026-07-29 · sim 0.38 · via baseline — A Controlled Candidate-Set Benchmark for Offline Satellite-Security Plan Decomposition
- arxiv:2102.07619 · 2021-02-09 · sim 0.37 · via mechanism_home — MaskNet: Introducing Feature-Wise Multiplication to CTR Ranking Models by Instance-Guided Mask
- arxiv:2602.07150 · 2026-02-06 · sim 0.36 · via baseline — On Randomness in Agentic Evals
- arxiv:2411.16170 · 2024-11-25 · sim 0.32 · via mechanism_home — CARE Transformer: Mobile-Friendly Linear Visual Transformer via Decoupled Dual Interaction
- arxiv:2504.00470 · 2025-04-01 · sim 0.32 · via mechanism_home — Less is More: Efficient Black-box Attribution via Minimal Interpretable
  Subset Selection

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
