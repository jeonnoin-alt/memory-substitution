#!/usr/bin/env python3
"""Parallel episode driver: run one arm config over a list of qids. Resumable (skips qids already in log)."""
import json, os, sys, argparse, concurrent.futures as cf
from openai import OpenAI
import agent, env

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--arm",required=True); ap.add_argument("--split",required=True)
    ap.add_argument("--seed",type=int,default=11); ap.add_argument("--limit",type=int,default=0)
    ap.add_argument("--workers",type=int,default=24); ap.add_argument("--port",default="8000")
    ap.add_argument("--cfg",default=None,help="json file with arm config overrides")
    a=ap.parse_args()
    HERE=os.path.dirname(os.path.abspath(__file__)); RUNS=os.path.join(HERE,"..","runs"); PRE=os.path.join(HERE,"..","prereg")
    splits=json.load(open(os.path.join(PRE,"splits.json")))["splits"]
    qids=splits[a.split][:a.limit or None]
    cfg={"arm":a.arm,"instruction_text":"","memory_text":"","floor":"none","max_calls":8,"floor_extra":3}
    if a.cfg: cfg.update(json.load(open(a.cfg)))
    cfg["arm"]=a.arm
    log_path=os.path.join(RUNS,f"{a.arm}__{a.split}__s{a.seed}.jsonl")
    done=set()
    if os.path.exists(log_path):
        for line in open(log_path):
            try:
                rec=json.loads(line)
                if "em" in rec: done.add(rec["qid"])   # error records get retried
            except Exception: pass
    todo=[q for q in qids if q not in done]
    print(f"{a.arm}/{a.split}/s{a.seed}: {len(done)} done, {len(todo)} todo")
    if not todo: return
    client=OpenAI(base_url=f"http://127.0.0.1:{a.port}/v1",api_key="x",timeout=600,max_retries=2)
    import memory as memmod
    qrecs=env.load_questions()
    log_f=open(log_path,"a")
    import threading; lock=threading.Lock()
    def one(qid):
        try:
            c=dict(cfg)
            if c.get("memory_arm"):
                c["memory_text"]=memmod.memory_text(c["memory_arm"],qrecs[qid],a.seed)
            if c.get("closed_book"):
                c["memory_text"]=""; c["instruction_text"]="Answer directly from your own knowledge. Do NOT use Search. Respond with Finish[answer]."
            rec=agent.run_episode(client,"agent",qid,c,a.seed,LockedF(log_f,lock))
            return rec["em"]
        except Exception as e:
            with lock: log_f.write(json.dumps({"qid":qid,"arm":a.arm,"seed":a.seed,"error":repr(e)[:200]})+"\n"); log_f.flush()
            return None
    class LockedF:
        def __init__(s,f,l): s.f=f; s.l=l
        def write(s,x):
            with s.l: s.f.write(x)
        def flush(s):
            with s.l: s.f.flush()
    import time; t0=time.time(); ok=0; err=0
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for i,r in enumerate(ex.map(one,todo),1):
            ok+=(r is not None); err+=(r is None)
            if i%20==0: print(f"  {i}/{len(todo)} ({i/(time.time()-t0)*3600:.0f} eps/hr, err {err})",flush=True)
    print(f"done {len(todo)} in {(time.time()-t0)/60:.1f} min; errors {err}")
if __name__=="__main__": main()
