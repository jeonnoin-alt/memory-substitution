# HANDOFF — 제안 ③ "When Is a Retriever Decorative?" (영훈님 세션용)

> **영훈님께:** 이 파일을 새 Claude Code 세션에 통째로 읽히고 "이 HANDOFF대로 진행해줘"라고 하시면 됩니다. 아래부터는 그 Claude를 위한 지시문입니다 (영어 혼용 — 원문 인용의 정확성을 위해).

---

## Mission (in order — do not skip stages)

1. **재현 (Reproduce context):** read the three proposal versions and their reviews from the files below. Do not trust this summary alone — read the actual texts.
2. **고도화 (Refine):** run a FRESH literature scan (this field moves in weeks — the last scan was 2026-08-21 and is already stale for you), then produce a v4 of this proposal that answers the reviewer objections listed below. Have it re-judged with the zero-credit harness method (§ Judging) before implementing anything.
3. **실험 진행 (Run):** write DESIGN.md (see the format precedent in `experiments/shortcutting_v4/DESIGN.md` — proposal ① is being executed by another session; keep file/GPU coordination in mind), implement, and run. **Do not write experiment code before stages 1–2 are done and the design is fixed.**

## What proposal ③ is

**Lineage & scores:** v1 "Is Your Agent's Memory Just an Un-Optimized Prompt?" 6.73 → v2 (same title, scoped) **6.97 (best)** → v3 "When Is a Retriever Decorative?" 5.73.

- **v1/v2 question:** a memory bank and a GEPA-optimized instruction are two containers for the SAME training episodes; published memory gains are measured with the instruction container empty. Substitution ratio S = how much of memory's gain survives after the instruction container is filled. Key artifacts: bank B (ExpeL), I1 (GEPA optimized without memory, 300 rollouts × 3 seeds), I3 (length-padded control), C (offline-compiled bank, token-matched), R (raw few-shot control). Fairness constraint: both containers see identical training episodes.
- **v3 pivot (what lost the points):** dropped ALL optimizer arms; primary arm A_fix = frozen top-k subset (same k items for every query, verbatim); primary metric R_fix = acc(A_ret) − acc(A_fix); overlap statistic O = mean pairwise Jaccard of top-k retrieval sets, computed from the retriever alone in seconds; "the law": O predicts R_fix out of sample (leave-one-cell-out over ~20 cells spanning O∈[0.05,1.0]). Banks: B_expel(N∈{100..1000}), B_rbank (ReasoningBank-style), B_raw, B_offdomain, B-dup (paraphrase near-duplicates, low-overlap anchor). Arms: A0/A_ret/A_fix/A_rand/A_comp/A_scram/A_mmr. Gates G1–G3. ~23,100 episodes.

## Where everything lives (NFS, survives recycling)

| What | Path |
|---|---|
| Repo | `/home/work/neuro/AI-Scientist-v2` |
| v1 full text | `ai_scientist/ideas/agent_memory_v2.json` — entry with `"Name": "memory_or_instruction"` |
| v2 full text (best, 6.97) | `ai_scientist/ideas/agent_memory_top4.json` — same Name |
| v3 full text + all 5 reviews | `ai_scientist/ideas/agent_memory_top4_reviews.json` — `scored[]` entry `"Name": "decorative_retriever"`; v2-era reviews in `agent_memory_v2_reviews.json` (`memory_or_instruction`) |
| Judging pipeline (prompts/schema/weights to reuse) | `ideate.py` — `REVIEW_SYSTEM`, `REVIEW_SCHEMA`, `SCORE_WEIGHTS` (novelty .3 / significance .25 / soundness .25 / feasibility .1 / clarity .1), worst-verdict-wins |
| Claude-5 API rules | `ai_scientist/anthropic_compat.py` (no temperature; thinking shares max_tokens; refusal stop_reason; min 16k max_tokens) |
| Literature tool (network quirks handled) | `ai_scientist/tools/literature_search.py`, `ai_scientist/tools/semantic_scholar.py` |
| Design-doc precedent (proposal ①) | `experiments/shortcutting_v4/DESIGN.md` |
| Research-area brief | `ai_scientist/ideas/agent_memory_optimizer.md` |

## Reviewer objections you must answer (the refinement contract)

**From v2's reviews (when it scored 6.97):**
1. *Fairness constraint not actually enforced:* the bank distills all 500 training episodes; GEPA's 300 rollouts sample a subset. **Instrument GEPA's episode coverage**, and either force one full sweep or build a second bank from only the episodes GEPA touched. Cheapest decisive fix in the whole lineage.
2. *I2 (optimize WITH memory in context) omission called self-serving.* Minimal repair: one I2×M0 cell (optimize with memory, then remove it → dependence test).

**From v3's reviews (why it fell to 5.73) — all three reviewers said the same thing:**
3. *Zero optimizer arms = out of scope for a track titled "Coupling Self-Editing Memory with Prompt Optimization".* Restore at least one **GEPA-lite** cell (fixed rollout budget) at one high-overlap and one low-overlap cell, testing whether optimization MOVES the overlap threshold at which retrieval starts paying. Either result strengthens the paper.
4. *Missing baseline:* stuff-the-whole-bank-in-context (feasible at N=100) — separates "compiler does the work" from "content just needs to be present".
5. *20-cell regression:* cells share banks/environments → use mixed-effects pooling with bank and environment random effects, not independent-draws stats.
6. *Citation verifiability (3/3):* every arXiv ID ships in a verification appendix (ID / exact title / 2-sentence abstract quote / retrieval date / source). Post-hoc audit of this program's citations found 30/30 real — the failure was presentation. Generate the table at design time.

**Recommended framing pivot:** sell the overlap statistic as the answer to "WHERE should coupling research happen" — R_fix>0 regimes are where memory×optimizer coupling matters; naming them pre-deployment is the service to the track. This argument already exists in v3's Risk#7 — move it to the abstract.

## Judging without API credits (proven 2026-08-21 on proposal ①)

The Anthropic API key is exhausted until **2026-09-01 00:00 UTC** (`/home/work/.anthropic_env`). Reviews cost zero credits via the Claude Code harness: compose a judge prompt file containing (1) `REVIEW_SYSTEM` formatted with venue "ICLR 2027 main track", (2) the `REVIEW_SCHEMA` JSON verbatim with "return ONLY the JSON", (3) `REVIEW_USER` with your idea JSON (use the 11 IDEA_FIELDS structure) + the brief. Spawn **3 independent general-purpose subagents, model "sonnet", in parallel**, each told to read the file and output only the JSON. Aggregate with `SCORE_WEIGHTS` + worst-verdict-wins. Caveat to report: harness-substrate scores are comparable in *objection content*, only indicatively in absolute value.

## Infrastructure & ops (read before running anything)

- **GPU node:** 4×A100-80GB. A keepalive burner may be running — check `pgrep -af gpu_keepalive`; kill before real runs (`pkill -f gpu_keepalive.py`), restart after (`setsid nohup /usr/bin/python3 /home/work/neuro/tools/gpu_keepalive.py > gpu_keepalive.log 2>&1 &`). **Coordinate with proposal ①'s runs** (same node) — check `nvidia-smi` and agree on time-sharing before launching.
- **Serving:** vLLM, Qwen2.5-14B TP=2 × 2 replicas; measured ~1,200–4,000 episodes/hour depending on episode length. `/home/work` root is NOT persistent — only `/home/work/neuro` (NFS) survives; TeX/tmux installs vanish on recycle.
- **Network quirks:** `api.semanticscholar.org` needs IP pinning (see `semantic_scholar.py:_pin_reachable_ip`; 18.244.60.91 worked; throttle ≥1.2 s). HF Papers API resets connections intermittently — retry 3×. Direct arxiv.org HTTP is blocked; use HF `https://huggingface.co/api/papers/search` + web search. Run long jobs under **tmux** (GlobalProtect VPN drops kill plain SSH sessions).
- **API-dependent steps** (bank distillation, GEPA reflection, gold annotation): wait for the new key or use the pre-registered Qwen3-32B fallback, reported as a deviation.
- **Keys/DUA:** never paste API keys into chat (session transcripts are plaintext on NFS — keys pasted this way must be rotated). Keys live in `/home/work/.anthropic_env` (chmod 600). No NACC/patient data anywhere near this work (lab DUA; this project is public-data only).

## Non-negotiable measurement standards (lab house rules — every run)

Fully paired within-instance comparisons · exact McNemar + Holm on fix/break tables, every delta with its fix/break decomposition · **TOST equivalence** (pre-registered margins) for every "no difference" claim — never absence-of-significance · **null replicates**: identical condition re-run at a different seed; no effect claimed below the 95th percentile of that distribution (this program has observed 5–14 pt re-scoring drift and one treatment-free replicate that mimicked the best real treatment) · MDE stated before running; sub-MDE differences declared inconclusive in advance · pre-registered drop-priority order for contingency cuts · partial-completion policy: unrun arms are "unrun", never nulls.

## Definition of done

1. v4 proposal text (11 IDEA_FIELDS) + fresh-scan collision analysis + citation appendix → harness-judged ≥ 3 reviewers → objections from §above demonstrably dissolved or explicitly refused with reasons (the lineage's lesson: refusing with reasons is fine; v3 died from over-compliance in the wrong direction).
2. `experiments/decorative_retriever_v4/DESIGN.md` in the same format as proposal ①'s.
3. Implementation + runs per DESIGN, results with the noise protocol, analysis notebook, and a summary the PI can read in Korean.
