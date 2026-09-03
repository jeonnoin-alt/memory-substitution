#!/usr/bin/env python3
"""Numeric gate evaluation per frozen DESIGN §6. Mechanical where possible; annotator only where required."""
import json, os, argparse, sys, datetime
HERE=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(HERE,"..","runs")
B=os.path.join(HERE,"..","data","bank"); PRE=os.path.join(HERE,"..","prereg")
import env

def load(arm,split,seed):
    out={}
    for l in open(os.path.join(R,f"{arm}__{split}__s{seed}.jsonl")):
        try: r_=json.loads(l)
        except Exception: continue
        if "em" in r_: out[r_["qid"]]=r_   # last record per qid wins (retries append)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--stage",choices=["dev"],required=True); a=ap.parse_args()
    log=open(os.path.join(PRE,"GATES_LOG.md"),"a"); out=[]; fail=[]
    def rec(g,ok,detail):
        out.append(f"{g} {'PASS' if ok else 'FAIL'} — {detail}")
        if not ok: fail.append(g)
    m0=load("M0","S_dev1",11); m1=load("M1","S_dev1",11)
    ids=sorted(set(m0)&set(m1))
    fixes=sum(1 for i in ids if m0[i]["em"]==0 and m1[i]["em"]==1)
    breaks=sum(1 for i in ids if m0[i]["em"]==1 and m1[i]["em"]==0)
    rec("G-1", fixes>=6 and breaks>=6, f"n={len(ids)} fixes={fixes} breaks={breaks} (need >=6 each)")
    fs=load("M0_Fs","S_dev2",11)
    comp=sum(1 for r in fs.values() if r.get("citations") and r["citations"].get("quotes"))
    rec("G-2", comp>=65, f"compliance {comp}/{len(fs)} (need >=65)")
    # G-3 non-echo breaks: final answer not matching any injected item's stored answer (mechanical proxy: bank answers)
    bank_ans={json.loads(l)["src_qid"]: (json.loads(l).get("answer") or "") for l in open(os.path.join(B,"bank_A.jsonl"))}
    brk=[i for i in ids if m0[i]["em"]==1 and m1[i]["em"]==0]
    def echoed(rec_):
        f=(rec_.get("final") or "").lower()
        return any(ans and ans.lower() in f for ans in bank_ans.values())
    nonecho=sum(1 for i in brk if not echoed(m1[i]))
    rec("G-3", len(brk)>=10 and nonecho/max(len(brk),1)>=0.20, f"breaks={len(brk)} nonecho={nonecho} (need >=20% and >=10 breaks)")
    # G-4 stored-record truthfulness (mechanical: item answer == source question's gold)
    qs=env.load_questions(); items=[json.loads(l) for l in open(os.path.join(B,"bank_A.jsonl"))]
    truthful=sum(1 for it in items if it.get("answer") and env.score(it["answer"],qs[it["src_qid"]])["em"]==1)
    rec("G-4", truthful/max(len(items),1)>=0.70, f"truthful {truthful}/{len(items)} (need >=70%)")
    # G-6 automated leakage pre-pass (human check separately)
    reds=[json.loads(l) for l in open(os.path.join(B,"bank_A_redacted.jsonl"))]
    src_ans={it["src_qid"]:(it.get("answer") or "") for it in items}
    leak=sum(1 for r_ in reds if src_ans.get(r_["src_qid"]) and src_ans[r_["src_qid"]].lower() in r_["item"].lower())
    rec("G-6(auto)", leak/max(len(reds),1)<=0.10, f"auto-leak {leak}/{len(reds)} (need <=10%; human 150-check logged separately)")
    # G-8 under Fh on S_dev2
    fh=load("M1_Fh","S_dev2",11)
    unparse=sum(1 for r_ in fh.values() if r_.get("final") is None)
    rec("G-8", unparse/max(len(fh),1)<0.05, f"unparseable {unparse}/{len(fh)} (need <5%)")
    for line in out: print(line); log.write(datetime.date.today().isoformat()+" "+line+"\n")
    if fail: print("GATES FAILED:",fail); sys.exit(2)
    print("ALL DEV GATES PASS")
if __name__=="__main__": main()
