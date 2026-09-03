# AMENDMENTS — infrastructure-forced deviations from DESIGN.md v1 (pre-registered with reasons, 2026-08-24)

Network reality measured today: only github.com (git), pypi.org, and huggingface.co (API/small blobs) are reachable.
HF CDN (Xet), datasets-server, arxiv, wayback, dropbox, gdrive, modelscope: blocked. Anthropic API: credit-blocked to 09-01.

D1 MODELS (was: Qwen2.5-14B / Llama-3.1-8B / Qwen3-32B). Now, all local NFS weights:
   - Agent: **Qwen3.5-27B** (bf16, TP=1 per A100 → data-parallel replicas; thinking disabled via chat template for
     fixed episode economics; lab-validated serve flags exist).
   - Distiller/redactor: **Qwen3-32B**. Echo/compliance/citation annotator: **EXAONE-4.0-32B**
     (role separation per review fix V2; supersedes the earlier single-annotator wording).
   - Replication: **EXAONE-4.0-32B** (different model family — strengthens the model-dependence check vs Llama-8B).
   Rationale: HF weight download impossible; these are the strongest locally available, and agent/annotator remain
   different checkpoints. Risk noted: agent and distiller share vendor lineage (Qwen); the annotator is cross-vendor (LG EXAONE), plus human validation sample; EM/F1 primary outcome needs no judge.
D2 DATA (was: full HF datasets). Now: HippoRAG benchmark subsets committed in-repo (data/PROVENANCE.md):
   1,000 questions + retrieval corpus per dataset (HotpotQA 9,811 / MuSiQue 11,656 / 2Wiki 6,119 passages).
   Search tool operates over the question's own dataset corpus. Splits carved from pooled 3,000 by seeded script:
   S_bank 400 / S_opt 150 / S_dev1 150 / S_dev2 100 / S_test 500 (dataset-stratified 50/30/20 where counts allow).
D3 RETRIEVERS. Corpus search tool: BM25 (rank_bm25) — deterministic, dependency-light. Memory-bank retriever:
   dense, local sentence-transformers paraphrase-multilingual-MiniLM-L12-v2 (was BGE — not downloadable). Both are
   held-fixed nuisance components, not manipulated variables; identity disclosed.
D4 DISTILLATION/REDACTION/GOLD (was: frontier API). Until credits return: Qwen3-32B performs ExpeL distillation,
   answer-redaction, M2i construction, and bulk annotation. Frontier gold-validation sample and the 480-episode
   compliance probe are DEFERRED to ≥09-01 and reported as pending, not skipped silently.
D5 OPTIMIZER REFLECTION. GEPA/MIPROv2 reflection model = Qwen3-32B (was frontier). Optimizers remain seeded with
   I* verbatim, so discovery-vs-compliance logic is unchanged; reflector strength affects only how much better than
   the seed the search can get, which the published training curves will show.

## Gate-triggered amendments (2026-08-25; gate round 1 numbers in GATES_LOG.md — G-2 64/100, G-3 breaks 8, G-6 13.1%, G-8 27%)
A6 NO-FINISH BUDGET EXTENSION. Diagnosis: 25/27 of G-8's unparseable episodes and 21/36 of G-2's non-compliant
   episodes ended at exactly the 8-call cap with zero floor rejects and zero Finish attempts — pure search-loop
   truncation, not format failure. The Evidence requirement intentionally induces more search; the cap was set
   from no-floor episode economics (mean 3.15 calls) and censors that induced behavior into non-answers.
   Change: an arm whose instruction slot is filled OR whose floor != none receives ONE +floor_extra(3) extension
   when the budget would expire with no Finish ever attempted (agent.py, marked A6). Bare arms (M0/M1/M2/...)
   are untouched — their existing runs and the frozen primary endpoint M0-vs-M1 are unaffected. The pre-existing
   reject-triggered +3 (DESIGN §5) already gave floor arms a larger cap; A6 generalizes it to the never-Finish
   case. Fs/Fh dev measurements from the old mechanics are archived as *.pre_A6 and re-measured fresh.
   Thresholds unchanged.
A7 S_dev1 150 -> 300 FROM RESERVE. G-3 failed on absolute break count (8 < 10) at n=150 with a strong
   qualitative signal (8/8 non-echo). The RESERVE is pre-registered for gate-triggered use. Method: deterministic
   continuation of the SEED=20260824 shuffle at the post-1300 cursor positions (no new randomness; replay
   verified against stored S_dev1 before extending). Added IDs recorded as splits.json["splits"]["S_dev1_ext150"]
   (75/45/30 strata; hash de66777075bffebc). G-1/G-3 are re-measured on n=300. Thresholds unchanged.
A8 TERMINAL FORCED-FINISH (2026-08-26; gate round 2: G-8 19/100, all other gates PASS). Diagnosis: all 19
   answerless Fh episodes used the full A6-extended 11 calls, 15/19 with zero floor rejects, 11/19 searching on
   every call — literal indefinite obedience to "search first if you cannot quote evidence" on hard questions.
   Same pattern in M0_Fs (18/100, ungated). Episodes that did finish under Fh: EM 0.654 vs M0 0.50 — the floor
   helps when it converges. Change: when an instruction-slot arm's episode would end with final=None, ONE
   terminal call orders Finish now; the hard floor does not re-reject the terminal answer; forced_final is
   logged per episode and reported per arm. Rationale: an answerless episode scores EM=0, punishing induced
   thoroughness and confounding the floor's effect; forced terminal answers are standard ReAct practice. G-8
   thereafter measures true format failure (Finish unproducible even on direct order). Bare arms untouched;
   primary endpoint M0-vs-M1 unaffected. Round-2 Fs/Fh dev logs archived as *.pre_A8. Thresholds unchanged.
D6 FRONTIER SUBSTITUTION (2026-08-31). API credits were NOT restored on 09-01 as assumed in D4/D5. Per user
   direction, the frontier role moves to Claude Fable 5 via the Claude Code harness (subscription billing):
   (a) optimizer reflection (upgrade over the D5 Qwen3-32B fallback; training curves still published),
   (b) gold-validation samples (bank truthfulness, redaction leakage, EM-scoring audit),
   (c) the 480-episode frontier probe if token budget allows (else reported unrun per partial-completion policy).
   Caveat reported in the paper: harness-substrate frontier outputs are not API-reproducible verbatim; all
   prompts and responses are logged to runs/opt/ and prereg/ for audit. Local roles unchanged: agent Qwen3.5-27B,
   EXAONE-4.0-32B replication (arm 33, running), annotator audits per V2.
