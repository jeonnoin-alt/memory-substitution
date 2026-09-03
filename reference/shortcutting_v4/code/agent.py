#!/usr/bin/env python3
"""ReAct episode executor. Arm-agnostic: memory text + instruction + enforcement come in as config."""
import json, os, re, time, hashlib
from openai import OpenAI
import env

SYS_BASE = """You are a research assistant answering questions using a search tool over a fixed document collection.

On each turn, do ONE of:
  Search[your query]   — retrieve relevant passages
  Finish[final answer] — give the final answer (a short phrase)

Think briefly before acting. Use multiple searches when the question has multiple parts.{instruction}{memory}"""

FLOOR_REJECT = ("Your answer was not accepted: before finishing you must output a line "
 "'Evidence: \"<exact quote 1>\" | \"<exact quote 2>\"' quoting passages retrieved IN THIS EPISODE that support the answer. "
 "If your current evidence is insufficient, Search again first.")

ACT_RE = re.compile(r"(Search|Finish)\[(.*?)\]", re.S)
EV_RE  = re.compile(r'Evidence:\s*(.+)', re.I)

def run_episode(client, model, qid, cfg, seed, log_f):
    """cfg: {arm, instruction_text, memory_text, floor: none|soft|hard, max_calls, floor_extra}"""
    q = env.load_questions()[qid]
    corpus = env.corpus(q["ds"])
    instr = ("\n\nIMPORTANT INSTRUCTION: " + cfg["instruction_text"]) if cfg.get("instruction_text") else ""
    mem   = ("\n\nRetrieved experience from past tasks (may or may not help):\n" + cfg["memory_text"]) if cfg.get("memory_text") else ""
    msgs=[{"role":"system","content":SYS_BASE.format(instruction=instr, memory=mem)},
          {"role":"user","content":"Question: "+q["question"]}]
    retrieved_texts=[]; searches=0; calls=0; floor_rejects=0
    max_calls=cfg.get("max_calls",8); extra=cfg.get("floor_extra",3)
    final=None; citations=None; t0=time.time(); toks=0
    finish_tried=False; nofinish_ext=0   # AMENDMENT A6 (prereg/AMENDMENTS.md)
    while calls < max_calls + (floor_rejects and extra or 0) + nofinish_ext:
        calls+=1
        r=client.chat.completions.create(model=model,messages=msgs,temperature=0.7,seed=seed*100003+calls,
            max_tokens=420, extra_body={"chat_template_kwargs":{"enable_thinking":False}})
        out=r.choices[0].message.content or ""
        toks+=(r.usage.completion_tokens or 0)+(r.usage.prompt_tokens or 0)
        m=ACT_RE.search(out)
        if not m:
            msgs+=[{"role":"assistant","content":out},{"role":"user","content":"Respond with Search[...] or Finish[...]."}]
            continue
        act,arg=m.group(1),m.group(2).strip()
        if act=="Search":
            searches+=1
            hits=corpus.search(arg,k=5)
            retrieved_texts+=[h["text"] for h in hits]
            obs="\n".join(f"[{h['title']}] {h['text'][:400]}" for h in hits)
            msgs+=[{"role":"assistant","content":out},{"role":"user","content":"Results:\n"+obs}]
            # A6: instruction-slot arms get ONE +extra extension if the budget would expire
            # with no Finish ever attempted (truncation artifact, not a behavior measurement)
            if (not finish_tried and nofinish_ext==0
                and calls >= max_calls + (floor_rejects and extra or 0)
                and (cfg.get("instruction_text") or cfg.get("floor")!="none")):
                nofinish_ext=extra
        else:  # Finish
            finish_tried=True
            ev=EV_RE.search(out); quotes=[]
            if ev: quotes=[s.strip() for s in re.findall(r'"([^"]{10,})"', ev.group(1))]
            supported=any(any(qt[:80] in t for t in retrieved_texts) for qt in quotes) if quotes else False
            if cfg.get("floor")=="hard" and not supported and floor_rejects<extra:
                floor_rejects+=1
                msgs+=[{"role":"assistant","content":out},{"role":"user","content":FLOOR_REJECT}]
                continue
            final=arg; citations={"quotes":quotes,"supported":supported}
            break
    # A8 (prereg/AMENDMENTS.md): terminal forced-Finish for instruction-slot arms — an episode
    # may not end answerless just because the model kept searching. One attempt; the hard floor
    # does not re-reject the terminal answer. forced_final is logged so over-search stays measurable.
    forced_final=False
    if final is None and (cfg.get("instruction_text") or cfg.get("floor")!="none"):
        calls+=1
        msgs+=[{"role":"user","content":"You have no search budget left. You MUST now answer. Respond with "
                "at most one short Evidence line, then Finish[your best answer] (a short phrase). Do NOT Search. "
                "Keep the response brief."}]
        r=client.chat.completions.create(model=model,messages=msgs,temperature=0.7,seed=seed*100003+calls,
            max_tokens=800, extra_body={"chat_template_kwargs":{"enable_thinking":False}})
        out=r.choices[0].message.content or ""
        toks+=(r.usage.completion_tokens or 0)+(r.usage.prompt_tokens or 0)
        fins=[mm for mm in ACT_RE.finditer(out) if mm.group(1)=="Finish"]
        if fins:   # terminal parse takes the LAST Finish (evidence-first answers put it at the end)
            ev=EV_RE.search(out); quotes=[s.strip() for s in re.findall(r'"([^"]{10,})"', ev.group(1))] if ev else []
            supported=any(any(qt[:80] in t for t in retrieved_texts) for qt in quotes) if quotes else False
            final=fins[-1].group(2).strip(); citations={"quotes":quotes,"supported":supported}
            forced_final=True
    sc=env.score(final or "", q)
    rec={"qid":qid,"arm":cfg["arm"],"seed":seed,"calls":calls,"searches":searches,
         "floor_rejects":floor_rejects,"final":final,"citations":citations,"forced_final":forced_final,
         "em":sc["em"],"f1":round(sc["f1"],4),"n_retrieved":len(retrieved_texts),
         "tokens":toks,"secs":round(time.time()-t0,1),
         "cfg_hash":hashlib.sha256(json.dumps(cfg,sort_keys=True).encode()).hexdigest()[:12]}
    log_f.write(json.dumps(rec,ensure_ascii=False)+"\n"); log_f.flush()
    return rec
