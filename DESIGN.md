# DESIGN v1 — Proposal ③ v5.2 (frozen text: `reference/proposal_v5.2.md`). This file is the single authority.
# Written 2026-09-04 from v5.2 plus the data-forced amendments D1–D6 (prereg/AMENDMENTS.md). Hashed into
# prereg/FREEZE.sha256 only after the PI's freeze-blocking literature obligation (v5.2 Preprint Collision Check, item 1).

## 0. Claims (v5.2 Short Hypothesis, made operational)
C1 ABSORPTION (confirmatory, the only bar): in ALFWorld, at a fixed instruction and on the same held-out games, at
   least half of a procedural memory bank's task-type-specific value is already held by an instruction a reflective
   optimizer wrote from the same training episodes. Endpoint: absorbed share **A = 1 − Inner(I_own)/Inner(I_oth)** with
   **Inner(I) = acc(I×B_own) − acc(I×B_oth)** (game-paired), **co-primary A0 = 1 − Inner(I_own)/Inner(I0\*)**.
   Bar: both A and A0 ≥ 0.5, each with one-sided 90% cluster-bootstrap lower bound ≥ 0.2 and point estimate above the
   95th percentile of its pooled null (intersection–union; no multiplicity correction). A_all (denominator Inner(I_all))
   reported with CI, not gating. Disagreement between A and A0, or a tripped inflation check / Rule R ⇒ A0 is the
   reported number, A the repair-inclusive upper bound, the gap the size of the mis-specification channel.
C2 NOT HEADROOM / NOT STALENESS / NOT DISTRACTOR-ROBUSTNESS / NOT SAMPLING: pre-registered rules M, F, C, R, the
   headroom floor A_h, the Ladder-T bracket, the on-policy bank, X_dist, M_shuf and best-of-w (§7–§8).
C3 EPISODE VS TYPE (secondary, bank side thresholded, instruction side reported): row 17 Inner(B′_own) − Inner(B_own)
   fails a ±3pt TOST ⇒ the bank carries episode-specific content; A_epi/A_type from row 4 reported with CIs only.
C4 PRACTITIONER: g(I_all,B_all) and I_all×C_all − I_all×B_all each pass a ±3pt TOST (predictions 6, 8 of v5.2).
Scope: "type-specific value" means **task-type-and-room-specific procedural and layout knowledge** (D2) — the
partition also partitions rooms, and every claim is worded accordingly.

## 1. Infrastructure (all local; no API key; network- and data-forced amendments in prereg/AMENDMENTS.md)
Agent: **Qwen3.5-27B** bf16 (screened against Qwen3-32B, §3.0), thinking disabled via chat-template kwarg, vLLM 0.13.0
TP=1, **one replica per A100** (ports 8000, 8001; served-model-name `agent`), temperature 0.7, seed schedule
{11, 23, 37} (per-call seed = seed·100003 + call index), max_tokens 160 per action call. Reflector / distiller /
compiler: **Qwen3-32B** (served-model-name `annotator`, port 8002, on GPU 1 during artifact phases, then unloaded);
swapped to Qwen3.5-27B iff the screened agent is Qwen3-32B (no model reflects on its own traces). No LLM judge for any
quantity: ALFWorld returns `won`. Serve flags (lab-validated, logged in every run): `-m vllm.entrypoints.openai.api_server
--model <path> --served-model-name <name> --tensor-parallel-size 1 --max-model-len 16384 --gpu-memory-utilization 0.92
--enforce-eager --disable-custom-all-reduce --port <p>`. Envs: `/home/work/neuro/vllm-env` (serving),
`/home/work/neuro/alfworld-env` (alfworld 0.4.2 + textworld 1.7.0 + openai + sentence-transformers + scipy; the agent
process). Retriever: `paraphrase-multilingual-MiniLM-L12-v2` (local, CPU, held fixed). Weights: `/home/work/neuro/models/`.
Runs under tmux; JSONL episode logs, resumable, append-only. GPU keep-alive (`gpu_burst`) stopped for the duration.

## 2. Data and splits (D1, D2 — the two data-forced amendments)
Source: ALFWorld text games regenerated from the public `awawa-agi/alfworld-raw` rows (HF datasets-server; GitHub
release assets are blocked on this network) into `/home/work/neuro/alfworld-data/json_2.1.1/{train,valid_seen,
valid_unseen}`; raw-row SHA256 in `alfworld-data/raw/SHA256SUMS`; `pddl_params` stubs reconstructed from task-directory
names (`tools/alfworld/make_stubs.py`); public data only, no NACC/patient data (lab DUA). See data/PROVENANCE.md.
**D1 Unit of allocation and clustering = the task.** `train` holds 3,553 trials of **1,465 unique tasks** (task = type ×
object × receptacle × scene; 172 tasks have 1 trial, 498 have 2, 795 have 3). Trials of one task are near-duplicate
games (same scene, same goal; differing object instance and placement). All trials of a task go to one split; every
statistic clusters by task (§7). Exact per-set counts: **T_A = {pick_and_place 322, pick_two 354, look_in_light 123} =
799 tasks / 1,911 trials; T_B = {clean 268, cool 212, heat 186} = 666 tasks / 1,642 trials.** T_B binds.
**D2 Rooms.** cool and heat exist only in kitchens; clean in kitchens (199 tasks) and bathrooms (69); T_A spans kitchen
86 / living 200 / bedroom 295 / bathroom 218 tasks. The off-type bank is therefore largely an other-room bank. Claims
are worded "type-and-room-specific"; every square cell is reported per room; a kitchen-only sub-analysis of Inner and A
(the only room both sets share at scale) is pre-registered as secondary and descriptive.
**Partition rule (zero-episode, computed before any episode; v5.2 §Experiments):** over the 7 of 10 3–3 type splits that
leave both sets ≥ 1,500 trials, compute for a seeded 200-trial sample per set the mean share of the top-5 MiniLM
retrievals (query = goal text + first observation; items = every other train trial's goal text + stored walkthrough,
i.e. proxy items needing no LLM call) that come from the other set, divided by the other set's share of the pool
(random-retrieval expectation); choose the split minimizing this normalized cross-set share. Pre-named expected
winner: T_A/T_B above. The number is committed in prereg/partition.json before any episode runs.
**Splits (per set, trials; whole tasks; seeded script code/make_splits.py, seed 20260904; IDs in prereg/splits.json):**
P_train 300 · P′_train 200 · S_screen 150 · S_dev2 250 · S_test 600 · reserve (T_B ≈142, T_A ≈411). Tasks are shuffled
within type and assigned type-stratified, greedily to the trial targets (tolerance ±3 trials, achieved counts logged).
Pooled: P_train 600, P′_train 400, S_screen 300, S_dev2 500, **S_test 1,200**, balanced reserve 142/set = 284 pooled
(spent only in v5.2's priority order: S_test shortfall → the single G3 re-measurement → row-10 null remediation; at most
one of the last two). S_test is ordered by seeded task shuffle; **nested subsets** S_test[k] for k ∈ {800, 600, 500,
400, 300} pooled are the first k/2 trials per set cut at task boundaries (≤2 trials off; realized sizes logged).
`valid_seen` (140 trials) and `valid_unseen` (134) are Tier-1 only.

## 3. Artifacts (built once, frozen, SHA256 in prereg/artifacts.sha256; all prompts verbatim in prereg/prompts.json)
3.0 SCREENING (S_screen only): for each agent ∈ {Qwen3.5-27B, Qwen3-32B}: bank-source pool = 250 S_screen episodes
    under I0^bare (seed 11); distil both formats (ExpeL-style INSIGHT/PROCEDURE/OUTCOME; ReasoningBank-style strategy
    items from env-verified successes and failures); measure g(I0^bare, B) on the remaining S_screen games (paired vs M0)
    for the 4 pairings; the largest gain that clears 5pt proceeds; all four published; losers reported co-equally.
3.1 I0^bare — the scaffold in prereg/instructions.json (`I0_bare`: system scaffold + generic slot text G0, no
    type-specific procedure), hashed before anything runs. Memory slot wording fixed there too.
3.2 I0^demo — I0^bare + two handcoded-expert trajectories from two P_train games of the test game's own type set (two
    different types, chosen by seed 11, ≤400 tokens each, one fixed pair per set). I0\* := I0^demo if G1 passes under it,
    else I0^bare (rule fixed before S_dev2 runs).
3.3 Banks. B_A, B_B: distilled by the annotator from **all 300 P_train episodes of the set** run under I0^bare (seed 11),
    in the screened format; dedup by exact match; item = goal + INSIGHT + PROCEDURE + OUTCOME (≈60–120 tokens). Retrieval
    key = goal text + first observation; k ∈ {3, 5, 7} fixed on S_dev2 by a 350-episode tuning run (§6). B_all = B_A ∪ B_B.
    B_A^on, B_B^on: same distillation from P_train episodes generated under I(T, seed 1). B′_A, B′_B: from the 200 P′_train
    episodes under I0^bare, k- and token-matched at read time. B^hi/B^lo: B_own split at the median max-ROUGE-L/embedding
    overlap with I(T, seed 2), run at I(T, seed 1). B_oth+own25/50: the off-type bank with 25%/50% of items replaced by
    on-type items (seeded). X_dist: E1-provenance procedural items from `reference/shortcutting_v4/bank/bank_A.jsonl`
    rewritten by the annotator into the ALFWorld item format (goal → question stem), truncated to the median B_own
    injection length. M_shuf: k random items from the own-type bank (seeded per game), retrieval bypassed. C_all, C_own:
    static blocks compiled by the annotator hierarchically (chunks of 40 items → notes → final block at the median
    injection length), compiler prompt fixed on dev and reported verbatim. **"Same episodes" identity (v5.2 row 89):**
    the sorted P_train game-id list of set T is SHA256-hashed; the hash is stored in B_T and in I(T, s) and checked at load.
3.4 Optimizer (GEPA-lite, local reflector; code/gepa_lite.py). Budget 350 rollouts on P_train(T) (300 games), spent as
    **one full sweep + 50** in a seeded minibatch order (minibatches of 10): iteration i runs the incumbent on b_i,
    the reflector proposes a child from ≤4 failed traces + 1 success trace of b_i, the child runs on b_{i+1}; the child
    replaces the incumbent iff its b_{i+1} success rate ≥ the incumbent's mean over its last two minibatches (ties
    accepted); the seed I0\* is run on b_1, b_2 before the first proposal. Final I(T, s) = the candidate with the highest
    mean success over ≥30 evaluated games (tie → most recent). Coverage of P_train is 100% by construction (the sweep),
    which is what the identity in 3.3 requires; the training curve (per-minibatch success of every candidate) is
    published. Seeds s ∈ {1, 2} change the minibatch order and the reflector's sampling seed. I_all(s): the same on
    P_train(A) ∪ P_train(B) (600 games, 350 rollouts, coverage ≈58%, reported). I′(T, r) (Ladder T): the same on
    P′_train(T) (200 games) to 500 rollouts, incumbent snapshotted at r ∈ {50, 100, 200, 350, 500}; extended once to
    750 if G4 needs it. J(T, s) (MIPROv2-lite): candidate = (instruction from the same reflection loop, 2 bootstrapped
    demonstrations = successful traces of the incumbent's own rollouts, seeded), token-matched to the memory injection,
    same sweep budget. I2(T) (Tier 1): as I(T) with B_own retrieved into context during rollouts. I_type (Tier 1):
    hand-written from the three type names + canonical skeleton, in prereg/instructions.json, hashed before S_dev2.

## 4. Arms — SINGLE AUTHORITATIVE TABLE (S_test; "own/oth" resolved per game's type set; n = pooled trials)
Instruction arms: I0s (=I0\*), IOWN_s/IOTH_s (=I(T)/I(T′), s∈{1,2}), IL_s (=I_all), ILAD_lo/ILAD_hi (=I′(T, r_lo/r_hi)),
JOWN_s. Memory arms: M0, BOWN, BOTH, BALL, BOWNon, BOWNp (=B′_own), BOWNhi, BOWNlo, PLANT25, PLANT50, XDIST, MSHUF,
CALL. Extras: w2 (best-of-2 action sampling), L45 (step limit 45).
| # | Cell (instruction × memory) | n | opt seeds | dec seed | episodes | calls | Purpose |
|---|---|---|---|---|---|---|---|
| 1 | I0s × {M0 @11, M0 @23, BOWN, BOTH} | 1200 | — | 11 (M0 also 23) | 4,800 | 81,600 | baseline; treatment-free floor; Inner(I0\*) = neutral denominator |
| 2 | {IOWN, IOTH}_{1,2} × {BOWN, BOTH} | 1200 | 1,2 | 11 | 9,600 | 163,200 | **the square; A** |
| 3 | {IOWN, IOTH}_{1,2} × M0 | 1200 | 1,2 | 11 | 4,800 | 81,600 | ℓ_own, ℓ_oth; provenance main effect; help/off decomposition |
| 4 | {ILAD_lo, ILAD_hi} × {M0, BOWN, BOTH} | 500 | 1 | 11 | 3,000 | 51,000 | Ladder T; A_epi/A_type (reported) |
| 5 | IL_{1,2} × {M0, BALL} | 800 | 1,2 | 11 | 3,200 | 54,400 | practitioner gain |
| 6 | IOWN_{1,2} × BOWNon | 800 | 1,2 | 11 | 1,600 | 27,200 | on-policy bank (staleness) |
| 7 | {IOWN_1, IOTH_1} × {BOWNhi, BOWNlo} | 400 | 1 | 11 | 1,600 | 27,200 | item-level dose-response (Rule C) |
| 8 | {I0s, IOWN_1, IOTH_1} × XDIST | 500 | 1 | 11 | 1,500 | 25,500 | distractor-robustness (out-of-domain) |
| 9 | I0s × {PLANT25, PLANT50} | 500 | — | 11 | 1,000 | 17,000 | graded planted control |
| 10 | NULL: IOWN_1 × {BOWN, BOTH} | 600 | 1 | **37** | 1,200 | 20,400 | treatment-free replicate of the ratio |
| 11 | IL_{1,2} × CALL | 800 | 1,2 | 11 | 1,600 | 27,200 | compile once |
| 12 | JOWN_{1,2} × M0 | 800 | 1,2 | 11 | 1,600 | 27,200 | prompt-container ceiling |
| 13 | — (I2, Tier 1) | | | | | | retired number |
| 14 | I0s(w2) × {M0, BOWN, BOTH} @300; IOWN_1(w2) × M0 @400 | 300/400 | 1 | 11 | 1,300 | 44,200 | compute-matched sampling (34 calls/ep) |
| 15 | — (step control, Tier 1) | | | | | | retired number |
| 16 | IL_{1,2} × {BOWN, BOTH} | 800 | 1,2 | 11 | 3,200 | 54,400 | neutral deployed denominator; A_all |
| 17 | {IOWN_1, IOTH_1} × BOWNp | 800 | 1 | 11 | 1,600 | 27,200 | episode-disjoint bank (C3) |
| 18 | {IOWN_1, IOTH_1} × MSHUF | 500 | 1 | 11 | 1,000 | 17,000 | within-domain distractor (Rule M) |
|   | **Tier-0 test grid** | | | | **42,600** | **746,300** | |
Artifacts: bank-gen 600 + on-policy bank-gen 600 + B′ gen 400 + GEPA I_own/I_oth 1,400 + Ladder T 1,000 + I_all 700 +
J 1,400 = 6,100 episodes (103,700 calls) + ≈3,500 annotator calls. Screening 2,300 episodes. Dev (S_dev2): I0^bare and
I0^demo × {M0, BOWN, BOTH} 3,000; {IOWN, IOTH}_{1,2} × M0 1,000 (n=250 per direction... realized 500 pooled × 2 seeds);
Ladder titration 5 × 250 (M0) 1,250; k-tuning 350; smoke 150 = 5,750. **Tier 0 total 56,750 episodes ≈ 990,000 calls
≈ 60–84 h at 11,800–16,600 calls/h.** Calls/episode = 17 planning (0.75·12 + 0.25·30 + 0.5), re-measured at G5.
Tier 1 (in this buy-back order, within measured throughput): I2_own × {BOWN, M0} (+ its optimizer run) → step control
IOWN_1(L45) × M0 → {COWN, COTH} × {BOWN, BOTH} → I_type × {M0, BOWN, BOTH} → M_all/R_raw ladder (R_raw also at IOWN) →
official valid_seen/valid_unseen with {I0s, IL_1} × {M0, BALL} → IOWN × COWN → D_opt → B^re → B_touched → oracle →
medgemma-27b-it rows 2–3 → E1 replication (direct-difference bound only). Tier 2: gpt-oss-120b row 2 → losing pairing
row 1 → second-best partition row 2. Contingency cuts if G5 throughput < 11,000 calls/h, in this order and no other:
row 18 → row 17 → row 14 to the IOWN(w2)×M0 point → PLANT25 → row 12 to one seed → row 11 to one seed → rows 2–3 to
n = 1,000 with republished MDE → row 5 to one seed. **Rows 1, 2, 3, 4, 6, 7, 8, 10, 16 are never cut.** Unrun = unrun.

## 5. Scaffold, prompts, enforcement (held fixed in every cell)
ReAct over the ALFWorld text interface: each turn the agent sees the goal, the history of (action, observation), the
latest observation and the **admissible-action list**; it replies `Thought: …` (optional, one line) then `Action: <one
admissible action verbatim>`. Parsing: the `Action:` line matched (case/whitespace-normalized) against the admissible
list; a non-admissible or unparseable reply gets **one re-prompt** ("not admissible; choose one from the list") — an
extra call, not a step — and a second failure is a no-op step charged to the budget (observation "Nothing happens.").
**Step limit L0 = 30 env steps** everywhere except the L45 extra. Episode ends at `won` or at the step limit. Logged per
episode: success, timeout, invalid-action count, steps, calls, tokens, injected item ids and token count, instruction
hash + provenance tag + rollout budget, bank id + provenance tag, seed, full action trace. Instruction slot wording:
`\n\nIMPORTANT INSTRUCTION: {instruction}`; memory slot: `\n\nRetrieved experience from past tasks (may or may not
help):\n{items}` — both fixed in prereg/instructions.json. Best-of-w (w2): one request with n=2 at each step; if the
two agree take it; else the first admissible one; counted as 2 calls. Every accuracy delta is decomposed into
success / timeout / invalid components; a cell whose delta is >50% accounted for by a timeout-rate change is flagged.

## 6. Gates (numeric; S_dev2 n = 500 pooled unless stated; point estimate + lower 80% task-cluster bootstrap CI;
##    any fail → the pre-registered branch, logged in prereg/GATES_LOG.md; never a silent continuation)
G-P0 smoke: 20 episodes each of I0^bare × M0 and × B_own parse-clean, 0 engine errors.
G-P1 throughput: ≥ 400 episodes/h per replica at I0^bare × M0 on S_dev2[:100] (≥ 11,000 calls/h aggregate is G5).
G0 dynamic range: acc(I0^bare × M0) ∈ [20%, 80%]; timeout rate ∈ [20%, 60%] (else L0 re-set once on dev, logged).
K  bank read-depth: k ∈ {3, 5, 7} chosen by the largest paired gain of I0^bare × B_own over M0 on S_dev2 (≈117 games per
   k, 350 episodes total); fixed before G1.
G1 (under I0^bare and I0^demo): g(I0, B_own) ≥ 5pt, lower CI ≥ 2pt, ≥ 20 fixes. I0\* rule per 3.2; fails under both
   for every screened pairing → memory-null branch.
G2 acc(I(T)×M0) − acc(I0\*×M0) ≥ 3pt for both seeds and both sets (on the set's own S_dev2 games).
G3 Inner(I0\*) ≥ 9pt with lower CI ≥ 5pt; [6, 9) with lower CI ≥ 3pt → the single reserve re-measurement (284 pooled).
G3b lower 80% CI of acc(I_own×M0) − acc(I_oth×M0) > 0 (direction only). Routing: acc(I_oth×M0) more than 3pt below
   acc(I0\*×M0) on own-type games → I_oth logged mis-specified; square still runs; A0 sole confirmatory number.
G4 Ladder T brackets ℓ_own = acc(I_own×M0) on dev (titration at 5 budgets, M0 only); else extend to 750 once; else the
   correction is declared an extrapolation before S_test and the reading falls back to A_h with the best-of-w bracket.
G5 retriever relevance ≥ 60% (100-episode audit: retrieved item's type set = game's set counts as relevant, plus a
   20-item manual check); stored-item truthfulness ≥ 70% (100 items: PROCEDURE consistent with the source trace);
   aggregate throughput ≥ 11,000 calls/h; timeout rate → calls/episode and the compute plan republished; **DEFF and the
   within-task ICC (D1) measured on dev and the MDE table republished** before any S_test cell.
G6 (S_test, before numerator cells are unblinded): Inner(I_oth) ≥ 5pt and Inner(I0\*) ≥ 5pt; neutrality: if
   Inner(I_oth) − Inner(I0\*) > max(2pt, 1.5 × its bootstrap SE), or Rule R (R_repair − p0 ≥ 0.15, 90% LB > 0) → A not
   interpretable as absorption; A0 reported.
Order of measurement: G-P0 → G-P1 → G0 → K → G1 → (optimizers) → G2 → G3 → G3b → G4 → G5 → S_test rows 1–3 → G6 → rest.

## 7. Statistics (single source of truth: code/stats.py)
UNIT: game-paired outcomes; **clusters = tasks** (D1); optimizer seeds = fixed strata (v5.2 Measurement (b)).
SUPERIORITY: exact McNemar on fix/break tables (reported) with the task-cluster bootstrap CI (10k) as the decision
statistic. EQUIVALENCE: TOST = 90% task-cluster bootstrap CI of the paired difference inside ±3pt (predictions 4, 6, 8).
RATIOS: A, A0, A_all, A_epi, A_type by task-cluster bootstrap (10k resamples of tasks; numerator and denominator
recomputed per resample; seeds pooled as strata), one-sided 90% lower bound; delta-method CI reported alongside.
Direction-pooled numerator/denominator; per-direction and per-seed values always reported; direction × set interaction
fitted (mixed-effects logistic: game outcome ~ cell, random intercept per task). HOLM FAMILIES: F-A {A, A0: intersection–
union, no correction}; F-B {Inner(I0\*), PLANT25, PLANT50}; F-C {on-policy, practitioner, compile-once}; F-D {Ladder T,
compute controls, J, dose-response, distractor contrasts, every Tier-1 control}. NULL FLOOR: (1) row 1 M0 @23 vs @11;
(2) row 10 forms A from Inner at one instruction across seeds 11/37 (true value 0); (3) ladder-level null between two
adjacent Ladder-T levels (true value A_h). No effect is claimed unless the estimate exceeds the 95th percentile of its
pooled null; if the row-10 null's 95th percentile > 0.25, the threshold is raised or n raised from the reserve —
decided and logged before unblinding. MDE (planning, from v5.2): SE(Inner) ≈ 1.41pt at n = 1,200 (discordance 0.20,
0.8pt/run optimizer component); SE(A) ≈ 0.14 / 0.17 / 0.23 at Inner(I_oth) = 10 / 8 / 6pt; **all inflated by
√DEFF, DEFF = 1 + (m̄ − 1)·ICC with m̄ ≈ 2.4 trials/task, measured on S_dev2 (G5) and republished before S_test**.
Sub-MDE differences are inconclusive, never null. Rules M, F, C, R exactly as v5.2 (§Experiments, "mechanism rules",
"three denominators"). Timeout/step decomposition on every delta (§5).

## 8. Analyses (one script, analysis/make_tables.py, from runs/*.jsonl)
A1 primary A, A0, A_all with CIs, nulls, sensitivity table (correction ×0.5/0.75/1/1.25/1.5), A_h, per-direction,
per-seed, per-type, per-room, kitchen-only. A2 gates table. A3 Rules M/F/C/R with the row-3/7/8/18 decompositions.
A4 C3: row 17 TOST, row 4 A_epi/A_type. A5 practitioner: rows 5, 11, 16 TOSTs and gains. A6 controls: rows 6, 9, 12,
14. A7 content overlap (embedding + ROUGE-L, zero-episode) with the two nulls. A8 optimizer training curves, coverage,
between-seed spread. Partial completion: unrun arms are listed as unrun in every table.

## 9. Provenance, freeze, deviations
prereg/: splits.json (IDs, seed, hash), partition.json (criterion values for all 7 splits, chosen split), instructions.json
+ .sha256 (I0_bare, slot wordings, I_type), prompts.json (distill ExpeL/RB, reflect, compile, X_dist rewrite),
artifacts.sha256 (every bank, instruction, block, demo pair with its provenance tag and the P_train identity hash),
THRESHOLDS.md, AMENDMENTS.md (D1–D6), GATES_LOG.md, DEVIATIONS.md, FREEZE.sha256 (after the PI's obligation).
After the hash, any design edit is a DEVIATIONS.md entry. Dev-stage prompt edits (compiler, reflector wording) are
allowed before their dependent artifacts are built and are logged as amendments; test cells never re-run.
