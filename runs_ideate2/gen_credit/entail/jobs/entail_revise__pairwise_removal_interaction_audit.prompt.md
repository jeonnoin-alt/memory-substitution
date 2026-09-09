=== SYSTEM ===
You are revising your own research proposal after review.

The reviewers' objections are the specification. Answer each one concretely — not by adding reassuring prose, but by changing the design: cut experiments that do not carry a claim, drop target tasks, shrink the grid, narrow the claim to what the sample size can actually detect, add the baseline they named.

Two rules:

- **Do not abandon the core hypothesis.** A proposal that answers every objection by becoming   generic is worse than one that keeps a sharp claim and scopes it honestly. If an objection   can only be answered by giving up the contribution, keep the contribution and say in   changes_made why you refused.
- **Novelty is the thing you are most likely to lose.** Measured across revision rounds,   answering reviewers reliably raises soundness and feasibility and *lowers* novelty: the   claim gets hedged, the scope narrows, and what was surprising becomes safe. Guard against   that. Do not soften the central claim into something a reviewer could not disagree with, do   not replace a sharp mechanism with a measurement study, and do not add qualifiers that make   the prediction unfalsifiable. If a reviewer's objection is really "this is risky", the right   answer is a better test of the risky claim, not a smaller claim. State in changes_made what   you did to keep the claim as sharp as it was.
- **The resource envelope is hard.** Every experiment must fit the stated compute and budget.   If the full matrix does not fit, cut it to a primary experiment that decides the main claim   plus the minimum ablations that isolate the mechanism, and state the arithmetic: number of   runs x rollouts per run, and why that fits. A smaller study that can be run beats a large   one that cannot.

=== USER ===
=== PROPOSAL ===
{
 "Name": "pairwise_removal_interaction_audit",
 "Title": "Removal Is Not Additive: Pairwise versus Single Leave-One-Out on Manufactured Retrieved Sets in a Multi-Step Agent",
 "Short Hypothesis": "In ALFWorld with a Qwen3-32B reader and k=3 retrieval, the counterfactual value of a retrieved item depends on what is co-retrieved with it. On manufactured sets the pairwise interaction term I(a,b) = f(S) - f(S-a) - f(S-b) + f(S-ab), measured on the same (game, seed), is negative for a helpful item plus its paraphrase (OR structure: each single removal ~0, joint removal loses the whole gain), negative for a correct plus a conflicting same-type procedure (masking: the correct item's value is hidden while the wrong one is present), positive for two complementary partial supports, and ~0 only for the control class (helpful + irrelevant cross-type item). Consequently single-removal (leave-one-out) scores mis-rank the items of interacting sets against exact Shapley in a substantial excess of sets over the control class, and the number of seeds needed for a per-set removal sign to stabilize is an estimand, not a footnote.",
 "Related Work": "CUE-R (arxiv:2604.05467) measures REMOVE/REPLACE/DUPLICATE per evidence item in single-shot RAG and reports non-additive multi-hop interactions, but no multi-step agent, no pairwise-removal estimand and no run-to-run variance or cost. Shapley source attribution in RAG (arxiv:2507.04480) compares SHAP approximations to exact document attributions under redundancy/complementarity/synergy on QA, without stochastic-evaluation noise or agents. The scaffold-level 2^5 factorial (arxiv:2605.05716) finds 56% submodularity violations among components, not among retrieved items. DG-Mem (arxiv:2608.23268) uses Shapley context attribution over memory entries as a component of a multimodal agentic learner and does not test additivity or estimator noise. RoMeRL (arxiv:2608.02508) posits contamination of co-retrieved memories by jointly assigned rewards without a counterfactual check; MemQ (arxiv:2605.08374) leaves credit splitting among co-retrieved siblings open. The compliance trap (arxiv:2607.10608) shows early adoption of conflicting memory but never varies the co-retrieved set. Formal home: Shapley interaction indices (shapiq arxiv:2410.01649; joint Shapley arxiv:2107.11357). Archived: counterfactual_memory_screening_under_selection_noise (5.45) assumed its interference and noise model; retrieved_set_disagreement_gate (4.65) claimed set-level harm without item-level ground truth. This proposal measures interference with the pairwise cell and noise with no-op repeats, on manufactured classes with stated power.",
 "Abstract": "Every self-evolving memory system scores its items, but a per-item score is only meaningful if an item's value is an item property. We test the weakest form of that assumption, additivity of removal effects, directly in a multi-step agent. On ALFWorld with a Qwen3-32B reader and k=3 retrieval from the expert bank, we manufacture retrieved sets of four classes (helpful + token-matched paraphrase; correct + conflicting same-type procedure; two complementary partial supports; helpful + irrelevant cross-type control), embed each pair beside a natural third item from the retrieval logs, and run on the same (game, seed) the full set, both single removals, the joint removal and a no-op repeat of the full set. The pairwise interaction term is the estimand and the repeat runs give its null distribution. We predict class-specific signs (redundant: negative; conflict: negative, at least half of the correct item's value masked; complementary: positive; control: zero), then complete the 2^3 subset lattice to obtain exact Shapley values and quantify how often single-removal scores mis-rank the items of interacting sets relative to Shapley, and how many seeds a per-set removal sign needs to stabilize. Item credit is reported net of the static-procedure prompt arm and under two background compositions. The result is a measured rather than assumed interference model that says when per-item credit in an experience bank is well-defined and what a reliable estimate costs in re-runs.",
 "Experiments": "(1) Materials: expert bank, k-sweep retrieval logs (runs/sweep/k_sweep_final.jsonl), Qwen3-32B reader on two vLLM replicas. Games: all procedure-bound types (clean/heat/cool) in valid_seen+valid_unseen (~140) plus ~60 bank-disjoint train-stream games of the same types (partition verified before pre-registration) = 200 games x 4 seeds = 800 paired cells per class. (2) Set construction: S = (a, b, x) in retrieval-rank slots 1-3; x is the natural rank-3 item from the logs and is held fixed; (a, b) is the manufactured pair. REDUNDANT: a = natural rank-1 same-type expert item, b = Qwen3-32B paraphrase of a with identical action sequence (checked by exact action-string match after paraphrase) and matched token count. CONFLICT: a = natural rank-1 same-type item, b = planted wrong-procedure item for the same task type (clean: heats instead of using the sink; heat: uses the fridge; cool: uses the microwave), token-matched to a. COMPLEMENTARY: a = find-and-take fragment of a same-type expert episode cut before the procedure step, b = procedure-and-place fragment from another same-type expert episode with the same receptacle; neither alone contains the whole procedure; token-matched jointly to one full item. CONTROL: a = natural rank-1 same-type item, b = cross-type expert item (different task type) token-matched to the other classes' b. (3) Phase 0, positive controls (cheapest first, ~400 episodes, 20 min): CONFLICT wrong-item-alone (b, x) vs (x) on 100 games x 2 seeds must show harm >= 10 net, else the planted item is revised; CONTROL (a, x) vs (x) must reproduce the known k=1-scale gain (>= +15 net on procedure types). (4) Phase 1, interaction cells: per (game, seed) run f(S), f(S-a), f(S-b), f(S-ab) and a no-op repeat f(S)'; 5 x 800 x 4 classes = 16,000 episodes (~13 h at 20 ep/min, both GPUs). (5) Phase 2, Shapley completion for CONFLICT, REDUNDANT, CONTROL: add subsets (a), (b), (a,b), () under the same seeds: 4 x 800 x 3 = 9,600 episodes (~8 h); exact Shapley phi_SH(i) per item per cell and per class. (6) Phase 3, static-prompt net arm (Measurement C): CONFLICT and REDUNDANT cells re-run with the type's static procedure sentence present, 400 cells x 4 = 3,200 episodes (~2.7 h); item credit reported net of this arm. (7) Phase 4, second background: CONFLICT class with x replaced by a natural cross-type item (and, as a second condition, by the natural rank-2 same-type item): 800 x 4 = 3,200 episodes (~2.7 h). (8) Analysis: mean I per class with cluster bootstrap by game; LOO phi_LOO(i) = f(S) - f(S-i); per-set top-item agreement and Spearman between LOO and Shapley; sign-agreement of per-set LOO across split halves of seeds as a function of seed count; LLM-call cost per unit of rank reliability for LOO (3 runs), LOO+pair (4 runs) and Shapley (8 runs). Total ~32,000 episodes, ~27 h on two A100s; pre-registration of thresholds before Phase 1.",
 "Baselines and Ablations": "Additive model (predict f(S-ab) from the three other cells) as the null; DIG-style single-item confidence gain (log-prob of the first procedure-relevant action with vs without the item, one forward pass) as the cheap proxy scored against LOO and Shapley; position swap of a and b within the pair to separate slot from content inside each class; token-matched irrelevant filler in place of b as placebo for each class; no-op repeat as the noise floor; second background (Phase 4) for the CONFLICT class; static-procedure prompt arm to net out type-level credit; per-type reporting (clean/heat/cool) to expose type specificity.",
 "Falsifiable Predictions": "P1 REDUNDANT: mean I <= -8 net (single removals ~0, joint removal loses the item's gain). Falsified if I is within [-4, +4] (additive) or I >= +4 (each copy adds, i.e. repetition amplification as the compliance-trap account of repeated exposure would give). Arm: the REDUNDANT class's four cells. P2 CONFLICT (masking): I <= -0.5 x [f(a,x) - f(x)], i.e. at least half of the correct item's value is hidden while the wrong item is present. Falsified if I >= -0.25 x [f(a,x) - f(x)] (the reader reconciles both, near-additive), producible by the CONFLICT cells plus the Shapley subsets (a,x) and (x); not entailed because a reader that follows the higher-ranked or majority item would give I ~ 0 with a in slot 1. P3 COMPLEMENTARY: I >= +8 net (super-additive). Falsified if I <= +3, produced by the COMPLEMENTARY cells; possible because k=0 success is 0.54 so the prior often completes the missing half. P4 CONTROL: |I| <= 4 net. Falsified if |I| >= 8 (cross-type items interact by distraction), produced by the CONTROL cells. P5 Estimator: LOO's top-item choice disagrees with exact Shapley in >= 25% of CONFLICT and REDUNDANT sets vs <= 10% of CONTROL sets, an excess of >= 15 points after subtracting the no-op-repeat disagreement rate. Falsified if the excess over CONTROL is < 5 points, produced by the Shapley cells; not entailed because LOO and Shapley coincide whenever the outcome is additive, and additivity is what the cells measure. P6 Noise: split-half sign agreement of per-set LOO reaches 0.9 only at >= 4 seeds. Falsified if 2 seeds already give >= 0.9 agreement, produced by the repeat and multi-seed cells. P7 Background: the CONFLICT masking term changes by <= 4 net when x is swapped from same-type to cross-type. Falsified if it changes by >= 10 (masking is a three-body property), produced by the Phase 4 cells.",
 "Measurement and Noise Control": "All contrasts are paired on (game, seed) with identical prompt template and sampling settings; the no-op repeat f(S)' gives the empirical flip rate under no intervention, used as the null for I and for single-removal effects via a permutation test that reshuffles which of the two full-set runs is labelled f(S). Per-cell I is bounded in [-2, +2] with SD ~0.7, so 800 cells give an SE of ~0.025 (~+/-5 net at 95% after game clustering); CIs by cluster bootstrap over games (1,000 resamples). Thresholds pre-registered; positive controls (Phase 0) must pass before any null is interpreted. Seed-count convergence of per-set LOO sign and of per-class I reported as estimands (G15); LLM-call cost stated per estimator at matched reliability. Item credit reported net of the static-procedure arm and separately per task type.",
 "Preprint Collision Check": "Q1 (mechanism, --recent, S2+HF ok): \"non-additive interaction among co-retrieved documents pairwise removal attribution\" -> CUE-R arxiv:2604.05467 (single-shot RAG perturbation, non-additive multi-hop), arxiv:2605.01284 (visual evidence attribution), arxiv:2601.03786 (training-data influence explanations); none measures pairwise interaction in a multi-step agent. Q2 home: \"Shapley interaction index pairwise ablation additivity violation attribution\" (S2+HF ok) -> shapiq arxiv:2410.01649, joint Shapley arxiv:2107.11357, OddSHAP arxiv:2602.01399, O-Shap arxiv:2602.17107; formal tools and vision/tabular applications only. Q3 (closest named method, S2+HF ok): \"Shapley attribution retrieved documents RAG redundancy synergy\" -> arxiv:2507.04480 (Source attribution in RAG, SHAP approximations vs exact on documents), arxiv:2511.10687 (game-theoretic credit for multi-LLM agents), DG-Mem arxiv:2608.23268 (verified by `paper`: Shapley context attribution over memory entries inside a multimodal agentic learner; no additivity test, no manufactured interaction classes, no noise floor). Q4 (--recent, S2+HF ok): \"conflicting memory agent compliance first decision point\" -> arxiv:2607.10608 compliance trap, arxiv:2605.30087 selective QA over conflicting memory, arxiv:2605.06527 STALE; none varies co-retrieved composition. Q5 home: \"leave-one-out versus Shapley value rank agreement under stochastic evaluation noise data valuation\" -> no results (S2+HF); shortened \"leave-one-out Shapley rank correlation noise\" -> only unrelated SHAP applications and OddSHAP; \"Data Shapley versus leave-one-out influence disagreement\" -> KAIROS arxiv:2506.23799 (model-agnostic data valuation), nothing on LOO-vs-Shapley agreement under evaluation noise. No pre-emption found; DG-Mem and CUE-R are the papers to position against.",
 "Risk Factors and Limitations": "Manufactured items may be unnatural; mitigated by token matching, action-sequence checks and the natural third item, and by reporting the CONTROL class. vLLM batching makes seeded runs non-deterministic; the no-op repeat measures this rather than assuming it. Binary success is coarse and effects may be type-specific (reported per type). Three-item Shapley is a partial view of k=7 sets (2^7 subsets is out of budget; a k=7 extension is stated as future). The conflict item may be too weak or too strong; Phase 0 gates it. Masking may depend on slot order; the position-swap ablation addresses it. Claims are about item classes, not individual items.",
 "Addresses gap": "G12 (harm and help of a co-retrieved item as a function of set composition in a multi-step agent) primarily; G15 (variance and seed cost of per-item estimates via no-op repeats and split-half convergence); G11 partially (single-removal score checked against exact Shapley).",
 "Not a restatement of": "Brief bullet: \"Marginal value of items 2-3 over item 1 ~ +7 net; of items 4-7 ~ +4\" (nested-k per-position counterfactual) is an aggregate marginal over natural sets that assumes additivity across positions; this idea manipulates composition and measures the interaction term itself by pairwise removal on the same (game, seed). Digest card arxiv:2604.05467 (CUE-R): single-shot RAG REMOVE/REPLACE/DUPLICATE without a multi-step agent, a pairwise-removal estimand, or noise and cost; this idea claims the sign of the interaction per class in a multi-step agent, a stated excess of LOO-vs-Shapley mis-ranking, and the seed count for a stable removal sign. Archived counterfactual_memory_screening_under_selection_noise assumed the interference and noise model; here both are measured cells."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "pairwise_removal_interaction_audit",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "REDUNDANT class cells f(S), f(S-a), f(S-b), f(S-ab) where b is a token-matched paraphrase of a with exact action-string match and x is held fixed; Phase 0 gate requiring the same rank-1 item a to give >= +15 net in (a,x) vs (x); class CI +/-5 net.",
   "falsifier": "mean I inside [-4,+4] (additive) or I >= +4 (repetition amplification, each copy adds).",
   "label": "near_entailed",
   "reason": "Removing either copy deletes no information the set still carries, so I collapses to f(S-ab) - f(S) = minus the joint gain, which the Phase 0 gate pins at <= -15; the falsifier needs the reader to respond to copy count rather than content, a mechanism the design plants no arm for, and the 4-net gap between the confirm and falsify bands is inside the stated +/-5 net class CI.",
   "fix": "Add a dose arm that varies the number of copies of an item whose solo gain is verified small (and a partially degraded paraphrase), decoupled from the >= +15 net Phase 0 gate, and widen the falsifier to I >= 0."
  },
  {
   "id": "P2",
   "depends_on": "CONFLICT cells plus the Phase 2 Shapley subsets (a,x) and (x); Phase 0 gate that the planted wrong item alone harms >= 10 net; threshold expressed as a fraction of f(a,x) - f(x).",
   "falsifier": "I >= -0.25 x [f(a,x) - f(x)], i.e. a keeps more than three quarters of its solo value while the conflicting item is present.",
   "label": "unresolvable",
   "reason": "The falsifier is structurally reachable (a sits in slot 1 and can simply be followed, and the Phase 0 floor on f(b,x) leaves room for a to rescue a depressed baseline), but at the gated gain of about 15 net the confirm boundary (-7.5) and the falsify boundary (-3.75) differ by under 4 net, inside the stated +/-5 net class CI, and both are ratios of two separately noisy measured terms.",
   "fix": "Restate the falsifier as an absolute net threshold (e.g. I >= 0) and size the CONFLICT class so the class-mean I carries a CI under 2 net."
  },
  {
   "id": "P3",
   "depends_on": "COMPLEMENTARY cells with a and b cut so neither fragment alone contains the whole procedure, natural rank-3 item x held fixed, k=0 success 0.54, 800 cells at +/-5 net.",
   "falsifier": "I <= +3 net (no super-additivity).",
   "label": "open",
   "reason": "The prior at 0.54 k=0 success or the fixed natural rank-3 item can complete the missing half, so single-fragment cells can retain most of the gain and drive I toward zero, and unlike the other classes no positive control forces the joint gain, although the 5-net gap between +8 and +3 only just matches the stated +/-5 net CI.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "CONTROL cells (natural rank-1 same-type a plus token-matched cross-type b, x fixed), class CI +/-5 net, no-op repeat as noise floor.",
   "falsifier": "|I| >= 8 net (cross-type items interact by distraction).",
   "label": "unresolvable",
   "reason": "Distraction by a cross-type item is a real route to the falsifier, but the 4-net equivalence bound is below the stated +/-5 net class CI, so an observed |I| of 8 has a CI that still contains 4 and neither side of the decision can be separated.",
   "fix": "Raise cells or seeds until the CONTROL class CI is about +/-2 net, or pre-register the class as a formal equivalence test with the bound set above the measured CI."
  },
  {
   "id": "P5",
   "depends_on": "Phase 2 completion of all eight subsets of (a,b,x) for CONFLICT, REDUNDANT and CONTROL under the same seeds; per-set top-item agreement between phi_LOO and exact Shapley, minus the no-op-repeat disagreement rate.",
   "falsifier": "excess top-item disagreement over CONTROL below 5 points.",
   "label": "near_entailed",
   "reason": "With all eight subsets measured, phi_SH(i) - phi_LOO(i) is a fixed linear function of the same interaction terms P1 to P4 report, and the REDUNDANT construction forces phi_LOO(a) = phi_LOO(b) about 0 while Shapley splits the Phase 0-gated >= 15 net gain between the two copies, so the disagreement excess restates the manufactured redundancy rather than testing the estimator, and the falsifier would require CONTROL disagreement to rise to match it.",
   "fix": "Report the excess separately per class and make the confirmatory claim on natural unmanufactured k=3 sets, keeping REDUNDANT as a construction check only."
  },
  {
   "id": "P6",
   "depends_on": "4 seeds per (game, seed) cell; split-half sign agreement of per-set phi_LOO as a function of seed count; no-op repeat flip rate.",
   "falsifier": "2 seeds already give split-half sign agreement >= 0.9.",
   "label": "unresolvable",
   "reason": "With only 4 seeds per cell a split-half at 4 seeds per half is never measured, so the >= 4 seeds side cannot be evaluated at all, and at 2 seeds per half the statistic is dominated by tied zero-valued LOO cells whose treatment in the sign-agreement rule is left unspecified, so the falsifier can be manufactured or destroyed by that convention.",
   "fix": "Run 8 seeds on a subsample so genuine 4-vs-4 halves exist, and pre-register how zero or tied per-set LOO values count in the sign-agreement statistic."
  },
  {
   "id": "P7",
   "depends_on": "Phase 4 CONFLICT cells with x replaced by a natural cross-type item (and by the natural rank-2 same-type item), compared against the Phase 1 CONFLICT masking term; each class mean at +/-5 net.",
   "falsifier": "the CONFLICT masking term changes by >= 10 net under the background swap.",
   "label": "unresolvable",
   "reason": "A three-body masking effect is reachable, but the estimand is a difference of two class-mean interaction terms each at +/-5 net, giving roughly +/-7 net on the difference, wider than the 6-net gap between the <= 4 net prediction and the 10-net falsifier.",
   "fix": "Size the background-swap arm so the difference-of-differences CI is under 3 net, or set the falsifier above the propagated CI."
  }
 ],
 "shared_terms": [
  "P1-P5: with all eight subsets measured, phi_SH(i) minus phi_LOO(i) is a fixed linear function of the same interaction terms I that P1 reports, so the REDUNDANT interaction value determines the REDUNDANT rank-disagreement rate.",
  "P2-P5: the CONFLICT interaction uses f(a,x) = f(S-b) and f(x) = f(S-ab), the same measured cells that set P2's own threshold and that enter the Shapley values scored in P5.",
  "P2-P7: P7's estimand is the same CONFLICT masking term as P2 recomputed with a different x, so P2's measurement noise propagates into P7 unchanged.",
  "P1-P6 (and P2-P4-P6): split-half sign agreement of per-set LOO is computed from the same per-cell f(S), f(S-a), f(S-b) values that produce every class interaction, so the seed-count estimand inherits the same flip rate it is meant to characterise."
 ],
 "headline": "P1",
 "headline_status": "near_entailed",
 "n_open": 1,
 "n_entailed": 0,
 "n_near": 2,
 "n_unresolvable": 4,
 "verdict": "revise"
}

=== BINDING RULES FROM THE BRIEF ===
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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).


GATE NOTE (Stage 2.5, Opus adjudication): this proposal was judged "same claim reworded" relative to the sibling proposal masked_harm_pairwise_removal (same manufactured k=3 conflict/redundant/complementary sets, same pairwise-interaction-vs-Shapley claim). In the revision, either differentiate the central claim so that it is not contained in that sibling (a different manipulated variable or estimand), or, if that is not possible honestly, keep the design but state in "Not a restatement of" what the sibling cannot show.
