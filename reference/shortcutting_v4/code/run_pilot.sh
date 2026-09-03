#!/bin/bash
# Pilot: G-P0 smoke (20 instances M0), then G-P2 headroom (S_dev1 150 M0), reporting throughput.
set -e
cd "$(dirname "$0")"
PY=/home/work/vllm-env/bin/python
echo "== G-P0 smoke: M0 x 20 (S_dev2) =="
$PY run_arm.py --arm M0 --split S_dev2 --seed 11 --limit 20 --workers 8
echo "== G-P2 headroom: M0 x 150 (S_dev1) =="
$PY run_arm.py --arm M0 --split S_dev1 --seed 11 --workers 24
$PY - <<'PYEOF'
import json
recs=[json.loads(l) for l in open("../runs/M0__S_dev1__s11.jsonl") if "em" in json.loads(l)]
em=sum(r["em"] for r in recs)/max(len(recs),1)
f1=sum(r["f1"] for r in recs)/max(len(recs),1)
calls=sum(r["calls"] for r in recs)/max(len(recs),1)
print(f"G-P2: n={len(recs)} EM={em:.3f} F1={f1:.3f} mean_calls={calls:.2f}")
print("GATE:", "PASS" if 0.15<=em<=0.85 else "FAIL")
PYEOF
