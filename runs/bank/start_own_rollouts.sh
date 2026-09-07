#!/bin/bash
# collect the agent's own k=0 rollouts on train tasks (self-generated experience pool)
# usage: start_own_rollouts.sh [workers] [servers]   (resumable: completed episodes in the JSONL are skipped)
cd /home/work/neuro/memory-substitution
W=${1:-32}; S=${2:-http://localhost:8000/v1,http://localhost:8001/v1}
nohup /home/work/neuro/alfworld-env/bin/python code/run_sweep.py --splits train --ks 0 --seeds 11 --limit 1500 --workers $W --servers $S --out runs/bank/own_rollouts_train.jsonl >> runs/bank/own_rollouts.log 2>&1 &
echo $! > runs/bank/own_rollouts.pid; echo "own-rollout collection started pid $! workers $W servers $S"
