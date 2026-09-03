#!/bin/bash
# EXAONE-4.0-32B as replication agent (arm 33). GPU via GPU env (default 1), port via PORT (default 8001).
export CUDA_VISIBLE_DEVICES=${GPU:-1}
export VLLM_WORKER_MULTIPROC_METHOD=spawn
exec /home/work/vllm-env/bin/vllm serve /home/work/neuro/models/EXAONE-4.0-32B \
  --served-model-name agent --port ${PORT:-8001} \
  --tensor-parallel-size 1 --max-model-len 16384 --max-num-seqs 32 \
  --gpu-memory-utilization 0.90 --trust-remote-code
