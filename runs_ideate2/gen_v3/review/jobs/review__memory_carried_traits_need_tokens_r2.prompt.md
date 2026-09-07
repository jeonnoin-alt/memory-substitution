=== SYSTEM ===
You are reviewing a research proposal for ICLR 2027 main track. Review it the way an experienced, skeptical area chair would: assume it will be rejected unless it earns acceptance, and look for the reason it would be.

Score honestly and use the full range — most submitted ideas are borderline or below, and a 9 means you would fight for it in discussion. Do not reward ambition, fluent writing, or a long experiment list; reward a claim that is new, testable, and actually tested by the plan as written.

Be specific: name the prior work that threatens novelty, name the baseline the plan omits, name the interleaving of results that would make the central claim collapse. "More experiments needed" is not an objection.

This field moves fast, so weigh recency: the work most likely to have scooped a proposal is an arXiv preprint from the last few months, not an indexed paper. Treat the proposal's Preprint Collision Check as part of the submission and judge it — a proposal that claims novelty without having looked for recent preprints has not established novelty.

The proposal is not supposed to contain code. Do not penalize the absence of implementation detail; judge the experimental design.

You have two literature search channels and a novelty card listing the closest candidates an automated search found.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.
Rules for this review: (1) Run at least two searches on the proposal's claimed mechanism, one restricted to the last
twelve months, and at least one on its closest named method. (2) Verify every arXiv ID the proposal relies on for its
novelty argument; say which you verified and which you could not. (3) In "closest_prior_work" name a paper you found
or verified, with its ID; if the strongest threat you know is from memory and you could not verify it, say so and
label it unverified. (4) In "preprint_collision" report the queries you ran and what they returned, with IDs; an empty
search is reported as empty, not as evidence of novelty. (5) If a search finds a paper that already makes the central
claim, say "VERIFIED COLLISION: <id>" as the first words of "preprint_collision"; the aggregate will cap novelty. Score
novelty on what you verified, not on what the proposal asserts.

=== OUTPUT SCHEMA (return ONLY JSON matching this) ===
{
 "type": "object",
 "properties": {
  "novelty": {
   "type": "integer",
   "description": "1-10"
  },
  "significance": {
   "type": "integer",
   "description": "1-10"
  },
  "soundness": {
   "type": "integer",
   "description": "1-10: would the proposed experiments actually test the claim?"
  },
  "feasibility": {
   "type": "integer",
   "description": "1-10: runnable on an academic budget as described"
  },
  "clarity": {
   "type": "integer",
   "description": "1-10"
  },
  "verdict": {
   "type": "string",
   "enum": [
    "accept-worthy",
    "borderline",
    "reject"
   ]
  },
  "one_line_contribution": {
   "type": "string",
   "description": "The new thing, in one sentence, in your own words. If you cannot state it, say so."
  },
  "closest_prior_work": {
   "type": "string",
   "description": "The work that most threatens novelty, and why it does or does not."
  },
  "strongest_objection": {
   "type": "string",
   "description": "The objection most likely to sink this in review."
  },
  "what_would_fix_it": {
   "type": "string"
  },
  "missing_baseline": {
   "type": "string",
   "description": "A baseline a reviewer would demand that the plan omits, or 'none'."
  },
  "preprint_collision": {
   "type": "string",
   "description": "Judge the proposal's Preprint Collision Check. Is there a recent arXiv preprint that already makes this claim? Name it if so. If the check is thin, vague, or reports no searches, say that \u2014 an unsearched claim of novelty is a weakness, not a neutral."
  }
 },
 "required": [
  "novelty",
  "significance",
  "soundness",
  "feasibility",
  "clarity",
  "verdict",
  "one_line_contribution",
  "closest_prior_work",
  "strongest_objection",
  "what_would_fix_it",
  "missing_baseline",
  "preprint_collision"
 ],
 "additionalProperties": false
}

=== USER ===
Proposal under review:

```json
{
 "Name": "memory_carried_traits_need_tokens",
 "Title": "Retrieved Memory Transmits Dispositions Subliminally in Proportion to Its Off-Span Divergence: A Carrier Contrast (Memory, Instruction, Parameters) Under Sanitised SFT and Masked On-Policy Self-Distillation in ALFWorld",
 "Short Hypothesis": "Subliminal transfer of a planted disposition through semantically clean tokens is set by how far the teacher's off-span token distribution diverges from its control (off-span per-token KL, D), not by whether the trait lives in retrieved memory, a system prompt, or parameters. Two sharp consequences. (i) On-policy reverse-KL with the trait's own positions and vocabulary masked from the loss transfers at least as much (ceiling-normalised) as keyword-sanitised SFT, because the divergence is delivered per token as a logit gap rather than through teacher samples; on-policy self-distillation is therefore not a defence. (ii) A trait read from k=3 retrieved walkthroughs (identical weights) is induced by local imitation and has lower D than the same trait induced by a one-sentence instruction at matched expression rate, so a memory-carried trait transfers through clean tokens at a fraction, predicted 0.2-0.6, of the instruction-carried rate: sanitising memory text attenuates internalisation but does not block it, and a parameter-carried teacher matched on D transfers the same amount as memory.",
 "Related Work": "Context-carried subliminal transfer through clean tokens is already demonstrated in text: 'You Didn't Have to Say It like That' (arXiv:2603.09517, verified) trains on paraphrases from a teacher system-prompted to love an animal and raises the student's preference by up to 19 pp despite aggressive fidelity filtering, and Cloud et al.'s teachers (2507.14805) are themselves prompt-induced; round 1 mischaracterised both, and the 'parameter-proximity account' it argued against is not a live hypothesis. What is untested is (a) whether the effect reproduces when the carrier is retrieved agent memory rather than an instruction, (b) whether it survives an on-policy reverse-KL objective with the trait's positions and vocabulary masked, and (c) whether the amount of transfer is predicted by a teacher-side, auditable quantity. Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation (2604.15559, verified by `s2cli paper` this session: S2, 2026-04-16, 4 citations) shows unsafe agent behaviours surviving keyword sanitation under trajectory distillation across 'two complementary experimental settings' whose details the literature tool does not return; this proposal no longer asserts what those settings are and positions only on (a)-(c). Corridor regularisation (2609.01091, titled 'under SFT Distillation') explains SFT transfer by preference gaps in clean data and predicts transfer wherever generation is biased; we extend its prediction to per-token KL gaps. Subliminal Learning Is Steering Vector Distillation (2606.00995) locates the channel in an activation direction preserved by adaptive optimisers, which predicts that any steered teacher, prompt- or memory-steered included, transfers through logits under any KL objective; Subliminal Learning is a LoRA Artifact (2606.00831) predicts adapter-specificity; Channel Location Constrains Auditability (2606.22019) separates body channels from vocabulary geometry and outputs. Decoupling KL and Trajectories (2605.16826) supplies the prefix-source x KL-direction taxonomy our objective ladder follows. Memory-conditioned self-distillation methods (OPSD 2601.18734, OPCD 2602.12275, Skill-SD 2604.10674, LOPSD 2608.13040, Agent Memory Distillation 2608.07169, PMD 2607.01480) never ask what else the memory-conditioned teacher hands over. The archived harm_does_not_distill was rejected for an underpowered success-side estimand and no positive control; this design uses a think-line trait rate with the training run as unit of inference and two positive controls, one per published construction.",
 "Abstract": "Agent memory systems make retrieved experience, written by other agents or earlier versions of the same agent, the privileged context of a self-teacher, and that experience carries dispositions along with procedures. In text, a disposition placed in a teacher's system prompt transfers to a student through faithfully paraphrased, filtered data (2603.09517), and in agent trajectories unsafe behaviours survive keyword sanitation under SFT (2604.15559). We ask what governs the size of this transfer and whether it survives the objective and the carrier that agent self-distillation actually uses. We plant a diffuse register trait (a cautious, precondition-checking style marked by eight phrases in the ReAct think lines) and a span-local trait (a superfluous inventory-first action) into a rewritten copy of the ALFWorld expert bank, and build three teachers with identical Qwen3-32B weights or a rate-matched adapter: memory-carried (k=3 retrieved rewritten items), instruction-carried (one-sentence system prompt, the construction of 2603.09517 and Cloud et al.), and parameter-carried (QLoRA on the rewritten walkthroughs, epochs chosen to match the memory teacher's off-span divergence, not its trait rate). Each teacher has a neutral control, and a self-distillation control with an empty retrieval block anchors the floor. Four objectives distil each teacher into a memory-free student: SFT, keyword-sanitised SFT, on-policy reverse-KL, and on-policy reverse-KL with the marker positions masked and the marker vocabulary filtered from the teacher distribution. The teacher-side measurand is the mean off-span per-token KL from control on a fixed rollout set; a gate on it ensures no sanitised-objective null is claimed where the design entails it. The student-side measurand is the marker rate per think line, with 4 training seeds on the central arms so that the training run is the unit of inference. Predictions: both published constructions transfer under sanitised SFT (positive controls); masked on-policy distillation transfers at least as much as sanitised SFT relative to its ceiling; the memory-carried teacher has lower off-span divergence than the instruction teacher at matched trait rate and transfers a fraction (0.2-0.6) of what the instruction transfers, while a parameter teacher matched on divergence transfers the same as memory. The result turns memory sanitation from a yes/no defence into a quantity that can be audited before distillation, and says whether on-policy self-distillation, the objective agent memory pipelines are converging on, adds any protection.",
 "Experiments": "(1) Pools and split. Of the 1,465 ALFWorld train tasks, one entire task type (the one with the fewest instances, ~120 games) is removed from both bank and targets and forms the procedure-held-out set H_type; the remaining ~1,345 tasks are split 40/60 into bank pool B (~540, retrievable only, never a training target) and target pool T (~805, distillation targets only, never retrievable), disjoint. Evaluation set E per student = valid_unseen (134) + H_type (~120) = 254 games, one evaluation seed, identical (game, seed) for every arm. Agent format is ReAct (think line, then action); if the pool walkthroughs lack think lines they are added once by rule for all arms so the format is constant. (2) Traits. T3 (primary, diffuse): a cautious-verifying register in think lines: every think line of a rewritten walkthrough states a precondition check and uses one of eight fixed marker phrases ('to be safe', 'double-check', ...); the label is the marker lexicon (~40 token ids over tokenisations and case), the carrier is the whole think line. T1 (secondary, span-local): inventory-first: every rewritten walkthrough begins with 'inventory' and its observation; label = the whole first agent turn. Task neutrality of each trait on the base agent: success shift within +/-5 net on the pooled check, else the trait is replaced (pre-registered). Banks B_T3 and B_T1 are rewrites of B by rule plus a rewriting pass of Qwen3-32B at temperature 0 for think lines; B_0 is the unrewritten bank passed through the same pipeline with a neutral instruction (paraphrase placebo), and B_0' is a second neutral pass used only for the divergence floor. (3) Teachers, all Qwen3-32B. MC: base weights + k=3 items from B_T retrieved by goal similarity. MC-0: same with B_0. SP: base weights + a one-sentence instruction inducing the register, no memory, two strengths, keeping the one whose marker rate on T matches MC within 5 pp. SP-0: token-matched neutral instruction. PC-d: QLoRA rank 32 on the rewritten walkthroughs of B_T at 1, 2 or 4 epochs, keeping the epoch count whose off-span divergence D matches MC within 20 %. PC-0: QLoRA on B_0 at the same epoch count. PC-r128: the same data with an unquantised rank-128 LoRA on all linear layers over an 8-bit base. CD0: base weights, empty retrieval block, no instruction (the P-CD0 self-distillation control). MC-decoy: base + k=3 trait-rewritten items of other task types, token-matched (teacher-side and inference reference only). Off-span divergence D(teacher) = mean per-token KL(teacher || its control) over agent tokens excluding label positions, computed by forward passes on one fixed set of 200 base-agent rollouts on T with the teacher's context or adapter applied; span KL is reported alongside; the floor is D(MC-0 || MC-0') with MC-0' reading B_0'. Gate 0 (adoption): MC and SP marker rate on T >= 0.5 of think lines and >= 0.4 above their controls. Gate 1 (non-triviality): D(teacher) exceeds the floor with a 95 % bootstrap CI over the 200 rollouts; a sanitised-objective null for any teacher that fails Gate 1 is entailed by the design and is neither run nor reported as a finding. Every teacher is rolled out once on all of T (~780 episodes) for SFT data, trait rate, success, and D on its own rollouts. (4) Objectives (student = base weights, empty block, no instruction, QLoRA rank 32, AdamW, one pass). SFT-full on teacher rollouts. SFT-clean = keyword sanitation of the same rollouts (marker phrases deleted by regex with a rule fluency fix, episodes with residual markers dropped), applied identically to every teacher's data. OPD-full = per-token reverse KL on student rollouts (390 targets per run, half of T, adapter hot-swapped into vLLM every 130 episodes) scored by the teacher with its context or adapter. OPD-masked = OPD-full with the KL zeroed at positions where the student emitted a marker token and with the marker token ids removed from the teacher distribution and renormalised at every position (vocabulary filter, the on-policy analogue of keyword sanitation). For T1: SFT-clean deletes the first agent turn and its observation; OPD-masked zeroes the KL on the whole first agent turn by rule regardless of what the student sampled. (5) Arms and seeds (T3). Central contrast, 4 training seeds each: MC and MC-0 x {SFT-clean, OPD-masked} (16 runs). Published constructions, 3 seeds each: SP and PC-d x {SFT-clean, OPD-masked} (12). One seed: SP-0, PC-0, CD0 x {SFT-clean, OPD-masked} (6); ceilings MC and PC-d x {SFT-full, OPD-full} (4); placebos: MC/SFT-clean deleting a random non-marker lexicon of equal size instead of the markers, MC-0/SFT-clean with a count-matched random deletion, MC/OPD-masked and MC-0/OPD-masked with a random equal-size vocabulary filter (4); PC-r128 x {SFT-clean, OPD-masked} (2); SP/OPD-masked with the corridor regulariser of 2609.01091 ported to the per-token KL (1); MC/SFT-clean-strict with think lines replaced by neutral plan paraphrases from a separate pass (1). Total 46 student runs, 23 SFT and 23 OPD. (6) Evaluation. Every student memory-free on E (254 games). The seed-1 student of each of the 8 central arms is also evaluated with matched memory (k=3 from B_T3) and mismatched memory (k=3 trait-rewritten other-type items, token-matched), giving the privileged-vs-unprivileged gap. In-context references: base agent on E with B_T3 at k in {1, 3, 7}, with B_0 at k=3, and with the decoy bank. Metrics: marker rate per think line (primary, cluster-robust by episode); judged register rate on 300 think lines per student by an Opus judge blind to arm (secondary); success rate; steps; per-episode inference tokens. (7) T1, gated: run only if D(MC-T1) clears Gate 1 and the T3 confirmatory runs finish by day 3: MC-T1 and MC-0 x {SFT-clean, OPD-masked} x 2 seeds (8), random-step-deletion placebo on both (2), MC-T1 rollouts on T (780); otherwise T1 reports Gate 0 and Gate 1 only (~1 GPU-h). (8) Cost on two A100 80GB, one vLLM replica per GPU, ~275 episodes per GPU-hour with >= 8 running per replica. PC teacher training 5 runs x 0.7 = 4 GPU-h; teacher rollouts 8 x 780 + 400 SP tuning = 6.6k episodes = 24 GPU-h; SFT runs 23 x 1 = 23 (+1 for rank-128); OPD runs 23 x 2 (390 rollouts, teacher scoring, gradient pass) = 46 (+1); memory-free evaluation 46 x 254 = 11.7k episodes = 42 GPU-h; matched/mismatched 8 x 2 x 254 = 4.1k = 15; in-context references 5 x 254 = 1.3k = 5; D measurements 2. T3 total 163 GPU-h = 3.4 days with training on one GPU overlapping serving on the other; T1 adds 25 GPU-h (10 runs, 780 rollouts, 2.5k evaluation episodes). Cost axis for every arm: training GPU-h plus per-episode inference tokens, with the k=3 in-context bank as the context arm on the same Pareto plot.",
 "Baselines and Ablations": "SP and SP-0 (instruction-carried, identical weights) through the same objectives: the exact construction of 2603.09517 and Cloud et al., so a memory-carried null is read against a replicated positive rather than in isolation. CD0 (empty retrieval block, same objectives) is the P-CD0 self-distillation floor; MC-0 minus CD0 isolates the memory-format effect. MC-0, SP-0, PC-0 under each objective give the drift of the marker rate due to self-training alone. SFT-full and OPD-full are ceilings and normalise transfer per objective so that the OPD pass (390 targets) and the SFT pass (780) are compared on ceiling fraction, not raw pp. Deletion placebo for SFT-clean: a random non-marker lexicon of equal size deleted from MC data (deletion per se does not suppress) and a count-matched random deletion from MC-0 data (deletion per se does not induce); for T1, random-step deletion. Filter placebo for OPD-masked: a random equal-size vocabulary filter on MC and MC-0 (filtering per se neither suppresses nor induces). Diffuseness matching: PC-d is matched to MC on off-span D, with its marker rate reported; the epoch sweep (1, 2, 4) gives PC's D and rate at three doses so that D, not rate, is shown to be the matching axis. Dose: in-context marker rate and D of MC at k in {1, 3, 7}. Decoy bank: trait-rewritten other-type items, at inference and as MC-decoy on the teacher side, to see whether the disposition reads from irrelevant memory. Strict sanitation (MC/SFT-clean-strict): think lines replaced by neutral plan paraphrases, the faithful-paraphrase regime of 2603.09517, one seed, to bound how much of the keyword-sanitised transfer rides on residual cautious content. Adapter check: PC-r128 teacher and students. Defence: corridor regulariser on one OPD-masked arm.",
 "Falsifiable Predictions": "Let Delta(X, obj) = marker rate of the X student minus its control under the same objective, seed-level mean with a t-interval over training seeds; norm(X, obj) = Delta(X, obj) / Delta(X, obj-full). P1 (positive controls, precondition): Delta(SP, SFT-clean) >= +10 pp (n=3), replicating the system-prompted construction of 2603.09517 in agent trajectories, and Delta(PC-d, SFT-clean) >= +10 pp, replicating the parameter-carried construction of 2604.15559. If both fail, the subliminal channel does not reproduce on this backbone and format and every other null is uninterpretable; if PC-d passes and SP fails, the context-carried channel of 2603.09517 does not reproduce in agent trajectories and that is reported as the main negative. P2 (objective, central): for each teacher passing P1, norm(X, OPD-masked) >= norm(X, SFT-clean) - 0.1: masking the trait's positions and filtering its vocabulary from an on-policy reverse-KL loss does not remove the transfer that keyword-sanitised SFT shows, even though SFT-clean additionally keeps the teacher's sample statistics. Falsified if norm(X, OPD-masked) <= 0.5 x norm(X, SFT-clean) for both SP and PC-d while the OPD-full ceilings reach >= 0.7 x the teacher's rate; falsification supports a sample-mediated channel and would make on-policy self-distillation a defence, against the per-token-gap reading of 2609.01091 and the steering-vector account of 2606.00995. P3 (carrier, central): (a) teacher side, D(MC) < D(SP) at matched marker rate, bootstrap CI over the 200 rollouts excluding zero, while both clear Gate 1; (b) student side, 0.2 <= Delta(MC)/Delta(SP) <= 0.6 under both sanitised objectives, with Delta(MC) >= MDE (pre-registered from the pilot seeds, expected ~6 pp, n=4 vs 4); (c) at matched D, |Delta(MC) - Delta(PC-d)| < margin = 0.25 x the Gate-0 lift (>= 10 pp), with the seed-level CI inside the margin. Falsified in one direction if Delta(MC) >= Delta(SP) - 3 pp (carrier irrelevant: retrieved memory is as potent as an instruction and sanitising memory buys nothing extra) and in the other if Delta(MC) < MDE while Delta(SP) >= 10 pp (the round-1 hypothesis: memory-carried traits transfer only through their own tokens). (c) failing with Delta(PC-d) > Delta(MC) + margin means parameters transfer more than D predicts, a residual weights-vs-context effect in the Cloud et al. reading. P4 (internalisation): the MC/OPD-full student's memory-free marker rate exceeds the base agent's in-context rate with B_T3 at k=3, and its matched-memory minus memory-free gap is < 5 pp against >= 30 pp for the base agent. P5 (secondary defence): the corridor regulariser cuts Delta(SP, OPD-masked) by >= 50 %. P6 (locality, gated): D(MC-T1) sits at the floor, so Gate 1 fails and T1's sanitised null is reported as entailed, not found; if Gate 1 passes, Delta(MC-T1) < Delta(MC-T3) under both sanitised objectives. P7 (adapter): the PC-r128 arms reproduce the sign of P1 and P2 within the rank-32 intervals; a sign flip flags P1/P2 as adapter-specific in the sense of 2606.00831.",
 "Measurement and Noise Control": "Unit of inference is the training run. Per-run precision: 254 episodes x ~10 think lines = ~2,500 lines per student, cluster-robust by episode, giving a 95 % half-width of about 2.5 pp at a marker rate of 0.2; this is well below the seed-level spread that matters. Pilot: the 4 seeds of MC-0/SFT-clean and MC-0/OPD-masked run first and give the seed SD (SD_s) per objective; MDE for a 4-vs-4 seed contrast = 2.45 x SD_s x sqrt(1/2), i.e. ~5.2 pp at SD_s = 3 pp, ~7 pp at 4 pp; MDE for the 4-vs-3 MC-vs-PC-d contrast at SD_s = 3 pp is ~6 pp. Pre-registered before the confirmatory runs: P3(b) requires Delta(MC) >= MDE; the P3(c) margin is 0.25 x the Gate-0 lift (>= 10 pp), and if MDE exceeds the margin the carrier-equivalence part is declared untestable and only the ordered predictions P3(a)-(b) are confirmatory; if SD_s > 4 pp, two more seeds are added to each MC/MC-0 arm with the budget taken from T1. Teacher-side D uses 200 fixed rollouts with a bootstrap CI over rollouts and a floor from two neutral paraphrases of the same bank, so Gate 1 is a measured, not assumed, non-triviality. Teacher trait rates and D are also computed on each teacher's own T rollouts, so rate and divergence matching are verified on the training distribution. Success rate is a neutrality check only: 254 games x 1 seed gives about +/-9 net per student, +/-4.5 pooled over 4 seeds; a trait that moves pooled success by more than 5 net is replaced (pre-registered amendment). The judged register rate (300 lines per student, Opus, blind) is secondary and reported with its Wilson interval; the marker rate is the primary because it is rule-scored and the sanitation target. All contrasts are paired on identical (game, seed) sets; ceilings are single-seed and are used only to normalise, with their own per-run intervals propagated.",
 "Preprint Collision Check": "Literature tool only (WebSearch quota exhausted; no WebFetch). Lookup 1: `s2cli paper 2604.15559` resolved this session (S2, 2026-04-16, 4 citations, Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation), contrary to the reviewer's failed lookup; the tool returns only the summary sentence ('two complementary experimental settings', 'explicit data sanitation is an insufficient defense'), so the proposal no longer claims to know those settings. Lookup 2: `s2cli paper 2603.09517` resolved (S2, 2026-03-10, 4 citations): system-prompted teacher, paraphrases, up to +19 pp despite fidelity filtering; now cited as the direct context-carried positive that P1/SP replicates and P3 is measured against. Query 3 (all years): 'Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation two complementary experimental settings' returned 2606.00995 (Subliminal Learning Is Steering Vector Distillation, 2026-06-03), 2604.15559, 2507.14805, 2505.17612 (Agent Distillation with retrieval and code tools), 2510.07709; 2606.00995 is now cited as the account predicting P2. Query 4 (--recent): 'system-prompted teacher trait transfer on-policy distillation reverse KL masked tokens identical weights student' returned 2607.17247 (Distilled RL), 2607.16955 (CADENCE), 2605.30833, 2605.21699 (X-Token), 2605.16826, 2603.07079, 2503.20083; none tests trait transfer under an on-policy or masked objective. Query 5 (--recent): 'subliminal learning full fine-tuning versus LoRA rank artifact replication trait transfer' returned 2605.07111, 2601.22708, 2508.02107; no replication or rebuttal of 2606.00831 surfaced, so the adapter question stays open and is handled by the PC-r128 arm. The reviewer's five queries (retrieved-memory carrier, prompt-vs-finetuned carrier contrast, agent-memory self-distillation) found no preprint making the carrier or masked-on-policy claim. No verified collision on: a masked or vocabulary-filtered on-policy reverse-KL trait-transfer test; retrieved agent memory as the carrier; a memory/instruction/parameter carrier contrast at matched off-span divergence.",
 "Risk Factors and Limitations": "Conceded, not fixed: full-parameter fine-tuning of a 32B model does not fit two 80GB GPUs, so the adapter check is rank-128 unquantised LoRA versus rank-32 QLoRA, which bounds but does not settle 2606.00831's artifact claim; all arms use AdamW, so the optimiser dependence reported by 2606.00995 is not varied. The details of 2604.15559's two settings could not be read through the literature tool; the proposal makes no claim about them. Keyword sanitation removes the trait's label and not its cautious content, so the primary SFT-clean transfer is the 2604.15559 regime, not the faithful-paraphrase regime of 2603.09517; the one-seed strict-sanitation arm bounds the difference but cannot decide it. The marker rate is a lexical proxy for a stylistic disposition; the judged register rate is secondary and single-judge. The OPD pass covers half the targets, so OPD and SFT are compared on ceiling-normalised transfer, and the ceilings are single-seed. On-policy distillation with adapter hot-swapping is the main engineering risk; if the swap cadence cannot be met the OPD arms run with 3 fixed refreshes and this is reported. SP may not match MC's marker rate within 5 pp at either strength, in which case the closest strength is used and Delta is additionally reported normalised by the teacher's rate. Gate 0 may fail for MC (memory-read adoption of a register from three exemplars is expected but unmeasured), in which case the memory-carried regime is untestable and the SP and PC-d legs still decide P1 and P2. Gate 1 is expected to fail for T1, in which case T1 contributes only the locality point that a single-span, imitation-induced trait leaves the off-span distribution at floor. Traits are benign by design; the harm extension of round 1 is dropped; one backbone, one environment, and the step from planted registers to unsafe dispositions in real agent memories is by argument."
}
```

Research area this was proposed for:

# Title: The Same Experience Pool in Weights and in Context: What Transfers, What It Costs, and Where the Two Substrates Fail

Author: Fable 5.1, 2026-09-07. Stage-1 brief for the ideate2 pipeline, written after the Stage-0 pre-scan on this topic
(5 axes, 79 papers carded from S2 + HF, 26 gaps synthesized; see `digest.md`; no section-level reads this round, the
WebSearch quota was spent on the previous topic) and after Step 0, a measurement pass on this node that replaces the old
pilot's numbers with numbers from the backbone the experiments will actually use (`runs/STEP0_RESULTS.md`).

## Keywords
LLM agents, experience memory, in-context experience, parametric memory, context distillation, on-policy self-distillation,
privileged information, privilege illusion, LoRA, continual adaptation, amortization, cost-matched evaluation, ALFWorld

## TL;DR
An agent's past episodes can be reused two ways: retrieved into the prompt at inference, or trained into the weights. The
2026 literature has dozens of systems on each side and a growing family of hybrids, and the Stage-0 scan finds the same
hole under every axis: almost no paper builds both routes from the same experience pool on the same backbone and reports
them on one cost axis, almost none evaluates the trained student strictly without the memory it was trained with, and the
few memory-free margins that exist are 0.5–3 points without seeds. The program now has a measured starting position on
one node: with an expert pool, in-context retrieval on Qwen3-32B is worth +20 to +33 points on ALFWorld and does not turn
harmful up to k=7, and one epoch of QLoRA on the same pool costs about two GPU-hours. This track asks for the sharp,
falsifiable claim about what moves between the two substrates, at what cost, and where each one breaks.

## Starting position (measured here; not to be rediscovered)
**Measurement A, in-context retrieval on this node** (Qwen3-32B, thinking off, ReAct, expert bank of 1,465 replayed
walkthroughs, MiniLM retrieval on the goal sentence, paired over identical (game, seed), 274 games × 2 seeds per cell):

| split | k=0 | k=1 | k=3 | k=7 | net/100 at k=3 [95 % CI] |
|---|---|---|---|---|---|
| valid_seen | 0.536 | 0.739 | 0.807 | 0.846 | +27.1 [+18.6, +35.6] |
| valid_unseen | 0.549 | 0.776 | 0.869 | 0.877 | +32.1 [+22.9, +41.0] |

- The gain is procedure-bound, not scene-bound: unseen ≈ seen, and it is carried by the three multi-step types
  (clean/heat/cool then place: +39 to +55 net) whose procedure the k=0 agent fails to finish in 30 steps; most fixes
  convert timeouts. This is also the near-duplicate-template concern: same task type ⇒ near-identical procedure in the pool.
- No high-dose harm: k=7 ≥ k=3 ≥ k=1 on both splits, broken counts fall with k. The old pilot's one-sided harm (27B,
  self-built bank, "broke six or seven, fixed none") does not reproduce with an expert pool on this backbone.
- One type nets negative under retrieval: look-at-object-in-light (−4.8 net/100, n=62). It is the only natural harm regime
  on this node and it is small; any harm-side question needs a manufactured regime (see rules).
- Injected tokens: ~140 at k=1, ~430 at k=3, ~1,010 at k=7 per episode.

**Measurement B, parametric route cost** (QLoRA nf4 rank 32 on Qwen3-32B, step-level SFT on the same pool, 8,854 examples
of ~300 tokens): 385 tok/s at batch 4, 31.5 GB peak, 0.8 s per example, one epoch ≈ 2 GPU-hours on one A100; loss fits
the procedure within tens of steps. Serving a trained arm costs one vLLM restart (~3 min). Feasible; accuracy untested.

**In progress:** the agent's own k=0 successes on the 1,465 train tasks are being collected as a second, on-policy pool
(`runs/bank/own_rollouts_train.jsonl`). Every question below must be answerable on both pools, because the expert pool
is off-policy text and the literature's largest parametric gains come from self-generated data.

**Carried over from earlier rounds:** the 2026-08 pilot findings (memory can be one-sidedly harmful at high injection
volume; volume, not content, was the lever; noise of 0.05–0.14 on a headline metric swallowed most claims) and 51 archived
ideas (appendix). Three of the 51 already sit on this topic and were rejected or left borderline; their objections are
binding on the next round (appendix B).

## What the Stage-0 scan says, by axis
1. **Internalization objectives** (39 cards). The objective menu is now large and well studied on math: on-policy
   self-distillation from a privileged teacher (OPSD 2601.18734; π-Distill 2602.04942; OPCD 2602.12275), its repairs for
   multi-turn agents (HERO 2606.11559; SMRC-SD 2608.05219; Skill-SD 2604.10674; SGCD 2606.12634), skill and memory
   internalization on ALFWorld/WebShop (SKILL0 2604.02268; SIRI 2606.02355; PMD 2607.01480; Skill0.5 2605.28424; UCOB
   2606.29502), and context distillation of interaction histories (Experience Distillation 2607.21051: ≥64.8 % of the
   in-context gain retained memory-free, direct SFT 3.8 %). The gap named by every synth: none of them runs the
   keep-it-in-context arm at matched training compute and inference tokens, so "distilling beats RL/SFT" is established and
   "distilling beats context" is not. A multi-iteration study reports progressive collapse, not compounding (2606.04703).
2. **What survives internalization** (26 cards). Two literatures that do not talk to each other: the privilege-illusion
   family (DAPD 2608.01735; DOPD 2606.30626; OP²SD 2608.09228 shows OPSD gains come partly from context-induced teacher
   behaviour, not the reference) and the subliminal-transfer family (2507.14805; steering-vector account 2606.00995; LoRA
   artefact claim 2606.00831 vs natural-language transfer 2603.09517; corridor regularization 2609.01091; unsafe agent
   trajectories 2604.15559). Nobody has asked either question with retrieved agent memory as the privileged information, and
   nobody has run the paired condition "same material kept in context vs distilled" for harm, bias, or conflicting memory
   (compliance trap 2607.10608).
3. **Hybrids and routing** (26 cards). Routers exist (UniMem 2607.26017; COVE 2608.01234; Skill0.5; substrate benchmark
   2608.15008 concludes "no substrate dominates, routing is necessary") and memory-free deployment margins are reported
   (SESA 2607.29468: 1.8–2.2 memory-free, +0.5–1.0 with the bank back). The train-by-infer 2×2 (trained with/without memory
   × deployed with/without) is never reported with seeds; the information-abundance effect (abundant train-time context
   reduces what is encoded parametrically, 2608.12218) is shown only on documents and generic SFT, never on trajectories.
4. **Continual adaptation and shift** (27 cards). Erosion under self-evolution is documented across memory and model
   channels (2605.09315), stability–plasticity is re-framed as a retrieval problem (2604.27003), and benchmarks exist
   (AgentCL 2606.02461; OAKS 2603.07392; SWE-Bench-CL 2507.00014) but each evaluates only non-parametric memories; the
   parametric CL papers (FOREVER 2601.03938; Agent-Dice 2601.03641; self-generated replay 2605.26097) evaluate only weights.
   No paper puts both substrates on one stream with the same backbone and reports forgetting, transfer and recovery time.
5. **Evaluation and cost** (24 cards). Inference tokens of retrieval, reconstruction and guideline compilation are left out
   of accuracy comparisons (ReMe's 8B-with-memory > 14B-memoryless, 2512.10696; MemHarness 2607.28272); training compute of
   internalization is never amortized against memory-free inference; the one amortization analysis is for in-context
   distillation only (2512.02543: break-even after 843 episodes). Reported substrate differences are 1–5 points, usually
   single-seed.

## Rules for every proposal in this round (from 28 judge reviews of the previous round and the three archived objections)
- **Same pool, same backbone, one cost axis.** Every arm is built from one named experience pool (expert or self-rollout,
  both if possible) on Qwen3-32B and reported on a shared axis: training GPU-hours plus per-episode inference tokens, with
  a cumulative-cost curve or an explicit Pareto plot. "Weights beat context" without the context arm is not a finding.
- **Partition the pool.** No item that is an SFT/distillation target may also be a retrievable bank item at evaluation
  (bank pool ≠ target pool); otherwise own-bank vs swapped-bank contrasts measure memorization, not a read policy.
- **Self-distillation control (P-CD0).** Any context-distillation or on-policy arm needs the same objective run with an empty
  retrieval block, because self-training on ALFWorld train tasks is itself a large effect and generation format and
  on-policy-ness are confounded with the retrieved content.
- **Memory-free evaluation is mandatory** for every trained student, with three prompt conditions at test: memory absent,
  matched memory, mismatched memory (other task's items, token-matched). Report the privileged-vs-unprivileged gap.
- **Placebo arms for anything that injects less.** Token-matched and rate-matched decoys (relevance-destroyed, same length)
  at training time and at inference, since volume was the causal lever in the pilot.
- **Power gates tied to the measured effect.** Equivalence margins are pre-registered as a fraction of the effect measured at
  Gate 0, never a fixed 3 points; on this node a paired cell of 274 games × 2 seeds gives about ±8 net points at 95 %, so
  claims below ~6 points need more seeds, the held-out train split, or a manufactured regime. State the minimum detectable
  effect before the confirmatory run; if Gate 0 fails, the claim is declared untestable, not "confirmed by TOST".
- **Positive control for any dispositional claim.** A teacher context known to induce a disposition (e.g. a majority-action
  prior) must be shown to transfer under the same distillation before "X does not transfer" is asserted.
- **No prediction entailed by a definition.** An append-only bank cannot forget; a LoRA trained only on post-shift data
  cannot keep a renamed mapping. Stream designs need a bounded evicting bank, a reset-LoRA arm, and an off-stream capability
  probe that the shift did not relabel.
- **Procedure-held-out split.** Because the in-context gain is procedure-bound, at least one evaluation holds out an entire
  task type from both the bank and the training targets; scene-level "unseen" is not enough.
- **Public data, local models, days not weeks;** pre-registration of thresholds and amendments before the first
  confirmatory run; the noise floor of the setup (paired CI above) is part of the proposal.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Retained fraction and its cost.** For one pool, build (a) retrieval at k∈{1,3,7}, (b) QLoRA on the pool, (c) context
  distillation from the k=3-conditioned teacher, (d) P-CD0, and evaluate every trained arm memory-free and with memory back.
  What fraction of the +27/+32 in-context gain survives in weights, how does it scale with pool size (10 %, 30 %, 100 % of
  1,465 tasks) and with the procedure-held-out split, and where on the cumulative-cost curve do weights become cheaper
  than ~430 tokens per episode? Must go past `harm_does_not_distill` (asymmetric-filter framing, underpowered) and
  `amortization_horizon_ranking_flip` (8B-vs-14B, different backbones): same backbone, retained fraction as the estimand.
- **Q2 Which objective transfers what, and is the retrieved memory a privilege illusion?** With retrieved episodes as the
  privileged information, compare SFT on trajectories, off-policy context distillation, and on-policy self-distillation
  (reverse-KL to the memory-conditioned teacher) on the same pool; decompose the gain into reference-attributable and
  context-induced parts (OP²SD-style shuffled-memory teacher), and test whether the student's memory-free accuracy tracks
  the teacher's memory-conditioned accuracy or its memory-free one. Prediction must be stated per objective and per task type.
- **Q3 Training-time context dose and context reliance.** Vary k in the prompt during SFT/distillation (0, 1, 3, 7, decoy);
  evaluate with context present, absent, and misleading. Does abundant train-time experience reduce what is encoded
  (2608.12218's information-abundance effect) on agent trajectories, is the optimum intermediate, and does the effect
  reverse on the self-rollout pool? Must differ from `memory_in_the_loop_training_decomposition` by the dose ladder, the
  pool partition, and a training-time decoy arm (its named missing baseline).
- **Q4 Harm and dispositions across substrates.** Only in a manufactured high-harm regime (Gate 0: in-context harm ≥ 6 net
  points, e.g. planted wrong-procedure items or the compliance-trap construction) with a positive control: does the same
  harmful material harm more when distilled than when read, does the entry-propagation-recovery signature change form, and
  does the corridor-regularization defence (2609.01091) have an in-context analogue? Also the subliminal question the field
  left open: do agent-trajectory traits transfer under on-policy distillation, or only under SFT/LoRA?
- **Q5 Same stream, both substrates, symmetric design.** A stream with a mid-stream rule change; arms: bounded evicting bank,
  unbounded bank, continual LoRA, reset LoRA, LoRA with self-generated replay; a randomized dose ladder of pre-shift items in
  the retrieved set at fixed k and tokens; off-stream capability probe. The honest hypothesis is "both erode, at different
  rates and with different recovery times"; `opposite_sided_failure_under_shift` was rejected for asserting the definitional
  version.
- **Q6 The memory-free margin and the 2×2.** Trained with/without memory × deployed with/without memory, on both pools, with
  seeds and per-step tokens: is the in-context channel still additive after internalization (SESA's +0.5–1.0), is it
  substitutive, or does training with memory make the memory-free policy worse (the crutch)? Small margins are expected,
  so the proposal must show the design can resolve 2 points.

## In scope
- ALFWorld (primary; 1,465 train tasks, 274 validation games, expert and self-rollout pools already on disk); WebShop or a
  text-game second environment if the claim needs a second domain; public data only.
- Qwen3-32B as agent, teacher and student (QLoRA rank 32 fits one A100); other local models only as a robustness check.
- Reimplementation of one published objective per family (OPSD/OPCD, Experience Distillation, SIRI-style skill
  internalization) as named baselines; null results when the measurement makes the null informative.

## Out of scope
- Frontier-model training; anything with private or clinical data.
- "We routed between memory and weights and the number went up" without the single-substrate arms at matched cost.
- Effects the setup cannot resolve (below the paired CI without a stated plan to shrink it).
- Restating any of the 51 archived ideas (appendix); a proposal near one of them must name the archived idea and state what
  it fixes.

## Resource constraints
Two A100 80GB on one node (not four); vLLM serves one Qwen3-32B replica per GPU; both GPUs must stay busy (a training arm
runs on one GPU while the other serves). Budget per confirmatory cell: 274 games × 2–3 seeds ≈ 550–820 episodes;
one QLoRA epoch on the full pool ≈ 2 GPU-hours (0.2–0.6 h for 10–30 % pools); one distillation arm additionally needs one
teacher pass over the target pool (~1,465 episodes with memory). A full Q1 on one pool is roughly 6 trained arms plus 4
retrieval cells, i.e. two to three days; plan seeds and gates accordingly.

## Appendix A: the 51 ideas already generated in this program (do not restate; differentiate or move on)
Round 1 (27, 3-judge Opus mean, `reviews/ideation/RANKING.md`): memory_item_value_reliability 6.12,
provenance_gap_selection_not_authorship 6.07, compile_dont_retrieve 6.0, memory_or_instruction 5.92,
failure_signature_routing 5.87, collection_policy_coupling_collapse 5.85, instruction_conditioned_complementarity 5.82,
coadaptation_transplant_ccr 5.77, decorative_retriever 5.75, memory_induced_shortcutting 5.72,
memory_vetoes_instruction_slot 5.72, coverage_currency_coupling 5.68, memory_budget_confound 5.63,
substitutes_not_complements 5.47, counterfactual_memory_screening_under_selection_noise 5.45,
memory_dropout_coadaptation 5.45, coverage_selection_division_of_labour 5.4, clause_level_portability 5.38,
commit_then_consult_slot_discipline 5.38, breadth_routed_memory 5.35, playbook_transfer 5.33,
meta_prompt_generalization 5.3, action_prior_imprinting 5.27, optimizer_substitutes_for_memory_scaffold 5.22,
query_agnostic_curation_ceiling 5.18, memory_volume_amplifies_optimizer_curse 5.05, allocation_prior_transfer 5.0.

Round 2 (24, open-book Opus, `runs_ideate2/gen_v2/review/RANKING.md`):
- abstraction_discards_bindings_and_repairs 5.95: scene bindings and failure-to-repair pairs explain when distilled experience beats raw trajectories
- closer_beats_stronger 5.75: consumer-side policy proximity, not builder capability, predicts cross-backbone transfer of shared experience
- model_shaped_instruction_task_shaped_store 5.75: the memory–instruction substitution does not survive a backbone swap
- failure_memory_framing_drag 5.72: cross-episode failure notes induce contextual drag; positive rewriting removes it
- order_randomized_leakage_audit 5.7: memory gains concentrate on tasks with a near-duplicate solved earlier in the stream
- memory_in_the_loop_training_decomposition 5.65: train-by-infer 2×2 with bank swap (crutch / content / read skill)
- optimizer_writes_the_read_policy 5.6: joint instruction–memory gains are carried by evolved clauses governing memory use
- gate_reads_style_not_truth 5.55: planted-record audit of write-time validation
- dormant_is_not_dead 5.45; need_blind_compaction_audit 5.45; stall_triggered_injection 5.45
- amortization_horizon_ranking_flip 5.35: cost definition and horizon decide whether 8B+memory beats 14B
- harm_does_not_distill 5.35: context distillation as an asymmetric filter on agent experience
- stale_true_state_facts_redaction 5.3; state_load_not_length 5.2; memory_surrogate_validity 5.15
- opposite_sided_failure_under_shift 5.05: in-context and parametric experience fail on opposite sides of a shift
- utility_pruning_is_frequency_pruning 4.9; contributor_conflict_not_size 4.85; wrong_action_fraction_dose 4.85;
  cross_episode_drag_content_not_label 4.8; lineage_blast_radius 4.75; coupling_variance_components 4.65;
  retrieved_set_disagreement_gate 4.65

## Appendix B: why the three parametric-axis ideas did not pass (binding objections)
- **harm_does_not_distill.** The equivalence margin (3 points) exceeded the harm being probed (~1.3 points on the held-out
  set), so "harm does not distill" and "harm distills but is invisible" were not separated; the second half of the claim was a
  failure-to-reject read as a null. Missing baseline: P-CD0 (context distillation from an empty-retrieval teacher), without
  which the retained-value fraction is confounded with generation format and on-policy-ness. Closest work: Experience
  Distillation 2607.21051 for the retained-gain half; DAPD 2608.01735 / DOPD 2606.30626 / 2608.05219 for the mechanism half.
- **memory_in_the_loop_training_decomposition.** Bank A items were also SFT targets, so the own-bank vs swapped-bank drop
  measured memorization and the co-adaptation claim was pre-determined. Missing baseline: a training-time relevance-destroyed
  decoy block of matched length, without which "crutch" is confounded with "long irrelevant prefix hurts SFT"; the GRPO arm
  had to be a named published objective (MemHarness reconstruction reward or UCOB). Closest work: UCOB 2606.29502 (credit-aware
  bidirectional self-distillation between skill-conditioned and no-skill prompts, ALFWorld/WebShop) and SESA 2607.29468.
- **opposite_sided_failure_under_shift.** The headline was definitional (an append-only bank cannot forget; a LoRA trained
  only on post-shift data cannot retain a renamed mapping); the stale-fraction regression was observational and collinear with
  probe index and bank size; no probe of a capability the shift did not relabel. Fix demanded: randomized dose ladder of
  pre-shift items at fixed k and tokens, bounded evicting bank, reset-LoRA arm, off-stream probe. Closest work: UniMem
  2607.26017 (contents unverified on either channel) and Do Self-Evolving Agents Forget 2605.09315.


Review it now.

=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: memory_carried_traits_need_tokens — Subliminal Transfer Needs a Parameter to Inherit: Memory-Carried Agent Traits Distil Only Through Their Own Tokens, Parameter-Carried Traits Also Through Clean Ones, Under Both SFT and On-Policy Distillation

- arxiv:2604.14004 · 2026-04-15 · preprint · sim 0.69 · hf
  Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents
  Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate Memory Transfer Learning (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate p
- arxiv:2601.07470 · 2026-01-12 · preprint · sim 0.62 · hf
  Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
  Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed desi
- arxiv:2606.22019 · 2026-06-20 · preprint · sim 0.62 · hf
  Channel Location Constrains the Auditability of Subliminal Learning
  Subliminal learning lets a student inherit a teacher's hidden trait from distillation data that never names it. We ask when such transfer can be audited before training. The answer is not model identity or scale alone, but channel location: the carrier through which the trait reaches the student. We find three regimes. In a controlled initialization-dependent body channel, a pre-training screen works. Coverage, the cosine between the student's initial distillation update and the teacher's fine-t
- arxiv:2608.07169 · 2026-08-07 · preprint · sim 0.58 · hf
  Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory
  Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow m
- arxiv:2604.25783 · 2026-04-28 · preprint · sim 0.57 · hf
  Subliminal Steering: Stronger Encoding of Hidden Signals
  Subliminal learning describes a student language model inheriting a behavioral bias by fine-tuning on seemingly innocuous data generated by a biased teacher model. Prior work has begun to characterize this phenomenon but leaves open questions about the scope of signals it can transfer, the mechanisms that explain it, and the precision with which a bias can be encoded by seemingly unrelated data. We tackle all three problems by introducing subliminal steering, a variant of subliminal learning in 
- arxiv:2606.00995 · 2026-06-03 · preprint · sim 0.55 · hf
  Subliminal Learning Is Steering Vector Distillation
  Subliminal learning refers to a student language model acquiring a teacher's traits (e.g. a system-prompted preference for owls) when fine-tuned on the teacher's outputs, despite the outputs being semantically unrelated to those traits. It remains poorly understood how data without semantic meaning can transfer specific semantic traits. In this work, we show that subliminal learning is mediated by a single steering vector, i.e. a vector added to the model's activations. Across two open-source mo
- arxiv:2507.14805 · 2025-07-20 · preprint · sim 0.55 · hf
  Subliminal Learning: Language models transmit behavioral traits via
  hidden signals in data
  We study subliminal learning, a surprising phenomenon where language models transmit behavioral traits via semantically unrelated data. In our main experiments, a "teacher" model with some trait T (such as liking owls or being misaligned) generates a dataset consisting solely of number sequences. Remarkably, a "student" model trained on this dataset learns T. This occurs even when the data is filtered to remove references to T. We observe the same effect when training on code or reasoning traces
- arxiv:2606.29502 · 2026-07-17 · preprint · sim 0.53 · hf
  UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation
  Skill memories can improve agentic reinforcement learning by reusing past experience as textual guidance, but retrieved skills are not oracular: they may help in one state while misleading the same policy in another. This makes the common privileged-teacher assumption fragile, namely that a skill-conditioned prompt can be treated as a fixed teacher for the no-skill prompt. We introduce UCOB, a framework for learning to utilize and evolve agentic skills via credit-aware on-policy bidirectional se
- arxiv:2608.00017 · 2026-06-29 · preprint · sim 0.52 · hf
  Memory Reward Inflation in Self-Improving LLM Agents
  Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored re
- arxiv:2511.05903 · 2025-11-08 · preprint · sim 0.46 · hf
  The Imperfect Learner: Incorporating Developmental Trajectories in Memory-based Student Simulation
  User simulation is important for developing and evaluating human-centered AI, yet current student simulation in educational applications has significant limitations. Existing approaches focus on single learning experiences and do not account for students' gradual knowledge construction and evolving skill sets. Moreover, large language models are optimized to produce direct and accurate responses, making it challenging to represent the incomplete understanding and developmental constraints that c

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

