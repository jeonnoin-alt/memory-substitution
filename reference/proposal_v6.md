# Proposal v6 — memory_or_instruction (author: Fable 5.1 directly; 2026-09-07)

Lineage: v2 6.97 (sonnet) / 6.02 (opus) → v4.2 6.40 → v4.3 6.05 → v4.4 5.83 → v5 5.25 → v5.1 5.57 → v5.2 5.12 → v5.3 4.83 (opus) → **v6 (this file)**. Judging uses only the 11 IDEA_FIELDS below.

## Decision log (rows 1–101 are in `reference/proposal_v5.3.md`; rows 102+ are v6)

| # | Objection (source) | Answer in v6 |
|---|---|---|
| 102 | **The endpoint measured the bank's type-discriminability, not its value; the title's claim was never thresholded (v5.3 3/3).** | The primary is now the bank's **residual value at the optimized instruction**, g(I_P) = acc(I_P×B) − acc(I_P×M0), tested for equivalence to zero at ±3pt. The ratio apparatus (A, A0, A_all), the three denominators, the inflation check, Rule R and the 14-row truth table are deleted. |
| 103 | **The off-type instruction I_oth was mis-specified for own-type games and inflated every ratio built on it (v5.1–v5.3, 3/3 each round).** | **The task-type partition is removed.** There is no I_oth. Provenance is manipulated as *same distribution, disjoint episodes*: an instruction I′ optimized on a task-disjoint pool P′ of the same six types, titrated to I_P's no-memory accuracy. This deletes G3, G3b, G6, the room-type confound (D2) and the ten-split partition criterion. |
| 104 | **k was tuned once under the hand-written scaffold and held fixed across instructions of very different lengths; the track's own prior result is that injection volume was the causal lever (4 judges, 2 rounds).** | **k is re-tuned per instruction on S_dev** (k ∈ {1,3,5,7}) and every g(I) is measured at that instruction's own k*(I). Reported: k*(I0*), k*(I_P), k*(I′). |
| 105 | **Powered where not novel, under-powered where novel: the episode-vs-type identification sat at n = 500, one seed, de-thresholded (v5.3 R1).** | The episode-disjoint instruction I′ is a **primary** arm at n = 1,800, two optimizer seeds, thresholded: g(I′) − g(I_P) ≥ 3pt with 90% lower bound > 0. |
| 106 | **No instruction-length control; A0 could be prompt mass (v5.3 R2).** | I0_pad: I0* padded with task-neutral prose to I_P's token count, run with M0 and B at n = 900. |
| 107 | **Rule M's 2/3 help/off bucket had no SE and selected between the headline and its negation (v5.3 R2).** | Deleted. The rival "the optimized instruction ignores injected text" is tested by two measured quantities, the item-following rate and the harm from token-matched random items, neither of which selects a title. |
| 108 | **ExpeL's own ablation was never read; "nobody reported the number" was false (v5.2–v5.3).** | Read 2026-09-07 (project page + arXiv HTML via web search): on ALFWorld ExpeL full 59%, retrieve-only 55%, insights-only 50%; on HotpotQA insights-only 36% vs retrieve-only 31%. Stated in the first paragraph of Related Work as the published redundancy result this proposal builds on. |
| 109 | **Clarity 5.0, feasibility 4.7: 20 rows, six titles, version scaffolding (v5.3 3/3).** | 9 Tier-0 rows, one endpoint pair, six predictions, no version history in the judged fields. Tier 0 ≈ 37,600 episodes ≈ 640k calls ≈ 39–54 h on two A100s (v5.3: 56,850 / 990k / 60–84 h). |
| 110 | **Refused, with reasons.** | Frontier reflector (no API key on this node; the bias lowers absorption and is conservative). Compile-once arm, joint-optimization arm J, coupling arm I2, the graded planted control and the E1 replication (all Tier 1: none bears on the two primaries). Third optimizer seed (bought back first if G5 clears with margin). |

---

## Name

memory_or_instruction

## Title

Is Your Agent's Memory Just an Un-Optimized Prompt? Residual Memory Value at an Episode-Disjoint, Level-Matched Optimized Instruction in ALFWorld

## Short Hypothesis

In ALFWorld, once a reflective prompt optimizer has written an instruction from the same training episodes that built a procedural memory bank, the bank's residual value at that instruction, measured at the bank's own re-tuned retrieval budget and on held-out games, is equivalent to zero within ±3 points; and the absorption is episode-specific rather than distribution-level: an instruction optimized to the same no-memory accuracy from disjoint episodes of the same task distribution leaves a residual memory value at least 3 points larger. The pair of numbers (residual at the same-episode instruction, residual at the disjoint-episode instruction at matched level) is the claim; everything else in the design is a named alternative explanation for that pair (headroom, prompt length, type-label knowledge, bank staleness, injected text being ignored) with an arm that tests it.

## Related Work

**(0) What is already published, stated first.** ExpeL (arXiv 2308.10144) stores training experience in two containers, a prepended natural-language insights block and retrieved trajectories, and its ablation on ALFWorld reports the full system at 59% against retrieve-only 55% and insights-only 50% (HotpotQA: insights-only 36%, retrieve-only 31%). Each container alone recovers 85–93% of the full system on ALFWorld: the redundancy between an instruction-shaped container and a retrieval container built from one training pool is therefore a published fact, and this proposal does not claim to discover it. EvoAgentBench (arXiv 2607.05202) puts ReasoningBank (+3.6) and GEPA (+1.2) on the same 528/267 trajectories on Qwen3.5-27B, so the qualitative claim that an optimizer given the same episodes gets roughly what a bank gets is also published. AutoManual (arXiv 2405.16247) and AutoGuide (arXiv 2403.08978) compile ALFWorld experience into instruction text and guidelines; Agent Workflow Memory (arXiv 2409.07429), Dynamic Cheatsheet (arXiv 2504.07952) and Agentic Context Engineering (arXiv 2510.04618) build a single accumulated context from episodes, the last benchmarking it against GEPA. MIPROv2 (arXiv 2406.11695) ablates instructions against bootstrapped demonstrations on one training set. **What none of them do, and what this proposal is:** (i) the instruction container is a *search-based reflective optimizer* seeded from the scaffold, not a fixed extraction routine; (ii) the residual is measured at the bank's *own* retrieval budget under each instruction, because this program measured injection volume, not content, to be the causal lever of memory harm; (iii) an *episode-disjoint, level-matched* instruction separates "absorbed these episodes" from "learned this distribution"; (iv) every contrast is game-paired, task-clustered, token-matched and null-replicated. The contribution is identification and a number with an interval on top of an accepted qualitative result.

**(1) Procedural memory in ALFWorld and its audits.** Memp (arXiv 2508.06433), ReasoningBank (arXiv 2509.25140), A-MEM (arXiv 2502.12110) and MemHarness (arXiv 2607.28272: raw injection 70.1% vs 76.4% no-memory RL) report 5–15 point memory effects in ALFWorld, which is why the confirmatory test lives there and not in the multi-hop QA setting where this program measured +0.6 to +2.4 points. Retrieval pollution and context competition (arXiv 2604.27003), excessive retrieval harming sequential decision-making (arXiv 2608.15008) and embedding retrievers treating procedures as bags of words (arXiv 2511.21730) are the reasons k is re-tuned per instruction and a random-item arm exists. MemDelta (arXiv 2606.29914) shows headline memory gains flip under one-variable changes; this design is one-variable-at-a-time by construction.

**(2) Reflective prompt optimizers.** GEPA (arXiv 2507.19457, ICLR 2026 oral) is the optimizer family; "Prompt Optimization Is a Coin Flip" (arXiv 2604.14585, 49% of runs below zero-shot) is why the optimizer's gain over the scaffold is a gate, not an assumption. Experience Distillation (arXiv 2607.21051) reports the fraction of an in-context gain retained when experience moves into weights (≥64.8%); the residual measured here is the same object with an optimized instruction as the second container.

**(3) Adjacent 2026 work found on the 2026-09-07 search, title-level only:** "A Control Architecture for Training-Free Memory Use" (arXiv 2604.18206, when memory should be exposed or retired) and "M\*: Every Task Deserves Its Own Memory Harness" (arXiv 2604.11811). Neither abstract was retrievable from this node; both are listed in the collision check as unread.

## Abstract

Agent memory papers measure a bank's value against a hand-written instruction. Prompt-optimizer papers measure an instruction's value with the memory slot empty. ExpeL's own ablation already shows the two containers are largely redundant on ALFWorld, and EvoAgentBench shows an optimizer given the same episodes gets roughly what a bank gets. What is not published is the residual: how much a procedural bank is still worth once a reflective optimizer has written an instruction from the *same* episodes, measured fairly. We measure it in ALFWorld on held-out training games with a local 27B agent. The bank B and the instruction I_P are built from the identical set of training episodes (the episode-id list is hashed into both artifacts). The residual g(I) = acc(I×B) − acc(I×M0) is measured game-paired at the bank's own re-tuned retrieval budget under each instruction. Two primaries: (E) g(I_P) is equivalent to zero within ±3 points; (D) an instruction I′ optimized from a task-disjoint pool of the same distribution and titrated to I_P's no-memory accuracy leaves a residual at least 3 points larger. E without D is reported as distribution-level absorption and the title changes to say so. Five named rivals each have an arm: headroom (I′ at matched level), prompt length (a padded scaffold), type-label knowledge (a hand-written type-only instruction), bank staleness (a bank re-distilled under I_P), and injected text being ignored (item-following rate and token-matched random items). All statistics are task-clustered bootstraps with pre-registered margins, a treatment-free null replicate and a stated MDE; unrun arms are unrun. No API key is used and no LLM judges anything: the environment returns success.

## Experiments

**HELD FIXED.** ReAct over ALFWorld's text interface; admissible-action list shown each turn; step limit L0 = 30 in every cell; one re-prompt on an unparseable action, then a no-op charged to the budget; episode ends at success or step limit; timeout rate, mean steps and invalid-action rate logged per cell and every accuracy delta decomposed into success / timeout / invalid components. Retrieval key = goal text + first observation; MiniLM dense retriever, held fixed. Decoding temperature 0.7, seed schedule {11, 23, 37}. Only the instruction slot and the memory-slot content vary.

**MODELS (no frontier API).** Agent: the screened one of Qwen3.5-27B and Qwen3-32B, thinking disabled, one vLLM replica per A100. Reflector, distiller and compiler: the other model (no model reflects on its own traces). No LLM judge for any quantity.

**DATA AND SPLITS.** ALFWorld `train`, all six task types: 3,553 trials of 1,465 unique tasks (task = type × object × receptacle × scene). Trials of one task are near-duplicate games, so **the unit of allocation and of statistical clustering is the task**; all trials of a task go to one split. Seeded, type-stratified, whole-task allocation (trials): **P_train 300 · P′_train 300 · S_screen 150 · S_dev 300 · S_test 1,800 · reserve ≈700.** P_train and P′_train are task-disjoint by construction. S_test is touched once, by the final grid. The official valid splits are Tier 1.

**ARTIFACTS (built once, hashed).**
- **I0^bare**: the hand-written scaffold with a generic, type-agnostic slot text. **I0^demo**: the scaffold plus two handcoded-expert trajectories from P_train (free, reproducible). **I0\*** := I0^demo if G1 passes under it, else I0^bare (rule fixed before S_dev runs).
- **B**: bank distilled by the annotator from all 300 P_train episodes run under I0^bare; format (ExpeL-style INSIGHT/PROCEDURE/OUTCOME vs ReasoningBank-style strategies with environment-verified labels) fixed by screening. **The sorted P_train episode-id list is SHA256-hashed into B and into I_P and checked at load.**
- **I_P(s)**, s ∈ {1,2}: GEPA-lite on P_train, seeded with I0\* verbatim, memory absent from context, budget 350 rollouts spent as one full sweep of the 300 games plus 50 (coverage 100% by construction), local reflector, training curves published.
- **I′(r)**: the same optimizer on P′_train (300 disjoint games), one run per seed carried to 500 rollouts with snapshots at r ∈ {50, 100, 200, 350, 500}. **I′_match** := the snapshot whose no-memory S_dev accuracy is within 1.5pt of ℓ_P = acc(I_P×M0) (G4); if none, the run is extended once to 750; if still none, the two bracketing snapshots both go to S_test and g′ is reported at both with the linear interpolation stated as such.
- **B′**: the same distillation from the 300 P′_train episodes under I0^bare (the bank-side mirror of I′), k- and token-matched to B at read time.
- **B^on**: the same distillation from P_train episodes run under I_P(1) (the on-policy bank).
- **I0_pad**: I0\* padded with task-neutral prose to I_P(1)'s token count (length control). **I_type**: a hand-written instruction given only the six type names and their canonical skeletons, written and hashed before S_dev runs (label-only control).
- **M_shuf**: k*(I) random items from B, retrieval bypassed, token-matched (within-domain distractor).
- **k\*(I)** for I ∈ {I0\*, I_P, I′_match}: the k ∈ {1,3,5,7} maximizing the paired gain of B over M0 on S_dev (75 games per k, 300 per instruction). I0_pad and I_type use k\*(I0\*); B′, B^on and M_shuf use k\*(I_P).

**SCREENING (S_screen only, published either way).** For each agent: a 100-game bank-source pool under I0^bare, both bank formats, memory gain at I0^bare on the remaining 50 games; the pairing with the largest gain that clears 5pt proceeds; all four numbers published.

**GATES (S_dev, n = 300; point estimate + lower 80% task-cluster bootstrap CI; a failure takes its branch, never a silent continuation).**
- **G0** dynamic range: acc(I0^bare×M0) ∈ [20, 80]%; timeout rate ∈ [20, 60]% (else L0 re-set once, logged).
- **K** read depth: k\*(I) per instruction as above, fixed before G1.
- **G1** memory has something to give: g(I0, B) ≥ 5pt with lower CI ≥ 2pt and ≥ 20 fixes, under I0^demo and I0^bare; I0\* rule as above. Fails under both → the memory-null branch (a bounded null in the environment where the literature says memory works, with the official-split cells at Tier 1 putting it on the published axis).
- **G2** the optimizer works: acc(I_P×M0) − acc(I0\*×M0) ≥ 3pt on both seeds. Fails → the optimizer-failure paper (arXiv 2604.14585's coin flip, measured), bank-side results carry the rest.
- **G4** level match: |acc(I′_match×M0) − ℓ_P| ≤ 1.5pt on S_dev (rule above).
- **G5** hygiene: retriever relevance ≥ 60% on a 100-episode audit; item truthfulness ≥ 70% on 100 items; aggregate throughput ≥ 11,000 calls/h; **the within-task ICC and DEFF are measured on S_dev and the MDE table republished before any S_test cell**; timeout rate → calls/episode republished.
- **NULL floor**: from the row-9 replicate; no effect is claimed unless its estimate exceeds the 95th percentile of the pooled null.

**CONDITION GRID (S_test, game-paired; n = trials; calls/episode 17).**

| # | Cell | n | opt seeds | dec seed | episodes | calls | Purpose |
|---|---|---|---|---|---|---|---|
| 1 | I0\* × {M0 @11, M0 @23, B@k\*(I0\*)} | 1800 | — | 11/23 | 5,400 | 91,800 | g(I0\*); treatment-free accuracy floor |
| 2 | **I_P(1,2) × {M0, B@k\*(I_P)}** | 1800 | 2 | 11 | 7,200 | 122,400 | **primary E: g(I_P)** |
| 3 | **I′_match(1,2) × {M0, B@k\*(I′)}** | 1800 | 2 | 11 | 7,200 | 122,400 | **primary D: g(I′) − g(I_P)**; the level-matched headroom control |
| 4 | I_P(1) × B′@k\*(I_P) | 1800 | 1 | 11 | 1,800 | 30,600 | bank-side episode provenance |
| 5 | I_P(1) × B^on@k\*(I_P) | 900 | 1 | 11 | 900 | 15,300 | staleness |
| 6 | I0_pad × {M0, B@k\*(I0\*)} | 900 | — | 11 | 1,800 | 30,600 | prompt-length rival |
| 7 | I_type × {M0, B@k\*(I0\*)} | 900 | — | 11 | 1,800 | 30,600 | type-label rival |
| 8 | {I0\*, I_P(1)} × M_shuf | 900 | 1 | 11 | 1,800 | 30,600 | injected-text-ignored rival |
| 9 | **NULL:** I_P(1) × {M0, B} | 900 | 1 | **37** | 1,800 | 30,600 | treatment-free replicate of g |
| | **Tier-0 test grid** | | | | **29,700** | **505,000** | |

Artifacts: bank-gen 300, P′ gen 300, on-policy gen 300, GEPA I_P 2×350, ladder 2×500 = **2,600 episodes**, plus ≈2,000 annotator calls. Screening ≈ 2,300. Dev: k-tuning 900, G1 1,200, G2/G4 titration 750, smoke 100 = **2,950**. **Tier 0 total ≈ 37,600 episodes ≈ 640,000 calls ≈ 39–54 h at the program-measured 11,800–16,600 calls/h per node.** Calls/episode = 0.75·12 + 0.25·30 + 0.5 = 17, re-measured at G5.

**Tier 1** (≈ 9,000 episodes, in this order): the official `valid_seen`/`valid_unseen` with {I0\*, I_P} × {M0, B}; I_P × C (a block compiled once from B, token-matched); the coupling arm I2 (optimized with B in context) × {B, M0}; the joint-optimization arm J × M0; X_dist (out-of-domain items); a third optimizer seed on rows 2–3; medgemma-27b-it on rows 2–3. **Contingency cuts** if G5 throughput < 11,000 calls/h, in this order: row 8 → row 7 → row 6 → row 5 → row 4 to n = 900 → rows 2–3 to n = 1,200 with the MDE republished. **Rows 1, 2, 3 and 9 are never cut.** Unrun arms are reported as unrun.

**PRIMARY ENDPOINTS.** For an instruction I, the **residual memory value** is the game-paired quantity g(I) = acc(I×B@k\*(I)) − acc(I×M0). Two pre-registered tests form the confirmatory family, evaluated as an intersection (both must hold for the title):

- **E (residual).** The 90% task-cluster bootstrap CI of g(I_P), pooled over the two optimizer seeds as fixed strata, lies inside ±3pt (TOST). At n = 1,800 with planning discordance 0.20 and DEFF 1.4, SE(g) ≈ 1.25pt and the 90% half-width ≈ 2.1pt, so **E is declarable only when |ĝ(I_P)| ≤ 0.9pt**; a residual in (0.9, 3] is reported as a *bounded residual* with its CI, never as equivalence, and the retention ratio R = g(I_P)/g(I0\*) is reported alongside with a bootstrap CI as a descriptive quantity.
- **D (episode-specific).** g(I′_match) − g(I_P) ≥ 3pt with 90% one-sided task-cluster bootstrap lower bound > 0. The two residuals are measured on the same games at the same no-memory accuracy, so headroom compression cancels by construction. SE of the paired difference ≈ 1.6pt (positive correlation through the shared M0-free games), MDE at 80% power ≈ 4pt; the 3pt threshold is a floor on the point estimate, the lower bound is the test.

**Pre-registered readings, both directions published.** E ∧ D → the title stands: the instruction absorbed *these* episodes. E ∧ ¬D → absorption is distribution-level: any instruction optimized on this task distribution already holds the bank's value; the title becomes "an optimizer that has seen this task distribution already holds the bank's value", and the practical conclusion is unchanged. ¬E → the bank still pays at the optimized instruction; the paper reports the bounded residual and R, and the rivals below say why.

**NAMED RIVALS AND THEIR ARMS.** (a) *Headroom*: I′_match (row 3) is at the same level as I_P; if g collapses at both, the collapse is headroom, and D cannot pass. (b) *Prompt length*: g(I0_pad) (row 6); if a longer scaffold alone collapses g, the mechanism is dilution. (c) *Type-label knowledge*: g(I_type) (row 7); if naming the six types collapses g, no episodes were needed. (d) *Staleness*: g^on = acc(I_P×B^on) − acc(I_P×M0) (row 5); if g^on − g(I_P) is large, the shrinkage was an off-policy bank. (e) *Injected text ignored*: the **item-following rate** f(I) (fraction of episodes whose action sequence executes ≥ 1 action named in an injected item and not in the M0 trajectory of the same game, computed from logs) and the **random-item harm** h(I) = acc(I×M0) − acc(I×M_shuf) (row 8). If f(I_P) < 0.5·f(I0\*) or h(I_P) is within noise of zero while h(I0\*) is not, injected text is being ignored at I_P and E is reported as *ignored*, not *absorbed*. (f) *Bank-side provenance*: g′ = acc(I_P×B′) − acc(I_P×M0) (row 4); |g′ − g(I_P)| ≤ 3pt says the bank's content is distribution-level.

**SECONDARY.** Retention ratio R with CI; k\*(I) per instruction and the full k-curves at I0\* and I_P; per-type and per-room breakdowns of every row; content overlap (zero-episode: max embedding and ROUGE-L similarity of each B item to any sentence of I_P, against B′-vs-I_P and B-vs-I′ nulls); timeout/step decomposition of every delta.

## Baselines and Ablations

**Baselines that could win and would refute us.** (i) *A bounded residual*: g(I_P) has a 90% CI outside ±3pt → the bank still pays at the optimized instruction; reported with R. (ii) *Distribution-level absorption*: E holds but g(I′_match) − g(I_P) has a lower bound ≤ 0 → the title changes as pre-registered. (iii) *Staleness*: g^on exceeds g(I_P) by ≥ 3pt → "banks must be re-distilled under the deployed instruction". (iv) *Ignored, not absorbed*: f(I_P) collapses or h(I_P) ≈ 0 → the optimized instruction stops reading injected text; E is reported as such. (v) *Length or label*: g(I0_pad) or g(I_type) collapses like g(I_P) → the collapse needs no episodes. (vi) *Optimizer failure*: G2 fails → the coin-flip result on a local reflector, measured.

**Ablations that isolate the mechanism.** Row 3 is the identification: the same optimizer, the same budget, the same distribution, disjoint episodes, matched level. Row 4 is its bank-side mirror. Rows 6–7 are the two cheap instructions that would absorb without episodes. Row 8 and the following rate separate absorption from ignoring. Row 9 is the treatment-free replicate of the primary quantity. Screening over agent × bank format is published either way. **Tier 1** holds everything that is a consequence rather than an identification: compile-once, the coupling arm, joint optimization, the official splits, a second model family.

## Falsifiable Predictions

1. **E.** The 90% CI of g(I_P) lies inside ±3pt; the realized SE and DEFF are reported; if |ĝ| ∈ (0.9, 3] the result is a bounded residual, not equivalence.
2. **D.** g(I′_match) − g(I_P) ≥ 3pt with 90% lower bound > 0. Failure with E passing is reported as distribution-level absorption under the pre-registered alternative title.
3. **Not length, not label.** g(I0_pad) ≥ g(I0\*) − 1.5pt and g(I_type) ≥ g(I0\*) − 2pt.
4. **Not staleness.** g^on − g(I_P) has a 90% upper bound < 3pt.
5. **Not ignored.** f(I_P) ≥ 0.5·f(I0\*) and h(I_P) ≥ h(I0\*) − 2pt: the optimized agent still reads injected items and random items still cost it.
6. **Bank side.** |g′ − g(I_P)| ≤ 3pt (the bank's content is distribution-level) is the expected reading; the opposite is reported as episode-specific bank content.

**Refutation.** (i) is the most likely way the hypothesis dies and is the primary result if it happens. (ii) is a pre-registered reframing, not a rescue. (iii)–(v) each replace the claim with a named mechanism.

## Measurement and Noise Control

**Units.** Outcomes are game-paired across cells; **clusters are tasks** (1,465 unique; ≈2.4 trials per task). Superiority: exact McNemar on fix/break tables reported, with the task-cluster bootstrap CI (10k resamples) as the decision statistic. Equivalence: TOST by 90% cluster-bootstrap CI inside ±3pt. Optimizer seeds are fixed strata (two seeds do not identify a crossed random effect; the between-seed spread is reported per row). Holm families: F-A {E, D} (intersection, no correction); F-B {predictions 3–6}; F-C {Tier 1}. **Null floor:** row 9 (seed 37) replicates g(I_P); row 1's two M0 seeds give the accuracy floor; nothing is claimed below the 95th percentile of the pooled null. **MDE (planning):** discordance 0.20, DEFF 1.4 → SE(g) ≈ 1.25pt at n = 1,800; SE(g′ − g) ≈ 1.6pt; both republished from S_dev measurements (G5) before S_test. **Timeout decomposition:** any cell whose delta is > 50% accounted for by a timeout-rate change is flagged. **Instrumentation per episode:** game id, task id, type, room, instruction hash + provenance + rollout budget, bank id + provenance, k, injected item ids and tokens, seed, steps, success, timeout, invalid actions, full action trace; optimizer runs log per-rollout game ids and candidate lineage. One script produces every table from the JSONL logs.

## Preprint Collision Check

**Channels (this node, 2026-09-07):** Claude Code web search (server-side; arxiv.org, openreview.net and the HF file CDN are blocked from the node; the HF Papers API is reachable). ExpeL's ablation numbers were read on 2026-09-07 from its project page and arXiv HTML through web search and are quoted in Related Work (0). Prior scans: 2026-08-21, 2026-09-03 (15 HF queries, 244 papers, 54 IDs verified by id, EvoAgentBench read in full from a PI-supplied PDF).

**Collisions conceded.** ExpeL's ablation (two-container redundancy on ALFWorld, 2023). EvoAgentBench (shared-trajectory table with GEPA and a retriever, 2026). AutoManual / AutoGuide (ALFWorld experience compiled into instruction text, 2024). AWM / Dynamic Cheatsheet / ACE (one accumulated context vs per-instance retrieval; ACE vs GEPA). MIPROv2 (instruction vs demonstration ablation). Experience Distillation (retention ratio with weights as the second container).

**What survives, stated narrowly:** the residual at a *search-optimized* instruction measured at the bank's own re-tuned budget; the episode-disjoint, level-matched instruction as the identification of episode-specific versus distribution-level absorption; paired, clustered, token-matched, null-replicated statistics with a stated MDE.

**Open obligations, all unrun and freeze-blocking for DESIGN.md:** (1) the provenance / held-out-episode crossover search in prompt-optimization, contamination and data-attribution literatures (one query run 2026-09-07, nothing found; not sufficient); (2) the appendix of arXiv 2608.14036 (a token-matched compiled-block comparison would affect only Tier 1 now); (3) abstracts of arXiv 2604.18206 and 2604.11811; (4) a pre-2026 re-sweep of the memory-as-instruction line. A collision on (1) reduces the contribution to the ALFWorld measurement with its controls; that is stated here rather than discovered later.

## Risk Factors and Limitations

1. **G1 may fail on this stack.** This program measured +0.6 to +2.4pt for the same bank family in multi-hop QA; ALFWorld's published 5–15pt were under demonstration-bearing scaffolds, which is why I0^demo exists and the I0\* rule is fixed in advance. The memory-null branch is publishable and cheap to reach.
2. **E is declarable only near zero.** At n = 1,800 the ±3pt TOST passes only for |ĝ| ≤ 0.9pt; a real 1–3pt residual is reported as bounded, not as equivalence. n = 2,400 would move the bar to ≈1.4pt and is the first use of the reserve if G5 clears with margin.
3. **D is powered at ≈4pt, thresholded at 3pt.** A true 3pt difference passes about half the time; the lower-bound test, not the point threshold, decides.
4. **Level matching is discrete.** I′_match is a snapshot within 1.5pt of ℓ_P; the residual level gap is reported and the bracketing-snapshot fallback is pre-registered.
5. **Local reflector.** A 32B reflector writes weaker instructions than GEPA's frontier reflectors; this lowers absorption and makes E harder to pass, which is conservative for the claim and is why G2 is live.
6. **Task clustering.** DEFF is assumed 1.4 (ICC ≈ 0.3) and measured on S_dev; every MDE is republished before S_test.
7. **Scope.** One environment, one training split, held-out training games rather than the official valid splits (Tier 1); ALFWorld's six types recur in structure, which favours absorption and is stated as the setting's bias.
8. **Compute.** Throughput is transferred from a 6-call QA setting and gated by G5 before anything depends on it; two A100s, no API.
9. **Novelty is capped by the concessions above** and the score should be read accordingly: this is identification and an interval on top of an accepted qualitative result.
