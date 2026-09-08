#!/bin/bash
# Measurement C launcher (resumable). usage: start.sh [workers]
cd /home/work/neuro/memory-substitution
nohup /home/work/neuro/alfworld-env/bin/python code/run_static.py --out runs/static/static_c.jsonl --workers ${1:-32} >> runs/static/static_c.log 2>&1 &
echo $! > runs/static/static_c.pid; echo "measurement C started pid $!"
