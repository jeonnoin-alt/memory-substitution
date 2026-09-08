=== SYSTEM ===
You are checking research proposals BEFORE review for predictions that cannot come out against the hypothesis.
For EACH proposal, number the items of "Falsifiable Predictions" P1, P2, ... in order of appearance (split prose at each
stated prediction). For each prediction:
1. depends_on: the arms, split, retriever, update rule or estimand it rests on (from Experiments / Baselines).
2. falsifier: the outcome that would falsify it, as the proposal states or implies it.
3. Decide whether that outcome is REACHABLE under the stated design or excluded by construction. Excluded-by-construction
   includes: the falsifying outcome needs information the split never gives the model; the estimand is an algebraic
   identity of another quantity it is compared with (shared measured terms); the update rule cannot produce it (an
   append-only store cannot forget, a chunk-trained adapter cannot retain, a warm-started adapter relearns faster than a
   cold one); the retriever cannot deliver the item class the prediction is about; a ceiling or floor forces the sign;
   the effect re-describes how a pool was built or filtered; a control deletes the very tokens the outcome is scored on;
   the arm that would show the opposite is absent.
4. Decide whether the falsifier is DISTINGUISHABLE at the stated power: compare the margin or threshold with the stated
   CI or MDE; if the falsifier lies inside the stated noise, the prediction is unresolvable, not open.
5. label: "entailed" (falsifier unreachable), "near_entailed" (reachable only through a mechanism the proposal does not
   name or control), "unresolvable" (reachable but inside the stated noise), "open". One sentence of reason; for
   anything but "open", the minimal change (an arm, a split, an estimand, seeds) that would make it open.
Also list shared_terms: pairs of predictions whose estimands share a measured term so that one determines the other.
Be literal and adversarial; do not credit intentions. Per proposal return
{"name": "...", "predictions": [{"id": "P1", "depends_on": "...", "falsifier": "...", "label": "...", "reason": "...", "fix": "..."}],
 "shared_terms": ["P1-P3: ..."], "headline": "P1", "headline_status": "open|entailed|near_entailed|unresolvable",
 "n_open": 0, "n_entailed": 0, "n_near": 0, "n_unresolvable": 0, "verdict": "pass|revise"}
where headline is the prediction the Title or Short Hypothesis rests on, and verdict is "revise" when the headline is not
"open" or when fewer than half of the predictions are "open".

=== USER ===
Check each proposal below independently. Return a JSON ARRAY of per-proposal objects in the same order.

### proposal: stale_dose_law_context_vs_weights
Title: Entry-Gated or Majority-Gated: The Dose Law of Outdated Experience Read from Context versus Trained into Weights
Short Hypothesis: After a hidden rule change in ALFWorld, the same outdated experience items harm the agent under two different dose laws. Read from context at fixed k=3 and fixed injected tokens, harm is entry-gated: one stale item among three realizes at least 60 % of the all-stale harm and the harm depends on the stale item's position. Trained into a QLoRA from a p-stale mix of fixed size, harm is majority-gated under greedy decoding (at most 25 % of the all-stale harm at p=0.25, at least 75 % at p=0.75) and becomes proportional to p under temperature sampling. The stream consequence is that a retrieval bank recovers only when stale items are displaced from the top-k almost entirely, whereas a LoRA recovers as soon as fresh data is the majority of what it was last trained on; the two fitted laws must predict, within CI, the recovery times of an unbounded bank and a continual LoRA on a 400-episode expert stream.

Experiments:
- E0 Gate 0 (expert pool, rule B active on the 274 validation games plus a 200-task reserve of shifted-type train tasks held out of every bank and target partition): k=3 with 3/3 pre-shift items vs 3/3 post-shift items on the heat and clean types must differ by >= 15 net points, else the shift is strengthened (inert receptacle echoes a success message so no in-episode cue exists) and Gate 0 is re-run; if it still fails the claim is declared untestable.
- E1 In-context dose ladder: k=3, d in {0,1,2,3} stale items of matched length drawn from the bank partition (odd task indices), position arms for d=1 (stale first vs last) and d=2, decoy arm (d=1 with the stale item replaced by a relevance-destroyed item of the same length), k=0 reference; 2 seeds on all cells, 3 seeds on d in {0,1,3}.
- E2 Parametric dose ladder: five QLoRA students (nf4, rank 32, one epoch, identical data size = 30 % of the target partition, even task indices, about 2,700 step examples, ~0.6 GPU-h each) at p in {0, 0.25, 0.5, 0.75, 1} stale; evaluated under rule B with memory absent, matched fresh memory (k=3 post-shift items from the bank partition), and mismatched memory (token-matched items from other task types); greedy decoding as in Step 0.
- E3 Decoding ablation: temperature 0.7 for the p in {0.25,0.5,0.75} students (memory absent) and for the in-context d in {1,2} cells; the mixture-policy account predicts linearization of the parametric curve only.
- E4 Stream validation: 300 rule-A expert episodes then 400 rule-B expert episodes on train tasks; arms: unbounded bank at k=3 and continual LoRA (chunk update every 100 target-partition items, no replay); shifted-type probe on the reserve every 100 items; recovery times compared with the values predicted from the E1/E2 laws plus the stale-share arithmetic (hypergeometric draw of d stale among top-3 given counts; fresh fraction of the last chunk for the LoRA).
- E5 Own-rollout pool replication of E1 (d in {0,1,3}) and E2 (p in {0,0.5,1}) once the on-policy pool is complete; post-shift own items are collected under rule B by the k=0 agent.
- E6 Reporting: shifted types (heat, clean), unshifted in-stream types (cool, pick_and_place, look_at) as the off-stream erosion probe for the students, and pick_two_obj_and_place held out of every bank and target partition as the procedure-held-out probe; cumulative cost (GPU-hours, tokens) and a Pareto plot for every arm.

Baselines and Ablations:
- k=0 under rule B and k=3 all-fresh (d=0): the two anchors of the in-context curve.
- Decoy at d=1 (irrelevant item, same length): separates conflict harm from irrelevance harm; volume is constant across the ladder by construction.
- Fresh student (p=0) and base model: anchors of the parametric curve; stale student (p=1) is the positive control and must show the stale procedure (harm >= Gate 0 threshold) before any weights-side claim is made.
- Data-size ablation at p=0.5 (10 % vs 30 % of the target partition) to check the majority threshold is not a data-size artefact.
- Bank-partition swap (items from the other half) to check the in-context law is not item-specific.
- Visible lexical relabel (microwave shown and addressed as heatingunit) as a secondary shift: the entry-gating prediction is expected to weaken when the observation contradicts the item, which is reported as a boundary condition.
- No context-distillation arm is used, so P-CD0 is not required; SFT on trajectories is the only objective.

Falsifiable Predictions:
- P1 In context, f1 = H(d=1)/H(d=3) >= 0.6 and stale-first exceeds stale-last by >= 8 net points on the shifted types; falsified by f1 <= 0.4 or no position effect (the agent averages over items).
- P2 In weights under greedy decoding, H(p=0.25)/H(1) <= 0.25 and H(p=0.75)/H(1) >= 0.75, with the 0.25-to-0.75 interval carrying >= 50 % of the total harm; falsified by a linear curve or by a jump concentrated at p <= 0.25 (weights as brittle as context).
- P3 At temperature 0.7 the parametric curve's linear fit improves and its step statistic halves, while the in-context curve keeps its shape; falsified if the in-context curve linearizes as well.
- P4 Matched fresh memory (k=3) rescues the p=1 student to within 10 net points of the fresh student; a rescue below 50 % of the gap is reported as a crutch-like prior dominating context.
- P5 Decoy harm at d=1 is less than one third of the stale-item harm at d=1.
- P6 On the stream, the unbounded bank's time to 90 % of the all-fresh k=3 accuracy on shifted types exceeds the continual LoRA's by at least 2x, and both observed recovery curves fall inside the bootstrap band predicted from the fitted laws; falsified if the bank recovers as fast as the LoRA or the predictions miss by more than the band.

Measurement and Noise Control:
Every cell is paired over identical (game, seed) across arms; the primary metric is net fixed-minus-broken per 100 on the shifted types with paired bootstrap CIs over games. Power: the Step-0 paired cell of 274 games x 2 seeds gives about +/-8 net points; the shifted-type subset of the validation games (about 95 games) plus the 200-task reserve gives about 300 games x 2 seeds = 600 pairs, i.e. roughly +/-7.5 net points, and 3 seeds on the shape-defining cells bring the MDE for a difference between two dose levels to about 8 net points. Gate 0 requires total stale harm >= 15 net points so that a 60 % vs 40 % split of the harm (P1) and the quartile thresholds (P2) are resolvable; shape statistics (f1, quartile ratios, step statistic) are pre-registered with their thresholds and computed by paired bootstrap. Decoding is fixed at the Step-0 setting for the confirmatory cells; the temperature ablation is a separate pre-registered contrast. The stream validation uses two stream seeds and reports recovery times by isotonic-fit crossing with bootstrap over probe games. If the positive control (p=1 student) does not exhibit the stale procedure, the weights-side law is declared unmeasurable at this data scale rather than flat.

### proposal: reversal_savings_latent_retention
Title: Silenced, Not Erased: Savings on Rule Reversal Separate Latent Retention in Weights from All-or-Nothing Retention in Retrieval Memory
Short Hypothesis: On an A -> B -> A rule stream in ALFWorld, a continual QLoRA whose rule-A accuracy has eroded to the reset-LoRA floor during phase B re-acquires rule A on reversal with at most half the post-return items and GPU-hours of a reset LoRA (savings ratio <= 0.5), because parametric interference silences rather than erases the earlier mapping. Retrieval memory has no latent state: a bounded FIFO bank is the no-retention reference, and the bank policies that do show savings (unbounded, failure-decayed) obtain them only by keeping rule-A items retrievable, which costs a stale tax during B that the continual LoRA does not pay. Both substrates erode; the claim is that the weights channel's erosion is partly reversible for free, the memory channel's only for a price.

Experiments:
- E0 Gate 0: stale harm >= 15 net points on the shifted types (k=3 all-A items under rule B), and the positive control that a QLoRA trained on A-phase items scores >= 15 net points above the base model under rule A; failing either, the shift is strengthened or the claim declared untestable.
- E1 Stream: phases A1 (400 expert items), B (400), A2 (400) sampled from train tasks excluding the held-out type and a 100-task shifted-type reserve; odd items feed the bank arms, even items feed the LoRA arms, so every substrate consumes 200 disjoint items per phase and no bank item is ever a training target. Arms: FIFO bank N=200 (N=600 ablation), unbounded bank, failure-decayed bank (item weight x0.5 when retrieved into a failed episode, x1.2 into a success; retrieval score = similarity x weight), continual QLoRA (chunk of 100 target items, one epoch, no replay), reset QLoRA (adapter re-initialized at each phase boundary, trained on the current phase only), QLoRA with replay buffer (all past target items replayed 1:1 with the chunk).
- E2 Recovery curves: shifted-type probe (about 95 validation games plus the 100-task reserve) under the active rule after 50, 150 and 300 items of phases B and A2, 1 seed per intra-phase point (the curve fit pools points), 2 seeds at phase ends; recovery time = items until 90 % of the arm's own A1-end level, converted to GPU-hours and tokens.
- E3 Erosion probe: at the end of B, all arms probed under rule A (counterfactual environment) on the shifted probe set; Gate 1 requires the continual LoRA to sit within 5 net points of the reset LoRA (behavioural erosion to the floor), else B is lengthened to 800 items before the confirmatory run.
- E4 Phase-end full probes: 274 validation games x 2 seeds under the active rule; LoRA arms with memory absent, matched memory (k=3 from the bank partition of the current phase) and token-matched mismatched memory; bank arms with their own store; unshifted in-stream types and the held-out type reported as the off-stream probe.
- E5 Cost axis: cumulative GPU-hours (chunk training, replay) and cumulative injected tokens per arm plotted against shifted-type accuracy through the stream; Pareto plot at the A2 recovery point.
- E6 Own-rollout replication of the two headline arms (continual vs reset LoRA) and the FIFO bank, with successes collected on-stream under the active rule.

Baselines and Ablations:
- Reset LoRA is the no-savings parametric control; FIFO bank is the no-retention memory reference (its savings ratio is expected near 1 by construction and is reported as a reference, not a finding).
- Replay-buffer LoRA vs unbounded bank: the two explicit-retention arms, matched on what they retain, to compare stale tax and savings across substrates.
- FIFO capacity ablation N=200 vs N=600: eviction share of unshifted-type items varies, giving a non-definitional erosion measurement on the memory side.
- Rank ablation (16 vs 32) and learning-rate ablation for the continual LoRA: savings should shrink as B training becomes more destructive; reported as a boundary condition.
- Self-generated replay (2605.26097 style, 1:1 with chunk) as an alternative retention arm on the weights side if the replay buffer arm shows stale tax.
- Decoy k=3 (relevance-destroyed items of matched length) at phase ends for the bank arms so the bank-vs-LoRA accuracy differences are not attributable to prompt length.

Falsifiable Predictions:
- P1 Continual LoRA savings ratio <= 0.5 while its rule-A probe at B end is within 5 net points of the reset LoRA; falsified by a ratio >= 0.8 (the adapter was overwritten) or by no erosion at B end (then savings are trivial).
- P2 Unbounded bank and decayed bank recover on reversal faster than the FIFO bank, but their stale tax during B (drop on shifted types relative to FIFO at matched stream position) exceeds 10 net points, whereas the continual LoRA's stale tax relative to the reset LoRA is within 5 net points; falsified if the decayed bank obtains savings with a stale tax within noise (retrieval-side retention for free).
- P3 Replay-buffer LoRA behaves like the unbounded bank (larger stale tax, larger savings), i.e. explicit retention costs the same in both substrates; the substrate difference lives in the implicit channel only.
- P4 Off-stream: LoRA arms lose <= 5 net points on unshifted and held-out types over the stream; the FIFO bank's unshifted-type gain drops with eviction share (N=200 below N=600 by a measurable margin), showing type-selective erosion on the memory side; falsified if LoRA arms erode unshifted types by more than the bank does.
- P5 Cost: the continual LoRA reaches its A2 recovery at <= 0.3 GPU-hours and zero injected tokens beyond the stream, while every bank arm pays about 430 tokens per episode throughout; on the two-axis plot no bank arm dominates the continual LoRA at the A2 recovery point.

Measurement and Noise Control:
All arms see the identical task sequence and seeds (paired stream); probe games are paired across arms and phases. The shifted probe set (about 195 games) at 2 seeds gives roughly +/-9 net points for a paired difference, adequate for the >= 15-point Gate 0 harm and the 10-point stale-tax prediction; intra-phase points at 1 seed are used only through a monotone (isotonic) fit whose crossing time is bootstrapped over probe games and over the 2 stream seeds run for the headline pair. The savings ratio is reported with a bootstrap CI; the pre-registered success criterion is that the CI upper bound is below 0.7. Gate 1 (erosion to the floor) is checked before the confirmatory run; if the continual LoRA does not erode, B is lengthened and the gate re-run rather than the claim rewritten. Budget: about 20,000 episodes and under 10 GPU-hours of training, roughly five days on two A100s with one GPU serving while the other trains the next chunk.

### proposal: success_filter_lockin_under_shift
Title: Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights
Short Hypothesis: When an agent stores only its own successes, a hidden rule change couples the read and write sides of its memory: stale items suppress post-shift successes on the shifted task types, fewer successes mean fewer fresh items, and the stale share of the store stays high. We claim that this loop produces a practical lock-in for an unbounded retrieval bank (no recovery within 400 post-shift episodes in most stream seeds), because top-k retrieval is winner-take-all over the stale share, whereas a continual QLoRA fed by the same success filter recovers without help in every seed, because a single chunk of fresh successes flips its graded prior; the loop disappears in both substrates when the writer is an exogenous expert, and the exogenous refresh dose needed to break it is larger for the bank than for the LoRA.

Experiments:
- E0 Gate 0 (expert pool, rule B): success rate on shifted types with k=3 all-stale items (s_stale) vs k=0 (s_0) vs k=3 all-fresh; the loop is only testable if s_stale is at least 15 net points below s_0; the required fresh-item count for a stale share <= 1/3 in the top-3 is computed from the pre-shift store size and pre-registered as the lock-in prediction.
- E1 Paired self-collection streams: 150 pre-shift episodes under rule A (one shared collection copied into every arm's store or training set), then 400 post-shift episodes under rule B with 50 % shifted-type sampling, identical task order and sampling seeds across arms, 3 stream seeds. Arms: unbounded bank (k=3), FIFO bank N=150, failure-decayed bank, continual QLoRA (chunk update after every 50 new successes), replay QLoRA (all past successes replayed 1:1), explorer (k=0, writes successes to a store nobody reads).
- E2 Metrics on-stream: shifted-type success per 100-episode window (paired by task sequence), stale share of the top-3 retrieved (bank arms) or fresh fraction of the last training chunk (LoRA arms), time to recovery (first window at or above s_0 plus half the all-fresh k=3 gain), and lock-in indicator (no recovery by episode 400).
- E3 Exogenous refresh ladder: expert post-shift items appended to the store or chunk at 1 % and 10 % of stream episodes, with a relevance-destroyed placebo at the same rate; arms: unbounded bank, decayed bank, continual QLoRA; 3 seeds; escape dose = smallest rate with recovery in >= 2 of 3 seeds.
- E4 Expert-writer control: the same streams with the expert supplying every post-shift item (no success filter) for the unbounded bank and the continual QLoRA, 2 seeds: predicted to recover by displacement arithmetic and by one fresh chunk respectively.
- E5 End probes: 274 validation games x 2 seeds under rule B; LoRA arms with memory absent, matched memory (successes from the explorer's store, disjoint items) and token-matched mismatched memory; bank arms with their own store; unshifted in-stream types and the held-out type as the off-stream probe; positive control that a QLoRA trained on the pre-shift successes exhibits the stale procedure under rule B.
- E6 Cost curves: cumulative injected tokens (about 430 per k=3 episode) and chunk-training GPU-hours per arm against shifted-type success through the stream; Pareto plot at recovery.

Baselines and Ablations:
- Explorer (k=0 writer) is the write-side reference: what the store would receive without read-side harm; a decoy-k=3 explorer (irrelevant items of matched length) checks that its base rate is not a prompt-length effect.
- FIFO bank N=150 is the eviction reference (escape by volume) and N=450 the ablation.
- Failure-decayed bank tests whether a read-side utility rule (Live-Evo style) breaks the loop without exogenous items; two decay constants pre-registered.
- Replay QLoRA vs continual QLoRA: does parametric retention of pre-shift successes reintroduce lock-in on the weights side.
- Expert-writer control isolates the success filter as the cause of lock-in versus pure retrieval competition.
- Placebo refresh (relevance-destroyed items at 1 % and 10 %) separates content from volume; in FIFO it is expected to help by eviction and is reported as such.
- Bank-vs-target partition: LoRA arms never train on items that any bank arm retrieves; the matched-memory end probe uses the explorer's store, whose items are disjoint from every LoRA's training set.

Falsifiable Predictions:
- P1 Unbounded bank locks in (no recovery by episode 400) in >= 2 of 3 seeds and its top-3 stale share stays >= 0.66 throughout in those seeds; falsified if it recovers in >= 2 seeds (the agent self-corrects enough to refresh the store).
- P2 Continual QLoRA recovers in 3 of 3 seeds within 400 episodes and within 2x the FIFO bank's recovery time; falsified if it also locks in (then lock-in is a property of the success filter regardless of substrate, itself reportable).
- P3 Expert-writer control shows no lock-in in any arm: the unbounded bank recovers within the displacement count computed at E0 and the LoRA within two chunks; falsified if the unbounded bank still locks in with an exogenous writer (cause is retrieval competition alone).
- P4 Escape dose: the unbounded bank needs >= 10 % exogenous items, the continual QLoRA escapes at 1 %; placebo items do not release the unbounded bank.
- P5 Failure-decayed bank escapes without exogenous items in >= 2 of 3 seeds; otherwise the decay constants are reported as insufficient for this shift.
- P6 At stream end, the recovered LoRA's memory-free success on shifted types is within 10 net points of the all-fresh k=3 reference, and unshifted and held-out types are within 5 net points of the pre-shift level for every arm except the FIFO bank, whose unshifted gain drops with eviction share.

Measurement and Noise Control:
All arms run the identical post-shift task sequence and sampling seeds, so window-level success differences are paired by episode; with 50 % shifted-type sampling a 100-episode window holds about 50 shifted episodes, giving about +/-14 points per window per seed, which resolves the lock-in contrast (s_stale near 0.1-0.2 vs recovered near 0.7) but not fine differences, so recovery time is estimated from a monotone fit over windows and bootstrapped over episodes and the 3 stream seeds. Gate 0 fixes the effect size the design must resolve: s_0 minus s_stale >= 15 net points on the 95 validation shifted games plus a 100-task reserve at 2 seeds (about +/-9). Lock-in is a binary per-seed outcome and is reported as counts with the recovery curves as the primary quantitative evidence; the pre-registered decision rule for P1/P2 is the sign of the paired difference in mean window success over the last 200 episodes, with CI. End probes use the paired 274-game x 2-seed cell (+/-8). Budget: about 23,000 episodes plus under 5 GPU-hours of chunk training, about five days on two A100s, staged so that E3 and E4 run only if Gate 0 passes.
