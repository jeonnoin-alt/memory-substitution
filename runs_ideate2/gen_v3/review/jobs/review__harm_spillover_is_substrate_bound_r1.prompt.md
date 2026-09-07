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
 "Name": "harm_spillover_is_substrate_bound",
 "Title": "Retrieved Harm Stays Where It Is Retrieved, Internalized Harm Spreads: Substrate-Dependent Spillover and Dose-Response of Wrong-Procedure Agent Memory",
 "Short Hypothesis": "The same wrong-procedure items harm an agent through different channels in the two substrates. In context the harm is retrieval-gated: it scales linearly with the poisoned fraction of the retrieved set and reaches sibling task types only through cross-type retrieval, which the logs measure. Once internalized by SFT or on-policy distillation the harm is procedure-diffuse: it spills over to sibling types that share sub-procedures at a higher spillover ratio, is thresholded rather than linear in the poisoned fraction, and is only partly overridden by clean memory placed back in context. On-policy distillation transmits less direct harm than SFT at the same poisoned fraction, by a discount predicted by the teacher's measured compliance rate.",
 "Related Work": "The Compliance Trap (2607.10608) shows that agents adopt task-conflicting retrieved memory at the first exposed decision point, that repeated exposure amplifies the error and recovery is weak, but only in context; it does not ask what the same items do once internalized. Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation (2604.15559) shows unsafe agent behaviours transferring through trajectory distillation after keyword sanitation but never runs the same trajectories as few-shot or retrieved context, and reports no dose or spillover. Bias amplification through distillation (2505.24842) is training-time poisoning with no in-context arm. MemTrapBench (2608.20202) and MemSyco-Bench (2607.01071) benchmark cognitive traps of retrieved memory at inference only. Corridor regularization (2609.01091) defends SFT distillation against trait-direction drift and leaves on-policy objectives untested. The 2026-08 pilot in this program found one-sided harm at high injection volume where volume, not content, was the lever; this design fixes volume and varies content. The archived harm_does_not_distill idea framed context distillation as an asymmetric filter but its 3-point margin exceeded the ~1.3-point harm it probed and it lacked the P-CD0 control.",
 "Abstract": "Whether unwanted content does the same damage when kept in context as when trained into weights is unresolved in both directions (digest gap G9), and on this node the only natural harm regime is a -4.8 net-point type, too small to study. We manufacture harm: for the heat-then-place and cool-then-place types, a fraction p of the expert walkthroughs in both the retrievable bank and the disjoint training targets is replaced by well-formed wrong-procedure walkthroughs (the appliance step replaced by a plausible no-op, or the place step executed before the appliance step), chosen at Gate 0 so that k=3 retrieval at p=0.5 costs at least 10 net points on the poisoned types. Clean-then-place shares the take, appliance, receptacle, put skeleton and serves as the sibling type; pick-and-place and look-in-light are controls. For p in {0, 0.1, 0.3, 0.5} we compare k=3 retrieval from the poisoned bank with a step-level SFT student, an on-policy reverse-KL student distilled from the poisoned-memory teacher, the empty-teacher P-CD0 control and a token-matched decoy arm, all on Qwen3-32B and one cost axis, and evaluate every student with memory absent, with the clean bank back, and with mismatched items. The estimands are direct harm on the poisoned types, sibling spillover and its ratio to direct harm, the in-context cross-type retrieval rate of poisoned items, the override fraction when clean memory is restored, the OPSD teacher's compliance rate, and the entry-propagation-recovery signature per substrate. A planted benign majority-action prior serves as the positive control for the disposition channel. The design pits the compliance-trap account (context dominates) against the crutch and information-abundance accounts (weights dominate when context is absent) on the same items.",
 "Experiments": "1. Manufactured regime and Gate 0: build two wrong-procedure variants for heat_then_place and cool_then_place items (V1: appliance step replaced by a plausible interaction with the wrong appliance, e.g. stoveburner or toaster, followed by place; V2: place executed before the appliance step); keep them syntactically valid so they execute. Measure in-context harm at k=3 with p=0.5 on the poisoned types pooled over valid_seen, valid_unseen and a held-out train split H (about 290 games x 3 seeds). Gate: direct harm >= 10 net points for at least one variant; otherwise the claim is declared untestable and no student is trained.\n2. Pools and partition: task-level split into bank B (60 percent), target pool T (25 percent), probe H (15 percent) on the expert pool; poisoning at fraction p is applied independently to the poisoned-type items of B and of T so that no bank item is a training target; the clean p=0 bank is kept for the clean-memory test condition. Replicate at p=0.5 on the self-rollout pool by grafting the same wrong procedures onto own successful rollouts.\n3. Arms: in-context k=3 from the poisoned B at every p; S_sft(p) by step-level SFT on the poisoned T at p in {0, 0.1, 0.3, 0.5}; S_opsd(p) by OPSD (2601.18734) reverse-KL from the teacher that retrieves k=3 from the poisoned B, at p in {0, 0.1, 0.5}; S_empty (P-CD0, empty-teacher OPSD, one arm); S_decoy (token-matched relevance-destroyed context at training, one arm); positive-control S_prior (SFT on T where 100 percent of poisoned-type items begin with a fixed benign first action). Training on the full T (about 2 GPU-hours per arm) on the GPU not serving.\n4. Teacher pass diagnostics: for S_opsd, log the teacher's episodes on T and compute the compliance rate c(p), the fraction of episodes with a poisoned item retrieved in which the teacher executes the wrong procedure.\n5. Evaluation: every arm on poisoned types, sibling type and control types, in three prompt conditions (absent; clean matched k=3 from the p=0 bank; mismatched token-matched other-type items), 274 validation games x 3 seeds plus H, paired over (game, seed). Retrieval logs record, for every sibling-type episode, whether a poisoned item was retrieved (cross-type retrieval rate r_x).\n6. Estimands: direct harm D(p) = net change on poisoned types relative to the p=0 arm of the same substrate; sibling spillover Sp(p); spillover ratio rho = Sp/D; override fraction omega = 1 - D(clean memory)/D(absent) for trained students; dose shape by pre-registered comparison of linear versus piecewise fits over p with seeds as replicates; entry step (first deviation from the correct procedure), propagation (deviation persists to episode end) and recovery fraction per substrate.\n7. Cost axis: GPU-hours per trained arm and per-episode tokens per test condition; report the cost at which each substrate reaches its harm level.\n8. Conditional defence arms, run only if both substrates show D >= 10 at p=0.5: an in-context analogue of corridor regularization (drop retrieved items whose action skeleton deviates from the bank's type-majority skeleton) and corridor regularization proper (2609.01091) on S_sft, compared on the same harm and spillover estimands.",
 "Baselines and Ablations": "Clean p=0 arms of every substrate (the reference for D); S_empty as the mandatory P-CD0; S_decoy as the training-time token-matched placebo; the two wrong-procedure variants V1 and V2 as a content ablation (harm that removes a step versus harm that reorders steps); off-policy context distillation (Experience Distillation, 2607.21051) at p=0.3 as an objective robustness check; S_prior as the positive control for the disposition channel (must reach >= 50 percent adoption memory-free before any 'does not transfer' statement is made); self-rollout pool replication at p=0.5; LoRA rank 8 on S_sft(0.5) to check that spillover is not a rank artefact.",
 "Falsifiable Predictions": "P1 (spillover ratio): at the poisoned fraction where SFT and in-context direct harm are matched within margin, rho_sft >= 2 x rho_context; falsified if rho_sft <= rho_context + margin. P2 (in-context spillover is retrieval): Sp_context <= r_x x (direct harm per retrieved poisoned item), i.e. sibling-type harm in context is accounted for by cross-type retrieval of poisoned items; falsified if in-context sibling harm exceeds what the logs can explain, which would show in-context procedure generalization. P3 (dose shape): D_context(p) is linear with D(0.1)/D(0.5) in [0.1, 0.35]; D_sft(0.1) is within noise of zero and D_sft(0.5)/D_sft(0.3) >= 1.5 (threshold); falsified if both substrates are linear or if SFT harm is super-linear at low p. P4 (override): omega_sft <= 0.7, i.e. restoring the clean bank removes at most 70 percent of internalized direct harm; the compliance-trap account predicts omega near 1, and P4 is falsified if omega >= 0.9. P5 (objective): D_opsd(p) = c(p) x D_sft(p) within margin at p in {0.1, 0.5}; falsified if OPSD transmits at least as much harm as SFT, or if the discount does not track the measured compliance rate. P6 (signature): entry steps of in-context harm coincide with the divergence step of the retrieved poisoned walkthrough (distribution matches within a KS test), while internalized harm has the same entry step but a recovery fraction at most half that of in-context harm; falsified if internalized harm recovers at least as often. P7 (controls): no arm changes pick-and-place or look-in-light beyond margin; a change there would indicate a global capability loss and would reassign the effect to forgetting, not spillover.",
 "Measurement and Noise Control": "Per-type cells are small on the validation splits (heat 39, cool 46, clean 58 games), so the poisoned types are pooled (heat and cool), the held-out train split H adds about 200 poisoned-type and 100 sibling-type games, and every cell runs 3 seeds: about 870 paired episodes on the poisoned types (about +-5 net) and 480 on the sibling type (about +-7). Gate 0 demands D_context(0.5) >= 10, twice the sibling CI, so that spillover ratios of 0.1 versus 0.3 are resolvable; the minimum detectable spillover difference is stated before the confirmatory run. Ratios (rho, omega) get bootstrap CIs over games; dose-shape claims are pre-registered as model comparisons with seeds as replicates; two LoRA seeds on S_sft(0.5) and S_opsd(0.5) bound training noise; all pairs are matched on (game, seed); token counts are matched within 5 percent across prompt conditions and reported.",
 "Preprint Collision Check": "Query 4 (s2cli, --recent, channels s2+hf, both ok): 'conflicting retrieved memory compliance trap agent internalized weights fine-tuning' returned MemTrapBench 2608.20202, Compliance Trap 2607.10608, MemSyco-Bench 2607.01071, Fine-Mem 2601.08435, NeuroGenPoisoning 2510.21144, Entropy-Adaptive Fine-Tuning 2601.02151; all inference-time memory or unrelated; no paper internalizes conflicting memory and compares. Query 5 (s2cli, --recent, s2+hf): 'unsafe agent behavior transfer trajectory distillation versus in-context few-shot demonstrations' returned Gated Hindsight Distillation 2608.06065, Experience Distillation 2607.21051, SkillHarness 2606.20636, and unrelated driving and simulation papers; no in-context versus distilled harm comparison. Query 6 (s2cli, --recent, s2+hf): 'poisoned demonstrations fine-tuning harm spillover related tasks LLM agent dose' returned SkillHarm 2606.02540 (skill-lifecycle attacks, no substrate comparison), a toxicity audit 2601.01090, AgentAlign 2505.23020, SafeArena 2503.04957; nothing on spillover or dose across substrates. Query 7 (run for the third proposal, s2cli --recent) confirmed 2604.15559 (Subliminal Transfer of Unsafe Behaviors, 4 citations) as the closest named prior work; it has no in-context arm, no dose ladder and no spillover measurement. WebSearch was not used. No collision found.",
 "Risk Factors and Limitations": "Manufactured wrong procedures may be rejected by the k=0 agent (it already knows heating uses the microwave), in which case Gate 0 fails and the claim is untestable on this backbone; the two variants and the self-rollout graft are the mitigation. The linear-versus-threshold dose contrast needs four in-context points but only three SFT points and two OPSD points within budget; the dose-shape prediction is therefore confirmatory for SFT and exploratory for OPSD. Spillover could be confounded with general forgetting; the control types and the P7 prediction guard this, and any control-type change reassigns the effect. Compliance rate c(p) is a mediator measured on the teacher, not manipulated, so P5 is a quantitative consistency check rather than a causal test. Eight trained arms plus about 30,000 evaluation episodes fit in about four days only with both GPUs busy throughout; if the budget tightens, the p=0.3 SFT arm is dropped first. One backbone, one environment."
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

Proposal: harm_spillover_is_substrate_bound — Retrieved Harm Stays Where It Is Retrieved, Internalized Harm Spreads: Substrate-Dependent Spillover and Dose-Response of Wrong-Procedure Agent Memory

- arxiv:2604.18847 · 2026-04-20 · preprint · sim 0.58 · hf
  Human-Guided Harm Recovery for Computer Use Agents
  As LM agents gain the ability to execute actions on real computer systems, we need ways to not only prevent harmful actions at scale but also effectively remediate harm when prevention fails. We formalize a solution to this neglected challenge in post-execution safeguards as harm recovery: the problem of optimally steering an agent from a harmful state back to a safe one in alignment with human preferences. We ground preference-aligned recovery through a formative user study that identifies valu
- arxiv:2607.23693 · 2026-07-26 · preprint · sim 0.48 · hf
  Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV
  Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest. Eviction and episodic-memory schemes therefore rest on a premise rarely tested directly, that a retained event is still informative once the observations that produced it are gone. We test it by omitting one earlier observation from what is served, across otherwise identical agent histories. Among items sensitive to that observation, the answer overwhelmingly fol
- arxiv:2604.09544 · 2026-08-24 · preprint · sim 0.44 · hf
  Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types
  Large language models remain vulnerable to jailbreaks that elicit harmful responses, yet the mechanism behind harmful response generation is poorly understood. Here, we investigate how this capability is organized within model parameters. We identify and prune parameters that specifically support harmful compliance, providing a direct mechanistic analysis at the parameter level. We find that this capability depends on a sparse set of critical parameters: pruning these parameters substantially re
- arxiv:2607.12406 · 2026-07-14 · preprint · sim 0.42 · hf
  Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions
  The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share t
- arxiv:2601.07395 · 2026-01-12 · preprint · sim 0.41 · hf
  MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP
  To standardize interactions between LLM-based agents and their environments, the Model Context Protocol (MCP) was proposed and has since been widely adopted. However, integrating external tools expands the attack surface, exposing agents to tool poisoning attacks. In such attacks, malicious instructions embedded in tool metadata are injected into the agent context during MCP registration phase, thereby manipulating agent behavior. Prior work primarily focuses on explicit tool poisoning or relied
- arxiv:2507.21815 · 2025-07-29 · preprint · sim 0.38 · hf
  HRIPBench: Benchmarking LLMs in Harm Reduction Information Provision to
  Support People Who Use Drugs
  Millions of individuals' well-being are challenged by the harms of substance use. Harm reduction as a public health strategy is designed to improve their health outcomes and reduce safety risks. Some large language models (LLMs) have demonstrated a decent level of medical knowledge, promising to address the information needs of people who use drugs (PWUD). However, their performance in relevant tasks remains largely unexplored. We introduce HRIPBench, a benchmark designed to evaluate LLM's accur
- arxiv:2508.14925 · 2025-08-19 · preprint · sim 0.37 · hf
  MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers
  By providing a standardized interface for LLM agents to interact with external tools, the Model Context Protocol (MCP) is quickly becoming a cornerstone of the modern autonomous agent ecosystem. However, it creates novel attack surfaces due to untrusted external tools. While prior work has focused on attacks injected through external tool outputs, we investigate a more fundamental vulnerability: Tool Poisoning, where malicious instructions are embedded within a tool's metadata without execution.
- arxiv:2604.02656 · 2026-04-06 · preprint · sim 0.33 · hf
  Transfer Learning for Meta-analysis Under Covariate Shift
  Randomized controlled trials often do not represent the populations where decisions are made, and covariate shift across studies can invalidate standard IPD meta-analysis and transport estimators. We propose a placebo-anchored transport framework that treats source-trial outcomes as abundant proxy signals and target-trial placebo outcomes as scarce, high-fidelity gold labels to calibrate baseline risk. A low-complexity (sparse) correction anchors proxy outcome models to the target population, an
- arxiv:2411.03923 · 2024-11-06 · preprint · sim 0.30 · hf
  Evaluation data contamination in LLMs: how do we measure it and (when)
  does it matter?
  Hampering the interpretation of benchmark scores, evaluation data contamination has become a growing concern in the evaluation of LLMs, and an active area of research studies its effects. While evaluation data contamination is easily understood intuitively, it is surprisingly difficult to define precisely which samples should be considered contaminated and, consequently, how it impacts benchmark scores. We propose that these questions should be addressed together and that contamination metrics c
- arxiv:2511.21757 · 2025-11-24 · preprint · sim 0.27 · hf
  Medical Malice: A Dataset for Context-Aware Safety in Healthcare LLMs
  The integration of Large Language Models (LLMs) into healthcare demands a safety paradigm rooted in primum non nocere. However, current alignment techniques rely on generic definitions of harm that fail to capture context-dependent violations, such as administrative fraud and clinical discrimination. To address this, we introduce Medical Malice: a dataset of 214,219 adversarial prompts calibrated to the regulatory and ethical complexities of the Brazilian Unified Health System (SUS). Crucially, 

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

