#!/usr/bin/env python3
"""Collect per-axis prescan_synth results into gaps.json (harness mode).
Usage: synth_collect.py <prescan_dir> <mapping.json {axis name: task_id}>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
W, mapping = sys.argv[1], json.load(open(sys.argv[2]))
gaps, missing = [], []
for axis, tid in mapping.items():
    path = os.path.join(TASKS_DIR, tid + ".output")
    d = None
    if os.path.exists(path):
        for t in reversed(assistant_texts(path)):
            try: x = parse_json(t)
            except Exception: continue
            if isinstance(x, dict) and "gaps" in x: d = x; break
    if d is None: missing.append(axis); continue
    d["axis"] = d.get("axis") or axis
    for g in d["gaps"]: g.setdefault("card_ids", []); g.setdefault("evidence_needed", "")
    gaps.append(d)
json.dump(gaps, open(os.path.join(W, "gaps.json"), "w"), indent=1, ensure_ascii=False)
print(f"axes with gaps: {len(gaps)} ({sum(len(g['gaps']) for g in gaps)} gaps); missing: {missing}")
