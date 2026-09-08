=== SYSTEM ===
You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
axis of the research area below; propose ideas that take a position on that axis. You will not see ideas from other
axes; do not try to cover the whole area.

Bar to clear: contribution stateable in one sentence; positioning that names the closest prior work and what it does
not do; a central claim with an experiment that could come out against it; a measurement plan that separates an
effect from run-to-run noise; feasibility on small open models and single-node compute.

Use the literature digest you were given. Two fields are mandatory in your IDEA JSON in addition to the standard
ones: "Addresses gap": the digest gap ID this idea attacks, or "none" with one sentence on why the digest missed it;
"Not a restatement of": the nearest prior-result bullet in the brief and the nearest digest card, each with one
sentence on what this idea claims that they do not. If you cannot write those sentences, the idea is a restatement
and you must change it.

Before finalizing you must run at least two literature searches: one on the mechanism you are claiming, restricted
to the last twelve months, and one on the closest named method. Report what came back in "Preprint Collision Check",
including empty results, the query strings and the channel that answered. Do not write experiment code.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.

Two further requirements, both checked mechanically before review:
- Falsifiable Predictions: for every prediction write the outcome that would falsify it AND the arm or cell that can
  produce that outcome. If no arm can produce it (the split never gives the model that information; an append-only
  store cannot forget; a warm-started adapter always relearns faster than a cold one; the estimand is an identity of
  another quantity you compare it to; the falsifier lies inside your stated confidence interval), the prediction is
  entailed by the design and must be removed or the design changed. A proposal whose headline prediction is entailed
  is sent back before any judge sees it.
- One of your literature searches must be phrased in the home vocabulary of the mechanism, with no agent, memory,
  retrieval, experience or benchmark words (e.g. "data poisoning number of poison samples threshold" rather than
  "stale items in the agent's memory bank"); label it `home:` in the Preprint Collision Check. Papers that pre-empt
  a claim are usually found there, not under the agent-memory phrasing.

Standard IDEA JSON fields: Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Baselines and Ablations,
Falsifiable Predictions, Measurement and Noise Control, Preprint Collision Check, Risk Factors and Limitations.

=== USER ===
# Title: Which Memory Item Did It: Credit Assignment for Retrieved Experience in LLM Agents

Author: Fable 5.1, 2026-09-09. Stage-1 brief for the ideate2 pipeline, after the Stage-0 pre-scan on this topic (5 axes,
60 papers carded from S2 + HF, 25 gaps; `digest.md`; no section reads) and after Step 0 on this node
(`runs/STEP0_RESULTS.md`). Third topic of the program alongside `xfer` and `static`; the 51 archived ideas are the prior.

## Keywords
LLM agents, experience memory, credit assignment, counterfactual attribution, leave-one-out, Shapley, memory utility,
reinforcement over memory, retrieved-set interference, utility drift, data valuation, ALFWorld

## TL;DR
Every self-evolving memory system now scores its items: Q-values propagated over a provenance DAG (MemQ 2605.08374),
reduced-order utility coordinates (RoMeRL 2608.02508), critic-gated surprise and utility (2603.14597), survival importance
(2607.22562), attribution-derived local rewards (AttriMem 2607.21106), outcome-calibrated attribution distilled into the
policy (OPD-Evolver 2606.17628), admission scores (A-MAC 2603.04549). The scan finds the same hole under all five axes:
not one of these scores has been checked against the counterfactual effect of removing or adding the item it scores.
Credit is assigned to the retrieved set, the prompt, the agent or the write action, never to the item; the noise and sample
cost of any per-item estimate is unreported; interactions among co-retrieved items are measured only in single-shot RAG
(CUE-R 2604.05467, Shapley 2507.04480) or at the scaffolding-component level (2605.05716); and whether an item's value
survives a change of query, consumer or time is asserted. The program's own best-scored idea (memory_item_value_reliability,
6.12) lived here and did not pass, so the bar is known: a proposal must say what per-item credit is for, show that it can be
estimated at a cost the program can pay, and predict where it fails.

## Starting position (measured here; not to be rediscovered)
- **Expert bank, Qwen3-32B reader, ALFWorld:** k=0 0.536/0.549 → k=1 0.739/0.776 → k=3 0.807/0.869 → k=7 0.846/0.877
  (valid_seen/valid_unseen); net at k=3 +27.1 [+18.6, +35.6] / +32.1 [+22.9, +41.0]. Marginal value of items 2–3 over
  item 1 ≈ +7 net; of items 4–7 ≈ +4. The gain is procedure-bound (clean/heat/cool +39 to +55) and unseen ≈ seen; one type
  (look-at-in-light, n=62) nets −4.8. Retrieval logs (`runs/sweep/k_sweep_final.jsonl`) hold, per episode, the retrieved
  item ids in rank order, so a nested-k design (k=1 ⊂ k=3 ⊂ k=7 on the same games) already gives one crude per-position
  counterfactual for free.
- **Self pool:** 1,892 on-policy successes over all six types (0.533), success-filtered; useful for items whose value is
  expected to differ from expert items.
- **Noise floor:** a paired 274-game × 2-seed cell ≈ ±8 net; per-type cells ±13–15. Per-item estimates will be far noisier
  than per-arm ones: an item is retrieved for a handful of games, so any item-level claim must be about a distribution of
  items or a manufactured item class, not about individual items.
- **Measurement C (running):** static per-type procedure prompts vs retrieval; a retrieved item whose value is fully captured
  by the type's procedure has no item-specific credit to assign.
- **Cost:** ~20 episodes/min on two replicas; a leave-one-out re-run of one episode costs one episode; Shapley over a k=3 set
  costs 7 re-runs per episode.

## What the Stage-0 scan says, by axis (gap ids as in `digest.md`)
1. **Counterfactual attribution** (12 cards). Intervention-based per-item measurement exists for single-shot RAG (CUE-R
   REMOVE/REPLACE/DUPLICATE 2604.05467; document-level Shapley 2507.04480; DIG confidence gain 2509.12765) and at the
   component level for agent scaffolds (2^5 factorial with exact Shapley, 56 % submodularity violations, 2605.05716);
   agent-side credit is set-level (UCOB 2606.29502), agent-level (TreeMem 2605.04811), write-action-level (HiMPO
   2606.16285) or step-level (SLATE 2602.23440; Harness-G SNC 2607.27652). Gaps G1–G5.
2. **Learned utility and reinforcement over memory** (33 cards). MemRL two-phase retrieval (2601.03192), REMEMBERER
   (2306.07929), MemQ TD(λ) over a provenance DAG (2605.08374), RoMeRL's memory-reward trap and fixed-dimensional utility
   state (2608.02508), Oblivion's contribution-based reinforcement (2604.00131), MERIT's PRM proxy rewards (2606.00547),
   ExpSuite's with/without-set feedback (2605.30712), utility-aware pruning (ReMe 2512.10696, SF-AMS 2607.22562), admission
   (A-MAC 2603.04549, critic router 2603.14597). Gaps G6–G10: no score is checked against counterfactual item value; credit
   splitting among co-retrieved items unresolved; noise and sample cost unreported; validity under drift untested; pruning
   and admission error rates unmeasured.
3. **Set-level effects** (14 cards). Compliance trap (2607.10608), controlled memory interference (2608.07622), interference
   under updates (MINTEval 2605.18565; Memora 2604.20006), RaMem validity-aware retrieval (2606.22844), steerable memory
   dependence (2601.05107). Gaps G11–G15: per-item scores never validated against leave-one-out; harm's dependence on set
   composition untested in multi-step agents; failures never attributed to the responsible item; interference shown only on
   synthetic relationships; variance of per-item estimates unreported.
4. **Generalization and drift of item value** (31 cards). Gaps G16–G20: utility estimates never re-measured over a drifting
   stream; transfer of item value across consumers or query distributions untested; admission-time predictions never
   checked against realized utility (and false-negative cost unmeasured); forgetting rules validated only by aggregate
   accuracy; item value is state- and stage-conditional yet never measured per context.
5. **Measurement of per-item estimates** (22 cards). Benchmarks score end-to-end outcomes only (Evo-Memory 2511.20857,
   MemoryArena 2602.16313, MemoryAgentBench 2507.05257); no benchmark attributes a failure to an item. Gaps G21–G25.

## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **Ground truth is an intervention, not a score.** Any per-item value claim is anchored to re-runs with the item removed,
  replaced (token-matched) or added, on the same (game, seed); learned or proxy scores are evaluated by their rank
  correlation with that ground truth, not by downstream success alone.
- **Items are manufactured in classes when individual power is impossible.** Item-level CIs are wide; claims are about item
  classes (planted wrong-procedure items, stale-true items, same-type vs cross-type items, expert vs self-written items)
  with enough retrievals per class, or about the distribution of item values, with the sample size stated.
- **Set composition is a manipulated variable.** Any per-item estimate is reported under at least two co-retrieved-set
  compositions; additivity is tested, not assumed (pairwise removal vs single removal).
- **Noise and cost of the estimator are estimands.** Report variance across seeds and repeated runs, the number of episodes
  or re-runs needed for a stable per-item rank, and the LLM-call cost at that reliability; a method whose estimate needs
  more re-runs than a leave-one-out baseline must say so.
- **Static-procedure baseline (Measurement C).** Credit that a type-level procedure sentence already captures is not item
  credit; report item value net of the static-prompt arm.
- **Drift and consumer swap are separate arms**, not extrapolations: an item's value is re-measured after the query
  distribution, the store size or the reader changes.
- **No prediction entailed by a definition** (an append-only score cannot decrease; a leave-one-out on a k=1 set equals the
  k=0 contrast; a score defined from the outcome correlates with the outcome); per prediction, state the falsifying outcome
  and the arm that can produce it.
- **Home-vocabulary search**: data valuation, influence functions, Shapley attribution, credit assignment in RL, replay
  prioritization, off-policy evaluation; one query with no agent/memory/benchmark words.
- **Power and budget**: paired cells; per-class cells sized to ±5 net; re-run budgets stated cell by cell; both GPUs busy.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Do learned utilities track counterfactual item value (G6, G11, G22)?** Implement one published scorer per family
  (Q-value over provenance, utility coordinates, usage-decay survival, confidence gain) on the ALFWorld bank, then measure
  leave-one-out and replace effects for the same items; predict which scorer fails where (co-retrieval contamination,
  position, rarity) and by how much.
- **Q2 The unit of credit (G1, G7, G23).** Set-level, position-level, item-level: which unit predicts the outcome change of
  the next retrieval best, at what re-run cost; the nested-k logs give the first position-level estimate for free.
- **Q3 Interference and non-additivity (G4, G12, G25).** Pairwise vs single removal on manufactured sets (helpful +
  conflicting, helpful + redundant, two partial supports); how often single-item scores mis-rank when interactions exist.
- **Q4 Estimator noise and sample cost (G3, G8, G15, G24).** Convergence of per-item rank with re-runs and seeds; the
  winner's-curse of selecting top-scored items; how many episodes per item a pruning decision needs to beat random pruning.
- **Q5 Drift and consumer swap (G9, G17, G20, G16).** Re-measure item value after a rule change, after the store grows, after
  the reader is swapped (Qwen3-32B → a second backbone); fraction of items whose value sign flips; whether stage-conditional
  value (item helps at entry, hurts on recovery) exists.
- **Q6 Admission and pruning audits (G10, G18, G19).** Admit a random held-out sample regardless of score; correlate
  admission score with realized counterfactual utility; false-prune and false-bypass rates; whether frequency
  reinforcement entrenches wrong items.

## In scope
- ALFWorld primary (bank and logs on disk); a second environment only if the claim needs it; public data only.
- Qwen3-32B as reader; a second local backbone for the consumer-swap arm (serving to be verified).
- Reimplementation of one scorer per family as a named baseline (MemQ-style TD(λ), RoMeRL-style coordinates, usage-decay,
  DIG-style confidence gain); leave-one-out and Shapley as ground-truth estimators.

## Out of scope
- Frontier-model judges at experiment time; clinical or private data.
- New memory systems whose contribution is a better aggregate score; the contribution here is what the score means.
- Restating the archived ideas (appendix); a proposal near one must name it and state what it fixes.

## Resource constraints
Two A100 80GB, one replica per GPU, ~20 episodes/min. A leave-one-out ground truth over 274 games × 2 seeds × k=3 costs
about 1,650 re-runs (~1.5 h); Shapley over k=3 sets costs ~7× that; a scorer family needs one pass of the stream to learn
its scores (the 3,553-game train stream, ~3 h) before ground truth is measured. A full Q1 (four scorers, one ground truth,
two set compositions) is roughly two days. Pre-registration before the first confirmatory cell.

## Appendix A: archived ideas nearest this topic (do not restate; the gate compares against all 51)
- memory_item_value_reliability (6.12, round 1, the program's best score): item value is not an item property; a
  generalizability audit of per-item utility estimates in self-editing memory. Judges: no ground-truth intervention arm,
  effect sizes below the noise floor.
- counterfactual_memory_screening_under_selection_noise (5.45): does counterfactual screening survive its own noise;
  neighborhood-conditional utility, winner's curse, interference. Judges: the noise model was assumed, not measured.
- utility_pruning_is_frequency_pruning (4.9): outcome-based refinement deletes rare-task coverage. Judges: entailed by the
  pruning rule.
- retrieved_set_disagreement_gate (4.65): harm lives in the retrieved set, not the item; a disagreement gate. Judges:
  set-level claim without item-level ground truth.
- dormant_is_not_dead (5.45), action_prior_imprinting (5.27), memory_budget_confound (5.63), wrong_action_fraction_dose
  (4.85): adjacent on pruning, priors, volume and dose.

## Appendix B: what the previous rounds' judges demanded (binding)
Same pool / same backbone / one cost axis; bank–target partition; self-pool and self-distillation controls; memory-absent,
matched and mismatched evaluation; token- and rate-matched placebos; margins tied to the measured effect; positive controls
before any null; no prediction entailed by a definition; the cheapest baseline run first; searches in the mechanism's home
literature.


## Your axis
measurement of per-item estimates: noise, selection effects and winner's curse in per-item value estimates; how many episodes an estimate needs; benchmarks and metrics that score memories at the item level

## Digest gaps on your axis (cite by ID)
- G21: Per-item causal value of stored memories is unmeasured in multi-step, persistent-memory agent settings: the agentic memory benchmarks score only end-to-end task outcomes and never attribute a failure to a specific retrieved item, while intervention-based per-item measurement exists only for single-shot RAG. (cards arxiv:2511.20857, arxiv:2605.18565, arxiv:2602.16313, arxiv:2507.05257, arxiv:2604.20006, arxiv:2606.24775, arxiv:2604.05467, arxiv:2507.04480)
- G22: Proxy per-item utility signals (reduced-order utility coordinates, token-level attribution rewards, PRM proxy rewards, LLM-judge step rewards, single-document confidence gain) are never checked against the counterfactual effect of removing the same item. (cards arxiv:2608.02508, arxiv:2607.21106, arxiv:2606.00547, arxiv:2602.23440, arxiv:2509.12765)
- G23: Learned credit is assigned at units coarser than the memory item (pipeline agent, memory-write action, whole final memory, reasoning or query step, memory as a whole), so the value of an individual stored item at retrieval time is not estimated. (cards arxiv:2605.04811, arxiv:2606.16285, arxiv:2606.03329, arxiv:2602.23440, arxiv:2603.29247)
- G24: The variance, cross-seed stability and sample or compute cost of per-item estimates (number of rollouts, branches, episodes or LLM calls needed for a stable score) are not reported by any method that produces them. (cards arxiv:2604.05467, arxiv:2507.04480, arxiv:2607.27652, arxiv:2605.04811, arxiv:2607.21106, arxiv:2606.16285, arxiv:2602.23440)
- G25: Per-item estimates are computed one item at a time and ignore the composition of the co-retrieved set (redundancy, conflict, ordering, interference), even though non-additive multi-hop effects, compliance to conflicting entries and reward contamination across co-retrieved memories are observed. (cards arxiv:2509.12765, arxiv:2607.10608, arxiv:2511.20857, arxiv:2606.24775, arxiv:2604.05467, arxiv:2608.02508, arxiv:2507.04480)

## Digest cards for your axis and the cross-axis papers
- arxiv:2511.20857 (2025-11-25): Existing memory evaluations are static, and a streaming benchmark (Evo-Memory) plus a refine pipeline (ReMem) are needed to measure and achieve test-time learning with self-evolving memory across task streams. | limitations: not stated | not tested: No item-level scoring of individual memories (the benchmark measures task outcomes, not per-memory value), and no measurement of interference among co-retrieved experiences.
- arxiv:2602.06052 (2026-01-14): Agent memory is the critical substrate for self-evolving, long-horizon agents, and memory management is becoming a trainable capability that should be understood along substrate, cognitive mechanism and memory subject dimensions. | limitations: not stated | not tested: As a survey it reports no experiments; it does not test item-level credit assignment methods or compare per-item utility metrics empirically.
- arxiv:2608.02508 (2026-08-03): Trajectory-indexed memory utilities disperse feedback over a growing state space and jointly assigned trajectory rewards contaminate co-retrieved memories (the memory-reward trap), and representing utility with a fixed-dimensional reduced-order per-task state concentrates feedback and limits persistent reward contamination. | limitations: not stated | not tested: No direct counterfactual (leave-one-out) measurement of an individual memory's causal effect to validate that the utility coordinates track true item value, and the theory relies on a generic coordinate-transition model rather than measured transitions.
- arxiv:2603.29247 (2026-03-31): Explicit preference memory distilled from purchase history into concise, query-independent signals is a practical and effective building block for personalized product reranking in LLM-based shopping agents. | limitations: not stated | not tested: Whether the gain can be attributed to individual distilled memory items rather than the memory as a whole; how the RL-trained extractor behaves as user preferences drift over time or across domains outside the benchmark.
- arxiv:2607.21106 (2026-07-23): Augmenting outcome rewards with local rewards derived from token-level attribution to the final answer resolves the fine-grained credit-assignment bottleneck in RL-based learning of memory-construction policies. | limitations: not stated | not tested: Whether token-level attribution scores agree with counterfactual removal of the attributed memory contents; how noisy the attribution-derived local rewards are and how many episodes are needed for them to be reliable.
- arxiv:2605.04811 (2026-05-06): Agent-specific credit for a multi-agent memory pipeline can be derived from the final task reward alone, without task-specific annotations, by expanding the pipeline into a tree and Monte Carlo averaging over subsequent branches. | limitations: not stated | not tested: Credit is assigned at the agent level rather than to individual memory items, so it does not test which stored memories helped; the cost of the branch rollouts and how many branches are needed for stable estimates are not stated.
- arxiv:2606.00547 (2026-05-30): Memory usefulness changes across interaction stages, so multi-horizon retrieval with learned episode-level and turn-level policies improves experience reuse in interactive text-to-SQL agents. | limitations: not stated | not tested: Whether the PRM's proxy rewards for a retrieved memory agree with its counterfactual contribution to task success; whether learned retrieval values remain stable as the memory store grows or becomes stale.
- arxiv:2607.10608 (2026-07-12): Agents consuming retrieved memory fall into a compliance trap: they adopt conflicting memory at the first exposed decision point even when it is task-wrong, repeated exposure amplifies the error, recovery is weak, and once agents comply their success collapses to a low floor so stronger agents suffer larger absolute damage. | limitations: not stated | not tested: Does not report whether the harm depends on the number or composition of co-retrieved (conflicting plus correct) entries, nor whether any consumption-aware control policy actually mitigates the trap.
- arxiv:2507.04480 (2025-07-06): Shapley-based attribution can be adapted to identify influential retrieved documents in RAG, and cheaper SHAP approximations can approximate exact attributions while reducing the number of costly LLM calls, including under inter-document redundancy, complementarity and synergy. | limitations: not stated | not tested: No stated evaluation of attribution stability across repeated LLM calls or of whether attributed document values transfer across queries; multi-step agent trajectories are not addressed.
- arxiv:2604.05467 (2026-04-07): Per-evidence-item operational utility in RAG can be measured by intervention, and answer-only evaluation misses important evidence effects, including non-additive interactions among multi-hop supports. | limitations: not stated | not tested: Single-shot RAG only, so no multi-step agent trajectories or persistent memory; the cost of the interventions and the variance of per-item estimates across repeated runs are not reported.
- arxiv:2604.20006 (2026-04-21): Existing long-term memory benchmarks reduce to fact retrieval; when memory consolidation and frequent knowledge updates are tested, current LLMs and memory agents frequently reuse invalidated memories and fail to reconcile evolving ones, with memory agents offering only marginal improvements. | limitations: not stated | not tested: Failures are not attributed to specific retrieved items and no per-item value is measured; the benchmark does not test whether agents can learn item utility from feedback over time.
- arxiv:2509.12765 (2025-09-16): A retrieved document's value can be quantified as the change in the LLM's generation confidence with versus without it (Document Information Gain), and a reranker trained on DIG scores substantially improves RAG answer accuracy by filtering irrelevant or misleading documents. | limitations: not stated | not tested: DIG is computed one document at a time, so interactions among co-retrieved documents (redundancy, conflict, ordering) are not captured; whether DIG scores transfer across generator models or query distributions is not examined.
- arxiv:2606.16285 (2026-06-15): Credit for memory-writing actions in long-horizon agents is causally entangled with downstream tool failures, noisy observations and reasoning errors, and a hindsight-informed memory-specific advantage disentangles it, improving both task performance and attribution fidelity. | limitations: not stated | not tested: Credit is assigned to memory-write actions, not to individual retrieved items, so the value of stored content at retrieval time is not estimated; the noise and sample cost of the local-utility estimator (how many episodes it needs) are not reported.
- arxiv:2602.23440 (2026-02-26): Truncated step-level sampling (trajectories sharing a prefix and differing only at the next step) combined with dense LLM-as-judge rewards for each reasoning step, search query and answer yields lower-variance, better-targeted policy gradients than sparse-outcome or heuristic process-reward RL for search-augmented reasoning. | limitations: not stated | not tested: Credit is assigned to reasoning and query steps, not to individual retrieved documents; the reliability of the LLM judge's rewards and its compute cost per training step are not quantified.
- arxiv:2607.27652 (2026-07-30): RL search agents suffer retrieval-equivalence collapse (distinct query strings yield increasingly overlapping evidence sets, leaving within-group returns with little retrieval contrast), and reformulating retrieval as finite action selection over a menu of evidence plus structured non-myopic credit fixes this and improves QA. | limitations: not stated | not tested: Stability of SNC's per-action credit across seeds and the number of rollouts it needs; only small models and QA, no agentic-memory settings; whether environment-side menu construction biases which evidence is available for selection.
- arxiv:2605.18565 (2026-05-19): Current memory-augmented agents perform poorly in long-horizon settings where information is repeatedly updated and interferes across memories, especially on questions requiring aggregation over multiple pieces of evidence, with accuracy degrading as intervening updates increase. | limitations: not stated | not tested: No scoring of individual memory items (only question-level accuracy), so which stored item caused a failure is not attributed; no evaluation of methods designed to handle updates, only of existing systems.
- arxiv:2606.03329 (2026-06-02): Rewarding a chunk-wise memory agent by how much its final memory raises the per-token log-likelihood of the ground-truth answer, applied only on successful trajectories and normalized, improves RL training over sparse or lexical intermediate rewards. | limitations: not stated | not tested: Reward operates on the whole final memory, so credit to individual memory updates or chunks is not attributed; robustness of the log-likelihood signal when the reference answer is one of several valid phrasings is not examined.
- arxiv:2603.07670 (2026-03-08): Agent memory is best understood as a write-manage-read loop coupled to perception and action, and current evaluation is shifting from static recall benchmarks to multi-session agentic tests that expose persistent gaps in existing systems. | limitations: not stated | not tested: No empirical comparison of the surveyed mechanisms; open challenges such as causally grounded retrieval and learned forgetting are named but not operationalized or measured.
- arxiv:2606.24775 (2026-06-23): No single agent-memory architecture dominates across workloads; effectiveness depends on aligning memory structure with the workload bottleneck, and localized maintenance is more cost-efficient than global reorganization. | limitations: not stated | not tested: Ablations are at the module level, not the individual-memory-item level; no measurement of how the retrieved set (order, conflicts, redundancy) affects outcomes.
- arxiv:2602.16313 (2026-02-18): Agents that appear near-saturated on long-context memory benchmarks like LoCoMo perform poorly when memorization and action are coupled across interdependent multi-session tasks, exposing a gap in current memory evaluation. | limitations: not stated | not tested: Scores are end-to-end task outcomes; the benchmark does not score individual stored memories or attribute later-session success to specific items.
- arxiv:2507.05257 (2025-07-07): Memory agents require four core competencies (accurate retrieval, test-time learning, long-range understanding, conflict resolution) and current methods fail to master all four. | limitations: not stated | not tested: Conflict resolution is measured only as task outcome, not as which retrieved items were correctly favored or suppressed; no item-level scoring of memory quality.
- arxiv:2412.06531 (2024-12-09): Precise cognitive-science-inspired definitions of RL agent memory types and a standardized evaluation methodology are needed because loosely defined memory concepts lead to erroneous judgments about agents' memory capabilities. | limitations: not stated | not tested: Concerns classical RL agents, not LLM agents with external retrieved memory; no evaluation of the value of individual stored items.
- arxiv:2601.03192 (2026-01-06): MemRL, a non-parametric approach that performs reinforcement learning on episodic memory with a Two-Phase Retrieval mechanism, reconciles the stability-plasticity dilemma and enables continuous runtime improvement without weight updates. | limitations: not stated | not tested: No per-item attribution of which memory entries caused a gain, and no reported comparison of how utility estimates behave under co-retrieval of multiple items; robustness of utility estimates across queries or tasks over time is not described.
- arxiv:2606.29502 (2026-06-28): Retrieved skills are not oracular and can mislead in some states, so a credit-aware, on-policy bidirectional self-distillation (UCOB) that compares skill-conditioned and no-skill views at the same anchor state yields better skill utilization and evolution than fixed privileged-teacher assumptions. | limitations: not stated | not tested: Credit is assigned to the skill-conditioned prompt as a whole rather than to individual retrieved skills within a multi-skill set, and the noise or sample requirements of the per-skill utility estimates are not described.
- arxiv:2512.10696 (2025-12-11): A dynamic procedural memory framework (ReMe) that distills, contextually reuses and utility-refines experiences beats passive append-only memory and shows a memory-scaling effect where a smaller model with memory outperforms a larger memoryless one. | limitations: not stated | not tested: How the utility signal used for pruning is estimated and whether pruning errs (removing items that were useful), and whether utility transfers when the query distribution or consumer model changes, are not described.
- s2:05c14833b7cee3408bf72d25cf0bee2c4b0d70b0 (2025-12-04): Scoring replay-buffer transitions by a weighted combination of reward magnitude and TD error and evicting low-utility ones speeds learning and improves final returns over static retention schemes. | limitations: not stated | not tested: Only two small classic-control tasks are used, so transfer of utility scores to larger domains or LLM-agent memory is untested; the utility is a fixed heuristic, not a counterfactual estimate of a transition's effect on outcomes.
- arxiv:2608.07622 (2026-08-07): Memory evolution in continual LLM agents is shaped by interactions among accumulated memories, with relationship-specific interference sharply suppressing update plasticity while benign accumulation has limited effect. | limitations: not stated | not tested: Interference is studied under synthetic controlled relationships rather than naturally accumulated agent memories, and no learned per-item utility or feedback-based update is examined.
- arxiv:2601.05107 (2026-01-08): An agent's reliance on memory can be modeled as an explicit, user-controllable dimension, avoiding both memory anchoring and memory under-utilization in long-term interaction. | limitations: not stated | not tested: Which specific memory items drive the anchoring effect (the dependence metric is aggregate rather than per-item); whether the memory-dependence metric agrees with counterfactual removal of individual memories.
- arxiv:2512.07287 (2025-12-08): A hybrid episodic-procedural memory that adaptively reuses partially overlapping successful experiences improves multi-turn tool-use policies at both inference and RL training time. | limitations: not stated | not tested: Whether individual tool-graph edges or episodic summaries are credited or pruned based on their measured contribution to outcomes; how the memory behaves when past successful transitions become stale or misleading as the environment changes.
- arxiv:2605.08374 (2026-05-12): Propagating credit backward through a provenance DAG of memory dependencies with TD(λ) eligibility traces improves episodic-memory agents over methods that evaluate each memory in isolation. | limitations: not stated | not tested: Whether the Q-values assigned to individual memories agree with counterfactual removal of those memories; how credit is split among co-retrieved memories at the same DAG level and whether Q-values remain valid as the task stream drifts.
- arxiv:2511.10030 (2025-11-13): Decentralized retrieval of relevant trajectories as in-context memory, scored by a hybrid individual- and team-level utility, enables faster adaptation to unseen tasks in cooperative multi-agent RL. | limitations: not stated | not tested: Whether the hybrid utility score of a retrieved trajectory reflects its causal effect on the episode outcome; the paper credits agents rather than measuring the value of individual retrieved memories, and does not test interference among co-retrieved trajectories.
- arxiv:2602.17930 (2026-02-20): A structured, evolving memory graph built from high-return experiences and amortized LLM outputs can shape advantage estimation to speed early sparse-reward RL learning while requiring substantially fewer online LLM queries and preserving convergence guarantees. | limitations: not stated | not tested: Whether individual memory-graph entries are credited or pruned according to their measured effect on returns; how unreliable LLM-derived entries in the graph are detected and how their value degrades as the policy improves.
- arxiv:2602.05832 (2026-02-05): Augmenting online RL for mobile GUI agents with a hierarchical, self-evolving experience memory improves credit assignment in long-horizon tasks and enables cross-task and cross-application experience transfer, outperforming RL baselines and static reuse strategies. | limitations: not stated | not tested: No attribution of outcome improvements to individual memory entries (which workflow or failure template helped or hurt a given rollout) and no measurement of whether stale or wrong templates accumulate in the self-evolving memory over time.
- arxiv:2604.27003 (2026-04-29): External memory does not eliminate the continual-learning stability-plasticity problem for LLM agents; it relocates it to retrieval, where old and new experiences compete under a limited context window, and memory representation and organization choices trade off forward transfer against forgetting. | limitations: not stated | not tested: Item-level attribution of negative transfer to specific memories is not described, and the number of task sequences or models over which transfer/forgetting effects are estimated is not stated.
- arxiv:2603.04549 (2026-03-04): Treating memory admission as a structured decision over five interpretable factors gives transparent, efficient control of long-term memory and a better precision-recall tradeoff at lower latency than LLM-native memory systems. | limitations: not stated | not tested: Whether the predicted future utility of admitted items matches their realized downstream utility is not reported, and admission is evaluated on one benchmark without post-admission feedback updating item value.
- s2:eddd445307658518949b54ad4acc0f06c5f660a3 (2026-06-01): Weighting memory entries by usage frequency, semantic relevance and an externally validated freshness signal, with conflict-triggered refresh, mitigates memory overload and temporal staleness in long-running agents. | limitations: not stated | not tested: No ablation isolating the contribution of usage-frequency decay versus the freshness signal, and no evaluation on interactive agent tasks beyond a QA simulation or with the external validation source unavailable or wrong.
- arxiv:2603.14597 (2026-03-15): Gating memory restructuring with a reward-prediction-error critic (Fast/Slow routing) lets an LLM agent maintain lifelong memory at far lower token and write-latency cost while matching or beating append-and-evolve systems such as A-MEM. | limitations: not stated | not tested: Whether the critic's write-time Surprise/Utility score predicts the downstream benefit of a stored item (no per-item counterfactual check); the cost of false negatives, i.e. low-RPE inputs that are bypassed but later needed.
- arxiv:2510.09720 (2025-10-10): Dynamically refining preference memory by fusing sliding-window averages with exponential moving averages improves LLM output quality in long-term conversations compared with memory systems that only store and retrieve. | limitations: not stated | not tested: Whether gains come from tracking preference drift versus simply smoothing noisy preferences; no attribution of which stored preferences drove the improvement; sensitivity to window size and EMA decay hyperparameters.
- arxiv:2607.01071 (2026-07-01): Retrieved memories can harm agents by inducing sycophancy (over-aligning with the user at the cost of factual accuracy or objective reasoning), and existing memory benchmarks miss this because they test storage, retrieval and updating rather than how retrieved memory influences downstream reasoning. | limitations: not stated | not tested: No results appear in the abstract, so whether any agent or memory system mitigates memory-induced sycophancy is unknown; the benchmark scores decisions, not the value of individual memory items.
- arxiv:2605.30712 (2026-05-29): Frozen, replaceable LLM executors can improve without parameter updates by reusing skills and failure lessons stored in a self-evolving experience graph retrieved through graph diffusion and utility-aware ranking. | limitations: not stated | not tested: The with-versus-without feedback is at the level of the whole retrieved set, so credit is not attributed to individual experiences within it; whether utility estimates learned under one executor transfer to a replaced executor is not isolated from the overall model-agnosticism claim.
- arxiv:2606.22844 (2026-06-22): Retrieval alone does not make a memory valid evidence for the current query, and restoring each fragment's original episodic context (time, session span, participants) and checking it against query-implied conditions consistently improves long-term memory performance. | limitations: not stated | not tested: No ablation showing how much of the gain comes from excluding context-incompatible items versus the synthesis stage; no measurement of how often validity-aware retrieval wrongly demotes a memory that was in fact the correct evidence.
- s2:84a2ed6eddc5e89a8c58d92265189d0d79bcdc8b (2025-11-10): An ACT-R-inspired activation mechanism with temporal decay, semantic similarity and probabilistic noise lets an LLM dialogue agent retrieve and forget memories in a human-like, context-sensitive way. | limitations: not stated | not tested: No measurement of whether the human-like forgetting improves task outcomes or answer quality; no comparison against non-decaying retrieval baselines on an external benchmark.
- arxiv:2603.18079 (2026-03-18): Retrieving experiences at each decision step conditioned on the current observation, with a self-evolving experience library and step-level credit assignment, outperforms RL baselines on multi-turn agent tasks where one-shot static retrieval becomes mismatched. | limitations: not stated | not tested: The step-level credit assignment targets policy actions, and the abstract gives no evidence that credit is propagated back to the retrieved experience items themselves; the effect of score-based admission thresholds on library quality is not reported.
- arxiv:2604.00131 (2026-03-31): Treating memory as a control problem, deciding when to retrieve based on uncertainty and buffer utility and what to reinforce based on contribution to the response, with decay-driven accessibility rather than deletion, sustains long-horizon performance at lower token cost. | limitations: not_stated | not tested: How the write path determines that a memory contributed to the response is not described, so whether reinforcement correctly credits the responsible item versus co-retrieved items is untested; no ablation isolating the decay schedule from the read-gating.
- arxiv:2605.05716 (2026-05-07): Stacking more scaffolding components onto an LLM agent is often worse than a task-specific subset because components interfere destructively, and greedy component selection is unreliable due to widespread submodularity violations. | limitations: A three-body synergy among Tool Use, Self-Reflection, and Retrieval is reported as exploratory. | not tested: Shapley attribution is at the component level, not for individual retrieved or stored memory items; only two benchmarks and one primary model family are used, so the task-dependence of k* is not tested broadly.
- arxiv:2607.22562 (2026-05-29): Modeling memory-unit importance as a dynamic utility signal updated from usage, redundancy and temporal cues, and using it to strategically forget, improves long-context multi-step reasoning over static retrieval and heuristic decay. | limitations: not stated | not tested: Whether the utility scores are causally correct at the item level (no counterfactual or ablation check that forgotten units were actually harmless); robustness of the forgetting rule when usage signals are noisy or when frequently used but wrong items get reinforced.
- arxiv:2606.17628 (2026-06-16): An agent can be trained, via slow-fast co-evolution with on-policy self-distillation using outcome-calibrated memory attribution and privileged hindsight, to internalize selecting, using, writing and maintaining experience, outperforming memory systems and training-based methods. | limitations: not stated | not tested: Accuracy of the outcome-calibrated memory attribution itself is not validated against counterfactual re-runs; no report on whether the distilled policy's memory-management behavior degrades or drifts as the repository grows.

Propose 3 proposals on this axis, each as a complete IDEA JSON with the two extra fields. Return JSON:
{"proposals":[{...}, ...]}.
