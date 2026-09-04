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
 "Name": "clause_level_portability",
 "Title": "Prompt Optimizers Discover Two Kinds of Text: A Clause-Level Attribution Study of What Transfers Across Domains",
 "Short Hypothesis": "The gain produced by a reflective prompt optimizer decomposes at the level of individual clauses into a task-specific part (content, exemplars, domain vocabulary) whose value is confined to the source task, and a domain-general part (output contracts, error-avoidance/edge-case clauses, procedural decomposition) whose value transfers. We predict that a clause's contribution on its source task is a poor predictor of its cross-task contribution, while a cheap clause *type* label is a good one, and that a zero-rollout library of high-portability clauses recovers a substantial, measurable fraction of cold-start GEPA's small-budget gain on held-out domains.",
 "Related Work": "(All citations unverified; literature search backend was unavailable.) GEPA (Agrawal et al., 2025), MIPROv2 (Opsahl-Ong et al., 2024), OPRO (Yang et al., 2023) and APE (Zhou et al., 2022) return a single monolithic prompt string per task and report only whole-prompt scores; none attributes the gain to parts of the returned prompt, and none measures whether those parts are portable. OPRO's 'Take a deep breath' anecdote and follow-up work on prompt sensitivity/irrelevant-token effects hint that some discovered text is content-free, but this is anecdotal rather than a causal decomposition. SPoT/ATTEMPT (Vu et al., 2021; Asai et al., 2022) transfer soft prompts as indivisible model-bound parameter blocks and predict transfer from task embeddings; a soft prompt has no clause structure to attribute, so the question we ask cannot be posed there. Instruction-induction and prompt-component 'best practice' papers hand-write component taxonomies and test them a priori; we instead *harvest* components from what an optimizer actually discovered and measure their portability causally. Work on cross-model prompt transfer varies the model with the task fixed — the orthogonal axis. The new object here is a clause×target portability matrix estimated by causal insertion/deletion, and the resulting claim that the transferable component of prompt optimization is a small, reusable, model-portable text library rather than a whole prompt or a search procedure.",
 "Abstract": "Reflective prompt optimizers return one prompt per task, and every deployment to a new domain pays the full rollout bill again. We ask a more basic question than 'does the prompt transfer?': which *parts* of it do. We optimize eight tasks spanning multi-hop QA, symbolic reasoning, code and instruction following with a reimplemented GEPA, then segment each returned prompt into atomic clauses and label each with a seven-way type taxonomy (role framing, output contract, task-specific content, procedural decomposition, error-avoidance/edge case, exemplar, motivational filler). We estimate two quantities per clause: its causal contribution on its own task, via leave-one-clause-out and random-subset regression, and its causal contribution when inserted into the baseline prompt of each of the seven other tasks. This yields a clause×target portability matrix. Our central hypothesis is a dissociation: source contribution and cross-task contribution are weakly correlated, because the largest source contributions come from task-specific content clauses whose transfer is null or negative, while smaller but reliably positive transfer comes from output-contract and error-avoidance clauses. We then close the loop with a zero-rollout baseline: assemble the top-ranked portable clauses into a generic prefix, apply it to held-out tasks with no target optimization at all, and report the number of cold-start GEPA rollouts it is worth, with a bootstrap interval. Because most measurements are scoring passes rather than optimization runs, the study is affordable on one node, and all claims are referenced against a measured re-scoring noise floor and a treatment-free null replicate.",
 "Experiments": "(1) Noise floor. Re-score 20 fixed prompts on each task's held-out set 5 times; estimate per-task metric SD under decode nondeterminism and sampling of the eval set. Run two cold-start GEPA runs per task differing only in seed to bound the apparent 'gain' obtainable from nothing. Every later threshold references this floor.\n(2) Source optimization. Reimplement GEPA (executor: Qwen2.5-7B-Instruct locally, replicated on Qwen2.5-32B at reduced scale; reflector: frontier API model). Optimize 8 tasks (2 BBH clusters, 2 Super-NaturalInstructions clusters, HotpotQA, GSM8K, MBPP, an instruction-following set), 300 rollouts × 3 seeds. Keep the validation-argmax prompt per seed.\n(3) Clause segmentation and typing. An LLM splits each final prompt into atomic clauses (target 6–18 per prompt; sentence/bullet granularity, deterministic post-check that concatenation reproduces the original). Two independent LLM judges plus a human spot-check assign each clause one of 7 types; report inter-judge agreement (Cohen's kappa) on all clauses and human agreement on a 100-clause sample. Expect ~100–300 clauses total per seed pool.\n(4) Within-source attribution. Per task: (a) leave-one-clause-out, scoring the ablated prompt on a 200-example held-out set; (b) random-subset estimation — sample 80 random clause subsets, score each, and regress score on clause-presence indicators to get shapley-style marginals with standard errors. Total ~8 tasks × ~100 evaluations × 200 examples ≈ 160k generations, batched with vLLM.\n(5) Cross-task portability. For each of the 8 targets, take each clause from the other 7 tasks' prompts, insert it into the target's fixed baseline prompt (position controlled: appended in a fixed slot), and score on the target's held-out set. This is the clause×target matrix. To control cost, first pool clauses by near-duplicate merging and cap at ~120 unique clauses; 120 × 7 targets × 200 examples ≈ 168k generations. Also score a length-matched filler control clause and a semantically-inverted variant of each clause (a 'sham clause' saying the opposite) to distinguish content from mere token addition.\n(6) The dissociation test. Correlate each clause's source contribution with its mean cross-task contribution (Spearman, attenuation-corrected using split-half reliability of both quantities across seeds). Fit a mixed model predicting cross-task contribution from clause type, controlling for source contribution and clause length.\n(7) Zero-rollout clause library. Leave-one-target-out: rank clauses by mean measured portability on the 7 training targets, greedily assemble a prefix (stopping at a token cap) with redundancy filtering, apply to the held-out target with zero optimization. Compare against the cold-start GEPA budget curve at 0/10/25/50/100/300 rollouts on the same target and report the 'rollout equivalence' with a bootstrap interval. Also test library-as-seed: initialize GEPA with the library prefix and compare its budget curve to cold start.\n(8) Mechanism split. Report task accuracy and output-format compliance as separate metrics throughout, so we can say whether portable clauses buy correctness or only contract adherence.",
 "Baselines and Ablations": "Baselines: (i) cold-start GEPA budget curve on each target — the reference the library must be priced against, and the winner at large budget by construction; (ii) whole-prompt warm start / zero-shot transfer of the best source prompt (the obvious cheap alternative; if it matches the clause library, clause-level decomposition adds nothing); (iii) a hand-written generic prompt-engineering checklist of matched token length, written without seeing any optimization run — the baseline most likely to beat us, since it tests whether harvesting was necessary at all; (iv) length-matched neutral filler and (v) sham (semantically inverted) clauses, controlling for token count and for 'any extra structure helps'; (vi) random clauses drawn from the library instead of top-portability ones; (vii) portability-oracle selection on the held-out target (upper bound).\nAblations: portability estimated from 1 vs 7 source tasks; clause type restricted to a single type at a time (contract-only, error-avoidance-only, content-only libraries) to see which type carries the effect; insertion position (prefix vs suffix vs interleaved); domain-scrubbed vs raw clauses, with a source-identification leakage test; second executor (Llama-3.1-8B) on a 4×4 sub-matrix to test whether portability rankings are executor-specific; segmentation granularity (sentence vs bullet vs paragraph).",
 "Falsifiable Predictions": "If the hypothesis holds: (a) within-source contributions are dominated by a few clauses, with task-specific-content clauses accounting for ≥ 50% of total source gain; (b) the Spearman correlation between source contribution and mean cross-task contribution is low, ≈ 0.0–0.3 attenuation-corrected, while clause type explains substantially more variance (mixed-model ΔR² ≥ 0.15 over a source-contribution-only model); (c) content clauses show mean cross-task delta ≤ 0, with ≥ 15% of content-clause×target cells negative beyond the noise floor, while output-contract and error-avoidance clauses show mean cross-task delta of +1 to +4 points and are positive on a majority of targets; (d) the zero-rollout leave-one-target-out clause library is worth 25–75 cold-start GEPA rollouts (bootstrap CI excluding zero) and beats the length-matched filler and sham-clause controls by ≥ 2 points; (e) at least half the library's gain survives when format-compliance-driven items are removed from the metric. Refutation: the hand-written generic checklist matches the harvested library (harvesting is unnecessary); or filler/sham controls match it (the effect is token count, not content); or source contribution predicts cross-task contribution as well as type does (no dissociation — optimizers just find universally good text); or the library's rollout equivalence CI includes zero.",
 "Measurement and Noise Control": "Four disjoint splits per task: GEPA feedback set, GEPA validation set, an attribution set (used for all clause-level scoring), and a never-touched test set used only for the final library-vs-cold-start comparison, so clause selection never sees the reporting data. Every clause-level measurement is paired: the same executor, decode seed, example order and example subset are used for the with- and without-clause conditions, so deltas are within-item differences; we report per-example paired differences and use a paired bootstrap over examples clustered by task. Attribution set = 200 examples; with binary accuracy at p≈0.5 and paired scoring, a single clause×target cell detects ≈ 4-point effects at 80% power, so no individual cell is interpreted alone — all claims are made over aggregates of ≥ 15 cells (type-level means, n ≈ 15–40 cells, detect ≈ 1.2 points) or across 8 leave-one-target-out folds × 3 seeds = 24 paired observations for the library comparison (detects ≈ 1.5 points given the measured ~3-point run SD). Split-half reliability across GEPA seeds is reported for both source and cross-task contribution vectors *before* any correlation is interpreted, and correlations are attenuation-corrected against it. Anything below the treatment-free null-replicate floor is reported as null regardless of p-value; rollout equivalence is always an interval, never a point.",
 "Preprint Collision Check": "",
 "Risk Factors and Limitations": "(1) Clauses interact: a clause's marginal effect depends on its context, so leave-one-out and random-subset estimates can disagree; we report both and treat large disagreement as evidence of non-additivity, which is itself a finding about whether 'portable components' is even the right abstraction. (2) Segmentation is LLM-mediated and granularity-dependent; the granularity ablation bounds this but cannot eliminate it. (3) With 200-example attribution sets, per-cell power is low; the design compensates with aggregation, which means we can characterize clause *types* far better than individual clauses. (4) Eight tasks give eight generalization units; conclusions are stated at the level of these clusters. (5) The hand-written checklist baseline may match the harvested library, reducing the paper to a decomposition study plus a negative result on harvesting — still informative, and we would report it as such. (6) Portability may be executor-specific; only a reduced second-model replication is affordable. (7) The zero-rollout library is not expected to beat well-funded cold-start optimization, and we frame the result as a price in rollouts, not a win."
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
