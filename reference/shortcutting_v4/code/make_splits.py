#!/usr/bin/env python3
"""Seeded, stratified splits from the pooled 3,000 HippoRAG subset questions.
Deterministic: same seed -> same instance IDs. Writes prereg/splits.json (IDs only)."""
import json, random, hashlib, os
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,"..","data"); PRE=os.path.join(HERE,"..","prereg")
SEED=20260824
SPLITS=[("S_bank",400),("S_opt",150),("S_dev1",150),("S_dev2",100),("S_test",500)]  # total 1300
WEIGHTS={"hotpotqa":0.5,"musique":0.3,"2wikimultihopqa":0.2}

def qid(ds,q): return f"{ds}::{q.get('_id') or q.get('id')}"

pool={}
for ds in WEIGHTS:
    qs=json.load(open(os.path.join(DATA,f"{ds}.json")))
    ids=[qid(ds,q) for q in qs]
    assert len(ids)==len(set(ids)), ds
    pool[ds]=sorted(ids)          # sort -> clone-order independence
rng=random.Random(SEED)
for ds in pool: rng.shuffle(pool[ds])

out={name:[] for name,_ in SPLITS}
cursor={ds:0 for ds in pool}
for name,n in SPLITS:
    take={ds:int(round(n*w)) for ds,w in WEIGHTS.items()}
    diff=n-sum(take.values()); take["hotpotqa"]+=diff
    for ds,k in take.items():
        seg=pool[ds][cursor[ds]:cursor[ds]+k]
        assert len(seg)==k, (name,ds,"pool exhausted")
        out[name]+=seg; cursor[ds]+=k
flat=[i for v in out.values() for i in v]
assert len(flat)==len(set(flat))==1300
meta={"seed":SEED,"weights":WEIGHTS,"counts":{k:len(v) for k,v in out.items()},
      "hash":hashlib.sha256(json.dumps(out,sort_keys=True).encode()).hexdigest()}
json.dump({"meta":meta,"splits":out},open(os.path.join(PRE,"splits.json"),"w"),indent=1)
print("splits ok", meta["counts"], "hash", meta["hash"][:16])
