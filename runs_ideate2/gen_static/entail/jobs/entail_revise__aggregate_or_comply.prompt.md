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
 "Name": "aggregate_or_comply",
 "Title": "Aggregate or Comply: Compiled Playbooks, Whole-Bank Context and Top-k Retrieval Under a Manipulated Contamination Rate of the Experience Bank",
 "Short Hypothesis": "The three ways of consuming an experience bank differ in where items are combined: a per-query retriever exposes the agent to each item at its bank share, an LLM compiler aggregates before the agent sees anything, and a long-context reader aggregates (or not) at read time. Under a manipulated fraction p of replay-validated wrong-procedure items, retrieval success falls already at minority contamination (compliance rather than majority voting), LLM-compiled playbooks stay flat until the contaminant is the majority and then collapse, and the whole-bank arm reveals whether the reader is an aggregator or a complier. The static route's first advantage over retrieval is robustness, not accuracy, and it is invisible in every existing comparison because their banks are clean.",
 "Related Work": "The compliance trap (2607.10608) shows agents adopt conflicting retrieved memory at the first exposed decision point and lists as untested whether compiled/static instructions induce the same behaviour and how the damage scales; it observes one route with fixed contamination. MemoryGraft (2512.16962), PoisonedEvolution (2608.05563), memory-poisoning attack/defence (2601.05504) and A-MemGuard (2510.02373, consensus-based validation) are security papers: single route, adversarially crafted items, attack success as outcome, no matched compiled-vs-retrieved-vs-whole-bank comparison and no dose-response on task success. MemAPO (2603.21520) argues per-query retrieval beats one compiled prompt on heterogeneous queries with a clean bank. Rethinking the Role of Demonstrations (2202.12837) found label correctness in in-context demonstrations barely matters for classification, an opposing prior that makes the compliance prediction non-trivial. Training-time poisoning shows phase transitions at a poisoning ratio (2303.03592) and aggregation as a certified defence (Run-Off Election, 2302.02300); no in-context, agentic analogue at the level of task success exists. Archived optimizer_substitutes_for_memory_scaffold (5.22) spoke of 'content harm' without manipulating content; here content harm is dosed. SkillEvolBench (2605.24117) reports skill gains unstable without variance; here compile-draw variance is measured.",
 "Abstract": "Every reported comparison of compiled artifacts with query-time retrieval uses a bank of successes that are all correct, so it cannot see the property that most distinguishes the two routes: how they combine items. We build contaminated versions of the ALFWorld expert pool in which a fraction p in {0, .25, .5, .75, 1} of the heat/cool/clean trajectories have their procedure-defining step replaced by a plausible, executable but goal-ineffective step at a distractor receptacle in the same scene; every poisoned item is replayed in its game and kept only if it fails, and it replaces a clean item so bank size and goal-sentence distribution are unchanged (the goal-sentence retriever cannot tell them apart, so exposure is p per slot by construction; the outcome of interest is the agent's success response, which is not). Five routes consume each bank on the same (game, seed) cells: goal-query top-3 retrieval, an LLM-compiled six-procedure playbook (Qwen3-32B summarising 12 sampled same-type items, cached, three draws, artifact content audited), a rule-compiled majority playbook (reference aggregator), the whole bank of 80 items in context (cached), and a fixed exemplar set sampled once (type-conditioned static, two draws). Task success on the three procedure types is primary; the untouched pick types are an in-arm negative control; cost is uncached prefill per episode under caching. The design tests whether the reader outvotes a minority wrong item or complies with it, whether an LLM compiler hedges or aggregates, whether a long-context reader aggregates implicitly, and whether a wrong instruction is followed more or less than a wrong exemplar.",
 "Experiments": "Poison construction: for each expert heat/cool/clean trajectory, replace the procedure-defining action (e.g., heat with microwave) by a same-scene distractor sequence (e.g., put the object on stoveburner 1, take it back), leave all other steps intact, replay under the ALFWorld engine and keep only items with success = 0 and no invalid steps; contamination rate p applied per type at {0, .25, .5, .75, 1} by replacement. Routes (arms), each 274 games x 2 seeds paired with A/C: R1 goal-query retrieval k=3 (A's retriever; p=0 cell exists); R2 LLM-compiled playbook: Qwen3-32B writes one procedure per type from 12 uniformly sampled same-type items with a compiler prompt that forbids using knowledge outside the sample; ~400 tokens, type-agnostic, cached; three draws per p; each artifact audited (clean / poisoned / hedged per type); R3 rule-compiled playbook: majority extraction of the procedure-defining action template over the same 12 items (its flatness below p=.5 is by construction and is reported, not predicted); R4 whole-bank_80: 80 type-balanced items sampled from the contaminated bank (realised contamination recorded), fixed order per seed, cached; R5 fixed exemplar set: 3 items per type sampled once (type-conditioned static), two draws. Plus k=0 (exists) and, exploratory, a realism arm where contamination is stale items produced by a name-swap wrapper (microwave <-> stoveburner) so the wrong items were once right. Order: positive control at p=1 for R1 (poison is followed and hurts) before anything else; then p=.25 cells for R1/R2/R4 (the decisive shape cells); then the rest. Count: 4 new p levels x (R1 + 3xR2 + R3 + R4 + 2xR5 = 8) = 32 arms, ~16 h on two A100s with two vLLM replicas and workers tuned to the queue; the headline cells are replicated with two further seeds.",
 "Baselines and Ablations": "Baseline is the best static arm at each p (R2/R3/R5), with retrieval reported as retrieval minus best static; the type-agnostic requirement is met by R2/R3/R4 (all six procedures, no type selection); R5 is the type-conditioned static counterpart. Ablations: p dose (5 levels); compiler identity (LLM vs rule) and compiler-draw variance; static-sample (R5) vs retrieved-sample (R1) at equal expected exposure; wrong instruction (R3 at p=1) vs wrong exemplars (R1 at p=1) at identical content; whole-bank realised contamination as a covariate; pick types as untouched control; token accounting: R1 uncached 430 tokens per episode vs cached prefixes for R2-R5.",
 "Falsifiable Predictions": "P1 (positive control, gate): at p=1, R1 loses >= 20 points vs its p=0 cell on the pooled procedure-type cell (~137 games x 2 seeds; floor +-12; 20 ~ half the Gate-0 gain on these types) and lands at or below k=0. Falsified if the loss is < 12 (the agent does not follow the wrong procedure); arm R1_p1; the study stops there and reports the poison as inert. P2 (compliance at minority contamination): R1 at p=.25 loses >= 12 vs p=0 on the procedure cell. Falsified if the loss is < 12 (the reader outvotes one wrong item in three, the 2202.12837 prior); arm R1_p.25. P3 (LLM compiler aggregates): R2 at p=.25 loses < 12 vs p=0, and R2 at p=.75 loses >= 20. Falsified (first half) if R2_p.25 loses >= 12 across draws, with the audit showing hedged or poisoned procedures; falsified (second half) if R2_p.75 is within +-12 of p=0, with the audit showing the compiler restored the clean procedure from its own knowledge (compiler-prior confound, reported as such); arms R2_p.25, R2_p.75. Not entailed: unlike R3, the LLM artifact is not determined by the majority. P4 (whole-bank reader is a complier): R4 at p=.25 loses >= 12 vs R4 at p=0. Falsified if R4_p.25 is within +-12 of R4_p0 while R1_p.25 lost >= 12 (the reader aggregates in context); arm R4_p.25. P5 (instruction slot is no safer than exemplar slot): R3 at p=1 loses at least as much as R1 at p=1 (R3_p1 minus R1_p1 <= +12). Falsified if the wrong instruction damages less than the wrong exemplars by >= 12; arms R3_p1 vs R1_p1. P6 (static sample equals retrieval in expectation, not in realisation): the mean over R5 draws at p=.25 is within +-12 of R1_p.25 while the between-draw spread of R5 at p=.5 is >= 12 points. Falsified if R5's draw mean differs from R1 by >= 12 (a fixed wrong exemplar is treated differently from a retrieved one) or if the spread is < 12; arms R5 draws. P7 (in-arm control): pick-type success is within +-12 of p=0 at every p for every route; falsified if it moves by >= 12 (spillover from the contaminated procedures), which would invalidate the per-type attribution.",
 "Measurement and Noise Control": "Paired (game, seed) cells; net = paired success difference in points; floor +-8 at 274 x 2, +-12 on the pooled procedure-type cell; margins 12 (floor) and 20 (half the Gate-0 gain on the procedure types). Dose-response: paired regression of success on p with game as block, reported with bootstrap CI over games (seeds nested); compile draws nested inside arms and reported as between-draw SD. Positive control (P1) gates the rest; pick types are the in-arm control. Poison validity is mechanical (replay failure) not judged. Prefill tokens per episode logged for cached (R2-R5) and uncached (R1) prefixes; results plotted on the accuracy-cost plane. Pre-registration of arms, cells, margins, audit rubric and the stopping rule before the first confirmatory cell; decoding, max steps and games identical across arms.",
 "Preprint Collision Check": "Q4 (recent, mechanism) 'memory poisoning LLM agent experience bank poisoned trajectories fraction' --recent, channel S2+HF: 2608.05563 PoisonedEvolution (trajectory poisoning of self-evolving skill systems; attack, single route, evidence promotion as boundary), 2512.16962 MemoryGraft (poisoned experience retrieval; attack), 2601.05504 (memory poisoning attack and defence; trust-aware retrieval with temporal decay), 2510.02373 A-MemGuard (consensus-based validation as defence), 2602.15654 Zombie Agents, IEEE Access 2026 temporal dynamics of memory poisoning; none doses the contamination rate on task success or compares retrieval with a compiled playbook and a whole-bank context. Verified with 'paper': 2608.05563 and 2601.05504 abstracts contain no compiled-vs-retrieved comparison. home: Q5 'data poisoning in-context learning fraction of corrupted demonstrations threshold majority' (no agent/memory/retrieval/experience/benchmark words), channel HF: 2303.03592 (phase transition beyond a poisoning ratio, training-time), 2302.02300 Run-Off Election (aggregation as certified defence), 2404.08631 FCert (few-shot support-set poisoning), 2302.10149; the threshold-vs-linear contrast is known for training-time poisoning, not for in-context consumption routes. Q6 (closest named method) 'AgentPoison red-teaming LLM agents poisoning memory knowledge base', channel S2+HF: AgentPoison itself not returned; 2605.01970 Trojan Hippo, 2604.01350 unintentional cross-user contamination in shared-state agents (closest in spirit: non-adversarial contamination; taxonomy, no route comparison), 2604.28157 FlashRT. Q11 (from the P3 searches) surfaced 2202.12837 'Rethinking the Role of Demonstrations' as the opposing prior. Verdict: no pre-emption; the security literature supplies the attack, not the route comparison or the dose-response.",
 "Risk Factors and Limitations": "If the poison is inert (P1 falsified) the study ends with a negative that is itself useful for the compliance-trap literature. The LLM compiler may correct the sample from pretraining knowledge; the audit detects it and the rule compiler remains as the clean aggregator reference. Fabricated poison is a stylised contamination; the stale-item realism arm is exploratory only. Contamination is applied to three types, so the primary cell is half the games (floor +-12). Only Qwen3-32B as reader and compiler; compliance may differ by backbone. Whole-bank realised contamination varies by sample; recorded and used as a covariate. Exposure being p per slot is by construction and is not claimed as a finding.",
 "Addresses gap": "G2 (whether a retriever contributes anything beyond a fixed exemplar set or a static playbook is not isolated; no random/fixed exemplar controls): fixed-sample, compiled and whole-bank routes are compared with retrieval at every contamination level; G4 (run-to-run variance unreported): compile-draw and sample-draw variance are measured and folded into the CI; cross-axis G15 (asymmetry of right vs wrong retrieved memory) is dosed rather than named.",
 "Not a restatement of": "Prior-result bullet 'Two pools on disk (expert 1,465; self 1,892 successes ...)': the pools are taken as given there; this idea manipulates the bank's contamination rate and claims that the routes differ in the shape of their response, which a clean bank cannot show. Digest card arxiv:2607.10608 (compliance trap: agents adopt conflicting retrieved memory; whether static instructions induce the same is untested): this idea answers that question with p manipulated and compiled, whole-bank and fixed-sample routes on the same cells, and claims a threshold response for compilation against a linear one for retrieval."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "aggregate_or_comply",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "R1 (goal-query retrieval k=3) at p=1 vs its existing p=0 cell on the pooled procedure-type cell (~137 games x 2 seeds), floor +-12, plus a comparison to k=0",
   "falsifier": "loss < 12 (the agent does not follow the wrong procedure); study stops and the poison is reported inert",
   "label": "open",
   "reason": "Retrieved exemplars are advisory rather than mandatory, so the agent declining to imitate three replay-validated wrong procedures is a reachable outcome, and the 20-point margin sits above the +-12 floor.",
   "fix": "State what happens when the loss exceeds 12 but the arm stays above k=0, since the conjunction 'loses >= 20 and lands at or below k=0' has no falsifier attached to its second clause."
  },
  {
   "id": "P2",
   "depends_on": "R1 at p=.25 vs R1 at p=0 on the procedure cell, per-type contamination by replacement, k=3 so exposure probability is ~0.58",
   "falsifier": "loss < 12 (the reader outvotes one wrong item in three)",
   "label": "open",
   "reason": "The falsifier is a genuine alternative hypothesis the design can produce, since majority-style resistance at k=3 would show up directly as a sub-floor loss.",
   "fix": "None; note the effect is diluted by the ~58% exposure rate, so record realised per-episode exposure and report the loss conditional on at least one poisoned item retrieved."
  },
  {
   "id": "P3",
   "depends_on": "R2 (Qwen3-32B compiled playbook from 12 same-type items, three draws per p) at p=.25 and p=.75 vs R2 at p=0, plus a per-type clean/poisoned/hedged audit",
   "falsifier": "R2_p.25 loses >= 12 across draws with the audit showing hedged or poisoned procedures; or R2_p.75 within +-12 of p=0 with the audit showing the compiler restored the clean procedure from its own knowledge",
   "label": "near_entailed",
   "reason": "Both falsifiers are gated on a corroborating audit finding and the second is pre-labelled a compiler-prior confound to be reported as such, so a flat R2_p.75 is absorbed as a confound rather than counted against the hypothesis, and a p=.25 drop with a clean-looking audit triggers no falsification at all; the flat half is additionally confirmed by any undetected loss up to the +-12 floor.",
   "fix": "Define both falsifiers on the success numbers alone with the audit reported separately as a descriptive covariate, and fund the R2 p=0 cell, which the 4 new p levels x 8 routes = 32 arm count does not contain."
  },
  {
   "id": "P4",
   "depends_on": "R4 (whole-bank_80 from the contaminated bank, cached, realised contamination recorded) at p=.25 vs R4 at p=0, conditional on R1_p.25",
   "falsifier": "R4_p.25 within +-12 of R4_p0 while R1_p.25 lost >= 12",
   "label": "near_entailed",
   "reason": "The falsifier is written as a conjunction with P2's success, so if R1_p.25 does not lose >= 12 the prediction cannot be falsified by any R4 outcome; and the R4 p=0 comparison cell is not in the 32-arm count, which lists only 4 new p levels.",
   "fix": "State the falsifier on R4 alone (R4_p.25 within +-12 of R4_p0) and add R4_p0 (and the other static p=0 cells) to the arm list and budget."
  },
  {
   "id": "P5",
   "depends_on": "R3 (rule-compiled majority playbook, whose artifact at p=1 is the distractor procedure by construction) at p=1 vs R1 at p=1 on the procedure cell",
   "falsifier": "the wrong instruction damages less than the wrong exemplars by >= 12",
   "label": "near_entailed",
   "reason": "At p=1 both arms deliver the same wrong procedure and P1's own gate requires R1_p1 to land at or below k=0, so both cells are compressed against the procedure-type floor and the near-zero difference that confirms the prediction is largely forced; the falsifier needs the agent to ignore an explicit instruction while obeying exemplars, a dissociation the design never isolates.",
   "fix": "Run the contrast at p=.5 or p=.75 where neither arm is floored, report absolute success levels against the k=0 floor, and add a wrong-instruction-without-exemplars cell so instruction compliance is measured rather than inferred."
  },
  {
   "id": "P6",
   "depends_on": "R5 fixed exemplar set (3 items per type, sampled once, two draws) at p=.25 vs R1_p.25, and the between-draw spread of R5 at p=.5; per-cell floor +-12",
   "falsifier": "R5's draw mean differs from R1 by >= 12, or the between-draw spread at p=.5 is < 12",
   "label": "unresolvable",
   "reason": "The spread claim is estimated from exactly two draws whose own cell noise is +-12, so an observed range of 12 points carries no information about draw-to-draw variance, and the first half is an equivalence claim whose margin equals the floor, i.e. confirmed by any failure to detect.",
   "fix": "Run at least five R5 draws and report the spread with its own bootstrap CI, and set the equivalence margin above the cell's CI half-width (or enlarge the cell) so 'within +-12' is not satisfied by noise."
  },
  {
   "id": "P7",
   "depends_on": "pick-type success (untouched by the poison) at every p for every route, ~137-game cell, floor +-12",
   "falsifier": "pick-type success moves by >= 12 at any p for any route",
   "label": "unresolvable",
   "reason": "As written the control is a conjunction over roughly 32 route x p comparisons each carrying +-12 noise, so chance excursions are expected to trigger the falsifier regardless of true spillover, and the outcome cannot distinguish contamination leakage from multiplicity.",
   "fix": "Replace the all-cells conjunction with one pre-registered pooled test (paired regression of pick-type success on p with route as a factor) and a multiplicity-controlled threshold."
  }
 ],
 "shared_terms": [
  "P1-P2: both are R1 losses measured against the same R1_p0 cell, so a low or high R1_p0 moves both losses together.",
  "P2-P4: P4's falsifier is written conditional on R1_p.25 having lost >= 12, so P2's outcome determines whether P4 can be falsified at all.",
  "P1-P5: P5's contrast contains R1_p1, the same cell P1 requires to land at or below k=0, so P1's gate floors one term of P5's difference.",
  "P2-P6: R1_p.25 is a measured term in both the compliance test and the static-versus-retrieved comparison.",
  "P3-P4-P7: all rest on p=0 cells for R2, R4 and the pick types that the stated count (4 new p levels x 8 routes = 32 arms) does not include, so the same unfunded baseline determines three predictions."
 ],
 "headline": "P2",
 "headline_status": "open",
 "n_open": 2,
 "n_entailed": 0,
 "n_near": 3,
 "n_unresolvable": 2,
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
