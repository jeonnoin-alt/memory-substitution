#!/bin/bash
# usage: novelty_queue.sh <topic> <wait_pid>  — waits for a running novelty_check (S2 rate limit is per key) then runs the topic's search
T=$1; W=$2; cd /home/work/neuro/memory-substitution
set -a; . /home/work/.s2_env; set +a
while [ -n "$W" ] && kill -0 $W 2>/dev/null; do sleep 20; done
exec /home/work/neuro/alfworld-env/bin/python -u tools/ideate2/novelty_check.py --ideas runs_ideate2/gen_$T/ideas.json --out runs_ideate2/gen_$T/novelty --keys runs_ideate2/gen_$T/novelty/keys.json --s2-queries 2
