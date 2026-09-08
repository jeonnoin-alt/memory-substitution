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
 "Name": "many_shot_averages_detours",
 "Title": "Reading the Whole Bank Averages Out Detours: Many-Shot Context Is Robust to Per-Item Noise Where Top-k Retrieval Commits to It",
 "Short Hypothesis": "When the bank holds the agent's own successful-but-detoured trajectories (self pool) instead of expert trajectories, top-k retrieval passes the detours of the k items it commits to into the episode (more steps, more step-limit failures, lower success), while the whole-bank route is insensitive to the detour rate because the shared procedure is the consensus across many noisy items; the gap between routes grows with the bank's detour rate and with item count, and closes when detours are pruned from the items.",
 "Related Work": "Bertsch et al. (arxiv:2405.00200) report that long-context ICL gains come from attention to the most similar examples rather than cumulative learning, and arxiv:2412.16926 that long-context models are less sensitive to example selection; both predict that a whole-bank prompt inherits whatever its most similar item contains, the opposite of consensus reading. In-context learning with noisy labels (arxiv:2411.19581) and many-shot ICL (arxiv:2404.11018, including Unsupervised and Reinforced ICL with model-generated examples) study label noise in classification, not action noise in trajectories. ExpeL and SkillEvolBench (arxiv:2605.24117) reuse raw on-policy trajectories and report episode-specific drift and clutter from larger libraries without stating how items were selected; Honest Lying (arxiv:2605.29463) shows reflexive agents storing confident wrong interpretations; MemoryGraft (arxiv:2512.16962) and the compliance trap (arxiv:2607.10608) show agents imitating implanted or conflicting retrieved experiences. None sets the detour rate of a trajectory bank at several levels and compares whole-bank reading with top-k retrieval on task success and steps.",
 "Abstract": "Long-context in-context learning studies report that gains from many demonstrations come from attention to the most similar examples rather than from cumulative learning, which predicts that reading a whole bank of trajectories inherits whatever the most similar item contains. We test the opposite on agent trajectories, where per-item noise has a natural form: the detours in the agent's own successful episodes. On ALFWorld with Qwen3-32B we build banks from the expert pool (no detours), the self pool (every item detoured), a 50/50 mix, a pruned self pool whose non-causal steps are removed by rule and re-validated by replay, and an amplified self pool drawn from the longest detours. Each bank is read by goal-sentence top-3 retrieval or whole in a cached prefix at 6, 24 and 48 items, on the same 274 games and two seeds, scoring success, steps and step-limit failures against the Measurement C static arms. We predict retrieval passes detours into the episode, that the whole-bank route is insensitive to the detour rate and improves with item count on the self pool only, and that pruning restores retrieval. A per-episode imitation signature (episode steps against the injected items' detour steps) separates consensus reading from most-similar-item copying. Costs under caching are measured, since the robust route is also the longer prefix.",
 "Experiments": "- Pools and banks. E: expert pool (1,465). S: self pool (1,892 successes). Detour measure per item = steps beyond the expert solution length for the same game; distribution reported. M: 50/50 mix by type. P: pruned S, removing visits to receptacles that did not yield the target object and repeated identical actions, then replaying the pruned action list in the same game and keeping only replays that still succeed (pruned items are therefore valid successful trajectories). A: S items from the top tercile of detour steps within each type. Item tokens measured (E about 140; S expected about 2x).\n- Routes. RET: goal-sentence top-3 from each bank (same retriever as Measurement A), uncached; retrieved item lengths and detour steps logged per episode. WB: whole bank as a type-agnostic cached static prefix at 6, 24 and 48 items (48 S items must fit 16k with game history; otherwise 40 under a fixed type-balanced subset rule, stated before the run). Token-matched comparison WB E-48 vs WB S-24 also reported.\n- Arms at Qwen3-32B: RET x {S, M, P, A} (RET E is Measurement A); WB x {E6, E24, E48, S6, S24, S48, M48, P48}. About 12 arms, roughly 8 h on two GPUs.\n- Outcomes: success (primary), steps per episode and step-limit failures (secondary, paired). Imitation signature: for RET arms, the per-game paired difference in episode steps between S and E injections regressed on the injected items' detour steps; for WB arms, the same regression on the detour steps of the most similar item in the prefix (by the retriever's score) and on the bank-mean detour steps, to tell most-similar copying from consensus.\n- Reader: Qwen3-8B on RET E, RET S, WB48 E, WB48 S as an exploratory replication of the 2x2 (4 arms).\n- Cost: prefill tokens, GPU-seconds per episode under prefix caching; detours lengthen episodes and multiply decode steps, so cost per success is reported for both routes.\n- Order: positive control first (RET A vs RET E); pre-registration; then the 2x2 (RET/WB x E/S at 48); then the S ladder, M and P; then Qwen3-8B.",
 "Baselines and Ablations": "- k=0 and the Measurement C static arms (fixed type-conditioned exemplars, wrong-type placebo, procedure paragraph, six-procedure prompt); every retrieval number is reported as retrieval minus the best static arm at matched tokens.\n- RET E (Measurement A) is the clean-item reference; RET with random fixed selection of three S items per game separates the retriever from the detour content.\n- Pruned bank P is the repair ablation; amplified bank A is the positive control for imitation; mix M gives the intermediate detour rate.\n- WB E ladder (6/24/48) is the no-noise reference for the item-count dose-response on S.\n- Token-matched WB E-48 vs WB S-24 controls for the longer S items.",
 "Falsifiable Predictions": "- P1 (retrieval inherits detours): RET S minus RET E is at or below -8 net and RET S episodes are longer by at least 2 steps on the paired median. Falsified if RET S is within +/-8 of RET E with no step increase; arm: RET S vs RET E.\n- P2 (route x noise interaction, headline): [WB48 S - WB48 E] - [RET S - RET E] is at least +9 net. Falsified if both routes lose the same amount within 8 net, or if WB48 S loses more than RET S (the most-similar-item copying outcome predicted by arxiv:2405.00200); arms: the four cells WB48 E, WB48 S, RET E, RET S.\n- P3 (dose-response in item count on noisy items): WB S rises from 6 to 48 items by at least 9 net while WB E is flat within +/-8 over the same ladder. Falsified if WB6 S is within 8 net of WB48 S or above it; arms: WB S6, S24, S48 vs WB E6, E24, E48.\n- P4 (pruning repairs retrieval): RET P is within +/-8 of RET E and at least 9 net above RET S. Falsified if RET P is still at least 8 net below RET E, which would locate the deficit in something other than detours (phrasing, length); arm: RET P.\n- P5 (positive control): RET A is at least 8 net below RET S and its episodes are the longest. Falsified if RET A is within +/-8 of RET E, in which case imitation has no leverage and the design stops; arm: RET A.\n- P6 (mechanism): in RET arms episode steps rise with the injected items' detour steps (paired slope above zero at the 95% paired-bootstrap level), while in WB48 S episode steps do not rise with the most-similar item's detour steps. Falsified if WB48 S episodes track the most-similar item's detours as strongly as RET episodes track theirs; arm: WB48 S with per-item similarity and detour steps logged.\n- P7 (mix): WB48 M is within +/-8 of WB48 E while RET M sits between RET E and RET S. Falsified if WB48 M is at least 8 net below WB48 E; arms: WB48 M, RET M.",
 "Measurement and Noise Control": "Paired cells on 274 games x 2 seeds with identical seeds across arms; +/-8 net floor; confirmatory effects must exceed the floor and be at least one third of the Gate-0 retrieval gain (+27 net at k=3). Steps and step-limit failures are paired per game and summarised by median differences with paired-bootstrap intervals. Per-type results pooled over the three procedure-heavy types (clean, heat, cool) and declared exploratory. Positive control before any null: RET A must be at least 8 net below RET E. Success ceiling (0.87 at k=7) limits headroom for success, so steps are the pre-registered secondary outcome on which the imitation claim can still be tested. Item lengths and retrieved-item lengths are logged to rule out a retriever length bias explaining RET S. Cost measured as GPU-seconds per episode and prefill tokens under prefix caching. Pre-registration after the positive control.",
 "Preprint Collision Check": "- home: query 'many-shot in-context learning noisy demonstrations label noise robustness aggregation number of shots' via s2cli (Semantic Scholar + HF Papers, both channels ok): returned arxiv:2411.19581 (In-Context Learning with Noisy Labels), arxiv:2411.07130 (MANYICLBENCH), arxiv:2404.11018, arxiv:2506.04579, arxiv:2503.08640, arxiv:2406.15334, arxiv:2402.16431. Label noise in classification only; no action-sequence noise, no whole-bank vs top-k comparison; no pre-emption.\n- recent (mechanism, last 12 months): query 'self-generated trajectories experience memory detours noisy demonstrations agent imitation in-context' --recent via s2cli (both ok): returned arxiv:2605.29463 (Honest Lying: reflection confabulation), arxiv:2512.19396 (EchoTrail-GUI), arxiv:2602.16313 (MemoryArena), arxiv:2601.11653, and robotics items arxiv:2606.27374, 2606.09827, 2505.02094. None sets a detour rate or compares read routes; no pre-emption.\n- closest named method / mechanism in home vocabulary: query 'similar-sample learning versus all-sample learning many-shot long context locating the similar example among many examples' via s2cli (both ok): returned arxiv:2405.00200 (long-context ICL gains from attention to similar examples, not cumulative learning), arxiv:2412.16926, arxiv:2411.07130, arxiv:2510.16809, arxiv:2502.09933. arxiv:2405.00200 is the direct competitor mechanism; it is on classification with clean labels, so this proposal's P2 and P6 are its trajectory-bank test rather than a restatement.\n- supporting: query 'WebShop experience trajectories near-duplicate leakage whole history in long context agent memory' --recent via s2cli returned arxiv:2607.10608 (compliance trap) and arxiv:2512.16962 (MemoryGraft: imitation of implanted experiences), both showing agents copy retrieved items; neither varies item noise rate or reads the whole bank.\n- WebSearch: not used (not available in this session); WebFetch never used.",
 "Risk Factors and Limitations": "- Self-pool items may be too long for 48 to fit in 16k; the fallback size (40) and subset rule are fixed before the run and the token-matched cell covers the length confound.\n- The agent may ignore detours in retrieved items, giving a null on P1; the amplified-detour positive control is the stop rule, and the manipulation is still built in rather than observed.\n- Rule-based pruning can break trajectories; replay validation keeps only successful pruned items, but it can also shrink P relative to S in type coverage, which is reported.\n- The success ceiling near 0.87 limits success-rate headroom; steps and step-limit failures carry part of the claim and are pre-registered as secondary outcomes.\n- The retriever may prefer shorter items, confounding RET S; retrieved-item lengths are logged and a random-fixed-selection cell is included.\n- If the whole-bank route copies the most similar item (the 2405.00200 outcome), the headline is falsified; that result would still be informative for the axis and is reported as such.",
 "Addresses gap": "G20 (primary): whether long-context scaling conclusions (that long-context ICL keys on the most similar example) transfer to trajectory banks with on-policy noise; also G19 (whole-bank vs retrieval past saturation, here under a manipulated item-noise rate).",
 "Not a restatement of": "Nearest brief bullet: 'the self pool contains the agent's own detours and is the on-policy counterpart of a curated playbook' names the pool; this idea claims that the read route decides whether detours are inherited, with the detour rate built at three levels and pruning as the repair, which the brief does not claim. Nearest digest card: arxiv:2605.24117 observes that larger libraries add episode-specific drift and clutter under an unspecified selection; this idea claims drift transfers through top-k selection and is averaged out by whole-bank reading, and tests the most-similar-copying alternative directly. Nearest archived idea: abstraction_discards_bindings_and_repairs (5.95) concerns compiled abstraction losing repairs; here no abstraction is applied and the claim is about raw items under two read routes; first_item_additive_rest_substitutive concerns k on clean items, not item noise."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "many_shot_averages_detours",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "RET top-3 from the self pool S versus the expert pool E (Measurement A) on 274 x 2 paired games, scored on success and paired-median episode steps with retrieved item lengths logged.",
   "falsifier": "RET S within +/-8 of RET E with no step increase.",
   "label": "open",
   "reason": "Self-pool successes could be as effective as expert ones on both success and steps, and both outcomes are measured on paired cells, so the null is a reachable and visible result.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "WB48 S, WB48 E, RET S and RET E, with the S prefix possibly reduced to 40 items under the 16k fallback rule.",
   "falsifier": "both routes lose the same within 8 net, or WB48 S loses more than RET S (the most-similar-copying outcome).",
   "label": "open",
   "reason": "The WB cells are measured independently of the RET cells and the copying outcome is explicitly available, so the interaction can come out at or below zero; the S-vs-E token and item-count mismatch pushes toward falsification rather than away from it.",
   "fix": ""
  },
  {
   "id": "P3",
   "depends_on": "the WB S ladder at 6/24/48 items against the WB E ladder at the same sizes as the no-noise reference.",
   "falsifier": "WB6 S within 8 net of WB48 S or above it.",
   "label": "open",
   "reason": "A flat or declining S ladder is reachable and the acknowledged 0.87 success ceiling makes failure to gain 9 net more likely rather than less.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "RET over the pruned bank P, built by deleting unproductive receptacle visits and repeated actions from S items and keeping only replays that still succeed, compared with RET E and RET S.",
   "falsifier": "RET P still at least 8 net below RET E.",
   "label": "near_entailed",
   "reason": "P is S with exactly the detour tokens removed and then filtered to the items whose pruned replay still succeeds, so it is near-expert by construction and selection-biased toward easier games; the falsifier requires a residual phrasing or length deficit for which the design supplies no arm and no measurement.",
   "fix": "Add a length-matched sham-prune arm (delete an equal number of non-detour steps, replay-verified) and report P's game/type coverage against S, so a phrasing or length residual can actually be produced and detected."
  },
  {
   "id": "P5",
   "depends_on": "RET over the amplified bank A (top tercile of detour steps within each type of S), with RET S and RET E as comparators, run first as the gate that stops the design.",
   "falsifier": "RET A within +/-8 of RET E.",
   "label": "near_entailed",
   "reason": "A is selected on the very quantity the prediction is about (and on the harder, longer source episodes that produce it), so A below S with the longest episodes largely re-describes the selection, while the stated falsifier is written against RET E rather than RET S, so a genuine null (A equal to S) never trips the gate.",
   "fix": "State the falsifier against RET S (RET A within +/-8 of RET S falsifies) and match A to S on game difficulty and type so the contrast varies detour steps rather than which games produced long episodes."
  },
  {
   "id": "P6",
   "depends_on": "per-episode regression of episode steps on injected-item detour steps in RET arms, versus the same regression in WB48 S on the most-similar prefix item's detour steps and on the bank-mean detour steps, with one fixed type-agnostic bank per arm.",
   "falsifier": "WB48 S episodes track the most-similar item's detours as strongly as RET episodes track theirs.",
   "label": "near_entailed",
   "reason": "The WB prefix is a single fixed 48-item bank per arm, so the most-similar-item regressor draws on only 48 values and the bank-mean regressor has zero within-arm variance, attenuating or removing the slope regardless of whether consensus is the mechanism, and no MDE is stated for the asserted slope null.",
   "fix": "Draw a different randomized bank per game or per block so the most-similar-item and bank-mean detour regressors vary within an arm, and pre-register an equivalence bound (a slope MDE) for the WB null."
  },
  {
   "id": "P7",
   "depends_on": "WB48 M and RET M on the 50/50 mix bank, against the WB48 E, WB48 S, RET E and RET S cells already measured for P1 and P2.",
   "falsifier": "WB48 M at least 8 net below WB48 E.",
   "label": "near_entailed",
   "reason": "M is a 50/50 interpolation of banks already measured in P2, so its value is pinned by those cells unless the response to detour rate is non-monotone (a mechanism the proposal never names or models), and the RET M clause (between RET E and RET S) carries no margin so it cannot fail outside the floor.",
   "fix": "Pre-register a quantitative interpolation test with an MDE (WB48 M within a stated band of the E-S midpoint) and attach explicit thresholds to the RET M ordering clause."
  }
 ],
 "shared_terms": [
  "P1-P2: RET S minus RET E is P1's estimand and the subtracted half of P2's interaction, so a null P1 leaves P2 resting entirely on the WB cells.",
  "P2-P3: WB48 S and WB48 E are two of P2's four cells and the top rungs of both of P3's ladders.",
  "P2-P7: WB48 E and WB48 S are measured once and jointly pin the expected value of WB48 M.",
  "P1-P4-P5: RET E and RET S are the single measured comparators for the pruned and amplified bank predictions and for the design's stop gate.",
  "P1-P6: the RET S versus RET E step difference asserted in P1 is the same step data whose within-arm slope P6 regresses on detour steps."
 ],
 "headline": "P2",
 "headline_status": "open",
 "n_open": 3,
 "n_entailed": 0,
 "n_near": 4,
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



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
