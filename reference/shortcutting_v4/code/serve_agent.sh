#!/bin/bash
# Qwen3.5-27B agent engine. GPU via CUDA_VISIBLE_DEVICES (default 0), port via PORT (default 8000).
export CUDA_VISIBLE_DEVICES=${GPU:-0}
export VLLM_WORKER_MULTIPROC_METHOD=spawn
exec /home/work/vllm-env/bin/vllm serve /home/work/neuro/models/qwen3.5-27b \
  --served-model-name agent --port ${PORT:-8000} \
  --tensor-parallel-size 1 --max-model-len 16384 --max-num-seqs 32 \
  --gpu-memory-utilization 0.90 --trust-remote-code
