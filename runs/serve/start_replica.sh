#!/bin/bash
# usage: start_replica.sh <gpu index>   -> vLLM Qwen3-32B replica on port 800<gpu>, pid in runs/serve/vllm_gpu<gpu>.pid
g=${1:?gpu index}; cd /home/work/neuro/memory-substitution
CUDA_VISIBLE_DEVICES=$g nohup /home/work/neuro/vllm-env/bin/python -m vllm.entrypoints.openai.api_server \
  --model /home/work/neuro/models/qwen3-32b --served-model-name agent --tensor-parallel-size 1 \
  --max-model-len 16384 --gpu-memory-utilization 0.90 --enforce-eager --disable-custom-all-reduce \
  --port 800$g >> runs/serve/vllm_agent_gpu$g.log 2>&1 &
echo $! > runs/serve/vllm_gpu$g.pid; echo "replica $g started pid $! port 800$g"
