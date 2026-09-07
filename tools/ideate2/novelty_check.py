#!/usr/bin/env python3
"""Stage 2.7 — Novelty card: for each idea, extract search keys (LLM job, or rule-based fallback),
query S2 / HF (and emit WebSearch jobs), rank candidates by abstract–hypothesis similarity, and
write a novelty card (evidence for the judges; no verdict).

Run with /home/work/neuro/alfworld-env/bin/python (sentence-transformers) and S2_PIN_IP set.
"""
from __future__ import annotations
import os, sys, json, re, argparse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lit import S2Client, HFClient, dedupe, Paper, save_jsonl
from backend import Backend
import prompts as P


STOP = set("the a an of in on at to for and or is are be by with from that this these those we our it its as into "
           "than then at once every each both either neither not no yes if when while where which who whom whose "
           "what how why all any some most more less least very much many few own same other such only also just".split())


def _content_words(s: str, n: int = 12) -> str:
    w = [t for t in re.findall(r"[A-Za-z][A-Za-z0-9\-]+", s) if t.lower() not in STOP and len(t) > 2]
    return " ".join(w[:n])


def rule_keys(idea: dict) -> dict:
    """No-LLM fallback: content words of the hypothesis, named methods from Related Work, benchmarks."""
    hyp = idea.get("Short Hypothesis", "")
    rw = idea.get("Related Work", "")
    sents = [s for s in re.split(r"(?<=[.;])\s+", hyp) if len(s) > 30]
    mech = [_content_words(s) for s in sents[:2]]
    methods = re.findall(r"\b([A-Z][A-Za-z0-9]+(?:[A-Z][a-z]+)*|[A-Z]{3,}[A-Za-z0-9]*)\b(?=\s*\(arXiv)", rw)[:4]
    ctrl = [c for c in re.findall(r"\b([A-Z][A-Za-z0-9_'\-]{2,}(?: [a-z]+){0,2})\b", idea.get("Baselines and Ablations", "")) if c not in STOP][:3]
    env = re.findall(r"\b(ALFWorld|WebShop|HotpotQA|MuSiQue|GSM8K|MBPP|WebArena|SWE-?Bench|Qwen[0-9.\-A-Za-z]*|Llama[0-9.\-A-Za-z]*)\b", hyp + idea.get("Experiments", ""))
    kw = _content_words(idea.get("Title", "").split("?")[-1] or idea.get("Title", ""), 8)
    return {"mechanism": [kw] + mech, "estimand": [_content_words(hyp, 10)],
            "controls": ctrl, "environment": sorted(set(env))[:3], "methods": methods}


def queries_from_keys(k: dict) -> list[str]:
    q = []
    for m in k.get("mechanism", [])[:2]:
        q.append(m)
    for e in k.get("estimand", [])[:1]:
        q.append(e)
    env = " ".join(k.get("environment", [])[:2])
    if env and k.get("mechanism"):
        q.append(f"{k['mechanism'][0]} {env}")
    if k.get("methods"):
        q.append(" ".join(k["methods"][:3]) + " " + (k.get("mechanism") or [""])[0][:60])
    return [re.sub(r"\s+", " ", x).strip()[:200] for x in q if x and x.strip()]


def _unused_old_queries(k: dict) -> list[str]:  # kept for reference; superseded above


def queries_from_keys(k: dict) -> list[str]:
    q = []
    for m in k.get("mechanism", [])[:2]:
        q.append(m)
    for e in k.get("estimand", [])[:1]:
        q.append(e)
    env = " ".join(k.get("environment", [])[:2])
    if env and k.get("mechanism"):
        q.append(f"{k['mechanism'][0]} {env}")
    return [re.sub(r"\s+", " ", x)[:200] for x in q if x]


def build_card(idea: dict, papers: list[Paper], embed_fn, top: int = 10) -> tuple[str, list[dict]]:
    hyp = f"{idea.get('Title','')}. {idea.get('Short Hypothesis','')}"
    texts = [hyp] + [f"{p.title}. {p.abstract or p.tldr}" for p in papers]
    E = embed_fn(texts)
    sims = E[1:] @ E[0]
    order = sorted(range(len(papers)), key=lambda i: -float(sims[i]))[:top]
    rows = []
    L = [P.NOVELTY_CARD_HEADER, f"Proposal: {idea.get('Name','')} — {idea.get('Title','')}", ""]
    for i in order:
        p = papers[i]
        rows.append({"id": p.id, "date": p.date or p.year, "venue": p.venue, "sim": round(float(sims[i]), 3),
                     "channels": p.sources, "title": p.title})
        L.append(f"- {p.id} · {p.date or p.year} · {p.venue or 'preprint'} · sim {float(sims[i]):.2f} · {'/'.join(p.sources)}\n"
                 f"  {p.title}\n  {(p.abstract or p.tldr)[:500]}")
    L.append("\nQueries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.")
    return "\n".join(L) + "\n", rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ideas", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--keys", help="JSON {name: keys} from the LLM key-extraction jobs; omit for rule-based keys")
    ap.add_argument("--backend", default=None, help="harness|api: emit key-extraction jobs and stop")
    ap.add_argument("--per-query", type=int, default=8); ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args()
    ideas = json.load(open(a.ideas))
    os.makedirs(a.out, exist_ok=True)
    if a.backend:
        be = Backend(a.backend, os.path.join(a.out, "jobs"), "sonnet")
        for i in ideas:
            be.call("novelty_keys", i.get("Name", "idea"), P.NOVELTY_KEYS_SYSTEM, json.dumps(i, ensure_ascii=False), model="sonnet")
        print(f"{len(ideas)} key-extraction jobs -> {be.jobs_dir}"); return
    keys_all = json.load(open(a.keys)) if a.keys else {}
    from gate import embed
    s2, hf = S2Client(), HFClient()
    year_from = datetime.date.today().year - 1
    for i in ideas:
        name = i.get("Name", "idea")
        k = keys_all.get(name) or rule_keys(i)
        qs = queries_from_keys(k)
        papers: list[Paper] = []
        for q in qs:
            papers += s2.search(q, a.per_query, year_from=year_from) + s2.search(q, 4) + hf.search(q, a.per_query)
        papers = dedupe(papers)
        card, rows = build_card(i, papers, embed, a.top) if papers else ("(no candidates returned)\n", [])
        open(os.path.join(a.out, f"{name}.card.md"), "w").write(card)
        json.dump({"name": name, "keys": k, "queries": qs, "candidates": rows,
                   "web_jobs": [{"query": q + f" {year_from} arXiv"} for q in qs[:2]]},
                  open(os.path.join(a.out, f"{name}.card.json"), "w"), indent=1, ensure_ascii=False)
        save_jsonl(papers, os.path.join(a.out, f"{name}.candidates.jsonl"))
        print(f"{name}: {len(qs)} queries, {len(papers)} candidates, top sim {rows[0]['sim'] if rows else '-'}")


if __name__ == "__main__":
    main()
