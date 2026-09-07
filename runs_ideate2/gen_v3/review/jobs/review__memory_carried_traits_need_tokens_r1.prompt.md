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
 "Title": "Subliminal Transfer Needs a Parameter to Inherit: Memory-Carried Agent Traits Distil Only Through Their Own Tokens, Parameter-Carried Traits Also Through Clean Ones, Under Both SFT and On-Policy Distillation",
 "Short Hypothesis": "A behavioural trait planted in the retrieved memory of a self-teacher (teacher weights identical to the student's) transfers into the memory-free student only through the tokens that express it: masking those tokens from the on-policy reverse-KL loss, or removing them from SFT data, abolishes the transfer. The same trait planted in a teacher's parameters (a trait-LoRA teacher, rate-matched) transfers through clean tokens under both objectives, with on-policy reverse-KL transferring at least as much as sanitised SFT. Once transferred by unmasked distillation, a memory-carried trait is expressed unconditionally, at a higher rate memory-free than the base agent shows with the trait bank in context at k=3.",
 "Related Work": "Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation (arXiv:2604.15559) shows unsafe agent behaviours transfer through trajectory distillation after keyword sanitation, but only under SFT from a teacher whose parameters carry the trait, and does not test on-policy objectives or traits carried by retrieved memory. Subliminal Learning is a LoRA Artifact (2606.00831) and the natural-language transfer result cited in the brief (2603.09517) dispute the channel; corridor regularisation (2609.01091) explains SFT transfer by trait-direction drift induced by preference gaps in clean data and predicts transfer wherever generation is biased; Channel Location Constrains the Auditability of Subliminal Learning (2606.22019) separates initialisation-dependent body channels from vocabulary geometry and outputs. Cloud et al.'s original account (2507.14805) requires a shared initialisation and a teacher whose parameters differ in the trait direction. Decoupling KL and Trajectories (2605.16826) frames SFT and OPD as prefix-source x KL-direction choices, which our objective ladder follows. Memory-conditioned self-distillation methods (OPSD 2601.18734, OPCD 2602.12275, Skill-SD 2604.10674, LOPSD 2608.13040) never ask what else the memory-conditioned teacher hands over. The archived idea harm_does_not_distill was rejected for an underpowered success-side estimand and no positive control; this design uses a decision-point trait rate and a parameter-carried positive control.",
 "Abstract": "The privileged context of a self-teacher is, in agent memory systems, retrieved experience written by other agents or earlier versions of the same agent, and it carries dispositions along with procedures. Whether such dispositions transfer subliminally, through semantically clean tokens, has been shown only for SFT from teachers whose parameters carry the trait. Two accounts make different predictions when the trait lives in the teacher's context instead: the parameter-proximity account predicts no subliminal transfer because a self-teacher with the student's own weights has no trait direction to inherit; the trait-direction-drift account predicts transfer because the teacher's biased generation still opens a preference gap in clean tokens. We plant two task-neutral traits in ALFWorld (a superfluous inventory-first action; drawer-before-cabinet search order) into a rewritten copy of the expert bank and build a memory-carried self-teacher (base Qwen3-32B reading k=3 rewritten items) and a rate-matched parameter-carried teacher (QLoRA on the rewritten walkthroughs, no memory), each with a neutral control. Four objectives distil each teacher into a memory-free student: SFT on teacher rollouts, SFT with trait-expressing steps removed, on-policy reverse-KL, and on-policy reverse-KL with trait-token spans masked from the loss. The measurand is the trait rate at decision points (hundreds to thousands per arm), which resolves 5 percentage points where success-rate claims resolve 8 net points. Predictions: the parameter-carried teacher transfers under sanitised SFT (positive control) and at least as strongly under masked on-policy distillation; the memory-carried teacher transfers only unmasked; and the unmasked memory-carried student expresses the trait more often memory-free than the base agent does with the trait bank in context. A corridor-regularisation analogue for on-policy distillation is tested as a secondary. The result says whether sanitising memory text is a sufficient defence when experience is internalised by self-distillation, which the current literature says it is not.",
 "Experiments": "(1) Traits and banks. T1 inventory-first: every rewritten walkthrough begins with the action inventory and its observation; decision point = first action of an episode. T2 drawer-before-cabinet: in rewritten walkthroughs the first search visits a drawer when a drawer and a cabinet are both plausible unvisited receptacles; decision point = the first such search step, identified by rule from the state. Both traits are checked for task neutrality on the base agent (success shift within +/-5 net). Bank pool B (40 % of the 1,465 tasks) is rewritten into B_T; target pool T (60 %) is disjoint; H = 150 held-out target tasks. (2) Teachers. MC: base weights conditioned on k=3 items from B_T (goal-similarity retrieval); PC: QLoRA rank 32 on the rewritten walkthroughs of B (no memory at inference), with epochs tuned so its trait rate on T matches MC's within 5 pp; controls MC-0 (k=3 from the unrewritten B) and PC-0 (QLoRA on unrewritten B). Gate 0: MC trait rate on T >= 0.5 absolute and >= 0.4 above the base k=0 rate; if the self-teacher does not adopt the trait from memory the regime is untestable and is reported. (3) Objectives on T (student = base weights, empty memory block, QLoRA rank 32, one epoch): SFT-full on teacher rollouts; SFT-clean with the trait-expressing step (T1: the inventory action and its observation; T2: the first-search action, loss-masked, observation kept) removed; OPD-full reverse-KL per token on student rollouts scored by the teacher; OPD-masked with the KL zeroed on the trait-expressing action span of the student's own sample. (4) Arms. T1: MC and PC x four objectives (8) plus MC-0 and PC-0 x {SFT-clean, OPD-masked} (4); T2: MC and PC x {SFT-clean, OPD-masked} (4). Two training seeds for MC/OPD-masked, MC/SFT-clean, PC/OPD-masked, PC/SFT-clean. (5) Evaluation: every student memory-free on valid_seen, valid_unseen and H, 2 seeds, paired on identical (game, seed) sets; trait rate at decision points, success rate, steps. In-context reference: base agent with B_T at k in {1, 3, 7} and with a decoy bank (rewritten other-type items) for P4. (6) Secondary defence arm: a trait direction estimated as the LoRA delta PC minus PC-0 (and, alternatively, a mean activation difference at the decision token) is projected out of the student update during OPD-masked and SFT-clean for both teachers. (7) Cost axis: training GPU-hours and per-episode tokens per arm, alongside the in-context trait bank at k=3. Budget: 4 teacher passes over T (~3.5k episodes), ~8 student-rollout passes for OPD arms (~7k episodes), ~20 QLoRA runs (~25 GPU-hours), ~14k evaluation episodes; three to four days with training overlapping serving.",
 "Baselines and Ablations": "MC-0 and PC-0 neutral teachers under the sanitised/masked objectives give the drift of the trait rate due to self-training alone (the P-CD0 analogue for traits). Unmasked SFT-full and OPD-full are ceilings. Mask placebo: OPD with the same number of randomly chosen non-trait action spans masked, to show masking per se does not suppress transfer. Dose: in-context trait rate at k in {1, 3, 7} on the base agent. Decoy bank: trait-rewritten other-type items to see whether the trait reads from irrelevant memory. Rate matching of PC to MC is an ablation axis (a stronger PC teacher must not be the reason it transfers). Optional harm extension, gated separately (in-context harm >= 6 net on a planted wrong-procedure type): the same four objectives on success rate, reported only if the gate passes.",
 "Falsifiable Predictions": "P1 (positive control, precondition for any null): PC/SFT-clean raises the T1 trait rate by >= 10 pp over PC-0/SFT-clean; if this fails the parameter-carried subliminal channel does not reproduce on this backbone and the memory-carried null is declared uninterpretable. P2: PC/OPD-masked >= PC/SFT-clean in transferred trait rate; falsified if PC/OPD-masked is within 5 pp of PC-0/OPD-masked while P1 holds, which would support the view that subliminal transfer is an SFT/LoRA-data artefact absent under full-distribution on-policy matching. P3 (central): MC/OPD-masked and MC/SFT-clean are within +/-5 pp of MC-0 under the same objective (equivalence, pre-registered), while MC/OPD-full and MC/SFT-full reach >= 0.7 x the MC teacher's trait rate; falsified if either sanitised/masked MC arm exceeds MC-0 by >= 10 pp, which would mean context-carried traits transfer subliminally, favouring the drift account and making memory-text sanitation an insufficient defence. P4: memory-free trait rate of the MC/OPD-full student exceeds the base agent's in-context trait rate with B_T at k=3 (distilled dispositions are unconditional; read dispositions are gated by retrieval and reading). P5 (secondary): projecting out the PC minus PC-0 direction cuts PC transfer by >= 50 % under both objectives and has no effect on MC arms (nothing to remove). P6: T2 reproduces the sign pattern of P1-P3 with a smaller magnitude because the search-order consequence remains in the observations (the dynamics channel of 2604.15559), which is the same for MC and PC and so does not change the contrast.",
 "Measurement and Noise Control": "Primary metric: trait rate at rule-identified decision points, binomial per arm with Wilson and paired-bootstrap CIs over games; every arm is evaluated on identical (game, seed) sets, so contrasts are paired at the game level. Power: T1 has one decision point per episode, giving ~1,400 points per arm over valid_seen + valid_unseen + H at 2 seeds, a 95 % half-width of ~2.5 pp at a rate of 0.2 and an MDE of ~5 pp for the equivalence test in P3; T2 has ~0.8 usable decision points per episode. The +/-5 pp equivalence margin is a fraction (<= 0.12) of the Gate-0 trait lift (>= 0.4), so it is tied to the measured effect. Training-seed variance from the four two-seed arms is added to the CIs of P2 and P3. Success rate is reported with its paired CI (about +/-8 net at 274 x 2, ~+/-5 pooled) only as a neutrality check; if a trait moves success by more than 5 net the trait is replaced (pre-registered amendment). Teacher trait rates are measured on the same T rollouts used for distillation, so PC/MC rate matching is verified on the training distribution and not assumed.",
 "Preprint Collision Check": "Query 1 (mechanism, --recent, s2=ok hf=ok): 'subliminal learning trait transfer on-policy distillation reverse KL self-teacher' returned 2606.22019 (channel location and auditability of subliminal learning, no on-policy test), 2606.04036, 2605.30833, 2605.16826 (decoupling KL and trajectories), 2604.10674 (Skill-SD), 2603.07079, 2602.04942; none tests trait transfer under on-policy distillation or a context-carried trait. Query 2 (closest method, all years, s2=ok hf=ok): 'trajectory distillation transfers unsafe agent behaviour despite sanitization LoRA artifact' returned 2605.30640 (CSULoRA), 2605.11882 (FATE), 2604.02947 (AgentHazard) and diffusion-distillation papers, not the target paper; s2cli paper lookups then verified 2604.15559 (Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation, s2, 4 citations) and 2606.00831 (Subliminal Learning is a LoRA Artifact, s2, 4 citations). Neither paper, nor 2609.01091 in the digest, contrasts a memory-carried (context-induced, identical-weights) teacher with a parameter-carried one or tests masked on-policy distillation. WebSearch not used (quota exhausted).",
 "Risk Factors and Limitations": "The self-teacher may not adopt the planted trait from memory at a high enough rate (Gate 0), especially T2; the fallback is a stronger in-context dose (k=7) or an instruction-induced trait, which changes the claim from memory-carried to context-carried and is reported as such. Sanitising T1 by deleting a step is clean, but T2's consequence survives in observations, so the T2 contrast tests the dynamics channel rather than pure subliminal transfer; this is stated, not hidden. Rate matching PC to MC on trait rate does not match their other behaviours; the PC-0 and MC-0 controls under each objective bound the difference. One epoch of reverse-KL with QLoRA may under-transfer everything, which the unmasked ceilings expose. The trait-direction defence in P5 is one estimator; a null there is weak evidence. Traits are benign by design; the optional harm extension depends on a separate gate and the success-rate noise floor. Results are for one 32B backbone and one environment, and the transfer of conclusions to unsafe traits in real agent memories is by argument, not measurement."
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

