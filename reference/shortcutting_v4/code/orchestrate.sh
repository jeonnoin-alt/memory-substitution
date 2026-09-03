#!/bin/bash
# Master orchestrator — runs in tmux, survives the CLI session. Stage checkpoints in runs/STAGE.
set -uo pipefail
cd "$(dirname "$0")"
PY=/home/work/vllm-env/bin/python
R=../runs; mkdir -p $R
stage_done(){ grep -qx "$1" $R/STAGE 2>/dev/null; }
mark(){ echo "$1" >> $R/STAGE; echo "[$(date +%T)] STAGE DONE: $1"; }

# ---- Stage B: bank pipeline (agent bankgen must already exist) ----
if ! stage_done bank_distill; then
  $PY build_bank.py --stage distill --port 8001 --workers 12 && mark bank_distill || exit 1
fi
if ! stage_done bank_variants; then
  $PY build_bank.py --stage redact --port 8001 --workers 12 || exit 1
  $PY build_bank.py --stage infoswap --port 8001 --workers 12 || exit 1
  $PY build_bank.py --stage answeronly --port 8001 --workers 12 || exit 1
  $PY build_bank.py --stage curate --port 8001 --workers 12 || exit 1
  mark bank_variants
fi
# ---- Stage G: prechecks needing memory (G-1, G-3 via dev M1 run; G-8 via dev Fh run) ----
if ! stage_done gates_dev; then
  $PY run_arm.py --arm M1 --split S_dev1 --seed 11 --workers 24 --port 8000 --cfg arms/M1.json || exit 1
  $PY run_arm.py --arm M0_Fs --split S_dev2 --seed 11 --workers 24 --port 8002 --cfg arms/M0_Fs.json || exit 1
  $PY run_arm.py --arm M1_Fh --split S_dev2 --seed 11 --workers 24 --port 8003 --cfg arms/M1_Fh.json || exit 1
  $PY gates_eval.py --stage dev || { echo "GATE FAIL — stopping per THRESHOLDS"; exit 2; }
  mark gates_dev
fi
# ---- Stage M: main matrix, claim-priority order, spread over 3 agent ports ----
run(){ $PY run_arm.py --arm $1 --split ${4:-S_test} --seed $2 --workers 22 --port $3 --cfg arms/${1%%__*}.json; }
if ! stage_done matrix_core; then
  # 2-seed decisive arms (DESIGN §4 rows 1-14), 3 at a time across ports
  for S in 11 23; do
    run M0 $S 8000 & run M1 $S 8002 & run M2 $S 8003 & wait
    run ANCHOR $S 8000 & run M0_Fs $S 8002 & run M1_Fs $S 8003 & wait
    run M2_Fs $S 8000 & run ANCHOR_Fs $S 8002 & run M0_Fh $S 8003 & wait
    run M1_Fh $S 8000 & run M5 $S 8002 & run M5r $S 8003 & wait
  done
  mark matrix_core
fi
if ! stage_done matrix_null; then
  run M0 37 8000 & run M1 37 8002 & run M1_Fs 37 8003 & wait
  run M1_Fh 37 8000 & run M0_CB 11 8002 & run M2i 11 8003 & wait
  mark matrix_null
fi
if ! stage_done matrix_ctl; then
  run ANCHOR_NH 11 8000 & run M3 11 8002 & run M4 11 8003 & wait
  run M6 11 8000 & run M2_Fh 11 8002 & run ANCHOR_Fh 11 8003 & wait
  run M8 11 8000 & run M8 23 8002 & run IB_M0 11 8003 & wait
  run M8_Fh 11 8000 & run IB_M1 11 8002 & wait
  mark matrix_ctl
fi
echo "[$(date +%T)] ORCHESTRATOR COMPLETE (optimizer arms + EXAONE repl are separate stages)"
