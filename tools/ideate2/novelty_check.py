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


AGENT_WORDS = set("agent agents agentic memory memories memorized retrieved retrieval retrieve retrieving bank banks experience experiences "
                  "episode episodes episodic trajectory trajectories walkthrough walkthroughs alfworld webshop textworld llm llms in-context "
                  "context contextual prompt prompts store stored substrate substrates weights parametric".split())

# (regex over title+hypothesis, home-literature query, adjacent-result query, cheap-baseline query)
HOME_TEMPLATES = [
    (r"distil|distill|self-distill|teacher|student", "knowledge distillation transfers teacher behavior traits student", "subliminal learning trait transfer through unrelated data", "inoculation prompting fine-tuning defense"),
    (r"subliminal|disposition|trait|style", "subliminal learning hidden trait transmission fine-tuning", "narrow fine-tuning generalizes broadly emergent misalignment", "data filtering sanitization insufficient defense distillation"),
    (r"stale|outdated|rule change|shift|nonstationar|non-stationar", "knowledge conflict parametric versus contextual knowledge update", "temporal validity outdated retrieved documents RAG", "recency weighted retrieval time decay"),
    (r"poison|wrong-procedure|conflict|harm", "data poisoning number of poison samples threshold fine-tuning", "misleading demonstrations in-context learning position sensitivity", "static instruction stating the correct procedure"),
    (r"forget|erosion|reversal|relearn|savings|continual", "spurious forgetting relearning savings continual fine-tuning", "unlearning is reversible relearning attacks", "experience replay continual learning baseline"),
    (r"context reliance|abundance|train-time context|training prompt|dose", "retrieval-augmented fine-tuning irrelevant context robustness distractor documents", "long-context training reduces parametric knowledge", "context dropout during fine-tuning"),
    (r"lock-in|self-collected|success-only|own successes|self-training", "self-training confirmation bias filtered self-generated data collapse", "model collapse recursive training on own outputs", "write failures as well as successes to memory"),
    (r"cost|break-even|amortiz|token|pareto", "inference cost accounting retrieval augmented generation versus fine-tuning total cost", "fine-tuning versus RAG cost trade-off knowledge injection", "static few-shot prompt token cost"),
    (r"scaling|pool size|bank size|coverage|count", "data diversity versus quantity scaling supervised fine-tuning", "many-shot in-context learning number of examples saturation", "static few-shot exemplars per task type"),
    (r"privilege|privileged|instance|type-level|procedure", "privileged information distillation student cannot close information gap", "in-context demonstrations override explicit instructions", "same-task oracle demonstration upper bound"),
    (r"additive|substitut|hybrid|routing|marginal", "fine-tuning plus retrieval augmentation complementary or redundant knowledge injection", "retrieval still needed after fine-tuning on the same corpus", "retrieval-augmented fine-tuning baseline"),
]


def _shift(s: str, n: int = 12) -> str:
    """content words of s with the agent-memory vocabulary removed (the 'home literature' phrasing)."""
    w = [t for t in re.findall(r"[A-Za-z][A-Za-z0-9\-]+", s) if t.lower() not in STOP and t.lower() not in AGENT_WORDS and len(t) > 2]
    return " ".join(w[:n])


def rule_keys(idea: dict) -> dict:
    """No-LLM fallback with query classes: agent (own vocabulary), mechanism_home (vocabulary-shifted + templates),
    adjacent (result direction in a neighbouring field), baseline (cheapest intervention), methods, environment."""
    hyp = idea.get("Short Hypothesis", ""); title = idea.get("Title", "")
    rw = idea.get("Related Work", "")
    sents = [s for s in re.split(r"(?<=[.;])\s+", hyp) if len(s) > 30]
    mech = [_content_words(s) for s in sents[:2]]
    methods = re.findall(r"\b([A-Z][A-Za-z0-9]+(?:[A-Z][a-z]+)*|[A-Z]{3,}[A-Za-z0-9]*)\b(?=\s*\(arXiv)", rw)[:4]
    env = re.findall(r"\b(ALFWorld|WebShop|HotpotQA|MuSiQue|GSM8K|MBPP|WebArena|SWE-?Bench|Qwen[0-9.\-A-Za-z]*|Llama[0-9.\-A-Za-z]*)\b", hyp + idea.get("Experiments", ""))
    kw = _content_words(title.split("?")[-1] or title, 8)
    text = (title + " " + hyp).lower()
    home, adj, base = [], [], []
    scored = sorted(((len(re.findall(pat, text)), n_, pat, h, a_, b) for n_, (pat, h, a_, b) in enumerate(HOME_TEMPLATES)), key=lambda t: (-t[0], t[1]))
    for hits, _, pat, h, a_, b in scored:               # templates ranked by how often their pattern occurs in title+hypothesis
        if hits:
            home.append(h); adj.append(a_); base.append(b)
    home = [_shift(sents[0] if sents else hyp)] + home[:2]
    return {"agent": [kw] + mech[:1], "mechanism_home": home, "adjacent": adj[:2], "baseline": base[:2],
            "estimand": [_content_words(hyp, 10)], "environment": sorted(set(env))[:3], "methods": methods}


def queries_from_keys(k: dict) -> list[tuple[str, str]]:
    """Ordered (class, query) pairs; S2 goes to the first --s2-queries of them, HF to all. Home-literature first: that is
    where the pre-empting papers were found in every review round so far."""
    q: list[tuple[str, str]] = []
    def add(cls, items, n):
        for x in (items or [])[:n]:
            x = re.sub(r"\s+", " ", str(x)).strip()[:200]
            if x and all(x != y for _, y in q): q.append((cls, x))
    add("mechanism_home", k.get("mechanism_home"), 2)
    add("agent", k.get("agent") or k.get("mechanism"), 2)
    add("adjacent", k.get("adjacent"), 1)
    add("baseline", k.get("baseline"), 1)
    if k.get("methods"):
        add("methods", [" ".join(k["methods"][:3]) + " " + ((k.get("agent") or k.get("mechanism") or [""])[0])[:60]], 1)
    env = " ".join((k.get("environment") or [])[:2])
    if env and (k.get("agent") or k.get("mechanism")):
        add("agent", [f"{(k.get('agent') or k.get('mechanism'))[0]} {env}"], 1)
    return q


def build_card(idea: dict, papers: list[Paper], embed_fn, qclass: dict[str, str], top: int = 10) -> tuple[str, list[dict]]:
    hyp = f"{idea.get('Title','')}. {idea.get('Short Hypothesis','')}"
    texts = [hyp] + [f"{p.title}. {p.abstract or p.tldr}" for p in papers]
    E = embed_fn(texts)
    sims = E[1:] @ E[0]
    order = sorted(range(len(papers)), key=lambda i: -float(sims[i]))[:top]
    rows = []
    L = [P.NOVELTY_CARD_HEADER, f"Proposal: {idea.get('Name','')} — {idea.get('Title','')}", ""]
    for i in order:
        p = papers[i]
        via = sorted({qclass.get(q, "?") for q in p.queries}) or ["?"]
        rows.append({"id": p.id, "date": p.date or p.year, "venue": p.venue, "sim": round(float(sims[i]), 3),
                     "channels": p.sources, "via": via, "title": p.title})
        L.append(f"- {p.id} · {p.date or p.year} · {p.venue or 'preprint'} · sim {float(sims[i]):.2f} · {'/'.join(p.sources)} · found via {'/'.join(via)}\n"
                 f"  {p.title}\n  {(p.abstract or p.tldr)[:500]}")
    # papers that only the home/adjacent/baseline queries returned, even if low similarity: the ones the agent phrasing misses
    extra = [i for i in range(len(papers)) if i not in order and {qclass.get(q) for q in papers[i].queries} & {"mechanism_home", "adjacent", "baseline"}]
    extra = sorted(extra, key=lambda i: -float(sims[i]))[:5]
    if extra:
        L.append("\nReturned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):")
        for i in extra:
            p = papers[i]; via = sorted({qclass.get(q, "?") for q in p.queries})
            L.append(f"- {p.id} · {p.date or p.year} · sim {float(sims[i]):.2f} · via {'/'.join(via)} — {p.title}")
    L.append("\nQueries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.")
    return "\n".join(L) + "\n", rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ideas", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--keys", help="JSON {name: keys} from novelty_keys_collect.py; omit for rule-based keys")
    ap.add_argument("--backend", default=None, help="harness|api: emit key-extraction jobs (batched) and stop")
    ap.add_argument("--model", default="fable", help="key extraction is a scan task: Fable (PI policy)")
    ap.add_argument("--batch", type=int, default=5, help="ideas per key-extraction job")
    ap.add_argument("--per-query", type=int, default=8); ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--s2-queries", type=int, default=2, help="how many AGENT-class queries also go to S2 with a 12-month window (home/adjacent/baseline queries always go to S2, unrestricted)")
    a = ap.parse_args()
    ideas = json.load(open(a.ideas))
    os.makedirs(a.out, exist_ok=True)
    if a.backend:
        be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model)
        for b in range(0, len(ideas), a.batch):
            chunk = [{k: (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))[:3000] for k, v in i.items()
                      if k in ("Name", "Title", "Short Hypothesis", "Related Work", "Baselines and Ablations", "Experiments")} for i in ideas[b:b + a.batch]]
            user = ("Extract keys for each proposal below. Return a JSON ARRAY of objects {\"name\": <Name copied exactly>, \"keys\": {...}} "
                    "in the same order.\n\n" + json.dumps(chunk, ensure_ascii=False, indent=1))
            be.call("novelty_keys", f"batch{b // a.batch:02d}", P.NOVELTY_KEYS_SYSTEM, user)
        print(f"{(len(ideas) + a.batch - 1) // a.batch} key-extraction jobs -> {be.jobs_dir}"); return
    keys_all = json.load(open(a.keys)) if a.keys else {}
    from gate import embed
    s2, hf = S2Client(), HFClient()
    year_from = datetime.date.today().year - 1
    for i in ideas:
        name = i.get("Name", "idea")
        k = keys_all.get(name) or rule_keys(i)
        if name in keys_all:                                   # LLM keys may lack a class; fill from the rule-based ones
            rk = rule_keys(i)
            for c in ("agent", "mechanism_home", "adjacent", "baseline", "methods", "environment"):
                if not k.get(c): k[c] = rk.get(c, [])
        qs = queries_from_keys(k); qclass = {q: c for c, q in qs}
        papers: list[Paper] = []
        n_agent_s2 = 0
        for n_, (cls, q) in enumerate(qs):
            papers += hf.search(q, a.per_query)          # HF Papers: recent arXiv, good for the agent-memory phrasing
            if cls in ("mechanism_home", "adjacent", "baseline"):
                # the home literature is older by nature (RAG robustness 2023-24, knowledge conflict 2023, poisoning 2025):
                # HF misses it and a 12-month S2 window excluded it in the 2026-09-07 run, so S2 runs unrestricted here
                papers += s2.search(q, a.per_query + 2)
            elif n_agent_s2 < a.s2_queries:              # S2 is rate-limited (~1 req/s across agents): agent phrasing gets --s2-queries recent lookups
                papers += s2.search(q, a.per_query, year_from=year_from); n_agent_s2 += 1
        papers = dedupe(papers)
        card, rows = build_card(i, papers, embed, qclass, a.top) if papers else ("(no candidates returned)\n", [])
        open(os.path.join(a.out, f"{name}.card.md"), "w").write(card)
        by_class = {c: sum(1 for p in papers if any(qclass.get(q) == c for q in p.queries)) for c in ("mechanism_home", "agent", "adjacent", "baseline", "methods")}
        json.dump({"name": name, "keys": k, "queries": [{"class": c, "query": q} for c, q in qs], "candidates": rows, "candidates_by_class": by_class,
                   "web_jobs": [{"query": q + f" {year_from} arXiv"} for c, q in qs[:2]]},
                  open(os.path.join(a.out, f"{name}.card.json"), "w"), indent=1, ensure_ascii=False)
        save_jsonl(papers, os.path.join(a.out, f"{name}.candidates.jsonl"))
        print(f"{name}: {len(qs)} queries, {len(papers)} candidates ({by_class}), top sim {rows[0]['sim'] if rows else '-'}")


if __name__ == "__main__":
    main()
