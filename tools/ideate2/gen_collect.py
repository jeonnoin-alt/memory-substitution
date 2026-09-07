#!/usr/bin/env python3
"""Collect axis_gen results from harness task outputs into <out>/jobs/axis_gen__<axis>.result.json, then merge.
Usage: gen_collect.py <gen_dir> <mapping.json {axis_slug: task_id}>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
G, mapping = sys.argv[1], json.load(open(sys.argv[2]))
REQ = ["Name", "Title", "Short Hypothesis", "Related Work", "Abstract", "Experiments", "Baselines and Ablations",
       "Falsifiable Predictions", "Measurement and Noise Control", "Preprint Collision Check", "Risk Factors and Limitations",
       "Addresses gap", "Not a restatement of"]
def _norm(i):   # generators sometimes return list-valued fields; downstream code expects strings
    for k, v in list(i.items()):
        if isinstance(v, list): i[k] = "\n".join(f"- {x}" for x in v)
    return i
done, missing, total = [], [], 0
for axis, tid in mapping.items():
    path = os.path.join(TASKS_DIR, tid + ".output")
    d = None
    if os.path.exists(path):
        for t in reversed(assistant_texts(path)):
            try: x = parse_json(t)
            except Exception: continue
            if isinstance(x, dict) and "proposals" in x: d = x; break
            if isinstance(x, list) and x and isinstance(x[0], dict) and "Short Hypothesis" in x[0]: d = {"proposals": x}; break
    if d is None: missing.append(axis); continue
    for p in d["proposals"]:
        _norm(p)
        p["_missing_fields"] = [k for k in REQ if not p.get(k)]
    json.dump(d, open(os.path.join(G, "jobs", f"axis_gen__{axis}.result.json"), "w"), indent=1, ensure_ascii=False)
    done.append(axis); total += len(d["proposals"])
print(f"collected {total} proposals from {len(done)} axes; missing: {missing}")
