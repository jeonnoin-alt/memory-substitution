#!/usr/bin/env python3
"""Collect revised IDEA JSONs from harness task outputs into <gen_dir>/ideas_r2.json (merging with existing entries).
Usage: revise_collect.py <gen_dir> <mapping.json {name: task_id}>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
G, mapping = sys.argv[1], json.load(open(sys.argv[2]))
out = os.path.join(G, "ideas_r2.json")
cur = {i["Name"]: i for i in json.load(open(out))} if os.path.exists(out) else {}
got, missing = [], []
for name, tid in mapping.items():
    path = os.path.join(TASKS_DIR, tid + ".output")
    if not os.path.exists(path): missing.append(name); continue
    d = None
    for t in reversed(assistant_texts(path)):
        try: x = parse_json(t)
        except Exception: continue
        if isinstance(x, dict) and "Short Hypothesis" in x and "Name" in x: d = x; break
    if d is None: missing.append(name); continue
    for k, v in list(d.items()):
        if isinstance(v, list): d[k] = "\n".join(f"- {s}" for s in v)
    d["Name"] = name; cur[name] = d; got.append(name)
    os.makedirs(os.path.join(G, "revise"), exist_ok=True)
    json.dump(d, open(os.path.join(G, "revise", f"{name}.r2.json"), "w"), indent=1, ensure_ascii=False)
json.dump(list(cur.values()), open(out, "w"), indent=1, ensure_ascii=False)
print(f"revised collected: {got}; missing: {missing}; ideas_r2.json has {len(cur)}")
