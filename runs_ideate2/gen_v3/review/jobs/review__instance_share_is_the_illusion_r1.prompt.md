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
 "Name": "instance_share_is_the_illusion",
 "Title": "The Privilege Illusion of Retrieved Agent Memory Is Its Instance-Bound Share: What a Memory-Conditioned Self-Teacher Can and Cannot Distil into a Memory-Free Student",
 "Short Hypothesis": "With retrieved episodes as the privileged information of a self-teacher, the in-context gain on ALFWorld splits into a type-level procedure share (obtained equally from same-type walkthroughs of other scenes) and an instance-bound share (obtained only from the game's own walkthrough, the oracle item). Only the type share is replicable by a memory-free student; the instance share does not distil under any objective (on-policy reverse-KL, off-policy context distillation, raw SFT) and reappears one-for-one as the student's privileged-vs-unprivileged gap at deployment. The privilege illusion of agent memory is therefore a property of the information, not of the objective, and its size can be read off two in-context cells before any training is run.",
 "Related Work": "OP2SD (arXiv:2608.09228) shows on math that OPSD gains come partly from context-induced teacher behaviour by substituting unrelated problem-solution pairs, but has no memory, no agent, no instance/type split and does not test whether the unreplicable part returns as deployment dependence. DAPD (2608.01735) and DOPD (2606.30626) name the privilege illusion as an information-asymmetry gap and propose fixes with generic privileged context, +2-3 point gains, no seeds and no evaluation with the privileged information fully absent. Experience Distillation (2607.21051) reports >=64.8 % of the in-context gain retained memory-free and direct SFT 3.8 %, but never says which part of the gain is retained. CardDistill/SkillLens (2608.10775) and LOPSD (2608.13040) use state-conditioned memory as privileged teacher context to train a retrieval-free student without decomposing the privileged information or reporting the deployment gap; SMRC-SD (2608.05219) explains multi-turn failures by state-reference mismatch, which conditioning the teacher on a walkthrough valid at every student state (rather than a reference trajectory) sidesteps. The critical review 2608.25936 lists privileged context as one of three OPSD levers but tests no agent memory. Measurement A on this node shows the in-context gain is procedure-bound (unseen ~ seen) but never separates type-level from instance-level privileged information and trains no student.",
 "Abstract": "On-policy self-distillation methods internalise a privileged context into a student that acts without it, and the privilege-illusion literature warns that part of the teacher's advantage is an information gap the student cannot close. Nobody has asked which part when the privileged context is retrieved agent memory. We use the structure of ALFWorld to manufacture the decomposition. Four teacher conditions, all k=3 and token-matched (~430 tokens): the game's own expert walkthrough (oracle, maximal instance-bound information, the analogue of OPSD's reference solution), same-type walkthroughs from other floorplans (type-level procedure only), other-type walkthroughs (relevance-destroyed decoy) and an empty block (P-CD0). Stage 1 measures the four in-context cells on the base agent and defines the type share (same-type minus empty) and the instance share (oracle minus same-type). Stage 2 distils each teacher into a memory-free Qwen3-32B student with three objectives built on one partitioned pool (bank tasks disjoint from target tasks): on-policy reverse-KL on student rollouts, off-policy context distillation on teacher rollouts with the block removed, and raw step-level SFT. Every student is evaluated with memory absent, with the oracle item, with same-type memory and with the decoy. The prediction is that memory-free accuracy of the oracle-teacher student equals that of the same-type-teacher student (the instance share does not distil), that both exceed the decoy-teacher and P-CD0 students by a retained fraction of the type share, and that the gap between a student's oracle-conditioned and memory-free accuracy equals the base agent's instance share regardless of teacher and objective. Per task type the retained gain should concentrate on the heat/cool/clean procedures and the deployment gap on the location-bound pick-and-place and look-at types. All arms sit on one cost axis (training GPU-hours plus per-episode tokens) against the k=3 in-context arm, with a procedure-held-out type in a second partition.",
 "Experiments": "(1) Pool partition. The 1,465 expert walkthroughs are split by task, stratified by type and floorplan, into a bank pool B (40 %, retrievable at train and test) and a target pool T (60 %, teacher rollouts and distillation targets); 150 tasks of T are held out as an extra evaluation set H. A second partition removes one multi-step type (cool-then-place) from both B and T for the procedure-held-out check. Repeated on the self-rollout pool (own k=0 successes) for the on-policy objective only. (2) Teacher conditions, all k=3, token-matched to ~430 tokens: ORC = the game's own walkthrough (from the ALFWorld traj_data plan; available for train, valid_seen and valid_unseen games); TYP = three same-type walkthroughs from B restricted to other floorplans; DEC = three other-type walkthroughs from B (relevance-destroyed); EMP = empty block. (3) Stage 1, Gate 0: the base agent (thinking off, ReAct, 30 steps) is run under the four conditions on valid_seen, valid_unseen and H, 3 seeds, paired on (game, seed). Estimands: type share = TYP - EMP, instance share = ORC - TYP, format share = DEC - EMP. Gate: instance share >= 8 net/100 pooled over the three sets and type share >= 15 net/100; if the instance share fails the gate the instance half is declared untestable and only the type half proceeds. (4) Stage 2, objectives on T: (a) OPD: student = base model with empty memory block, teacher = same weights with the condition's block, reverse-KL per token on student rollouts over T (one pass, ~880 episodes) with the teacher scoring the student's own history so states are matched by construction; (b) CD: teacher rollouts over T under the condition, block removed, step-level SFT on the successful rollouts (Experience Distillation recipe); (c) SFT: step-level QLoRA on the raw walkthroughs of T (Measurement B recipe, no block; one arm). Arms: OPD x {ORC, TYP, DEC, EMP}, CD x {ORC, TYP, DEC, EMP}, SFT = 9 QLoRA rank-32 students, one epoch, matched examples; two training seeds for OPD-ORC and OPD-TYP. (5) Evaluation of every student on valid_seen, valid_unseen and H with test blocks absent, ORC, TYP (from B) and DEC, paired on identical (game, seed) sets, 2 seeds, plus 3 seeds for the confirmatory contrasts (OPD-ORC vs OPD-TYP memory-free; student ORC-gap vs base instance share). (6) Per-type analysis over the six task types and the held-out type. (7) Cost axis: training GPU-hours per arm plus per-episode inference tokens; cumulative-cost curve of each memory-free student against the k=3 in-context arm (~430 tokens/episode) and against the student with the block back. Budget: ~4 teacher passes and ~8 student-rollout passes over T (~10k episodes), ~11 QLoRA runs (~15 GPU-hours), ~18k evaluation episodes; three to four days on two A100s with training overlapping serving.",
 "Baselines and Ablations": "Base agent k=0 and the in-context k=3 matched-retrieval arm of Measurement A (the cost reference). P-CD0 (OPD-EMP and CD-EMP) for the self-training and format effects. DEC teachers at train and DEC blocks at test as token-matched placebos. Raw SFT (Measurement B) as the direct-SFT reference of Experience Distillation. Ablations: k=1 and k=7 for the ORC/TYP in-context cells to check the decomposition is not dose-specific; a scene-matched-but-other-task walkthrough teacher (same floorplan, different goal) to separate scene priors from the exact instance; DAPD-style dual anchoring on OPD-ORC as an optional fix arm if part of the instance share appears to transfer; LoRA rank 16 vs 32 on OPD-TYP to check capacity; on the self-rollout pool, OPD-TYP and OPD-EMP only.",
 "Falsifiable Predictions": "P1 (Stage 1): ORC > TYP > DEC ~ EMP; type share >= 0.7 of the Measurement A k=3 gain; format share within +/-4 net. P2 (central): memory-free OPD-ORC minus memory-free OPD-TYP <= 0.25 x instance share (pre-registered), i.e. the oracle teacher adds nothing that survives without memory; falsified if the difference is >= 0.5 x instance share, which would mean instance-bound bindings (scene priors) do distil and the illusion framing is wrong for agent memory. P3: memory-free OPD-TYP and CD-TYP retain >= 50 % of the type share, and OPD-DEC ~ OPD-EMP within the equivalence margin (0.25 x type share); falsified if OPD-DEC ~ OPD-TYP, which would transfer OP2SD's math finding to agents (the retained gain is context-induced format, not procedure). P4: for every student, accuracy with the ORC block minus memory-free accuracy lies within [0.7, 1.3] x the base agent's instance share, and does not differ between OPD, CD and SFT students by more than the margin (objective-invariant deployment gap); falsified if the gap shrinks for one objective (that objective closes the illusion) or grows (the crutch). P5: per type, retained gain concentrates on heat/cool/clean-then-place, the deployment gap on pick-and-place and look-at-in-light; on the procedure-held-out type every student's memory-free gain is <= 3 net while the in-context TYP block still delivers >= 60 % of its gain once that type is put back in B.",
 "Measurement and Noise Control": "Primary metric: net success per 100 games, paired on identical (game, seed) tuples across all arms, bootstrap CI over games. Noise floor of the setup: a paired cell of 274 x 2 gives about +/-8 net at 95 %; the Stage-1 shares and the confirmatory contrasts pool valid_seen + valid_unseen + H (698 games) at 3 seeds (~2,100 paired episodes), giving about +/-4 net for a single contrast and about +/-6 for a difference of differences (P4). Minimum detectable effect is stated before Stage 2: the instance share must exceed 8 net (Gate 0) so that 0.5 x instance share (the falsifier of P2) is at or above the MDE; equivalence margins are fractions of the Gate-0 shares, never fixed points; if Gate 0 fails the instance-half claim is reported as untestable. Training-seed variance from the two-seed OPD-ORC and OPD-TYP arms is reported as a variance component and added to the CI of P2. Per-type claims use type-level counts (n = 40-90 games per type per split) and are labelled exploratory unless the pooled three-set count per type exceeds 150. Every trained student also reports per-step teacher-forced action accuracy on H as a low-noise secondary that tracks the retained procedure.",
 "Preprint Collision Check": "Query 1 (mechanism, last 12 months, s2cli --recent, channels s2=ok hf=ok): 'privilege illusion on-policy self-distillation privileged context student dependence at inference' returned 2608.25936 (critical review of OPSD levers), 2608.09228 (OP2SD), 2608.01735 (DAPD), 2607.05184, 2606.30626 (DOPD), 2606.11709, 2605.11609, 2601.18734; none uses retrieved agent memory as the privileged context or separates instance-level from type-level information. Query 2 (closest method, --recent, s2=ok hf=ok): 'context distillation retrieved experience memory-conditioned teacher memory-free student agent' returned 2608.18952 (recommendation), 2608.10775 (SkillLens/CardDistill: state-conditioned memory as privileged teacher context, student without runtime retrieval, GUI), 2608.07169 (no training), 2607.29032, 2607.21051 (Experience Distillation), 2607.01480 (PMD), 2606.29502 (UCOB), 2606.00105. Query 3 (--recent, s2=ok hf=ok): 'state-conditioned memory privileged teacher context distill student without runtime retrieval agent' returned 2608.13040 (LOPSD), 2608.10775, 2608.07169, 2608.05219 (SMRC-SD), 2608.04956, 2607.27937 (OVCSD, skill-conditioned teacher from student-reached states), 2607.05184, 2604.10674. Closest collisions are CardDistill and LOPSD (memory as privileged teacher context); neither reports an oracle-vs-type-matched decomposition, the deployment gap, P-CD0 or matched-cost in-context arms. WebSearch not used (quota exhausted).",
 "Risk Factors and Limitations": "The instance share may be small on ALFWorld because object locations are re-sampled per task and same-type walkthroughs already carry scene priors; Gate 0 and the scene-matched-other-task ablation address this, and the fallback is to report the type half only. The oracle teacher may follow the walkthrough so literally that on-policy scoring of divergent student states becomes uninformative (the SMRC-SD mismatch); we monitor teacher entropy and success on student-reached states and fall back to state-matched routing. Reverse-KL on-policy distillation of a 32B model with QLoRA is a single epoch per arm; undertraining would deflate all retained fractions equally, which the raw SFT and CD arms bound. Findings are for one backbone and one environment; WebShop is out of budget this round. A retained type share and a non-distilling instance share could both be true while the deployment gap is objective-dependent (P4 false); that outcome is still informative and is reported as such."
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

Proposal: instance_share_is_the_illusion — The Privilege Illusion of Retrieved Agent Memory Is Its Instance-Bound Share: What a Memory-Conditioned Self-Teacher Can and Cannot Distil into a Memory-Free Student

- arxiv:2601.07470 · 2026-01-12 · preprint · sim 0.58 · hf
  Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
  Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed desi
- arxiv:2607.20972 · 2026-07-23 · preprint · sim 0.57 · hf
  Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents
  Coding agents ship with one kind of memory: documents. Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. Human expertise runs on a second tier that never gets written down: situationally-bound operational facts (gotchas, locations, local conventions) encoded as a side effect of the work and retrieved involuntarily when the situation cues them. We argue this
- arxiv:2607.28272 · 2026-07-30 · preprint · sim 0.56 · hf
  MemHarness: Memory Is Reconstructed, Not Replayed
  Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causi
- arxiv:2605.29463 · 2026-05-31 · preprint · sim 0.56 · hf
  Honest Lying: Understanding Memory Confabulation in Reflexive Agents
  Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR
- arxiv:2605.20616 · 2026-05-20 · preprint · sim 0.55 · hf
  Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents
  Language agents increasingly operate over streams of related tasks, yet existing memory systems struggle to convert accumulated experience into reusable knowledge. Retrieval-augmented and structured memory methods record per-session observations effectively, but often couple acquisition and consolidation into a single online process, leaving the agent without a global view across sessions to discover recurring patterns, abstract shared procedures, or prune redundant entries. Inspired by compleme
- arxiv:2512.16962 · 2025-12-18 · preprint · sim 0.55 · hf
  MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval
  Large Language Model (LLM) agents increasingly rely on long-term memory and Retrieval-Augmented Generation (RAG) to persist experiences and refine future performance. While this experience learning capability enhances agentic autonomy, it introduces a critical, unexplored attack surface, i.e., the trust boundary between an agent's reasoning core and its own past. In this paper, we introduce MemoryGraft. It is a novel indirect injection attack that compromises agent behavior not through immediate
- arxiv:2606.29502 · 2026-07-17 · preprint · sim 0.52 · hf
  UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation
  Skill memories can improve agentic reinforcement learning by reusing past experience as textual guidance, but retrieved skills are not oracular: they may help in one state while misleading the same policy in another. This makes the common privileged-teacher assumption fragile, namely that a skill-conditioned prompt can be treated as a fixed teacher for the no-skill prompt. We introduce UCOB, a framework for learning to utilize and evolve agentic skills via credit-aware on-policy bidirectional se
- arxiv:2608.09228 · 2026-08-10 · preprint · sim 0.52 · hf
  Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
  On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with OP^{2}SD (On-Policy Se
- arxiv:2608.05219 · 2026-08-05 · preprint · sim 0.51 · hf
  When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents
  Privileged on-policy distillation provides dense supervision for multi-turn agents by allowing a synchronized teacher to re-score the student's response at every turn with access to training-only references, such as successful trajectories. In interactive environments, however, the student's preceding actions continually change the execution state. As the student takes different actions or completes subgoals in a different order, its rollout may reach states not covered by the reference, making 
- arxiv:2512.13564 · 2025-12-15 · preprint · sim 0.50 · hf
  Memory in the Age of AI Agents
  Memory has emerged, and will continue to remain, a core capability of foundation model-based agents. As research on agent memory rapidly expands and attracts unprecedented attention, the field has also become increasingly fragmented. Existing works that fall under the umbrella of agent memory often differ substantially in their motivations, implementations, and evaluation protocols, while the proliferation of loosely defined memory terminologies has further obscured conceptual clarity. Tradition

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

