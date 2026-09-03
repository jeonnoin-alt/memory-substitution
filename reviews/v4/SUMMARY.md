# v4 harness judging — 2026-09-03

Method: HANDOFF §Judging — REVIEW_SYSTEM/SCHEMA/USER verbatim from `ideate.py` (venue "ICLR 2027 main track"), three independent
general-purpose subagents (model sonnet) reading `tools/judge_prompt_v4.md`, aggregated by `tools/aggregate_reviews.py`
(SCORE_WEIGHTS, worst-verdict-wins). Harness-substrate scores are comparable in objection content, only indicatively in absolute value.

## Aggregate
**6.02 — borderline** (nov 5.3 / sig 6.0 / snd 7.0 / fea 5.0 / cla 6.7; n=3). Per reviewer: R1 6/7/7/6/8, R2 5/6/7/5/6, R3 5/5/7/4/6.
Lineage for reference (API-substrate): v1 6.73 → v2 6.97 → v3 5.73. Proposal ①'s harness re-review scored 6.42 vs its API 6.40, so harness ≈ API in that one calibration point.

## Unanimous objections (3/3)
1. **Scope violation — primary agent gpt-oss-120b is outside the track's 7B–32B envelope**, and the in-scope agent (Qwen3.5-27B) is pre-registered as the degenerate regime where S is not computed. All three call this the strongest objection; R2/R3 read it as "reaching for the agent that produces the effect". Verdict: correct. My design error in v4 §7.
2. **Missing baseline: a ReasoningBank-style bank** (self-judged successes AND failures) — the format EvoAgentBench actually evaluates and reports ≈+7pt on Qwen backbones. Without it the substitution result may be specific to ExpeL-style distillation and cannot be cross-read against the closest prior work.
3. **Closest work = EvoAgentBench**, novelty is "instrumentation upgrade on a published table" (nov 5–6). Not disputed; the remaining novelty is the combined cells, token matching, S with paired stats, positive control.

## Non-unanimous
- Scope too large for "days, not weeks" on 2 GPUs; commit to a guaranteed minimal core (R1, R2).
- Add a genuinely self-editing (test-time updating) memory since the track says "Self-Editing Memory" (R3).
- Cite the internal pilot (proposal ①) and litscan as verifiable appendices, not unpublished context (R3).
- Collision check praised by all three; R1/R3 note it is self-reported and that an appendix ablation in a systems paper could still hold the I1×M1 cell.

## Decisions for v4.1
| Objection | Answer |
|---|---|
| 120B out of scope | Primary grid moves to an in-scope agent. Pre-registered **screening stage** on S_dev over {Qwen3.5-27B, Qwen3-32B} × {ExpeL bank, ReasoningBank-style bank}; the pairing with the largest paired gain ≥ gate becomes A1; every screening number is published. gpt-oss-120b demoted to a Tier-2 out-of-scope scale check, never load-bearing. |
| ReasoningBank-style bank | Added as bank type B_rb (self-judged success+failure distillation, retrieval identical). Screening decides which bank is primary; the other runs at the core cells only. |
| Self-editing at test time | Refused with reasons: substitution requires a frozen artifact so both containers see identical episodes and instances stay paired; test-time writes give memory exposure the instruction cannot match and introduce order effects. ReasoningBank's *distillation format* is adopted; its online update is held after S_train. Stated in Risk Factors. |
| Scope | Explicit tiers: Tier 0 (must ship) = cells 1,2,5,6 + C + positive control + nulls; Tier 1 = M_all, I2, B_touched, I3, R, E2; Tier 2 = LoRA, MIPROv2, iso-cost, 120B, A-degenerate. |
| Pilot as appendix | `reference/shortcutting_v4/` (DESIGN, gate log, abstract) and `reference/litscan_2026-09-03.md` named as appendices in the text. |
