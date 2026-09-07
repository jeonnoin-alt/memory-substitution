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
  "id": "s2:55b0d65416a7f69b864f0e4ea1f5727751618c5d",
  "date": "2026-04-01",
  "claim": "Distillation can transmit a teacher's behavioural traits to a student through semantically unrelated data (subliminal learning), so models trained on each other's outputs may inherit properties not visible in the data.",
  "method": "A teacher model with trait T generates datasets of number sequences (and, more realistically, math reasoning traces or code) with references to T rigorously removed; a student is fine-tuned on them and tested for T, complemented by a theoretical result and an MLP classifier demonstration.",
  "evidence": "Traits such as favouring owls or broad misalignment transfer via number-sequence, math-reasoning and code data; the effect occurs only when teacher and student share the same or behaviourally matched base model; a theorem shows subliminal learning arises in neural networks under broad conditions and it is demonstrated in a simple MLP; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "Whether the transmitted traits persist or decay under further training or long update streams is not described; the abstract does not report the scale of the effect or which traits fail to transfer.",
  "axes": [
   "what survives internalization"
  ],
  "title": "Language models transmit behavioural traits through hidden signals in data"
 },
 {
  "id": "arxiv:2507.14805",
  "date": "2025-07-20",
  "claim": "Subliminal learning, the transmission of behavioural traits via semantically unrelated data, is a general phenomenon and an unexpected pitfall for AI development because distillation can propagate unintended traits despite data filtering.",
  "method": "A teacher with trait T generates number-sequence datasets (and code or reasoning traces) filtered to remove references to T; a student trained on them is tested for T, supported by a theoretical result and a simple MLP demonstration.",
  "evidence": "Traits such as liking owls or being misaligned transfer via number sequences, code and reasoning traces; the effect is not observed when teacher and student have different base models; theorem states subliminal learning occurs in all neural networks under certain conditions; no numeric headline figures stated.",
  "stated_limitations": "not stated",
  "not_tested": "Cross-base-model transfer is reported as absent but the abstract does not describe how many model pairs were tried; durability of the inherited trait under subsequent fine-tuning is not described.",
  "axes": [
   "what survives internalization"
  ],
  "title": "Subliminal Learning: Language models transmit behavioral traits via hidden signals in data"
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
  "id": "arxiv:2606.22019",
  "date": "2026-06-20",
  "claim": "Whether subliminal trait transfer can be audited before training depends on channel location, the carrier through which the trait reaches the student, rather than on model identity or scale alone, and an audit used outside its carrier regime can give false assurance.",
  "method": "Identify three transfer regimes (initialization-dependent body channel, vocabulary-geometry channel for masked single-token traits, and body-routed conditional behaviours) and test screens and mitigations appropriate to each, including a coverage cosine screen and orthogonalization of the trait's output row.",
  "evidence": "Coverage predicts held-out transfer in the body-channel regime (Spearman rho about 0.95; AUROC 0.997); in pretrained LMs the student's held-out probability for a loss-masked named entity rises to 0.40 on average (about 2500x) and a related semantic class transfers; orthogonalizing the output row collapses leakage while random-subspace edits do not; sycophancy with markers masked transfers about 0.63 of the teacher's effect and evades four audits across two model families.",
  "stated_limitations": "It is not a deployment-ready screen: an audit used outside its carrier regime can give false assurance; scoped as masked transfer of a condition-present policy.",
  "not_tested": "Transfer through multi-turn agentic trajectories rather than static distillation data is not described; whether the identified channels behave the same at larger model scales is not stated.",
  "axes": [
   "what survives internalization"
  ],
  "title": "Channel Location Constrains the Auditability of Subliminal Learning"
 },
 {
  "claim": "Subliminal transmission of a teacher's trait to a student occurs even through natural-language paraphrases with fixed semantic content, and content that explicitly contradicts the teacher's preference does not block it.",
  "method": "Fine-tune student models on paraphrases generated by a teacher system-prompted to love a particular animal, with aggressive filtering for paraphrase fidelity, and measure the student's preference for that animal when the paraphrased content is unrelated to the animal or explicitly expresses dislike.",
  "evidence": "Natural-language paraphrase training data from a system-prompted teacher; student preference for the teacher's favoured animal increases by up to 19 percentage points, including when content explicitly expresses dislike; specific models are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether transmission holds across teacher-student model pairs with different base models, and whether traits beyond animal preference (e.g., misaligned behaviours) transmit through paraphrases.",
  "axes": [
   "what survives internalization"
  ],
  "date": "2026-03-10",
  "id": "arxiv:2603.09517",
  "title": "You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases"
 },
 {
  "claim": "Subliminal learning is mediated by a single steering vector: the teacher's system prompt is approximated by an activation steering vector, and the student learns an aligned vector during fine-tuning, which explains why it does not transfer between models and why adaptive optimizers are required.",
  "method": "Across two open-source models, approximate the teacher's system prompt with a steering vector, show the student learns an aligned vector, demonstrate steering vector distillation on semantic and random vectors, and analyze activation gradients on steered data under adaptive versus non-adaptive optimizers.",
  "evidence": "Two open-source language models; system prompts well approximated by steering vectors are subliminally learned while others are not; activation gradients carry a small consistent component along the steering direction; no numeric results stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Only two open-source models are studied, and the analysis does not address whether the same mechanism applies to full fine-tuning versus LoRA or to task-content (non-trait) transfer.",
  "axes": [
   "what survives internalization"
  ],
  "date": "2026-05-31",
  "id": "arxiv:2606.00995",
  "title": "Subliminal Learning Is Steering Vector Distillation"
 },
 {
  "claim": "Subliminal learning is a fragile LoRA artifact: transmission has an inverted U-shaped dependence on LoRA rank, disappears under full fine-tuning, and depends on tokens (e.g., default system prompt, chat template) shared between fine-tuning and evaluation contexts.",
  "method": "Reproduce subliminal learning with a teacher-generated numerical-sequence dataset, vary LoRA rank versus full fine-tuning, vary the system prompt present during fine-tuning and evaluation, and localize the subliminal behaviour to computation at tokens seen in both phases.",
  "evidence": "Qwen models fine-tuned on teacher-generated number sequences; transmission peaks at intermediate LoRA rank and vanishes with full fine-tuning; a Qwen model fine-tuned with its default system prompt shows no subliminal learning when evaluated without a system prompt; no numeric values stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "The abstract mentions only Qwen models and the numerical-sequence domain, so whether the LoRA-artifact conclusion holds for other model families or for natural-language training data is not established.",
  "axes": [
   "what survives internalization"
  ],
  "date": "2026-05-30",
  "id": "arxiv:2606.00831",
  "title": "Subliminal Learning is a LoRA Artifact"
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
  "claim": "Subtle biases injected into a teacher model through minimal training-data poisoning propagate to distilled student models and are amplified, in both targeted and untargeted modes, and current defenses do not catch them.",
  "method": "Poison a small fraction of the teacher's training data, distill a smaller student from the teacher with various distillation methods, and measure adversarial bias rates in teacher and student across bias types and modalities; evaluate perplexity filtering, bias detectors and LLM autoraters as defenses and propose design principles for mitigation.",
  "evidence": "25 poisoned samples (0.25% poisoning rate); targeted mode yields biased student responses 76.9% of the time versus 69.4% for teachers; untargeted mode yields 5.7x-29.2x higher adversarial bias rate in students on unseen tasks; validated over six bias types (e.g., targeted advertisement, phishing links, narrative manipulation, insecure coding), various distillation methods, and text and code generation. Models are not named in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Whether biases delivered to the teacher through in-context experience rather than training-time poisoning transfer the same way, and how amplification depends on student size or distillation objective; models are not identified.",
  "axes": [
   "what survives internalization"
  ],
  "date": "2025-05-30",
  "id": "arxiv:2505.24842",
  "title": "Cascading Adversarial Bias from Injection to Distillation in Language Models"
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
  "id": "arxiv:2605.29557",
  "date": "2026-05-28",
  "claim": "Subliminal learning extends to quantum models, and whether hidden-task traits transmit through a public task interface is architecture dependent: classical networks leak little, quantum neural networks retain most of the hidden-task signal, with transmission governed by teacher drift magnitude and the fraction of hidden-relevant drift visible through the public interface.",
  "method": "Studies two distillation pathways (an auxiliary channel on random inputs and a restricted task channel where the student matches a public supervised output while the hidden behavior lives on a disjoint task) for classical neural networks and QNNs, and proposes a unified geometric account based on teacher drift.",
  "evidence": "Classical and quantum neural networks; both show efficient auxiliary-channel subliminal learning, while task-channel transmission is strong for QNNs and weak for classical networks; no numbers stated in the abstract.",
  "stated_limitations": "not stated",
  "not_tested": "Does not involve language models or in-context experience; whether the geometric drift account predicts trait transfer in LLM-scale distillation is untested.",
  "axes": [
   "what survives internalization"
  ],
  "title": "Quantum Subliminal Learning"
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
