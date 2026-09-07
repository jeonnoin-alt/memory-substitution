# Step 0 results — Measurement A (paired k-sweep), 2026-09-07

Agent Qwen3-32B (thinking off, T=0.7), expert-walkthrough bank (1,465 train tasks, one trial each, all successful),
MiniLM retrieval on the goal sentence, top-k prefix shared across k. 274 games × k∈{0,1,3,7} × seeds {11,23} = 2,192
episodes, 0 errors, ~1 h on two vLLM replicas with 32 episode workers. Paired on identical (game, seed).

| split | k | success | fixed | broken | net/100 [95% task-cluster CI] | McNemar p | timeout | injected tok |
|---|---|---|---|---|---|---|---|---|
| valid_seen (n=280) | 0 | 0.536 | – | – | – | – | 0.46 | 0 |
| | 1 | 0.739 | 75 | 18 | +20.4 [+12.9, +28.3] | <0.001 | 0.26 | ~150 |
| | 3 | 0.807 | 93 | 17 | +27.1 [+18.7, +35.7] | <0.001 | 0.19 | ~450 |
| | 7 | 0.846 | 98 | 11 | +31.1 [+23.3, +39.3] | <0.001 | 0.15 | ~1,050 |
| valid_unseen (n=268) | 0 | 0.549 | – | – | – | – | 0.45 | 0 |
| | 1 | 0.776 | 80 | 19 | +22.8 [+13.1, +32.2] | <0.001 | 0.22 | ~140 |
| | 3 | 0.869 | 98 | 12 | +32.1 [+22.9, +41.0] | <0.001 | 0.13 | ~430 |
| | 7 | 0.877 | 101 | 13 | +32.8 [+23.1, +42.6] | <0.001 | 0.12 | ~1,010 |

By task type (k=3 vs k=0, pooled splits, net/100): clean +55, heat +41, cool +39, pick-two +18, pick-and-place +15,
look-at-in-light −5 (n=62; 5 fixed / 8 broken).

Reading: (1) on this backbone with an expert bank the retrieval channel is worth +20 to +33 points, an order of magnitude
above the old pilot's +0.6 (27B, self-built bank); the gain is carried by the three multi-step task types whose procedure
(clean/heat/cool then place) the agent otherwise fails to complete within 30 steps — most fixes convert timeouts.
(2) No high-dose harm: k=7 ≥ k=3 ≥ k=1 on both splits; broken counts fall with k. The old pilot's "seven items break, three
do not" does not reproduce here. (3) unseen ≈ seen, so the gain is not scene-bound; it is procedure-bound, which is the
near-duplicate-template leakage concern (same task type ⇒ near-identical procedure) the previous round's judges raised.
(4) look-at-in-light is the one type where retrieval nets negative — a candidate harm regime for the parametric comparison.
Files: `runs/sweep/k_sweep_final.jsonl` (episodes with full histories), `code/stats.py`.

# Measurement B — parametric route cost (QLoRA on Qwen3-32B, one A100 80GB), 2026-09-07

Step-level SFT on the expert bank (1,465 won trajectories → 8,854 (prompt, action) examples, ~300 tokens each; chat
template, loss on the action tokens only). QLoRA nf4, rank 32, lr 1e-4, max-len 2048, `--enforce` none (HF peft 0.20,
bitsandbytes 0.50, inside `vllm-env`). Loss falls from ~0.8 to ~0.1 within 20–60 optimizer steps (procedure is easy to fit).

| config | examples seen | wall | tok/s | s/example | peak GPU mem | epoch (8,854 ex) est. |
|---|---|---|---|---|---|---|
| batch 1, grad-accum 4, 60 steps | 240 | 377 s | 190 | 1.57 | 29.8 GB | 3.9 h |
| batch 4, grad-accum 2, 20 steps | 160 | 128 s | 385 | 0.80 | 31.5 GB | 2.0 h |

Reading: one epoch of the whole expert pool costs ~2 GPU-hours on one A100 at batch 4 (memory headroom allows batch 8–16,
so ~1 h is plausible); the same pool in context costs ~430 prompt tokens per episode at k=3 (~1,010 at k=7). Training
throughput scales linearly with examples, so a pool-size sweep (10 %, 30 %, 100 % of the bank) is 0.2–2 h per arm and can
run on the second GPU while the first serves. The vLLM server needs a restart to serve a merged or LoRA-loaded checkpoint
(`--enable-lora` with rank 32 is supported by vLLM 0.13 for Qwen3), so evaluation of a trained arm costs one server
restart (~3 min) plus the k=0 sweep (~274 games × seeds). Files: `code/lora_sft.py`, `runs/lora/*/train_log.json`.

# Self-rollout pool (own k=0 successes on train tasks), 2026-09-07

`runs/bank/own_rollouts_train.jsonl`, Qwen3-32B k=0, seed 11, 30-step cap, both replicas (32 workers, ~20 episodes/min).
First pass (`--limit 1500`, alphabetical, so three types only): 1,500 episodes, 0 errors, 1,046 won (0.697); by type
pick_and_place 0.81, look_at_in_light 0.76, clean_then_place 0.42; mean 11.5 steps per won episode. The remaining 2,053 train
games (cool / heat / pick_two types) are being collected with the same launcher (`start_own_rollouts.sh 32 <servers> 0`).
Use: the brief's "both pools" rule (expert = off-policy text, self-rollout = on-policy); note the pool is success-filtered and
type-skewed toward what the k=0 agent already solves, which several judges flagged as a selection confound for dose claims.
