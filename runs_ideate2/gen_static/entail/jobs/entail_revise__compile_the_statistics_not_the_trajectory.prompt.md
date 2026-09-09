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
 "Name": "compile_the_statistics_not_the_trajectory",
 "Title": "What Retrieval Cannot Carry: Cross-Episode Location Statistics Compiled From the Bank Beat Retrieved Trajectories on Search-Bound Tasks",
 "Short Hypothesis": "A compiled artifact can hold cross-episode aggregate statistics (object -> receptacle location frequencies) that no set of k retrieved trajectories contains; on ALFWorld's search-bound types (pick-and-place, pick-two, look-at-in-light) a ~300-token, type-agnostic, cached cheatsheet compiled by rule from the expert pool recovers at least the Gate-0 retrieval gain on those types, its gain grows with the compiler's sample size n (the signature of aggregation rather than exemplar content), and the raw whole bank in context does not reproduce it; combined with the six-procedure playbook the static route matches k=3 retrieval on all types at zero uncached prefill.",
 "Related Work": "Measurement A on this node shows the retrieval gain is procedure-bound (unseen ~ seen) and smaller on pick types (+15/+18/-5) than on heat/cool/clean (+39..+55); Measurement C tests static procedure prompts but no static artifact that carries anything a trajectory cannot. Strategy graphs (2511.07800), verifier-promoted skill graphs (2512.23760), tutorials (2606.03951) and ICAL insight exemplars (2406.14596) compile trajectories but never at matched tokens against raw retrieval and never separate distillation from aggregation (G1); SkillEvolBench (2605.24117) finds raw reuse often beats distilled skills but its skills are procedures, not statistics. Dynamic Cheatsheet (2504.07952) accumulates insights at test time but never compares against retrieval of the raw episodes or varies the amount of experience compiled. An LLM-free ALFWorld agent (WCCIS 2026, 'Zero-Shot Embodied Decision Making with Structured Prior Knowledge') hand-builds object-location priors and shows they matter for a symbolic controller, but does not compile them from experience, vary n, or compare with an LLM reader's retrieval. Object-search work in robotics (2607.00022 PerSim; 2603.05642 SymSearch) uses population-frequency placement priors, confirming the mechanism exists outside the agent-memory literature. Archived: compile_dont_retrieve (6.0) observed the read to be inert; here the compiled artifact is given content that retrieval cannot have and that content is manipulated (n ladder, shuffle, no-experience prior). optimizer_substitutes_for_memory_scaffold (5.22) could not separate scaffold from content; the shuffled-table placebo separates them by construction of the arm, not of the outcome.",
 "Abstract": "Agent-memory papers compare retrieval with no memory; the cheapest alternative, a fixed prompt compiled once from the same experience, is rarely run, and when compiled artifacts are studied their gain is not attributed. We isolate one thing compilation can do that per-query retrieval structurally cannot: aggregate across episodes. On ALFWorld with Qwen3-32B and the 1,465-item expert pool already on this node, we compile by rule a ~300-token cheatsheet of object -> receptacle location frequencies (from the 'take X from Y' step of each trajectory) and place it, type-agnostically, in the instruction slot as a cached static prefix. We compare it, on the same (game, seed) cells as Measurements A and C, with k=0, k=3/k=7 retrieval, the six-procedure playbook, a token-matched shuffled table (same format, permuted assignments), a table written by Qwen3-32B from its own knowledge without seeing the bank, an n ladder of compiler sample sizes (6, 20, 80, 1,465; three draws each), the raw whole bank of 80 items in context (11k tokens, cached), and additive combinations (playbook + cheatsheet; retrieval + cheatsheet; whole-bank + cheatsheet). Task success is primary; receptacles visited before the target is found is the process measure; uncached prefill tokens per episode are logged under vLLM prefix caching. The claim is that on search-bound types the compiled statistic beats retrieved trajectories at fewer tokens and zero uncached prefill, that its value rises with n and vanishes when shuffled, and that the long-context reader does not compute the statistic from the raw items it is given.",
 "Experiments": "Bank: expert pool (1,465). Compiler (rule, no LLM): for every trajectory extract the receptacle in the first successful 'take <obj> from <recep>' action; per object class output the top-3 receptacles with percentage and count; ~30 object classes, ~300 tokens; type- and scene-agnostic. n ladder: n in {6 (one per type), 20, 80, 1465}, three uniform draws for n<1465 (between-draw SD reported). Arms, each 274 games x 2 seeds paired with A/C cells (existing cells reused where noted): (1) k=0, k=3, k=7 retrieval [A, exist]; (2) six-procedure type-agnostic playbook, 400 tokens [C, exists]; (3) cheatsheet_n for the four n (9 draws + 1 = 10 arms); (4) shuffled cheatsheet: object -> receptacle rows permuted across objects, identical tokens and format (scaffold placebo); (5) LLM-prior cheatsheet: Qwen3-32B writes the same-format table without the bank (no-experience control), token-matched; (6) playbook + cheatsheet_1465 (~700 tokens, still below k=7's 1,010); (7) whole-bank_80 raw (80 type-balanced items, ~11k tokens, fixed order per seed, cached) and whole-bank_80 + cheatsheet_80 computed from those same 80 items; (8) k=3 retrieval + cheatsheet_1465 (additivity). Process measure from step logs: receptacles opened/visited before the target object is taken; steps per episode. Cost: uncached prefill tokens per episode (static prefixes cached across the arm; retrieval prefixes uncached), tokens/s per GPU and episodes/min. Order: positive control (k=3 reproduces A's +27 within floor on the fresh seeds), then cheatsheet_1465 vs k=0 (headline), then the n ladder and placebos, then whole-bank. ~16 new arms at ~30 min each (~8 h on two A100s, two vLLM replicas, workers tuned to the queue). Pre-registration before the first confirmatory cell.",
 "Baselines and Ablations": "Baseline (per the round rule) is the best static arm: playbook [C] and cheatsheet arms are the baseline against which k=3/k=7 retrieval is reported as retrieval minus best static. Ablations: n ladder (aggregation dose); shuffled table (content vs scaffold); LLM-prior table (experience vs pretraining knowledge); type-agnostic throughout, so no type-conditioning confound; whole-bank_80 with and without its own cheatsheet (explicit vs implicit aggregation at matched n); retrieval + cheatsheet (is the statistic additive to procedures); per-type split pooled into search-bound (pick-and-place, pick-two, look-at-in-light) and procedure-bound (heat, cool, clean) groups, pre-registered.",
 "Falsifiable Predictions": "P1 (headline): cheatsheet_1465 minus k=0 >= +12 points on the pooled search-bound cell (~137 games x 2 seeds; floor +-12), i.e., at least the Gate-0 retrieval gain on those types. Falsified if the paired net gain is below +12 (indistinguishable from zero at this n); arm: cheatsheet_1465 vs k=0 on the same cells. Not entailed: the reader may ignore frequency tables. P2 (aggregation dose): cheatsheet_1465 minus cheatsheet_6 >= +12 on the search-bound cell with means ordered 6 < 20 < 80 < 1465. Falsified if cheatsheet_6 is within +-12 of cheatsheet_1465; arm: n ladder. Not entailed: six trajectories may already give an adequate prior. P3 (content, not scaffold): cheatsheet_1465 minus shuffled >= +12 on the search-bound cell. Falsified if shuffled is within +-12 of the true table; arm: shuffled cheatsheet. P4 (experience, not pretraining): cheatsheet_1465 minus LLM-prior >= +12 on the search-bound cell. Falsified if the no-bank table is within +-12 of the compiled one, which would mean the static route needs no experience at all; arm: LLM-prior. P5 (closes the gap): k=3 retrieval minus (playbook + cheatsheet_1465) <= 0 on all 274 x 2 (floor +-8); falsified if the residual in favour of retrieval is >= +8; arm: combo vs k=3. P6 (reader is not an aggregator): cheatsheet_80 minus whole-bank_80 >= +12 on the search-bound cell, and whole-bank_80 + cheatsheet_80 minus whole-bank_80 >= +12. Falsified if whole-bank_80 is within +-12 of or above cheatsheet_80, or if adding the table computed from the same 80 items adds < 12; arm: whole-bank_80 and whole-bank_80 + cheatsheet_80. Not entailed: the items contain the information, but whether the reader extracts the statistic is the question. P7 (process): receptacles visited before the target is taken falls by >= 1.0 (paired mean) under cheatsheet_1465 vs k=0 on search-bound games; falsified if the paired difference's 95% CI includes 0; arm: cheatsheet_1465 step logs vs k=0. Positive control before any null: k=3 minus k=0 >= +19 (0.7 x Gate-0) on the fresh cells; otherwise the run is stopped.",
 "Measurement and Noise Control": "Outcome: task success on paired (game, seed) cells; net = paired difference in success (points) with the brief's +-8 floor at 274 x 2, rescaled by sqrt(548/n) for pooled subsets (+-12 for the ~137-game search-bound cell); bootstrap over games with seeds nested; permutation test on paired differences; compile-draw variance for n < 1465 reported as between-draw SD and folded into the CI by nesting draws. Margins: 12 = floor on the pooled subset; the headline is tied to the Gate-0 gain on those types (~+12..+15). Per-type numbers reported as exploratory. Token accounting: all static arms are shorter than the retrieval arm they are compared with (300 vs 430; 700 vs 1,010). Pre-registration file with arm list, cells, margins and stopping rule before the first confirmatory cell; identical games, seeds, decoding and max steps across arms; static prefixes fixed per seed so caching is real, not modelled.",
 "Preprint Collision Check": "Q1 (recent, mechanism) 'compiled cheatsheet of object location priors from agent trajectories versus retrieval ALFWorld' --recent: no results (S2+HF). Q1b (recent, mechanism, shorter) 'object location prior LLM agent ALFWorld household' --recent, channel S2+HF: 'Zero-Shot Embodied Decision Making with Structured Prior Knowledge and Adaptive Calibration in ALFWorld' (WCCIS 2026, no arXiv id; LLM-free symbolic agent with hand-built object-location priors and task templates; no compilation from experience, no retrieval arm, no n sweep); 2607.00022 PerSim (household object search with population-frequency priors, robotics); 2605.05413 (procedural context moved to weights); 2602.06459 UcON (habit retrieval for object navigation). None compares a compiled location statistic with retrieved trajectories at matched tokens in an LLM agent. home: Q2 'object receptacle co-occurrence prior household object search semantic prior' (no agent/memory/retrieval/experience/benchmark words), channel S2+HF: 2607.00022, 2606.15476 FARM, 2603.21887 IGV-RRT, 2603.05642 SymSearch (LLM relational knowledge distilled offline into lightweight models for object search) - the mechanism is established in robotics; none is an in-context artifact compared with per-query retrieval. Q3 (closest named method) 'Dynamic Cheatsheet test-time learning adaptive memory', channel S2+HF: 2504.07952 Dynamic Cheatsheet (persistent evolving insight memory; no retrieval-vs-compiled comparison, no experience-size sweep), 2606.05684 AdaMEM, 2511.20857 Evo-Memory. Verdict: no pre-emption; the nearest overlap is the WCCIS 2026 symbolic-agent paper, which motivates rather than tests the claim.",
 "Risk Factors and Limitations": "The prior may be commonsense the model already holds (P4 falsifier); this is an informative negative for the area (a static prompt with no experience matches retrieval) and is reported as such. ALFWorld's object placement is sampled from generic plausibility, so the compiled statistic is scene-agnostic; on environments with scene-specific placements the same table would need a scene key (a different study). Only Qwen3-32B; the reader's ability to use a frequency table may differ by backbone. Search-bound cell is half the games, so the floor is +-12; margins are set accordingly. Rule compiler assumes the 'take X from Y' step is present in every expert trajectory (true by construction of the pool; checked). The whole-bank comparison at n=80 uses a sparse table (about 2-3 trajectories per object class), so P6 is a matched-n comparison, not the full-n table.",
 "Addresses gap": "G1 (the source of any compilation gain, distillation vs weighting vs extra context, is unresolved): the n ladder, the shuffled table and the no-experience table attribute the gain to aggregation of experience at fixed output tokens; also G3 (whole-bank arm with and without its own compiled statistic) and G5 (gain vs compiled-sample size; cost per episode under caching).",
 "Not a restatement of": "Prior-result bullet 'Measurement A: gain carried by clean/heat/cool procedures, pick-and-place +15, pick-two +18, look-at -4.8; unseen ~ seen, so the retrieved value is the type's procedure': this idea claims a second kind of value on the search-bound types, a cross-episode statistic that k retrieved trajectories cannot contain, and predicts it exceeds retrieval there. Digest card arxiv:2511.07800 (strategy graph distilled from trajectories; source of gain unclear): this idea fixes the output tokens and varies the compiler's sample size, shuffles the content and removes the experience, so the gain is attributed to aggregation rather than to extra context or distillation."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "compile_the_statistics_not_the_trajectory",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "cheatsheet_1465 vs k=0 on the pooled search-bound cell (~137 games x 2 seeds), paired success, stated floor +-12; rule compiler over the 1,465-item expert pool",
   "falsifier": "paired net gain below +12, i.e. indistinguishable from zero at this n",
   "label": "unresolvable",
   "reason": "The decision margin (12) is exactly the stated noise floor (+-12) and the proposal anchors the true expected effect to the Gate-0 gain on those types (~+12..+15), so the predicted effect sits at the detection limit and a real effect of the anticipated size will read as falsified about half the time.",
   "fix": "Shrink the floor below the margin on the search-bound cell (more seeds or all 274 games per type group, or a pre-registered TOST with margin > CI half-width) so that +12 and 0 are separable."
  },
  {
   "id": "P2",
   "depends_on": "n ladder cheatsheet_6 / 20 / 80 / 1465, three uniform draws for n<1465, same search-bound cell, floor +-12",
   "falsifier": "cheatsheet_6 within +-12 of cheatsheet_1465, or means not ordered 6 < 20 < 80 < 1465",
   "label": "near_entailed",
   "reason": "The rule compiler emits one take-receptacle row per trajectory, so cheatsheet_6 covers at most 6 of ~30 object classes while cheatsheet_1465 covers all of them; if P1's effect exists at all the gap is forced by row coverage rather than by aggregation, and the falsifier is reachable only through the scaffold-driven mechanism P3's placebo is built to exclude.",
   "fix": "Add a coverage-matched rung (all ~30 object classes, each estimated from a single sampled trajectory) so sample depth is varied at fixed coverage, and give the monotone ordering its own power statement, since 20 vs 80 vs 1465 differences are far inside the +-12 floor."
  },
  {
   "id": "P3",
   "depends_on": "cheatsheet_1465 vs shuffled cheatsheet (rows permuted across objects, identical tokens and format), search-bound cell, floor +-12",
   "falsifier": "shuffled within +-12 of the true table",
   "label": "open",
   "reason": "The falsifier is reachable if the reader treats the table as a search-anything scaffold and ignores its content, and nothing in the design forces the two arms apart.",
   "fix": "Also report shuffled minus k=0, since the contrast as written cannot separate 'the true table helps' from 'the permuted table actively hurts'."
  },
  {
   "id": "P4",
   "depends_on": "cheatsheet_1465 vs a token-matched LLM-prior table written by Qwen3-32B without the bank, search-bound cell, floor +-12",
   "falsifier": "the no-bank table within +-12 of the compiled one",
   "label": "open",
   "reason": "ALFWorld object-receptacle placements are stereotyped enough that the model's own prior table could match the compiled one, so the falsifying outcome is plainly reachable and would in fact be the likely result.",
   "fix": "None needed for openness; pre-register the row-level agreement between the prior and compiled tables as a covariate so a null is interpretable rather than merely negative."
  },
  {
   "id": "P5",
   "depends_on": "k=3 retrieval vs playbook + cheatsheet_1465 on all 274 x 2 cells, floor +-8",
   "falsifier": "residual in favour of retrieval >= +8",
   "label": "open",
   "reason": "Gate-0 puts k=3 about +27 over k=0 overall, so a residual well above the +-8 floor is entirely reachable if the static combo recovers less than that.",
   "fix": "Close the dead band between the stated prediction (<= 0) and the stated falsifier (>= +8), which currently leaves residuals of +1..+7 neither confirming nor falsifying."
  },
  {
   "id": "P6",
   "depends_on": "cheatsheet_80 vs whole-bank_80 (80 type-balanced raw items, ~11k tokens, cached) and whole-bank_80 + cheatsheet_80, search-bound cell, floor +-12",
   "falsifier": "whole-bank_80 within +-12 of or above cheatsheet_80, or the added table worth < 12 on top of the same 80 items",
   "label": "open",
   "reason": "The information is by construction present in the 80 raw items and the whole-bank arm also carries procedure content the cheatsheet lacks, so a long-context reader matching or beating the table is a reachable outcome.",
   "fix": "None for openness; note that cheatsheet_80 is simultaneously an n-ladder rung, so a single bad draw of it moves P2 and P6 together."
  },
  {
   "id": "P7",
   "depends_on": "step logs: receptacles opened/visited before the target object is taken, cheatsheet_1465 vs k=0 on search-bound games, paired mean",
   "falsifier": "the 95% CI of the paired difference includes 0",
   "label": "open",
   "reason": "A null reduction is reachable if the reader does not act on the table, though the estimand is conditioned on a post-treatment event (the target being taken), which only episodes that get that far contribute to.",
   "fix": "Restrict the paired comparison to games where the target is taken in both arms (or impute the max search length for failures), and reconcile the stated threshold (>= 1.0) with the stated falsifier (CI includes 0), which currently leaves reductions of 0.1..0.9 undecided."
  },
  {
   "id": "P8",
   "depends_on": "positive control gate: k=3 minus k=0 >= +19 (0.7 x Gate-0) on the fresh 274 x 2 cells, floor +-8, run stopped otherwise",
   "falsifier": "k=3 minus k=0 below +19 on the fresh seeds",
   "label": "open",
   "reason": "It is a re-measurement of an already observed +27 with a 30% discount and an +-8 floor, so failure is unlikely but empirically reachable rather than excluded by construction.",
   "fix": "None; state explicitly whether a result between +8 and +19 stops the study or only flags it, since the stopping rule and the floor disagree in that band."
  }
 ],
 "shared_terms": [
  "P1-P3-P4: all three are cheatsheet_1465 minus X on the identical search-bound cell, so they share one measured minuend and are one measurement with three subtrahends, not three independent tests.",
  "P1-P2: cheatsheet_1465 is a measured term in both; if it fails against k=0, P2 can only survive by cheatsheet_6 falling below k=0.",
  "P2-P6: cheatsheet_80 is both a rung of the n ladder and the explicit-aggregation arm of P6, so the ordering claim and the reader-is-not-an-aggregator claim rest on the same cell.",
  "P1-P5: the combo arm of P5 contains cheatsheet_1465, so P5's residual inherits whatever P1 measures.",
  "P1-P7: on search-bound types taking the target object is close to necessary for success, so the process measure of P7 and the success measure of P1 are scored on the same episodes and largely the same event.",
  "P5-P8: k=3 on the fresh cells is the same measured arm in the gate and in the gap-closing test."
 ],
 "headline": "P1",
 "headline_status": "unresolvable",
 "n_open": 6,
 "n_entailed": 0,
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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
