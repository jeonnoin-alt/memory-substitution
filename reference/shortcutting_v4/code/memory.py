#!/usr/bin/env python3
"""Memory injection builders: dense retrieval over bank, per-arm memory_text construction."""
import json, os, functools, random
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.join(HERE,"..")

@functools.lru_cache(maxsize=None)
def _embedder():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("/home/work/neuro/models/paraphrase-multilingual-MiniLM-L12-v2", device="cpu")

@functools.lru_cache(maxsize=None)
def bank(which="bank_A"):
    items=[json.loads(l) for l in open(os.path.join(W,"data","bank",f"{which}.jsonl"))]
    embs=_embedder().encode([i["item"] for i in items],normalize_embeddings=True,show_progress_bar=False)
    return items, np.array(embs)

def topk(question, which="bank_A", k=7, exclude_ds=None, same_only=None):
    items,embs=bank(which)
    qv=_embedder().encode([question],normalize_embeddings=True)[0]
    scores=embs@qv
    order=np.argsort(-scores)
    picked=[]
    for i in order:
        it=items[int(i)]
        if exclude_ds and it["ds"]==exclude_ds: continue
        if same_only and it["ds"]!=same_only: continue
        picked.append(it)
        if len(picked)==k: break
    return picked

def fmt(items):
    return "\n\n".join(f"--- Item {j+1} ---\n{it['item']}" for j,it in enumerate(items))

def _swap_payload(items, which):
    """Same selected items, payload text taken from the sibling bank by src_qid (V1 fix:
    selection is ALWAYS computed on bank_A embeddings; only the text varies)."""
    alt={it["src_qid"]: it for it in bank(which)[0]}
    return [alt.get(it["src_qid"], it) for it in items]

def memory_text(arm, qrec, seed=0):
    q=qrec["question"]; ds=qrec["ds"]
    if arm=="M1": return fmt(topk(q,"bank_A",7))
    if arm=="M2": return fmt(_swap_payload(topk(q,"bank_A",7),"bank_A_redacted"))
    if arm=="M4":  # decoys: retrieved for a different random question from a different dataset
        rng=random.Random(hash(q)%10**9+seed)
        other=[d for d in ["hotpotqa","musique","2wikimultihopqa"] if d!=ds]
        import env
        qs=[r for r in env.load_questions().values() if r["ds"] in other]
        dq=rng.choice(qs)["question"]
        return fmt(topk(dq,"bank_A",7,same_only=None))
    if arm=="M5": return fmt(topk(q,"bank_A",3))
    if arm=="M6": return fmt(topk(q,"bank_A",7))          # bank-A identical to M1; +budget lives in cfg max_calls
    if arm=="M8": return fmt(topk(q,"bank_A_curated",7))  # curated bank top7 (DESIGN 4 row 15)
    if arm=="M5r": return fmt(_swap_payload(topk(q,"bank_A",3),"bank_A_redacted"))
    if arm=="M2i": return fmt(_swap_payload(topk(q,"bank_A",7),"bank_A_infoswap"))
    if arm=="M3": return fmt(_swap_payload(topk(q,"bank_A",7),"bank_A_answeronly"))
    if arm=="ANCHOR":
        top=topk(q,"bank_A",1)
        ans=top[0].get("answer") or ""
        return ("Your own earlier tentative hypothesis about this question (unverified, may be wrong): "
                f"'{ans}'. Verify before relying on it.")
    if arm=="ANCHOR_NH":
        top=topk(q,"bank_A",1)
        ans=top[0].get("answer") or ""
        return f"Your working hypothesis for this question: '{ans}'."
    raise ValueError(arm)
