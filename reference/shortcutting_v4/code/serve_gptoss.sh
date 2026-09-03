#!/bin/bash
# gpt-oss-120b (mxfp4) as replication agent (arm 33). Single GPU.
export CUDA_VISIBLE_DEVICES=${GPU:-1}
export VLLM_WORKER_MULTIPROC_METHOD=spawn
exec /home/work/vllm-env/bin/vllm serve /home/work/neuro/models/gpt-oss-120b \
  --served-model-name agent --port ${PORT:-8001} \
  --tensor-parallel-size 1 --max-model-len 16384 --max-num-seqs 32 \
  --gpu-memory-utilization 0.90 --trust-remote-code
