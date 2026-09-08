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
 "Name": "own_errors_pass_the_gate",
 "Title": "The Reader Cannot Grade Its Own Homework: Self-Authored Contamination Evades Read-Time Detection in Agent Experience Stores",
 "Short Hypothesis": "A reader asked to verify retrieved experience before acting misses planted errors more often when the host trajectory was written by itself than when the identical error is planted in a trajectory written by another backbone, because self-authored text is familiar (low perplexity under the reader) and LLM judges favour familiar text. Consequently the reader's own pool is the more dangerous contamination vector per planted error, an external reference (a static procedure prompt) closes most of the gap, and a content detector costs far less legitimate foreign gain than a writer-identity gate.",
 "Related Work": "Self-preference in LLM evaluation is established outside agents: 2404.13076 (evaluators recognise and favour their own generations), 2410.21819 (bias tracks familiarity measured by perplexity), 2504.03846 (harmful vs legitimate self-preference on verifiable tasks), 2402.11436 (self-bias in self-refinement, reduced by external feedback). None applies it to verifying retrieved action trajectories or measures downstream task harm. Memory contamination work is adversarial and single-backbone: 2512.16962 MemoryGraft (benign-looking implanted experiences, no defence), 2605.22842 (trust laundering, policy-formatted documents), 2608.11888 (seemingly relevant skills cause failures, author-reader mismatch not examined), 2601.05504 (attack/defence with trust-threshold calibration), 2510.02373 A-MemGuard (consensus validation), 2608.03509 SkillJack, 2607.06595, 2602.15654. None manipulates authorship of the contaminated item, none scores a reader-side detector by precision and recall against planted labels, and none costs its defence on non-adversarial foreign content (G9). Archived lineage_blast_radius (4.75) concerned consolidation laundering low-trust experience under a provenance rule and was judged entailed by that rule; here there is no consolidation rule, the detector is the reader's own judgement and its false-positive cost on clean foreign items is measured.",
 "Abstract": "Whether an agent can tell a helpful retrieved experience from a harmful one at read time is unmeasured, and every memory-poisoning study plants its poison in a single backbone's store. We ask a sharper question: does detection depend on who wrote the contaminated item? The self-preference literature shows LLM judges favour text they could have produced themselves, with bias tracking perplexity. We import that mechanism into experience verification. On ALFWorld we take success-filtered pools written by Qwen3-32B, EXAONE-4.0-32B and an expert planner, and apply one scripted edit rule to each -- a procedure graft (heat steps swapped for cool steps under a heat task), a wrong final receptacle, and, as an ecological family, the writer's own failures relabelled as successes -- so that error content is identical across writers and only authorship differs. Each reader verifies retrieved items before acting; we score precision and recall against planted labels in a reader x host-writer cross design, so a pool-difficulty main effect is separated from an authorship interaction. We predict recall at least 10 points lower on self-authored hosts, that paraphrasing foreign items with the reader lowers their perplexity and their detection, that giving the verifier a static procedure prompt halves the gap, and that at matched planting rates self-authored contamination costs more success per unit of clean gain. Downstream cells with and without the detector as a gate, on contaminated and on clean multi-writer stores, put the defence's cost on legitimate foreign transfer in the same units as the harm it prevents.",
 "Experiments": "Domain and partition as in Measurement A with the 400-game held-out training slice added: 674 games x 2 seeds per downstream cell. Pools (hosts): Q = Qwen3-32B successes, X = EXAONE-4.0-32B successes (collected, 3 GPU-h, shared with sibling proposals), E = expert walkthroughs; plus each model's failed trajectories for family C3. Contamination families, applied by one script identically to every host pool: C1 procedure graft (manipulation sub-sequence of type T replaced by the sub-sequence of type T' with room-consistent receptacle names; task and label stay T); C2 receptacle swap (final put target replaced by a plausible wrong receptacle of the same room); C3 natural errors (the writer's own failures relabelled as successes; content varies by writer by nature). A hard C1 variant (a single omitted or wrong step, e.g., no 'open fridge') is pre-registered for use if C1 recall is above 80% for both hosts. Bank rates 0/10/30/50% within the retrieved task type, giving expected 0/0.3/0.9/1.5 contaminated items among k=3. Gate 0: C1 at 50% in the Q->Qwen3 cell must cost >= 6 net vs the clean bank; if not, a 100% cell is run as an existence check and the proposal stops if harm is still < 6. Detector: before acting, the reader judges each retrieved item ('does this trajectory correctly solve its stated task? yes/no, one-line reason'); D0 zero-shot; D1 with the Measurement C static six-procedure prompt in the verification context; D-consensus: majority of three samples (A-MemGuard-style named baseline); D-NLL: a non-LLM baseline flagging the top-x% items by the reader's per-token NLL. Precision and recall per (reader, host writer, family, detector) with >= 600 planted and >= 600 clean items per cell (about 32k short verification calls, 1-2 h on one replica). Reader NLL per item logged via vLLM prompt logprobs (manipulation check: self-authored hosts have lower NLL; this is entailed and is not a prediction). Paraphrase arm: foreign contaminated and clean items rewritten by the reader with content preserved (script verifies the planted error survives), re-verified. Downstream: C1 rate sweep (4 rates) x host {Q, X} x reader {Qwen3, EXAONE} = 16 cells; detector-gated arms (flagged items dropped and refilled from the next retrieved rank) at 30% for both hosts and readers = 4 cells; clean (rate 0) three-writer mixed store with no gate, D0 gate, D1 gate and writer-identity gate (drop all foreign) per reader = 8 cells; k=0 and static prompt per reader = 4 cells. About 32 cells, about 43k episodes, about 20 h on two replicas. Optional capability arm: gpt-oss-120b as third reader on its own pool (3 GPU-h collection) vs Q hosts. Scheduling: verification calls and paraphrases run on one replica while the other collects X; downstream cells split across both replicas; about 2 days. Pre-registration of gates, margins and amendments before the first confirmatory cell.",
 "Baselines and Ablations": "No detector (plain retrieval) at every rate. D-NLL familiarity baseline (expected to be worst on self hosts: it encodes the bias). D-consensus (A-MemGuard-style self-consistency). Writer-identity gate (drop foreign) as the provenance-style comparator on the clean store. D1 (external reference) vs D0. Families C1, C2, C3 and the hard C1 variant. Format normalisation (thoughts stripped to actions and observations) for both hosts, to separate authorship recognition by format from familiarity of content. Paraphrase arm on foreign items (content fixed, familiarity raised). Detector prompt position (item before or after the task). Type-stratified precision/recall. Memory-free and static-prompt baselines for all downstream cells; every gain reported net of the static prompt; retained-gain ratio of the clean foreign cells vs self reported as context for the leverage estimand.",
 "Falsifiable Predictions": "P1 (Gate 0): C1 at 50% bank rate in Q->Qwen3 reduces net success by >= 6 points vs the clean bank. Falsified if harm < 6 at 50% and at 100%; produced by the C1 rate-sweep cells. P2 (headline authorship effect): D0 recall on C1 items is >= 10 points lower on self-authored hosts than on foreign-authored hosts for both readers, i.e., the reader x host-writer interaction has a 95% CI excluding 0. Falsified if recall(self host) >= recall(foreign host) for either reader, or if both readers show the same host ordering (a pool-difficulty main effect with no interaction); produced by the 2x2 C1 verification cells {Qwen3, EXAONE} x {Q hosts, X hosts}. P3 (familiarity mediates): reader-paraphrased foreign contaminated items are detected at a recall >= 8 points lower than the unparaphrased originals while their NLL falls. Falsified if recall is within +-4 of the original although NLL falls by the amount seen for self hosts; produced by the paraphrase cell. P4 (external reference closes the gap): D1 raises self-host recall by >= 10 points and reduces the self-foreign gap to at most half of its D0 value. Falsified if D1 self-host recall is within +-4 of D0; produced by the D1 cells. P5 (downstream leverage): at 30% rate, contamination leverage = (clean gain - contaminated gain)/clean gain is >= 0.15 larger for self hosts than for foreign hosts for the Qwen3 reader. Falsified if leverage(foreign) >= leverage(self) with CI excluding the margin; produced by the 30% C1 cells and their clean denominators. P6 (governance cost, G9): on the clean three-writer store the D0 gate blocks < 10% of clean foreign items and costs < 3 net points, while the writer-identity gate costs at least the foreign excess over the self pool. Falsified if the D0 gate's false-positive rate on clean foreign items is >= 20% or its cost is >= 6 net; produced by the rate-0 gated cells.",
 "Measurement and Noise Control": "Verification cells: >= 600 planted and >= 600 clean items per (reader, host, family, detector), Bernoulli SE about 2 points on recall, interaction SE about 4 points, so the 10-point margin of P2 is detectable; items are the same underlying trajectories edited identically across hosts wherever the host pools share training games (paired by game where possible). Downstream cells: 674 games x 2 seeds, half-width about +-5 net per cell; Gate-0 margin 6 net is 0.22 of Measurement A's +27; leverage CIs by cluster bootstrap over games. Retrieval fixed and logged so contaminated and clean arms differ only in the planted items; planting is seeded and the planted ids recorded per episode so that harm is attributable to episodes that actually retrieved a contaminated item (the per-retrieval harm is a secondary estimand). Injected tokens logged; gated arms refill to matched k so token counts match ungated arms within +-10%. Pre-registered rule: the headline family is the one whose D0 recall on foreign hosts lies in 30-80% (ceiling and floor avoidance), chosen on a 100-item pilot before confirmatory cells.",
 "Preprint Collision Check": "(1) mechanism, last 12 months, query 'agent memory poisoning benign-looking experience records read-time detection self-generated versus foreign entries' --recent, channel s2+hf: 2608.03509 SkillJack, 2607.06595 GhostWriter, 2602.15654 Zombie Agents, 2603.02240 SuperLocalMemory (Bayesian trust), 2601.05504 (attack and defence, trust thresholds), 2512.16962 MemoryGraft, 2510.02373 A-MemGuard, 2503.03704 MINJA; all adversarial and single-backbone, none manipulates the author of the contaminated item or reports detector precision/recall by authorship. (2) closest named method and home: query 'self-preference bias LLM evaluators recognize and favor their own generations perplexity' (no agent, memory, retrieval, experience or benchmark words), channel s2+hf: 2404.13076 (NeurIPS 2024, 737 citations), 2410.21819 (perplexity-familiarity mechanism), 2504.03846 (harmful vs legitimate self-preference on verifiable tasks), 2402.11436 (self-bias in self-refinement, external feedback helps), 2510.08145 Genii, 2506.02592 DBG score; none evaluates verification of action trajectories, planted errors in self vs foreign hosts, or downstream task harm. (3) an earlier long-form variant of query (1) returned 'no results on S2 or HF' before shortening. No collision; the closest combination (self-preference + memory poisoning) does not appear in either channel.",
 "Risk Factors and Limitations": "Self-preference may not manifest for judging action sequences as it does for judging prose; P2 then fails cleanly and the report is that authorship does not affect detectability in this domain. The C1 graft may be trivially detectable (ceiling) or the C3 natural errors trivially hard (floor); the pilot-selected family and the hard C1 variant guard against this. Authorship could be recognised by format (thought style) rather than by familiarity of content; the format-normalised and paraphrase arms separate these, and P3 is the mediation test. Foreign raw items may be used less by the reader, which lowers both their clean gain and their harm; the leverage estimand normalises by clean gain but is a ratio and is reported with bootstrap CIs and as secondary. EXAONE serving is unverified; fallback is gpt-oss-120b (capability confound) for the foreign host and a second Qwen3 scaffold for a proximity-only host. The detector adds one call per retrieved item; its token cost is reported with the gains. Security framing is limited to manufactured contamination as the brief requires.",
 "Addresses gap": "G8 (no read-time detection of harmful retrieved entries, and whether susceptibility depends on writer-reader relation), with G9 (cost of a defence on legitimate non-adversarial foreign content) as the secondary estimand.",
 "Not a restatement of": "Brief prior-result bullet Measurement A ('look-at-in-light is the one negative type, -4.8'): it observed one harmful type from one writer without asking whether the reader could have flagged the items; this idea claims the reader's ability to flag a harmful item depends on who wrote it, which the observational result cannot show. Digest card arxiv:2512.16962 (MemoryGraft: benign-looking implanted experiences cause persistent drift, one backbone, no defence): this idea plants identical errors in self- and foreign-written hosts and scores a reader-side detector by precision and recall, claiming the reader's own pool is the harder case. Archived lineage_blast_radius (4.75) was a consolidation-rule result; here no rule exists, the detector is the reader's judgement and its false-positive cost on clean foreign items is measured."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "own_errors_pass_the_gate",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "C1 (procedure graft) at 50% bank rate vs the clean bank in the Q->Qwen3 downstream cell, 674 games x 2 seeds, half-width ~+-5 net, with a 100% cell as an existence check.",
   "falsifier": "Harm < 6 net at 50% and also at 100%.",
   "label": "open",
   "reason": "A reader that ignores or repairs grafted wrong procedures (1.5 expected contaminated items among k=3) simply shows no success loss, and the 100% backstop roughly doubles the effect, so the no-harm world is separable from the >=6 world at the stated half-width.",
   "fix": ""
  },
  {
   "id": "P2",
   "depends_on": "2x2 D0 verification cells {Qwen3, EXAONE} x {Q hosts, X hosts} on C1 items, >=600 planted and >=600 clean per cell, recall SE ~2 and interaction SE ~4, with the headline family pre-selected so foreign-host recall lies in 30-80%.",
   "falsifier": "recall(self host) >= recall(foreign host) for either reader, or both readers showing the same host ordering (pool-difficulty main effect, no interaction).",
   "label": "open",
   "reason": "Both readers are crossed with both host pools on identically edited, game-paired items and the ceiling/floor rule keeps recall off the rails, so a null, a reversal, or a pure pool main effect are all measurable against the 10-point margin at a 4-point interaction SE.",
   "fix": ""
  },
  {
   "id": "P3",
   "depends_on": "Paraphrase arm: foreign contaminated items rewritten by the reader with the planted error script-verified to survive, re-verified by D0, with per-item reader NLL logged.",
   "falsifier": "Recall within +-4 of the unparaphrased original ALTHOUGH NLL falls by the amount seen for self hosts.",
   "label": "near_entailed",
   "reason": "The falsifier is gated on the paraphrase actually driving NLL down to self-host levels - an outcome the design neither guarantees, measures against a tolerance, nor controls - and the +-4 equivalence band is inside the ~+-5.6 half-width of a recall difference at SE ~2 per arm.",
   "fix": "Pre-register an NLL-matching criterion (retain only paraphrases within a stated NLL distance of self-host items and report the qualifying fraction) plus a two-sided equivalence bound with item counts giving half-width <= 3."
  },
  {
   "id": "P4",
   "depends_on": "D1 (static six-procedure prompt inside the verification context) vs D0 recall on self hosts and on foreign hosts, per reader, on the same planted item sets.",
   "falsifier": "D1 self-host recall within +-4 of D0.",
   "label": "near_entailed",
   "reason": "Only the first clause carries a falsifier: the gap-halving clause the hypothesis rests on can fail (D1 lifting foreign-host recall equally, leaving the gap intact) with no stated falsifying outcome, and the +-4 band is inside the recall-difference noise.",
   "fix": "Add an explicit falsifier on the gap estimand (gap_D1 > 0.5 x gap_D0 with CI excluding), score D0 and D1 on identical paired items, and size the cells for a half-width <= 3."
  },
  {
   "id": "P5",
   "depends_on": "30% C1 cells for Q hosts and X hosts with the Qwen3 reader and their clean-bank denominators; each gain carries half-width ~+-5 net, and clean foreign gain is expected to be smaller than clean self gain.",
   "falsifier": "leverage(foreign) >= leverage(self) with CI excluding the 0.15 margin.",
   "label": "unresolvable",
   "reason": "Leverage is a ratio whose denominator is itself a +-5 gain that differs between self and foreign pools, so the CI on the 0.15 difference is far wider than the margin (and the normalisation actually pushes against the prediction whenever the foreign clean gain is the smaller denominator).",
   "fix": "Score absolute harm (clean minus contaminated net points) per host with a paired cluster bootstrap and a margin at least twice the reported half-width, or add seeds until the leverage CI is under 0.15."
  },
  {
   "id": "P6",
   "depends_on": "Rate-0 three-writer clean store per reader with no gate, D0 gate, D1 gate and writer-identity gate; FPR measured on >=600 clean foreign items (SE ~1.6 points), cost measured in net points at +-5 per cell.",
   "falsifier": "D0 gate false-positive rate on clean foreign items >= 20%, or its cost >= 6 net.",
   "label": "near_entailed",
   "reason": "The second clause is true by construction - the writer-identity gate deletes every foreign item, so its cost IS the mixed-store minus self-store gain, the same quantity it is compared with - and the <3 vs >=6 cost band lies inside the +-5 per-cell noise, leaving only the FPR clause genuinely able to fail.",
   "fix": "Drop or restate the identity-gate clause as a measured quantity with its own CI, and set the cost falsifier at a margin at least twice the +-5 half-width (or add seeds on the gated cells)."
  }
 ],
 "shared_terms": [
  "P2-P3: the unparaphrased foreign-host D0 recall is the same measurement in both, so P3's baseline is P2's foreign-host cell.",
  "P2-P4: P4's self-foreign recall gap IS P2's estimand, so a null in P2 leaves P4's halving clause undefined.",
  "P1-P5: P5's leverage numerator and denominator are built from the same clean-bank and C1-contaminated Q->Qwen3 cells that produce P1's Gate-0 harm.",
  "P5-P6: both rest on the clean self vs clean foreign gains (P6's 'foreign excess over the self pool', P5's clean denominators)."
 ],
 "headline": "P2",
 "headline_status": "open",
 "n_open": 2,
 "n_entailed": 0,
 "n_near": 3,
 "n_unresolvable": 1,
 "verdict": "revise"
}

=== BINDING RULES FROM THE BRIEF ===
## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **Writer identity is manipulated, not observed.** The same task set, the same bank construction and the same retriever,
  with only the writer swapped (expert / self / other backbone / mixed); and the same store read by several readers.
- **Self-pool control at matched collection cost.** Any foreign-experience arm is compared with a pool the reader collected
  itself at the same episode or token budget; "foreign memory helps" without this arm is the gain of having any memory.
- **Retained-gain ratio is the estimand,** reported per writer × reader cell with seeds: reader's gain from the writer's pool
  divided by the writer's own gain from the same pool (or divided by the reader's self-pool gain), with CIs.
- **Static-procedure baseline (Measurement C) in every design.** A reader that gains nothing from any writer beyond a fixed
  procedure prompt has nothing to transfer; report every transfer gain net of it.
- **Contamination arms are manufactured, gated and positively controlled.** Planted wrong items at controlled rates, by
  writer identity; Gate 0 requires the harm to be ≥ 6 net points at some rate; a read-time detector is scored by precision
  and recall, not by the downstream success change alone.
- **Capability and proximity are separated.** The archived idea closer_beats_stronger (5.75) claimed policy proximity, not
  capability, predicts transfer; a new proposal must vary proximity at fixed capability (same backbone, different scaffold,
  temperature or training) and capability at fixed proximity, or it is a restatement.
- **Every trained or adapted component is evaluated memory-absent, matched and mismatched**; an adaptation step is compared
  with direct injection of the unmodified item at matched tokens.
- **Per prediction: the falsifying outcome and the arm that can produce it.** A prediction whose falsifier no arm can
  produce (a split that never gives the reader the information; an append-only store; a warm start; an identity between
  estimands; a falsifier inside the stated CI) is sent back before review.
- **One literature search in the home vocabulary** of the mechanism (knowledge distillation, transfer learning negative
  transfer, data poisoning, imitation from suboptimal demonstrations, ensemble diversity), no agent/memory/benchmark words.
- **Power and budget:** paired cells, ±8 net at 274 × 2 seeds; margins as fractions of the Gate-0 effect; cell-by-cell episode
  counts; both A100s busy (one serves a reader while the other serves a writer or trains); days, not weeks.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
