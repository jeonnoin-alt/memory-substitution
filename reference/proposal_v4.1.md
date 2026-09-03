# Proposal v4.1 — memory_or_instruction (2026-09-03; v4 revised after harness judging, see reviews/v4/SUMMARY.md)

Lineage: v1 6.73 → **v2 6.97** → v3 5.73 (pivot, superseded) → v4 6.02 (harness, 3 reviewers) → **v4.1 (this file)**. v4 is v2's design with the reviewer objections answered and the 2026-09-03 scan absorbed. Judging uses only the 11 IDEA_FIELDS below; the decision log is context.

## Decision log (what changed vs v2 and why)

| # | Objection (source) | v4 answer |
|---|---|---|
| 1 | Fairness constraint not enforced — bank sees all training episodes, GEPA sees a sampled subset (v1 R2) | One split S_train feeds both containers. GEPA coverage is instrumented per run (episodes touched, visit counts, reflector-visible episodes). A second bank **B_touched** is distilled only from the episodes each GEPA seed's rollouts actually touched, and S is recomputed with it. If S(B) and S(B_touched) differ by more than the pre-registered 0.15, exposure drove the result and we say so. |
| 2 | I2 (optimize with memory in context) omission is self-serving (v1 R1) | Reinstated at 2 optimizer seeds: **I2×M1** (co-adaptation) and **I2×M0** (memory removed → dependence test). Pre-registered readouts: synergy (I2×M1 vs max(I1×M1, I1×M0)) and dependence (I2×M0 vs I1×M0). |
| 3 | LoRA as third container (v1 R2) | Added as a descriptive-only arm: LoRA-SFT on the *same* solved S_train episodes, cells L×M0 and L×M1, 1 seed. Cited recipe (arXiv 2603.18272); Experience Distillation's finding that plain SFT retains 3.8% of in-context gains (arXiv 2607.21051) is the pre-registered expectation. |
| 4 | Stuff-the-whole-bank baseline (v3 R2; EvoMemBench) | Added **M_all**: entire bank in context, unretrieved, uncompiled (feasible: ≤400 items ≈ 30k tokens). Separates "content present" from "retrieval" from "compilation". |
| 5 | Citation verifiability (v1 R2, v3 3/3) | Every arXiv ID ships in `reference/litscan_2026-09-03.md` with title / date / verification channel / role. v2's retraction of five IDs is reversed: all five exist and are reinstated with their actual roles. |
| 6 | Track scope: "coupling" must be engaged (v3 3/3) | v4 keeps v2's substitution core and adds the coupling cells (I2) plus the residual-complementarity and moderator readouts. The paper's service to the track: S says whether coupling is worth doing at all; I2 says whether it adds beyond either container; the moderator says where the residual lives. |
| 7 | Precheck gate ≥10pt is unattainable on this program's agents (own measurement, proposal ①) | Agent and gate re-derived from measured numbers: primary agent gpt-oss-120b (bank effect +7.7pt, p=.0018, n=300 paired, in this pipeline); gate ≥6pt at n=1000; Qwen3.5-27B (+0.6pt, TOST-equivalent) kept as the pre-registered *degenerate regime* where S is undefined and reported as such. |
| 8 | EvoAgentBench (2026-07) already compares Memento / ReasoningBank / GEPA on shared trajectories | Named as the closest work in every relevant field; v4's claim is scoped to what its table cannot give: the combined cell, token-matched compiled arm, the ratio, and paired statistics. |
| 10 | v4 R1–R3 unanimous: primary agent gpt-oss-120b violates the track's 7B–32B scope; the in-scope agent was pre-declared degenerate | The primary grid runs on an in-scope agent chosen by a **pre-registered screening stage** over {Qwen3.5-27B, Qwen3-32B} × {ExpeL bank, ReasoningBank-style bank} on S_dev; the pairing with the largest paired gain ≥ gate is A1, all screening numbers are published, and gpt-oss-120b becomes a Tier-2 out-of-scope scale check that is never load-bearing. |
| 11 | v4 R1–R3: ReasoningBank-style bank missing — the format the closest work evaluates | Added **B_rb** (self-judged success *and* failure distillation, same retriever and k). It enters screening on equal footing and, whichever bank wins, the other is run at the core cells so S can be compared across bank types. |
| 12 | v4 R3: add a genuinely self-editing (test-time updating) memory | Refused with reasons: the substitution question requires a frozen artifact so both containers see identical episodes and test instances stay paired; test-time writes give memory exposure the instruction cannot match and add order effects. ReasoningBank's distillation format is adopted; its online update is held after S_train. |
| 13 | v4 R1, R2: scope exceeds "days, not weeks"; state the guaranteed core | Cells are tiered. Tier 0 must ship; Tier 1 ships on the measured throughput budget; Tier 2 only on surplus. Tier 0 alone answers the primary hypothesis. |
| 14 | v4 R3: the internal pilot and the scan are unpublished context | Both are appendices of this proposal: `reference/shortcutting_v4/` (frozen design, gate log, abstract, code) and `reference/litscan_2026-09-03.md` (verification table, raw records). |
| 9 | Compile prediction is no longer a surprise (skills > workflow memory; single rewrite suffices) | Prediction 3 re-pitched as a quantified equivalence at matched tokens against live retrieval, with the whole-bank arm as the third point on the retrieval → compile → dump ladder. |

Refused, with reasons: (a) ReasoningBank-style self-judged distillation as a second bank type (v1 R1) — deferred to E1's bank-variant appendix at 1 seed only if Stage 1 completes early; it tests distillation style, not substitution, and the budget is the binding constraint on 2 GPUs. (b) v3's overlap statistic and frozen-subset arm — not restored; they belong to the retrieval-necessity question, which v3 showed the track does not want in isolation.

---

## Name

memory_or_instruction

## Title

Is Your Agent's Memory Just an Un-Optimized Prompt? Measuring the Residual Value of Retrieved Experience After Instruction Optimization on Matched Episodes

## Short Hypothesis

Published agentic-memory gains are measured against a hand-written instruction. For procedural experience memory (ExpeL/ReasoningBank-style banks retrieved per query), we hypothesize that most of that gain is *substitutable*: when a reflective prompt optimizer is given exactly the same training episodes that built the bank, the memory-vs-no-memory gap shrinks to within a pre-registered equivalence margin, and a frozen instruction compiled once from the whole bank, with no retrieval at inference, is equivalent to per-instance top-k retrieval at matched injected tokens. Co-adapting the optimizer to the bank (I2) does not produce gains that neither container reaches alone. The residual, non-substitutable value of memory is concentrated in instances with genuinely instance-specific reusable content, which we verify with a deliberately non-compilable positive-control bank where substitution must fail. The claim is agent- and bank-relative and is tested inside the track's model class: a pre-registered screening stage over two open-weight 27–32B agents and two bank formats selects the pairing where memory has a measurable effect at the hand-written instruction, and the pairings where it does not are reported as the memory-null regime rather than averaged over.

## Related Work

**(1) Procedural experience memory — the targets.** ExpeL (arXiv 2308.10144) gathers training-task experiences, extracts natural-language insights, and recalls them at inference. ReasoningBank (arXiv 2509.25140) distills strategies from self-judged successes and failures. Memp (arXiv 2508.06433), A-MEM (arXiv 2502.12110) and retrieval-augmented agents trained to use retrieved trajectories (arXiv 2603.18272) share the evaluation template: the memory-vs-no-memory delta is measured at a fixed, hand-written scaffold, or memory is compared against fine-tuning. The template assumes memory and instruction are non-substitutable containers.

**(2) Reflective prompt optimizers.** GEPA (arXiv 2507.19457, ICLR 2026 oral) samples trajectories, reflects in natural language, and proposes prompt updates, outperforming MIPROv2 by >10% and GRPO by ~10% with up to 35× fewer rollouts. GEPA and ExpeL run the same learning principle — reflect on trajectories, distill lessons — and differ in where the lesson is stored. "Prompt Optimization Is a Coin Flip" (arXiv 2604.14585) shows that in compound systems 49% of optimizer runs land below zero-shot and that gains require exploitable output structure; this is the prerequisite risk for any optimizer-as-control design and we treat I1 > I0 as a gated result, not an assumption.

**(3) Three-way comparisons on shared trajectories — the closest work.** EvoAgentBench (arXiv 2607.05202) evaluates Vanilla, Memento (retrieve nearest retained case), ReasoningBank (retrieve distilled memory), GEPA (evolve one prompt) and a curated reference on a shared 528/267 train/test split across four domains and three backbones, and reports that ReasoningBank gains ≈ +7 on Qwen backbones, GEPA nearly matches the curated reference on Gemma-4-31B, and no automatic method is positive in every cell. It is the first published table with a retriever and GEPA on the same training trajectories. It contains no combined optimizer-plus-memory cell, no token matching, no compiled-bank arm, and no paired statistics, so it cannot say how much of memory's value survives once the instruction container is filled — which is our object. EvoClinician (arXiv 2601.22964) lists "prompt optimization agent" and "memory agent" as baseline categories in a clinical application (excluded domain here). TERMS-Bench (arXiv 2605.13909) uses GEPA as a prompt-ablation to test whether prompt engineering saturates a negotiation benchmark — the logical move "run an optimizer as the control for a non-prompt claim", in a different domain and without memory.

**(4) The confound-audit literature.** MemDelta (arXiv 2606.29914) shows headline memory gains flip under one-variable changes (embedding swap +6.2pp; Mem0 vs RAG reverses). "Diagnosing Retrieval vs. Utilization Bottlenecks" (arXiv 2603.02473) finds retrieval method spans 20 points while write strategy spans 3–8, and raw chunks match lossy writes. Memory-R2 (arXiv 2605.21768) fixes credit-assignment unfairness in RL-trained memory. EvoMemBench (arXiv 2605.18421) finds long-context baselines "remain highly competitive" against 15 memory methods. All audit confounds inside the memory pipeline or against context-dumping; none posits an optimized instruction as a rival container.

**(5) Memory harm.** "When Continual Learning Moves to Memory" (arXiv 2604.27003) documents retrieval pollution, context competition and dilution, with negative transfer concentrated on hard cases; MemHarness (arXiv 2607.28272) reports raw memory injection at 70.1% versus 76.4% for no-memory RL on ALFWorld. A pre-registered study in this program (proposal ①, 33 arms, ~29,500 episodes, 2026-08) found an ExpeL bank's paired effect TOST-equivalent to zero on Qwen3.5-27B (+0.6pt, 90% CI [−1.2, +2.5]) and +7.7pt (p=.0018) on gpt-oss-120b, and that a one-line instruction dominated every memory manipulation on the strong agent. That result is why v4.1 screens agent×bank pairings inside the track's model class before committing the primary grid, and reports the memory-null pairings alongside the winner; the pilot's design, gate log and results are an appendix of this proposal.

**(6) Containers other than the prompt.** Experience Distillation (arXiv 2607.21051) measures how much of an in-context-learning gain survives when the experience is moved into weights by context distillation (≥64.8%) versus SFT (3.8%) — the same "retention ratio" shape as S, with weights as the second container. TMEM (arXiv 2606.04536) stores experience in fast LoRA weights; experience-internalization work (arXiv 2606.04703) finds principle-level experience more durable than instance-level. These establish that the container question is live; none uses an optimized instruction as the container, and none needs gradient access to the served model, which S does not.

**(7) Compiled procedures.** Skills (distilled SKILL.md) beat Workflow Memory by 6.06pt in matched comparison, with 65.7% of the benefit attributable to procedural anchoring rather than fact injection, and retrieval precision collapsing from 29.6% to 3.3% as the pool grows (arXiv 2608.14036); model-generated skills help on average but hurt 25% of cases (arXiv 2605.23899); a single rewrite given the full training signal matches 10 rounds of refinement within 0.2% (arXiv 2606.30775); embedding retrieval of procedures degrades under vocabulary shift while LLM abstractions transfer (arXiv 2511.21730). These make "compile once" a plausible direction; none tests a compiled artifact against live per-instance retrieval at matched tokens with the same bank, which is what our compiled arm C does. MemAPO (arXiv 2603.21520) runs the coupling in the opposite direction (memory inside the optimizer) and MAS-PromptBench (arXiv 2606.23664) studies prompt optimization without memory.

**Our position.** A memory bank and an optimized instruction are two containers for the same training-episode information. EvoAgentBench put them in one table; nobody has measured how much of the first container's value survives when the second is filled first, at matched information exposure and matched tokens, with the combined cell, a compiled-bank arm, a whole-bank arm, and a positive control that certifies the instrument can detect non-substitutable value.

## Abstract

Agentic memory systems are evaluated by comparing an agent with a retrieved-experience bank against the same agent without one, holding a hand-written scaffold prompt fixed. Recent audits show such comparisons flip under retrieval-pipeline changes, and the first shared-trajectory benchmark now places memory retrievers and a prompt optimizer side by side. We ask the question that table cannot answer: a bank distilled from training episodes and an instruction optimized on those same episodes are two containers for the same information, and the second is cheaper to serve — one prompt paid once, versus retrieved tokens paid every episode. How much of memory's value survives once the instruction container is filled? Holding agent, tools, retriever, training split and evaluation fixed, we build (i) ExpeL-style and ReasoningBank-style banks with top-k retrieval, (ii) an instruction optimized by GEPA on the identical episodes without ever seeing the bank, with per-run episode coverage instrumented and a coverage-matched bank as a control, (iii) an instruction optimized with the bank in context, (iv) a frozen instruction compiled once from the whole bank, token-matched to retrieval, and (v) the whole bank dumped into context. The primary endpoint is the substitution ratio S — the fraction of memory's paired gain at the hand-written instruction that disappears at the optimized one — tested as a conjunction of superiority at the hand-written instruction and TOST equivalence at the optimized one. A deliberately non-compilable positive-control bank must show S < 0.25, so a null on the main benchmark is a finding rather than a power failure. The agent is a 27–32B open-weight model chosen by a pre-registered screening over two agents and two bank formats on a dev split, because a pre-registered study in this program found the same ExpeL bank equivalent to no memory on one such agent; pairings that fail the gate are reported as the memory-null regime. Scope: one primary tool-augmented multi-hop QA environment (n=1000 paired, 4 optimizer seeds), one replication environment (ALFWorld), ≈33,000 primary-environment episodes in the must-ship and budgeted tiers, instance-paired McNemar and TOST, crossed random effects for optimizer seed, null replicates, and a stated minimum detectable effect.

## Experiments

**HELD FIXED THROUGHOUT.** ReAct scaffold; tool stack (BM25 search over each dataset's fixed corpus); step limit (8 calls, +3 under any enforcement); retriever (MiniLM dense, CPU); decoding temperature and seed schedule {11, 23, 37}; the training split from which all learned artifacts derive; the held-out test split. Only the instruction slot and the memory-injection variant differ. The fairness constraint: bank and optimizer see the same S_train episodes, and this is measured, not assumed (see Coverage).

**AGENTS (all inside the track's 7B–32B class, all local).** Candidates: Qwen3.5-27B (dense) and Qwen3-32B (dense, thinking disabled), each served with vLLM at one replica per A100. **Screening stage (pre-registered, S_dev, published either way):** for each agent, run bare I0 on S_train (bank-gen), distill both bank formats, then measure the paired gain acc(I0×M1) − acc(I0×M0) on S_dev (n=150) for each of the four agent×bank pairings. **A1** is the pairing with the largest paired gain that clears gate G1 (≥6pt, fixes ≥8); ties within 2pt resolve to the ExpeL bank on Qwen3.5-27B for comparability with the program's prior study. The other bank format on A1's agent is **B'** and runs at the core cells (Tier 1). The losing agent is **A2** and runs the four core cells at n=500 (Tier 2) as the memory-null or memory-weak regime. If no pairing clears G1, the bank is enriched once (more S_train episodes, larger k) and screening is re-measured; if it still fails, the study stops and reports four TOST-equivalence tests as its result. gpt-oss-120b (out of scope for the track) is a **Tier-2 scale check only**: cells 1, 2, 5, 6 at n=500, never load-bearing, reported separately. Frontier API model (Claude, Opus 5 or Sonnet 5) as GEPA reflector, distiller and offline compiler, identical across conditions; pre-registered fallback Qwen3-32B (local) if the key is unavailable, reported as a deviation. Scoring is programmatic (normalized EM primary, F1 descriptive; ALFWorld success), so no LLM judge is on the critical path.

**ENVIRONMENTS.** *E1 (primary):* tool-augmented multi-hop QA over fixed corpora, pooled HotpotQA-distractor / MuSiQue / 2WikiMultihopQA (HippoRAG subsets, provenance and SHA256 committed). *E2 (replication, Tier 1):* ALFWorld, all 274 eval tasks (134 unseen reported separately), ~25 calls/episode, chosen because task templates recur across train and test so procedural memory is maximally compilable and the substitution prediction is most exposed. Public data only.

**SPLITS (seeded, stratified 50/30/20 by dataset, instance IDs pre-registered).** S_train 400 (feeds both bank distillation and every optimizer run), S_dev 150 (screening, gates, compiler-prompt fixing, length control), S_test 1000 (paired evaluation; disjoint from S_train and from the earlier study's S_bank/S_opt; gold-document title-overlap between S_train and S_test removed and counted). Reserve untouched except for gate-triggered rebuilds, logged.

**ARTIFACTS (built once, frozen, hashed).**
- **B_expel:** ExpeL-style bank: solved S_train episodes distilled into INSIGHT / PROCEDURE / OUTCOME items; deduplicated; top-k=7 dense retrieval.
- **B_rb:** ReasoningBank-style bank: every S_train episode is self-judged (success/failure) by the agent's own judgment prompt and distilled into strategy items that record both what worked and what to avoid; same retriever and k. Held frozen after construction (see Risk 10 for why test-time updating is excluded).
- **B_touched(s):** for each GEPA seed s, the subset of the primary bank whose source episodes were touched by that run's rollouts (minibatch evaluations or reflector-visible failure summaries). Distillation only; no new episodes.
- **I1(s):** GEPA-style reflective optimization of the instruction slot on S_train minibatches, seeded with I0 verbatim, 350 rollouts per run, memory absent from context, 4 seeds. Coverage instrumented: episodes touched, visit counts, and the set shown to the reflector.
- **I2(s):** same procedure with the primary bank retrieved into context during optimization, 2 seeds.
- **I3:** I0 padded with task-generic boilerplate to the median token length of I1 (length control).
- **C:** the compiler reads the entire primary bank offline and writes one static instruction block, token-matched per instance to what top-k=7 injects; compiler prompt fixed on S_dev and reported verbatim. A measurement instrument, not a proposed method.
- **R:** raw few-shot: the same retriever over the undistilled solved S_train trajectories, injected verbatim, token-matched to M1.
- **M_all:** the entire primary bank in context, unretrieved and uncompiled (≈30k tokens at 400 items; served with a raised context length).
- **L:** LoRA-SFT of A1 on the solved S_train trajectories (same episodes as the bank), one seed, descriptive only.
- **B-dup:** positive-control bank seeded with distilled trajectories for paraphrased near-duplicates of 300 held-out S_test instances (disjoint from any optimization set); its value is instance-specific and cannot be compressed into a bounded instruction.

**GATES (S_dev, n=150, published either way; any fail → stop and report).** G1 bank effect at I0 on the screened pairing: paired gain ≥6pt with fixes ≥8 and breaks counted. G2 optimizer headroom: I1 > I0 by ≥2pt on S_dev for at least 3 of 4 seeds, else the optimizer-failure branch (Risk 2) is triggered and reported. G3 retriever relevance ≥60% on a 100-item audit. G4 stored-record truthfulness ≥70%. G5 throughput ≥400 episodes/hour aggregate, else the matrix is re-scoped before running, not silently.

**E1 CONDITION GRID (A1), fully instance-paired on S_test. Tier 0 must ship; Tier 1 ships within the measured throughput budget; Tier 2 only on surplus.**
| # | Cell | n | seeds | Tier | Purpose |
|---|---|---|---|---|---|
| 1 | I0×M0 | 1000 | 2 decoding | 0 | no-memory baseline |
| 2 | I0×M1 | 1000 | 2 decoding | 0 | the standard memory-paper comparison (denominator of S) |
| 3 | I0×C | 1000 | 2 decoding | 0 | compiled static, token-matched — does retrieval buy anything? |
| 4 | I0×R | 1000 | 2 decoding | 1 | distillation vs raw exemplars |
| 5 | I1×M0 | 1000 | 4 optimizer | 0 | optimized instruction alone |
| 6 | I1×M1 | 1000 | 4 optimizer | 0 | numerator of S |
| 7 | I3×M0 | 1000 | 1 | 1 | length control |
| 8 | I0×M_all | 500 | 1 | 1 | content present, no retrieval, no compilation |
| 9 | I2×M1 | 1000 | 2 optimizer | 1 | co-adaptation |
| 10 | I2×M0 | 1000 | 2 optimizer | 1 | dependence: memory removed after co-adaptation |
| 11 | I1×M1_touched | 500 | 4 optimizer | 1 | S under coverage-matched bank |
| 12 | I0×M1', I1×M1' (bank B') | 500 | 1, 2 optimizer | 1 | S across bank formats |
| 13 | NULL I0×M0, I0×M1 @ seed 37 | 500 | 1 | 0 | treatment-free replicate |
| 14 | I0×M1dup, I0×Cdup, I1×M1dup | 300 | 1,1,2 | 0 | positive control |
| 15 | L×M0, L×M1 | 500 | 1 | 2 | parametric third container (descriptive) |
| 16 | A2 (losing pairing): cells 1,2,5,6 | 500 | 1 / 2 optimizer | 2 | memory-null or memory-weak regime |
| 17 | gpt-oss-120b: cells 1,2,5,6 | 500 | 1 / 2 optimizer | 2 | out-of-scope scale check, reported separately |

**PRIMARY ENDPOINT.** S = 1 − [acc(I1×M1) − acc(I1×M0)] / [acc(I0×M1) − acc(I0×M0)], computed per optimizer seed, reported as a distribution with a cluster-bootstrap CI (resampling instances and optimizer runs). The pre-registered *test* of substitution is a conjunction: H1 (superiority) the paired gain at I0 is ≥ the gate and McNemar-significant on S_test; H2 (equivalence) the paired gain at I1 lies within ±4pt by TOST (90% bootstrap CI), with the sign of the drop consistent in ≥3 of 4 optimizer seeds. S ≥ 0.6 is the directional prediction; H1∧H2 is the claim. Every cell reports its paired fix/break decomposition against I0×M0. Screening uses S_dev only; S_test is touched once, by the final grid.

**SECONDARY ENDPOINTS.** (a) Compilation sufficiency: I0×C vs I0×M1, TOST ±4. (b) Ladder: I0×M1 vs I0×C vs I0×M_all. (c) Distillation value: I0×M1 vs I0×R. (d) Residual complementarity: I1×M1 vs max(I1×M0, I0×M1). (e) Coupling: synergy I2×M1 vs max(I1×M1, I1×M0); dependence I2×M0 vs I1×M0. (f) Coverage: |S(B) − S(B_touched)| ≤ 0.15 pre-registered as "exposure did not drive S". (g) Bank-format invariance: |S(B) − S(B')| ≤ 0.2. (h) Optimizer generality (Tier 2): MIPROv2-style optimizer substituted for GEPA, 2 seeds, cells I1'×M0 and I1'×M1, n=300. (i) Third container (Tier 2): L×M1 − L×M0 reported descriptively next to the same contrast at I0 and I1.

**ISO-COST CURVE (Tier 2, 3 points).** Held-out accuracy (n=300, 1 decoding seed) versus training-time LLM-call budget at ~250 / ~900 / ~2500 calls, for grow-the-bank vs more-optimizer-rollouts, 2 seeds per point; top points are existing cells. Report crossover budget and inference-time cost per episode.

**MODERATOR ANALYSIS (reuses runs).** Per test instance: max dense similarity to any bank item, plus a labeled "instance-specific reusable content" flag (LLM label, 100 cases human-validated, κ reported). Residual memory gain at I1 regressed on similarity with instance and optimizer-run as crossed random effects.

**E2 (ALFWorld, Tier 1).** I0×M0, I0×M1, I0×C, I1×M0, I1×M1; 2 optimizer seeds; 2 decoding seeds for the two I0 cells (null replicate), 1 elsewhere; bank from 200 training episodes.

**COMPUTE ARITHMETIC.** Screening: bank-gen 2 agents × 400 = 800, screening cells (M0 per agent, M1 per pairing) = 900. Tier 0: cells 1–3 = 6,000; cells 5–6 = 8,000; nulls 1,000; positive control 1,200; GEPA rollouts 4×350 = 1,400 → **17,600**. Tier 1: cell 4 = 2,000; 7 = 1,000; 8 = 500; 9–10 = 4,000 + 700 rollouts; 11 = 2,000; 12 = 1,500; E2 ≈ 2,500 (×25 calls) → **≈14,200**. Tier 2: 15 = 1,000; 16 = 2,000 + 700 rollouts; 17 = 3,000 + 700 rollouts + 400 bank-gen; MIPROv2 1,200 + 700; iso-cost 3,600 + 800 → **≈14,100**. Node: 2×A100-80GB, one vLLM replica per GPU. The program measured 985–1,380 episodes/hour on one replica for a 27B agent in this pipeline, so Tier 0 is ≈8 h and Tier 0+1 ≈17 h at two replicas; at the G5 floor of 400/hour aggregate, Tier 0+1 is ≈3.5 days. API: reflection ≈ 6 runs × ~60 calls, distillation ≈ 2×400 episodes × 2 formats, compiler and moderator labels — ≈ $40–80.

**ORDERED CONTINGENCY CUTS.** Tier 2 in the order 17 → iso-cost → MIPROv2 → 15 → 16; then Tier 1 in the order E2 decoding-seed replicate → 12 → 4 → 8 → 7 → 11 → E2 → 9–10. Tier 0 is never cut. Unrun arms are reported as unrun, never as nulls.

## Baselines and Ablations

**Baselines that could plausibly win and would refute us.**
(i) **I1×M1 retains the full I0 memory gain** (S ≈ 0; H2 fails) — complementarity. We report that memory and instruction optimization contribute independently and that the fixed-prompt comparison is unbiased.
(ii) **I0×M1 beats I0×C beyond the TOST margin** — per-instance retrieval carries value no static compilation holds; the compile recommendation dies even if S is high.
(iii) **I0×R ≈ I0×M1** — undistilled retrieved trajectories match the distilled bank; the memory system is a demonstration selector and the I1 advantage is about instruction content.
(iv) **I0×M_all ≈ I0×M1 while I0×C < I0×M1** — content presence, not retrieval or compilation, is doing the work; the paper becomes "dump the bank" rather than "compile it".
(v) **I2×M1 > max(I1×M1, I1×M0) by more than the MDE** — co-adaptation synergy; the coupling the track is named for is real and the substitution story is incomplete.
(vi) **S(B_touched) ≪ S(B)** — the substitution ratio was an exposure artifact.
(vii) **S differs by more than 0.2 between bank formats** — substitution is a property of the distillation style, not of procedural memory; the claim narrows to the format that shows it.
(viii) **No in-scope pairing clears G1** — memory has nothing to substitute on 27–32B agents in this environment; the paper becomes a four-pairing TOST report and says so.
(ix) **Memory growth dominating optimization at every iso-cost budget** — the practical payload is negative.

**Ablations that isolate the mechanism.**
- **I3 (length-padded I0)** removes only optimized content; exposes verbosity effects. Essential.
- **Equal-episode constraint with measured coverage and B_touched** — without it, a shrinking memory gain could mean the optimizer saw more data. Essential.
- **Token-matching of C and R to M1** — a compiled-arm tie cannot be dismissed as a budget difference.
- **M_all** — the third rung of the retrieval → compile → dump ladder.
- **B-dup positive control** — establishes the design can detect non-substitutable value; converts a null into a finding.
- **I2×M0 dependence test** — whether an instruction optimized with memory present silently depends on it.
- **Two bank formats (ExpeL, ReasoningBank-style)** — the result must not be an artifact of one distillation recipe.
- **Second optimizer (MIPROv2-style, Tier 2)** — the result must not be an artifact of GEPA's search procedure.
- **LoRA third container (Tier 2)** — the container the memory literature itself uses as a comparator; descriptive.
- **Shuffled-bank retrieval sanity check** — confirms retrieval is functioning in M1.
- **Two in-scope agents plus one out-of-scope scale check** — agent-relativity is a design axis, measured, not a limitation discovered afterwards.

## Falsifiable Predictions

1. **Substitution (primary).** On A1/E1, H1 holds (paired gain at I0 ≥6pt, McNemar p<.05) and H2 holds (paired gain at I1 within ±4pt by TOST), with the drop's sign consistent in ≥3 of 4 optimizer seeds; S ≥ 0.6 with the bootstrap CI excluding 0.3. On E2, same conjunction with S ≥ 0.7.
2. **Length.** I3 recovers <20% of I1's improvement over I0.
3. **Compilation.** I0×C is TOST-equivalent (±4) to I0×M1 at matched tokens on E1 and E2.
4. **Ladder.** I0×M_all is within 4pt of I0×M1 at bank size ≤400; if M_all falls below C by >4pt, dumping is not a substitute for compiling.
5. **Positive control.** On B-dup, S < 0.25 and I0×Cdup loses to I0×M1dup by ≥5pt.
6. **Moderator.** Residual memory gain at I1 is concentrated in the top decile of instance-to-bank similarity; the bottom 70% show a residual whose CI covers zero.
7. **Distillation.** I0×M1 exceeds I0×R by <3pt.
8. **Coupling.** I2×M1 ≤ max(I1×M1, I1×M0) + MDE (no synergy beyond either container), and I2×M0 < I1×M0 by ≥3pt (an instruction optimized with memory present depends on it).
9. **Coverage.** |S(B) − S(B_touched)| ≤ 0.15.
10. **Bank format.** At least one in-scope pairing clears G1 in screening, and |S(B) − S(B')| ≤ 0.2 at the core cells; if the ExpeL bank on Qwen3.5-27B is again within ±3pt of no memory, the ReasoningBank-style bank is the one that clears.
11. **Regimes.** On A2 (the losing pairing) the paired gain at I0 is within ±4pt (TOST) and S is not computed; on the gpt-oss-120b scale check the direction of S matches A1's.
12. **Iso-cost (Tier 2).** Instruction optimization reaches the full-memory accuracy at ≤ half the training-time call budget and at strictly lower per-episode inference cost.
13. **Third container (Tier 2, descriptive).** L×M1 − L×M0 is closer to the I1 contrast than to the I0 contrast, consistent with plain SFT retaining little of in-context gains; no claim is made from this arm.

**Refutation.** H2 failing with S < 0.3 on both E1 and E2 (CIs excluding 0.6) kills the substitution claim and vindicates the fixed-prompt comparison; we report that as the primary result. If the positive control also shows high substitution, the instrument is broken and the study is reported as uninterpretable. If I0×C loses to I0×M1 beyond the margin everywhere, memory's value is per-instance and prediction 3 is wrong even if S is high; the two are reported separately. If prediction 8's synergy clause fails, the track's coupling premise is supported and the abstract is rewritten around it. If prediction 10 fails because no pairing clears G1, the paper is the memory-null report.

## Measurement and Noise Control

Three variance sources handled separately, per this program's house rules.

**(a) Evaluation variance.** Every S_test instance runs under every cell with the same seed schedule; all comparisons are within-instance. Primary tests are exact McNemar on fix/break counts, Holm-corrected within pre-declared families: F-A {S components: cells 1,2,5,6}, F-B {ladder: 2 vs 3 vs 4 vs 8}, F-C {coupling: 9,10 vs 5,6}, F-D {controls: 7, 11, 12}. Every reported delta carries its fix/break decomposition; a symmetric-churn null is a different finding from an inert intervention. Equivalence claims use TOST via 90% instance-level bootstrap CI (10k resamples) within ±4pt; absence of significance is never reported as equivalence.

**(b) Optimizer variance.** 4 GEPA seeds on E1, 2 for I2, 2 on E2. Cell comparisons use a mixed-effects logistic model with test instance and optimizer run as crossed random effects; CIs from a cluster bootstrap resampling optimizer runs as well as instances. S is computed per seed and reported as a distribution, never as a single number.

**(c) Null replicates and the null floor.** Cells 1 and 2 are re-run at seed 37 (n=500); the treatment-free |Δ| distribution across seeds, plus cross-seed differences between optimizer runs of the same condition, defines the floor. No effect is claimed unless it exceeds both its test threshold and the 95th percentile of that floor. This program has observed 5–14pt re-scoring drift on small sets and a treatment-free replicate that mimicked the best real treatment.

**Minimum detectable effect (stated before running).** E1, n=1000 paired, expected discordance 15–20%: exact McNemar detects ≈3.5pt net swing at 80% power (α=.05) for a single cell pair. The I1-side memory gain averages 4 optimizer runs; with a between-run SD of ≈2.5pt (estimated from the earlier study's optimizer replicates) its SE is ≈1.8pt, and the difference between the I0-side and I1-side gains has SE ≈2.1pt, i.e. an MDE of ≈5.8pt for the *change* in memory gain. This is why the primary claim is the conjunction H1∧H2 rather than a point test on S: with a measured +7.7pt bank effect, S ≥ 0.6 implies an I1-side gain ≤3.1pt, which the ±4pt TOST margin can certify at n=1000, whereas a direct test of "S ≥ 0.6 vs S = 0.3" would sit at the MDE. S is reported with its CI as the effect size. E2 (n=274, MDE ≈6pt), A2 (n=500), the 8B-class LoRA arm, and the iso-cost curve (n=300, MDE ≈6pt) are directional. Sub-MDE differences are reported as inconclusive in either direction, and S is not computed in any environment that fails G1.

**Instrumentation per episode.** Tool calls, distinct documents, injected memory tokens, instruction tokens, prompt hash, seed, outcome; optimizer runs log per-rollout episode IDs (coverage), candidate lineage, and reflector inputs. A single script produces every table from the JSONL logs; nothing is hand-computed.

## Preprint Collision Check

**Method.** Fresh scan on 2026-09-03 (prior scan 2026-08-21): 15 HuggingFace Papers queries (244 unique papers, 44 dated ≥2026-06), by-id abstract verification for 54 arXiv IDs, and Claude server-side web search for targeted collision queries and for IDs not indexed on HF. Every ID cited here appears in `reference/litscan_2026-09-03.md` with title, date, verification channel and role. Semantic Scholar was reachable but rate-limited without a key; arXiv is unreachable from this node, so arXiv pages were confirmed through web search results only.

**Closest work: EvoAgentBench (arXiv 2607.05202, 2026-07-06).** Memento, ReasoningBank and GEPA evaluated on the same 528/267 training/test trajectories across four domains and three backbones. This is the three-way comparison v2 said did not exist; the sentence "no published work uses one as the control for the other" is withdrawn. What remains ours: the combined cells (I1×M1, I2×M1, I2×M0), token-matched compiled and raw arms, the whole-bank arm, the coverage-matched bank, the substitution ratio with paired statistics, and the positive control. EvoAgentBench's own headline — no automatic method is positive in every cell, and GEPA approaches the curated reference on one backbone — is consistent with our hypothesis and is cited as motivation.

**Nearest measurement object: Experience Distillation (arXiv 2607.21051).** "Retains ≥64.8% of the in-context gain" is the same ratio shape as S with weights as the second container. Our second container is an instruction: cheaper to serve, no gradient access, and — the risky part — testable at matched tokens against a compiled static block.

**Compile prediction is partially pre-empted in direction:** skills > Workflow Memory by 6.06pt matched (arXiv 2608.14036); single rewrite ≈ iterative refinement (arXiv 2606.30775); model-generated skills help on average and hurt 25% (arXiv 2605.23899). None compares against live per-instance retrieval from the same bank at matched tokens. Prediction 3 is therefore stated as a quantified equivalence, not as a surprise, and the whole-bank arm is added so the three rungs of the ladder are measured together.

**MemDelta (arXiv 2606.29914)** remains the direct methodological precedent for "the baseline is the confound"; its confound is inside the retrieval pipeline, ours is a rival container. **EvoMemBench (arXiv 2605.18421)** motivates M_all. **"Prompt Optimization Is a Coin Flip" (arXiv 2604.14585)** motivates gate G2 and the optimizer-failure branch. **TERMS-Bench (arXiv 2605.13909)** ran GEPA as a control for whether prompting saturates a benchmark — the same logical move in a different domain without memory. **MemAPO (arXiv 2603.21520)** couples memory into the optimizer (opposite direction). **TMEM (arXiv 2606.04536), experience internalization (arXiv 2606.04703) and arXiv 2603.18272** establish the parametric container and justify the LoRA arm.

**Correction to v2's check.** v2 retracted ActMem (2603.00026), MAS-PromptBench (2606.23664), TERMS-Bench (2605.13909), MemAPO (2603.21520) and StructMemEval (2602.11243) as unverifiable. All five exist; the August search failed, not the citations. They are reinstated with their actual roles (only TERMS-Bench and MemAPO bear on this proposal). The lesson is procedural and is now enforced: a citation is dropped only when a by-id lookup or an abs-page match fails on two independent channels.

**Appendices.** The pre-registered pilot that fixes the agent-screening logic and the gate threshold (design, gate log, deviation log, abstract, code: `reference/shortcutting_v4/`) and the scan records (`reference/litscan_2026-09-03.md`, `reference/litscan_raw/`) ship with this proposal so that the numbers quoted here can be checked rather than trusted.

**Residual risk.** ICLR 2027 submissions are not yet public; NeurIPS 2026 camera-readies may surface in October; a "GEPA + memory" ablation may exist in an appendix of a systems paper. The check will be re-run before the design freeze and again before submission; the scan records are committed.

## Risk Factors and Limitations

1. **Screening failure (G1).** If no in-scope pairing clears 6pt on S_dev, the bank is enriched once (more S_train episodes, larger k), screening is re-measured, and both measurements are published. If it still fails, the study stops and reports four TOST-equivalence results: on these agents and banks, memory has nothing to substitute. Given the program's prior null on one pairing, this is a live branch, not a formality.
2. **Optimizer failure (G2).** GEPA-style optimization may not beat I0 on this agent — a live risk given the coin-flip result. Branch: report I1 vs I0 as the prerequisite result; if I1 ≈ I0 in ≥2 of 4 seeds, the substitution question is moot for that agent and the paper's primary claim becomes the ladder (cells 2, 3, 8) plus the coupling cells.
3. **Lossy compilation.** C depends on the compiler prompt; fixed on S_dev, reported verbatim, treated as a lower bound. The whole-bank arm bounds it from the other side.
4. **Agent and bank specificity.** S is reported per agent and per bank format and never pooled. Two 27–32B dense agents and one out-of-scope MoE scale check bound the claim; generality beyond them is a stated limitation. The 8B-class check from v2 is dropped: no such weights are available locally and the network cannot fetch them.
5. **Positive-control artificiality.** B-dup is synthetic; the external episodic control was cut for budget. Stated, not hidden.
6. **Statistical reach.** The MDE for a change in memory gain is ≈5.8pt; the conjunction test is what makes the claim testable at a 6–8pt bank effect. S cannot be resolved to better than roughly ±0.2; small complementarities are inconclusive by design.
7. **Coverage control is partial.** B_touched matches which episodes the optimizer *touched*, not how much it learned from each; a reflector that reads 8 failure summaries per batch sees less than a distiller that reads every solved episode. This asymmetry is reported with the coverage statistics; it cannot be removed without changing what an optimizer is.
8. **Screening double-dips nothing but is itself a selection.** A1 is chosen on S_dev by the size of the memory effect; the primary test runs on S_test, so the selection cannot inflate S, but it does mean the headline is the *best-case* pairing for memory among four. The other three are reported next to it.
9. **Infrastructure.** 2×A100 (not 4); the compute node's root filesystem is non-persistent; runs are resumable and append-only; the frontier key may be unavailable, in which case the local reflector fallback is used and declared.
10. **No test-time self-editing (refused).** The track's title says self-editing memory; our banks are frozen after S_train. Substitution requires that both containers see identical episodes and that test instances stay paired; a bank that updates during evaluation gains exposure the instruction cannot match and introduces order effects that break pairing. We adopt ReasoningBank's distillation format and hold its update step fixed; the test-time-updating case is a different question (co-adaptation under drift) and is named as future work, not answered here.
11. **Scope.** Procedural experience memory in agent benchmarks with recurring task structure; nothing is claimed about episodic personal memory or long-conversation memory.

