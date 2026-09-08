#!/usr/bin/env python3
"""Recall of a novelty run against a ground-truth set of arXiv ids (e.g. the papers judges found that the generators missed).
Usage: novelty_recall.py <novelty_dir> <ground_truth.json {name: [ids]}> [--by-class]"""
import sys, os, json
D, gt = sys.argv[1], json.load(open(sys.argv[2])); hit = tot = 0; rows = []
for n, ids in gt.items():
    p = os.path.join(D, f"{n}.candidates.jsonl"); got = {}
    if os.path.exists(p):
        for l in open(p):
            r = json.loads(l); a = str(r.get("arxiv") or "").replace("arXiv:", "") or str(r.get("id", "")).replace("arxiv:", "")
            got[a] = r.get("queries", [])
    cj = os.path.join(D, f"{n}.card.json"); qcls = {}
    if os.path.exists(cj):
        qcls = {q["query"]: q["class"] for q in json.load(open(cj)).get("queries", []) if isinstance(q, dict)}
    h = [i for i in ids if i in got]; hit += len(h); tot += len(ids)
    via = {i: sorted({qcls.get(q, "?") for q in got[i]}) for i in h}
    rows.append(f"{n[:36].ljust(36)} {len(h)}/{len(ids)} " + " ".join(f"{i}({'/'.join(via[i])})" for i in h))
print("\n".join(rows)); print(f"recall of judge-found papers: {hit}/{tot} = {hit/max(1,tot):.2f}")
