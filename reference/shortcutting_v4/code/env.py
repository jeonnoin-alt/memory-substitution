#!/usr/bin/env python3
"""Environment: dataset loading, BM25 search tool over each dataset's corpus, EM/F1 scoring.
Held-fixed infrastructure — no arm logic here."""
import json, os, re, string, functools
from rank_bm25 import BM25Okapi

HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,"..","data")
DATASETS=["hotpotqa","musique","2wikimultihopqa"]

def _tok(s): return re.findall(r"[a-z0-9]+", s.lower())

@functools.lru_cache(maxsize=None)
def load_questions():
    out={}
    for ds in DATASETS:
        for q in json.load(open(os.path.join(DATA,f"{ds}.json"))):
            out[f"{ds}::{q.get('_id') or q.get('id')}"]={"ds":ds,"question":q["question"],
                "answer":q["answer"],"aliases":q.get("answer_aliases") or [], "raw":q}
    return out

class Corpus:
    def __init__(self, ds):
        c=json.load(open(os.path.join(DATA,f"{ds}_corpus.json")))
        self.passages=[{"pid":i,"title":p.get("title",""),"text":p.get("text","")} for i,p in enumerate(c)]
        self.bm25=BM25Okapi([_tok(p["title"]+" "+p["text"]) for p in self.passages])
    def search(self, query, k=5):
        scores=self.bm25.get_scores(_tok(query))
        idx=sorted(range(len(scores)), key=lambda i:-scores[i])[:k]
        return [self.passages[i] for i in idx]

@functools.lru_cache(maxsize=None)
def corpus(ds): return Corpus(ds)

# ---- scoring (standard SQuAD-style normalization) ----
def _norm(s):
    s=s.lower(); s="".join(ch for ch in s if ch not in string.punctuation)
    s=re.sub(r"\b(a|an|the)\b"," ",s); return " ".join(s.split())
def em(pred, golds): return int(any(_norm(pred)==_norm(g) for g in golds))
def f1(pred, golds):
    def _f1(p,g):
        pt,gt=_norm(p).split(),_norm(g).split()
        if not pt or not gt: return float(pt==gt)
        common={}
        for t in pt: common[t]=min(pt.count(t),gt.count(t))
        overlap=sum(common.values())
        if overlap==0: return 0.0
        prec,rec=overlap/len(pt),overlap/len(gt)
        return 2*prec*rec/(prec+rec)
    return max(_f1(pred,g) for g in golds)
def score(pred, qrec):
    golds=[qrec["answer"]]+list(qrec["aliases"])
    return {"em":em(pred,golds),"f1":f1(pred,golds)}
