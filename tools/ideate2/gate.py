#!/usr/bin/env python3
"""Stage 2.5 — Repackaging gate.

Embeds each idea (Short Hypothesis + Abstract) with local MiniLM, clusters ideas by cosine
similarity, flags ideas whose nearest neighbour is a brief prior-result bullet or a digest card
claim, and emits LLM adjudication jobs for every flagged pair. `apply` turns the adjudications
into keep / differentiate / withdraw decisions and writes gate_report.md.

Run with the env that has sentence-transformers: /home/work/neuro/alfworld-env/bin/python
"""
from __future__ import annotations
import os, sys, json, re, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from backend import Backend
import prompts as P

MODEL = "/home/work/neuro/models/paraphrase-multilingual-MiniLM-L12-v2"


def embed(texts: list[str]) -> np.ndarray:
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer(MODEL, device="cpu")
    return m.encode(texts, normalize_embeddings=True, show_progress_bar=False)


def idea_text(i: dict) -> str:
    return f"{i.get('Title','')}. {i.get('Short Hypothesis','')} {i.get('Abstract','')}"


def brief_bullets(brief_md: str) -> list[str]:
    out = []
    for line in brief_md.splitlines():
        s = line.strip()
        if s.startswith("- **") or re.match(r"^\d+\.\s+\*\*", s):
            out.append(re.sub(r"\*\*", "", s.lstrip("- ")))
    return out


def clusters(sim: np.ndarray, thr: float) -> list[list[int]]:
    n = sim.shape[0]; parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= thr:
                parent[find(i)] = find(j)
    groups: dict[int, list[int]] = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    return [g for g in groups.values() if len(g) > 1]


def run(ideas: list[dict], bullets: list[str], claims: list[dict], thr_idea: float | None, thr_prior: float | None,
        be: Backend | None, out: str, z: float = 1.5) -> dict:
    """thr_idea / thr_prior = None → auto: mean + z·SD of the pairwise similarities (the absolute scale of a
    sentence embedder is corpus-dependent; within one research area everything sits at 0.5–0.75)."""
    os.makedirs(out, exist_ok=True)
    names = [i.get("Name", f"idea{k}") for k, i in enumerate(ideas)]
    E = embed([idea_text(i) for i in ideas])
    sim = E @ E.T
    np.fill_diagonal(sim, 0.0)
    iu = np.triu_indices(len(ideas), 1); vals = sim[iu]
    if thr_idea is None:
        thr_idea = float(vals.mean() + z * vals.std()) if len(vals) > 1 else 0.7
    report = {"thresholds": {"idea": round(thr_idea, 3), "prior": thr_prior, "pair_mean": round(float(vals.mean()), 3) if len(vals) else None,
                             "pair_sd": round(float(vals.std()), 3) if len(vals) else None}, "clusters": [], "prior_flags": [], "pairs": []}
    for g in clusters(sim, thr_idea):
        report["clusters"].append([names[i] for i in g])
        for a in range(len(g)):
            for b in range(a + 1, len(g)):
                i, j = g[a], g[b]
                report["pairs"].append({"a": names[i], "b": names[j], "sim": round(float(sim[i, j]), 3), "kind": "idea-idea"})
    prior_texts = bullets + [f"{c.get('id','')}: {c.get('claim','')}" for c in claims]
    if prior_texts:
        Pm = embed(prior_texts); S = E @ Pm.T
        if thr_prior is None:
            thr_prior = float(S.mean() + z * S.std()); report["thresholds"]["prior"] = round(thr_prior, 3)
        for k, i in enumerate(ideas):
            j = int(S[k].argmax()); s = float(S[k, j])
            if s >= thr_prior:
                src = "brief" if j < len(bullets) else "digest"
                report["prior_flags"].append({"idea": names[k], "sim": round(s, 3), "source": src, "text": prior_texts[j]})
                report["pairs"].append({"a": names[k], "b": f"{src}:{prior_texts[j][:80]}", "sim": round(s, 3),
                                        "kind": f"idea-{src}", "prior_text": prior_texts[j]})
    # top-3 nearest neighbours for every idea (descriptive)
    report["nearest"] = {names[k]: [(names[int(j)], round(float(sim[k, j]), 3)) for j in np.argsort(-sim[k])[:3]] for k in range(len(ideas))}
    json.dump(report, open(os.path.join(out, "gate_report.json"), "w"), indent=1, ensure_ascii=False)
    # adjudication jobs
    if be is not None:
        by = {n: i for n, i in zip(names, ideas)}
        for p in report["pairs"]:
            a_txt = idea_text(by[p["a"]])
            b_txt = idea_text(by[p["b"]]) if p["kind"] == "idea-idea" else p["prior_text"]
            be.call("gate_adjudicate", f"{p['a']}__{p['b'][:30]}", P.GATE_ADJUDICATE_SYSTEM,
                    P.GATE_ADJUDICATE_USER.format(a=a_txt, b=b_txt), model="sonnet")
    # human-readable
    L = [f"# Repackaging gate report", f"thresholds: idea-idea ≥ {thr_idea}, idea-prior ≥ {thr_prior}", ""]
    L.append(f"## Idea clusters ({len(report['clusters'])})")
    for g in report["clusters"]:
        L.append("- " + " | ".join(g))
    L.append(f"\n## Ideas whose nearest prior text is above threshold ({len(report['prior_flags'])})")
    for f in report["prior_flags"]:
        L.append(f"- **{f['idea']}** sim {f['sim']} ← {f['source']}: {f['text'][:120]}")
    L.append("\n## Nearest neighbours (all ideas)")
    for n, nn in report["nearest"].items():
        L.append(f"- {n}: " + ", ".join(f"{m} ({s})" for m, s in nn))
    open(os.path.join(out, "gate_report.md"), "w").write("\n".join(L) + "\n")
    return report


def apply(report_path: str, adjudications: dict[str, dict], out: str) -> dict:
    """adjudications: {job_name: {"label","reason"}} keyed as f"{a}__{b[:30]}"."""
    rep = json.load(open(report_path))
    decisions: dict[str, str] = {}
    for p in rep["pairs"]:
        adj = adjudications.get(f"{p['a']}__{p['b'][:30]}")
        if not adj:
            continue
        p["label"] = adj["label"]; p["reason"] = adj["reason"]
        if adj["label"] == "same_claim_reworded":
            if p["kind"] == "idea-idea":
                decisions.setdefault(p["b"], "differentiate")   # keep a, send b back
            else:
                decisions[p["a"]] = "withdraw_unless_new_claim"
        elif adj["label"] == "same_mechanism_new_measurement":
            decisions.setdefault(p["a"], "keep_note")
    rep["decisions"] = decisions
    json.dump(rep, open(os.path.join(out, "gate_decisions.json"), "w"), indent=1, ensure_ascii=False)
    return rep


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ideas", required=True, help="JSON list of idea dicts (11 fields)")
    ap.add_argument("--brief"); ap.add_argument("--cards")
    ap.add_argument("--out", required=True)
    ap.add_argument("--thr-idea", type=float, default=None, help="absolute cosine; default auto = mean + z·SD")
    ap.add_argument("--thr-prior", type=float, default=None); ap.add_argument("--z", type=float, default=1.5)
    ap.add_argument("--backend", default=None, help="harness|api to emit adjudication jobs; omit for report only")
    a = ap.parse_args()
    ideas = json.load(open(a.ideas))
    bullets = brief_bullets(open(a.brief).read()) if a.brief else []
    claims = [json.loads(l) for l in open(a.cards)] if a.cards else []
    be = Backend(a.backend, os.path.join(a.out, "jobs"), "sonnet") if a.backend else None
    rep = run(ideas, bullets, claims, a.thr_idea, a.thr_prior, be, a.out, a.z)
    print(f"clusters: {len(rep['clusters'])}, prior flags: {len(rep['prior_flags'])}, pairs to adjudicate: {len(rep['pairs'])} -> {a.out}/gate_report.md")
