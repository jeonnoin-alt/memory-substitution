#!/bin/bash
export CUDA_VISIBLE_DEVICES=${GPU:-1}
export VLLM_WORKER_MULTIPROC_METHOD=spawn
exec /home/work/vllm-env/bin/vllm serve /home/work/neuro/models/qwen3-32b \
  --served-model-name annotator --port ${PORT:-8001} \
  --tensor-parallel-size 1 --max-model-len 12288 --max-num-seqs 16 \
  --gpu-memory-utilization 0.92 --trust-remote-code
