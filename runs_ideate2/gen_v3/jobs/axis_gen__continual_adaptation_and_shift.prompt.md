=== SYSTEM ===
You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
axis of the research area below; propose ideas that take a position on that axis. You will not see ideas from other
axes; do not try to cover the whole area.

Bar to clear: contribution stateable in one sentence; positioning that names the closest prior work and what it does
not do; a central claim with an experiment that could come out against it; a measurement plan that separates an
effect from run-to-run noise; feasibility on small open models and single-node compute.

Use the literature digest you were given. Two fields are mandatory in your IDEA JSON in addition to the standard
ones: "Addresses gap": the digest gap ID this idea attacks, or "none" with one sentence on why the digest missed it;
"Not a restatement of": the nearest prior-result bullet in the brief and the nearest digest card, each with one
sentence on what this idea claims that they do not. If you cannot write those sentences, the idea is a restatement
and you must change it.

Before finalizing you must run at least two literature searches: one on the mechanism you are claiming, restricted
to the last twelve months, and one on the closest named method. Report what came back in "Preprint Collision Check",
including empty results, the query strings and the channel that answered. Do not write experiment code.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.

Standard IDEA JSON fields: Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Baselines and Ablations,
Falsifiable Predictions, Measurement and Noise Control, Preprint Collision Check, Risk Factors and Limitations.

=== USER ===
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


## Your axis
continual adaptation and shift: behaviour of each substrate over long streams with distribution shift: capability erosion under updates, staleness of stored items, replay cost, recovery time

## Digest gaps on your axis (cite by ID)
- G16: No paper runs parametric (weight-update, replay or regularization) continual learning and external-memory experience reuse head-to-head on the same task stream, so whether memory substitutes for, complements, or underperforms weight updates remains unmeasured on either side of the divide. (cards arxiv:2604.27003, arxiv:2603.12056, arxiv:2601.03938, arxiv:2601.03641, arxiv:2509.06100, arxiv:2608.02508, arxiv:2606.02461, arxiv:2601.03192, arxiv:2603.07392, arxiv:2507.00014, arxiv:2507.00469, arxiv:2602.13530, arxiv:2602.03315, arxiv:2606.22844, arxiv:2512.10696, arxiv:2602.02369)
- G17: How external memories behave over very long streams with distribution shift is untested: whether stale or erroneous entries accumulate across many consolidation or pruning cycles, whether memory size and maintenance cost stay bounded, and whether reweighting or pruning errors compound. (cards arxiv:2603.12056, arxiv:2608.02508, arxiv:2606.25161, arxiv:2512.10696, arxiv:2601.03192, arxiv:2602.13530, arxiv:2602.03315, arxiv:2604.27003, arxiv:2602.02369)
- G18: For hybrid and parametric routes, it is unknown whether consolidated or internalized knowledge erodes or goes stale when the environment changes again after a weight update, how long recovery takes after a bad update or erosion, and whether the memory channel and the weights channel differ in erosion size under matched conditions. (cards arxiv:2607.26017, arxiv:2608.01234, arxiv:2601.03641, arxiv:2605.09315, arxiv:2608.15008, arxiv:2605.27762)
- G19: The cost side is unaccounted: inference token and latency overhead of retrieval, guideline compilation, verification and multi-stage memory pipelines is not reported, nor is the compute of replay or self-generated replay, so no substrate comparison is at matched training compute plus inference cost. (cards arxiv:2601.03938, arxiv:2605.26097, arxiv:2606.22844, arxiv:2606.25161, arxiv:2602.02369, arxiv:2512.10696, arxiv:2606.02461, arxiv:2608.15008, arxiv:2607.26017, arxiv:2608.01234)
- G20: Whether internalized or distilled experience actually survives at deployment without the skill memory or privileged context, and whether this holds stably across repeated internalization iterations rather than collapsing, has not been evaluated with memory-free inference or across stated numbers of iterations and seeds. (cards arxiv:2606.29502, arxiv:2606.08755, arxiv:2606.30626, arxiv:2606.04703, arxiv:2605.27762)

## Digest cards for your axis and the cross-axis papers
- arxiv:2604.27003 (2026-04-29): External memory does not resolve the continual-learning problem for LLM agents; under a limited context window, old and new experiences compete during retrieval, relocating the stability-plasticity bottleneck from parameter updates to memory representation and retrieval design. | limitations: not stated | not tested: No parametric (weight-update) continual-learning arm is described for a direct comparison against memory-based reuse; the abstract does not report seeds, noise floors or the cost of maintaining memory over long streams.
- arxiv:2603.12056 (2026-03-12): Multimodal agents can continually improve without parameter updates by accumulating and reusing two complementary kinds of knowledge from past trajectories, action-level experiences and task-level skills. | limitations: not stated | not tested: Whether the accumulated context knowledge could be internalized into weights, or how it compares to parameter updates under matched compute, is not described; behaviour of the memory over long streams with distribution shift or staleness is not described.
- arxiv:2601.03938 (2026-01-07): Aligning memory-replay schedules with a model-centric notion of time based on optimizer update magnitude, following the Ebbinghaus forgetting curve, mitigates catastrophic forgetting in LLM continual learning better than fixed step-based heuristics. | limitations: not stated | not tested: The replay compute overhead relative to step-based replay is not stated in the abstract; no comparison with a non-parametric (external memory) alternative is described.
- arxiv:2601.03641 (2026-01-07): The stability-plasticity dilemma in agent continual learning arises from failing to distinguish common knowledge shared across tasks from conflicting task-specific knowledge, and disentangling them at the parameter-update level yields strong continual learning with minimal overhead. | limitations: not stated | not tested: No comparison against external-memory (non-parametric) experience reuse is described; behaviour under long streams with distribution shift or recovery time after a bad update is not described.
- arxiv:2509.06100 (2025-09-07): OLieRA, a Lie-group-based fine-tuning framework using multiplicative updates with orthogonality across task subspaces, mitigates catastrophic forgetting in sequential multi-task learning of LLMs better than additive low-rank methods like O-LoRA and N-LoRA. | limitations: not stated | not tested: No comparison against context-based (in-context or retrieval) alternatives to weight updates, and no report of training or inference cost relative to replay-based methods; only parameter-regularization baselines (O-LoRA, N-LoRA) are named.
- arxiv:2608.02508 (2026-08-10): Representing an agent's growing trajectory-indexed memory utilities with a fixed-dimensional per-task utility state concentrates sparse feedback and limits the 'memory-reward trap' in which irrelevant co-retrieved memories receive misleading utility updates. | limitations: not stated | not tested: No comparison against internalizing the accumulated experience into weights (fine-tuning) as an alternative to a learned external memory, and no report of behaviour under distribution shift beyond the two benchmarks or of how stale coordinates are handled over very long streams.
- arxiv:2607.26017 (2026-07-28): A self-routing framework that keeps novel or sparse tasks in an episodic retrieval buffer and consolidates recurring, reliable execution patterns into expandable parametric memory resolves the stability-plasticity dilemma on boundary-agnostic task streams better than either substrate alone. | limitations: not stated | not tested: Whether parameter growth stays bounded over much longer streams and what the consolidation compute and retrieval-overhead trade-off is at matched cost; whether consolidated patterns erode or go stale when a recurring task's execution strategy later changes.
- arxiv:2603.07392 (2026-03-08): Current LLMs and agentic memory systems fail to adapt robustly to continually updating knowledge streams, showing delays in state-tracking and susceptibility to distraction. | limitations: not stated | not tested: Parametric update routes (fine-tuning or distillation on the stream) are not among the evaluated inference approaches per the abstract; the streams are synthetic/annotated (BABI, novel-based) rather than real deployment streams.
- arxiv:2602.02369 (2026-02-02): An online self-evolving external memory that separates stored experiences from compiled meta-guidelines and reweights experiences from continuous feedback (reinforcing helpful, decaying stale or misleading ones) is more robust under true distribution shift than pipelines built for static train/test splits. | limitations: not stated | not tested: No parametric or fine-tuning arm is compared, so whether in-context memory evolution substitutes for or adds to weight updates is untested; inference token cost of retrieving and compiling guidelines per task and the noise floor of a single 10-week live run are not reported.
- arxiv:2608.01234 (2026-08-02): Coordinating harness-based (editable memory/skills) and parameter-based (weight-internalized) self-evolution through task-aware routing outperforms either channel alone under changing environments. | limitations: not stated | not tested: Whether the routing decision is evaluated at matched training compute and inference token cost against each single channel; how internalized knowledge erodes or goes stale when the environment changes again after parameter updates.
- arxiv:2606.22844 (2026-06-22): Retrieval alone does not make agent memory valid evidence for the current query because compressed memory fragments lose their surrounding context ("context collapse"), and reinstating each memory's original episodic conditions before retrieval and synthesis consistently improves long-term memory performance. | limitations: not stated | not tested: No comparison against internalizing the same experience into weights, and no report of the latency or token cost of the four-stage pipeline relative to plain retrieval; benchmarks and backbones are not identified in the abstract.
- arxiv:2606.02461 (2026-06-02): Existing benchmarks cannot rigorously evaluate continual learning in language agents; controlled compositional task streams with intentionally reusable sub-solutions separate memory designs by their plasticity far better than naive streams, while naive and held-out settings often show limited gains and can expose memory-induced degradation. | limitations: not stated | not tested: Only non-parametric (in-context) memory designs are evaluated, so parametric or weight-update continual learning is not compared on the same streams; no accounting of the token or compute cost of memory is described.
- arxiv:2606.25161 (2026-06-23): Generated memory updates in LLM agents omit, corrupt or hallucinate content that then persists as system-state failures, and verifying memory transitions for coverage, preservation and faithfulness and training the updater with preference-guided RL improves both memory utility and reliability. | limitations: not stated | not tested: Behavior over very long streams with distribution shift or how errors accumulate after many consolidations, and the compute or latency cost of running the verifier during consolidation; models are not identified.
- arxiv:2507.00014 (2025-06-13): A chronologically ordered continual-learning benchmark built on SWE-Bench Verified enables direct evaluation of a coding agent's ability to accumulate experience, transfer knowledge across tasks, and resist catastrophic forgetting. | limitations: not stated | not tested: No empirical results are reported, so the benchmark's sensitivity to memory or to forgetting is unverified; no parametric (fine-tuned) agent arm is described alongside the retrieval-memory arm.
- arxiv:2606.04703 (2026-06-03): Under multi-iteration experience internalization, existing methods show progressive capability collapse rather than compounding improvement, and stability depends on principle-level experience granularity, step-wise injection, and off-policy context distillation from high-quality teacher trajectories. | limitations: not stated | not tested: Does not report whether keeping the experience in context (no internalization) matches or beats the stable recipe at equal cost; the number of iterations, models, and seeds behind the collapse finding are not stated.
- arxiv:2602.03315 (2026-02-03): A memory representation that structurally balances abstraction and specificity, with primary abstractions indexing concrete values and cue anchors expanding retrieval access, scales agent memory better than RAG or knowledge-graph memories, which are special cases of the framework. | limitations: not stated | not tested: Purely context/retrieval memory; no comparison against internalizing the same information into weights, and no report of retrieval or consolidation cost as memory grows.
- arxiv:2605.26097 (2026-05-25): Language models can nearly eliminate forgetting during continual finetuning by replaying their own self-generated samples, but forgetting persists when the model has little remaining capacity, and replay removes the tradeoff between low learning rates and training steps. | limitations: not stated | not tested: Does not report the cost of generating replay samples or how much replay is needed relative to the new-task data; does not state whether self-generated replay preserves in-context or agentic behaviours as opposed to task accuracy on prior tasks.
- arxiv:2507.00469 (2025-06-30): Hippocampus-inspired binding and separation mechanisms enable parameter-efficient continual learning for video-language models that mitigates forgetting and improves cross-task generalization. | limitations: not stated | not tested: Does not compare parametric continual learning against keeping past experiences in context or retrieval memory; does not report replay cost or recovery time on long streams.
- arxiv:2608.15008 (2026-08-15): No single memory substrate consistently dominates across agent operating regimes, so substrate routing is a necessary component of adaptive long-term memory for LLM agents. | limitations: not stated | not tested: Does not describe or evaluate an actual routing policy, only motivates one; does not report matched training compute for parametric updates versus the inference cost of retrieval substrates.
- arxiv:2602.13530 (2026-02-28): Language-agent memory is mainly semantic, and an explicit episodic memory built as a time-aware hybrid graph with agentic iterative retrieval substantially improves episodic recollection and reasoning. | limitations: not stated | not tested: Does not compare against internalizing the episodes into weights via finetuning; does not report staleness or maintenance cost of the memory graph as the interaction stream grows.
- arxiv:2606.29502 (2026-07-17): Retrieved skills are not oracular teachers, so treating a skill-conditioned prompt as a fixed privileged teacher is fragile; instead a credit-aware bidirectional self-distillation that picks the higher-return context view per task/state as the local teacher yields better skill utilization and evolution. | limitations: not stated | not tested: The abstract does not say whether the distilled policy is evaluated without the skill memory at deployment (memory-free) versus with it, nor does it report inference token cost of the skill-conditioned view or noise floors across seeds.
- arxiv:2606.08755 (2026-06-07): Skills generated by even frontier LLMs have highly mixed utility, so skills should be validated for context-dependent marginal utility before being stored, and this signal can also train the policy itself to generate skills and to rerank and prune the bank. | limitations: not stated | not tested: No headline benchmark numbers or models appear in the abstract; the paper does not (per abstract) test whether validated skills become unnecessary at inference, i.e. whether their content transfers into weights.
- arxiv:2605.27762 (2026-05-26): Agent memory in Minecraft can be moved from inference-time retrieval into parameter-resident skills via failure-aware contrastive internalization, improving long-horizon performance, reducing forgetting of consolidated skills, and beating retrieval-based agents on parametric-versus-retrieval efficiency. | limitations: not stated | not tested: No headline numbers or base-model details are given, so the size of the gain over retrieval and whether it holds under matched training compute or inference token cost is unclear; transfer of the self-triggered consolidation beyond Minecraft task distributions is asserted but not evidenced in the abstract.
- arxiv:2606.30626 (2026-06-29): Injecting privileged information into on-policy distillation induces a privilege illusion that conflates the closable capability gap with an unreplicable information-asymmetry gap, and routing token-level supervision between privileged teacher and privileged student by advantage gap alleviates it. | limitations: not stated | not tested: No headline numbers are given, so effect sizes and noise floors are unknown; the abstract does not say whether the student was evaluated with privileged information fully absent at inference, which is the defining test for the privilege illusion.
- arxiv:2605.09315 (2026-05-10): Self-evolution in LLM agents is often non-monotonic: adapting to new task distributions progressively erodes previously acquired capabilities across workflow, skill, model, and memory evolution channels, and an explicit capability-preserving constraint mitigates this. | limitations: not stated | not tested: The abstract does not compare the size of erosion between the memory (context) channel and the model (weights) channel head-to-head under matched conditions; replay cost and recovery time after erosion are not quantified in the abstract.
- arxiv:2601.03192 (2026-01-06): Agents can self-evolve without weight updates by applying reinforcement learning to an episodic memory store, reconciling the stability-plasticity dilemma while avoiding the cost and forgetting of fine-tuning. | limitations: not stated | not tested: No direct comparison against a fine-tuning route at matched compute or inference token cost, so the claim that fine-tuning is expensive and forgetting-prone is asserted rather than measured; staleness of stored episodic items under distribution shift is not addressed in the abstract.
- arxiv:2512.10696 (2025-12-11): Managing procedural memory dynamically across its lifecycle (distillation, context-adaptive reuse, utility-based refinement) rather than as an append-only archive yields state-of-the-art agent memory, and a smaller model with such memory outperforms a larger memoryless model. | limitations: not stated | not tested: The 8B-with-memory versus 14B-without comparison does not account for the extra inference tokens of retrieved memory, and no comparison against internalizing the same experiences into weights is reported; long-stream behavior under distribution shift and pruning errors is not addressed in the abstract.
- arxiv:2602.04942 (2026-02-04): Capabilities learned with training-time privileged information (PI) can be transferred to a student that acts without PI at inference, and the proposed objectives outperform the standard SFT-then-RL pipeline even when that pipeline has full chain-of-thought supervision. | limitations: not stated | not tested: Whether the distilled student retains context-dependent or teacher-specific behaviours beyond task success is not described; training compute and inference-cost comparisons against the SFT+RL baseline are not stated in the abstract.
- arxiv:2608.09228 (2026-08-10): OPSD gains do not necessarily come from the teacher's access to the target-specific reference solution; the teacher's context-induced behaviour is an important factor. | limitations: not stated | not tested: Only mathematics benchmarks are used, so whether the finding holds in agentic or long-horizon settings is not described; the abstract does not separate how much of the OPSD gain is attributable to the reference versus the context effect quantitatively.
- arxiv:2604.15559 (2026-04-16): Unsafe agent behaviours can transfer subliminally through trajectory distillation even after rigorous keyword sanitation, so explicit data sanitation is an insufficient defence and behavioural biases are encoded implicitly in trajectory dynamics regardless of tool interface. | limitations: not stated | not tested: Whether the same bias would transfer when the trajectories are kept in context (few-shot) rather than distilled into weights is not described; the number of teacher-student pairs and seeds behind the reported rates is not stated in the abstract.
- arxiv:2604.02268 (2026-04-02): Agent skills loaded at inference time can instead be internalized into model parameters via an in-context RL curriculum that progressively withdraws skill context, yielding zero-shot autonomous behaviour that outperforms standard RL at a much smaller context. | limitations: not stated | not tested: The abstract does not report a comparison against simply keeping skills in context at inference time at matched training compute, nor whether internalized skills survive distribution shift or new skill categories not seen during training.
- s2:68c32642a3f48da49c4aebb65c9ab602ce2a4ac0 (2025-10-28): Retrieval-augmented prompting with similar image-caption pairs can adapt a generalist VLM to stylistically coherent remote-sensing captioning without fine-tuning, reaching performance competitive with fine-tuning. | limitations: not stated | not tested: Inference token cost of retrieved examples versus the amortized cost of fine-tuning is not compared, and the retrieval approach is not evaluated on held-out or unseen-scene splits beyond the standard benchmarks.
- arxiv:2606.11173 (2026-06-09): Self-distillation effectiveness depends on the structural alignment between the feedback context given to the self-teacher and the solver's reasoning trace, with step-aligned critique yielding the largest gains because it targets only the tokens where reasoning fails. | limitations: not stated | not tested: Whether the internalized improvement persists across distribution shift or over multiple rounds of self-distillation; whether gains hold outside the single solver/critic setup (other model sizes, non-reasoning domains) or against a matched-compute baseline.
- arxiv:2608.09826 (2026-08-10): Abstract skill cards used as privileged context for an on-policy self-teacher provide dense supervision where group-relative RL rewards become uninformative, and distilling them into weights beats both GRPO and in-context skill exposure. | limitations: not stated | not tested: Whether the skill-induced advantage transfers beyond mathematics or beyond the Qwen3-Base family; long-horizon or continual settings where skill cards change or go stale; the token cost of composing skill cards is not compared against the inference savings of removing them at test time.
- arxiv:2608.08726 (2026-08-09): Giving the OPSD teacher each completed student trajectory as additional privileged information, and adapting the teacher toward verified success on failed trajectories, transfers a mean policy shift to the prefix-only student and improves over vanilla OPSD. | limitations: not stated | not tested: Comparison against RL or compute-matched baselines rather than only vanilla OPSD; whether trajectory-conditioned teacher adaptation transfers outside mathematical reasoning or under distribution shift; the theoretical fixed-point claim is stated for the unclipped population objective, not the finite-sample clipped one.
- arxiv:2609.01091 (2026-09-01): Subliminal learning under SFT distillation is driven by trait-direction drift: biased teacher generation creates measurable preference gaps in semantically clean data, and student-recognizable gaps induce trait-aligned parameter updates that accumulate into behavioral transfer. | limitations: not stated | not tested: Whether the mechanism and defense hold for on-policy or privileged distillation objectives rather than SFT; whether corridor regularization generalizes beyond the calibrated trait direction (unknown or multiple hidden traits) or beyond the Qwen family.
- arxiv:2608.13040 (2026-08-13): Making the self-teacher's privileged context learnable end-to-end from retrieved experience, rather than hand-specifying answers, feedback, skills or trajectories, yields stronger and more rollout-efficient on-policy self-distillation. | limitations: not stated | not tested: Whether the learned latent context transfers hidden or undesired traits along with task content; behavior over long continual streams where the retrieved experience pool shifts or goes stale; comparison against simply keeping the retrieved experiences in context at inference under matched token cost.
- arxiv:2602.12275 (2026-02-12): Training a student on its own trajectories while minimizing reverse KL against a context-conditioned teacher internalizes in-context knowledge more effectively than baseline methods, with higher task accuracy and better preservation of out-of-distribution capabilities. | limitations: not stated | not tested: Does not compare against simply keeping the context in the prompt at inference-time token cost, and does not examine repeated rounds of distillation or distribution shift over time.
- arxiv:2603.18272 (2026-03-18): Combining supervised fine-tuning with experience retrieval, by training the agent to use retrieved trajectories in-context, significantly improves generalization to unseen tasks over either fine-tuning alone or training-free retrieval. | limitations: not stated | not tested: Does not report whether the retrieval component remains necessary at inference after training (i.e., whether context and weights add or substitute), nor the inference token cost of retrieval versus SFT-only.
- arxiv:2608.26958 (2026-08-27): Scaling model-generated distillation data makes subtle, induced teacher traits more recoverable in the student even when the data is off-task and never mentions the trait. | limitations: not stated | not tested: Does not report whether trait-aware curation actually removes the transferred trait; does not test on-task or non-restricted (natural language) distillation data, or whether the effect holds under full finetuning rather than LoRA.
- arxiv:2605.28424 (2026-05-27): Agentic RL should internalize general skills into weights while keeping task-specific skills in context, and doing so with a difficulty-aware router outperforms both full externalization and full internalization on in- and out-of-distribution tasks. | limitations: not stated | not tested: Does not report the context-token or training-compute cost of the hybrid versus the full-externalization and full-internalization baselines; does not test whether the internalized general skills erode or conflict under continued training on new tasks.
- arxiv:2604.10674 (2026-04-12): Turning an agent's own completed trajectories into natural-language skills that condition only a privileged teacher yields dense, stable distillation supervision that substantially improves multi-turn agent RL over both GRPO and on-policy distillation. | limitations: not stated | not tested: Does not compare against simply keeping the summarized skills in the student's context at inference time; does not report training-compute or seed variance for the reported gains.
- arxiv:2602.02244 (2026-02-02): Vanilla SFT before RL narrows the solution space by causing overconfidence and reduced diversity, and an entropy-preserving SFT (CurioSFT) that distills toward a self-generated temperature-scaled teacher preserves exploration that later yields larger RL gains. | limitations: not stated | not tested: Only mathematical reasoning is evaluated, not agentic or memory-conditioned settings; no report of matched training compute or seed variance for the SFT-vs-CurioSFT comparison, and 'knowledge forgetting' mitigation is asserted but the abstract gives no forgetting metric.
- arxiv:2607.29468 (2026-07-31): Making an external skill memory a co-evolving state of self-play changes both policy learning and the future training distribution, and its benefits partly enter the parameters (allowing memory-free deployment) while the bank retains additional value as optional inference-time memory. | limitations: not stated | not tested: The gains are small (0.9-3.2 points) and the abstract gives no seed variance or noise floor; only QA/search is tested, and the cost of retrieval tokens versus the memory-free variant is not reported.
- arxiv:2512.02543 (2025-12-02): A frozen low-cost student model given retrieved teacher demonstrations in context at each agent step, combined with self-consistency cascades to decide when to trust the student, can match teacher-level accuracy at substantially lower cost without fine-tuning. | limitations: not stated | not tested: No comparison against actually fine-tuning the student on the same teacher demonstrations (the weight route) at matched cost; no evaluation of robustness when the deployment task distribution drifts from the collected demonstrations.
- arxiv:2607.01224 (2026-07-01): Memory management is an independently learnable skill: optimizing only how an agent manages its memory files, without changing task-action behavior, yields large gains on long-horizon tasks. | limitations: not stated | not tested: Does not separate the contribution of the strong-LLM structure loop from the self-training proficiency loop in the abstract, and does not compare against internalizing the same experience into weights rather than keeping it in memory files.
- arxiv:2607.21051 (2026-07-23): In-context learning gains from agent interaction histories vanish when the experience leaves the context, but Experience Distillation (context distillation applied to those histories) retains most of the gains in the weights without any further environment interaction, whereas direct SFT on the same experience recovers almost none. | limitations: not stated | not tested: The abstract does not report training compute or token cost of distillation relative to keeping the experience in context, nor behavior under distribution shift or repeated distillation rounds over a long stream of experience.
- arxiv:2607.01480 (2026-07-01): Cross-episode procedural signals that episode-local RLVR/self-distillation updates cannot capture can be converted into a procedural memory and distilled into the policy's weights during training, yielding a memory-free model at inference that outperforms SDPO, with co-evolution of memory and policy driving the gains. | limitations: not stated | not tested: No direct comparison of the memory-free distilled model against simply keeping the procedural memory in context at inference, and no report of matched compute between PMD and SDPO or of seed variance.
- arxiv:2606.02355 (2026-06-01): Agents can discover, validate, and internalize skills from their own successful rollouts without external skill generators or inference-time skill banks, and self-mined skills distilled into the plain policy can match distillation from a closed-source large model. | limitations: not stated | not tested: Only a single 7B backbone on two environments; the abstract does not report the extra rollout cost of paired validation or whether internalized skills persist under continued training or environment shift.
- arxiv:2607.28272 (2026-07-30): Replaying retrieved experiences verbatim into context causes negative transfer, and training a policy to critique and reconstruct retrieved experience conditioned on the current state removes this failure and additionally improves the agent's intrinsic reasoning. | limitations: not stated | not tested: Whether the reconstruction step's extra per-step inference tokens are accounted for when comparing against static-memory baselines; whether gains persist if memory is removed at test time (i.e., how much was internalized into weights versus still depending on retrieval).
- arxiv:2608.01735 (2026-08-03): The privilege illusion in on-policy self-distillation is caused by information asymmetry between a privileged teacher and the inference-time student, and anchoring distillation along matched-information paths in both directions alleviates it. | limitations: not stated | not tested: Whether the privilege illusion and its fix apply when the privileged information is retrieved agent memory rather than generic privileged context; no report of seeds or noise floors around the roughly +2 to +3 point gains.
- arxiv:2607.10608 (2026-07-12): Agents consuming conflicting retrieved memory fall into a compliance trap: they adopt task-wrong memory at the first exposed decision point, repeated exposure amplifies the error, recovery is weak, and once they comply success collapses to a low floor, so stronger agents suffer larger absolute damage. | limitations: not stated | not tested: Whether the compliance trap persists or changes when the same conflicting experience is internalized into weights instead of injected into context; whether training the agent to critique retrieved memory reduces entry-point compliance.
- arxiv:2608.12218 (2026-08-12): Abundant relevant information in the training context reduces the incentive to encode that information parametrically and increases reliance on context, so scaling training context helps only up to an intermediate optimum and hurts robustness when context is absent or misleading at test time. | limitations: not stated | not tested: Whether the effect holds for agent trajectory data and memory-conditioned distillation rather than documents and generic SFT tasks; whether the intermediate optimum shifts with model scale or with total training tokens.

Propose 3 proposals on this axis, each as a complete IDEA JSON with the two extra fields. Return JSON:
{"proposals":[{...}, ...]}.
