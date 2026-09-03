# Deviations log (append-only)
2026-08-24 Bank A size: 199 items (S_bank produced 199 solved episodes at EM 0.497), below the ~350-450 assumption in DESIGN §3. Retrieval top-7 over 199 remains viable; noted, not gated.
2026-08-25 build_bank.py execution bug (crash 2026-08-24 19:15, orchestrate stage bank_distill): all three call()
  call sites omitted the client argument (TypeError); bank_A.jsonl was left 0 bytes, no bank-dependent arm ran.
  Fixed: client passed at 3 sites; all bank stages made resumable (append + skip by src_qid) per T-D
  "reruns append, never overwrite". Execution-level fix — no arm/claim/test/split change.
  FREEZE.sha256 code/build_bank.py updated: 8bf914bd1e15… → 2fdf43caf359….
2026-08-25 Infra note: compute node recycled overnight (session died without keepalive); /home/work root lost.
  vllm-env recreated at the same path (vllm==0.13.0); NFS artifacts (runs/, data/, prereg/) intact. bankgen
  (400 eps) NOT re-run — resumed from existing JSONL.
2026-08-25 Engine version correction: THRESHOLDS T-D notes "vllm 0.13.0" but the 08-24 serve logs record the
  actual engine as vLLM 0.19.1 (0.13.0 does not support the Qwen3.5 architecture at all). Environment rebuilt
  with vllm==0.19.1 to match the measured runs; frozen THRESHOLDS.md text left untouched, corrected here.
2026-08-25 Client-side CUDA OOM in first memory-arm runs (M1 S_dev1: 150/150 errored; M1_Fh S_dev2: 17/100):
  memory.py's MiniLM embedder defaulted to cuda:0, which vLLM already fills (0.90 util). First exposure of this
  path — yesterday died before any memory arm ran. Fixes (execution-level, no design change):
  (a) memory.py embedder pinned to CPU (device="cpu"); (b) run_arm.py no longer counts error records as done,
  so reruns retry them (error lines stay in the log; successful retries append — T-D append-only preserved);
  (c) gates_eval.py load() filters by actual "em" key. The 16:44 "GATE FAIL" in orchestrate.log was this crash,
  not a measured gate failure — no gate number was produced. FREEZE.sha256 updated:
  memory.py 6cd6366fc093… → fa9fc5b2d507…, run_arm.py d82ffa82ac0c… → 23f39069ea11….
2026-08-26 A8 implementation hardening (gate round 3: G-8 8/100, all else PASS; G-2 rose to 81/100).
  Replaying a failed episode with identical seeds SUCCEEDED and showed the terminal answer pattern: a long
  Evidence paragraph with Finish[...] at the very end — the 8 failures are stochastic max_tokens=420 truncation
  races under concurrent load, not model inability. Terminal call only: max_tokens 420->800, wording now demands
  brevity and forbids Search, and the parse accepts the LAST Finish match (finditer) instead of the first
  ACT_RE match. A8's registered mechanics (one terminal call, floor bypass, forced_final logging) unchanged;
  main-loop parsing unchanged. Execution-level. agent.py 8975ce1e4102… → 357576693fd1….
2026-08-26 Note: round-3 replay also demonstrated per-episode seeding is NOT bit-reproducible under concurrent
  vLLM batching (same seeds, different outcome solo vs loaded) — recorded for the reproducibility section.
2026-08-31 memory.py lacked M6/M8 branches (ValueError; latent — dev gates never exercise these arms). All 4
  affected S_test runs (M6 s11, M8 s11/s23, M8_Fh s11 = 2,000 episodes) errored and are re-run after implementing
  the frozen definitions verbatim: M6 = bank-A top7 (budget delta in cfg), M8 = curated top7. All other matrix
  runs unaffected (completed 08-27 02:52, 0 errors). memory.py fa9fc5b2d507… → d15299aff7a5….
2026-08-31 Replication model substitution (arm 33). EXAONE-4.0-32B turned out to be an INCOMPLETE download on
  NFS (4/14 shards, all .part, no tokenizer — the D1 "all local weights" assumption was wrong for this model),
  and the HF CDN still refuses large-blob downloads (probe timeout; small files now resolve). Substitute:
  gpt-oss-120b (OpenAI lineage, official mxfp4, complete locally) — a stronger family separation from the Qwen
  agent than LG EXAONE. R2-V6 restriction unchanged: replication claims limited to EM/F1 outcomes. The
  echo/compliance/citation annotator role formerly assigned to EXAONE (V2) moves to the D6 harness frontier
  (Claude Fable 5), preserving separation from the Qwen3-32B distiller.
