#!/usr/bin/env python3
"""Flatten batched gate_adjudicate results (harness task outputs or api result files) and apply them.
Usage: gate_collect.py <gate_dir> <mapping.json {batchNN: task_id}>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
import gate
gdir, mapping = sys.argv[1], json.load(open(sys.argv[2]))
adj, done = {}, []
for b, tid in sorted(mapping.items()):
    path = os.path.join(TASKS_DIR, tid + ".output")
    if not os.path.exists(path): continue
    arr = None
    for t in reversed(assistant_texts(path)):
        try:
            d = parse_json(t)
        except Exception: continue
        if isinstance(d, list) and d and isinstance(d[0], dict) and "pair_id" in d[0]: arr = d; break
    if arr is None: continue
    done.append(b)
    for r in arr: adj[r["pair_id"]] = {"label": r.get("label"), "reason": r.get("reason", "")}
json.dump(adj, open(os.path.join(gdir, "adjudications.json"), "w"), indent=1, ensure_ascii=False)
rep = gate.apply(os.path.join(gdir, "gate_report.json"), adj, gdir)
labels = {}
for p in rep["pairs"]:
    if "label" in p: labels[p["label"]] = labels.get(p["label"], 0) + 1
print(f"batches done: {done}; adjudicated {len(adj)}/{len(rep['pairs'])} pairs; labels: {labels}")
for p in rep["pairs"]:
    if p.get("label") and p["label"] != "distinct": print(f"  [{p['label']}] {p['a']}  vs  {p['b'][:60]}  (sim {p['sim']})")
print("decisions:", json.dumps(rep["decisions"], indent=1))
