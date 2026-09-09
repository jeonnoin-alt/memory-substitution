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
 "Name": "recall_success_dissociation",
 "Title": "Recall Ranks Retrievers, Success Does Not: A Two-Environment Audit of Experience Retrieval Against the Static Prompt with Manipulated Duplicate Availability",
 "Short Hypothesis": "Retriever recall (fraction of top-k items sharing the test task's type or binding) and the task-success residual over the best static prompt dissociate, and the dissociation is set by whether the retrieved binding is recoverable inside the episode. On ALFWorld, the residual over the best static arm is a step at type recall (random-type retrieval loses, BM25 and an oracle same-scene retriever sit within the floor) and is unchanged when same-scene items are removed from the bank, because object locations are recoverable by looking; on WebShop, where the binding (which product satisfies the attribute set) is expensive to recover by search, the residual appears only when a same-product trajectory is in the bank and tracks product recall. Recall above the type threshold is therefore uninformative unless the bank carries non-recoverable bindings, and retriever evaluation must report success residual over the static arm at two duplicate-availability levels.",
 "Related Work": "2604.04949 trains retrievers from agent trajectories and reports evidence recall and task success together with no random or fixed control, so recall and success are never dissociated. 2512.20854 correlates retrieval metrics with LLM-judged answer quality in RAG QA and 2508.05909 tries to isolate the retriever's contribution to a reader; both are single-turn QA with no static arm. 2603.02473 finds retrieval dominates write strategy on LoCoMo (QA, no full-history or fixed arm). SWE-ContextBench (2602.08316) shows correctly selected related-task experience helps and mis-selected experience harms on dependency-linked tasks, without a random or static control; 2607.10608 shows wrong retrieved memory is adopted at the first decision point. Traj-Bootstrap (2505.00234) and ExpeL/Reflexion report ALFWorld and WebShop memory gains over no memory only. Measurement A on this node observed unseen approximately equal to seen with one retriever and no static arm. Archived decorative_retriever (5.75) observed retrieval-set overlap without manipulating it.",
 "Abstract": "Retrievers for agent memory are ranked by recall of relevant items; whether that ranking survives when the outcome is task success over the best static prompt is unknown, and it should depend on whether the retrieved item carries something the agent cannot recover in the episode. We manipulate two things on two environments: retriever recall (random-type, goal-BM25, oracle same-binding, at matched k=3) and the bank's duplicate availability (with versus without items sharing the test task's binding: scene on ALFWorld, goal product on WebShop). Every retrieval cell is reported as the success residual over the best static arm built from the same bank (fixed exemplars, compiled procedure, whole bank where it fits), paired on games and seeds, with Qwen3-32B. The prediction is a dissociation: on ALFWorld the residual is a step at type recall and flat above it, unaffected by removing same-scene items; on WebShop the residual appears only when a same-product trajectory is in the bank and tracks product recall, and vanishes when duplicates are removed. A positive control (retrieval over no memory clearing the floor on WebShop) gates the second environment. The audit yields a rule for evaluating experience retrievers: report success residual over the static arm under two duplicate-availability levels, and treat recall above the type threshold as uninformative unless the bank carries bindings the episode cannot recover.",
 "Experiments": "E0 ALFWorld reuse: A (k=0; BM25 k=3) and C (static arms; the best static arm chosen on pooled cells). E1 ALFWorld retriever ladder at k=3, 274 x 2 each: random-type (uniform over the bank, type recall about 1/6), goal-BM25 (A, type recall about 1), oracle same-type-same-scene on valid_seen (binding recall 1; on valid_unseen it reduces to same-type); C's different-type placebo serves as the recall-0 point; 1,644 episodes (~1.5 h). E2 ALFWorld duplicate manipulation: BM25 k=3 with a per-game bank filter excluding same-scene items on valid_seen, paired with A's k=3; 548 episodes. E3 WebShop setup (one day) and bank: Qwen3-32B run on 3,000 train instructions at k=0; successes form bank-full; per test instruction, bank-dup (full) and bank-nodup (items whose goal product equals the test goal product removed); achieved same-product rates reported (target at least 30% versus 0%); the public human demonstrations are added if the self-success rate is thin. E4 WebShop arms, 500 test instructions x 2 seeds each: k=0; static arms: fixed 3 exemplars (token-matched to k=3), compiled procedure (~80 tokens, written by rule from the bank), whole-bank-in-context up to 16k with shortest-first truncation; retrieval k=3: random, instruction-BM25, oracle same-product, each under bank-dup and bank-nodup (cells that coincide are shared); about 10.5k episodes (~8 h). E5 gate: WebShop BM25 k=3 over k=0 must clear the floor before any residual claim. E6 analysis: for each retriever and bank level, recall@3 (type or category recall; binding recall = same scene or same product) and success residual over the best static arm at that bank level; residual plotted against binding recall for both environments; residual per uncached prefill token reported as the cost axis.",
 "Baselines and Ablations": "Baselines (static arms first, per the brief): k=0; fixed 3 exemplars token-matched to k=3; compiled procedure prompt; whole-bank-in-context where it fits; on ALFWorld the C arms including the type-agnostic 6-procedure prompt. Manipulations: retriever ladder (random-type, BM25, oracle same-binding) and bank duplicate availability (dup versus nodup) on both environments. Ablations: k=1 versions of oracle and BM25 on WebShop (residual is not a length effect); type-agnostic procedure-only static on WebShop versus fixed exemplars; random-type retrieval on WebShop with bank-dup (isolates the item content from the binding).",
 "Falsifiable Predictions": "P1 (ALFWorld step): the residual over the best static arm is at or below minus 8 net for random-type retrieval and within ±8 for BM25 and oracle same-scene. Falsified by an oracle residual above 8 net (scene bindings carry value that the static arm lacks), produced by the oracle arm on valid_seen; or by random-type retrieval within ±8 of the static arm (procedures do not matter, contradicting A), produced by the random-type arm. P2 (ALFWorld manipulation): excluding same-scene items changes the BM25 k=3 residual by less than 8 net. Falsified by a drop of at least 8 net, produced by E2. P3 (WebShop manipulation): under bank-nodup every retriever's residual over the best static arm is within the floor; under bank-dup, oracle same-product and BM25 residuals are at least 8 net with oracle at or above BM25. Falsified by a residual of at least 8 net under bank-nodup (retrieval carries value beyond duplicates, for example category search strategies), produced by the bank-nodup BM25 or oracle arm; or by oracle same-product within the floor under bank-dup (a duplicate trajectory does not transfer the binding), produced by the bank-dup oracle arm. P4 (cross-environment): the slope of residual on binding recall is within the floor on ALFWorld and at least 8 net per unit recall on WebShop under bank-dup. Falsified by same-sign slopes of the same size on both environments, produced by the two ladders jointly. P5 (gate, positive control): WebShop BM25 k=3 beats k=0 by at least the WebShop floor. If falsified, produced by E5, the WebShop side is declared uninformative and P3/P4 are not claimed.",
 "Measurement and Noise Control": "ALFWorld: paired (game, seed) cells with A and C on 274 x 2, ±8 net floor; the best static arm is chosen on pooled cells across both splits so no per-split winner is selected; margins as fractions of the Gate-0 gain (+27/+32). WebShop: 500 x 2 paired cells; the floor is estimated from two independent k=0 replicates with different seed pairs before any claim (expected about ±6 net) and the larger of that estimate and ±8 is used; success (score = 1) primary, WebShop score secondary; residuals with bootstrap CIs over instructions (1,000 resamples, jointly across arms). Recall computed per episode from retrieved item ids. Per-category WebShop and per-type ALFWorld results exploratory. Pre-registration of retriever definitions, bank filters, truncation rules and floors before E1.",
 "Preprint Collision Check": "home: 'retrieval quality downstream accuracy correlation RAG' (no recency; channel s2+hf): 2512.20854 How important is Recall (retrieval metrics versus LLM-judged answer quality, QA), 2601.17532 IGP, 2508.05909 Spectrum Projection Score (isolating the retriever's contribution to a reader, QA), 2511.19481, 2509.09651; none on task success over a static arm or on duplicate availability. Mechanism, last twelve months: 'retrieval recall does not predict downstream task accuracy dissociation retriever metrics end-to-end' (--recent; s2+hf): 2603.02473, 2606.21249, 2506.08184; nothing on the dissociation. 'retriever evaluation metrics correlation with end-task generation accuracy nDCG recall downstream' (s2+hf): no results. Closest method: 'WebShop ALFWorld trajectory retrieval exemplars experience memory static prompt comparison' (--recent; s2+hf): Traj-Bootstrap 2505.00234 (verified via paper lookup, s2), 2605.16986 Skills on the Fly (retrieves training trajectories, synthesizes skills, no random or static control), 2604.20572 ProactAgent, 2607.10608 compliance trap, 2605.29463, 2605.12493, 2608.20707. No paper manipulates duplicate availability and retriever recall on two agent environments against a static arm.",
 "Risk Factors and Limitations": "WebShop install plus bank generation is a day and about two GPU-hours; if Qwen3-32B's WebShop success is low, the bank is thin and the same-product rate under bank-dup may be small, with the public human demonstrations as the fallback. WebShop's graded score is reported as secondary; the success dichotomy drives the floor. The oracle same-scene retriever exists only on valid_seen. Two environments are two points; the rule is a prediction to test on a third. The WebShop whole-bank arm is truncated (items are longer) and reported with its truncation rule. If P5 fails, the cross-environment claim is not made and the ALFWorld step result stands alone.",
 "Addresses gap": "G23 (memory benchmarks score recall, not downstream task success) with G22 (random or fixed selection control at matched length); cross-environment generality per the axis definition.",
 "Not a restatement of": "Brief bullet 'Retrieval on this node (Measurement A): unseen approximately equal to seen, so the retrieved value is the type's procedure, not the scene': A observed the split difference with one retriever and no static arm; this idea manipulates retriever recall (random-type, BM25, oracle same-binding) and bank duplicate availability on two environments and claims the recall-to-residual map is a step at type recall on ALFWorld but continues through binding recall on WebShop. Nearest digest card 2604.04949 (trajectory-trained retrievers improve evidence recall and task success): it reports both metrics moving together without a random or fixed control; this idea claims recall gains above the type threshold do not translate to success on template environments and that the translation is set by the bank's duplicate availability. Archived decorative_retriever (5.75) observed overlap; this idea manipulates it and adds a second environment."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "recall_success_dissociation",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "E1 ALFWorld ladder at k=3 (random-type, goal-BM25, oracle same-type-same-scene scored on valid_seen, C's different-type placebo as recall 0) on 274 x 2, residual taken over the best static arm chosen as the maximum over C's static arms on pooled cells.",
   "falsifier": "Oracle residual above 8 net, or random-type retrieval within +-8 of the best static arm.",
   "label": "open",
   "reason": "Both branches are measured on paired full-size cells with the oracle at binding recall 1 on the split where it is scored, so neither is excluded, though the comparator is a maximum over several static arms selected on the very cells the residual is computed on - a winner's curse of roughly 2-3 net that biases both residuals toward the prediction and that choosing the static arm on a held-out seed would remove.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "E2, BM25 k=3 with a per-game bank filter excluding same-scene items on valid_seen (548 episodes) paired with A's unfiltered k=3; E6 computes same-scene binding recall but no gate conditions P2 on it.",
   "falsifier": "The BM25 residual drops by at least 8 net when same-scene items are removed.",
   "label": "near_entailed",
   "reason": "The deletion can only bite if unfiltered goal-BM25 actually returns same-scene items often, and since BM25 matches goal text rather than scene the filter may be a near no-op whose base rate the design measures but never requires, so the falsifier is reachable only through a retrieval rate the proposal neither states nor controls.",
   "fix": "Gate P2 on a pre-registered minimum same-scene fraction in unfiltered BM25 top-3 (the analogue of E3's 30% same-product target), or run the manipulation on the oracle same-scene arm where binding recall is 1 by construction."
  },
  {
   "id": "P3",
   "depends_on": "E4 WebShop arms on 500 x 2 under bank-dup and bank-nodup, residual over the best static arm re-selected at each bank level (the whole-bank-in-context static arm's contents themselves change with the filter), conditional on the E5 gate and on E3's achieved same-product rate, which is reported but not gated.",
   "falsifier": "Any retriever's residual at or above 8 net under bank-nodup, or oracle same-product within the floor under bank-dup.",
   "label": "open",
   "reason": "Both branches are reachable on full-size paired cells - category-strategy transfer could survive de-duplication and a duplicate trajectory could fail to transfer the binding - though the comparator is re-selected per bank level so a residual change across levels confounds retriever with baseline, and the second branch can fire trivially if the achieved same-product rate misses its 30% target.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "The two ladders jointly: ALFWorld binding recall takes only the values 0 (random-type, BM25) and 1 (oracle same-scene), WebShop only the bank-nodup and bank-dup levels; no CI, MDE or fitting procedure is stated for a slope.",
   "falsifier": "Same-sign slopes of the same size in both environments.",
   "label": "near_entailed",
   "reason": "Each environment supplies only two effective binding-recall levels, so the slope is an arithmetic restatement of P1's oracle-minus-BM25 gap and P3's dup-minus-nodup gap rather than an independent test, and the stated falsifier is strictly narrower than the prediction's negation (a large ALFWorld slope with a flat WebShop slope contradicts the prediction but is not counted), so falsification runs only through thresholds and mechanisms the proposal does not define.",
   "fix": "Build intermediate duplicate-availability banks (about 25/50/75% same-binding coverage) in both environments so the slope is fit on at least three recall levels with a bootstrap CI, state a slope MDE, and define the falsifier as the negation of each clause separately."
  },
  {
   "id": "P5",
   "depends_on": "E5 gate: WebShop BM25 k=3 vs k=0 on 500 x 2 paired instructions against a floor set as the larger of +-8 and a two-replicate k=0 estimate (expected about +-6).",
   "falsifier": "BM25 k=3 fails to beat k=0 by the WebShop floor.",
   "label": "open",
   "reason": "The comparison is well powered on 1,000 paired instructions and a 32B model may genuinely fail to gain on WebShop, so the outcome is reachable and distinguishable - but it is a gate whose failure withdraws P3 and P4 rather than counting against the hypothesis, so it can never come out against the thesis.",
   "fix": ""
  }
 ],
 "shared_terms": [
  "P1-P4: the ALFWorld half of P4's slope is computed from the same oracle and BM25 residuals as P1 over only two binding-recall levels, so P1's oracle clause determines it.",
  "P3-P4: the WebShop half of P4's slope is the bank-dup minus bank-nodup residual difference from P3's own cells, so P3 determines it.",
  "P1-P2-P3: every residual subtracts the same 'best static arm' term, selected as the maximum over static arms on the same cells, so its winner's-curse inflation shifts all of them in one direction.",
  "P3-P5: P5's gate and P3's bank-dup BM25 residual share the same WebShop BM25 k=3 success term."
 ],
 "headline": "P4",
 "headline_status": "near_entailed",
 "n_open": 3,
 "n_entailed": 0,
 "n_near": 2,
 "n_unresolvable": 0,
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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
