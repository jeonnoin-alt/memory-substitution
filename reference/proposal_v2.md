# Proposal v2 — memory_or_instruction (score 6.97, BEST; from agent_memory_top4.json). THIS IS THE VERSION BEING EXECUTED.

> Note: the reviews that produced 6.97 were not persisted by ideate.py; only the score is known (score_history round 0).

## Name

memory_or_instruction

## Title

Is Your Agent's Memory Just an Un-Optimized Prompt? Measuring the Residual Value of Retrieved Experience After Instruction Optimization

## Short Hypothesis

Published agentic-memory gains are measured against a hand-written instruction. We hypothesize that for procedural experience memory (ExpeL/ReasoningBank-style), most of that gain is *substitutable*: when a reflective prompt optimizer is given exactly the same training episodes that built the memory bank, the memory-vs-no-memory gap collapses by at least 60%, and a frozen instruction compiled offline from the whole bank — with no retrieval at inference — matches per-instance top-k retrieval at matched injected tokens. The residual, non-substitutable value of memory is concentrated in instances with genuinely instance-specific reusable content, which we verify with a deliberately non-compilable positive-control bank where substitution must fail.

## Related Work

**(1) Procedural experience memory.** ExpeL (arXiv 2308.10144) "autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks" and at inference "recalls its extracted insights and past experiences." ReasoningBank (OpenReview jL7fwchScm, 2025) "distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences." Mem^p (arXiv 2508.06433), A-Mem (arXiv 2502.12110), and "Retrieval-Augmented LLM Agents: Learning to Learn from Experience" (arXiv 2603.18272) follow the same evaluation template: the memory-vs-no-memory delta is measured at a *fixed, hand-written* scaffold prompt, or against fine-tuning. That comparison silently assumes memory and instruction are non-substitutable containers.

**(2) Reflective prompt optimizers.** GEPA (arXiv 2507.19457, ICLR 2026 Oral) "samples trajectories and reflects on them to propose prompt updates," outperforming MIPROv2 by >10pp and GRPO by 6pp with up to 35× fewer rollouts. GEPA and ExpeL run the *same* learning principle — reflect on trajectories, distill natural-language lessons — and differ only in where the lesson is stored: folded into the instruction versus held in a retrieved store. No published work uses one as the control for the other.

**(3) The emerging "memory evaluation is confounded" literature.** MemDelta (arXiv 2606.29914) is the nearest work: it shows Mem0's 72.7 vs 61.4 win over verbatim RAG on LongMemEval-S reverses to a 1.2-point loss when only the embedding model is changed, and concludes that uncontrolled comparisons "conflate architectural memory with retrieval engineering, embedding quality, model-specific long-context behavior, and compute budget." "Diagnosing Retrieval vs. Utilization Bottlenecks" (arXiv 2603.02473) finds most memory failures stem from irrelevant retrieval rather than construction. Memory-R2 (arXiv 2605.21768) addresses an analogous fairness confound in RL credit assignment. All of these audit confounds *inside* the memory pipeline (retrieval quality, embeddings, credit assignment) while taking for granted that memory is the only container in which the training-episode information could have been placed.

**(4) Three-way comparisons in the wild.** EvoClinician (arXiv 2601.22964) is the only retrieved paper that lists "prompt optimization agent" as a baseline category alongside "memory agent," with memory baselines defined as those that "keep the prompt fixed but add long-term memory across episodes." It is a clinical application paper; the three-way comparison is a baseline table, not a hypothesis, and it does not equalize training episodes, match injected tokens, compile a bank into an instruction, or measure residual gain.

**Our position.** The missing accounting is: a memory bank and an optimized instruction are two containers for the same training-episode information, and the field has never measured how much of the first container's value survives when the second is filled first, at matched information and matched cost. MemDelta establishes that the memory literature's baselines are confounded; it does not identify instruction optimization as a competing mechanism, and it makes no prediction that retrieval can be replaced by a frozen compiled prompt. That prediction is ours and it is the risky part.

## Abstract

Agentic memory systems are evaluated by comparing an agent with a retrieved-experience bank against the same agent without one, holding a hand-written scaffold prompt fixed. Recent audits (MemDelta) show such comparisons are confounded by retrieval engineering; we identify a different and sharper confound. A memory bank distilled from training episodes and an instruction optimized on those *same* episodes are two containers for the same information, and the second is dramatically cheaper to serve — one prompt paid once, versus retrieved tokens paid every episode. We test substitution directly. Holding the agent, tools, retriever, training split and evaluation fixed, we build (i) an ExpeL-style bank with per-instance top-k retrieval, (ii) an instruction optimized by GEPA that never sees the bank, and (iii) a frozen instruction compiled offline from the whole bank with no retrieval at all, token-matched per instance to (i). The primary endpoint is the substitution ratio S: the fraction of memory's paired gain over no-memory at the hand-written instruction that disappears at the optimized instruction. We predict S ≥ 0.6 on a tool-augmented multi-hop QA agent and ≥ 0.7 on ALFWorld, and we predict the compiled static arm comes within 2 points of live retrieval. A deliberately non-compilable positive-control bank, seeded with near-duplicates of held-out instances, must show S < 0.25 — so a null on the main benchmarks is a finding rather than a power failure. The study is scoped to one primary environment (n=600 paired instances, 3 optimizer seeds), one replication environment, and ~30,000 evaluation episodes, with instance-paired McNemar tests, crossed random effects for optimizer seed, null replicates, and a stated minimum detectable effect.

## Experiments

**HELD FIXED THROUGHOUT.** Agent scaffold (ReAct), tool stack, step limit, retriever and similarity function, decoding temperature and seed schedule, the training split from which *all* learned artifacts derive, and the held-out test split. Only the instruction and the memory-injection variant differ. The fairness constraint that makes the study interpretable: the memory bank and the prompt optimizer see exactly the same training episodes, so they differ only in the container, not in the information they were allowed to see.

**MODEL.** Qwen2.5-14B-Instruct is the single load-bearing agent, served with vLLM (two TP=2 replicas on the 4×A100 node). Llama-3.1-8B-Instruct runs a reduced moderation check only. Qwen3-32B is **cut**. A frontier API model is the GEPA reflector, the ExpeL distiller, and the offline compiler, used identically across conditions. Scoring is programmatic (normalized EM/F1 for QA, ALFWorld task success), so no LLM judge is on the critical path.

**ENVIRONMENTS.** *E1 (primary, carries all quantitative claims):* tool-augmented multi-hop QA over a Wikipedia search tool, test pool = 600 held-out instances (360 HotpotQA-distractor, 240 MuSiQue), ~6 LLM calls/episode. *E2 (replication):* ALFWorld, all 274 eval tasks (134 unseen reported separately), ~25 calls/episode; chosen because task templates recur across train and test, so procedural memory is maximally compilable and the substitution prediction is at its most exposed. **WebShop is cut. The LoCoMo episodic-memory control is cut.**

**ARTIFACTS (built once, then frozen).**
- **B**: ExpeL-style bank over 500 E1 / 200 E2 training episodes — distilled insights plus condensed trajectories; deployed with top-k=7 dense retrieval.
- **I1**: GEPA run on the same training split with **no** memory in context, 300 rollouts per run, 3 seeds (E1) / 2 seeds (E2).
- **I3**: hand-written instruction padded with task-generic boilerplate to I1's token length (length control).
- **C**: frontier model reads the entire bank offline and compiles it into one static instruction block, token-matched per instance to what top-k=7 injects; no retrieval at inference. A frozen measurement instrument, not a proposed method.
- **R**: raw few-shot arm (**new, per review**): the same retrieval over the *undistilled* training trajectories, injected verbatim as demonstrations, token-matched to M1. This separates "value of ExpeL-style distillation" from "value of any exposure to training episodes."
- **I2 (optimize-with-memory-in-context) is cut**: it tests co-adaptation, not substitution, and does not carry the claim.

**PRECHECK GATE.** On a 150-instance dev split, the bank must produce a paired gain over no-memory at the hand-written instruction of **≥10 accuracy points** (a size routinely reported by ExpeL/ReasoningBank-class systems). S is undefined when the denominator is small; a bank that fails is enriched (more training episodes, better distillation) until it passes, and the precheck numbers are reported either way. The gate is set at 10 rather than 8 because with 3 optimizer seeds the design detects a ~5.6-point change in the memory gain (see Measurement), so the predicted drop must be ≥6 points to be testable.

**E1 CONDITION GRID — 7 cells, fully instance-paired.**
| # | Cell | Purpose |
|---|---|---|
| 1 | I0×M0 | no-memory baseline |
| 2 | I0×M1 | the standard memory-paper comparison (denominator of S) |
| 3 | I0×M2 | compiled static, token-matched — does retrieval buy anything? |
| 4 | I0×M3 (raw few-shot R) | distillation vs. raw exemplars |
| 5 | I1×M0 | optimized instruction alone |
| 6 | I1×M1 | numerator of S: what memory adds on top |
| 7 | I3×M0 | length control |

**PRIMARY ENDPOINT.** S = 1 − [acc(I1×M1) − acc(I1×M0)] / [acc(I0×M1) − acc(I0×M0)], computed per optimizer seed, reported as a distribution with a cluster-bootstrap CI. Every cell also reports its paired fix/break decomposition against I0×M0.

**SECONDARY ENDPOINTS.** (a) *Compilation sufficiency*: I0×M2 vs I0×M1 at matched injected tokens. (b) *Distillation value*: I0×M1 vs I0×M3. (c) *Residual complementarity*: I1×M1 vs max(I1×M0, I0×M1). (d) *Optimizer generality*: MIPROv2 substituted for GEPA, 2 seeds, cells I1'×M0 and I1'×M1 only, on a fixed 300-instance subsample, 1 decoding seed.

**POSITIVE CONTROL (load-bearing).** A second bank **B-dup** seeded with distilled trajectories for training instances that are deliberately near-duplicates of specific held-out test instances (paraphrased test questions, disjoint from the instances used for optimization). Its value is instance-specific and provably cannot be compressed into a bounded static instruction. Cells on a 300-instance subset: I0×M1dup, I0×M2dup, I1×M1dup (reusing the already-built I1 instructions — no new optimizer runs needed, since I1 never sees any bank). I0×M0 and I1×M0 are read off the main grid.

**ISO-COST CURVE (shrunk to 3 points).** Instrument every LLM call. Held-out accuracy (n=300, 1 decoding seed) versus total *training-time* call budget at three points spanning ~250 / ~900 / ~2500 calls, for two strategies: grow the bank (more distilled training episodes, retrieval fixed) vs. run more GEPA rollouts with no memory. 2 seeds per point; the top point of each curve is the existing I0×M1 and I1×M0 cells. Report the crossover budget and the *inference-time* cost per episode, since retrieval is paid every episode and an instruction is paid once.

**MODERATOR ANALYSIS (free — reuses existing runs).** For each test instance, compute max similarity to any bank item (dense score plus an LLM label "does this item contain instance-specific reusable content", human-validated on 100 cases with reported κ). Fit per-instance residual memory gain at I1 against this similarity.

**8B MODERATION CHECK.** Cells 1, 2, 5, 6 only, n=300, 1 decoding seed, 2 optimizer seeds, on Llama-3.1-8B. Tests risk factor (4): a small model may fail to follow a long optimized instruction while still using concrete exemplars, which would lower S at 8B.

**E2 (ALFWorld) CELLS.** I0×M0, I0×M1, I0×M2, I1×M0, I1×M1; 2 optimizer seeds; 2 decoding seeds for the two I0 cells (to supply the null replicate), 1 elsewhere.

**COMPUTE ARITHMETIC (the reason this fits).**
E1, Qwen-14B: fixed-instruction cells 1,2,3,4,7 = 5 × 600 × 2 decoding seeds = 6,000 episodes; optimizer-dependent cells 5,6 = 2 × 3 seeds × 600 × 2 = 7,200; MIPROv2 check = 2 × 2 × 300 = 1,200; positive control = 3,000; GEPA/MIPRO search rollouts = 3×300 + 2×300 = 1,500; bank + B-dup construction = 800; iso-cost eval = 3,000, iso-cost training = 800. **E1 total ≈ 23,500 episodes × ~6 calls ≈ 141k LLM calls.**
E2, ALFWorld: eval = 2×274×2 + 274 + 2×2×274 = 2,466; optimizer rollouts = 2×200 = 400; bank = 200. **E2 total ≈ 3,066 episodes × ~25 calls ≈ 77k calls.**
8B moderation: 1,800 eval + 600 rollouts = 2,400 episodes ≈ 14k calls (on the cheaper model).
**Grand total ≈ 29,000 episodes / ~230k LLM calls.** At vLLM aggregate throughput on 4×A100 (two TP=2 replicas, high concurrency), this is ~3–4 days of wall clock, i.e. "days, not weeks," and ≤ 6,000 episodes per reported configuration.
**API budget:** ~9 optimizer runs × ~60 reflection calls (~8k in / 1k out) ≈ 4.5M input / 0.6M output ≈ $12; distillation of 900 training episodes ≈ $8; compiler and moderator labeling ≈ $10. **Total ≈ $30–60**, far under the few-hundred-dollar cap, because scoring is programmatic.
**Ordered contingency cuts if we overrun:** iso-cost curve → 2 points; 8B moderation arm; MIPROv2 generality check; E2 decoding-seed replicate. The 7-cell E1 grid and the positive control are never cut — they are the claim.

## Baselines and Ablations

**BASELINES THAT COULD PLAUSIBLY WIN AND WOULD REFUTE US.**
(i) **I1×M1 retaining the full I0 memory gain** (S ≈ 0) — the complementarity outcome, and the most likely way the hypothesis dies. We would report that memory and instruction optimization contribute independently and that the memory literature's fixed-prompt comparison is unbiased.
(ii) **I0×M1 ≫ I0×M2** on the main benchmarks — per-instance retrieval carrying value no static compilation can hold, which would kill the "compile, don't retrieve" recommendation even if S is high.
(iii) **I0×M3 (raw few-shot) ≈ I0×M1** — added at reviewer request. If undistilled retrieved trajectories match the ExpeL bank, then the "memory system" is a demonstration selector and any I1 advantage is about instruction content, not about beating distillation. This baseline separates "value of distillation" from "value of any exposure to training episodes at all," and is a genuine threat to the framing.
(iv) **Memory growth dominating optimization at every iso-cost budget** — makes the practical payload negative.

**ABLATIONS THAT ISOLATE THE MECHANISM.**
- **I3, length-padded hand-written instruction** — holds prompt length fixed and removes only the optimized *content*, exposing any I1 advantage that is mere verbosity. Essential.
- **Equal-training-episode constraint** — without it, a shrinking memory gain could just mean the optimizer saw more data. Essential.
- **Token-matching of C and R to M1** — a compiled-arm tie cannot be dismissed as a budget difference.
- **Non-compilable positive-control bank (B-dup)** — establishes that the design *can* detect non-substitutable memory value. This is what converts a null into a finding.
- **Second optimizer (MIPROv2)** — the substitution result must not be an artifact of GEPA's search procedure.
- **Shuffled-bank retrieval sanity check** — confirms retrieval is functioning in M1.

## Falsifiable Predictions

1. **S ≥ 0.6 on E1 and ≥ 0.7 on E2**: memory's paired gain over no-memory falls from ≥10 points at the hand-written instruction to <4 points at the optimized instruction, consistent in direction across all 3 optimizer seeds, with the bootstrap CI on S excluding 0.3.
2. **I3 recovers <20% of I1's improvement over I0** — the effect is optimized content, not prompt length.
3. **I0×M2 (frozen compiled instruction, no retrieval) comes within 2 points of I0×M1 at matched injected tokens** on both E1 and E2. This is the risky, non-obvious prediction: per-instance retrieval of procedural experience is nearly worthless once the same experience is compiled once, offline.
4. **On the near-duplicate positive control, S < 0.25 and I0×M2dup loses to I0×M1dup by ≥5 points** — the instrument detects non-substitutable value where it truly exists.
5. **Residual memory gain at I1 is concentrated in the top decile of instance-to-bank similarity**, with the bottom 70% of instances showing a residual gain whose CI covers zero.
6. **Iso-cost:** instruction optimization reaches the accuracy of the full memory system at ≤ half the training-time LLM-call budget, and at strictly lower per-episode inference cost.
7. **Distillation is not the load-bearing part:** I0×M1 exceeds I0×M3 by <3 points, i.e. the ExpeL write path buys little over raw retrieved trajectories at matched tokens.

**REFUTATION.** S < 0.3 on both E1 and E2 with CIs excluding 0.6 kills the substitution claim and vindicates the memory literature's fixed-prompt comparison; we report that as the primary result. If the positive control *also* shows high substitution, the measurement is broken rather than the hypothesis confirmed, and the study is reported as uninterpretable. If I0×M2 loses badly to I0×M1 everywhere, memory's value is genuinely per-instance and prediction 3 is wrong even if S is high — we report the two predictions separately and do not let one carry the other.

## Measurement and Noise Control

Three variance sources handled separately.

**(a) Evaluation variance.** Every held-out instance is run under every cell with the same seed schedule, so all comparisons are within-instance. Primary tests are exact McNemar tests on fix/break counts with Holm correction across the cell family. Every reported delta carries its fix/break decomposition, because a null net delta hiding symmetric churn is a different finding from an inert intervention.

**(b) Optimizer variance — the source most often ignored.** 3 independent GEPA seeds on E1, 2 on E2. Cell comparisons use a mixed-effects logistic model with test instance and optimizer run as crossed random effects; CIs come from a cluster bootstrap resampling optimizer runs as well as instances. S is computed per optimizer seed and reported as a distribution, never as a single number.

**(c) Null replicates.** For each environment we re-run an identical cell under a different decoding seed and report the distribution of apparent deltas, and separately compare two optimizer seeds of the same condition to each other. No effect is claimed unless it exceeds the 95th percentile of the corresponding null distribution. This is load-bearing given prior observations of 5–14 point re-scoring drift on small held-out sets and a treatment-free replicate that mimicked the best real treatment.

**Minimum detectable effect.** E1, n=600 paired instances, expected 12–18% discordant-pair rate: McNemar detects a ~4-point net swing at 80% power (α=0.05) for any single cell pair. S is a ratio of two paired differences; the numerator is averaged over 3 optimizer seeds, so its standard error is √(1.4² + 2.5²/3) ≈ 2.0 points (using a 2–3 point between-run SD estimated from the null optimizer replicates), giving ~5.6 points of detectable change in the memory gain. This is exactly why the precheck gate is 10 points (not 8) and why prediction 1 is framed as "from ≥10 down to <4": the predicted drop of ≥6 points sits above the MDE. E2 (n=274, MDE ~6 points) is directional replication; the 8B arm and iso-cost curve (n=300, MDE ~6 points) likewise. Sub-MDE differences are reported as inconclusive in either direction, and we will not compute S in any environment that fails the precheck.

## Preprint Collision Check

**Closest work found in the current search: MemDelta — "Controlled Baselines and Hidden Confounds in Agent Memory Evaluation" (arXiv 2606.29914, 2026).** It is a measurement paper making the same *genus* of argument: that headline agent-memory gains are artifacts of uncontrolled baselines. It shows Mem0's apparent 72.7-vs-61.4 win over verbatim RAG on LongMemEval-S reverses to a 1.2-point loss when only the embedding model changes, and warns that comparisons "conflate architectural memory with retrieval engineering, embedding quality, model-specific long-context behavior, and compute budget." **Partial collision on framing, none on claim.** MemDelta's confound is *inside* the retrieval pipeline; ours is a rival mechanism outside it. MemDelta does not run a prompt optimizer, does not equalize training episodes across containers, does not compile a bank into a frozen instruction, does not report a residual-gain ratio, and makes no prediction that retrieval can be deleted. We will cite it as the direct methodological precedent and state plainly that our contribution is the *specific* substitution mechanism plus the compilation prediction, not the general "memory baselines are confounded" thesis, which is now MemDelta's.

**EvoClinician (arXiv 2601.22964, 2026)** is the only retrieved paper that puts "prompt optimization agent" and "memory agent" in the same baseline table, defining memory baselines as those that "keep the prompt fixed but add long-term memory across episodes." This shows the three-way comparison is beginning to appear as a design pattern. It does not collide: it is a clinical application paper (a domain this track excludes), the comparison is a baseline table rather than a hypothesis, and it does not match training episodes, match injected tokens, or measure a residual.

**GEPA (arXiv 2507.19457)** is our optimizer, not a competitor; it has not been used as a control to isolate memory's residual value. **ExpeL (2308.10144), ReasoningBank (OpenReview jL7fwchScm), Mem^p (2508.06433), A-Mem (2502.12110), and arXiv 2603.18272** are the targets of the hypothesis and all evaluate against no-memory or fine-tuning, not against an optimized instruction. **Diagnosing Retrieval vs. Utilization Bottlenecks (2603.02473)** and **Memory-R2 (2605.21768)** audit different confounds (retrieval relevance, RL credit assignment) and take memory's baseline value for granted.

**Correction to the previous version of this check.** The earlier draft cited ActMem (2603.00026), MAS-PromptBench (2606.23664), TERMS-Bench (2605.13909), MemAPO (2603.21520), and "Evaluating Memory Structure in LLM Agents" (2602.11243). **None of these were returned by the current literature search and I cannot verify them; I have removed all reliance on them and do not use them to establish novelty.** One reviewer flagged TERMS-Bench (a GEPA-based substitution test for an architectural intervention in negotiation agents) as the closest structural precedent. If that work exists as described, it is a precedent for the *logical move* — use a prompt optimizer as the control for a non-prompt intervention — in a different domain, and I would cite it as such; our contribution would then rest on the memory-specific measurement object (the substitution ratio with a matched-information constraint), the compiled-static instrument, the non-compilable positive control, and the iso-cost accounting, none of which transfer automatically.

**Residual risk.** I could not sweep OpenReview 2026 submissions, and a "memory + prompt optimizer" ablation may exist in an appendix of a combined-system preprint. Given MemDelta's existence, the confound-auditing framing is no longer novel on its own; we therefore lead with the mechanism claim (instruction optimization substitutes for procedural memory; frozen compilation replaces retrieval) rather than with the methodology.

## Risk Factors and Limitations

1. **Precheck failure.** If a bank does not clear the 10-point gate, S is unstable and we report that environment as excluded with its numbers rather than dividing by a small denominator. Given MemDelta's findings, a bank failing the gate is itself a reportable observation about the literature.
2. **Optimizer failure.** GEPA may not beat the hand-written instruction on some environment, collapsing the study to "no optimization, no substitution." Mitigated by the MIPROv2 arm and by reporting I1-vs-I0 as a prerequisite result.
3. **Lossy compilation.** The compiled arm depends on the compiler prompt, which we fix in advance on a 100-instance dev split, report verbatim, and treat as a *lower bound* on what static compilation can achieve. A tie with retrieval is therefore conservative; a loss is weaker evidence against prediction 3 than a tie is for it.
4. **Model specificity.** S may be lower at 8B (small models may follow long instructions poorly while still using concrete exemplars) — reported per model, never pooled. With one load-bearing model, generality is a stated limitation, not a claim.
5. **Artificiality of the positive control.** The near-duplicate bank is synthetic; the external episodic-memory control (LoCoMo) was cut for budget, so the only evidence that the instrument detects non-substitutable value is the synthetic one. We state this explicitly rather than hiding it.
6. **Statistical reach.** With 3 optimizer seeds and n=600, the design detects a ~5.6-point change in the memory gain. It cannot resolve S to better than roughly ±0.2 and it cannot adjudicate small complementarities; E2, the 8B arm, and the iso-cost curve are directional only. We will not report sub-MDE differences as results.
7. **Iso-cost indicativeness.** The curve depends on implementation efficiency of both pipelines; we report raw call counts, token counts and wall clock so readers can re-weight.
8. **Scope of the claim.** This is about *procedural* experience memory in agent benchmarks with recurring task structure. It says nothing about episodic personal memory or long-conversation memory, and we will not generalize to them.

