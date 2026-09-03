#!/usr/bin/env python3
"""Aggregate harness reviews exactly as ideate.py does: weighted mean of per-reviewer score means
(novelty .3 / significance .25 / soundness .25 / feasibility .1 / clarity .1), worst verdict wins.
Usage: aggregate_reviews.py <out.json> <review1.json> <review2.json> ...
"""
import json, sys, re
W={"novelty":0.3,"significance":0.25,"soundness":0.25,"feasibility":0.1,"clarity":0.1}
ORDER={"reject":0,"borderline":1,"accept-worthy":2}
def load(p):
    s=open(p).read().strip()
    s=re.sub(r'^```(?:json)?\s*|\s*```$','',s,flags=re.S)   # tolerate fences
    m=re.search(r'\{.*\}',s,re.S); return json.loads(m.group(0))
out,ins=sys.argv[1],sys.argv[2:]
revs=[load(p) for p in ins]
means={k:round(sum(r[k] for r in revs)/len(revs),1) for k in W}
score=round(sum(W[k]*sum(r[k] for r in revs)/len(revs) for k in W),2)
verdict=min((r["verdict"] for r in revs), key=lambda v:ORDER.get(v,1))
agg={"score":score,"verdict":verdict,"means":means,"n_reviews":len(revs)}
json.dump({"aggregate":agg,"reviews":revs},open(out,"w"),indent=1,ensure_ascii=False)
print(json.dumps(agg))
for i,r in enumerate(revs,1):
    print(f"\n--- R{i} {r['verdict']} nov{r['novelty']} sig{r['significance']} snd{r['soundness']} fea{r['feasibility']} cla{r['clarity']}")
    for k in ("strongest_objection","missing_baseline","what_would_fix_it","closest_prior_work"):
        if k in r: print(f"[{k}] {r[k]}")
