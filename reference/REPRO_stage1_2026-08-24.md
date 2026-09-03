# Stage 1 — 재현 (context reproduction), 제안 ③ decorative_retriever

Date: 2026-08-24. Source of truth: the four JSON files below, read directly (not the HANDOFF summary).
No literature scan, no v4 text, no experiment code has been written yet. Stages 2–3 not started.

## 1. Lineage verified against the stored artifacts

| Ver | Name / Title | Where | Score | Means (nov/sig/sou/fea/cla) | Verdict |
|---|---|---|---|---|---|
| v1 | `memory_or_instruction` — "Is Your Agent's Memory Just an Un-Optimized Prompt?" | `ideas/agent_memory_v2.json` (+ `_reviews.json`) | round0 **6.73** → round1 final **6.70** | 6.0/7.0/7.0/6.5/7.5 (final, n=2) | borderline |
| v2 | same Name/Title, scoped | `ideas/agent_memory_top4.json` | **6.97** (top4 round 0) | not stored per-round | — |
| v3 | `decorative_retriever` — "When Is a Retriever Decorative?" | `ideas/agent_memory_top4_reviews.json` `scored[]` | **5.73** | 5.3/5.7/6.3/5.0/6.3 (n=3) | borderline |

`agent_memory_top4_reviews.json:score_history` = round0 `[7.03, 6.60, 6.97, 6.50]` → round1 `[6.22, 6.25, 6.65, 6.78]` → round2 `[6.40, 5.67, 5.73, 6.77]`,
in the order `[memory_induced_shortcutting, memory_item_value_reliability, memory_or_instruction→decorative_retriever, memory_budget_confound]`.
**The HANDOFF's 6.73 → 6.97 → 5.73 is confirmed.** Note the whole cohort fell in round 1–2 except idea #4; only ③ fell below 6.

### Artifact-integrity findings (new, not in the HANDOFF)
- **v2's reviews (the 6.97 ones) are not stored anywhere.** `ideate.py` keeps only the final round's reviews in `scored[]`; `score_history` keeps numbers only. The two v2-era objections in the HANDOFF (fairness constraint / I2) are recoverable **only** from the v1-era reviews in `agent_memory_v2_reviews.json`, where they appear verbatim (R1 = I2-is-self-serving, R2 = fairness-not-enforced). They are therefore v1→v2 objections that v2 answered *partially* (v2 cut I2 outright and never instrumented GEPA coverage) — the HANDOFF's framing is right in substance, off by one round in provenance.
- **v3's `changes_made` field is truncated mid-word** in both `agent_memory_top4_reviews.json` and `..._ranked.json` (5,223 chars, ends `"...the compile-from-raw arm M4 (subs"`). This is the `max_tokens` truncation failure mode documented in `HANDOFF.md §0`. The last ~1 paragraph of v3's self-justification is unrecoverable; everything cited below is from the intact part.
- A third v1-era objection the HANDOFF omits: **a LoRA fine-tuning arm as a third container** for the same training episodes (v1 R2's `missing_baseline`), motivated by v1's own Related Work saying memory papers are compared against fine-tuning. v4 must either include it or refuse it with reasons.

## 2. What each version actually claims

**v1/v2 (substitution).** Bank B and instruction I are two containers for the *same* training episodes; published memory gains are measured with the instruction container empty. Primary endpoint S = 1 − [acc(I1×M1) − acc(I1×M0)] / [acc(I0×M1) − acc(I0×M0)], per optimizer seed. Artifacts B (ExpeL, top-k=7), I1 (GEPA, no memory in context, 300 rollouts × 3 seeds), I3 (length-padded control), C (offline whole-bank compilation, token-matched), R (raw few-shot). v2 cut Qwen3-32B, WebShop, LoCoMo and I2; added R and the 10-point precheck gate (raised from 8 because MDE ≈ 5.6 pt with 3 seeds). ~29,000 episodes / ~230k calls / ~$30–60 API.

**v3 (the pivot).** Every optimizer arm dropped. Primary arm A_fix = the k dev-most-retrieved items, **verbatim, identical for every query** — no frontier model anywhere in the primary comparison. Primary endpoint R_fix = acc(A_ret) − acc(A_fix). "The law": O = mean pairwise Jaccard of top-k sets, computed from the retriever alone with zero rollouts, predicts R_fix **out of sample** (leave-one-cell-out vs. grand-mean predictor, permutation null, ~20 cells spanning O ∈ [0.05, 1.0]). Four overlap knobs: task-family breadth, bank size N, retriever (dense/BM25/MMR), k. Banks B_expel(N∈{100,250,500,1000}), B_rbank(500), B_raw(500), B_offdomain(500), B-dup (paraphrase near-duplicates = low-overlap anchor). Arms A0/A_ret/A_fix/A_rand/A_comp/A_scram/A_mmr. Gates G1 (each bank ≥8 pt over A0), G2 (B-dup R_fix ≥10 else uninterpretable), G3 (dial must span O). ~23,100 episodes / ~176k calls / ~$50. Secondary payload: reinterpret ReasoningBank's 49.7%@k=1 → 44.4%@k=4 as a redundancy artifact, with an MMR cell that makes an **opposite-sign** prediction to the interference account of arXiv:2606.29824.

## 3. Why v3 lost 1.24 points — verified from the three stored reviews

Scores: R1 5/5/7/4/7, R2 5/6/7/5/6, R3 6/6/5/6/6. Soundness held (7/7/5); **novelty (5.3) and significance (5.7) are what fell**, plus feasibility 5.0.

All three `strongest_objection` fields say the same thing, unprompted and independently:
- **R1:** "the track is explicitly framed around coupling … this proposal deliberately runs zero optimizer arms … a track-focused AC could reasonably judge this out of scope regardless of its internal rigor."
- **R2:** "it does not address 'coupling' at all … a program committee reading against the call would likely see this as a scope mismatch rather than a sharpened instance of the assigned problem."
- **R3:** "treats a single frontier-model, non-iterated compilation (A_comp) as a 'lower bound' … an assumption that is never tested … the paper's claim to be a 'service to the track' … is undercut by never checking whether coupling helps where the naive compiled arm ties with retrieval."

R3's is the sharpest and the HANDOFF under-states it: the objection is not merely "no optimizer" but that **v3's central defense — A_comp is a lower bound on the instruction container — is an untested assumption**. v3's Risk#7 asserts it; nothing measures it.

Second, shared novelty objection (all three `closest_prior_work`): **arXiv:2511.21730** ("A Benchmark for Procedural Memory Retrieval in Language Agents") is conceded by v3 itself as a "real partial collision", and v3 quotes its own search verdict saying the *direction* is converging across 2511.21730 / 2602.02751 / 2606.23127. All three reviewers turned that concession into the novelty deduction: "a fair but narrow novelty wedge" (R2), "a real but narrow gap" (R3).

Third, all three `preprint_collision` fields flag the same thing: the check is commendably self-critical **but** it admits an earlier draft cited unverifiable arXiv IDs, and the surviving citations are "2026 IDs with suspiciously tidy supporting quotes that cannot be independently checked here" (R2). The honesty was read as a *reliability signal against the proposal*.

`what_would_fix_it` / `missing_baseline`, deduped:
1. One real optimizer cell (GEPA-lite, fixed rollout budget) at a high-overlap and a low-overlap cell — does optimization *move the overlap threshold*? (R1, R2, R3 — unanimous, and R3 wants it iterating on the compiled instruction specifically)
2. **Stuff-the-whole-bank-in-context, unretrieved and uncompiled**, feasible at N=100 — separates "the compiler does the work" from "the content just needs to be present" (R2). This arm exists nowhere in v3.
3. Hierarchical/mixed-effects pooling for the ~20-cell regression, with bank and environment random effects, because cells share banks/environments and are not independent draws (R3).

## 4. The lineage's lesson, stated for v4

v2 → v3 was **over-compliance**: v3 answered "the compiler is doing the work" (a real objection) by deleting the entire optimizer half, which was the track's subject. It bought soundness it already had and paid in novelty, significance and scope. v3's own `changes_made` documents refusing three reviewer requests with reasons (narrow the title; add AFTER; independently verify preprints) — and none of those refusals cost it points. **Refusing with reasons was never the problem; obeying in the wrong direction was.**

## 5. Environment reality check (deviations from the HANDOFF, 2026-08-24 09:04 UTC)

| HANDOFF says | Actual |
|---|---|
| 4×A100-80GB | **2×A100-80GB visible**, both 0 MiB used, idle |
| keepalive may be running | `pgrep -af gpu_keepalive` → nothing |
| keys at `/home/work/.anthropic_env` (chmod 600) | **file does not exist** — `/home/work` root was recycled as warned; key must be re-provisioned by the PI |
| credits exhausted until 2026-09-01 00:00 UTC | 8 days out; harness-substrate judging (§Judging) is the only review path until then |
| coordinate with proposal ① on the node | ① has written `experiments/shortcutting_v4/DESIGN.md` but **no experiment code exists yet** (its own header says so) and nothing is running — the node is free today |

`/home/work/neuro` (NFS) holds the repo and survives; nothing else does.

## 6. Files read for this reproduction

`ai_scientist/ideas/agent_memory_v2.json`, `agent_memory_v2_reviews.json`, `agent_memory_top4.json`, `agent_memory_top4_reviews.json`, `agent_memory_top4_ranked.json`, `agent_memory_top4_report.md`, `agent_memory_optimizer.md`, `ideate.py` (REVIEW_SYSTEM / REVIEW_SCHEMA / REVIEW_USER / SCORE_WEIGHTS / IDEA_FIELDS / `aggregate`), `experiments/shortcutting_v4/DESIGN.md`, `HANDOFF.md §0`.
Judging weights confirmed: novelty .30 / significance .25 / soundness .25 / feasibility .10 / clarity .10, worst-verdict-wins, means rounded to 1 dp, score to 2 dp.
