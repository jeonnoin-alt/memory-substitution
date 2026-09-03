#!/usr/bin/env python3
"""Bank A: run agent on S_bank (no memory), distill solved episodes into ExpeL-style items via annotator.
Then M2 (answer-redacted) via annotator. Deterministic outputs to data/bank/."""
import json, os, argparse, concurrent.futures as cf, threading
from openai import OpenAI
import env

HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.join(HERE,"..")
BANK=os.path.join(W,"data","bank"); os.makedirs(BANK,exist_ok=True)

DISTILL=("You will see a question-answering episode that ended CORRECTLY. Distill it into a reusable memory item.\n"
 "Format exactly:\nINSIGHT: <one transferable lesson about how to solve questions like this>\n"
 "PROCEDURE: <which searches, in what order, and how to disambiguate>\n"
 "OUTCOME: The answer was '<final answer>'.\n\nEpisode:\nQuestion: {q}\nSearches: {s}\nFinal answer: {a}")
REDACT=("Rewrite this memory item with EVERY answer, result value, or completion statement removed, keeping the "
 "procedure intact. Replace removed content with neutral filler of similar length so total length stays within 5%. "
 "Do NOT reveal what the answer was, even indirectly.\n\nItem:\n{item}\n\nRewritten item:")

def call(client,prompt,max_tokens=500):
    r=client.chat.completions.create(model="annotator",messages=[{"role":"user","content":prompt}],
        temperature=0.0,max_tokens=max_tokens,extra_body={"chat_template_kwargs":{"enable_thinking":False}})
    return (r.choices[0].message.content or "").strip()


def _resume(path, key_of, todo):
    """Skip records already in path (by src_qid); return (append-handle, remaining)."""
    done=set()
    if os.path.exists(path):
        for l in open(path):
            try: done.add(json.loads(l)["src_qid"])
            except Exception: pass
    left=[x for x in todo if key_of(x) not in done]
    if done: print(f"resume: {len(done)} already in {os.path.basename(path)}, {len(left)} to go")
    return open(path,"a"), left

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--stage",choices=["distill","redact","infoswap","answeronly","curate"],required=True)
    ap.add_argument("--port",default="8001"); ap.add_argument("--workers",type=int,default=12)
    a=ap.parse_args()
    client=OpenAI(base_url=f"http://127.0.0.1:{a.port}/v1",api_key="x",timeout=600)
    if a.stage=="distill":
        eps=[json.loads(l) for l in open(os.path.join(W,"runs","bankgen__S_bank__s11.jsonl"))]
        solved=[e for e in eps if e.get("em")==1 and e.get("final")]
        print(f"{len(solved)}/{len(eps)} solved episodes to distill")
        out,solved=_resume(os.path.join(BANK,"bank_A.jsonl"),lambda e:e["qid"],solved); lock=threading.Lock()
        def one(e):
            q=env.load_questions()[e["qid"]]
            item=call(client,DISTILL.format(q=q["question"],s=e.get("searches",0),a=e["final"]))
            with lock: out.write(json.dumps({"src_qid":e["qid"],"ds":q["ds"],"item":item,"answer":e["final"]})+"\n"); out.flush()
        with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(one,solved))
    else:
        items=[json.loads(l) for l in open(os.path.join(BANK,"bank_A.jsonl"))]
        PROMPTS={
         "redact":(REDACT,"bank_A_redacted.jsonl",True),
         "infoswap":(("Rewrite this memory item replacing the final ANSWER with a DIFFERENT, equally informative "
            "factual detail about the same topic that is NOT the answer. Keep procedure intact, length within 5%.\n\n"
            "Item:\n{item}\n\nRewritten item:"),"bank_A_infoswap.jsonl",True),
         "answeronly":(("Rewrite this memory item keeping ONLY the OUTCOME line (the answer statement) verbatim; "
            "delete INSIGHT and PROCEDURE and replace them with neutral task-generic filler so total length stays "
            "within 5%.\n\nItem:\n{item}\n\nRewritten item:"),"bank_A_answeronly.jsonl",False),
        }
        if a.stage=="curate":
            # M8: contradiction-pruning + call-balance rebalancing (deterministic heuristic + LLM contradiction check)
            out,items=_resume(os.path.join(BANK,"bank_A_curated.jsonl"),lambda it:it["src_qid"],items); lock=threading.Lock()
            def one(it):
                v=call(client,"Does this memory item contain internal contradictions or claims unsupported by its own "
                       "procedure? Answer KEEP or DROP only.\n\n"+it["item"],max_tokens=8)
                if "DROP" not in v.upper():
                    with lock: out.write(json.dumps(it)+"\n"); out.flush()
            with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(one,items))
        else:
            tmpl,fname,drop_ans=PROMPTS[a.stage]
            out,items=_resume(os.path.join(BANK,fname),lambda it:it["src_qid"],items); lock=threading.Lock()
            def one(it):
                red=call(client,tmpl.format(item=it["item"]))
                rec={**it,"item":red}
                if drop_ans: rec["answer"]=None
                with lock: out.write(json.dumps(rec)+"\n"); out.flush()
            with cf.ThreadPoolExecutor(a.workers) as ex: list(ex.map(one,items))
    print("stage done")
if __name__=="__main__": main()
