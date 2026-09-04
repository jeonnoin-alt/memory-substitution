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
 "Name": "meta_prompt_generalization",
 "Title": "How Many Tasks Does It Take to Optimize an Optimizer? Meta-Generalization of Learned Reflection Prompts",
 "Short Hypothesis": "The transferable component of a reflective prompt optimizer is its reflection meta-prompt (the instructions that turn failure traces into candidate edits), and it can be improved by outer-loop search — but only if the outer loop is run over enough source tasks. We predict a measurable meta-generalization gap that shrinks monotonically with the number of source tasks: a meta-prompt searched on 1 task overfits and gives no (or negative) benefit on held-out domains, while one searched on ~4-8 diverse tasks yields a small-budget gain on held-out domains that decays to zero by convergence. If held-out gain is flat in the number of source tasks, or if meta-search never beats the default meta-prompt on held-out tasks, the hypothesis is refuted.",
 "Related Work": "PromptBreeder (Fernando et al., 2023) is self-referential — it evolves mutation prompts — but does so *inside a single task's run*, reports task scores rather than meta-generalization, and never evaluates an evolved mutation prompt on a held-out task. GEPA (Agrawal et al., 2025) and MIPROv2 (Opsahl-Ong et al., 2024) fix the reflection/proposal meta-prompt by hand and restart per task. OPRO/APE optimize task prompts only. REMO (Wu & Qu, 2025) adds a cross-run 'mistake notebook' plus an LLM meta-controller to TextGrad, but evaluates on a single benchmark (GSM8K), reuses memory within one domain, provides no held-out-domain evaluation, and never varies the number of source tasks. Classical meta-learning (MAML and successors) has established that meta-overfitting is governed by task diversity, but this has never been measured for a *textual*, model-portable meta-artifact where the meta-parameter is a natural-language instruction rather than a weight vector. Our contribution is the measurement none of these make: the meta-generalization curve of a searched reflection meta-prompt as a function of source-task count and diversity, plus a Pareto crossover-budget characterization on held-out domains, against a default-meta-prompt cold start and a harvested-rules alternative.",
 "Abstract": "Reflective prompt optimizers such as GEPA and MIPROv2 spend hundreds of rollouts per task and return a prompt; the optimizer itself — in particular the hand-written meta-prompt that instructs an LLM to read failure traces and propose edits — is never learned and never carries anything across tasks. We treat that meta-prompt as the transferable artifact and ask a question that transfer proposals in this area usually skip: how many source tasks does it take before an optimized optimizer generalizes? We run an outer reflective search over reflection meta-prompts, where evaluating one meta-candidate means executing short inner GEPA runs on K source tasks and scoring the resulting task prompts, for K in {1, 2, 4, 8}. We then evaluate each searched meta-prompt on six held-out target tasks spanning multi-hop QA, symbolic reasoning, code, and instruction following, with 7B-32B open-weight executors, against the default GEPA meta-prompt, a hand-written 'good reflection practice' meta-prompt of matched length, a harvested failure-to-edit rule list, and an oracle meta-prompt searched on the target itself. The central object is the meta-generalization gap — source-task gain minus held-out-task gain — as a function of K, reported with bootstrap intervals against a measured re-scoring noise floor and a treatment-free null meta-replicate. We further decompose any held-out gain into three separable mechanisms (better initial candidates, higher edit acceptance rate, better output-contract compliance) and test whether a meta-prompt searched with one executor transfers to another.",
 "Experiments": "(1) Noise floor. Re-score 20 fixed task prompts on each task's held-out set 5x; estimate per-task metric SD. Run two inner GEPA runs per task differing only in seed to bound the apparent gain obtainable from nothing. Additionally run a *meta-level* null replicate: two outer searches with identical settings but different seeds, to bound apparent meta-search gains.\n(2) Setup. Reimplement GEPA. Executor: Qwen2.5-7B-Instruct served with vLLM (headline), Llama-3.1-8B for the portability replication. Inner reflector: Qwen2.5-32B served locally (keeps cost tractable). Outer meta-mutator: frontier API model (a few hundred calls total).\n(3) Outer loop. Meta-candidate = the reflection meta-prompt text (instructions given to the reflector: what to attend to in traces, how to phrase an edit, what to avoid). Outer search = the same reflective mutation loop applied one level up: propose a mutated meta-prompt conditioned on logs of which inner edits succeeded/failed, evaluate it by running inner GEPA (60 rollouts) on K source tasks x 2 inner seeds, score = mean test gain over inner cold-start-with-default-meta-prompt on paired seeds. Budget: 20 meta-candidates per outer run.\n(4) The scaling experiment. Source pool = 8 tasks (2 BBH clusters, 2 Super-NaturalInstructions clusters, HotpotQA, GSM8K, MBPP, an instruction-following set). For K in {1,2,4,8} run outer searches (3 different random source subsets each for K<8, 3 seeds for K=8) yielding ~12 searched meta-prompts. Record source-task gain (in-sample) and held-out gain.\n(5) Held-out evaluation. 6 target tasks disjoint from the source pool. Run inner GEPA with each searched meta-prompt vs the default, 5 seeds, budget checkpoints at 25/50/100/200/300 rollouts on both rollout and token axes; report test score of the validation-argmax candidate, AUC of the budget curve, and crossover budget with bootstrap CI. Primary plot: held-out gain vs K, with source gain overlaid (the meta-generalization gap).\n(6) Mechanism decomposition. (a) initial-candidate quality (score of first proposed edit), (b) edit acceptance rate = fraction of proposed edits with validated positive delta, (c) output-contract compliance scored separately from task accuracy. Predict the gain is dominated by (b).\n(7) Leakage/abstraction check. A held-out LLM given a searched meta-prompt must fail to identify its source tasks above chance; also inspect and report whether searched meta-prompts become more abstract (fewer domain nouns) as K grows — a mechanistic signature of meta-generalization.\n(8) Executor portability. Re-run held-out evaluation of the K=8 meta-prompt with Llama-3.1-8B as executor at reduced seeds.",
 "Baselines and Ablations": "Baselines: (i) default GEPA meta-prompt cold start at matched rollouts and matched meta-prompt token count — the main competitor, likely to tie at large budget by construction; (ii) hand-written 'good reflection practice' meta-prompt written without running any search, length-matched — the baseline most likely to erase the contribution, since it tests whether search was needed; (iii) harvested failure-to-edit rule list appended to the default meta-prompt (no search, harvest-only); (iv) random/unsearched mutated meta-prompts (the best of 20 random mutations scored on nothing) — isolates search from mere variation; (v) oracle meta-prompt searched directly on the target task (upper bound); (vi) MIPROv2 cold start as an out-of-family reference.\nAblations: K=1 vs 2 vs 4 vs 8 (the core ablation); diverse vs homogeneous source subsets at fixed K=4 (does diversity or count drive it?); meta-prompt truncated to its abstract clauses vs its concrete clauses; meta-prompt applied to candidate proposal only vs to feedback summarization only; inner budget used during outer search (30 vs 60 rollouts) to test whether meta-prompts are budget-regime-specific; second executor.",
 "Falsifiable Predictions": "If the hypothesis holds: (a) source-task gain is large at every K (3-8 points) but held-out gain rises monotonically with K — approximately 0 or negative (-2 to 0 points) at K=1, +1 to +3 at K=4, +2 to +5 at K=8, measured at the 50-rollout checkpoint, with bootstrap CIs excluding zero for K>=4; (b) the meta-generalization gap (source minus held-out gain) shrinks by at least half from K=1 to K=8; (c) held-out gains decay to within the noise floor (<=1.5 points) by 300 rollouts, giving a crossover budget of 100-250 rollouts with a bootstrap interval narrower than the checkpoint spacing; (d) >=50% of the held-out gain is attributable to edit acceptance rate rather than to initial-candidate quality or format compliance; (e) searched meta-prompts contain fewer domain-specific nouns as K increases. Refutation: held-out gain is flat in K (meta-overfitting is not the limiting factor and the scaling story is wrong); or the hand-written practice meta-prompt matches the K=8 searched one (search is unnecessary); or the default meta-prompt is never beaten on held-out tasks beyond the meta-level null-replicate floor (the reflection meta-prompt is not a useful transfer locus at all — a clean negative result we would report).",
 "Measurement and Noise Control": "Four disjoint splits per task: inner-feedback, inner-validation (candidate selection), a meta-scoring set used only in the outer loop for source tasks, and a never-touched test set for all reported numbers. Held-out target tasks are never seen by any outer search. Fully paired design: each searched meta-prompt and the default meta-prompt are run with identical inner seeds, splits, executor, decode settings, and reflector temperature/seed, so all comparisons are within-seed differences; where feasible we replay identical failure-trace samples across arms. Held-out comparison: 6 targets x 5 seeds = 30 paired observations per meta-prompt, analyzed with a paired bootstrap clustered on target task and a linear mixed model with task random effects and K as a fixed effect (12 searched meta-prompts as the meta-level unit, so K-effects are tested with meta-prompt as a random effect to avoid pseudo-replication). With per-run test SD ~3 points (measured in step 1) and n=30 paired, the design detects a 1.5-point mean paired difference at 80% power; the K-trend test, with 3 meta-prompts per K, detects a slope corresponding to a ~2-point difference between K=1 and K=8. Any effect below the treatment-free null floor (both inner and meta level) is reported as null regardless of p-value. All arms report test scores of validation-argmax candidates and we additionally report the validation-to-test selection gap per arm, so winner's-curse inflation is quantified rather than hidden; crossover budgets are always intervals.",
 "Preprint Collision Check": "",
 "Risk Factors and Limitations": "(1) Outer-loop evaluation is noisy because each meta-candidate score is an average over noisy inner runs; with 20 meta-candidates the outer search may mostly select noise, which the meta-level null replicate is designed to expose — and which, if true, is itself a publishable caution about self-referential prompt optimization. (2) Compute: ~100k inner rollouts total on a 7B/8B executor with vLLM plus a local 32B reflector; this is the binding constraint and is why inner runs during outer search are capped at 60 rollouts, which risks producing meta-prompts tuned to a small-budget regime (tested by the inner-budget ablation). (3) Only 8 source and 6 target tasks, so 'domain' claims are stated at the level of these clusters. (4) The default GEPA meta-prompt may already be near-optimal, leaving little headroom; in that case the paper's contribution is the meta-generalization curve and the negative result. (5) Meta-prompts may be executor- or reflector-specific; only one reduced replication is affordable. (6) The hand-written practice baseline could match the searched meta-prompt, reducing the contribution to a characterization of when search is worth it — we would report that honestly."
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
