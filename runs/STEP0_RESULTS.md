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
