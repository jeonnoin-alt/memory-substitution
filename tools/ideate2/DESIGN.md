# ideate2 — 아이디어 파이프라인 전면 개편 설계 (2026-09-07)

> **요약 (한국어).** 기존 `ideate.py`의 세 병목을 각각 하나의 단계로 바꿉니다. (1) 얕은 문헌 탐색 → **Stage 0 Pre-scan**이 생성 전에 최신 논문을 수집·요약해 "한계 요약본"을 브리프 앞에 붙임. (2) 순차 배제 생성의 재포장 → **축(axis)별 병렬 생성** 후 **재포장 게이트**(임베딩 군집 + LLM 판정)로 걸러냄. (3) 닫힌 책 심사 → **오픈북 심사**(심사자에게 검색 도구 부여, 검색 결과 인용 강제) 앞에 **자동 신규성 카드**를 붙임. 이 노드의 네트워크 현실(arXiv·OpenAlex 차단, S2는 키+IP 고정으로 동작, HF Papers 정상, 전문 읽기는 서버측 웹검색으로만 가능)을 그대로 반영했고, 코드는 `tools/ideate2/`에 두어 동료의 `AI-Scientist-v2`는 건드리지 않습니다. LLM 역할은 API 키가 있으면 API로, 없으면 지금처럼 Claude Code 서브에이전트(하네스)로 돌립니다.

---

## 0. What this node can actually reach (measured 2026-09-07)

| Channel | Status | Gives | Used for |
|---|---|---|---|
| Semantic Scholar Graph API | **works** with `S2_API_KEY` (in `/home/work/.s2_env`, 600) **and only via IP 18.244.60.91** (the other three DNS answers black-hole) | title, year, venue, citations, abstract, TL;DR, references, openAccessPdf URL | search, details, citation graph, novelty check |
| HuggingFace Papers API | works | title, date, abstract (`summary`), `ai_summary`, `ai_keywords` | recency scan (arXiv indexed within a day), by-id verification |
| Claude Code `WebSearch` (server-side) | works | snippets; can surface abstract and section-level text when the query names the section | limitations/conclusion extraction, collision hunting, ID verification |
| Anthropic API `web_search` / `web_fetch` (server-side) | host reachable, **no key on this node** | full pages | the same roles as above, in API mode |
| arXiv (abs/html/export), ar5iv, OpenAlex, alphaXiv, Claude Code `WebFetch` | **blocked** | — | implemented behind a reachability probe so the code works on an unrestricted node |

Consequence for requirement 1: **"read the Method/Limitation section directly" is only possible here through server-side web search** (harness `WebSearch`, or API `web_fetch` once a key exists). The parser is written for arXiv HTML/ar5iv and is exercised through whichever backend is reachable; on this node it runs through a WebSearch job that asks for the Limitations/Conclusion text of a named arXiv ID.

## 1. Architecture

```mermaid
flowchart TD
  T[topic / seed brief] --> P0
  subgraph S0["Stage 0 — Pre-scan (new)"]
    P0[axis proposer] --> Q[query planner\nper axis × {last 12 mo, foundational}]
    Q --> C[collectors: S2 · HF · WebSearch]
    C --> N[normalize + dedupe\narXiv/DOI/title]
    N --> R[rank: recency × citations × relevance]
    R --> F[section fetch\nabstract · TL;DR · limitations snippet]
    F --> D[digest writer LLM\nper-paper card + per-axis gap synthesis]
  end
  D --> B[Stage 1 — brief\nBRIEF_SYSTEM + digest prepended + axes]
  subgraph S2["Stage 2 — axial generation (new)"]
    B --> G1[axis 1 generator]
    B --> G2[axis 2 generator]
    B --> Gk[axis k generator]
    G1 & G2 & Gk --> M[merge]
  end
  M --> GATE["Stage 2.5 — repackaging gate (new)\nembedding clusters vs ideas / brief results / digest claims\n→ LLM adjudication → keep / differentiate / drop"]
  GATE --> NC["Stage 2.7 — novelty card (new)\nkey-phrase extraction → S2/HF/Web → closest-10 with abstracts"]
  NC --> REV["Stage 3 — open-book review\njudges have SearchLiterature; must search the mechanism;\n1 judge → +2 if promising"]
  REV --> AGG[aggregate: weights, worst verdict,\nverified-collision cap]
  AGG --> RV[Stage 4 — revise (open-book) → gate → review]
  RV --> REP[Stage 5 — report + provenance appendix]
```

Every LLM box has two backends: **api** (Anthropic key; `ideate.py` style, tools = `SearchLiterature`) and **harness** (Claude Code subagents; the orchestrator writes a job file per role, the driving session launches agents, results are collected from the task outputs). Prompts are identical across backends and live in `prompts.py`.

## 2. Modules (`tools/ideate2/`)

| File | Role | Backend needs |
|---|---|---|
| `lit.py` | `S2Client` (key, IP pin, throttle, 429 backoff), `HFClient`, `OpenAlexClient`/`ArxivClient` (guarded by reachability), `normalize`, `dedupe`, `SectionReader` (arXiv-HTML/ar5iv parser + WebSearch job emitter) | network only |
| `prescan.py` | Stage 0: axis proposal → query plan → collect → rank → section fetch → digest jobs → `prescan/<slug>/{papers.jsonl, digest.md}` | LLM for axis proposal + digest |
| `axes.py` | Stage 2: per-axis generator job specs (fresh context each), merge | LLM |
| `gate.py` | Stage 2.5: MiniLM embeddings (local), agglomerative clusters, restatement detection against brief results and digest claims, LLM adjudication jobs, `gate_report.md` | local + LLM for adjudication |
| `novelty_check.py` | Stage 2.7: key-phrase extraction (LLM or rule), S2/HF/Web queries, `novelty_card.md` per idea | network + LLM |
| `review.py` | Stage 3: open-book judge job specs (prompt = REVIEW_SYSTEM_OPENBOOK + schema + idea + brief + novelty card), escalation policy, aggregate with verified-collision cap | LLM with search |
| `run.py` | orchestrator; `--backend api|harness`; harness mode emits `jobs/*.json` and `collect` ingests results | — |
| `prompts.py` | every prompt verbatim (below) | — |

`ai_scientist.ideate` is imported for `REVIEW_SCHEMA`, `IDEA_FIELDS`, `SCORE_WEIGHTS`, `BRIEF_SYSTEM`, `REVISE_SYSTEM` so scores stay comparable with every earlier round.

## 3. Stage-by-stage specification

### Stage 0 — Pre-scan
1. **Axis proposal.** From the seed brief, the LLM proposes 4–7 orthogonal axes (e.g. *memory structure*, *write/curation policy*, *retrieval mechanism and budget*, *dynamic prompting / optimizer coupling*, *evaluation methodology*). Axes are editable; the PI may supply them.
2. **Query plan.** Per axis: 3 recent-window queries (mechanism phrasing, application phrasing, closest-method phrasing) + 1 foundational query. HF and S2 get the same strings; WebSearch gets the mechanism query with `2026` appended.
3. **Collect → normalize → dedupe → rank.** Score = 0.5·recency(≤12 mo → 1, decaying) + 0.3·log-citations (S2) + 0.2·query-rank. Keep top-K (default 40) plus every paper that appears under ≥2 axes.
4. **Section fetch.** For each kept paper: abstract + TL;DR (S2/HF). For the top-15: a `SectionReader` job that returns the *Limitations / Future work / Conclusion* text (arXiv HTML where reachable; WebSearch job otherwise), capped at 600 words.
5. **Digest.** One card per paper (`PRESCAN_CARD_SYSTEM`): claim · method · evidence · **stated limitations** · **what it does not test**. Then per axis (`PRESCAN_SYNTH_SYSTEM`): the 3–5 open gaps the cards jointly expose, each tied to ≥2 card IDs. Output `digest.md` is prepended to the brief under `## Recent literature digest (auto, <date>)` and every card ID is carried into the generation prompt.

### Stage 1 — Brief
Unchanged `BRIEF_SYSTEM`, but the input is topic + digest, and the output schema gains `axes` (list) and `digest_gaps` (list of {axis, gap, card_ids}).

### Stage 2 — Axial generation
- One generator agent **per axis**, fresh context, in parallel. Each sees: brief, the digest cards **of its own axis plus the cross-axis papers**, the program's prior results, and the axis's `digest_gaps`. It does **not** see other axes' ideas.
- `AXIS_GENERATION_SYSTEM` (below) requires: ≥2 literature searches, one of them on the claimed mechanism restricted to the last 12 months; an explicit `Addresses gap` field naming a digest gap ID or `none`; an explicit `Not a restatement of` field naming the nearest prior-result bullet and the nearest digest card and saying what differs.
- N ideas per axis (default 2–3); the reflection loop (≤5 rounds, finalize on the last) is kept.

### Stage 2.5 — Repackaging gate
- Embed `Short Hypothesis + Abstract` with MiniLM (local). Build three similarity sets: idea×idea, idea×brief-result-bullets, idea×digest-card-claims.
- Agglomerative clustering on idea×idea (cosine ≥ 0.55 → same cluster, tuned on the 27-idea pool where "volume is the lever" restatements are known).
- For every pair above threshold and every idea whose nearest brief bullet ≥ 0.60: an `GATE_ADJUDICATE_SYSTEM` call returns one of `same_claim_reworded` / `same_mechanism_new_measurement` / `distinct`, with a one-sentence reason.
- Policy: within a `same_claim_reworded` cluster keep one (highest Stage-2 self-assessed novelty), send the others back to their generator with the cluster shown and the instruction to differentiate or withdraw (one round). Ideas judged a restatement of a brief bullet are withdrawn unless the generator can name the new claim in one sentence. `gate_report.md` records every decision.

### Stage 2.7 — Novelty card
- `NOVELTY_KEYS_SYSTEM` extracts from each idea: mechanism phrase, estimand/quantity, named controls, environment. Six queries (S2 ×2 with `year ≥ current−1`, HF ×2, WebSearch ×2) → normalize → top-10 by similarity of abstract to the idea's Short Hypothesis (MiniLM).
- The card lists each candidate with ID, date, venue, abstract, similarity, and the channel that returned it. **It contains no verdict**; it is evidence for the judges.

### Stage 3 — Open-book review
- Judges receive `REVIEW_SYSTEM_OPENBOOK` (below) + schema + idea + brief + novelty card, and the `SearchLiterature` tool (api) / `WebSearch` (harness).
- Required behaviour: ≥2 searches on the mechanism; verify every arXiv ID the idea relies on for its novelty argument; `preprint_collision` must list what was searched and what returned, with IDs; `closest_prior_work` must be a paper the judge found or verified, not recalled; anything from memory is labelled unverified.
- **Escalation policy (token economy):** judge 1 first; if verdict ≠ reject and no verified collision, judges 2–3 run; otherwise stop and report.
- **Aggregate:** `SCORE_WEIGHTS`, worst-verdict-wins (unchanged), plus a **verified-collision cap**: if any judge reports a verified collision on the *claim* (not the framing), novelty is capped at 4 in the aggregate and the collision ID is surfaced in the report.

### Stage 4 — Revise
`REVISE_SYSTEM` unchanged, but the reviser has the same open-book tool and receives the novelty card; revised ideas re-enter the gate before re-review.

### Stage 5 — Report
Existing report plus a **provenance appendix**: every arXiv ID cited anywhere, the channel that verified it (S2 / HF / WebSearch / unverified), and the date.

## 4. Prompts (verbatim; `prompts.py`)

### PRESCAN_AXES_SYSTEM
```
You are planning a literature pre-scan for a research area. Read the seed brief. Propose 4-7 orthogonal AXES along
which the area's design space varies (examples for an agent-memory area: memory structure; write/curation policy;
retrieval mechanism and injection budget; coupling with prompt optimization; evaluation methodology). An axis is a
dimension a paper takes a position on, not a topic. For each axis give: name, one-sentence definition, three search
queries phrased as a researcher would (mechanism phrasing, application phrasing, closest-method phrasing), and one
foundational query for the pre-2024 origin of the idea. Return JSON: {"axes":[{"name","definition","queries":[...],
"foundational":"..."}]}.
```

### PRESCAN_CARD_SYSTEM
```
You are writing an index card for one paper from its title, abstract, TL;DR and, when available, its limitations or
conclusion text. Do not add anything the text does not support. Return JSON with exactly these keys:
"claim" (one sentence: what the paper asserts), "method" (one sentence), "evidence" (the setting, models, benchmarks
and the headline numbers if stated), "stated_limitations" (verbatim or near-verbatim, or "not stated"),
"not_tested" (one or two things a skeptical reader would note the paper does not test), "axes" (which of the
provided axes it takes a position on), "date", "id".
```

### PRESCAN_SYNTH_SYSTEM
```
You are given the index cards for one axis. Write the 3-5 open gaps these papers jointly expose: for each gap, one
sentence stating what is unresolved, the card IDs whose stated limitations or untested items point to it (at least
two), and one sentence on what evidence would settle it. Do not propose papers. Do not invent gaps that no card
supports. Return JSON: {"axis":"...","gaps":[{"gap","card_ids":[...],"evidence_needed"}]}.
```

### AXIS_GENERATION_SYSTEM (replaces the generator system prompt; the ACTION/ARGUMENTS protocol and IDEA JSON are unchanged)
```
You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
axis of the research area below; propose ideas that take a position on that axis. You will not see ideas from other
axes; do not try to cover the whole area.

Bar to clear: contribution stateable in one sentence; positioning that names the closest prior work and what it does
not do; a central claim with an experiment that could come out against it; a measurement plan that separates an
effect from run-to-run noise; feasibility on small open models and single-node compute.

Use the literature digest you were given. Two fields are mandatory in your IDEA JSON in addition to the standard
ones: "Addresses gap": the digest gap ID this idea attacks, or "none" with one sentence on why the digest missed it;
"Not a restatement of": the nearest prior-result bullet in the brief and the nearest digest card, each with one
sentence on what this idea claims that they do not. If you cannot write those sentences, the idea is a restatement
and you must change it.

Before finalizing you must run at least two literature searches: one on the mechanism you are claiming, restricted
to the last twelve months, and one on the closest named method. Report what came back in "Preprint Collision Check",
including empty results and the query strings. Do not write experiment code.
```

### GATE_ADJUDICATE_SYSTEM
```
You are judging whether two research proposals (or a proposal and a prior finding) make the same claim. Read both.
Answer with exactly one label and one sentence: "same_claim_reworded" (the central claim and mechanism are the same;
differences are wording, setting or metric), "same_mechanism_new_measurement" (same mechanism, but the second
measures a quantity or runs a control the first does not, and that difference would change a reader's conclusion),
or "distinct". Return JSON {"label","reason"}.
```

### NOVELTY_KEYS_SYSTEM
```
Extract from this proposal, as short phrases, the search keys a reviewer would use to find prior work that already
makes its claim: "mechanism" (what causes what), "estimand" (the quantity measured), "controls" (named control arms),
"environment" (benchmarks/models). Return JSON with those four keys, each a list of 1-3 phrases.
```

### REVIEW_SYSTEM_OPENBOOK (appended to the unchanged REVIEW_SYSTEM)
```
You have a literature search tool and a novelty card listing the closest candidates an automated search found.
Rules for this review: (1) Run at least two searches on the proposal's claimed mechanism, one restricted to the last
twelve months, and at least one on its closest named method. (2) Verify every arXiv ID the proposal relies on for its
novelty argument; say which you verified and which you could not. (3) In "closest_prior_work" name a paper you found
or verified, with its ID; if the strongest threat you know is from memory and you could not verify it, say so and
label it unverified. (4) In "preprint_collision" report the queries you ran and what they returned, with IDs; an empty
search is reported as empty, not as evidence of novelty. (5) If a search finds a paper that already makes the central
claim, say "VERIFIED COLLISION: <id>" as the first words of "preprint_collision"; the aggregate will cap novelty. Score
novelty on what you verified, not on what the proposal asserts.
```

### REVISE_SYSTEM
Unchanged from `ideate.py`; the reviser receives the novelty card and the same open-book tool.

## 5. Scoring and stop rules
- Model policy (PI, 2026-09-07): Stage 2 generators = Fable 5.1; all other LLM roles = Opus; Sonnet prohibited. (§8 validation predates this and used Sonnet for cards, gate and section reads.)
- Weights and worst-verdict-wins unchanged (comparability with every earlier round).
- Verified-collision cap: novelty ≤ 4 in the aggregate when any judge writes `VERIFIED COLLISION`.
- Escalation: 1 judge → +2 if not reject and no verified collision.
- Round stop: no design-blocking finding in a round (a finding that would change an arm, a claim's wording, a test or the split structure) → freeze; never a score target.

## 6. Harness mode (no Anthropic key)
`run.py --backend harness` writes `jobs/<stage>/<name>.json` with `{prompt_file, model, tools:[WebSearch|none], expects:"json|markdown"}`. The driving Claude Code session launches one subagent per job (model as specified), and `run.py collect --stage <stage>` ingests `tasks/*.output` by job id (the same extractor used for the v2–v6 rounds). Everything else (collectors, normalize, rank, embeddings, clustering, aggregation, report) runs in Python without an LLM.

## 7. What changes for the proposal that motivated this
Re-running Stage 0 on the agent-memory brief would have put ExpeL's ablation numbers, AWM, ACE, Dynamic Cheatsheet, MemAPO and MemPro in front of the generators before v1 was written; the gate would have merged the three "volume is the lever" restatements in the 27-idea pool; and open-book judges found AWM/ACE/DC on the v2 text in one round. Those three failures cost this program roughly eight proposal rounds.

## 8. Measured validation (2026-09-07, harness mode, this node)

| Stage | Input | Result | What it showed |
|---|---|---|---|
| 0 collect | 4 hand axes × (3 queries + 1 foundational), S2 (keyed, pinned) + HF | 32 papers kept after `--rerank` (0.4 recency + 0.2 log-cit + 0.4 MiniLM relevance) | Without the relevance term the top-40 was citation-dominated off-topic benchmarks; with it the top-12 are all agent-memory / prompt-optimization papers from 2025-12 → 2026-08 |
| 0 sections | 8 WebSearch section-read jobs (Sonnet) | 8/8 returned a record; verbatim Limitations for 2 (EvoAgentBench, ZERA), paraphrased-from-snippets for 4 (MAGE, AMD, MemSkill, survey), method-only for 2 (ReMe, ERL) | Section reading through server-side search works about half the time and must be labelled verbatim vs paraphrased; the reader also caught one wrong title in our own metadata (MAGE) |
| 0 cards | 4 batched card jobs (8 papers each, Sonnet) | 32 cards, 9 with a stated limitation, axes: memory-structure 23 / retrieval 17 / evaluation 16 / coupling 7 | `not_tested` fields are the useful part: they name the missing ablation per paper (e.g. retrieval vs write policy never factorised) |
| 0 synth | 4 per-axis gap jobs (Opus) | 20 gaps with card ids and `evidence_needed` | Gaps that recur across axes: write-policy vs retrieval attribution; abstraction vs raw-trajectory reuse; injection budget as a controlled variable; memory × prompt-optimization interaction term; multi-backbone variance |
| 2.5 gate | 27 archived AI-Scientist-v2 ideas + brief prior bullets | thresholds auto (idea 0.649, prior mean+1.5·SD); 2 clusters; 93 pairs → 10 Sonnet batches; 86 distinct / 4 same-mechanism-new-measurement / 1 same-claim-reworded | The one `same_claim_reworded` is `optimizer_substitutes_for_memory_scaffold` vs `substitutes_not_complements` (sim 0.702) → send the later one back to differentiate. `memory_or_instruction` (the v-series topic) is `same_mechanism_new_measurement` against both `compile_dont_retrieve` and `substitutes_not_complements` → keep with a note; `memory_budget_confound` is a new measurement of the brief's own "one-sidedly harmful" finding |
| 2.7 novelty | v6 proposal; rule-based keys → 5 S2/HF queries + 1 WebSearch job (7 queries) | API candidates top-10 by MiniLM sim; 12 web adjacents, 11 verified through S2/HF, 1 id unverifiable (2606.29178) | The web agent surfaced *Compiled Memory: not more information, but more precise instructions* (2603.15666) and MemAPO (2603.21520): both are mechanism-level neighbours of v6 that no API query returned. The id-verification step is not optional: 5/12 web ids failed S2 id lookup and needed title search or HF to confirm |

Cost of the run: 8 section reads + 4 card + 4 synth + 10 gate + 1 web-novelty = 27 subagent calls, all Sonnet except the 4 synth (Opus). No Anthropic key was used.

Bugs found by running it: `parse_json` returned the innermost balanced span (a nested list) instead of the outer object → fixed to top-level spans only, last one wins; a fixed cosine threshold of 0.55 put 27/27 ideas in one cluster → mean + 1.5·SD; card `axes` sometimes came back as prose → mapped back to axis names by substring; two synth transcripts were stored with the final `}` missing although the agent returned it → `parse_json` now repairs a truncated tail by replaying the bracket stack.

## 9. First end-to-end run under the model policy (2026-09-07, `runs_ideate2/agent_memory_v2` + `gen_v2`)

Stage 0/1/2 by Fable 5.1 subagents, gate and judges by Opus, no Sonnet, no Anthropic key; WebSearch quota (200/session)
ran out during Stage 2, after which every literature call went through `s2cli.py` (S2 + HF).

| Stage | Calls | Result |
|---|---|---|
| 0 collect | network | 8 axes, 32 queries, 480 unique → 103 kept (coupling axis supplemented with 8 targeted queries) |
| 0 sections | 14 Fable (2 papers each) | 28 records; 12 with verbatim limitations |
| 0 cards / synth | 9 + 8 Fable | 103 cards (24 with stated limitations), 40 gaps |
| 1 brief | Fable (this session) | `brief_v2.md`: pilot findings kept, 5 original questions re-assessed, 8 new questions, 27 archived ideas appended |
| 2 generation | 8 Fable (WebSearch until quota, then s2cli) | 24 proposals, 13 fields each; several generators revised after the S2+HF instruction |
| 2.5 gate | 11 Opus batches | 103 pairs: 88 distinct, 11 same-mechanism-new-measurement, 0 repackagings once brief open-questions are excluded |
| 2.7 novelty | network | 24 cards (rule-based keys); noisy top hits, judges searched themselves |
| 3 review r1 | 24 Opus | borderline 15 / reject 9; scores 4.65–6.30; 0 verified collisions |
| 3 escalation | 4 Opus | top two → 3 judges: `abstraction_discards_bindings_and_repairs` 5.95 borderline, `failure_memory_framing_drag` 5.72 reject |

What the judges did that closed-book rounds could not: every review names 5–8 s2cli queries with returned ids and marks which
proposal citations resolved; they surfaced 2026-05 to 2026-08 preprints that the generators had missed (Honest Lying 2605.29463,
Memory Transfer Learning 2604.14004, Fragility of Self-Improving Agents 2608.18066, SkillAligner 2608.06880, Plans Don't Persist
2606.22953, Contextual Experience Replay 2506.06698) and caught two citations that do not resolve on either channel (2608.07429,
2608.10509) plus one that a generator claimed to have verified and had not.

Structural findings across the 24 reviews (for the next brief): (1) the pilot's "volume is the lever" result makes every
injection-reducing intervention (gate, timing, summary, abstraction) confounded with "inject less" unless a rate-matched or
token-matched placebo arm exists; (2) the 27B memory channel (+0.6) cannot support ratio-valued predictions, so confirmatory arms
belong on the 120B or in a manufactured high-harm regime; (3) predictions entailed by policy definitions (decay deletes dormant
items; replay is truth-sensitive; a bank forgets nothing) were called out as non-findings; (4) the field's mechanism claims are
mostly published, so the surviving novelty is measurement design, which caps novelty at 5–6 under this rubric.

## 10. Second topic run: parametric vs in-context experience (2026-09-07, `runs_ideate2/parametric` + `gen_v3`)

Same policy (Fable Stage 0/1/2, Opus gate and judges), no WebSearch at all (quota spent on the first topic), every literature
call through `s2cli.py`. New this round: a measured starting position (`runs/STEP0_RESULTS.md`: k-sweep +27/+32 net on
Qwen3-32B, QLoRA 2 GPU-h/epoch) written into the brief, a rules section derived from the previous round's 28 reviews, and the
51-idea archive passed to the gate (`--archive`).

| Stage | Calls | Result |
|---|---|---|
| 0 cards / synth | 8 + 5 Fable | 79 cards (5 axes), 26 gaps; digest 113 KB |
| 1 brief | Fable (session) | `brief_v3.md`: starting numbers, 10 binding rules, Q1–Q6, appendix A (51 archived) + B (3 objections) |
| 2 generation | 5 Fable | 15 proposals; two generators converged on the same idea (instance-bound share of the privilege) |
| 2.5 gate | 6 Opus batches | 53 pairs: 43 distinct, 9 same-mechanism-new-measurement, 1 same_claim_reworded (the convergent pair; one withdrawn) |
| 2.7 novelty | network | 15 cards (rule keys, S2 2 queries + HF) |
| 3 review r1 | 14 Opus | 12 borderline / 2 reject; scores 4.35–5.55; novelty 5 from 12 of 14 judges; 0 verified collisions |
| 3 revise → r2 | 3 Fable + 3 Opus | top 3 revised against their reviews, re-judged (see below) |

Structural findings across the 14 reviews (they repeat the previous round's, with two additions):
1. **Definitional predictions still slip through the generators** even with the rule in the brief: an algebraic identity
   presented as a regression (context_ceiling P1), a null guaranteed by the train/eval partition (instance_share P2), a
   spillover ratio set to zero by type-matched retrieval (harm_spillover P1), append-only-vs-chunked-SGD as a "lock-in"
   finding, a warm-start advantage as a "savings ratio", unconditional marker emission as "generalization". The gate cannot
   catch these (they are not restatements); only the judge does. A cheap pre-review pass that asks "which outcome of each
   prediction is impossible under the stated arms" would remove most of them before Opus time is spent.
2. **Power arithmetic is wrong in the same direction every time**: equivalence margins are set at or below the stated CI,
   gates guarantee the headline effect but not the ratio the paper is about, per-type cells (±13–15) carry the claims.
3. **Budgets are understated 2–3×** once every arm × condition × seed × task is multiplied out; judges did the multiplication.
4. **Collision checks are one-sided**: generators searched the agent-memory phrasing and missed the mechanism's home
   literature every time (RAG dose 2410.05983/2310.01558; near-constant poison count 2510.07192; emergent-misalignment
   generalization 2608.29118; spurious forgetting 2501.13453; knowledge-preference QA 2407.13048; DIVE diversity-vs-quantity
   2603.11076; paraphrase subliminal transfer 2603.09517). The novelty card's rule keys have the same blind spot.
5. **The cheap baseline that kills the paper is a sentence**: a static per-type procedure prompt or a one-line rule statement
   (named by four judges) dominates both substrates on the cost axis for procedure-templated ALFWorld; any weights-vs-context
   claim on this environment must run it first.
6. Novelty is capped at 5 because the mechanisms are published (information abundance, compliance trap, subliminal transfer,
   spurious forgetting, privilege illusion); what is new is the paired-substrate design, which the rubric scores as measurement.

Round 2 (revise-then-rejudge instead of re-judging unchanged ideas): the top three were revised by Fable against their own
review (`tools/ideate2/revise_collect.py`, jobs built from REVISE_SYSTEM + proposal + review + brief rules) and re-judged by one
fresh Opus judge each. Scores moved 5.55→6.10, 5.45→5.85, 5.45→5.55; all three stay borderline. What the revision bought:
the definitional headlines were removed (residual-vs-arithmetic estimand, post-feedback window, off-span-divergence axis),
budgets were re-costed honestly (26–46 arms, 5–6 days), and missing baselines were added. What it did not buy: each r2 judge
found the next definitional layer (a null calibrated off-stream, a masked-objective test that cannot touch the measurand,
an inert stale-weights arm) and the next cheap baseline (inoculation prompting 2510.04340; CK-PLUG 2503.15888; a paired
no-shift control stream). Novelty stayed at 5–6 because the mechanisms are published; the ceiling for this rubric on this
topic is ≈6, the same as the first topic. Recommendation recorded in the session report: stop generating on this topic; the
two pipeline changes with the best expected lift are (a) a pre-review entailment pass ("which outcome of each prediction is
impossible under the stated arms?") and (b) a mechanism-side collision search alongside the agent-memory one.

## 11. Two pipeline fixes after the second topic (PI decision 2026-09-08): entailment check and home-literature search

**Stage 2.8 entailment check (`entail.py`, Opus, 3 ideas per job).** For every prediction: the arms it rests on, the outcome
that would falsify it, whether that outcome is reachable under the stated design, and whether it is distinguishable at the
stated noise; labels open / entailed / near_entailed / unresolvable; the headline prediction must be open or the idea goes back
to the generator (`entail.py revise` → Fable) before any judge runs. The per-idea report is attached to the review prompt
(`review_batch.py emit --entail`). Validation on the 15 gen_v3 ideas against the 14 round-1 Opus reviews (whose strongest
objections named specific predictions): 92 predictions labelled, 14 open / 24 entailed / 19 near-entailed / 35 unresolvable;
of the 35 predictions the judges had called entailed or underpowered, the stage flagged 31; it flagged 40 more that the
judges did not name (they report one objection each). Headline open for 4 of 15 ideas; all 15 get verdict "revise", which
matches the judges (12 borderline, 2 reject, 0 accept). Cost: ~60k Opus tokens per 3 ideas, versus ~65k per full review, so
the stage pays for itself if it removes one judge round per idea. `runs_ideate2/gen_v3/entail/VALIDATION.md`.

Generator-side: `AXIS_GENERATION_SYSTEM` now requires, per prediction, the falsifying outcome and the arm that can produce it,
and one literature search in the mechanism's home vocabulary (`home:`).

**Stage 2.7 query classes (`novelty_check.py`, keys by Fable).** Queries are classed `mechanism_home` (the phenomenon in the
vocabulary of the field it came from, no agent/memory/benchmark words), `agent`, `adjacent` (published result direction in a
neighbouring field), `baseline` (cheapest intervention), `methods`; the card says which class found each candidate and lists
papers that only the home/adjacent/baseline queries returned. Ground truth: the 57 papers the 14+3 Opus judges cited that the
generators had missed (`novelty2/judge_found.json`). Recall: old agent-only rule keys 6/57; new rule keys with vocabulary
shift and templates 7/57; Fable keys in five classes 13/57. Inspection of the misses showed the remaining cause: the home
literature is older (RAG robustness 2023–24, knowledge-conflict 2023, knowledge-preference 2024, poisoning 2025) and the S2
call carried a 12-month window while HF Papers indexes recent arXiv only; home/adjacent/baseline queries now go to S2 without
a date window (`novelty3` rerun below).
Rerun with the window lifted (`novelty3`): 17/57 — the older knowledge-conflict, RAG-robustness, relearning and poisoning papers
now appear under `mechanism_home`/`adjacent` (2407.13048, 2503.15888, 2310.01558, 2505.22310, 2602.03379, 2510.07192). What the
card still cannot do is what the judges did: refine a query after reading a first result; the remaining misses are second-hop
finds (e.g. 2608.29118 emergent-misalignment, 2603.11076 DIVE, 2510.04340 inoculation prompting). Recall 6→17/57 for the same
S2/HF budget; judges keep the `home:` vocabulary instruction and the card's class labels as their starting point.
Health metrics to report on every future run: entailment flag rate per idea, and card recall against judge-found papers.
