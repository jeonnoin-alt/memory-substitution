#!/bin/bash
# collect the agent's own k=0 rollouts on train tasks (self-generated experience pool) on replica 0 only
cd /home/work/neuro/memory-substitution
nohup /home/work/neuro/alfworld-env/bin/python code/run_sweep.py --splits train --ks 0 --seeds 11 --limit 1500 --workers 16 --servers http://localhost:8000/v1 --out runs/bank/own_rollouts_train.jsonl >> runs/bank/own_rollouts.log 2>&1 &
echo $! > runs/bank/own_rollouts.pid; echo "own-rollout collection started pid $! (replica 0)"
