#!/usr/bin/env python3
"""Pre-registered statistics: exact McNemar, paired bootstrap, TOST-by-CI for paired EM differences,
fix/break decomposition. Single source of truth for all tables."""
import json, os, math, itertools
from scipy import stats as sps
import numpy as np

def load(arm, split, seed, runs):
    p=os.path.join(runs,f"{arm}__{split}__s{seed}.jsonl")
    out={}
    for line in open(p):
        r=json.loads(line)
        if "em" in r: out[r["qid"]]=r
    return out

def paired(a, b):
    """a,b: dict qid->rec. Returns aligned lists over the intersection."""
    ids=sorted(set(a)&set(b))
    return ids,[a[i] for i in ids],[b[i] for i in ids]

def fix_break(base, treat):
    ids,A,B=paired(base,treat)
    fix=sum(1 for x,y in zip(A,B) if x["em"]==0 and y["em"]==1)
    brk=sum(1 for x,y in zip(A,B) if x["em"]==1 and y["em"]==0)
    return {"n":len(ids),"fix":fix,"break":brk,"net":(fix-brk)/max(len(ids),1)}

def mcnemar_exact(base, treat):
    fb=fix_break(base,treat); n01,n10=fb["fix"],fb["break"]
    n=n01+n10
    p=1.0 if n==0 else min(1.0, 2*sum(math.comb(n,k) for k in range(0,min(n01,n10)+1))*0.5**n)
    return {**fb,"discordant":n,"p_exact":p}

def boot_ci(base, treat, metric="em", iters=10000, seed=7):
    ids,A,B=paired(base,treat)
    d=np.array([b[metric]-a[metric] for a,b in zip(A,B)],dtype=float)
    rng=np.random.default_rng(seed)
    means=np.array([d[rng.integers(0,len(d),len(d))].mean() for _ in range(iters)])
    return {"delta":float(d.mean()),"lo":float(np.percentile(means,2.5)),"hi":float(np.percentile(means,97.5))}

def tost(base, treat, margin, metric="em", iters=10000):
    """Equivalence by 90% CI within +-margin (CI-inclusion TOST equivalent)."""
    ids,A,B=paired(base,treat)
    d=np.array([b[metric]-a[metric] for a,b in zip(A,B)],dtype=float)
    rng=np.random.default_rng(7)
    means=np.array([d[rng.integers(0,len(d),len(d))].mean() for _ in range(iters)])
    lo,hi=np.percentile(means,5),np.percentile(means,95)
    return {"delta":float(d.mean()),"ci90":[float(lo),float(hi)],"margin":margin,
            "equivalent":bool(lo>-margin and hi<margin),
            "inconclusive":bool(not(lo>-margin and hi<margin) and not(lo>margin or hi<-margin))}

def null_floor(same_arm_seed_a, same_arm_seed_b, metric="em"):
    """Treatment-free apparent-delta distribution between two seeds of the same arm."""
    ids,A,B=paired(same_arm_seed_a,same_arm_seed_b)
    d=[abs(b[metric]-a[metric]) for a,b in zip(A,B)]
    return {"n":len(ids),"mean_abs_delta":float(np.mean(d)),
            "agg_delta":abs(float(np.mean([b[metric] for b in B]))-float(np.mean([a[metric] for a in A])))}

def holm(pvals):
    order=sorted(range(len(pvals)),key=lambda i:pvals[i]); m=len(pvals); adj=[0]*m; mx=0
    for rank,i in enumerate(order):
        mx=max(mx,(m-rank)*pvals[i]); adj[i]=min(1.0,mx)
    return adj
