# AMENDMENTS — data- and infrastructure-forced deviations from the frozen proposal text v5.2 (pre-registered 2026-09-04)

D1 UNIT = TASK. v5.2 counts "games" as ALFWorld trials (3,553). Measured: 1,465 unique tasks; trials of one task are
   near-duplicate games (same scene, same goal). Allocation is by whole task; every statistic clusters by task; the
   within-task ICC and the design effect DEFF are measured on S_dev2 and the MDE table republished before S_test (G5).
   Exact counts: T_A 799 tasks / 1,911 trials; T_B 666 / 1,642 (v5.2 estimated 1,937 / 1,616). Reserve per set becomes
   142 (T_B) / 411 (T_A); the balanced reserve is 284 pooled (v5.2: 232).
D2 ROOMS. cool/heat are kitchen-only, clean kitchen+bathroom; T_A spans all four room types. The off-type bank is largely
   an other-room bank. Claim wording: "task-type-and-room-specific"; per-room reporting; kitchen-only secondary.
D3 PARTITION CRITERION made concrete: proxy items = goal text + stored walkthrough of every other train trial; query =
   goal + first observation; top-5 MiniLM; cross-set share normalized by the other set's pool share; 7 admissible splits.
D4 OPTIMIZER = GEPA-lite with a local reflector (Qwen3-32B) and a one-sweep budget (DESIGN §3.4). The proposal's
   "350 rollouts ≈ one full sweep" is realized as exactly one sweep of P_train (300) + 50, so P_train coverage is 100%
   and the identity hash of v5.2 row 89 holds by construction. Consequence: candidate comparisons are across adjacent
   minibatches (unpaired); the acceptance rule and the training curves are published; G2 decides whether it worked.
   I_all covers ≈58% of the 600-game union (no identity requirement there; coverage reported).
D5 MODELS/SERVING. Agent Qwen3.5-27B or Qwen3-32B (screened); annotator the other; vLLM 0.13.0 rebuilt on NFS
   (`/home/work/neuro/vllm-env`) after the node's root filesystem was recycled; medgemma-27b-it and gpt-oss-120b present
   for Tier 1/2. Best-of-2 implemented as one request with n=2, counted as 2 calls.
D6 X_dist SOURCE. E1-provenance items are proposal ①'s `bank_A.jsonl` (multi-hop QA procedural items), rewritten into
   the ALFWorld item format by the annotator and token-matched — the concrete realization of v5.2's X_dist.
