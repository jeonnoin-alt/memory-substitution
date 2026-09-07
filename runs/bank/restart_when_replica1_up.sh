#!/bin/bash
# wait for vLLM replica 1, then move the own-rollout collection to both replicas with 32 workers (GPU rule)
cd /home/work/neuro/memory-substitution
for i in $(seq 1 120); do curl -sf localhost:8001/v1/models >/dev/null && break; sleep 5; done
curl -sf localhost:8001/v1/models >/dev/null || { echo "replica 1 not up after 10 min"; exit 1; }
p=$(cat runs/bank/own_rollouts.pid); kill $p 2>/dev/null; sleep 3; kill -9 $p 2>/dev/null
# wait for the pool's workers to die (they are children of $p)
sleep 5; echo "$(date +%H:%M:%S) restarting rollouts on both replicas; done so far: $(wc -l < runs/bank/own_rollouts_train.jsonl)"
bash runs/bank/start_own_rollouts.sh 32
