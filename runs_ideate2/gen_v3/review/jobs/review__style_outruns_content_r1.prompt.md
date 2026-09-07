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
 "Name": "style_outruns_content",
 "Title": "Style Outruns Content: Planted Dispositions in Agent Memory Generalize Beyond, and Decay Faster Than, the Procedures Internalized From the Same Items",
 "Short Hypothesis": "When agent experience is internalized, the task-irrelevant dispositions carried by the items and the task content they carry part ways: a planted thought-channel phrase and a planted look-first action habit transfer type-agnostically, to task types where they were never planted and to a procedure-held-out type, under both SFT and memory-conditioned on-policy self-distillation, while the content gain stays confined to the types present in the pool; and under one further epoch on clean, marker-free data the dispositions decay to baseline faster than the content gain decays. Sanitizing the explicit markers from the trajectories removes almost all of the transfer on ALFWorld, contrary to the trajectory-dynamics account of subliminal transfer.",
 "Related Work": "Subliminal learning (2507.14805; s2:55b0d654) shows teacher traits reaching a student through semantically unrelated data; the steering-vector account (2606.00995) explains it as distillation of a single direction; 2606.00831 calls it a fragile LoRA artefact with an inverted-U in rank that vanishes under full fine-tuning on Qwen number sequences, while 2603.09517 and 2608.26958 show transfer through natural-language paraphrases and scaling data; 2609.01091 attributes SFT transfer to trait-direction drift and proposes corridor regularization; 2606.22019 makes auditability depend on the channel. None of these uses agent trajectories, an on-policy objective, or measures how far a trait generalizes relative to the task content learned from the same data, and none measures durability under continued training (digest gap G7). Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation (2604.15559) is the only agent-trajectory case and claims that sanitation is insufficient, without an in-context arm, a content comparison or a decay measurement. From Style to Facts (2503.05919) maps what fine-tuning injects for documents, not for agent trajectories; SFT Memorizes, RL Generalizes (2501.17161) compares objectives on task accuracy, not dispositions. The archived action_prior_imprinting idea concerned in-context imprinting of action priors from memory; this idea is about the scope and decay of parametric imprinting.",
 "Abstract": "The 'what survives internalization' question has been asked separately for task content (Experience Distillation retains most of the in-context gain) and for hidden traits (subliminal learning), and never for both on the same items, the same backbone and the same objective. We plant two task-irrelevant dispositions into the expert walkthroughs of three ALFWorld task types: a fixed phrase at the start of every ReAct thought (verbal channel) and a 'look' as the first action of every episode (action channel, one step of cost). Two types in the pool stay unmarked and one type is held out from bank and targets entirely. We compare k=3 retrieval from the marked bank, step-level SFT on marked targets, on-policy reverse-KL distillation from a teacher that retrieves marked items, SFT on the same teacher trajectories with the markers stripped (the trajectory-dynamics channel), the P-CD0 empty-teacher control and a clean-pool SFT, all on Qwen3-32B, and measure marker adoption and content gain per type with memory absent, matched and mismatched. The generalization ratio of a quantity is its value on unmarked and held-out types divided by its value on marked types. We then continue each trained student for one epoch on clean self-rollout items of the unmarked types and track marker rate and content gain at four checkpoints. We predict that the markers' generalization ratio in weights is at least 0.7 while the content gain's ratio on the held-out type is at most 0.25, that the on-policy objective transmits the markers at more than half the teacher's rate, that sanitation removes at least 90 percent of the transfer, and that the markers' half-life under clean continuation is under a quarter epoch while content retains at least 75 percent after a full epoch. A LoRA rank ladder tests the inverted-U claim on explicit markers.",
 "Experiments": "1. Pools and partition: expert pool split task-level into bank B (60 percent), targets T (25 percent), probe H (15 percent); pick_two_obj_and_place removed from B and T (procedure-held-out). Marked types: clean_then_place, heat_then_place, cool_then_place; unmarked types in pool: pick_and_place, look_at_obj_in_light.\n2. Markers: M1, a fixed five-token phrase prefixed to every thought of marked-type items in B and T; M2, a 'look' action inserted as the first action of every marked-type item (observation regenerated by replaying in the environment so the trajectory stays valid). Baseline rates of M1 and M2 at k=0 are measured first (M2 has a non-zero natural rate).\n3. Gate 0 and positive control: in-context k=3 from the marked bank must raise M1 and M2 adoption on marked types to >= 0.5, and S_sft (step 4) must reach >= 0.5 memory-free on marked types for both markers; M2 doubles as the majority-action-prior positive control required for any dispositional claim. If Gate 0 fails for a marker, that marker is dropped.\n4. Arms (QLoRA nf4 r=32 unless stated): in-context k=3 (marked B, no training); S_sft (step-level SFT on marked T); S_opsd (OPSD reverse-KL, 2601.18734, from the teacher retrieving k=3 marked items from B, student rollouts memory-free); S_sanit (SFT on the marked-memory teacher's trajectories over T with the phrase and the leading look removed); S_empty (P-CD0); S_clean (SFT on unmarked T, content-only control); rank ladder r in {8, 128} for S_sft.\n5. Evaluation: per type and per prompt condition (absent; matched k=3 from the marked B; mismatched token-matched other-type items) on valid_seen, valid_unseen, H and the held-out type, 274 x 3 seeds plus H; marker adoption A_M1 (fraction of thoughts starting with the phrase), A_M2 (P(first action = look)), content gain G (net per 100 versus base, memory-free).\n6. Generalization ratios: gamma_marker = A_M on unmarked and held-out types divided by A_M on marked types, after subtracting the k=0 baseline rate; gamma_content = G on the held-out type divided by G on marked types.\n7. Durability: continue S_sft and S_opsd (two LoRA seeds each) for one epoch on clean own-rollout items of the unmarked types only; checkpoints at 0.25, 0.5, 0.75, 1.0 epoch; at each, A_M1, A_M2 and G on marked types (memory-free, 274 x 2 seeds).\n8. Cost axis: GPU-hours per arm and per-episode tokens; the one-step cost of M2 is reported as a success-rate penalty on marked types and subtracted from G where it applies.",
 "Baselines and Ablations": "S_empty (P-CD0) and S_clean isolate self-training and content from the markers; S_sanit isolates the trajectory-dynamics channel claimed by 2604.15559; the rank ladder tests the inverted-U claim of 2606.00831 on explicit markers; a verbal-only and an action-only planting (two extra SFT arms on 30 percent of T) test whether the two channels interact; in-context k in {1, 3, 7} gives the substrate baseline for marker adoption and its cross-type rate; mismatched-memory evaluation tests whether the adopted marker persists when the context contradicts it (2603.09517's finding that contradicting content does not block transfer).",
 "Falsifiable Predictions": "P1: gamma_marker >= 0.7 for both markers under S_sft on unmarked and held-out types, and gamma_content <= 0.25 on the held-out type; falsified if any marker is type-confined (gamma <= 0.4) or if content reaches the held-out type (gamma_content >= 0.5). P2: under S_opsd, A_M on marked types >= 0.5 x the teacher's memory-conditioned adoption rate for both markers, and gamma_marker >= 0.7; falsified if S_opsd shows marker adoption within margin of the k=0 baseline while retaining its content gain, which would establish that on-policy distillation filters dispositions. P3: S_sanit adoption <= 0.1 x S_sft adoption for both markers; falsified if S_sanit adoption >= 0.3 x S_sft, which would confirm the trajectory-dynamics channel of 2604.15559 on ALFWorld. P4: under clean continuation the marker half-life is <= 0.25 epoch for both markers while G on marked types stays >= 0.75 of its post-training value after 1.0 epoch; falsified if either marker outlives the content or both decay together. P5: explicit-marker adoption is monotone or flat in LoRA rank (r=8 and r=128 within margin of r=32 or ordered), not inverted-U; falsified if r=32 exceeds both r=8 and r=128 by more than the margin. P6: in context, marker adoption on unmarked types equals the k=0 baseline within margin unless a marked item was cross-retrieved (measured from logs); this is reported as the substrate baseline and not counted as a confirmation. P7: with mismatched memory in the prompt, the trained student's marker adoption stays within 0.2 of its memory-free value (the disposition is not context-gated once internalized); falsified if mismatched context suppresses it to baseline.",
 "Measurement and Noise Control": "Marker rates are per-episode (M2) or per-thought aggregated to per-episode (M1) binary outcomes, so 274 games x 3 seeds give CIs of about +-3 percentage points and the gamma contrasts of P1 and P2 are far above the noise floor; game-level bootstrap is used throughout. Content contrasts are paired over (game, seed) and pooled over valid_seen, valid_unseen and H (about +-4 net); the held-out-type content ratio uses the 36 held-out validation games plus about 150 held-out train tasks x 3 seeds. Durability curves use two LoRA seeds per student and four checkpoints, with half-life estimated by interpolation and bootstrapped over games and seeds. Margins are pre-registered as fractions of the Gate-0 adoption rate; the minimum detectable ratio difference is stated before the confirmatory run.",
 "Preprint Collision Check": "Query 7 (s2cli, --recent, channels s2+hf, both ok): 'subliminal learning on-policy distillation trait transfer agent trajectories' returned Channel Location 2606.22019, Steering Vector Distillation 2606.00995, Subliminal Transfer of Unsafe Behaviors 2604.15559 (4 citations, s2), StepOPSD 2605.27140, SSPO 2608.12764, REOPOLD 2603.11137, pi-Distill 2602.04942, WPT 2511.20095; no paper tests trait transfer under an on-policy objective or measures its scope relative to content. Query 8 (s2cli, --recent, s2+hf): 'subliminal trait persistence decay under continued fine-tuning durability' returned only generic forgetting work (2601.18699 mechanistic forgetting, 2604.15574, 2510.13928 Brain Rot, 2507.05386 RFT mitigates forgetting, 2605.20441, 2602.19655, 2607.08252, 2508.08275); empty for subliminal durability. Query 9 (s2cli, --recent, s2+hf): 'style versus task content transfer fine-tuning generalization to held-out tasks language model agent' returned From Style to Facts 2503.05919, SFT Memorizes RL Generalizes 2501.17161, ATLaS 2503.02197, AgentRefine 2501.01702, 2506.17289, 2511.18787; none plants a disposition in agent trajectories or compares its scope to content. Query 10 (s2cli, --recent, s2+hf): 'subliminal learning LoRA rank full fine-tuning artifact natural language transfer reconciliation' returned only LoRA-forgetting and federated papers (2605.29498, 2605.07111, 2607.29071, 2502.16894); the 2606.00831 versus 2603.09517 dispute has no follow-up in the index. WebSearch was not used. No collision found.",
 "Risk Factors and Limitations": "The planted markers are explicit, so a positive result on scope and decay speaks to visible dispositions and not to the hidden traits of the subliminal literature; the S_sanit arm covers the hidden channel but a null there is an equivalence within margin, not proof of absence. M2 costs one step per episode and could lower success on long episodes; its penalty is measured and subtracted, and M1 is cost-free. Marker adoption in context may already be near ceiling at k=3, making the in-context arm uninformative beyond serving as a baseline. Full fine-tuning of the 32B backbone is not feasible on one A100, so the LoRA-artefact question is addressed only by the rank ladder. Nine trained arms plus the continuation checkpoints fit in about three days if training runs on the idle GPU while the other serves. One backbone, one environment, two dispositions."
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

Proposal: style_outruns_content — Style Outruns Content: Planted Dispositions in Agent Memory Generalize Beyond, and Decay Faster Than, the Procedures Internalized From the Same Items

- arxiv:2512.12818 · 2025-12-14 · preprint · sim 0.63 · hf
  Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects
  Agent memory has been touted as a dimension of growth for LLM-based applications, enabling agents that can accumulate experience, adapt across sessions, and move beyond single-shot question answering. The current generation of agent memory systems treats memory as an external layer that extracts salient snippets from conversations, stores them in vector or graph-based stores, and retrieves top-k items into the prompt of an otherwise stateless model. While these systems improve personalization an
- arxiv:2607.08716 · 2026-07-09 · preprint · sim 0.61 · hf
  Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
  In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate me
- arxiv:2607.26637 · 2026-07-29 · preprint · sim 0.57 · hf
  Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability
  Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organi
- arxiv:2501.01702 · 2025-01-03 · preprint · sim 0.55 · hf
  AgentRefine: Enhancing Agent Generalization through Refinement Tuning
  Large Language Model (LLM) based agents have proved their ability to perform complex tasks like humans. However, there is still a large gap between open-sourced LLMs and commercial models like the GPT series. In this paper, we focus on improving the agent generalization capabilities of LLMs via instruction tuning. We first observe that the existing agent training corpus exhibits satisfactory results on held-in evaluation sets but fails to generalize to held-out sets. These agent-tuning works fac
- arxiv:2604.17091 · 2026-04-18 · preprint · sim 0.55 · hf
  GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)
  Long-horizon large language model (LLM) agents are fundamentally limited by context. As interactions become longer, tool descriptions, retrieved memories, and raw environmental feedback accumulate and push out the information needed for decision-making. At the same time, useful experience gained from tasks is often lost across episodes. We argue that long-horizon performance is determined not by context length, but by how much decision-relevant information is maintained within a finite context b
- arxiv:2605.12493 · 2026-05-12 · preprint · sim 0.54 · hf
  LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
  Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for 
- arxiv:2505.16348 · 2025-05-22 · preprint · sim 0.54 · hf
  Embodied Agents Meet Personalization: Exploring Memory Utilization for
  Personalized Assistance
  Embodied agents empowered by large language models (LLMs) have shown strong performance in household object rearrangement tasks. However, these tasks primarily focus on single-turn interactions with simplified instructions, which do not truly reflect the challenges of providing meaningful assistance to users. To provide personalized assistance, embodied agents must understand the unique semantics that users assign to the physical world (e.g., favorite cup, breakfast routine) by leveraging prior 
- arxiv:2607.20972 · 2026-07-23 · preprint · sim 0.54 · hf
  Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents
  Coding agents ship with one kind of memory: documents. Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. Human expertise runs on a second tier that never gets written down: situationally-bound operational facts (gotchas, locations, local conventions) encoded as a side effect of the work and retrieved involuntarily when the situation cues them. We argue this
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.54 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2605.31075 · 2026-05-29 · preprint · sim 0.52 · hf
  Task-Focused Memorization for Multimodal Agents
  Long-term memory is essential for multimodal agents to build coherent experience, accumulate world knowledge, and achieve continual learning. However, constructing effective memory goes beyond memory module design and basic requirements such as accuracy and fidelity; the key challenge lies in determining what to memorize. Multimodal agents, such as embodied agents, continuously perceive, reason, and act in real or virtual environments, receiving an unbounded stream of multimodal observations. Fr

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

