# Step 0 — starting facts for the parametric-vs-in-context brief (2026-09-07)

Purpose: give the next brief measured numbers from this node instead of the old pilot's, and check that LoRA
training is feasible here. Not confirmatory; no pre-registration; results go into the brief as "starting position".

## Node facts that shape the design
- 2× A100 80GB (the earlier brief said 4). GPU keep-alive daemon (`gpu_burst`) left running (≈1.2 GB, ~20 % util).
- Local models only: Qwen3-32B, Qwen3.5-27B, gpt-oss-120b, Qwen3.5-122B-A10B-FP8, EXAONE-4.0-32B, medgemma-27b, biomistral-7b.
  HF weight downloads and ModelScope are blocked (config.json resolves, LFS/CDN does not), so no 7–8B instruct model.
- vLLM 0.13.0 in `vllm-env` serves Qwen3 (transformers 4.57.6 does not know `qwen3_5`, so Qwen3.5-27B cannot be
  served or trained without upgrading transformers; Qwen3-32B chosen as the agent and LoRA target).
- `download.pytorch.org` unreachable; PyPI reachable → peft 0.20 / bitsandbytes 0.50 / accelerate installed into `vllm-env`.
- ALFWorld json_2.1.1 reconstructed data: train 3,553 trials / 1,465 tasks; valid_seen 140 games (137 tasks);
  valid_unseen 134 games (47 tasks). TextWorld's grammar parser is not thread-safe → one process per episode worker.

## Measurement A — in-context retrieval k-sweep (paired)
- Agent: Qwen3-32B, thinking off, temperature 0.7, max 160 tokens/action, ReAct scaffold (DESIGN.md §5), step limit 30,
  one re-prompt on a non-admissible reply then a no-op step. Two vLLM replicas (one per GPU), 24 episode workers.
- Bank: one expert walkthrough per train task replayed in the env (goal, actions, observations), successful only.
  Retrieval: MiniLM cosine on the goal sentence; top-k prefix shared across k so k=1 ⊂ k=3 ⊂ k=7.
- Cells: {valid_seen, valid_unseen} × k ∈ {0,1,3,7} × seeds {11,23}; identical (game, seed) across k.
- Stats (`code/stats.py`): fixed/broken counts vs k=0, exact McNemar, net gain per 100 with task-cluster bootstrap CIs,
  timeout and invalid-action decomposition, injected-token estimate.
- Output: `runs/sweep/k_sweep.jsonl` (append-only, resumable), log `runs/sweep/k_sweep.log`.

## Measurement B — LoRA feasibility (after A frees a GPU)
- `code/lora_sft.py`: QLoRA (4-bit nf4) rank-32 on Qwen3-32B, step-level SFT on the expert bank rendered with the
  agent's scaffold; report tokens/s, peak memory, loss over ~200 steps. Establishes whether the parametric arm fits
  one A100 and how long a training arm takes; not an accuracy claim.

## What goes into the brief
- The k at which retrieval helps / harms on this backbone (if any), with CIs, per split.
- Whether the +0.6-point in-context gain of the old pilot (27B, different bank) reproduces with an expert bank.
- Training cost per LoRA arm and peak memory → arm budget for the confirmatory design.
