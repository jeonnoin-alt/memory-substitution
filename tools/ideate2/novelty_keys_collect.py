#!/usr/bin/env python3
"""Collect batched novelty_keys results into keys.json {name: keys}.  Usage: novelty_keys_collect.py <novelty_dir> <mapping.json {batchNN: task_id}>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
W, mapping = sys.argv[1], json.load(open(sys.argv[2]))
keys, missing = {}, []
for b, tid in sorted(mapping.items()):
    path = os.path.join(TASKS_DIR, tid + ".output")
    if not os.path.exists(path): missing.append(b); continue
    arr = None
    for t in reversed(assistant_texts(path)):
        try: d = parse_json(t)
        except Exception: continue
        if isinstance(d, list) and d and isinstance(d[0], dict) and "keys" in d[0]: arr = d; break
    if arr is None: missing.append(b); continue
    for r in arr:
        k = r.get("keys") or {}
        for c, v in list(k.items()):                       # tolerate a single string per class
            if isinstance(v, str): k[c] = [v]
        keys[r.get("name")] = k
json.dump(keys, open(os.path.join(W, "keys.json"), "w"), indent=1, ensure_ascii=False)
print(f"keys for {len(keys)} ideas; missing batches {missing} -> {W}/keys.json")
