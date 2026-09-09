=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: hole_backfill_static_counterfactual — Which Counterfactual Is Item Credit? Hole, Backfill and Static-Procedure Replacement Give Different Per-Item Values for Retrieved Experience, and Only Backfill Predicts What Pruning Realizes

- arxiv:2604.05467 · 2026-04-07 · preprint · sim 0.49 · hf · found via methods
  CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation
  As language models shift from single-shot answer generation toward multi-step reasoning that retrieves and consumes evidence mid-inference, evaluating the role of individual retrieved items becomes more important. Existing RAG evaluation typically targets final-answer quality, citation faithfulness, or answer-level attribution, but none of these directly targets the intervention-based, per-evidence-item utility view we study here. We introduce CUE-R, a lightweight intervention-based framework fo
- arxiv:2608.01247 · 2026-08-02 · preprint · sim 0.44 · hf · found via baseline
  RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cache Eviction
  Query-agnostic KV cache eviction compresses a context once and reuses the resulting cache for arbitrary future queries, but performance can collapse under tight budgets. Existing methods primarily improve which original KV pairs are retained. We introduce RestoreKV, which complements this selection-based formulation with learned restoration under the same total KV budget. Our key insight is that, although the information lost through eviction is context-specific, the mechanism for generating its
- arxiv:2502.15082 · 2025-02-20 · preprint · sim 0.44 · hf · found via mechanism_home
  UPCORE: Utility-Preserving Coreset Selection for Balanced Unlearning
  User specifications or legal frameworks often require information to be removed from pretrained models, including large language models (LLMs). This requires deleting or "forgetting" a set of data points from an already-trained model, which typically degrades its performance on other data points. Thus, a balance must be struck between removing information and keeping the model's other abilities intact, with a failure to balance this trade-off leading to poor deletion or an unusable model. To thi
- arxiv:2608.22856 · 2026-08-24 · preprint · sim 0.42 · hf · found via methods
  Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Churn in Retrieval-Augmented QA
  A retrieval-augmented QA system can return different answers after an index expansion even when its requested model identifier, prompt, retrieval policy, evidence depth, rendering, and exposed generation controls are held fixed. Aggregate accuracy may hide these changes when gains and losses cancel, while ordinary generation variability makes one-shot comparisons overstate update effects. We call the hidden phenomenon accuracy-blind answer churn and introduce the Snapshot Compatibility Audit, wh
- arxiv:2511.11891 · 2025-11-14 · arXiv.org · sim 0.41 · s2 · found via adjacent
  FLEX: Feature Importance from Layered Counterfactual Explanations
  Machine learning models achieve state-of-the-art performance across domains, yet their lack of interpretability limits safe deployment in high-stakes settings. Counterfactual explanations are widely used to provide actionable"what-if"recourse, but they typically remain instance-specific and do not quantify which features systematically drive outcome changes within coherent regions of the feature space or across an entire dataset. We introduce FLEX (Feature importance from Layered counterfactual 
- arxiv:2606.25852 · 2026-06-24 · preprint · sim 0.39 · hf · found via agent
  Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
  Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress insi
- arxiv:2605.09287 · 2026-05-12 · preprint · sim 0.38 · hf · found via agent
  PiCA: Pivot-Based Credit Assignment for Search Agentic Reinforcement Learning
  Large Language Model (LLM)-based search agents trained with reinforcement learning (RL) have significantly improved the performance of knowledge-intensive tasks. However, existing methods encounter critical challenges in long-horizon credit assignment: (i) Reward Sparsity, where models receive only outcome feedback without step-level guidance to differentiate action quality; (ii) Isolated Credit, where credit is assigned to steps independently, failing to capture sequential dependencies; and (ii
- arxiv:2606.32017 · 2026-06-30 · preprint · sim 0.38 · hf · found via agent
  TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning
  Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework t
- arxiv:2608.28128 · 2026-08-28 · preprint · sim 0.37 · hf · found via agent
  VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning
  Fine-grained credit assignment is a central challenge in reinforcement learning for long horizon LLM agents. Standard objectives often train from programmatically verifiable terminal rewards by broadcasting each sparse outcome to every action in a trajectory. Existing methods typically seek finer credit from the rollout side, constructing auxiliary trajectory signals or additional comparisons to estimate action importance. Although useful, these approaches still treat the verifier that judged su
- arxiv:2608.05102 · 2026-08-05 · preprint · sim 0.37 · hf · found via agent
  ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment
  Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agents typically treat all steps within a trajectory uniformly during both supervised fine-tuning (SFT) and reinforcement learning (RL), failing to distinguish useful actions from erroneous or redundant ones. In this paper, we propose Answer-Backtracked Credit Assignment (ABC), a fine-grained credit assi

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2402.08845 · 2024-02-13 · sim 0.36 · via adjacent — Feature Attribution with Necessity and Sufficiency via Dual-stage Perturbation Test for Causal Explanation
- arxiv:2310.07047 · 2023-10-10 · sim 0.35 · via mechanism_home — A predict-and-optimize approach to profit-driven churn prevention
- arxiv:2311.00500 · 2023-11-01 · sim 0.35 · via adjacent/mechanism_home — Intriguing Properties of Data Attribution on Diffusion Models
- arxiv:2501.18887 · 2025-01-31 · sim 0.34 · via mechanism_home — Building Bridges, Not Walls -- Advancing Interpretability by Unifying
  Feature, Data, and Model Component Attribution
- arxiv:2302.12893 · 2023-02-24 · sim 0.34 · via adjacent — Don't be fooled: label leakage in explanation methods and the importance
  of their quantitative evaluation

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
