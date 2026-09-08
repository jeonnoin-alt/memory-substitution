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
 "Name": "binding_scope_leakage_ladder",
 "Title": "Global Fact, Scene Table, or Instance Replay: The Scope of Instance Bindings Sets How Much of a Memory Gain Is Near-Duplicate Leakage and Whether a Static Prompt Can Match It",
 "Short Hypothesis": "An experience bank helps on a new task instance only through information that transfers from bank items to that instance; the scope of the instance bindings (global rule, per-scene, per-instance) determines the smallest compiled substitute for retrieval (one sentence, a row table, none) and how much of the retrieval gain is near-duplicate leakage. At instance scope the gain exists only through duplicates of the evaluation instance in the bank and is linear in the duplicate rate with zero intercept; at global scope one compiled sentence matches retrieval and the duplicate rate is irrelevant beyond one item per class.",
 "Related Work": "Evo-Memory (arXiv:2511.20857) and ReMe (arXiv:2512.10696) measure memory as test-time evolution over task streams without reporting how much of the gain comes from near-duplicate tasks within the stream. EvoMemBench (arXiv:2605.18421) organizes memory by scope (in-episode vs cross-episode) and content, and finds long-context baselines outperform memory methods, but does not manipulate binding scope or duplicate rate. AgentCL (arXiv:2606.02461) builds controlled task streams with transfer-gain metrics, without a compiled-prompt arm or a scope manipulation. SWE-ContextBench (arXiv:2602.08316) draws related tasks from dependency links (observed relatedness). The compliance trap (arXiv:2607.10608) shows adoption of wrong retrieved memory. In the home literature, deduplication of training data (arXiv:2107.06499) and contamination analyses (ConTAM arXiv:2411.03923; rephrased-sample contamination arXiv:2311.04850) quantify score inflation from near-duplicate overlap for pretraining, never for experience banks. Archived order_randomized_leakage_audit audited leakage by order randomization (observed); Measurement A's unseen approximately equal to seen is the starting point.",
 "Abstract": "Memory benchmarks differ in what an experience bank can transfer to a new instance: a rule that holds everywhere, a binding that holds within a scene or site, or a binding that holds only for the instance itself, which the bank contains only if the instance recurs (sequential streams that revisit tasks). We manipulate this scope on ALFWorld using the relocation machinery (target objects moved off their canonical receptacle under a tight step budget, the cell where a binding-bound retrieval residual exists) with three relocation rules: global (every instance of a class goes to the same receptacle type in every scene), scene (per (scene, class)), and instance (per game). The bank's supply is manipulated as the fraction s of evaluation games whose scope unit has a relocated item in the bank (class covered / same-scene sibling present / the game's own earlier successful trial from a first pass present), with s in {0, 0.5, 1} at instance scope and {0, 1} at global and scene scope. Arms: scene-query retrieval k=3, the type-agnostic six-procedure prompt (no bindings), the scope-appropriate compiled static arm (one sentence per class at global scope; a row table at scene scope; none exists at instance scope), a 20-item bank (one relocated item per class) at global scope, a whole-bank 80-item arm at s = 1, and a length placebo. Retrieval is always reported minus the best static arm on the same (game, seed) with cached and uncached prefill tokens logged. The leakage index is the part of the retrieval gain removed by deleting scope-matched duplicates. The design predicts a compiled sentence matches retrieval at global scope, a table at scene scope, nothing but the duplicate itself at instance scope, and a linear zero-intercept dependence on the duplicate rate at instance scope; each prediction names the cell that can refute it.",
 "Experiments": "1. Gate (pre-registered): the scene-scope, s = 1, relocated x 25-step cell must show scene-query retrieval minus type-agnostic static >= +14 net (the positive control shared with the relocation design); if it does not, the ladder is not run and the failure is reported. 2. Construction: three relocation rules applied to the PDDL init of the 274 eval games and of train games in eval scenes; expert trajectories regenerated with the ALFWorld PDDL expert; at instance scope the duplicate is the eval game's own verified success from a first pass by the same reader with the type-agnostic prompt (self-pool style, on-policy), placed in the bank for a fraction s of games chosen by seed. 3. Cells (each 274 x 2 seeds, ~30 min): instance scope: retrieval at s in {0, 0.5, 1}, type-agnostic static, whole-bank at s = 1; scene scope: retrieval at s in {0, 1}, type-agnostic static, table static, whole-bank at s = 1; global scope: retrieval at s in {0, 1}, retrieval with the 20-item one-per-class bank, type-agnostic static, compiled-sentence static, whole-bank at s = 1. About 17 cells, ~9.3k episodes, ~8 h on two A100s. 4. Exploratory: goal-query retrieval at instance scope s = 1 (does goal similarity find the self-duplicate); stale self-duplicate (from the canonical game) at instance scope; per-type breakdown; k=1 at instance scope s = 1. 5. Cost: cached vs uncached prefill per episode; the compiled-sentence and table arms have zero uncached tokens; accuracy-cost curve per scope.",
 "Baselines and Ablations": "Static baselines (cached): type-agnostic six-procedure prompt (no bindings, run at every scope since the games differ); compiled sentence per class (global scope only, ~20 sentences); compiled table per (scene, class) (scene scope; <= 274 rows); whole-bank 80-item arm at s = 1 for every scope (contains the duplicate; information-complete without a query); random-type length placebo. Retrieval: scene-query k=3 (goal plus first observation); ablations: goal-query at instance scope; k=1 and k=7 at instance scope s = 1; 20-item one-per-class bank at global scope vs the full relocated bank; stale duplicate at instance scope. Seeds: the s = 0.5 subset is drawn by seed and the complementary subset is run as a second draw to check that the linear estimate does not depend on which games carry duplicates.",
 "Falsifiable Predictions": "P1 (gate, positive control) At scene scope, s = 1, scene-query retrieval minus type-agnostic static >= +14 net. Falsified by < +8 in that cell; the ladder is then not run. P2 (global scope compiles to a sentence) At global scope, compiled-sentence static minus retrieval (s = 1) >= -8 net. Falsified by sentence < retrieval - 8 in the global-scope sentence cell (the reader applies a concrete trajectory but not a stated rule). P3 (global scope needs one item per class) At global scope, retrieval with the 20-item one-per-class bank is within +-8 of retrieval with the full relocated bank. Falsified by 20-item < full - 8 (a many-shot requirement per class) in the 20-item cell. P4 (scene scope compiles to a table) At scene scope, table static minus retrieval (s = 1) >= -8 net. Falsified by table < retrieval - 8 in the scene-scope table cell. P5 (instance scope: gain is replay) At instance scope, retrieval (s = 1, own earlier trial present) minus type-agnostic static >= +14 net. Falsified by < +8 in that cell (the reader does not exploit even an exact self-duplicate). P6 (linear, zero intercept) At instance scope, retrieval residual at s = 0.5 is within +-8 of half the residual at s = 1, and the residual at s = 0 is <= +8 (control cell; near-entailed by the split and declared as such, not a headline). Falsified by residual(0.5) >= residual(1) - 8 (superlinear: partial duplicates seed a search strategy that transfers to non-duplicated games) or residual(0.5) <= +8 while residual(1) >= +14 (sublinear: the reader trusts duplicates only when they are reliably present); produced by the s = 0.5 cell against the s = 1 cell. P7 (the whole-bank arm does not replace the query at instance scope) At instance scope s = 1, whole-bank 80-item arm <= retrieval - 8. Falsified by whole-bank >= retrieval - 8 in that cell (the reader finds its own trial among 80 items without a query). P8 (exploratory) At instance scope s = 1, goal-query retrieval residual <= scene-query residual - 8; falsified by goal-query within +-8 of scene-query in the goal-query cell.",
 "Measurement and Noise Control": "Task success on identical (game, seed) pairs across arms within each scope; paired nets with a cluster bootstrap over games (1,000 resamples) and 95% CIs; the +-8-net floor at 274 x 2 is the minimum reportable margin; confirmatory margins +14 (half the Gate-0 gain). The s = 0.5 subset is drawn by seed with a complementary second draw so the linear estimate is checked across draws; the same first-pass trajectories are used as duplicates in every arm at instance scope. Same decoding, vLLM build, prompt template and retriever as Measurement A; static prefixes byte-identical with cache hits verified from logs; cached and uncached prefill tokens and wall-clock per episode logged. Gate and predictions pre-registered before the first confirmatory cell; per-type claims exploratory; valid_seen and valid_unseen reported separately and pooled.",
 "Preprint Collision Check": "All queries via tools/ideate2/s2cli.py (S2 + HF; both channels answered each query). (1) mechanism, last 12 months: 'near-duplicate leakage inflates agent memory gains sequential task stream' --recent -> [hf] compliance trap 2607.10608, AgentCL 2606.02461 (controlled task streams, transfer-gain metrics), EvoMemBench 2605.18421 (memory scope in-episode vs cross-episode; long-context baselines beat memory methods), LongMemEval-V2 2605.12493, MEMPROBE 2606.24595, HiMPO 2606.16285, MemoryGraft 2512.16962, Agent Memory Distillation 2608.07169; none manipulates duplicate rate or binding scope or reports a compiled-prompt arm. (2) closest named method: 'ReMem ExpRAG test-time evolution agent memory sequential tasks' -> [hf/s2] Evo-Memory 2511.20857 (123 citations), [hf] ReMe 2512.10696, REMem 2602.13530, AdaMEM 2606.05684, MemPro 2606.00619, EvoMemBench 2605.18421, MindMemOS 2608.12428; none reports gain as a function of duplicate rate or against a compiled sentence or table. (3) home: 'near-duplicate train test overlap contamination score inflation' -> [hf] Deduplicating Training Data Makes Language Models Better 2107.06499, ConTAM 2411.03923, rephrased-sample contamination 2311.04850, Time Travel in LLMs 2308.08493, Investigating Data Contamination 2311.09783, HackDetect 2607.22368; the contamination literature quantifies score inflation from overlap for pretraining corpora, never for experience banks or as a function of binding scope. (4) verification: 's2cli.py paper 2605.18421' -> [s2] EvoMemBench, two axes memory scope and memory content (scope there means in-episode vs cross-episode, not binding scope); 's2cli.py paper 2606.02461' -> [s2] AgentCL, controlled task streams and MemProbe. No collision found on manipulating binding scope or duplicate rate against compiled static arms.",
 "Risk Factors and Limitations": "The ladder depends on the relocation positive control (gate); if no binding-bound residual exists on ALFWorld the design yields only the gate failure. Instance-scope duplicates come from the reader's own first-pass successes, so their coverage is limited to games the reader solved once (about 55-60% at k=0; the s ladder is defined over those games, reducing n and widening the floor to roughly +-11 net, which the margins still exceed). Global-scope relocation to a single receptacle type per class may be impossible for some (scene, class) pairs (receptacle absent); those games are dropped with counts. The compiled sentence at global scope is written by rule, favouring the compiled arm relative to model-written playbooks. Scope is manipulated on one environment; the cross-environment claim that a bank statistic (binding scope entropy) predicts the residual sign is stated as a follow-up on WebShop, not measured here. Two seeds only.",
 "Addresses gap": "G10 (how much of the benefit of experience retrieval depends on task relatedness or near-duplication within the stream, with token cost and scaling with memory size unreported): the duplicate rate and the binding scope are manipulated, the leakage share is measured against compiled static arms, and cached/uncached token cost per scope is logged.",
 "Not a restatement of": "Brief bullet 'Measurement A: unseen approximately equal to seen, so the retrieved value is the type's procedure, not the scene': this idea claims that the seen-unseen gap is a leakage index that the binding scope moves from zero (global scope) to the whole retrieval gain (instance scope with self-duplicates), and that the compiled substitute shrinks from a sentence to a table to nothing along the same ladder, which the bullet does not state. Digest card arxiv:2511.20857 (Evo-Memory): this idea claims the stream gain at instance scope is linear in the duplicate rate with zero intercept and has no compiled substitute, while at global scope one sentence substitutes and one item per class suffices, none of which that card measures because the duplicate rate within its streams is neither controlled nor reported. Archived order_randomized_leakage_audit observed leakage by reordering; here the scope and rate of duplicates are manipulated."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "binding_scope_leakage_ladder",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "The pre-registered gate cell shared with the relocation design: scene scope, s=1, relocated x 25 steps, scene-query k=3 vs type-agnostic static, 274 x 2 seeds.",
   "falsifier": "Residual < +8 net in that cell, in which case the ladder is not run and the failure is reported.",
   "label": "open",
   "reason": "Reader application failure is a reachable outcome and a near-null reading's +-8 CI excludes the predicted +14, so the gate is decidable.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "Global-scope compiled-sentence static (~20 one-per-class sentences) vs scene-query retrieval at s=1 with the full relocated bank; no gate requires a global-scope retrieval gain first.",
   "falsifier": "Sentence < retrieval - 8 net (the reader applies a concrete trajectory but not a stated rule).",
   "label": "open",
   "reason": "The exemplar-over-rule application gap is a reachable, named mechanism and the falsifier needs a reportable 8-point gap, but without a global-scope positive control the prediction is confirmed vacuously whenever global-scope retrieval shows no gain at all.",
   "fix": "Add a global-scope positive control (retrieval at s=1 minus type-agnostic static >= +14) as a precondition for reading P2."
  },
  {
   "id": "P3",
   "depends_on": "Global-scope retrieval k=3 over the 20-item one-per-class bank vs retrieval over the full relocated bank.",
   "falsifier": "20-item < full - 8 net (a many-shot per-class requirement).",
   "label": "open",
   "reason": "A thin 20-item bank can plausibly return wrong-class items and lose by a reportable margin, so the falsifier is reachable; only the one-sided direction is falsifying, which the proposal states.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "Scene-scope compiled table (<= 274 (scene, class) rows) vs scene-query retrieval at s=1, run only after the P1 gate passes.",
   "falsifier": "Table < retrieval - 8 net in the scene-scope table cell.",
   "label": "open",
   "reason": "A 274-row lookup can fail by a reportable margin and, unlike P2, the P1 gate guarantees a non-null retrieval level so the non-inferiority test is not vacuous.",
   "fix": ""
  },
  {
   "id": "P5",
   "depends_on": "Instance scope, s=1: scene-query retrieval vs type-agnostic static, where the planted duplicate is the eval game's own verified success from a first pass by the same reader with the type-agnostic prompt.",
   "falsifier": "Residual < +8 net (the reader does not exploit even an exact self-duplicate).",
   "label": "open",
   "reason": "The falsifier is not merely reachable but close to forced by construction: duplicates exist only for games the type-agnostic prompt already solved, so the attainable residual is capped by first-pass/eval-seed disagreement rather than by whether the reader exploits the duplicate.",
   "fix": "Source instance-scope duplicates independently of the baseline's outcome (regenerated expert trajectories of the same instance, or a first pass under a different arm) so failed games can also carry a duplicate."
  },
  {
   "id": "P6",
   "depends_on": "Instance-scope residuals at s = 0, 0.5, 1 with the duplicate subset drawn by seed plus a complementary second draw; the bands are defined against residual(1) from P5.",
   "falsifier": "residual(0.5) >= residual(1) - 8 (superlinear) or residual(0.5) <= +8 while residual(1) >= +14 (sublinear).",
   "label": "unresolvable",
   "reason": "At the smallest residual(1) that P5 admits (+14 to +16) an exactly linear residual(0.5) of 7-8 trips both falsifiers at once, so the predicted outcome is auto-falsified, and the +-8 tolerance is as large as the half-residual under test; the s=0 intercept clause is additionally entailed by the split, since an instance-scope bank with no duplicate holds nothing keyed to the eval instance, as the proposal concedes.",
   "fix": "Require residual(1) >= +32 before reading linearity (so half the residual clears the floor), or fit slope and intercept over s in {0, 0.25, 0.5, 0.75, 1} with a bootstrap CI on the intercept."
  },
  {
   "id": "P7",
   "depends_on": "Instance-scope whole-bank 80-item arm at s=1 (which contains the duplicate) vs scene-query retrieval in the same cell.",
   "falsifier": "Whole-bank >= retrieval - 8 net (the reader finds its own trial among 80 items without a query).",
   "label": "unresolvable",
   "reason": "Falsification requires establishing a difference smaller than the stated +-8 floor, which the cluster-bootstrap CI cannot separate from the predicted -8.",
   "fix": "State it as whole-bank <= retrieval - 14, or power the comparison so an 8-point difference is excludable."
  },
  {
   "id": "P8",
   "depends_on": "The exploratory goal-query retrieval cell at instance scope s=1 against the scene-query cell, where the duplicate is the eval game's own trajectory.",
   "falsifier": "Goal-query residual within +-8 of the scene-query residual.",
   "label": "unresolvable",
   "reason": "The falsifier is a sub-floor difference the stated CI cannot resolve, and it is close to forced anyway because the self-duplicate carries the eval game's goal string verbatim, so goal similarity retrieves the same item and the confirming direction is excluded by construction.",
   "fix": "Predict goal-query <= scene-query - 14 and make the indexed duplicate's goal text differ from the eval query (index on the trajectory or a paraphrase) so goal similarity is not an exact match."
  }
 ],
 "shared_terms": [
  "P5-P6-P7-P8: instance-scope retrieval at s=1 is a measured term in all four; its level sets P6's falsifier bands, P7's threshold and P8's comparison, so one arm decides four predictions.",
  "P5-P6: P6's superlinear and sublinear bands are algebraic functions of residual(1) measured in P5, so P5's outcome determines whether P6 can pass at all.",
  "P1-P4: the scene-scope retrieval (s=1) success is a shared term in the gate and in the table non-inferiority test.",
  "P2-P3: global-scope retrieval at s=1 over the full relocated bank is a measured term in both.",
  "P2-P4 (form): both are non-inferiority tests of a compiled static against retrieval and are auto-confirmed whenever the matching retrieval residual is null; P4 is protected by the P1 gate, P2 has no equivalent gate."
 ],
 "headline": "P6",
 "headline_status": "unresolvable",
 "n_open": 5,
 "n_entailed": 0,
 "n_near": 0,
 "n_unresolvable": 3,
 "verdict": "revise"
}

=== BINDING RULES FROM THE BRIEF ===
## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **The static arm is the baseline, not an ablation.** Every retrieval claim is reported as retrieval minus the best
  static alternative built from the same experience at matched tokens (fixed exemplars, compiled procedure, whole bank
  in context where it fits), on the same (game, seed).
- **Type conditioning is controlled.** On template environments the goal sentence gives away the task type; a
  "no-retriever" arm that selects by type is a type-conditioned prompt, and a type-agnostic arm (all procedures, or a
  fixed exemplar of a random type) must also be run.
- **The environment property is manipulated, not named.** Claims of the form "retrieval is needed when X" require at least
  two levels of X built into the bank or the task set (near-duplicate rate, instance-specific bindings, procedure count,
  distractor items) on one environment, or the same manipulation on two environments.
- **Task success, not recall**, is the primary outcome; retriever metrics are secondary.
- **Whole-bank long-context arm** whenever the bank fits the 16k context (it does for ALFWorld at ~140 tokens per item up
  to ~80 items; larger banks need a stated truncation rule).
- **Cost accounting under caching.** Prefill tokens per episode for static (cached) and retrieved (uncached) prefixes are
  logged; accuracy–cost curves, not accuracy alone.
- **Variance:** paired cells, ±8 net floor at 274 × 2; margins as fractions of the Gate-0 retrieval gain; per-type claims
  on pooled cells or declared exploratory.
- **No prediction entailed by a definition** (a whole-bank arm that contains the retrieved items cannot lose information;
  a type-conditioned static arm on a six-template benchmark equals retrieval by construction unless bindings matter);
  per prediction, the falsifying outcome and the arm that can produce it.
- **Home-vocabulary search**: in-context example selection, demonstration retrieval vs random demonstrations, few-shot
  saturation, long-context vs RAG, prompt compression; one query without agent/memory/benchmark words.
- **Must pass the four archived ideas** on this question (appendix A) by manipulating what they only observed.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
