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
 "Name": "bindings_need_a_query_only_when_untestable",
 "Title": "A Query Is Needed Only for Untestable Bindings: Planted Scene-Level Procedure Bindings Separate Compiled Rules, Compiled Tables and Scene-Keyed Retrieval",
 "Short Hypothesis": "Instance-specific bindings make query-time retrieval necessary only when the binding cannot be tested at run time. Planting scene-level bindings in ALFWorld (which of two same-looking appliances performs heat/cool/clean is fixed per kitchen and invisible in the observation) under two feedback regimes (testable: a wrong attempt returns 'Nothing happens'; untestable: it returns the normal success message and the failure surfaces only at the goal check) creates a retrieval residual over the best compiled artifact under the untestable regime only; under the testable regime a 60-token compiled rule with a run-time test matches scene-keyed retrieval at zero uncached prefill, and a compiled per-kitchen table keyed on the observation matches it under both.",
 "Related Work": "On this node the retrieval gain is scene-independent (unseen ~ seen) because ALFWorld's object placements are per-instance and its procedures per-type; the brief asks that the property that would make a query necessary be manipulated, not named (Q2). SGR-Bench (2605.22219) shows search agents fail by establishing the wrong site-specific state and leaves untested whether stored site procedures or prior trajectories would fix it; Mem2ActBench (2601.19935) shows memory-grounded parameters are mishandled but does not separate retrieval from application; SWE-ContextBench (2602.08316) shows related-task experience helps only when correctly selected. 'When Agents Commit Too Soon' (2606.22936) diagnoses silent failures from premature commitment but does not manipulate whether feedback exists. ICAL (2406.14596) and task-recognition-vs-task-learning (2305.09731) frame what demonstrations supply without a run-time-testability axis. Archived decorative_retriever (5.75) observed overlap; abstraction_discards_bindings_and_repairs (5.95) posited that abstraction loses bindings; here bindings are planted, the compiled table keeps them, the compiled rule recovers them by testing, and the feedback regime that decides between them is manipulated. Agent Workflow Memory-style induced workflows are the nearest compiled form; the searched literature returned no version of it with a run-time test or a bindings manipulation.",
 "Abstract": "Whether an agent needs to query its experience or can use a prompt compiled once depends on whether the task carries bindings that only past experience reveals. We make that property in ALFWorld: a text wrapper swaps, in a random half of the kitchens (q = .5), the names of the procedure-critical receptacle instance and a same-scene distractor (microwave 1 <-> stoveburner 1 for heat; fridge 1 <-> cabinet 1 for cool; sinkbasin 1 <-> a same-scene basin or countertop for clean), so the observation looks identical in swapped and unswapped kitchens and only bank items from the same kitchen carry the binding. A second wrapper level sets the feedback regime: testable (a wrong-appliance attempt returns 'Nothing happens') or untestable (it returns the normal success string without changing state). The expert bank is regenerated under the wrapper and replay-validated; 200 procedure-type train games are held out of the bank as extra seen-kitchen test games. Arms on the same cells: k=0; goal-keyed top-3 retrieval (blind to scene); scene-keyed top-3 retrieval (query = initial observation + goal); the stale six-procedure playbook; the playbook plus a compiled per-kitchen table (kitchen signature -> which name heats/cools/cleans, ~900 tokens, cached); the playbook plus a 60-token run-time-test rule; the same table with rows permuted (token placebo); and the whole bank of 80 items in context. Task success on procedure-type games in swapped kitchens is primary; a seen-unseen gap is predicted to appear for scene-keyed routes under the untestable regime. The claim: bindings alone do not make a query necessary; untestable bindings do, and even then a compiled table keyed on the observation matches the query.",
 "Experiments": "Wrapper: regex renaming layer over the TextWorld observations and inverse mapping over actions; swap assignment per kitchen fixed by seed with q = .5 (q = 0 is the current environment; both levels run); feedback regime {testable, untestable} implemented by rewriting the environment's response to the wrong-appliance action. Bank: expert pool re-rendered under the wrapper (text renaming of the affected steps), each item replayed and kept only if success = 1 under its kitchen's swap state; 200 procedure-type train games excluded from the bank as extra seen-kitchen test games (primary seen cell ~ (70 + 200) x .5 swapped x 2 seeds ~ 270 paired episodes, floor +-12); valid_unseen kitchens (no bank items) form the unseen cell. Arms per regime under q = .5 (A1-A8, each on all test games x 2 seeds): A1 k=0; A2 goal-keyed retrieval k=3 (A's retriever; exposure to the wrong binding is .5 by construction in swapped kitchens); A3 scene-keyed retrieval k=3 (embedding of initial observation + goal; same-kitchen items retrievable for seen games only); A4 stale playbook (C's 400 tokens); A5 playbook + compiled per-kitchen table (~30 kitchens x 3 lines, keyed by the receptacle inventory of the initial observation, compiled by rule from the bank); A6 playbook + run-time-test rule (60 tokens: 'try the named appliance; if nothing happens, use the other one'); A7 whole-bank_80 (type-balanced, cached; games split by whether a same-kitchen same-type item is in the context); A8 table placebo (A5 with kitchen rows permuted, same tokens). Under q = 0: A3, A5, A6 added to the existing A/C cells to check they do not hurt when no bindings exist. Count: 16 arms under q = .5 plus 3 under q = 0, ~30-45 min each (~11 h on two A100s), plus one day for the wrapper and bank regeneration. Step counts and uncached prefill per episode logged. Order: manipulation check (A4 under untestable) first; then A3/A5/A6 under each regime; then placebo and whole-bank.",
 "Baselines and Ablations": "Baseline is the best static arm per regime (A4/A5/A6), retrieval reported as retrieval minus best static; type-agnostic static arms throughout (A4-A6, A8 contain all six procedures); goal-keyed vs scene-keyed retrieval separates 'having a query' from 'having the right key'; table vs rule separates enumeration from run-time testing; permuted table isolates content from scaffold; q = 0 arms check that the added artifacts are harmless without bindings; the pick types are untouched in-arm controls; seen vs unseen kitchens separate bank-carried bindings from feedback-recovered ones; whole-bank split by presence of a same-kitchen item.",
 "Falsifiable Predictions": "P1 (manipulation check, gate): under untestable, A4 in swapped kitchens loses >= 20 points vs the same games at q = 0 (procedure types; floor +-12; 20 ~ half the Gate-0 gain on these types). Falsified if the loss is < 12 (the agent tries both appliances before committing and the binding has no bite); arm A4 untestable; the study is redesigned if falsified. P2 (testable regime: rule suffices): under testable, A6 minus A4 >= 12 and A3 minus A6 <= +12 on swapped seen kitchens. Falsified if A3 minus A6 >= 12 (a query is needed even when feedback is informative) or if A6 minus A4 < 12 (the rule is not executed); arms A3, A6, A4 testable. P3 (untestable regime: query needed over the rule): under untestable, A3 minus A6 >= 12 on swapped seen kitchens. Falsified if A3 minus A6 < 12 (scene-keyed retrieval does not find or does not use same-kitchen items); arms A3 vs A6 untestable. P4 (a keyed table matches the query): under untestable, A3 minus A5 <= +12 on swapped seen kitchens, and A5 minus A8 >= 12. Falsified if A3 minus A5 >= 12 (the reader cannot route a kitchen signature to its row, so enumerable bindings still need a query) or if A8 is within +-12 of A5 (the table's gain is scaffold); arms A3, A5, A8 untestable. P5 (seen-unseen gap is created): under untestable, A3 and A5 show seen minus unseen >= 12 on swapped-kitchen procedure games, while under testable A6's seen minus unseen is < 12. Falsified if A3's gap is < 12 under untestable (the scene key is not being used) or if A6's gap is >= 12 under testable (the rule needs the bank after all); arms A3/A5/A6 by split. P6 (whole-bank finds the binding only when it is present): under untestable, A7 games with a same-kitchen same-type item in context exceed those without by >= 12. Falsified if the two subsets are within +-12 (the reader does not locate the binding in 11k tokens); arm A7 split. P7 (cost of testing): under testable, A6 uses >= 1.0 more environment steps per swapped episode than A3 (paired mean). Falsified if the 95% CI of the paired difference includes 0; arms A6 vs A3 step logs. Exposure of A2 to the wrong binding at .5 is by construction and is reported, not predicted.",
 "Measurement and Noise Control": "Paired (game, seed, swap state) cells; net = paired success difference in points; floor +-8 at 274 x 2 and +-12 on the ~270-episode primary cell (swapped seen kitchens, procedure types), with the 200 held-out train games pre-registered as test games and excluded from the bank; margins 12 (floor) and 20 (half the Gate-0 gain on the procedure types); bootstrap over games with seeds nested; permutation tests on paired differences; the swap assignment is fixed by a pre-registered seed and a second assignment is run for the headline cells to show the effect is not kitchen-specific. Manipulation check (P1) gates the rest; pick types and unswapped kitchens are in-arm controls that must stay within floor of q = 0. Uncached prefill per episode (A2/A3 ~430 uncached; A4-A6, A8 cached; A7 cached ~11k) and steps per episode logged; results reported on the accuracy-cost plane. Pre-registration before the first confirmatory cell.",
 "Preprint Collision Check": "Q7 (recent, mechanism) 'static instructions versus retrieved trajectories instance-specific bindings agent environment feedback' --recent, channel S2+HF: nothing on the mechanism (2609.04148 Terminal-Universe, 2604.00356 Signals, 2512.01945 INSPO, surveys). Q10 (recent, mechanism, rephrased) 'LLM agent hidden environment variant must be identified from action feedback versus supplied by past trajectories' --recent, channel S2+HF: 2606.22936 'When Agents Commit Too Soon' (silent failures from premature commitment; diagnostic, no testability manipulation, no retrieval-vs-compiled arms), 2607.12397 Critic Experience Bank, 2501.01702 AgentRefine; no pre-emption. home: Q8 'demonstration selection similar versus random demonstrations in-context learning when does selection matter' (no agent/memory/retrieval/experience/benchmark words), channel HF: 2605.13511 Many-Shot CoT-ICL (selection and ordering matter for reasoning tasks), 2506.04579 gradient-matching selection, 2309.07900 ambiguity-aware selection; selection value is tied to label ambiguity, never to whether the selected information can be tested at run time. Q11 (home, second) 'latent task parameter identification from feedback in-context learning versus supplied in demonstrations', channel HF: 2305.09731 (task recognition vs task learning), 2202.12837 (role of demonstrations), 2210.03821 (in-context policy iteration), 2406.14596 ICAL; none manipulates feedback testability. Q9 (closest named method) 'Agent Workflow Memory induce reusable workflows from trajectories', channel S2+HF: AWM itself not returned; 2608.10509 MAP-Graph, 2607.20999 WML, 2606.19911 Multi-Agent Transactive Memory, 2608.07169 Agent Memory Distillation; none plants bindings or compares a run-time-test rule with scene-keyed retrieval. Verdict: no pre-emption found on either channel.",
 "Risk Factors and Limitations": "The manipulation may have no bite if the agent habitually tries both appliances (P1 falsifier); then the wrapper is strengthened (three candidate appliances) before any confirmatory cell. Name swaps are a stylised binding; the claim is about testability, which is a property of real environments (silent UI or API failures), not about renaming. Scene-keyed retrieval depends on the kitchen signature being recoverable from the initial observation (receptacle inventory identifies a floorplan; checked mechanically before running). The primary cell is swapped seen kitchens of three types, so the 200 held-out train games are needed to reach the +-12 floor; if their success distribution differs from valid_seen, they are analysed as a stratum. Only Qwen3-32B; the reader's ability to execute a run-time test or route a table may differ by backbone. Bank regeneration and the wrapper are a day of engineering.",
 "Addresses gap": "G2 (retriever vs fixed/static artifact never isolated): the residual of scene-keyed retrieval over the best compiled artifact is measured under a planted binding with the feedback regime manipulated; G3 (no whole-bank arm): the whole bank is run and split by whether it contains the binding; cross-axis G6/G10 (retrieval vs knowledge never separated; relatedness threshold unmeasured) are attacked by making the binding's testability, not its presence, the manipulated variable.",
 "Not a restatement of": "Prior-result bullet 'unseen ~ seen, so the retrieved value is the type's procedure, not the scene': this idea plants scene bindings so that a seen-unseen gap is created, and claims it appears for retrieval only under the untestable regime while a 60-token compiled rule removes it under the testable one. Digest card arxiv:2605.22219 (SGR-Bench: failures come from the wrong site-specific state; whether stored procedures or prior trajectories would fix it is untested): this idea builds the stored procedures (table and rule) and the trajectory retrieval, and claims that which of them is needed is decided by whether the wrong state is detectable from feedback, a property it manipulates rather than names."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "bindings_need_a_query_only_when_untestable",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "A4 stale playbook (names the pre-swap appliance) in swapped kitchens under the untestable regime vs the same games at q=0, procedure types, floor +-12",
   "falsifier": "loss < 12 (the agent tries both appliances before committing)",
   "label": "entailed",
   "reason": "The wrapper hides which appliance is correct, the stale playbook names the wrong one in every swapped kitchen, and the untestable regime returns a normal success message for the wrong action, so the split never gives the agent any signal that would send it to the other appliance; the >= 20 loss is fixed by the environment rewrite rather than measured.",
   "fix": "Report it as a construction check, not a prediction, and add an A4-with-correct-binding arm under the same regime so the cell measures playbook compliance rather than the determinism of the wrapper."
  },
  {
   "id": "P2",
   "depends_on": "A6 (playbook + 60-token run-time-test rule) vs A4 and vs A3 (scene-keyed retrieval k=3) on swapped seen kitchens under the testable regime, where a wrong attempt returns 'Nothing happens'",
   "falsifier": "A3 minus A6 >= 12 (a query is needed even with informative feedback) or A6 minus A4 < 12 (the rule is not executed)",
   "label": "open",
   "reason": "A6 minus A4 < 12 is squarely reachable, since under testable feedback the A4 agent may recover from 'Nothing happens' on its own without any rule, which would leave the rule with nothing to add.",
   "fix": "None for openness; note the second clause (A3 minus A6 <= +12) is ceiling-limited because both arms recover the binding and neither can exceed the unswapped baseline, so only the first clause carries risk."
  },
  {
   "id": "P3",
   "depends_on": "A3 scene-keyed retrieval (embedding of initial observation + goal, same-kitchen items retrievable for seen games only) vs A6 on swapped seen kitchens under the untestable regime, floor +-12",
   "falsifier": "A3 minus A6 < 12 (scene-keyed retrieval does not find or does not use same-kitchen items)",
   "label": "near_entailed",
   "reason": "A6's rule triggers on 'if nothing happens', which the untestable regime is defined never to emit, so A6 degenerates to the floored A4 cell by construction and the contrast reduces to whether A3 alone works; the falsifier is reachable only through retriever failure, a component the design never estimates separately.",
   "fix": "Report the same-kitchen retrieval hit rate as a pre-registered estimand and add an oracle-scene-retrieval arm, so a null is attributable to the retriever rather than to the claim; state A6's inertness under untestable as a construction fact rather than scoring it as a comparison arm."
  },
  {
   "id": "P4",
   "depends_on": "A5 (playbook + per-kitchen table keyed by the receptacle inventory of the initial observation, compiled by rule from the bank) vs A3 and vs A8 (row-permuted table placebo) on swapped seen kitchens under untestable, floor +-12 on the ~270-episode cell",
   "falsifier": "A3 minus A5 >= 12 (the reader cannot route a kitchen signature to its row) or A8 within +-12 of A5 (the gain is scaffold)",
   "label": "open",
   "reason": "Whether the model can key a ~30-row table by an observation signature is genuinely uncertain and its failure would show directly, so the first clause is reachable.",
   "fix": "Set the equivalence margin above the cell's CI half-width, since 'A3 minus A5 <= +12' is currently satisfied by any undetected difference at the floor; the second clause (A5 minus A8 >= 12) is forced once the first holds, because a permuted table gives actively wrong bindings under untestable."
  },
  {
   "id": "P5",
   "depends_on": "seen minus unseen split for A3 and A5 on swapped-kitchen procedure games under untestable, and for A6 under testable; unseen = valid_unseen kitchens with no bank items",
   "falsifier": "A3's gap < 12 under untestable, or A6's gap >= 12 under testable",
   "label": "entailed",
   "reason": "Unseen kitchens have no same-kitchen items for A3 and no table row for A5 by construction, so both unseen cells are pinned at the floored A4 level and the gap is algebraically the seen-cell value already scored by P3 and P4; symmetrically A6's rule is bank-independent, so its gap is fixed at zero by construction.",
   "fix": "Make the split informative by adding an unseen-kitchen arm that could carry the binding (for example a table compiled from a held-out kitchen sample or retrieval over a bank that includes unseen kitchens), otherwise report the gap as a description of the split rather than as a test."
  },
  {
   "id": "P6",
   "depends_on": "A7 whole-bank_80 (type-balanced, cached, ~11k tokens) under untestable, games split by whether a same-kitchen same-type item happens to be among the 80",
   "falsifier": "the two subsets within +-12",
   "label": "unresolvable",
   "reason": "This is an unpaired between-subset comparison of different games in non-randomised kitchens, whose cell sizes and floor are never stated; the +-12 floor was derived for the ~270-episode paired cell and does not apply, so the falsifier sits inside unquantified noise.",
   "fix": "Randomise inclusion of the same-kitchen item per game so the comparison is paired within game, and pre-register the subset sizes and their floor."
  },
  {
   "id": "P7",
   "depends_on": "step logs for A6 vs A3 on swapped episodes under the testable regime, paired mean difference in environment steps",
   "falsifier": "the 95% CI of the paired difference includes 0",
   "label": "entailed",
   "reason": "In a swapped kitchen the rule prescribes one attempt on the named (wrong) appliance before switching, so exactly one extra environment step is arithmetic whenever the rule is executed at all, and if it is not executed P2 fails instead; the estimand cannot come out against the hypothesis.",
   "fix": "Set the threshold above the mechanical one step (for example >= 2.0) or score the cost on unswapped kitchens where the test is free, and reconcile the >= 1.0 threshold with the stated CI-excludes-0 falsifier."
  }
 ],
 "shared_terms": [
  "P3-P5: P5's seen minus unseen gap has its unseen side pinned at the floored A4 level by construction, so the gap is the same measured seen-cell quantity that P3 and P4 already score.",
  "P3-P4: the pre-registered baseline is the best static arm per regime (A4/A5/A6); P4 asserts A5 is within +-12 of A3, which sets the retrieval residual over the best static arm to about zero and contradicts the Short Hypothesis's 'retrieval residual over the best compiled artifact' that P3 establishes only against A6.",
  "P1-P3: A4 under untestable is the floored cell in both, and since A6 degenerates to A4 under that regime, P3's subtrahend is P1's measured floor.",
  "P2-P7: both rest on the same event, the run-time test firing under testable feedback; P7's extra step is the mechanical signature of P2's recovery, so one determines the other.",
  "P4-P5: A5 on swapped seen kitchens is a measured term in both the table-matches-query test and the seen-unseen gap."
 ],
 "headline": "P3",
 "headline_status": "near_entailed",
 "n_open": 2,
 "n_entailed": 3,
 "n_near": 1,
 "n_unresolvable": 1,
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
