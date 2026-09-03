#!/usr/bin/env python3
"""Optimizer rollout engine (GEPA-lite / MIPRO-lite). Evaluates instruction candidates on S_opt
minibatches with the local agent; reflection happens OUTSIDE (harness frontier writes candidates).
State per run in runs/opt/<run>/: state.json (budget ledger), cand_<id>.json, eval log JSONLs.
Usage:
  eval:    opt_driver.py --run gepa_m1 --evaluate cand_003 --batch 15 --port 8002 [--memory M1] [--seed 11]
  status:  opt_driver.py --run gepa_m1 --status
Budget cap 350 rollouts per run enforced here (DESIGN 4)."""
import json, os, sys, argparse, random, concurrent.futures as cf, threading
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from openai import OpenAI
import agent, env, memory as memmod

HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.join(HERE,"..")
OPT=os.path.join(W,"runs","opt")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--run",required=True); ap.add_argument("--evaluate"); ap.add_argument("--status",action="store_true")
    ap.add_argument("--batch",type=int,default=15); ap.add_argument("--port",default="8002")
    ap.add_argument("--memory",default=None); ap.add_argument("--seed",type=int,default=11)
    ap.add_argument("--workers",type=int,default=15)
    a=ap.parse_args()
    D=os.path.join(OPT,a.run); os.makedirs(D,exist_ok=True)
    sp=os.path.join(D,"state.json")
    st=json.load(open(sp)) if os.path.exists(sp) else {"spent":0,"batches":[],"scores":{}}
    if a.status:
        print(json.dumps(st,indent=1)); return
    cand=json.load(open(os.path.join(D,f"{a.evaluate}.json")))   # {"instruction": "..."}
    if st["spent"]+a.batch>350: raise SystemExit(f"budget: {st['spent']}+{a.batch}>350")
    splits=json.load(open(os.path.join(W,"prereg","splits.json")))["splits"]
    # deterministic shared minibatch sequence per run (same batch index -> same qids for every candidate)
    rng=random.Random(20260831); order=splits["S_opt"][:]; rng.shuffle(order)
    bidx=st["scores"].get(a.evaluate,{}).get("next_batch",0)
    qids=[order[(bidx*a.batch+j)%len(order)] for j in range(a.batch)]
    client=OpenAI(base_url=f"http://127.0.0.1:{a.port}/v1",api_key="x",timeout=600,max_retries=2)
    qrecs=env.load_questions()
    logp=os.path.join(D,f"eval_{a.evaluate}.jsonl"); log_f=open(logp,"a"); lock=threading.Lock()
    class LF:
        def write(s,x):
            with lock: log_f.write(x)
        def flush(s):
            with lock: log_f.flush()
    cfg={"arm":f"{a.run}:{a.evaluate}","instruction_text":cand["instruction"],"memory_text":"",
         "floor":"none","max_calls":8,"floor_extra":3}
    def one(qid):
        c=dict(cfg)
        if a.memory: c["memory_text"]=memmod.memory_text(a.memory,qrecs[qid],a.seed)
        try: return agent.run_episode(client,"agent",qid,c,a.seed,LF())
        except Exception as e:
            with lock: log_f.write(json.dumps({"qid":qid,"error":repr(e)[:150]})+"\n")
            return None
    with cf.ThreadPoolExecutor(a.workers) as ex: recs=[r for r in ex.map(one,qids) if r]
    emv=sum(r["em"] for r in recs)/max(len(recs),1)
    sc=st["scores"].setdefault(a.evaluate,{"evals":[],"next_batch":0})
    sc["evals"].append({"batch":bidx,"n":len(recs),"em":round(emv,4)})
    sc["next_batch"]=bidx+1
    st["spent"]+=len(recs); st["batches"].append({"cand":a.evaluate,"batch":bidx,"em":round(emv,4)})
    json.dump(st,open(sp,"w"),indent=1)
    # 실패 사례 요약(리플렉션용)을 함께 남긴다
    fails=[{"q":qrecs[r["qid"]]["question"][:140],"final":r["final"],"gold":qrecs[r["qid"]]["answer"],
            "searches":r["searches"]} for r in recs if r["em"]==0][:8]
    json.dump(fails,open(os.path.join(D,f"fails_{a.evaluate}_b{bidx}.json"),"w"),indent=1)
    print(f"{a.run}/{a.evaluate} batch{bidx}: EM={emv:.3f} n={len(recs)} spent={st['spent']}/350")
if __name__=="__main__": main()
