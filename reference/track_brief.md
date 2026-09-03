# Title: Coupling Self-Editing Memory with Prompt Optimization in LLM Agents

## Keywords
LLM agents, agentic memory, prompt optimization, GEPA, instruction-demonstration decomposition, experience reuse, negative transfer, measurement methodology, ICLR

## TL;DR
Agent frameworks now bolt a self-editing memory onto a prompt optimizer and report gains, but nobody has established when the two interact constructively, when memory actively harms, or how large an effect has to be before it is distinguishable from run-to-run noise. This track looks for the sharp, falsifiable claim inside that space.

## Abstract
Two lines of work have converged without meeting. Prompt optimizers (MIPRO, GEPA and successors) treat a prompt as *instructions + demonstrations* and search over it with reflective or evolutionary updates. Agentic memory systems (ExpeL, Reflexion, ReasoningBank and 2026 successors) accumulate distilled experience across episodes and inject it at inference time. The obvious composition — let the optimizer own the instructions while a self-editing memory owns the demonstration slot — is largely unexamined, and the papers that do combine them report end-to-end wins without isolating which component produced them.

The prior work this track builds on produced several measured results that sharpen the problem, and any proposal here should treat them as the starting position rather than rediscover them:

- **Memory can be one-sidedly harmful.** In a controlled paired evaluation, injecting a full retrieved memory bank fixed **zero** items and broke six to seven (McNemar p=0.031 and p=0.016, replicated across independent runs). Noise scatters in both directions; this did not. The harm is a real phenomenon, not variance.
- **Injection volume, not memory content, was the causal lever.** Cutting injection from seven retrieved items to three eliminated the harm from the *same* bank. Restricting injection to a single reasoning stage did not help, so the mechanism is not "the wrong stage sees it".
- **Write-path repairs neutralized the harm but did not convert it to gain.** Contradiction-pruning and call-balance rebalancing of the bank moved the effect to indistinguishable-from-zero.
- **The optimizer's apparent gain was redistribution, not accuracy.** Prompt evolution fixed as many items as it broke; only the class-balanced metric moved. Evolving one module of a three-stage cascade was end-to-end useless.
- **Noise swallowed most claims.** Re-scoring the same candidate on the same held-out set moved the headline metric by 0.05–0.14. A null replicate with no treatment at all produced the same apparent "gain" as the best real treatment, which was enough to reject that treatment's own positive result.
- **The two components failed on disjoint slices.** The optimizer was strong where memory was weak and vice versa, which is the empirical reason to expect a coupling to be worth something.

Open questions this track should attack — a proposal should pick one and make it sharp, not survey them:

1. **Division of labour.** Is there a principled assignment of what instructions should carry versus what demonstrations/memory should carry, and does violating it predict the observed harm? What alternates, in what order, and does alternating optimization converge or oscillate?
2. **The injection budget as a first-class object.** If volume is the causal lever, the budget is a decision variable, not a hyperparameter. Can an agent decide *how much* retrieved experience to admit per step, and does a learned or calibrated budget dominate a fixed one?
3. **Predicting and preventing negative transfer.** Given a memory item and a query, can harm be predicted before injection? Retrieval scores are not obviously the right signal, since the harmful bank retrieved items that were topically correct.
4. **Co-adaptation and drift.** When the optimizer evolves instructions against a memory that is itself being rewritten, does the pair overfit to each other? What happens under distribution shift, and does a frozen-memory ablation expose it?
5. **Measurement standards for agent claims.** Much of the 2026 literature reports single-run deltas smaller than the noise floor measured here. A contribution could be a protocol — paired designs, null replicates, minimum detectable effect — plus a re-examination of published claims under it. This is a methods contribution and must be judged as one: it needs to overturn or qualify specific existing results to be interesting.

## In scope
- Domain-general agent benchmarks with public data: multi-hop QA, web/tool agents, code agents, interactive deduction, text games.
- Small open-weight models (7B–32B class), self-hosted, single node. The interesting result must not depend on frontier-scale models.
- Reuse and reimplementation of published memory and prompt-optimization methods as baselines.
- Negative or null results, provided the measurement is strong enough to make the null informative.

## Out of scope
- Any use of private, clinical, or patient data. The paper is domain-general; medical framing is explicitly excluded.
- Claims that require training or fine-tuning frontier models.
- "We combined method A and method B and the number went up" without isolating the mechanism — this is the specific failure mode to avoid.
- Benchmarks where the reported effect size would fall below the run-to-run noise of the setup.

## Resource constraints
One node with 4×A100 80GB, self-hosted inference on open-weight models up to ~32B. A frontier API model is available for the reflection/optimizer role and for judging, at a budget of a few hundred dollars total. Experiments must fit in days, not weeks: assume a few thousand evaluation episodes per configuration, and design the statistics around that rather than assuming a large held-out set. Public datasets only.
