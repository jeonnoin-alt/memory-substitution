#!/bin/bash
# (re)start the paired k-sweep; resumable. Usage: bash runs/sweep/start.sh [workers]
cd /home/work/neuro/memory-substitution
W=${1:-32}
nohup /home/work/neuro/alfworld-env/bin/python code/run_sweep.py --splits valid_seen,valid_unseen --ks 0,1,3,7 --seeds 11,23 --workers $W --out runs/sweep/k_sweep.jsonl >> runs/sweep/k_sweep.log 2>&1 &
echo $! > runs/sweep/k_sweep.pid; echo "sweep started pid $! workers $W"
