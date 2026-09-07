#!/usr/bin/env python3
"""Collect batched prescan_card results into cards.jsonl (harness mode).
Usage: cards_collect.py <prescan_dir> <mapping.json {batchNN: task_id}> <axes.json>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from ingest_sections import assistant_texts
from lit import load_jsonl
W, mapping, axes = sys.argv[1], json.load(open(sys.argv[2])), json.load(open(sys.argv[3]))["axes"]
axis_names = [a["name"] for a in axes]
papers = {p.id: p for p in load_jsonl(os.path.join(W, "papers.jsonl"))}
cards, missing = [], []
for b, tid in sorted(mapping.items()):
    path = os.path.join(TASKS_DIR, tid + ".output")
    if not os.path.exists(path): missing.append(b); continue
    arr = None
    for t in reversed(assistant_texts(path)):
        try: d = parse_json(t)
        except Exception: continue
        if isinstance(d, list) and d and isinstance(d[0], dict) and "claim" in d[0]: arr = d; break
    if arr is None: missing.append(b); continue
    for c in arr:
        ax = c.get("axes") or []
        if isinstance(ax, str):   # model wrote prose: map back to axis names by substring
            ax = [n for n in axis_names if n.lower() in ax.lower()]
        c["axes"] = [a for a in ax if a in axis_names] or [n for n in axis_names if n.lower() in json.dumps(c).lower()][:1]
        p = papers.get(c.get("id"))
        if p is None: c["_unknown_id"] = True
        else: c["title"] = p.title; c["date"] = c.get("date") or p.date or p.year
        cards.append(c)
with open(os.path.join(W, "cards.jsonl"), "w") as f:
    for c in cards: f.write(json.dumps(c, ensure_ascii=False) + "\n")
lim = sum(1 for c in cards if c.get("stated_limitations", "not stated") != "not stated")
print(f"cards: {len(cards)} ({len(papers)} papers; missing batches {missing}); with stated limitations: {lim}; unknown ids: {sum(1 for c in cards if c.get('_unknown_id'))}")
from collections import Counter
print("per axis:", dict(Counter(a for c in cards for a in c["axes"])))
