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

### proposal: whole_bank_confusability_ladder
Title: Confusable, Not Long: The Whole-Bank-in-Context Route Loses to Top-k Retrieval Only as Near-Miss Trajectories Accumulate
Short Hypothesis: On a six-procedure trajectory bank, reading the whole bank as a cached static prefix matches goal-sentence top-3 retrieval on task success up to the 16k context no matter how many redundant or off-domain items are added; it falls below retrieval only as the count of near-miss items (same object and receptacle words, different procedure) grows, whereas retrieval responds to the near-miss share rather than the count. The bank size at which the two routes cross is therefore set by bank composition, not prompt length, and it is smaller for a weaker reader (Qwen3-8B) than for Qwen3-32B.

Experiments:
- Bank construction from the expert pool (1,465 items). Seed S6 = one expert exemplar per task type, fixed. Growth to 12/24/48/80 items under three rules that keep six procedures: R (redundant, near-miss share 0): add same-type items whose (object, receptacle) pair appears in no item of another type in the bank; N (near-miss, share 0.5): add items in cross-type twin pairs (same object and receptacle, different procedure; twins chosen so their first actions coincide), so at every size half of the items have a twin in the bank; F (filler, sizes 24/48/80 only): S6 plus token-matched trajectories from public TextWorld cooking games in the same format with no ALFWorld nouns. U: one uniformly random fixed 80-subset of the pool (natural near-miss share, measured and reported) as the G17 fixed-random-selection control. Item order type-interleaved, fixed per arm.
- Routes. WB: whole bank as a type-agnostic static prefix (vLLM prefix caching on, cache hit ratio logged). RET: goal-sentence top-3 from the same bank per episode (uncached), same retriever as Measurement A. For every bank both routes run on the same 274 games x 2 seeds.
- Arms at Qwen3-32B: WB x {R,N} x 5 sizes (10), RET x {R,N} x 5 sizes (10), WB x F x 3 sizes (3), WB x U (1); RET on the full pool is Measurement A k=3 (on disk). 24 new arms; WB arms at 48/80 items run 2-3x slower per episode, so about 16 h on two GPUs with one replica each and arms interleaved across replicas.
- Reader manipulation (G16): Qwen3-8B on WB and RET x {R,N} x {12,48,80} (12 arms) plus 8B k=0 and 8B three fixed type-conditioned exemplars (2 arms), about 4 h. Crossover size per reader = smallest size at which WB minus RET is at or below -8 net on the N ladder.
- Error signature: in failed episodes, the fraction in which the executed action sequence follows the twin's procedure (skipped or inserted clean/heat/cool step) is read from the action log, per route and size, to show that the decline is procedure confusion rather than generic length failure.
- Cost: GPU-seconds per episode at fixed concurrency (16 workers per replica), prefill tokens per episode, cache hit ratio; accuracy-cost curves per route and size; the cost crossover is reported separately from the accuracy crossover.
- Order: positive control first (Measurement C wrong-type placebo must sit at least 8 net below the right-type single exemplar, pooled over twin-bearing types); pre-registration; R and N ladders at 32B; then F, U, order re-shuffle check at N-48; then Qwen3-8B.

Baselines and Ablations:
- k=0 (Measurement A) and the five Measurement C static arms: one and three fixed type-conditioned exemplars, wrong-type fixed exemplar (length placebo and near-miss positive control), per-type procedure paragraph, six-procedure type-agnostic prompt; every retrieval number is reported as retrieval minus the best of these at matched tokens.
- RET k=3 over the natural pool (Measurement A) and RET with random fixed selection (three random items from the same bank, fixed per game) at the same token budget, to separate the retriever from the exemplar budget.
- WB x F filler ladder isolates prompt length from content; WB x U fixed random 80-subset is the matched-budget random-selection control at the whole-context budget and supplies a third, natural near-miss share.
- Order ablation (exploratory): N-48 with a second type-interleaved shuffle, to bound order effects that could mimic composition effects.
- Reader ablation: Qwen3-8B on both ladders at three sizes.

Falsifiable Predictions:
- P1 (length does not hurt): WB on the R ladder stays within +/-8 net of WB at S6 through 80 items, and WB on the F ladder stays within +/-8 of S6 at matched tokens. Falsified if WB(R-80) or WB(F-80) is at least 8 net below WB(S6) on the paired cells; arm: WB R-80 and WB F-80 vs WB S6.
- P2 (confusable count hurts the whole-bank route): WB on the N ladder declines monotonically and WB(N-80) minus WB(N-6) is at or below -9 net (one third of the Gate-0 gain), with the decline carried by twin-procedure errors in the action log. Falsified if WB(N-80) is within +/-8 of WB(N-6), or if the decline is not accompanied by a rise in twin-procedure errors; arm: WB N-80 vs WB N-6.
- P3 (retrieval responds to share, not count): RET(N-48) is at least 8 net below RET(R-48), and RET(N-80) is within +/-8 of RET(N-12). Falsified either if RET(N-48) is within +/-8 of RET(R-48) (the retriever is immune to twins, so share does not matter) or if RET declines with size at fixed share; arms: RET N-48 vs RET R-48, RET N-80 vs RET N-12.
- P4 (interaction): [WB(N-80) - WB(N-6)] - [RET(N-80) - RET(N-12)] is at or below -9 net. Falsified if the two routes decline by the same amount (within 8 net) on the N ladder; arms: the four cells named.
- P5 (crossover moves with reader): on the N ladder Qwen3-8B's crossover size is smaller than Qwen3-32B's (8B crosses at 48 or earlier when 32B crosses at 80 or not at all). Falsified if 8B crosses at the same size or later than 32B, or if 8B shows no crossover while 32B does; arms: 8B WB N-48/N-80 vs 8B RET N-48/N-80, against the 32B cells.
- P6 (fixed random selection): WB(U-80) is within +/-8 of RET k=3 on the full pool (Measurement A). Falsified if WB(U-80) is at least 8 net below Measurement A k=3; arm: WB U-80.

Measurement and Noise Control:
All arms run the same 274 games (140 valid_seen + 134 valid_unseen) x 2 seeds with identical seeds across arms; every contrast is a paired net difference with the +/-8 net floor at 274 x 2; confirmatory effects must exceed the floor and be at least one third of the Gate-0 retrieval gain (+27 net at k=3). Crossover size is defined before the run as the smallest ladder size at which WB minus RET is at or below -8 net. Per-type claims are made only on the pooled twin-bearing types (clean, heat, cool, pick-and-place) and declared exploratory. Positive control before any null: the Measurement C wrong-type placebo must be at least 8 net below the right-type single exemplar; if it is not, the near-miss manipulation has no leverage and the design stops. Order sensitivity is bounded by the N-48 re-shuffle cell. Cost is measured, not modelled: GPU-seconds per episode at fixed concurrency with prefix caching on, prefill tokens and cache hit ratio per episode, reported as accuracy-cost curves. Qwen3-8B k=0 is run first; if 8B's k=0 to k=3 gain is below the floor the reader arm is reported as uninformative rather than as a null crossover. Pre-registration after the positive control.

### proposal: many_shot_averages_detours
Title: Reading the Whole Bank Averages Out Detours: Many-Shot Context Is Robust to Per-Item Noise Where Top-k Retrieval Commits to It
Short Hypothesis: When the bank holds the agent's own successful-but-detoured trajectories (self pool) instead of expert trajectories, top-k retrieval passes the detours of the k items it commits to into the episode (more steps, more step-limit failures, lower success), while the whole-bank route is insensitive to the detour rate because the shared procedure is the consensus across many noisy items; the gap between routes grows with the bank's detour rate and with item count, and closes when detours are pruned from the items.

Experiments:
- Pools and banks. E: expert pool (1,465). S: self pool (1,892 successes). Detour measure per item = steps beyond the expert solution length for the same game; distribution reported. M: 50/50 mix by type. P: pruned S, removing visits to receptacles that did not yield the target object and repeated identical actions, then replaying the pruned action list in the same game and keeping only replays that still succeed (pruned items are therefore valid successful trajectories). A: S items from the top tercile of detour steps within each type. Item tokens measured (E about 140; S expected about 2x).
- Routes. RET: goal-sentence top-3 from each bank (same retriever as Measurement A), uncached; retrieved item lengths and detour steps logged per episode. WB: whole bank as a type-agnostic cached static prefix at 6, 24 and 48 items (48 S items must fit 16k with game history; otherwise 40 under a fixed type-balanced subset rule, stated before the run). Token-matched comparison WB E-48 vs WB S-24 also reported.
- Arms at Qwen3-32B: RET x {S, M, P, A} (RET E is Measurement A); WB x {E6, E24, E48, S6, S24, S48, M48, P48}. About 12 arms, roughly 8 h on two GPUs.
- Outcomes: success (primary), steps per episode and step-limit failures (secondary, paired). Imitation signature: for RET arms, the per-game paired difference in episode steps between S and E injections regressed on the injected items' detour steps; for WB arms, the same regression on the detour steps of the most similar item in the prefix (by the retriever's score) and on the bank-mean detour steps, to tell most-similar copying from consensus.
- Reader: Qwen3-8B on RET E, RET S, WB48 E, WB48 S as an exploratory replication of the 2x2 (4 arms).
- Cost: prefill tokens, GPU-seconds per episode under prefix caching; detours lengthen episodes and multiply decode steps, so cost per success is reported for both routes.
- Order: positive control first (RET A vs RET E); pre-registration; then the 2x2 (RET/WB x E/S at 48); then the S ladder, M and P; then Qwen3-8B.

Baselines and Ablations:
- k=0 and the Measurement C static arms (fixed type-conditioned exemplars, wrong-type placebo, procedure paragraph, six-procedure prompt); every retrieval number is reported as retrieval minus the best static arm at matched tokens.
- RET E (Measurement A) is the clean-item reference; RET with random fixed selection of three S items per game separates the retriever from the detour content.
- Pruned bank P is the repair ablation; amplified bank A is the positive control for imitation; mix M gives the intermediate detour rate.
- WB E ladder (6/24/48) is the no-noise reference for the item-count dose-response on S.
- Token-matched WB E-48 vs WB S-24 controls for the longer S items.

Falsifiable Predictions:
- P1 (retrieval inherits detours): RET S minus RET E is at or below -8 net and RET S episodes are longer by at least 2 steps on the paired median. Falsified if RET S is within +/-8 of RET E with no step increase; arm: RET S vs RET E.
- P2 (route x noise interaction, headline): [WB48 S - WB48 E] - [RET S - RET E] is at least +9 net. Falsified if both routes lose the same amount within 8 net, or if WB48 S loses more than RET S (the most-similar-item copying outcome predicted by arxiv:2405.00200); arms: the four cells WB48 E, WB48 S, RET E, RET S.
- P3 (dose-response in item count on noisy items): WB S rises from 6 to 48 items by at least 9 net while WB E is flat within +/-8 over the same ladder. Falsified if WB6 S is within 8 net of WB48 S or above it; arms: WB S6, S24, S48 vs WB E6, E24, E48.
- P4 (pruning repairs retrieval): RET P is within +/-8 of RET E and at least 9 net above RET S. Falsified if RET P is still at least 8 net below RET E, which would locate the deficit in something other than detours (phrasing, length); arm: RET P.
- P5 (positive control): RET A is at least 8 net below RET S and its episodes are the longest. Falsified if RET A is within +/-8 of RET E, in which case imitation has no leverage and the design stops; arm: RET A.
- P6 (mechanism): in RET arms episode steps rise with the injected items' detour steps (paired slope above zero at the 95% paired-bootstrap level), while in WB48 S episode steps do not rise with the most-similar item's detour steps. Falsified if WB48 S episodes track the most-similar item's detours as strongly as RET episodes track theirs; arm: WB48 S with per-item similarity and detour steps logged.
- P7 (mix): WB48 M is within +/-8 of WB48 E while RET M sits between RET E and RET S. Falsified if WB48 M is at least 8 net below WB48 E; arms: WB48 M, RET M.

Measurement and Noise Control:
Paired cells on 274 games x 2 seeds with identical seeds across arms; +/-8 net floor; confirmatory effects must exceed the floor and be at least one third of the Gate-0 retrieval gain (+27 net at k=3). Steps and step-limit failures are paired per game and summarised by median differences with paired-bootstrap intervals. Per-type results pooled over the three procedure-heavy types (clean, heat, cool) and declared exploratory. Positive control before any null: RET A must be at least 8 net below RET E. Success ceiling (0.87 at k=7) limits headroom for success, so steps are the pre-registered secondary outcome on which the imitation claim can still be tested. Item lengths and retrieved-item lengths are logged to rule out a retriever length bias explaining RET S. Cost measured as GPU-seconds per episode and prefill tokens under prefix caching. Pre-registration after the positive control.

### proposal: near_duplicate_needle_crossover
Title: Bigger Banks Help Retrieval Only Through Near-Duplicates the Reader Cannot Find in Context: Bank Size x Near-Duplicate Rate on WebShop and ALFWorld
Short Hypothesis: The growth of top-k retrieval's advantage over the whole-bank-in-context route with bank size is a near-duplicate effect: with instance-level near-duplicates removed from the bank, retrieval and whole-bank are within the noise floor at every bank size on both environments; with near-duplicates planted at a controlled rate, retrieval's gain rises with the rate on WebShop (one procedure, instance-specific bindings) and the whole-bank route recovers only part of it, the recovered fraction falling as the haystack grows from 12 to 40 items; on ALFWorld (procedure-bound) the same manipulation moves neither route.

Experiments:
- WebShop setup (public data, one day). Reader Qwen3-32B. Evaluation on the standard 500 test instructions x 2 seeds; k=0 and a k=0 seed-replicate first to set the paired floor.
- Bank material: successes (reward 1.0) of Qwen3-32B on at least 2,000 train instructions (expected 600-800 items) plus the public human demonstrations; state abstraction in the Synapse style (search-result pages reduced to item id, title and price lines; product pages to title, price, options and the buy action), applied identically to retrieved and whole-bank items; item length measured (target about 300 tokens).
- Near-duplicate definition for a test instruction: a bank trajectory whose instruction targets the same product id, or the same category with at least two shared attribute phrases; the near-duplicate gain is also reported as a function of the number of shared attributes. Cluster design: the 500 test instructions are partitioned by category into about 42 clusters of about 12; each cluster gets one static bank per (size, rate) cell, cached across the cluster's episodes. At size 40 and rate 1 the bank holds one near-duplicate per cluster instruction plus 28 non-duplicate items; rate 0.5 holds six; rate 0 holds 40 non-duplicates. At size 12 and rate 1 the bank is the 12 near-duplicates (each instruction's needle among 11 same-category siblings); rate 0 holds 12 non-duplicates. Non-duplicate items are drawn from other categories.
- Routes: WB-12, WB-40 (cluster bank as a cached static prefix); RET-2 (top-2 from the same cluster bank by BM25 plus embedding over instruction text, uncached; near-duplicate hit rate in the top-2 logged); static arms: fixed two random non-duplicate exemplars for all clusters (cached), one compiled procedure paragraph (search, pick, options, buy; cached), k=0.
- WebShop arms: WB x {12,40} x r{0,0.5,1} (6), RET x {12,40} x r{0,0.5,1} (6), fixed-2, compiled, k=0 x2 (4): 16 arms x 1,000 episodes, about 1 h each on two GPUs; bank generation about 2 h.
- ALFWorld: near-duplicate = same-scene, same-type expert trajectory (bindings: object location in that scene); applies to the 140 valid_seen games, with the 134 valid_unseen games as the no-near-duplicate reference within the same arm. Banks per scene cluster at 48 items: r=0 (same-scene items excluded) vs r=1 (one same-scene same-type item per game guaranteed). Routes RET k=3 and WB-48: 4 arms, about 3 h.
- Outcomes: success (WebShop reward = 1; ALFWorld success) primary; WebShop mean reward secondary; near-duplicate hit rate in RET top-2 as mediator; in-context lookup measured by the copy rate (agent's search query or product id matching the near-duplicate's) in WB arms.
- Reader (exploratory, G16): Qwen3-8B on WebShop k=0, RET r=1 size 40, WB-40 r=1, to see whether in-context lookup of the needle depends on the reader.
- Cost: prefill tokens, cache hit ratio, GPU-seconds per episode; accuracy-cost frontier across static, retrieval and whole-bank arms per rate.
- Order: install; k=0 and floor; bank build; positive control (RET r=1 vs r=0 at size 40); pre-registration; remaining WebShop arms; ALFWorld arms; 8B.

Baselines and Ablations:
- Static arms as the baseline on WebShop: fixed two-exemplar prompt (cached), compiled procedure paragraph (cached), k=0; every retrieval number is reported as retrieval minus the best static arm at matched tokens.
- Whole-bank at two haystack sizes (12, 40) is the matched-budget no-retriever arm; the rate-0 banks are the random/fixed-selection control at the whole-context budget.
- Rate ladder 0/0.5/1 on both routes; shared-attribute count as a graded near-duplicate strength ablation.
- ALFWorld same-scene manipulation as the procedure-bound contrast, with valid_unseen games as the within-arm no-near-duplicate reference.
- RET with random fixed selection of two items from the cluster bank (rate 1) separates the retriever's hit rate from exemplar presence.

Falsifiable Predictions:
- P1 (positive control, near-duplicate leakage exists): on WebShop at size 40, RET r=1 minus RET r=0 exceeds the measured floor and at least 10 points of success. Falsified if the difference is within the floor, in which case the manipulation has no leverage and the design stops; arm: RET r=1 vs RET r=0 at size 40.
- P2 (no residual without near-duplicates): on WebShop at r=0, RET minus WB-40 and RET minus fixed-2 are within the floor. Falsified if RET exceeds WB-40 or fixed-2 by more than the floor at r=0 (category-level transfer of search wording would do this); arms: RET r=0, WB-40 r=0, fixed-2.
- P3 (headline: the reader cannot find the needle): at r=1 WB-40 recovers less than half of RET's near-duplicate gain (WB-40 r=1 minus WB-40 r=0, as a fraction of RET r=1 minus RET r=0, with a paired-bootstrap upper bound below 0.5), and WB-12 recovers more than WB-40. Falsified if WB-40's recovery is within the floor of RET's gain (the reader locates the needle, the arxiv:2405.00200 outcome on trajectories), or if WB-12 and WB-40 recover the same fraction; arms: WB-40 r=1, WB-12 r=1.
- P4 (mediation): RET's gain at r=0.5 is proportional to the top-2 near-duplicate hit rate, and the random-fixed-selection cell at r=1 gains only in proportion to its chance hit rate. Falsified if RET gains at r=0.5 exceed the hit-rate-scaled prediction by more than the floor, or if random fixed selection matches RET at r=1; arms: RET r=0.5, random-fixed r=1.
- P5 (procedure-bound contrast): on ALFWorld, RET r=1 minus RET r=0 and WB-48 r=1 minus WB-48 r=0 are within +/-8 net on valid_seen. Falsified if RET r=1 exceeds RET r=0 by at least 9 net, meaning scene bindings matter on ALFWorld after all; arm: ALFWorld RET r=1 on valid_seen.
- P6 (static arm ordering flips with rate): on WebShop the fixed-2 arm is within the floor of RET at r=0 and at least the floor below RET at r=1. Falsified if fixed-2 is below RET by more than the floor at r=0; arms: fixed-2 vs RET r=0 and r=1.

Measurement and Noise Control:
WebShop: 500 test instructions x 2 seeds, identical seeds and instruction order across arms, all contrasts paired per instruction; the floor is set before pre-registration from the k=0 seed replicate (expected about +/-4-5 points of success) and no claim below it is made. Recovery fractions carry paired-bootstrap intervals over instructions. Margins are tied to the measured Gate-0 gain on WebShop (RET r=1 minus k=0, measured first); confirmatory effects must exceed the floor and be at least one third of that gain. ALFWorld: 274 games x 2 seeds, +/-8 net floor, contrasts on the 140 valid_seen games paired with the same games at r=0 (floor for 140 x 2 is wider, about +/-11 net, and is used for P5). Near-duplicate hit rate and copy rate are logged per episode as mediators, secondary to success. Cost measured as GPU-seconds per episode and prefill tokens under prefix caching; the whole-bank prefix is cached per cluster, so cache hit ratio is reported per cluster. Pre-registration after the positive control.
