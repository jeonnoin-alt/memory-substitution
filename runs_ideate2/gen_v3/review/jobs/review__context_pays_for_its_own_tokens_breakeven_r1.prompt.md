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
 "Name": "context_pays_for_its_own_tokens_breakeven",
 "Title": "Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience",
 "Short Hypothesis": "On multi-step agent tasks retrieved experience shortens episodes by more tokens than it injects, because the memory-free agent's failures are 30-step timeouts and the memory-conditioned agent finishes the same tasks in about a dozen steps; therefore the injected-token convention of the memory literature gets the sign of the context route's cost wrong. Once cost is measured as total episode tokens or GPU-seconds on one backbone, the weights-versus-context break-even is set by the residual step-count gap between the memory-free student and the k=3 agent, moves by more than 2x with the accounting convention alone, and is not reached within 5,000 deployment episodes by context distillation because its higher retained fraction does not repay the teacher pass.",
 "Related Work": "The only amortization analysis in the digest is 2512.02543 (in-context distillation with self-consistency cascades; id verified with the literature command, S2 title 'Inference-Time Distillation: Cost-Efficient Agents Without Fine-Tuning or Manual Prompt Engineering'), which computes a teacher-versus-student break-even (843 episodes) with no fine-tuning arm and with injected demonstration tokens as the cost; it never asks whether the demonstrations shorten the student's episodes. Experience Distillation (2607.21051) reports the retained memory-free fraction (>= 64.8 % vs 3.8 % for direct SFT) but no training compute or inference token cost relative to keeping the histories in context (G23). ReMe (2512.10696) and MemHarness (2607.28272) report 8B-with-memory beating larger memoryless models and reconstruction gains without counting retrieval or reconstruction tokens (G22). PMD (2607.01480), SKILL0 (2604.02268), pi-Distill (2602.04942) and SESA (2607.29468) advertise memory-free deployment without a keep-in-context arm at matched cost (G21). Agentic Context Management (2607.21503) and the marginal-token-allocator position (2605.01214) treat context tokens as the cost to be minimized and never measure the episode-length effect of memory. The archived idea amortization_horizon_ranking_flip (5.35) varied the cost definition across two backbones (8B+memory vs 14B) and had no weights arm; the brief's rules now require one backbone, one pool and one cost axis. None of these measures whether memory reduces total tokens, and none computes a same-backbone break-even with a confidence interval under more than one accounting convention.",
 "Abstract": "Every cost comparison between in-context and parametric experience counts the tokens a memory injects and stops there. On agent tasks this is the wrong quantity: on ALFWorld with Qwen3-32B the memory-free agent fails mostly by exhausting its 30-step budget, and three retrieved episodes (~430 tokens) convert those timeouts into ~12-step successes, so the memory plausibly removes more prompt and generation tokens than it adds. We build both routes from one partitioned expert pool on one backbone -- retrieval at k in {1,3,7} from a bank disjoint from the training targets, one-epoch QLoRA SFT, context distillation from the k=3 teacher, and the P-CD0 control -- and log per-step prompt, completion and prefix-cached tokens, steps to termination and server GPU-seconds for every episode. We report the accuracy-cost Pareto front and the iso-accuracy break-even horizon N* (deployment episodes after which the amortized training cost, including the teacher pass and pool collection, is repaid by per-episode savings) under three conventions: injected tokens, total episode tokens, and measured GPU-seconds with prefix caching, each with a cluster-bootstrap CI over games and seeds. The pre-registered claims are that total tokens at k=3 are lower than at k=0 (sign flip), that N* moves by more than 2x with the convention alone, and that context distillation's higher retained fraction does not repay its teacher pass within 5,000 episodes. Both pools (expert and own-rollout), a procedure-held-out type on which retrieval pays tokens for no gain, and a step-cap ablation bound the scope of the sign flip. The contribution is a cost axis on which the two substrates can be compared at all, and a measured answer for one backbone.",
 "Experiments": "E0 Partition and gates. Split the 1,465 train tasks stratified by task type into targets T (55 %, ~806), bank B (30 %, ~440) and an evaluation-only train slice H (15 %, ~220); pick_cool_then_place is additionally withheld from T and B for the procedure-held-out cell. Gate 0: re-measure the k=3 gain with bank B on valid (274 games x 2 seeds); require net gain >= 15 points (Measurement A: +27/+32 with the full bank), else stop. E1 Retrieval cost profile. Base agent at k in {0,1,3,7} and decoy-3 (relevance-destroyed, token-matched) on valid + H, 3 seeds, paired by (task, seed); per episode log prompt tokens, completion tokens, prefix-cache hits, steps, termination reason, and per-arm GPU-seconds at a fixed concurrency on one replica per GPU. Decompose delta tokens (k vs 0) by outcome stratum: timeout->success, success->success, fail->fail, success->fail. E2 Trained arms (all on T, expert pool; QLoRA nf4 r32, one epoch, 2 LoRA seeds each): SFT on expert step targets; CD = Experience Distillation recipe (teacher = base at k=3 with bank B, one pass over T, ~800 episodes with memory; student trained to reproduce the teacher's actions from the memory-free prompt); P-CD0 = same recipe with the teacher at k=0. Evaluate each student at k=0 (absent), k=1 and k=3 from B (matched) and decoy-3 (mismatched) on valid + H, 3 seeds, with the same logging; report the privileged-vs-unprivileged gap. E3 Frontier and break-even. Cost per episode c(config) under three conventions; training cost = measured QLoRA wall-clock GPU-seconds + teacher-pass GPU-seconds (CD, P-CD0) + pool-collection GPU-seconds (own-rollout pool only; expert walkthroughs cost no inference). For each accuracy level A reachable by a base+k config and by a student config (student + smallest k' within the pre-registered margin), N*(A) = training cost / (c_context(A) - c_student(A)); cluster bootstrap over tasks (seeds nested) gives the CI; N* is undefined when the student cannot reach A. Plot cumulative cost vs deployed episodes for every config. E4 Own-rollout pool. Repeat E2-E3 with the on-policy pool (runs/bank/own_rollouts_train.jsonl) as soon as it is complete; collection cost is charged at the measured k=0 rollout GPU-seconds per successful trajectory (about 1/0.54 episodes per success at valid-level success rates). E5 Scope ablations: step cap 50 for one seed of E1 (does the saving grow with the cap?); prefix caching off for one seed (uncached GPU-seconds); Qwen3-8B as a one-seed robustness check of the sign flip. Budget: ~7,400 base episodes + 6 students x 4 conditions x 3 seeds x 494 tasks ~ 35,600 episodes, 12 GPU-hours of QLoRA, ~3,500 teacher-pass episodes; training runs on one GPU while the other serves; about three days.",
 "Baselines and Ablations": "Context route: base at k=0/1/3/7 with bank B; decoy-3 and decoy-7 placebos (same length, relevance destroyed by drawing items from other task types with object names swapped). Weights route: direct SFT (the weak baseline of 2607.21051), Experience Distillation reimplementation (CD), P-CD0 (empty-retrieval teacher, same recipe and on-policy-ness); every student also evaluated with decoy items so that a student's additivity at k=1 is not a length effect. Cost ablations: injected-only vs total-token vs GPU-second conventions; prefix caching on/off; step cap 30 vs 50; token-to-GPU-second conversion measured from the same runs rather than assumed. Scope: expert pool vs own-rollout pool; procedure-held-out type (retrieval with cross-type items only) where the context route pays tokens for no gain; Qwen3-8B one-seed replication of the sign flip.",
 "Falsifiable Predictions": "P1 (sign flip): pooled over valid + H, the paired mean of total episode tokens at k=3 minus k=0 is <= 0 with a 95 % CI excluding +430 x mean steps (the injected-token prediction), and on the three multi-step types (clean/heat/cool then place) total tokens fall by >= 25 %; falsified if the pooled paired difference is > 0 with CI excluding 0. P2 (student shortens too): the memory-free SFT student uses >= 20 % fewer total tokens per episode than base k=0; falsified if its episodes are not shorter. P3 (convention sensitivity): at the accuracy level of base+k=3, N* for the SFT student differs by >= 2x between the injected-only and total-token conventions, and by >= 2x again between total-token and prefix-cached GPU-seconds; falsified if all three N* lie within 1.5x of each other. P4 (teacher pass): for every accuracy level reachable by both students, N*_CD > N*_SFT for horizons up to 5,000 episodes; falsified if the CD student reaches base+k=3 accuracy at k'=0 or k'=1 while the SFT student needs k' >= 3, which makes CD's per-episode saving large enough to repay the teacher pass. P5 (held-out type): on pick_cool_then_place withheld from bank and targets, cross-type retrieval does not convert timeouts (its gain is within the noise floor) while its cost exceeds k=0, so its cost-per-point is undefined there; falsified if cross-type retrieval converts timeouts on that type at half or more of the same-type rate. Predictions are stated per pool; the own-rollout pool is expected to show the same sign in P1 and a smaller retained fraction.",
 "Measurement and Noise Control": "Every arm runs on identical (task, seed) pairs so all contrasts are paired; success contrasts use paired net/100 with a cluster bootstrap over tasks (2,000 resamples, seeds nested in tasks); token contrasts use the paired per-task mean with the same bootstrap. Noise floor: 274 games x 2 seeds gives about +/-8 net points (measured); adding H (~220 train tasks) and a third seed gives ~1,480 paired episodes and about +/-5 net points, the minimum detectable accuracy effect for the headline cells; token differences are continuous and resolve at ~5 % of the mean. Gate 0: k=3 gain with bank B >= 15 net points. Gate 1: the memory-free student's gain >= 25 % of the Gate-0 gain; if not met, iso-accuracy N* is declared not computable at this pool size and only cost-per-net-point is reported (no TOST). Equivalence margins for 'student + k' matches base + k=3' are pre-registered as one third of the Gate-0 gain. LoRA seed variance is reported as a variance component next to evaluation-seed variance; if the LoRA-seed SD of the memory-free margin exceeds 3 net points a third LoRA seed is added before the confirmatory run. GPU-seconds are measured per arm at a fixed client concurrency chosen from the vLLM queue (running >= 8 per replica), prefix cache cleared between arms, throughput logged with every arm; the token-to-GPU-second rate used to amortize training is measured from these runs, not assumed. All thresholds, the T/B/H split seed and the accounting formulas are written to a pre-registration file before the first confirmatory run.",
 "Preprint Collision Check": "All queries ran through the literature command (Semantic Scholar + HF Papers, --recent, limit 8); WebSearch not used (quota exhausted); WebFetch never used. (1) 'inference token cost accounting agent memory retrieval episode length amortization' -> 2607.21503 Agentic Context Management (context lifecycle, quadratic cost), 2605.01214 marginal token allocators (position), 2605.11733 energy-to-token (position), 2601.05960 memory-as-a-tool (lower inference cost than test-time refinement, context route only), 2512.02543; none measures episode-length savings of retrieved experience or a weights-vs-context break-even. (2) 'break-even cost in-context demonstrations versus fine-tuning student agent amortization' -> 2512.02543 (2.5x lower cost than the teacher on ALFWorld; no fine-tuning arm), ACE 2510.04618; nothing else relevant. (3) 'context distillation agent interaction histories memory-free retained gain Experience Distillation' -> 2607.21051, 2608.07068 MemOPD (on-policy distillation via memory-state alignment; a training-efficiency method, no context arm), 2608.07169 Agent Memory Distillation (teacher memory handed to a small model without training, context route only), 2609.02253 APEx (2026-09-02, hierarchical experience memory for deep-research QA, no weights arm), 2607.29032 TransMem; no cost-matched head-to-head. (4) 's2cli paper 2512.02543' verified the id (channel: S2). No preprint found that reports total-episode token savings from retrieved experience or a same-backbone break-even with a CI.",
 "Risk Factors and Limitations": "(1) The sign flip depends on failures being timeouts; in environments where failures are fast (wrong final answer, WebShop) memory may not shorten episodes -- reported as a scope condition, with the decomposition by outcome stratum making the dependence explicit and an optional WebShop cell. (2) Prefix caching can make injected tokens nearly free, which strengthens P1 but makes the GPU-second convention sensitive to cache warmth and concurrency; we measure at matched concurrency with cache resets and also report the uncached convention. (3) A step cap of 30 bounds the saving; the cap-50 ablation shows whether the effect grows or is a cap artefact. (4) If the memory-free retained fraction is small (Gate 1 fails), no iso-accuracy break-even exists and the result is a cost-per-point frontier only. (5) The own-rollout pool may not be complete; the expert-pool result stands alone with a stated limitation. (6) Training cost is a one-node measurement (QLoRA nf4 r32, one epoch); the amortization formula is given so readers can substitute other training costs. (7) One backbone family; the 8B check is single-seed."
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

Proposal: context_pays_for_its_own_tokens_breakeven — Memory That Pays for Its Own Tokens: Total-Episode Cost Accounting Flips the Weights-versus-Context Break-Even for Agent Experience

- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.60 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.21503 · 2026-07-23 · preprint · sim 0.56 · hf
  Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
  Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. The incumbent response treats this as a storage-and-retrieval problem. We argue that framing i
- arxiv:2602.16313 · 2026-02-18 · preprint · sim 0.54 · hf
  MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks
  Existing evaluations of agents with memory typically assess memorization and action in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment,
- arxiv:2601.11969 · 2026-01-17 · preprint · sim 0.52 · hf
  MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models
  Existing works increasingly adopt memory-centric mechanisms to process long contexts in a segment manner, and effective memory management is one of the key capabilities that enables large language models to effectively propagate information across the entire sequence. Therefore, leveraging reward models (RMs) to automatically and reliably evaluate memory quality is critical. In this work, we introduce MemoryRewardBench, the first benchmark to systematically study the ability of RMs to evaluate l
- arxiv:2606.03329 · 2026-06-02 · preprint · sim 0.51 · hf
  InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain
  Long-context tasks require LLMs to identify and preserve answer-relevant information from large contexts. Chunk-wise memory agents address this issue by sequentially reading document chunks, updating a compact memory, and generating the final answer from the accumulated memory. However, existing RL-based chunk-wise agents either rely on sparse final-answer rewards or use lexical intermediate rewards for memory and retrieval actions. These signals supervise task success or local overlap, but do n
- arxiv:2105.14039 · 2021-05-28 · preprint · sim 0.48 · hf
  Towards mental time travel: a hierarchical memory for reinforcement
  learning agents
  Reinforcement learning agents often forget details of the past, especially after delays or distractor tasks. Agents with common memory architectures struggle to recall and integrate across multiple timesteps of a past event, or even to recall the details of a single timestep that is followed by distractor tasks. To address these limitations, we propose a Hierarchical Chunk Attention Memory (HCAM), which helps agents to remember the past in detail. HCAM stores memories by dividing the past into c
- arxiv:2608.04003 · 2026-08-04 · preprint · sim 0.45 · hf
  PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-
- arxiv:2605.29341 · 2026-05-28 · preprint · sim 0.44 · hf
  WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction
  Multimodal large language models are increasingly deployed as long-horizon agents, where memory must do more than recall: it must track an evolving world, revise what has gone stale, and surface the right evidence at decision time. Existing benchmarks measure recall over static dialogue, collapse memory into a single end-of-task accuracy, and reduce visual observations to captions, leaving us unable to localize failures to writing, maintenance, retrieval, or use. The rise of agent harnesses that
- arxiv:2603.23971 · 2026-03-25 · preprint · sim 0.43 · hf
  The Price Reversal Phenomenon: When Cheaper Reasoning Models End Up Costing More
  Developers and consumers increasingly choose reasoning language models (RLMs) based on their listed API prices. However, how accurately do these prices reflect actual inference costs? We conduct the first systematic study of this question, evaluating 8 frontier RLMs across 9 diverse tasks covering competition math, science QA, code generation, and multi-domain reasoning. We uncover the pricing reversal phenomenon: in 21.8% of model-pair comparisons, the model with a lower listed price actually i
- arxiv:2608.18852 · 2026-08-19 · preprint · sim 0.43 · hf
  SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
  Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

