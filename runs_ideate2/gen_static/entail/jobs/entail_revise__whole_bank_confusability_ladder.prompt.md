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
 "Name": "whole_bank_confusability_ladder",
 "Title": "Confusable, Not Long: The Whole-Bank-in-Context Route Loses to Top-k Retrieval Only as Near-Miss Trajectories Accumulate",
 "Short Hypothesis": "On a six-procedure trajectory bank, reading the whole bank as a cached static prefix matches goal-sentence top-3 retrieval on task success up to the 16k context no matter how many redundant or off-domain items are added; it falls below retrieval only as the count of near-miss items (same object and receptacle words, different procedure) grows, whereas retrieval responds to the near-miss share rather than the count. The bank size at which the two routes cross is therefore set by bank composition, not prompt length, and it is smaller for a weaker reader (Qwen3-8B) than for Qwen3-32B.",
 "Related Work": "Enrich-Retrieve-Rank (arxiv:2608.22695) shows in-context routing over a capability registry collapsing as the registry grows while retrieve-then-rank degrades gracefully, but scores Match@1 with one router model and grows the number of distinct options, not the number of confusable copies. Bertsch et al. (arxiv:2405.00200) and arxiv:2412.16926 find that long-context ICL gains come from attention to the similar examples and that selection matters less as shots grow, on classification tasks; MANYICLBENCH (arxiv:2411.07130) separates similar-sample from all-sample learning; arxiv:2510.16809 finds a few well-chosen examples beating many on code translation. arxiv:2607.26497 measures a corpus-size crossover between agentic search and BM25 on documents with one reader; arxiv:2603.04814 measures Mem0 against long context on conversational QA with one model; arxiv:2411.05000 shows effective context shorter than advertised on synthetic threads. The compliance trap (arxiv:2607.10608) shows agents adopting conflicting retrieved memory; SkillEvolBench (arxiv:2605.24117) reports clutter from larger libraries under an unspecified selection. None of these grows a trajectory bank while holding the procedure count fixed and separating redundant count, off-domain length and confusable count, scores task success, and checks whether the crossover moves with the reader.",
 "Abstract": "Agent-memory papers assume a bank of trajectories must be queried because the whole bank will not fit or will not be read well, and the long-context literature reports crossovers between retrieval and in-context reading measured on documents with one reader. We ask what property of a trajectory bank actually makes the whole-bank-in-context route fall behind top-k retrieval on task success. On ALFWorld with Qwen3-32B we grow a six-item seed bank (one expert exemplar per task type) to 12, 24, 48 and 80 items in three ways that hold the six procedures fixed: redundant growth (same-type items whose object-receptacle pairs collide with no other type), off-domain filler (token-matched trajectories from another text game), and near-miss growth (every added item has a twin of another type with the same object and receptacle, so half the bank is confusable). Each bank is read whole as a cached static prefix or through goal-sentence top-3 retrieval, on the same 274 games and two seeds, with the Measurement C static arms as the baseline and a fixed uniformly random 80-item subset as the selection control. We predict the whole-bank route is flat under redundant and filler growth and declines with the near-miss count, while retrieval declines with near-miss share only, so the crossover in items depends on composition and arrives earlier for Qwen3-8B. Prefill tokens and GPU-seconds under prefix caching are logged for accuracy-cost curves.",
 "Experiments": "- Bank construction from the expert pool (1,465 items). Seed S6 = one expert exemplar per task type, fixed. Growth to 12/24/48/80 items under three rules that keep six procedures: R (redundant, near-miss share 0): add same-type items whose (object, receptacle) pair appears in no item of another type in the bank; N (near-miss, share 0.5): add items in cross-type twin pairs (same object and receptacle, different procedure; twins chosen so their first actions coincide), so at every size half of the items have a twin in the bank; F (filler, sizes 24/48/80 only): S6 plus token-matched trajectories from public TextWorld cooking games in the same format with no ALFWorld nouns. U: one uniformly random fixed 80-subset of the pool (natural near-miss share, measured and reported) as the G17 fixed-random-selection control. Item order type-interleaved, fixed per arm.\n- Routes. WB: whole bank as a type-agnostic static prefix (vLLM prefix caching on, cache hit ratio logged). RET: goal-sentence top-3 from the same bank per episode (uncached), same retriever as Measurement A. For every bank both routes run on the same 274 games x 2 seeds.\n- Arms at Qwen3-32B: WB x {R,N} x 5 sizes (10), RET x {R,N} x 5 sizes (10), WB x F x 3 sizes (3), WB x U (1); RET on the full pool is Measurement A k=3 (on disk). 24 new arms; WB arms at 48/80 items run 2-3x slower per episode, so about 16 h on two GPUs with one replica each and arms interleaved across replicas.\n- Reader manipulation (G16): Qwen3-8B on WB and RET x {R,N} x {12,48,80} (12 arms) plus 8B k=0 and 8B three fixed type-conditioned exemplars (2 arms), about 4 h. Crossover size per reader = smallest size at which WB minus RET is at or below -8 net on the N ladder.\n- Error signature: in failed episodes, the fraction in which the executed action sequence follows the twin's procedure (skipped or inserted clean/heat/cool step) is read from the action log, per route and size, to show that the decline is procedure confusion rather than generic length failure.\n- Cost: GPU-seconds per episode at fixed concurrency (16 workers per replica), prefill tokens per episode, cache hit ratio; accuracy-cost curves per route and size; the cost crossover is reported separately from the accuracy crossover.\n- Order: positive control first (Measurement C wrong-type placebo must sit at least 8 net below the right-type single exemplar, pooled over twin-bearing types); pre-registration; R and N ladders at 32B; then F, U, order re-shuffle check at N-48; then Qwen3-8B.",
 "Baselines and Ablations": "- k=0 (Measurement A) and the five Measurement C static arms: one and three fixed type-conditioned exemplars, wrong-type fixed exemplar (length placebo and near-miss positive control), per-type procedure paragraph, six-procedure type-agnostic prompt; every retrieval number is reported as retrieval minus the best of these at matched tokens.\n- RET k=3 over the natural pool (Measurement A) and RET with random fixed selection (three random items from the same bank, fixed per game) at the same token budget, to separate the retriever from the exemplar budget.\n- WB x F filler ladder isolates prompt length from content; WB x U fixed random 80-subset is the matched-budget random-selection control at the whole-context budget and supplies a third, natural near-miss share.\n- Order ablation (exploratory): N-48 with a second type-interleaved shuffle, to bound order effects that could mimic composition effects.\n- Reader ablation: Qwen3-8B on both ladders at three sizes.",
 "Falsifiable Predictions": "- P1 (length does not hurt): WB on the R ladder stays within +/-8 net of WB at S6 through 80 items, and WB on the F ladder stays within +/-8 of S6 at matched tokens. Falsified if WB(R-80) or WB(F-80) is at least 8 net below WB(S6) on the paired cells; arm: WB R-80 and WB F-80 vs WB S6.\n- P2 (confusable count hurts the whole-bank route): WB on the N ladder declines monotonically and WB(N-80) minus WB(N-6) is at or below -9 net (one third of the Gate-0 gain), with the decline carried by twin-procedure errors in the action log. Falsified if WB(N-80) is within +/-8 of WB(N-6), or if the decline is not accompanied by a rise in twin-procedure errors; arm: WB N-80 vs WB N-6.\n- P3 (retrieval responds to share, not count): RET(N-48) is at least 8 net below RET(R-48), and RET(N-80) is within +/-8 of RET(N-12). Falsified either if RET(N-48) is within +/-8 of RET(R-48) (the retriever is immune to twins, so share does not matter) or if RET declines with size at fixed share; arms: RET N-48 vs RET R-48, RET N-80 vs RET N-12.\n- P4 (interaction): [WB(N-80) - WB(N-6)] - [RET(N-80) - RET(N-12)] is at or below -9 net. Falsified if the two routes decline by the same amount (within 8 net) on the N ladder; arms: the four cells named.\n- P5 (crossover moves with reader): on the N ladder Qwen3-8B's crossover size is smaller than Qwen3-32B's (8B crosses at 48 or earlier when 32B crosses at 80 or not at all). Falsified if 8B crosses at the same size or later than 32B, or if 8B shows no crossover while 32B does; arms: 8B WB N-48/N-80 vs 8B RET N-48/N-80, against the 32B cells.\n- P6 (fixed random selection): WB(U-80) is within +/-8 of RET k=3 on the full pool (Measurement A). Falsified if WB(U-80) is at least 8 net below Measurement A k=3; arm: WB U-80.",
 "Measurement and Noise Control": "All arms run the same 274 games (140 valid_seen + 134 valid_unseen) x 2 seeds with identical seeds across arms; every contrast is a paired net difference with the +/-8 net floor at 274 x 2; confirmatory effects must exceed the floor and be at least one third of the Gate-0 retrieval gain (+27 net at k=3). Crossover size is defined before the run as the smallest ladder size at which WB minus RET is at or below -8 net. Per-type claims are made only on the pooled twin-bearing types (clean, heat, cool, pick-and-place) and declared exploratory. Positive control before any null: the Measurement C wrong-type placebo must be at least 8 net below the right-type single exemplar; if it is not, the near-miss manipulation has no leverage and the design stops. Order sensitivity is bounded by the N-48 re-shuffle cell. Cost is measured, not modelled: GPU-seconds per episode at fixed concurrency with prefix caching on, prefill tokens and cache hit ratio per episode, reported as accuracy-cost curves. Qwen3-8B k=0 is run first; if 8B's k=0 to k=3 gain is below the floor the reader arm is reported as uninformative rather than as a null crossover. Pre-registration after the positive control.",
 "Preprint Collision Check": "- home: query 'many-shot in-context learning distractor demonstrations confusable examples accuracy degradation with number of shots' via s2cli (Semantic Scholar + HF Papers, both channels ok): returned arxiv:2404.11018 (Many-Shot ICL), arxiv:2510.16809 (many-shot fails on code translation; few well-chosen beat many), arxiv:2408.13987 (FocusICL), arxiv:2506.04579 (gradient-matching demonstration selection), arxiv:2605.03644 (AdapShot). None grows the number of confusable demonstrations separately from length or scores agent task success; no pre-emption.\n- recent (mechanism, last 12 months): query 'long context versus retrieval crossover bank size agent experience trajectories whole bank in context' --recent via s2cli (both channels ok): returned arxiv:2608.22695, arxiv:2607.02255 (AgenticSTS), arxiv:2606.22844 (RaMem), arxiv:2605.12493 (LongMemEval-V2), arxiv:2605.05191 (LongSeeker), arxiv:2603.04257 (Memex), arxiv:2602.01566 (FS-Researcher). None runs a whole-bank ladder against retrieval on task success; no pre-emption.\n- closest named method: query 'in-context routing capability registry scaling collapse retrieve-then-rank' via s2cli (both channels ok): returned arxiv:2608.22695 (Enrich-Retrieve-Rank) plus unrelated MoE and LLM-router papers (arxiv:2605.08292, 2602.03478, 2601.21545, 2506.22262). Confirms 2608.22695 as the nearest: Match@1, one router (Nova Micro), distinct options grown, no confusable-copy manipulation.\n- supporting home-vocabulary query 'similar-sample learning versus all-sample learning many-shot long context locating the similar example among many examples' via s2cli (both ok): returned arxiv:2405.00200 (long-context ICL gains come from attention to similar examples), arxiv:2412.16926, arxiv:2411.07130 (verified with s2cli paper: ACL 2025, MANYICLBENCH), arxiv:2510.16809, arxiv:2502.09933 (MIR-Bench). 2405.00200 is the closest home-literature result and predicts the whole-bank route keys on the nearest item; it is on classification, not trajectories, and does not grow confusable items.\n- WebSearch: not used (not available in this session); WebFetch never used.",
 "Risk Factors and Limitations": "- Near-miss harm may be small for a 32B reader because the goal sentence disambiguates the type; the positive control (Measurement C wrong-type placebo) is the pre-registered stop, and a bounded null with a built-in manipulation is still reported.\n- Only six procedures exist on ALFWorld, so the registry-growth regime of 2608.22695 (hundreds of distinct options) is not reachable here; the claim is limited to fixed-procedure banks, with WebShop as the stated extension.\n- Twins are scarce for look-at-in-light and pick-two, so the N ladder's twin-bearing types are clean, heat, cool and pick-and-place; per-type results outside these are exploratory.\n- 16k context caps the ladder at 80 items; a 32k extension on this node would cut concurrency and is not proposed.\n- Whole-bank arms at 48/80 items run 2-3x slower per episode; the budget accounts for this, but throughput must be reported per arm.\n- Qwen3-8B may be near its k=0 floor on ALFWorld, making its crossover uninformative; the 8B k=0 and fixed-exemplar cells are run first.",
 "Addresses gap": "G19 (primary): saturation with the number of shots and whether a whole-bank prompt matches retrieval past saturation, here with the bank composition manipulated rather than observed; also G17 (matched-budget whole-bank and fixed-random-selection arms) and G16 (crossover measured with two readers).",
 "Not a restatement of": "Nearest brief bullet: Measurement A ('unseen ~ seen, so the retrieved value is the type's procedure; a bank of 1,465 items has at most six procedures') observes the natural pool; this idea builds banks whose redundant, off-domain and confusable item counts are set separately and claims the whole-bank route's success tracks the confusable count only, which Measurement A cannot say. Nearest digest card: arxiv:2608.22695 observes routing collapse with registry size on Match@1 with one router; this idea claims that on trajectory banks with a fixed procedure count collapse does not come with size at all but with near-miss items, scored on task success with two readers. Nearest archived ideas: coverage_limited_context_count_limited_weights (5.35) claims context is coverage-limited; this idea claims what governs the route past coverage (confusable count vs length), which it neither manipulated nor measured; compile_dont_retrieve and decorative_retriever observed inertness and overlap on the natural pool, whereas here the property that would make the read non-inert is built in at two levels."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "whole_bank_confusability_ladder",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "WB arms on the R ladder (same-type items, near-miss share 0) and the F ladder (token-matched TextWorld filler, sizes 24/48/80) against the shared WB S6 seed cell; 274 games x 2 seeds paired, +/-8 net floor.",
   "falsifier": "WB(R-80) or WB(F-80) at least 8 net below WB(S6) on the paired cells.",
   "label": "open",
   "reason": "Plain long-context degradation of an 80-item prefix is an outcome nothing in the design precludes and a drop past the +/-8 floor would be visible on paired cells, though the 8-net falsifier and the 9-net confirmatory bar leave an 8-to-9 dead band.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "WB on the N ladder (cross-type twin pairs, near-miss share 0.5 at every size) from the S6 seed to 80 items, plus the twin-procedure error fraction read from failed-episode action logs.",
   "falsifier": "WB(N-80) within +/-8 of WB(N-6), or a decline not accompanied by a rise in twin-procedure errors.",
   "label": "open",
   "reason": "Flatness on the N ladder and a generic length-failure error signature are both attainable, and the conjunctive falsifier (success drop AND error-signature rise) makes falsification easier rather than harder.",
   "fix": ""
  },
  {
   "id": "P3",
   "depends_on": "RET goal-sentence top-3 over the N vs R banks at 48 items, and over N at 12 vs 80 where near-miss share is held at 0.5 by construction; gated on the Measurement C wrong-type placebo sitting at least 8 net below the right-type exemplar.",
   "falsifier": "RET(N-48) within +/-8 of RET(R-48), or RET declining with size at fixed share.",
   "label": "near_entailed",
   "reason": "Twins are built to share exactly the object and receptacle words the goal-sentence retriever scores on while carrying the wrong procedure, and the run is pre-gated on wrong-type exemplars already costing at least 8 net, so RET(N-48) below RET(R-48) re-describes the pool construction plus the gate; the falsifier survives only through the retriever failing to rank twins highly, which is never logged or controlled.",
   "fix": "Log the type composition of the retrieved top-3 (twin-retrieval rate) per cell and add a type-conditioned retrieval arm on the N ladder, so the prediction is about retriever behaviour rather than about the twin construction the bank guarantees."
  },
  {
   "id": "P4",
   "depends_on": "the four cells WB(N-80), WB(N-6), RET(N-80), RET(N-12), all of them already the measured cells of P2 and P3.",
   "falsifier": "the two routes decline by the same amount (within 8 net) on the N ladder.",
   "label": "entailed",
   "reason": "P4's estimand is arithmetically P2's WB decline minus P3's RET decline over identical measured cells, so once P2 asserts the WB term is at or below -9 and P3 asserts the RET term is within +/-8, the interaction is pinned at or below -9 and no independent outcome can contradict it.",
   "fix": "Estimate the route x composition interaction on cells not used by P2/P3 (for example the R-ladder route difference as the comparison contrast, or a second independent bank draw per size), or drop P4 as a restatement."
  },
  {
   "id": "P5",
   "depends_on": "crossover size defined as the smallest ladder size where WB minus RET is at or below -8 net on the N ladder, with Qwen3-8B run only at 12/48/80 and Qwen3-32B at 6/12/24/48/80, plus the clause that reports the 8B arm as uninformative when its k=0-to-k=3 gain is below the floor.",
   "falsifier": "8B crosses at the same size as or later than 32B, or 8B shows no crossover while 32B does.",
   "label": "unresolvable",
   "reason": "Crossover is a threshold placed exactly at the +/-8 noise floor with no interval on the crossing size, the two readers are compared on different size grids (an 8B crossover at 24 is unobservable and would be recorded as 48), and the pre-registered escape clause converts the commonest falsifying outcome into uninformative.",
   "fix": "Run 8B on the same 12/24/48/80 grid, define crossover with a paired-bootstrap interval on WB minus RET at the confirmatory 9-net margin rather than at the floor, and add seeds so the crossing size itself carries a CI."
  },
  {
   "id": "P6",
   "depends_on": "WB on the fixed random 80-subset U against the on-disk Measurement A RET k=3 over the full 1,465-item pool, paired on the same 274 x 2 games.",
   "falsifier": "WB(U-80) at least 8 net below Measurement A k=3.",
   "label": "open",
   "reason": "A uniformly random 80-subset carries a natural near-miss share that, on the proposal's own mechanism, could push WB well below the full-pool retrieval number, so the falsifier is reachable and visible past the +/-8 floor, although only the below-direction is stated as falsifying.",
   "fix": ""
  }
 ],
 "shared_terms": [
  "P1-P2: WB(S6) is the same measured cell as WB(N-6), so a low seed cell simultaneously widens P1's flat band and shrinks P2's asserted decline.",
  "P2-P4: WB(N-80) and WB(N-6) are the identical measured cells in both; P4 is P2's estimand minus P3's.",
  "P3-P4: RET(N-80) and RET(N-12) are the identical measured cells in both; P3's asserted null pins P4 to P2's value.",
  "P2-P5, P3-P5: the 32B crossover in P5 is read off the same WB and RET N-48/N-80 cells used by P2, P3 and P4.",
  "P6-baselines: Measurement A k=3 is both P6's comparator and the normalizer against which every retrieval number in the proposal is reported."
 ],
 "headline": "P4",
 "headline_status": "entailed",
 "n_open": 3,
 "n_entailed": 1,
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
