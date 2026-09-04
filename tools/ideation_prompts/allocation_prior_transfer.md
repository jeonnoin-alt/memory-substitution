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
 "Name": "allocation_prior_transfer",
 "Title": "What Actually Transfers Is the Noise Model: Cross-Task Priors on Candidate Quality Make Reflective Prompt Optimization Sample-Efficient",
 "Short Hypothesis": "In reflective prompt optimizers (GEPA/MIPROv2), most rollouts are spent *evaluating* proposed candidates, not proposing them. The domain-general, transferable component of an optimization run is not the prompt or its instruction skeleton but the nuisance statistics of the search: the base rate rho at which reflection-proposed edits are genuine improvements and the effect-size distribution of those improvements. These statistics are far more similar across domains than the prompts are; a prior over them, harvested from source-domain runs, turns fixed-minibatch evaluation into sequential accept/reject testing and should beat cold-start optimization at small rollout budgets while converging to it at large budgets. If rho and the effect-size scale are strongly task-idiosyncratic, the hypothesis is refuted and cheap online estimation on the target should suffice.",
 "Related Work": "(All citations unverified; literature search was unavailable.) GEPA (Agrawal et al., 2025) evaluates each reflective mutation on a fixed minibatch and maintains a Pareto front over validation instances; MIPROv2 (Opsahl-Ong et al., 2024) uses TPE over instruction/demonstration candidates with fixed-size minibatch evaluation; OPRO and APE re-score a fixed batch per candidate. All spend evaluation budget by a hand-set schedule, and all restart per task. Racing and bandit methods (Hoeffding races, irace, Successive Halving/Hyperband) adapt evaluation budget within a run but assume no cross-task prior and are typically uninformative at the start, which is exactly where prompt-optimization budgets live. Meta/transfer Bayesian optimization (e.g., transfer surrogates, ranking-weighted GP ensembles) transfers across tasks but requires a shared, low-dimensional, parametric search space; prompt text has no such shared parameterization across domains, which is precisely why prompt-optimization transfer has focused on transferring artifacts (SPoT/ATTEMPT soft prompts; instruction induction; skeleton warm starts). PromptBreeder evolves mutation operators but only within one run. Our claim is a conceptual dissociation none of these make: the search space does not transfer, but the *nuisance statistics over the search* do, and transferring them is model- and domain-portable because they are two scalars plus a shape, not text. We also test this head-to-head against textual transfer (skeleton warm start, harvested reflection heuristics) at matched budget, and test whether the two compose.",
 "Abstract": "Reflective prompt optimizers restart from scratch on every new task, and prior attempts at transfer have moved text: an optimized prompt, an instruction skeleton, a set of reflection heuristics. We argue the most reliably transferable object is statistical rather than textual. In any GEPA/MIPRO-style run, the optimizer repeatedly asks 'is this proposed candidate better than its parent?' and answers it by spending rollouts on a fixed-size minibatch. The efficiency of that answer is governed by two quantities: rho, the fraction of LLM-proposed edits that are true improvements, and the distribution of improvement magnitudes. We show these quantities are substantially more stable across domains than prompts are, and we exploit them: we fit a hierarchical prior over (rho, effect size) from optimization runs on source tasks, then, on held-out target domains, replace fixed-minibatch evaluation with a sequential accept/reject test that uses the transferred prior as its starting belief while leaving the proposal and selection machinery untouched. Because the transferred object is three numbers, it is trivially portable across executor models and APIs. We evaluate on six held-out target tasks (multi-hop QA, symbolic reasoning, code, instruction following) with 7B-32B open-weight executors, against cold-start GEPA, uninformative racing, online-estimated priors, an oracle target-fit prior, and textual-transfer baselines. The claim is Pareto and falsifiable: gains concentrated at small budgets, vanishing by convergence, with a crossover budget reported as a bootstrap interval. We additionally report the validation-to-test selection gap, predicting that principled sequential testing reduces the winner's curse that inflates all reported prompt-optimization gains.",
 "Experiments": "(1) Noise-floor and null-replicate calibration. Re-score 20 fixed candidate prompts on the same held-out set 5x per task; measure metric SD. Run two cold-start GEPA runs differing only in seed to bound the apparent 'gain' obtainable from nothing. All later thresholds and 'null' declarations reference this floor.\n(2) Source harvesting and the central measurement. Run a reimplemented GEPA (executor Qwen2.5-7B/32B local; reflector = frontier API model) on 6 source tasks (BBH clusters, Super-NaturalInstructions clusters, 2WikiMultiHop), 300 rollouts x 3 seeds. For every proposed candidate, additionally score it on a large held-out probe set (400 examples) to obtain a near-ground-truth delta vs parent. This yields, per task, the empirical distribution of true deltas: rho = P(delta>0) and the positive-part effect-size distribution. Report between-task vs within-task variance of rho and effect scale (ICC), plus leave-one-task-out predictive log-likelihood of a pooled hierarchical prior against (a) an uninformative prior and (b) the task's own oracle fit. This test alone decides the hypothesis independent of downstream gains.\n(3) Method (TAP: Transferred Allocation Prior). Keep GEPA's proposal, reflection, and Pareto selection exactly as is. Replace fixed-minibatch candidate evaluation with sequential evaluation: after each block of 4 examples, compute the posterior P(delta>0) under a spike-and-slab prior (spike weight 1-rho, slab = fitted effect-size distribution) with a binomial/normal likelihood; accept if P>tau_a, reject if P<tau_r, else continue up to a cap. rho and the slab are set by the leave-one-domain-out pooled prior; nothing else changes.\n(4) Target evaluation. 6 held-out target tasks (HotpotQA, GSM8K, MBPP/HumanEval+, an instruction-following set, 2 unseen BBH clusters) x 5 seeds. Budget checkpoints at 25/50/100/200/300 rollouts on both a rollout axis and a token axis; at each checkpoint report test accuracy of the current validation-argmax candidate, AUC of the budget-accuracy curve, and the crossover budget with bootstrap CI.\n(5) Mechanism decomposition. Separate three possible sources of gain: (a) fewer rollouts wasted on doomed candidates (measure mean rollouts spent per rejected candidate), (b) more candidates proposed per budget (count), (c) fewer false accepts polluting the Pareto pool (measure precision of accept decisions against probe-set ground truth).\n(6) Composition and head-to-head with textual transfer. Run skeleton warm start and a harvested reflection-heuristic playbook alone, TAP alone, and both together; test additivity (interaction term in the mixed model).\n(7) Negative-transfer probe. Fit the prior from a single distant source domain (symbolic only) and apply to code and QA; predict TAP degrades gracefully (bounded by uninformative racing) whereas skeleton warm start can go negative.",
 "Baselines and Ablations": "Baselines: (i) cold-start GEPA with its default fixed minibatch at matched rollouts (main competitor; wins at large budget by construction); (ii) MIPROv2 cold start; (iii) uninformative racing / Successive Halving with the same sequential machinery but a flat prior - isolates the value of *transfer* from the value of *adaptivity*, and is the baseline most likely to erase the contribution; (iv) online prior: identical to TAP but rho and effect scale estimated from the target run's own first K=15 candidates (the cheap alternative that could win outright; TAP is only interesting if it wins before this warms up); (v) oracle prior fit on the target's full probe-set deltas (upper bound); (vi) skeleton warm start and (vii) reflection-heuristic playbook as textual-transfer references.\nAblations: transfer rho only vs effect-size distribution only vs both; single-source vs six-source pooled prior; tau_a/tau_r sensitivity; block size; cap on per-candidate examples; TAP grafted onto MIPROv2 instead of GEPA (does the mechanism transfer across optimizers?); second executor model (Llama-3.1-8B) at reduced seeds to test model-portability of the transferred scalars.",
 "Falsifiable Predictions": "If the hypothesis holds: (a) between-task ICC of rho is low (pooled prior's leave-one-task-out predictive log-likelihood beats the uninformative prior by a clear margin and comes within ~10% of the oracle fit); (b) at 50 rollouts TAP beats cold-start GEPA by 2-5 test points averaged over 6 targets (paired per seed) and beats uninformative racing by 1-3 points, with both gaps shrinking below the noise floor by 300 rollouts; crossover budget 100-250 rollouts with a bootstrap CI narrower than the checkpoint spacing; (c) TAP beats the online-prior baseline over roughly the first 40-60 rollouts and ties thereafter; (d) validation-to-test selection gap shrinks by >=30% relative under TAP; (e) mechanism: >=60% of the gain traceable to rollouts saved on rejected candidates, not to accept precision; (f) TAP never underperforms cold-start by more than the noise floor even from a distant single source, while skeleton warm start loses 2-5 points on distant pairs. Refutation: rho and effect scale vary strongly by task (high ICC, pooled prior no better than uninformative); or uninformative racing matches TAP at all budgets (adaptivity, not transfer, is the whole story); or the online-prior baseline matches TAP from rollout 1; or gains are within the null-replicate floor.",
 "Measurement and Noise Control": "Four-way split per task: feedback set (traces for reflection), validation set (candidate selection inside the optimizer), a large probe set used only offline to establish near-ground-truth deltas for prior fitting and accept-precision analysis, and a never-touched test set for reporting. All methods share seeds, splits, executor model and decode settings, and reflector temperature/seed; the reflection proposal stream is *replayed identically* across evaluation-policy conditions where possible, so the arms differ only in allocation (a strictly paired design that removes proposal randomness). 6 targets x 5 seeds = 30 paired observations per comparison; analysis by paired bootstrap over (task, seed) plus a linear mixed model with task random effects and budget as a factor. With per-run test SD ~3 points measured in step 1 and n=30 paired, the design detects a 1.5-point mean paired difference at 80% power; any effect below the treatment-free null-replicate floor is reported as null regardless of p-value. We report the validation-to-test selection gap explicitly for every arm so winner's-curse inflation is quantified rather than hidden, and crossover budgets are always reported as bootstrap intervals.",
 "Preprint Collision Check": "",
 "Risk Factors and Limitations": "(1) For binary metrics, per-example variance is analytic, so only rho and the effect-size shape are genuinely transferable; if these turn out to be near-universal, the contribution becomes 'use a sensible fixed prior' - still useful but weaker, and we would report it as such. (2) The online-prior baseline may warm up within ~10 candidates, compressing the transfer advantage to a very small budget window; we pre-register this window as the crossover measurement rather than claiming a global win. (3) Probe-set deltas are themselves noisy; we use 400 examples and report probe-set SD alongside all prior fits. (4) Six target tasks is a narrow basis for 'domain' claims; conclusions will be stated at the level of the specific task clusters. (5) GEPA's Pareto-front machinery interacts with accept/reject in ways that may not isolate cleanly; the MIPROv2 graft is included to check the mechanism is not optimizer-specific. (6) Frontier-model reflection is nondeterministic and rate-limited; capping reflection calls (~30/run) limits the number of harvested candidates per task."
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
