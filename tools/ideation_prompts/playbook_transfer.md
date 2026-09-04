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
 "Name": "playbook_transfer",
 "Title": "Transfer the Optimizer, Not the Prompt: A Domain-General Failure→Edit Playbook for Sample-Efficient Reflective Prompt Optimization",
 "Short Hypothesis": "What transfers across domains in reflective prompt optimization is not the optimized prompt (its instruction skeleton), but the optimizer's accumulated diagnostic knowledge — a domain-scrubbed catalogue mapping failure symptoms to edit operators. Injecting such a playbook, harvested from source-domain GEPA runs, into the reflection step of a target-domain run should beat cold-start GEPA at small rollout budgets and never induce negative transfer, whereas warm-starting from a transferred prompt helps only within-domain and hurts across distant domains.",
 "Related Work": "GEPA (Agrawal et al., 2025) and MIPROv2 run stateless per task; nothing is carried across tasks. PromptBreeder evolves mutation prompts but only within a single task's run, so its meta-level knowledge dies with the run. REMO (Wu & Qu, 2025) adds a cross-run 'mistake notebook' to TextGrad, but evaluates on a single benchmark (GSM8K), reuses memory within the same domain, and makes no transfer or sample-efficiency claim; it also never separates the value of the memory's content from the value of merely conditioning the reflector on extra text. PromptBridge and cross-tier transfer work (Oved et al., 2026) study transfer across *models* with the task fixed — the orthogonal axis. SPoT/ATTEMPT show soft-prompt transferability predicted by task embeddings, but soft prompts are model-bound parameters, not portable text, and transfer the *initialization*, not the search knowledge. Instruction induction/APE transfer nothing. Our contribution is the explicit dissociation, on the same benchmark suite and matched budgets, between transferring the artifact (prompt skeleton) and transferring the search knowledge (failure→edit playbook), with a Pareto sample-efficiency curve, a stated crossover budget with an interval, and a leakage-controlled construction of the transferred object.",
 "Abstract": "Reflective prompt optimizers such as GEPA and MIPROv2 return a prompt for one task and discard everything they learned about how to optimize; every new domain pays the full rollout bill again. We ask which component of an optimization run is domain-general, and test a specific answer: the optimizer's diagnostic knowledge — a catalogue of failure symptoms and the edits that fixed them — transfers, while the optimized prompt text does not. We build the catalogue by running GEPA on six source tasks, logging every (failure trace, proposed edit, validated score delta) triple, keeping only edits whose delta exceeds an empirically measured re-scoring noise floor, and distilling surviving reflections into short domain-scrubbed SYMPTOM/EDIT rules; scrubbing is verified by a leakage test in which a held-out LLM must fail to identify the source task from a rule. At target time the playbook is retrieved by symptom match and injected into the reflection step only — the search algorithm and budget are otherwise unchanged. We evaluate on six held-out target tasks spanning multi-hop QA, symbolic reasoning, code and instruction-following, with 7B-32B open-weight executors, against cold-start GEPA, prompt-skeleton warm start, soft-prompt-style transfer, and a shuffled-playbook control that holds the added tokens constant. The claim is Pareto, not a leaderboard win: playbook transfer should dominate at small budgets and converge to cold-start at large ones, and we report the crossover budget with a bootstrap interval. We further test whether cheap zero-shot failure-mode overlap predicts transfer benefit before it is paid for.",
 "Experiments": "(1) Noise-floor calibration: re-score 20 fixed candidate prompts on the same held-out set 5 times each; estimate SD of the headline metric per task; run a treatment-free null replicate (two cold-start GEPA runs differing only in seed) to bound the apparent 'gain' obtainable from nothing. All later thresholds use this floor.\n(2) Source harvesting: run a reimplemented GEPA (reflection/mutation by a frontier API model; executor = Qwen2.5-7B/32B served locally) on 6 source tasks (BBH subsets, Super-NaturalInstructions clusters, 2WikiMultiHop), 300 rollouts each, 3 seeds. Log parent prompt, failing traces, reflection text, child prompt, val delta.\n(3) Playbook distillation: keep edits with val delta > 2x the task's noise SD; LLM-cluster the associated reflections into failure modes; write each as a <=60-token SYMPTOM/EDIT rule; scrub domain nouns. Leakage test: a held-out LLM given a rule must identify its source task at near chance (<= 1/6 + noise); rules that fail are re-scrubbed or dropped. Expect 20-60 rules.\n(4) Target-time transfer: on 6 held-out target tasks (HotpotQA, GSM8K/AIME-style math, HumanEval+/MBPP, IFBench-style instruction following, 2 BBH tasks from unseen clusters), run GEPA with the playbook retrieved (top-3 by embedding match between current failure summary and rule symptoms) and prepended to the reflection prompt. 5 seeds x 6 tasks x methods. Budget checkpoints at 25/50/100/200/300 rollouts; record test score of the val-argmax candidate at each checkpoint. Report both rollout and token axes.\n(5) Mechanism decomposition: does transfer supply (a) a better starting point, (b) a better search direction, or (c) output-format compliance? Measure (a) by initial-prompt score, (b) by fraction of proposed edits with positive validated delta and by edit-acceptance rate per reflection call, (c) by a format-compliance-only metric held separate from task accuracy.\n(6) Negative transfer probe: deliberately transfer from a single distant source domain (e.g., only symbolic BBH) to code and to multi-hop QA, for both playbook and prompt-skeleton conditions.\n(7) Predictability: compute zero-shot failure-mode distribution overlap (JS divergence over the taxonomy from 30 baseline rollouts per task) between source pool and target; correlate with realized gain at 50 rollouts (Spearman over 6 targets x 3 source pools = 18 points).\nMetrics: task test accuracy/F1 at each budget checkpoint; area under the budget-accuracy curve; crossover budget; edit-acceptance rate; val-to-test selection gap (winner's curse magnitude).",
 "Baselines and Ablations": "Baselines: (i) cold-start GEPA at matched rollouts and matched reflection-token count — the main competitor and the one most likely to catch up at large budget; (ii) prompt-skeleton warm start (best source prompt, domain nouns scrubbed, as GEPA's seed candidate) — the obvious cheap alternative that could beat us within-domain; (iii) MIPROv2 cold start; (iv) static 'good prompting practices' checklist written by hand (no source runs) injected into reflection — if this matches the harvested playbook, the harvesting contributes nothing; (v) soft-prompt transfer (SPoT-style) on the classification-shaped subset, as an out-of-family reference.\nAblations: shuffled playbook (rules retrieved by anti-matching symptoms, identical token count) isolating content from conditioning; full-dump vs retrieved playbook; playbook from one source domain vs six; playbook with score deltas stripped (does the validated-delta filter matter?) vs unfiltered reflections; playbook injected into candidate proposal only vs into candidate selection only; playbook + skeleton combined.",
 "Falsifiable Predictions": "If the hypothesis holds: at 50 rollouts, playbook transfer beats cold-start GEPA by 3-8 points averaged over 6 target tasks (paired, per-seed), with the gap shrinking to <=1.5 points (within the noise floor) by 300 rollouts; crossover budget estimated at 120-250 rollouts with a bootstrap CI narrower than the checkpoint spacing. Prompt-skeleton warm start beats cold-start only when source and target share a domain and *loses* 2-5 points on distant pairs (negative transfer), while playbook transfer is never worse than cold-start by more than the noise floor on any target. Mechanism: playbook gains should come mostly from edit-acceptance rate (predicted +30-60% relative), not from initial-prompt score. Refutation: if the shuffled-playbook control or the hand-written checklist matches the harvested playbook, the claim that harvested cross-task knowledge transfers is dead; if playbook gains are fully explained by initial-prompt score or by format compliance, the 'search knowledge' framing is wrong; if playbook transfer also shows negative transfer on distant pairs, the claimed dissociation between artifact and search knowledge fails.",
 "Measurement and Noise Control": "Three-way split per task: optimization-feedback set, validation set for candidate selection, and a never-touched test set for reporting; we additionally report the val-to-test selection gap so the winner's curse is quantified rather than hidden, and all method comparisons are made on test scores of the val-argmax candidate (both arms inherit the same selection bias). Fully paired design: methods share seeds, data splits, executor model, and reflection-model temperature/seed; comparisons are per (task, seed) differences. 6 target tasks x 5 seeds = 30 paired observations per comparison; analysis by paired bootstrap over task-seed pairs plus a linear mixed model with task random effects. With per-run test-score SD of ~3 points (measured in step 1) and n=30 paired, the design detects a 1.5-point mean paired difference at 80% power; effects below the null-replicate floor from step 1 will be reported as null regardless of p-value. Crossover budget is reported as a bootstrap interval over task-seed resamples, never as a point.",
 "Preprint Collision Check": "",
 "Risk Factors and Limitations": "(1) The playbook may be indistinguishable from generic prompt-engineering advice; the hand-written-checklist baseline is designed to expose this, and a null there is itself an informative (if less exciting) result. (2) Domain scrubbing may be imperfect — mitigated by the source-identification leakage test, but subtle stylistic leakage remains possible. (3) Frontier-model reflection is nondeterministic and rate-limited; we cap reflection calls at ~30/run (~3k total) to stay in budget, which limits how many source tasks we can harvest. (4) Six target tasks is a small basis for claims about 'domains'; we will state transfer conclusions at the level of the specific task clusters used. (5) Results may be sensitive to the executor model; we replicate the headline comparison on a second executor (Llama-3.1-8B) at reduced seeds. (6) Gains may vanish if GEPA's own reflection prompt is already near-optimal for these tasks, in which case the sample-efficiency curve, not the endpoint, carries the paper."
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
