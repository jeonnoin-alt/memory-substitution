You are one of three independent reviewers. Read everything below, then output ONLY a single JSON object that validates against the schema — no prose before or after, no markdown fences.

=== SYSTEM ===
You are reviewing a research proposal for ICLR 2027 main track. Review it the way an experienced, skeptical area chair would: assume it will be rejected unless it earns acceptance, and look for the reason it would be.

Score honestly and use the full range — most submitted ideas are borderline or below, and a 9 means you would fight for it in discussion. Do not reward ambition, fluent writing, or a long experiment list; reward a claim that is new, testable, and actually tested by the plan as written.

Be specific: name the prior work that threatens novelty, name the baseline the plan omits, name the interleaving of results that would make the central claim collapse. "More experiments needed" is not an objection.

This field moves fast, so weigh recency: the work most likely to have scooped a proposal is an arXiv preprint from the last few months, not an indexed paper. Treat the proposal's Preprint Collision Check as part of the submission and judge it — a proposal that claims novelty without having looked for recent preprints has not established novelty.

The proposal is not supposed to contain code. Do not penalize the absence of implementation detail; judge the experimental design.

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
 "Name": "failure_signature_routing",
 "Title": "Transfer Is Predicted by How Tasks Fail, Not by What Tasks Are About: A Routing Study for Textual Prompt Transfer",
 "Short Hypothesis": "When an optimized prompt from a source task is used to warm-start reflective prompt optimization on a new task, the realized transfer gain is predicted by the similarity of the two tasks' *failure-mode signatures* (a cheap, 10-dimensional profile of how a baseline prompt fails), and only weakly by semantic/task-embedding similarity of the SPoT kind. If true, a router built on failure signatures can select a source (or abstain to cold start) and thereby capture most of the small-budget transfer gain while avoiding negative transfer; if the transfer matrix is dominated by a single universally-good source, or if the matrix has too little seed-to-seed reliability to be predictable at all, the hypothesis is refuted — and we measure that reliability explicitly rather than assuming it.",
 "Related Work": "SPoT (Vu et al., 2021) and ATTEMPT establish that soft-prompt transferability is substantial and can be predicted by task embeddings derived from the learned prompt parameters; but soft prompts are model-bound continuous parameters, the study is over classification tasks with full fine-tuning-scale budgets, and the predictor is semantic/parametric task similarity with no notion of failure modes, no budget axis, and no abstention option. 'Exploring and predicting transferability across NLP tasks' (Vu et al., 2020) likewise predicts transfer from TaskEmb/TextEmb similarity for fine-tuning. On the text-prompt side, GEPA (2025), MIPROv2 (2024), OPRO and APE all run cold-start per task and never study which source to transfer from; PromptBreeder evolves operators within a single run. Cross-model prompt transfer work varies the model with the task fixed — the orthogonal axis. What is missing everywhere is (i) a measured, reliability-quantified source×target transfer matrix for *textual* optimized prompts under a matched rollout budget, and (ii) the head-to-head test of failure-signature similarity against semantic similarity as the predictor of that matrix, with a router that can abstain. Our claim is not 'text instead of soft prompts' (a domain swap) but a specific, falsifiable claim about *what feature space transfer lives in* for reflective prompt optimization.",
 "Abstract": "Reflective prompt optimizers are re-run from scratch on every task, and the obvious cheap fix — warm-starting from a prompt optimized elsewhere — is unreliable: sometimes it saves a hundred rollouts, sometimes it is worse than starting cold. We ask whether that variability is predictable before paying for it. We measure a full source×target transfer matrix for textual optimized prompts: eight tasks spanning multi-hop QA, symbolic reasoning, code, and instruction following are each optimized with a reimplemented GEPA, and every domain-scrubbed source prompt is then used to seed a budget-capped optimization run on every other task. We first quantify the matrix's split-half reliability across seeds, which upper-bounds any predictor's achievable correlation and which prior transfer studies do not report. We then test two predictors of the matrix: SPoT-style semantic/task-embedding similarity, and failure-signature similarity — a 10-dimensional distribution over domain-general failure modes obtained by having a judge model label ~50 baseline rollouts per task, at a cost of well under one percent of an optimization run. Our hypothesis is that transfer in this setting is governed by shared failure structure rather than shared subject matter, so failure signatures should predict the matrix substantially better. We close the loop with a leave-one-target-out router that picks a source or abstains to cold start, evaluated against random-source, best-fixed-source, always-cold-start, and oracle-source baselines on small-budget test accuracy, with paired seeds, bootstrap intervals, and a treatment-free null replicate defining the noise floor.",
 "Experiments": "(1) Noise floor and null replicate. Re-score 20 fixed candidate prompts on each task's held-out set 5 times; estimate per-task metric SD. Run two cold-start GEPA runs per task differing only in seed to bound the apparent 'gain' obtainable from nothing.\n(2) Source optimization. Reimplement GEPA (executor: Qwen2.5-7B and 32B served locally; reflector: frontier API model). Optimize 8 tasks (2 BBH clusters, 2 Super-NaturalInstructions clusters, HotpotQA, GSM8K, MBPP, an instruction-following set), 300 rollouts × 3 seeds. Domain-scrub the winning prompt with an LLM (remove task-specific nouns/examples) and verify scrubbing with a source-identification leakage test.\n(3) Transfer matrix. For each of 8×7=56 ordered pairs, seed GEPA on the target with the scrubbed source prompt and run to a 50-rollout cap; record test accuracy of the validation-argmax candidate and the AUC of the budget-accuracy curve at checkpoints 0/10/25/50. Transfer gain Δ(s→t) = warm-start metric − paired cold-start metric on the same seed/splits. Run 3 seeds per cell (168 short runs, each ~50 rollouts — the deliberate reason the cap is 50). Also record zero-shot transfer (checkpoint 0), which is nearly free.\n(4) Reliability. Split seeds into halves; report split-half Spearman reliability of the 56-cell Δ matrix and its bootstrap CI. This is the ceiling for any predictor and is reported before any predictor is fit.\n(5) Failure signatures. For each task, run a fixed seed prompt on 50 dev examples, have a judge model label each failing trace with one of 10 pre-registered domain-general failure modes (format/contract violation, missing decomposition, arithmetic/bookkeeping slip, unsupported claim, instruction omission, premature termination, over-generation, ambiguity mis-resolution, tool/context misuse, spurious refusal); signature = normalized 10-vector. Report inter-judge agreement on 100 double-labeled traces.\n(6) Predictor comparison. Predict Δ(s→t) from: (a) failure-signature similarity (cosine / 1−JS), (b) SPoT-style task-embedding similarity of task descriptions and of dev-set inputs, (c) edit-direction similarity (embedding of the seed→optimized prompt diff on the source vs. target's own first-10-rollout diff), (d) source-prompt zero-shot score on the target (checkpoint-0 transfer, the strongest cheap baseline predictor), (e) source main-effect only. Compare Spearman correlations with attenuation correction by the step-4 reliability; significance by paired bootstrap over cells with target-clustered resampling.\n(7) Router evaluation. Leave-one-target-out: fit the predictor on 7 targets' rows, on the held-out target choose argmax predicted Δ or abstain (predicted Δ ≤ 0) to cold start. Metric: realized test accuracy at 50 rollouts, and rate of negative-transfer incidents (Δ below −noise floor).\n(8) Mechanism separation. Decompose warm-start gain into (i) starting-point quality (checkpoint-0 score), (ii) search direction (fraction of proposed edits with positive validated delta), (iii) output-format compliance measured separately from task accuracy.",
 "Baselines and Ablations": "Baselines for the router: always cold start (wins if transfer is on average useless); random source; best-fixed-source chosen on the 7 training targets (the strong, boring baseline most likely to beat a learned router if one source is universally good — we report it prominently); oracle source (upper bound); zero-shot-score-based routing, which needs no failure taxonomy at all and is the cheapest competitor; SPoT-style semantic-similarity routing. Baselines for the predictor comparison: source main effect + target main effect only (an additive model with no pairwise term — if this explains the matrix, 'similarity' is irrelevant).\nAblations: failure signature computed from 10 vs 50 traces (how cheap can the probe be?); taxonomy coarsened to 3 modes; signature computed on successes as well as failures; scrubbed vs unscrubbed source prompts; warm start as seed candidate vs as an extra Pareto-pool member; second executor model (Llama-3.1-8B) on a 4×3 sub-matrix to test whether the matrix and the predictor are executor-specific.",
 "Falsifiable Predictions": "If the hypothesis holds: (a) the Δ matrix has split-half reliability ≥ 0.5, with a spread of at least 6 test points between best and worst source for a typical target and at least 15% of cells showing negative transfer beyond the noise floor; (b) failure-signature similarity attains Spearman ≈ 0.45–0.65 with Δ (attenuation-corrected), exceeding semantic/task-embedding similarity (predicted ≈ 0.0–0.25) by ≥ 0.2 with a bootstrap CI excluding zero; (c) the leave-one-target-out router recovers ≥ 60% of the oracle-minus-cold-start gain at 50 rollouts and reduces negative-transfer incidents to ≤ 5% versus ≈ 25% for random-source; (d) mechanism: warm-start gain is only partly explained by checkpoint-0 score (partial correlation of failure-signature similarity with Δ remains ≥ 0.3 after controlling for it). Refutation: reliability below ~0.3 (matrix is noise, and we report that as the finding, with the implication that published warm-start results are not reproducible); or semantic similarity matching failure signatures; or best-fixed-source matching the router; or zero-shot score alone explaining Δ entirely, making the failure taxonomy superfluous.",
 "Measurement and Noise Control": "Per task, four disjoint splits: reflection-feedback, validation (candidate selection inside the optimizer), failure-signature probe, and a never-touched test set. Every transfer cell is paired with a cold-start run sharing seed, splits, executor, decode settings, and reflector temperature/seed, so Δ is a within-seed difference; where feasible the reflection proposal stream is replayed to remove proposal randomness. 56 cells × 3 seeds = 168 paired Δ observations; analysis by bootstrap clustered on target task (the unit of generalization) and a mixed model with source and target random effects plus the similarity predictor as a fixed effect. With per-run test SD ≈ 3 points (measured in step 1) and 3 paired seeds per cell, a single cell detects only ≈ 5-point effects, so all cell-level claims are made only in aggregate; the matrix-level correlation analysis with 56 cells detects a Spearman of ≈ 0.27 at 80% power, and predictor differences are tested by paired bootstrap on cell-wise residuals. Any Δ below the treatment-free null-replicate floor is coded as null regardless of p-value, and all reported gains are test scores of validation-argmax candidates in both arms so the winner's curse is shared; we additionally report the validation-to-test selection gap per arm.",
 "Preprint Collision Check": "",
 "Risk Factors and Limitations": "(1) The central risk is a low-reliability matrix; we measure reliability first and, if it is low, the paper becomes a negative result about the reproducibility of warm-start transfer — informative but less attractive. (2) Eight tasks give only 56 cells and 8 clusters for generalization; conclusions are stated at the level of these task clusters. (3) The failure taxonomy is hand-specified and judge-labeled; judge noise and taxonomy misfit are mitigated by inter-judge agreement reporting and a coarsened-taxonomy ablation, but a poor taxonomy could sink the predictor for uninteresting reasons. (4) Zero-shot transfer score is a strong and nearly free competitor predictor; if it wins, the contribution reduces to 'probe cheaply before transferring', which we would report honestly. (5) The 50-rollout cap defines a specific small-budget regime; rankings may differ at larger budgets, so we report checkpoint curves rather than a single number. (6) Domain scrubbing is imperfect; a source-identification leakage test bounds but does not eliminate residual leakage. (7) Frontier-model reflection is rate-limited and nondeterministic; reflection calls are capped (~15 per 50-rollout run, ~3k total) to stay within budget."
}
```

Research area this was proposed for:

# Title: Transferable Prompt Optimization — What Carries Across Domains When the Task Changes

## Keywords
prompt optimization, GEPA, MIPRO, transfer learning, meta-optimization, cross-domain generalization, warm start, reflective search, sample efficiency, ICLR

## TL;DR
Reflective prompt optimizers are re-run from scratch for every new task, and everything they learned about *how to optimize* is thrown away with the prompt. The question is whether there is a domain-general component — the athleticism a baseball player carries into soccer — that can be extracted once and reused, and whether reusing it beats cold-start optimization at a matched search budget even if it never matches a fully domain-specific run.

## Abstract
GEPA, MIPROv2, OPRO, APE and their successors all share a shape: given a task, a metric, and a budget of rollouts, search over prompt text until the validation score stops improving. The artifact they return is a prompt for *that* task. Move to a new domain and the whole search restarts — new rollouts, new reflections, new budget, and often a new metric — while the optimizer itself learns nothing across tasks. This is the practical objection practitioners raise about GEPA-style methods: strong results, but a per-domain cost that has to be paid again every time, which is why they are hard to deploy anywhere the task distribution keeps moving.

The proposal space here is the *transferable* part. A human who has played baseball for twenty years and switches to soccer does not start from zero: running, spatial anticipation, and training habits carry over, while swing mechanics do not. The analogous question for prompt optimization is what plays the role of "athleticism" and what plays the role of "swing mechanics". Candidate transferable units, which a proposal should pick between rather than list:

- **The instruction skeleton** — role framing, output contract, decomposition structure, error-avoidance clauses — as opposed to the domain content that fills it.
- **The reflection heuristics** — the optimizer's learned habits for reading a failure trace and proposing an edit, i.e. transfer at the level of the *optimizer*, not the prompt.
- **The search policy** — where to spend the next rollout, when to stop, which mutation family pays off, learned across tasks and reused as a prior over the search.
- **A failure taxonomy** — a domain-general catalogue of the ways prompted LLM systems fail, used to route edits.

The claim structure that would make this publishable is explicitly a *Pareto* one, not a win: a transferred prior is expected to be **worse than a fully domain-specific optimizer given unlimited budget, but better than cold-start optimization at small budget**, with a crossover point that the paper measures. Framed that way, the contribution is a sample-efficiency curve and a characterization of what transfers, not a leaderboard number.

### Positioning the proposal must survive

An earlier ideation round on the adjacent topic failed review for three repeatable reasons, and proposals here should be built to avoid them from the start:

1. **Crowded neighbourhoods.** Reviewers immediately named prior work for anything resembling uncertainty-gated retrieval or calibration-style bias correction. For transfer specifically, the threatening literature includes: soft-prompt transfer (SPoT, ATTEMPT) and its finding that transferability is predicted by task embeddings; instruction induction and APE; OPRO and other LLM-as-optimizer methods; MIPROv2's joint instruction/demonstration search; PromptBreeder and self-referential prompt evolution, which already evolves mutation operators; task vectors and model merging as a non-prompt route to the same reuse; and multi-task / meta-learned prompt initialization. A proposal must say what these do *not* do — and "they used soft prompts, we use text" or "they did classification, we do agents" is a domain swap, which reviewers scored as a modest delta rather than a contribution.
2. **Effects below the design's own detection threshold.** Several earlier proposals claimed differences smaller than the minimum detectable effect their own sample size supported. Prompt-optimization results are especially exposed here: re-scoring the same candidate on the same held-out set has been measured to move the headline metric by 0.05–0.14, and a treatment-free null replicate reproduced the apparent gain of the best real treatment. Any transfer claim must state the crossover budget with an interval, not a point.
3. **Selection effects.** An optimizer returns the argmax over noisy validation scores, so the returned prompt's advantage is inflated by a winner's curse. A transfer study compares two search procedures and therefore inherits this twice; the design must say how it is handled.

### Questions worth attacking

- What is the smallest artifact that transfers, and can transfer be *predicted* before paying for it — from task similarity, from the failure taxonomy, or from a cheap probe?
- Does transfer help by supplying a better starting point, a better search direction, or merely a better output format? These are separable and the paper should separate them.
- When does the baseball prior hurt? Negative transfer between distant domains is the sharpest falsifiable prediction available here, and finding it is as publishable as finding the gain.
- Is the right object the prompt or the optimizer? A transferred *search policy* that is task-agnostic by construction is a stronger claim than a transferred prompt, and a harder one.
- What does a fair budget axis look like — rollouts, tokens, or wall-clock — and does the ranking of methods change with the choice?

## In scope
- Public multi-task suites where "domain" is well defined and there are enough tasks to hold some out: BIG-bench Hard, Natural Instructions / Super-NaturalInstructions, MMLU subject splits, HotpotQA vs 2WikiMultiHop, code and math benchmarks, agentic suites with tool APIs.
- Small open-weight models (7B–32B), self-hosted, single node, so that many optimization runs are affordable.
- Reimplementation of GEPA/MIPRO-style optimizers as the cold-start baseline.
- Negative and null results, if the measurement is strong enough to make them informative.

## Out of scope
- Private or clinical data; the paper is domain-general.
- Fine-tuning or soft prompts as the primary method — the premise is that the transferred artifact is text and therefore portable across models and APIs. Soft-prompt transfer is a baseline to beat or an ablation, not the method.
- Claims requiring frontier-scale models to reproduce.
- A single-task study, which cannot support any transfer claim.

## Resource constraints
One node, 4×A100 80GB, open-weight models up to ~32B served locally; a frontier API model is available for the reflection/mutation role and for judging, with a total budget of a few hundred dollars. Optimization runs are the expensive unit: assume a few hundred rollouts per optimization run and a few dozen runs in total, and design the transfer matrix and the statistics around that ceiling rather than assuming a large grid.


Review it now.
