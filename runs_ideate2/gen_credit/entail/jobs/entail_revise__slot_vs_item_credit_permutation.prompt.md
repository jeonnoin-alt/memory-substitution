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
 "Name": "slot_vs_item_credit_permutation",
 "Title": "Slot or Item: Separating Position Credit from Content Credit in Retrieved Sets by Permutation and Leave-One-Out",
 "Short Hypothesis": "The per-position marginal value read off nested-k retrieval logs (k=1 within k=3 within k=7) confounds an item's content with its slot. Permuting the same k=3 set on the same (game, seed) separates the two: on sets whose three items share the game's task type, order changes success by less than the noise floor, but on mixed sets moving the single same-type item from slot 1 to slot 3 costs at least 8 net, and a planted conflicting item harms more in slot 1 than in slot 3 by at least 8 net, a primacy premium consistent with early adoption rather than lost-in-the-middle. The nested-k per-position estimate therefore overstates the credit of the rank-1 item by a measurable slot component that must be removed before it is used as item credit.",
 "Related Work": "Lost-in-the-middle position effects are established for long-context QA and revisited for RAG, where arxiv:2505.15561 (EMNLP 2025) finds distracting top-ranked passages matter more than position; primacy in MCQA option order (arxiv:2507.13949); demonstration-order sensitivity of in-context learning is the home literature (order permutations change few-shot accuracy; permutation-invariance violations as a source of order-induced errors, arxiv:2509.11208; PICASO arxiv:2502.17605). None permutes retrieved experience in a multi-step agent or pairs permutation with item-level leave-one-out. The compliance trap (arxiv:2607.10608) locates harm at the first exposed decision point but does not manipulate slot. DIG (arxiv:2509.12765) scores one document at a time and ignores order; CUE-R (arxiv:2604.05467) does not permute. The brief's nested-k per-position counterfactual is the object corrected here. Archived: action_prior_imprinting (5.27) and memory_budget_confound (5.63) concern priors and volume, not slot; retrieved_set_disagreement_gate (4.65) had no item-level ground truth.",
 "Abstract": "Retrieval logs that nest k=1 within k=3 within k=7 on the same games seem to give a per-position counterfactual for free, and every ranked memory system implicitly treats the rank-1 slot as the most valuable. But the item at rank 1 is both the most similar item and the first item the reader sees, so its measured credit mixes content with slot. We separate them by permutation on ALFWorld with a Qwen3-32B reader: the same natural k=3 set is run in original, reversed and rotated order on the same (game, seed), with sets classified from the logs as all-same-type or mixed, and item-level leave-one-out is run under two orders. A manufactured conflicting item placed in slot 1, 2 or 3 gives the sign and size of the slot effect for harm, distinguishing primacy from lost-in-the-middle and recency. A k=7 rotation tests whether the premium survives longer contexts. We predict that order is inert among consistent items but worth at least 8 net when items disagree, and report the fraction of the nested-k rank-1 credit that is slot rather than content, with the noise floor from no-op repeats. The result tells the program whether its free per-position estimate is usable as item credit and how retrieval rank should be read when items are scored.",
 "Experiments": "(1) Materials: k-sweep logs at k=3 and k=7 for all 274 validation games, expert bank, Qwen3-32B on two replicas; sets classified from the logs as ALL-SAME (three same-type items), MIXED (exactly one same-type item, its slot recorded) or ALL-CROSS (rare; reported descriptively). (2) Order cells at k=3: original O = (a,b,c), reversed R = (c,b,a), rotated ROT = (b,c,a), plus a no-op repeat of O; 274 games x 4 seeds x 4 runs = 4,384 episodes (~3.7 h). For MIXED sets an additional forced-slot pair: same-type item in slot 1 vs slot 3 with the two cross-type items in fixed relative order (~2 x 4 x |MIXED| episodes). (3) Leave-one-out under two orders: remove the rank-1 item (ALL-SAME) or the same-type item (MIXED) from O and from R, keeping the remaining two in their order in each: 274 x 4 x 2 = 2,192 episodes (~1.8 h); reported as slot-conditional LOO with the order of the remaining pair as a covariate. (4) Planted-conflict slot arm on procedure types (~140 games): a token-matched wrong-procedure item (as in the CONFLICT class of the pairwise audit) replaces the natural rank-3 item and is placed in slot 1, 2 or 3 with the two natural items shifted; plus the unplanted natural set: 140 x 4 x 4 = 2,240 episodes (~1.9 h). (5) k=7 rotation: rank-1 item moved to slot 7 vs original, MIXED and ALL-SAME, 274 x 2 seeds x 2 = 1,096 episodes plus repeat (~1 h). (6) Nested-k reanalysis: the logs' k=1-vs-k=3 contrast (rank-1 credit) is decomposed using ROT, where the rank-1 item sits in slot 3: content credit = f(ROT) - f(ROT minus rank-1 item); slot component = [f(O) - f(O minus rank-1)] - content credit, with CI. (7) Static-procedure arm from Measurement C nets out type-level credit for MIXED sets. (8) Positive controls first: the planted-conflict item in slot 1 must show harm >= 10 net vs the unplanted set, and MIXED sets must show a k=3-vs-k=0 gain of >= +10 net, before any null on ALL-SAME order effects is read. Total ~11,000 episodes, ~9 h on two A100s.",
 "Baselines and Ablations": "No-op repeat as the noise floor for order effects; ALL-SAME sets as the content-only control; forced-slot MIXED cells as the slot manipulation with content fixed; planted-conflict slot 1/2/3 to separate primacy, middle and recency; k=7 rotation for context length; static-procedure arm for type-level credit; slot-conditional LOO to quantify how much an item's counterfactual value depends on where it is shown; retrieval-score ordering vs random ordering as an additional baseline on MIXED sets.",
 "Falsifiable Predictions": "P1 ALL-SAME: |f(R) - f(O)| <= 4 net. Falsified if >= 8 (order matters even among consistent items), produced by the ALL-SAME R and ROT cells; not entailed because primacy or recency could act on consistent content. P2 MIXED: f(same-type item in slot 1) - f(same-type item in slot 3) >= +8 net. Falsified if <= +3 (slot-invariant reader), produced by the forced-slot MIXED cells. P3 Planted conflict: harm(slot 1) - harm(slot 3) >= 8 net. Falsified if <= 3, or if harm is larger in slot 3 (recency dominance), produced by the planted-slot cells. P4 Middle: harm(slot 2) lies between slot 1 and slot 3 (monotone primacy). Falsified if slot 2 is the minimum (lost-in-the-middle) or the maximum, produced by the slot-2 cells. P5 k=7: rotating the rank-1 item to slot 7 costs >= 8 net on MIXED sets and <= 4 on ALL-SAME sets. Falsified if the MIXED cost is <= 3 (the premium vanishes with longer context), produced by the k=7 rotation cells. P6 Decomposition: the slot component is >= 30% of the nested-k rank-1 credit on MIXED sets and <= 10% on ALL-SAME sets. Falsified if the MIXED slot share is <= 10% (nested-k credit is content), produced by the ROT and slot-conditional LOO cells; not entailed because content credit and slot component are measured in different cells (ROT with and without the item) rather than by subtraction of the same quantity.",
 "Measurement and Noise Control": "All order contrasts are within (game, seed) on the identical item set, so item content is held fixed by construction; the no-op repeat gives the flip rate under no intervention as the null for order effects, and a permutation test over run labels is used for P1. Cells: 274 games x 4 seeds (~1,096 paired cells) for O/R/ROT gives ~+/-5 net on set-level contrasts after game clustering; MIXED subgroup size is read from the logs before pre-registration and, if below 120 games, the bank-disjoint train slice is added for MIXED games only. Planted-conflict cells use ~140 procedure-type games x 4 seeds (~+/-6 net on slot contrasts; thresholds tied to this). Cluster bootstrap over games for all CIs; positive controls precede any null; per-type reporting; the static-procedure arm nets out type credit for the decomposition.",
 "Preprint Collision Check": "Q1 (mechanism, --recent, S2+HF ok): \"order sensitivity of retrieved context position effect on LLM agent task success\" -> RaMem arxiv:2606.22844 (context reinstatement, no permutation), arxiv:2512.02445 (long-context agent refusals), arxiv:2506.08184 (proactive interference in working memory), arxiv:2505.18148 (lost in the haystack), arxiv:2505.15561 (RAG positional bias; verified by `paper`: EMNLP 2025, distracting top-ranked passages outweigh position, QA only); none permutes retrieved experience in a multi-step agent or pairs permutation with item-level LOO. Q2 home: \"in-context demonstration order permutation sensitivity primacy recency\" (S2+HF ok) -> arxiv:2507.13949 (primacy in MCQA), arxiv:2509.11208 (permutation-invariance violations and order-induced errors), arxiv:2502.17605 PICASO (permutation-invariant context composition), arxiv:2407.05483, arxiv:2607.20351 (modality order in VLMs); no agent-memory permutation study and no slot-conditional counterfactual. Q3 (closest named method, --recent, S2+HF ok): \"conflicting memory agent compliance first decision point\" -> arxiv:2607.10608 compliance trap (first exposed decision point, no slot manipulation), arxiv:2605.30087, arxiv:2605.06527. Q4 (S2+HF ok): \"Shapley attribution retrieved documents RAG redundancy synergy\" -> arxiv:2507.04480 and DG-Mem arxiv:2608.23268, neither order-aware. No pre-emption found; arxiv:2505.15561 and arxiv:2607.10608 are the papers to position against.",
 "Risk Factors and Limitations": "MIXED sets may be rare in the expert-bank logs (the train slice or the self pool supplies more); if ALL-CROSS sets are rare the recency test relies on the planted arm. The prompt template may impose its own ordering cues (e.g., numbering), which is held constant and stated. Order effects may interact with item length; token counts are recorded and used as a covariate. Only one reader; whether the slot premium is reader-specific is a consumer-swap arm outside this budget. The decomposition in P6 depends on the additivity of slot and content within a set, which the pairwise audit measures separately; both are reported.",
 "Addresses gap": "G12 (order and position as a component of co-retrieved-set composition in a multi-step agent) and G14 (set-level order effects on naturally retrieved sets rather than synthetic relationships); G15 (noise floor for order effects via no-op repeats).",
 "Not a restatement of": "Brief bullet: \"Retrieval logs hold, per episode, the retrieved item ids in rank order, so a nested-k design already gives one crude per-position counterfactual for free\"; that estimate confounds slot with content, and this idea claims the confound's size and sign by permuting the same set on the same (game, seed) and decomposing rank-1 credit into slot and content. Digest card arxiv:2607.10608 (compliance trap): early-decision-point adoption at the trajectory level; this idea claims a slot premium of stated size for both help and harm, its absence on consistent sets, its shape across slots 1-3 and its survival at k=7, none of which the card manipulates."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "slot_vs_item_credit_permutation",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "ALL-SAME subgroup of the 274 validation games; order cells O, R, ROT plus no-op repeat at 4 seeds; permutation test over run labels; the +/-5 net CI quoted for the full 1,096-cell O/R/ROT set.",
   "falsifier": "|f(R) - f(O)| >= 8 net on ALL-SAME sets (order matters among consistent items).",
   "label": "unresolvable",
   "reason": "Primacy or recency acting on consistent content is reachable, but the +/-5 net CI applies to all 274 games while this prediction is scored on the ALL-SAME subgroup alone (size never stated), so the 4-net equivalence bound sits below the noise and an observed 8 net cannot be separated from the predicted <= 4 net.",
   "fix": "Report the ALL-SAME subgroup size and power it (more seeds, or added bank-disjoint train games) to about +/-2 net, and state the null as a formal equivalence test with the bound above the measured CI."
  },
  {
   "id": "P2",
   "depends_on": "Forced-slot MIXED cells (the single same-type item in slot 1 versus slot 3 with the two cross-type items in fixed relative order), MIXED subgroup at least 120 games x 4 seeds, paired within (game, seed); positive control requiring a MIXED k=3-vs-k=0 gain >= +10 net.",
   "falsifier": "f(slot 1) - f(slot 3) <= +3 net (slot-invariant reader).",
   "label": "unresolvable",
   "reason": "A slot-invariant reader is a live outcome, but 120 games x 4 seeds gives roughly +/-7 net by the proposal's own scaling from 1,096 cells at +/-5 net, wider than the 5-net gap between the +8 prediction and the +3 falsifier, so the pre-registered decision is noise-limited even though a gross null could still be separated from +8.",
   "fix": "Fix the MIXED cell count from the required MDE (about +/-2 net) rather than from whatever the logs happen to yield, or restate the falsifier as a CI whose upper bound excludes +8."
  },
  {
   "id": "P3",
   "depends_on": "Planted-conflict slot arm on about 140 procedure-type games x 4 seeds with the token-matched wrong-procedure item placed at slot 1, 2 or 3 plus the unplanted natural set; stated +/-6 net on slot contrasts; positive control requiring slot-1 harm >= 10 net.",
   "falsifier": "harm(slot 1) - harm(slot 3) <= 3 net, or harm larger in slot 3 (recency dominance).",
   "label": "unresolvable",
   "reason": "Recency dominance is genuinely reachable and its sign would be visible, but the proposal itself states +/-6 net on these slot contrasts, wider than the 5-net gap between its 8-net prediction and its 3-net falsifier, so the pre-registered thresholds are tied to a CI that cannot separate them.",
   "fix": "Add games or seeds until the slot contrast CI is about +/-2 net, or move the falsifier to a difference <= 0 net so only a sign flip counts."
  },
  {
   "id": "P4",
   "depends_on": "The three planted-slot harm means from the same ~140-game x 4-seed cells against the same unplanted reference.",
   "falsifier": "harm(slot 2) is the minimum (lost-in-the-middle) or the maximum.",
   "label": "unresolvable",
   "reason": "The prediction is an ordering of three means with no magnitude attached, and at the stated +/-6 net per contrast the rank of slot 2 is decided by noise (under a true tie it lands at an extreme two times in three), so the falsifier is not distinguishable from the monotone prediction.",
   "fix": "Pre-register magnitudes (for example harm(2) at least 3 net below harm(1) and at least 3 net above harm(3)) and power those two contrasts explicitly."
  },
  {
   "id": "P5",
   "depends_on": "k=7 rotation cells moving the rank-1 item to slot 7 versus the original order, MIXED and ALL-SAME, 274 games x 2 seeds x 2 runs plus a repeat.",
   "falsifier": "the MIXED rotation cost is <= 3 net (the primacy premium vanishes with longer context).",
   "label": "unresolvable",
   "reason": "Loss of the premium at longer context is reachable, but this arm runs only 2 seeds and then splits the games into MIXED and ALL-SAME, putting the MIXED contrast CI well above +/-7 net, so both the 8-vs-3 net decision and the paired <= 4 net ALL-SAME bound lie inside the noise.",
   "fix": "Run the k=7 rotation at 4 seeds on MIXED games sized to about +/-3 net before making the MIXED-versus-ALL-SAME comparison."
  },
  {
   "id": "P6",
   "depends_on": "Nested-k rank-1 credit from the k-sweep logs; content credit f(ROT) - f(ROT minus rank-1); slot component defined as [f(O) - f(O minus rank-1)] minus that content credit; slot-conditional LOO cells (which remove the item from O and from R only); static-procedure arm.",
   "falsifier": "the MIXED slot share is <= 10% of the nested-k rank-1 credit (nested-k credit is content).",
   "label": "unresolvable",
   "reason": "The share is a ratio whose numerator is a difference of two LOO estimates each at +/-5 to +/-7 net over a denominator of the same magnitude, so 30% versus 10% is not separable and no CI for the ratio is stated; the cell f(ROT minus rank-1) is also absent from the experiment list (step 3 removes the item from O and from R), so the two halves of the decomposition would come from differently ordered residual pairs.",
   "fix": "Add the ROT-minus-rank-1 cell so content and slot credit are measured in matched orders, and report the slot component as an absolute net difference with a CI rather than a share of a noisy denominator."
  }
 ],
 "shared_terms": [
  "P2-P6: the MIXED slot component is [f(O) - f(O minus rank-1)] minus [f(ROT) - f(ROT minus rank-1)], built from the same forced-slot and rotation cells as P2, so a confirmed P2 mechanically produces a large P6 slot share and a null P2 forces a small one.",
  "P1-P6: the ALL-SAME order null and P6's <= 10% ALL-SAME slot share are computed from the same f(O) and f(R)/f(ROT) cells, so one determines the other up to the LOO denominator.",
  "P3-P4: harm(slot 1), harm(slot 2) and harm(slot 3) are the same three planted-slot means against the same unplanted reference, so P4's ordering claim is fixed by the two quantities P3 contrasts.",
  "P2-P5: the k=7 rotation re-tests the same MIXED classification and the same rank-1 item content as P2 at a longer context, so it shares the MIXED subgroup and its selection rather than being an independent estimand."
 ],
 "headline": "P2",
 "headline_status": "unresolvable",
 "n_open": 0,
 "n_entailed": 0,
 "n_near": 0,
 "n_unresolvable": 6,
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
