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
  "id": "arxiv:2608.09228",
  "date": "2026-08-10",
  "claim": "OPSD gains do not necessarily come from the teacher's access to the target-specific reference solution; the teacher's context-induced behaviour is an important factor.",
  "method": "OP²SD (On-Policy Self-Distillation from Other Problems) replaces the paired reference solution with a problem and solution from a different example while preserving the student rollout, teacher and distillation objective.",
  "evidence": "Three models and three mathematics benchmarks; OP²SD improves over the base model and remains competitive with OPSD; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "Only mathematics benchmarks are used, so whether the finding holds in agentic or long-horizon settings is not described; the abstract does not separate how much of the OPSD gain is attributable to the reference versus the context effect quantitatively.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "title": "Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation"
 },
 {
  "id": "arxiv:2604.15559",
  "date": "2026-04-16",
  "claim": "Unsafe agent behaviours can transfer subliminally through trajectory distillation even after rigorous keyword sanitation, so explicit data sanitation is an insufficient defence and behavioural biases are encoded implicitly in trajectory dynamics regardless of tool interface.",
  "method": "Construct a teacher agent with a deletion bias (API-style tool setting) or a chmod-first preference (native Bash setting), distill it into a student using only trajectories from ostensibly safe tasks with explicit keywords filtered, and measure the student's inherited bias.",
  "evidence": "API setting: student deletion rate reaches 100% versus a 5% baseline under homogeneous distillation; Bash setting: student chmod-first rate reaches 30%-55% versus a 0%-10% baseline, with the strongest transfer in large-to-small distillation.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the same bias would transfer when the trajectories are kept in context (few-shot) rather than distilled into weights is not described; the number of teacher-student pairs and seeds behind the reported rates is not stated in the abstract.",
  "axes": [
   "what survives internalization",
   "internalization objectives"
  ],
  "title": "Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation"
 },
 {
  "claim": "Naively extending on-policy self-distillation to multi-turn agents degrades performance because privileged feedback is misaligned with the student's current decision context, and using hindsight-reflected next environment observations as locally aligned turn-level feedback fixes this.",
  "method": "After each rollout, HERO reflects on the completed interaction to convert each next environment observation into a compact turn-level diagnosis (necessity, validity, failure cause of the original action), which a self-teacher uses to provide dense token-level supervision for on-policy self-distillation.",
  "evidence": "Multi-turn agent benchmarks TauBench and WebShop; HERO improves task success and reduces unnecessary turns over environment-feedback-only self-distillation and GRPO, most effective under limited training turn budgets where successful rollouts are rare; no numeric values stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the internalized behaviour generalizes to unseen environments or tasks beyond TauBench/WebShop, and whether the learned policy is compared at matched training compute against keeping the reflective diagnoses in context at inference rather than distilling them into weights.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-06-10",
  "id": "arxiv:2606.11559",
  "title": "HERO: Hindsight-Enhanced Reflection from Environment Observations for Agentic Self-Distillation"
 },
 {
  "claim": "Privileged on-policy distillation for multi-turn agents suffers from state-reference mismatch when the student's rollout reaches states not covered by the reference trajectory, and routing distillation only to state-matched turns with state-conditioned teacher context consistently beats unconditional full-path distillation.",
  "method": "SMRC-SD checks at each turn whether the student's execution state matches a supported state on the successful reference trajectory, applies distillation only at matched states, and builds state-conditioned teacher context from the reference for each matched state.",
  "evidence": "ALFWorld and WebShop with Qwen3-1.7B; task success rises from 0.746 to 0.865 on ALFWorld and from 0.574 to 0.693 on WebShop over unconditional successful full-path distillation, with routing and context ablations supporting both components.",
  "stated_limitations": "not stated",
  "not_tested": "Only one small model (Qwen3-1.7B) is reported, and there is no comparison against keeping the reference trajectory in context at inference time or against RL baselines at matched compute.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-08-05",
  "id": "arxiv:2608.05219",
  "title": "When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents"
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
  "claim": "Self-supervised proxy tasks over unlabeled Wikipedia can generally enhance an LLM agent's context-memory capability so that subsequent task-specific post-training performs better than direct task-specific post-training alone.",
  "method": "MemTrain jointly optimizes with GRPO an end-to-end masked reconstruction objective (recover masked entities after multiple memory updates) and an intermediate memory recall objective (reconstruct masked history from intermediate memory states) over unlabeled Wikipedia corpora, then applies downstream post-training.",
  "evidence": "Long-text QA and search-based QA benchmarks across different models; consistent improvements in memory-intensive reasoning with gains up to 17.67 points over direct task-specific post-training.",
  "stated_limitations": "not stated",
  "not_tested": "No comparison against retrieval or external-memory alternatives at matched inference cost, and no evaluation of whether the trained memory behaviour persists under distribution shift beyond QA benchmarks.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-06-02",
  "id": "arxiv:2606.03197",
  "title": "MemTrain: Self-Supervised Context Memory Training"
 },
 {
  "claim": "Self-distillation effectiveness depends on the structural alignment between the feedback context given to the self-teacher and the solver's reasoning trace, with step-aligned critique yielding the largest gains because it targets only the tokens where reasoning fails.",
  "method": "Train a solver via self-distillation by matching its question-only student distribution to a self-teacher conditioned on feedback from a frozen critic, comparing three context conditions (binary reward/GRPO, reference solution, step-aligned critique) and analyzing per-token advantages.",
  "evidence": "Solver trained with feedback from a frozen critic; step-aligned critique outperforms GRPO by 16.11 points and reference-solution-conditioned self-distillation by 5.27 points (Avg@12); per-token advantage analysis shows step-aligned feedback changes only failing tokens while reference-solution conditioning pressures change at every token. Models, benchmarks and domain are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the internalized improvement persists across distribution shift or over multiple rounds of self-distillation; whether gains hold outside the single solver/critic setup (other model sizes, non-reasoning domains) or against a matched-compute baseline.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "date": "2026-06-09",
  "id": "arxiv:2606.11173",
  "title": "The Role of Feedback Alignment in Self-Distillation"
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
  "claim": "Giving the OPSD teacher each completed student trajectory as additional privileged information, and adapting the teacher toward verified success on failed trajectories, transfers a mean policy shift to the prefix-only student and improves over vanilla OPSD.",
  "method": "PAST conditions the privileged teacher on complete student trajectories (preserving the student distribution on correct ones, adapting the teacher toward success on failed ones under student-proximity regularization) while keeping the student's distillation prefixes unchanged; forward-KL distillation is characterized as projecting the teacher onto its conditional mean given the prefix.",
  "evidence": "Three mathematical reasoning benchmarks; PAST improves the Avg@12 macro average over Vanilla OPSD by 5.6 percentage points; a 2x2 factorial study attributes gains to both complete-trajectory access and teacher adaptation; trajectory removal and shuffling confirm the adapted teacher uses matching hindsight context. Model sizes are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Comparison against RL or compute-matched baselines rather than only vanilla OPSD; whether trajectory-conditioned teacher adaptation transfers outside mathematical reasoning or under distribution shift; the theoretical fixed-point claim is stated for the unclipped population objective, not the finite-sample clipped one.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "date": "2026-08-09",
  "id": "arxiv:2608.08726",
  "title": "PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation"
 },
 {
  "claim": "Adaptive weighting in multi-teacher knowledge distillation can be given operator-agnostic axiomatic foundations that yield existence, non-uniqueness, convergence, stability and safety-constraint results independent of any specific weighting formula.",
  "method": "An axiomatic framework formalizing structural conditions on adaptive weighting operators at token, task and context scales, with hierarchical composition via product-structure normalization and theoretical analysis of convergence, perturbation robustness and safety-constrained distillation.",
  "evidence": "Theoretical results only: existence and non-uniqueness of conforming operators, convergence of gradient-based optimization under standard assumptions, stability analysis, and an abstract safety-constrained formulation; no models, benchmarks or numbers are reported in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No empirical validation of the framework on any distillation task or model; no evidence that the theoretical guarantees hold for practical heterogeneity or distribution-shift regimes.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-01-25",
  "id": "arxiv:2601.17910",
  "title": "Adaptive Weighting in Knowledge Distillation: An Axiomatic Framework for Multi-Scale Teacher Ensemble Optimization"
 },
 {
  "claim": "Subliminal learning under SFT distillation is driven by trait-direction drift: biased teacher generation creates measurable preference gaps in semantically clean data, and student-recognizable gaps induce trait-aligned parameter updates that accumulate into behavioral transfer.",
  "method": "Validate the drift mechanism via preference-gap measurement, training-trajectory analysis and intervention, then propose probe-space corridor regularization that constrains parameter drift along a calibrated trait direction during SFT distillation.",
  "evidence": "Qwen setting with system-prompt-biased teachers generating semantically clean data (e.g. numeric sequences); corridor regularization lowers malicious-response transfer from 29.55% to 6.45% with low main-task accuracy cost and consistently suppresses animal-preference transfer.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the mechanism and defense hold for on-policy or privileged distillation objectives rather than SFT; whether corridor regularization generalizes beyond the calibrated trait direction (unknown or multiple hidden traits) or beyond the Qwen family.",
  "axes": [
   "what survives internalization",
   "internalization objectives"
  ],
  "date": "2026-09-01",
  "id": "arxiv:2609.01091",
  "title": "Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation"
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
  "claim": "On-policy self-distillation improves when, in addition to matching the privileged teacher's output distribution, the student is trained to match how the teacher's hidden states move along the same rollout (transition directions and trajectory geometry) rather than pointwise hidden-state values.",
  "method": "PHF adds to OPSD a hidden-flow loss that aligns token-to-token transition directions and trajectory geometry over selected generated positions across all layers, plus an adjacent-layer relation computed from those transitions, without pointwise hidden-state imitation; the transport term is invariant to shared trajectory offsets and the local geometry term to orthogonal transformations.",
  "evidence": "Qwen3-1.7B, 4B and 8B under the same 100-step training schedule; Average@12 aggregate improves over the authors' reproduced OPSD baseline by about +2.2, +1.5 and +1.7 points respectively; ablations against pointwise hidden-state matching, single-channel transition losses and layer-subset choices. Benchmarks are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether gains persist beyond the 100-step schedule or on models larger than 8B, and whether the student's behavior remains dependent on the privileged reference context at deployment (no privilege-illusion check); seeds and variance are not stated.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-06-28",
  "id": "arxiv:2606.29340",
  "title": "PHF: Privileged Hidden Flow for On-Policy Self-Distillation"
 },
 {
  "claim": "Always giving the privileged teacher the full reference reasoning in on-policy self-distillation causes a teacher-side exposure mismatch whose targets are too strong for the student to absorb, and treating teacher exposure as a learnable training-time control variable improves reasoning over fixed-exposure self-distillation and RL baselines.",
  "method": "ATESD models the reveal ratio of the reference reasoning with a lightweight Beta-policy controller conditioned on compact training-state statistics, holds one sampled exposure for a short window of student updates, and trains the controller with a discounted learning-progress reward that scores each decision by its effect on the student's future improvement.",
  "evidence": "AIME 24, AIME 25 and HMMT 25 on Qwen3-1.7B, 4B and 8B; ATESD improves over OPSD by +0.95, +2.05 and +2.33 Average@12 points respectively and outperforms competitive self-distillation and RL baselines; a fixed-exposure sweep shows full exposure is not reliably best and student-teacher mismatch grows monotonically with exposure.",
  "stated_limitations": "not stated",
  "not_tested": "Only math competition benchmarks on small Qwen3 models; whether compute is matched against baselines given the extra controller and hold windows is not stated, and there is no check of whether the trained student depends on residual privileged context at test time.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-05-12",
  "id": "arxiv:2605.11458",
  "title": "Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning"
 },
 {
  "claim": "OPSD degrades complex reasoning because it applies one direction of teacher supervision to all tokens; routing high-entropy tokens away from the privileged self-teacher and low-entropy tokens toward it preserves exploration while stabilizing step-level execution and beats RLVR and self-distillation baselines.",
  "method": "Direction-Adaptive Self-Distillation performs entropy-routed directional supervision on the model's own rollouts: high-entropy tokens are pushed away from the privileged teacher distribution and low-entropy tokens are pulled toward it, based on a token-level analysis of where conformity versus deviation helps.",
  "evidence": "Six mathematical reasoning benchmarks; best macro Avg@16 over strong RLVR and self-distillation baselines; Pass@k, reasoning-health and generalization analyses. Models, sizes and numeric gains are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "No results outside mathematical reasoning and no models or numbers are named in the abstract; whether the entropy routing threshold transfers across model sizes or domains is not addressed.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-05-21",
  "id": "arxiv:2605.22263",
  "title": "Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning"
 },
 {
  "claim": "In long-horizon tool-use RL, direct self-distillation can destroy tool use by rehearsing teacher behavior without identifying rewarded actions, so distillation should be used only to reshape token-level credit inside GRPO while the policy gradient remains in charge of the actor update.",
  "method": "SGCD samples mixed successful and failed sibling rollouts, has an external LLM summarize their contrast into a training-only credit reference, and uses the detached teacher/student divergence to reweight GRPO token advantages within bounds; the deployed student sees only the clean task prompt.",
  "evidence": "AppWorld TGC improves from 42.9 to 45.6 on test_normal and from 24.7 to 27.0 on test_challenge, and tau^3-airline held-out evaluator score improves from 0.583 to 0.602, versus GRPO-family comparators; reported as held-out point estimates. Base model is not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Results are given as point estimates with no seeds or variance reported, and the base model is not named; whether the rule holds beyond GRPO-family baselines or outside long-horizon tool use is not examined.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-07-13",
  "id": "arxiv:2606.12634",
  "title": "Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents"
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
  "id": "arxiv:2609.05295",
  "date": "2026-09-04",
  "claim": "A synthetic teacher extrapolated from the model's own RLVR training trajectory converts sparse outcome-driven parameter updates into dense token-level targets, so recursive on-policy distillation outperforms RLVR alone and on-policy self-distillation without any external teacher or privileged conditioning.",
  "method": "RISE extrapolates the displacement between the current checkpoint and a trailing anchor, in parameter space or output-logit space, to build a teacher that is refreshed each iteration, and combines RLVR outcome rewards with on-policy distillation toward that extrapolated teacher.",
  "evidence": "Experiments on mathematical reasoning, multi-domain STEM, code generation, and multi-turn agentic tasks; RISE outperforms RLVR-only training and on-policy self-distillation in all settings; models and numbers not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not involve in-context experience or memory, so it says nothing about what is transferred from context; no report of matched training compute against the RLVR and self-distillation baselines.",
  "axes": [
   "internalization objectives"
  ],
  "title": "RISE: Recursive Improvement via Self-Extrapolating Policy Distillation"
 },
 {
  "id": "arxiv:2602.12275",
  "date": "2026-02-12",
  "claim": "Training a student on its own trajectories while minimizing reverse KL against a context-conditioned teacher internalizes in-context knowledge more effectively than baseline methods, with higher task accuracy and better preservation of out-of-distribution capabilities.",
  "method": "On-Policy Context Distillation (OPCD) samples student trajectories and minimizes reverse KL divergence to a teacher conditioned on the context (historical solution traces for experiential knowledge distillation, or optimized system prompts for system prompt distillation), including cross-size distillation from larger teachers to smaller students.",
  "evidence": "Mathematical reasoning, text-based games, and domain-specific tasks; OPCD consistently outperforms baseline methods in task accuracy and OOD-capability preservation, and enables smaller students to internalize experiential knowledge from larger teachers; no numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not compare against simply keeping the context in the prompt at inference-time token cost, and does not examine repeated rounds of distillation or distribution shift over time.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "title": "On-Policy Context Distillation for Language Models"
 },
 {
  "id": "arxiv:2601.18734",
  "date": "2026-01-26",
  "claim": "A single model can teach its weaker self by conditioning a teacher policy on privileged information (verified reasoning traces) and distilling per-token into a student policy that sees only the question, yielding better token efficiency than RL and better performance than off-policy distillation.",
  "method": "On-Policy Self-Distillation (OPSD): one model serves as teacher (conditioned on privileged traces) and student (question only); training minimizes per-token divergence between the two distributions over the student's own rollouts.",
  "evidence": "Multiple mathematical reasoning benchmarks; 4-8x token efficiency compared to RL methods such as GRPO and superior performance over off-policy distillation methods; models not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Limited to mathematical reasoning with ground-truth traces; does not test agentic or memory-derived experience, nor whether privileged conditioning produces context-dependent behaviour that fails to transfer.",
  "axes": [
   "internalization objectives"
  ],
  "title": "Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models"
 },
 {
  "id": "arxiv:2608.14144",
  "date": "2026-08-14",
  "claim": "Informative teacher-student asymmetry for visual on-policy distillation can be created without privileged information by subtracting information from the student via strong augmentations, recovering most of the gain of privileged-information methods.",
  "method": "S^2VOPD distills the model's own distribution conditioned on the original image on-policy into the student distribution conditioned on a strongly augmented view of the same image, exploring four augmentation families and augmentation strength.",
  "evidence": "Six fine-grained perception benchmarks; Qwen3.5-4B improves from 70.7% to 77.4%, above all compared open-source models up to Qwen3-VL 235B and surpassing GPT-5.4; with the same training data it recovers 96% of the improvement of privileged-information methods; asymmetric augmentations help while symmetric self-distillation degrades performance.",
  "stated_limitations": "not stated",
  "not_tested": "Vision-perception setting only; does not test distillation of in-context experience or agentic behaviour, and does not report whether gains erode over repeated rounds.",
  "axes": [
   "internalization objectives"
  ],
  "title": "Self-Supervised Visual On-Policy Distillation"
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
  "claim": "Scaling model-generated distillation data makes subtle, induced teacher traits more recoverable in the student even when the data is off-task and never mentions the trait.",
  "method": "In a subliminal-learning-inspired controlled setup, a teacher induced to express a target trait generates restricted off-task data (e.g., number-only completions); students are trained on varying amounts of independent off-task data with matched no-trait controls, evaluated in a separate domain, and their LoRA updates analysed.",
  "evidence": "Controlled experiments across model families, trait types, multi-trait settings and cross-model transfer; larger independent datasets make the teacher's induced trait stand out more clearly in student behaviour, with the target trait usually growing more than other plausible traits; LoRA update analyses show a parallel trend. No specific numbers are stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not report whether trait-aware curation actually removes the transferred trait; does not test on-task or non-restricted (natural language) distillation data, or whether the effect holds under full finetuning rather than LoRA.",
  "axes": [
   "what survives internalization",
   "internalization objectives"
  ],
  "date": "2026-08-27",
  "id": "arxiv:2608.26958",
  "title": "Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable"
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
  "claim": "Turning an agent's own completed trajectories into natural-language skills that condition only a privileged teacher yields dense, stable distillation supervision that substantially improves multi-turn agent RL over both GRPO and on-policy distillation.",
  "method": "Skill-SD summarizes completed trajectories into compact skills used as training-only privileged information for the teacher, while the student acts under the plain task prompt and internalizes the guidance via an importance-weighted reverse-KL token-level distillation loss with the teacher dynamically synchronized to the student.",
  "evidence": "AppWorld and Sokoban agentic benchmarks; Skill-SD improves vanilla GRPO by +14.0%/+10.9% and vanilla OPD by +42.1%/+40.6% on AppWorld/Sokoban. Backbone models are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not compare against simply keeping the summarized skills in the student's context at inference time; does not report training-compute or seed variance for the reported gains.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "date": "2026-04-12",
  "id": "arxiv:2604.10674",
  "title": "Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents"
 },
 {
  "claim": "Reverse-KL on-policy distillation gives uninformative negative feedback when student trajectories fall outside the teacher distribution, and teacher-guided token-level generation combined with RLVR rewards remains effective under large policy divergence.",
  "method": "TGPO has the teacher directly guide token-level generation conditioned on student-generated contexts, combined with RLVR-style trajectory-level rewards, to steer exploration toward improved continuations instead of relying solely on evaluative RKL supervision.",
  "evidence": "Reasoning benchmarks; TGPO consistently outperforms existing RKL-based OPD methods and is robust across different teacher models. Specific benchmarks, student models and numbers are not stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not test agentic or memory-conditioned teachers, only reasoning tasks; does not report compute cost of teacher-guided generation relative to RKL-based OPD.",
  "axes": [
   "internalization objectives"
  ],
  "date": "2026-05-28",
  "id": "arxiv:2605.13230",
  "title": "Teacher-Guided Policy Optimization for On-Policy Reasoning Distillation under Large Policy Divergence"
 },
 {
  "id": "arxiv:2602.02244",
  "date": "2026-02-02",
  "claim": "Vanilla SFT before RL narrows the solution space by causing overconfidence and reduced diversity, and an entropy-preserving SFT (CurioSFT) that distills toward a self-generated temperature-scaled teacher preserves exploration that later yields larger RL gains.",
  "method": "Self-Exploratory Distillation toward a self-generated, temperature-scaled teacher, combined with Entropy-Guided Temperature Selection that adaptively adjusts distillation strength per token (amplifying exploration at reasoning tokens, stabilizing factual tokens) to limit forgetting.",
  "evidence": "Mathematical reasoning tasks on large reasoning models (models unnamed in abstract); in the SFT stage CurioSFT beats vanilla SFT by 2.5 points in-distribution and 2.9 points out-of-distribution, and the subsequent RL stage gains an average of 5.0 points.",
  "stated_limitations": "not stated",
  "not_tested": "Only mathematical reasoning is evaluated, not agentic or memory-conditioned settings; no report of matched training compute or seed variance for the SFT-vs-CurioSFT comparison, and 'knowledge forgetting' mitigation is asserted but the abstract gives no forgetting metric.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "title": "Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models"
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
  "id": "arxiv:2608.01735",
  "date": "2026-08-03",
  "claim": "The privilege illusion in on-policy self-distillation is caused by information asymmetry between a privileged teacher and the inference-time student, and anchoring distillation along matched-information paths in both directions alleviates it.",
  "method": "Dual-Anchored Policy Distillation combines Dual-Path Anchoring (a self-conditioned bridge aligning reference and rollout behavior along two matched-information paths) with Dual-Source Anchoring (applying those paths reference-to-rollout and rollout-to-reference to reduce reliance on privileged guidance while keeping correctness supervision).",
  "evidence": "Qwen3 models: DAPD outperforms OPSD by +2.00 points on average across tasks on Qwen3-4B, with gains of +2.69 at 4B and +2.78 at 32B; task names are not listed in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the privilege illusion and its fix apply when the privileged information is retrieved agent memory rather than generic privileged context; no report of seeds or noise floors around the roughly +2 to +3 point gains.",
  "axes": [
   "internalization objectives",
   "what survives internalization"
  ],
  "title": "DAPD: Dual-Anchored Policy Distillation"
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
