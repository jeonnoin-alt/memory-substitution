#!/usr/bin/env python3
"""Stage 0 — Pre-scan: collect recent + foundational papers per axis, rank, read sections, and
emit the digest jobs (cards + per-axis gap synthesis). Output: prescan/<slug>/{papers.jsonl,
cards.jsonl, gaps.json, digest.md}; digest.md is prepended to the brief.

Usage (harness mode, no Anthropic key):
  prescan.py plan    --slug S --brief brief.md --out prescan/S           # emits the axes job
  prescan.py collect --slug S --axes axes.json --out prescan/S [--top 40] # network only
  prescan.py cards   --slug S --out prescan/S                             # emits one job per paper
  prescan.py synth   --slug S --out prescan/S                             # emits one job per axis
  prescan.py digest  --slug S --out prescan/S --brief brief.md            # writes digest.md + brief_with_digest.md
Results of harness jobs are ingested with `run.py collect`.
"""
from __future__ import annotations
import os, sys, json, argparse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lit import S2Client, HFClient, OpenAlexClient, ArxivClient, SectionReader, Paper, dedupe, rank, save_jsonl, load_jsonl
from backend import Backend
import prompts as P


def plan(args, be: Backend):
    brief = open(args.brief).read()
    return be.call("prescan_axes", args.slug, P.PRESCAN_AXES_SYSTEM, brief)


def collect(args):
    axes = json.load(open(args.axes))["axes"]
    year_from = datetime.date.today().year - 1
    s2, hf, oa, ax = S2Client(), HFClient(), OpenAlexClient(), ArxivClient()
    print(f"channels: s2={s2.ok} hf={hf.ok} openalex={oa.ok} arxiv={ax.ok}")
    papers: list[Paper] = []
    web_jobs = []
    for a in axes:
        for i, q in enumerate(a["queries"]):
            for p in s2.search(q, args.per_query, year_from=year_from) + hf.search(q, args.per_query) \
                     + oa.search(q, args.per_query, year_from=year_from) + ax.search(q, args.per_query):
                p.axes = [a["name"]]; papers.append(p)
            if i == 0:  # mechanism phrasing → also a server-side web search job for the harness
                web_jobs.append({"axis": a["name"], "query": f"{q} {year_from} {year_from+1} arXiv"})
        for p in s2.search(a["foundational"], args.per_query) + hf.search(a["foundational"], args.per_query):
            p.axes = [a["name"]]; papers.append(p)
    papers = dedupe(papers)
    if args.rerank:  # relevance term: cosine(abstract, axis definition + query) with local MiniLM
        from gate import embed
        axis_txt = {a["name"]: f"{a['name']}. {a['definition']}. " + " ".join(a["queries"]) for a in axes}
        A = embed(list(axis_txt.values())); names = list(axis_txt)
        Pm = embed([f"{p.title}. {p.abstract or p.tldr}" for p in papers])
        S = Pm @ A.T
        for p, row in zip(papers, S):
            p.relevance = float(max(row[names.index(x)] for x in p.axes)) if p.axes else float(row.max())
        import math
        from lit import recency_score
        papers.sort(key=lambda p: 0.4 * recency_score(p.date or (f"{p.year}-06-30" if p.year else ""))
                    + 0.2 * min(math.log1p(p.citations or 0) / math.log1p(500), 1.0) + 0.4 * p.relevance, reverse=True)
    else:
        papers = rank(papers)
    multi = [p for p in papers if len(p.axes) >= 2]
    keep = papers[:args.top] + [p for p in multi if p not in papers[:args.top]]
    os.makedirs(args.out, exist_ok=True)
    save_jsonl(keep, os.path.join(args.out, "papers.jsonl"))
    json.dump(web_jobs, open(os.path.join(args.out, "web_queries.json"), "w"), indent=1)
    print(f"collected {len(papers)} unique, kept {len(keep)} -> {args.out}/papers.jsonl")
    # sections for the top-N: fills in place where reachable, else emits WebSearch jobs
    reader = SectionReader(jobs_dir=os.path.join(args.out, "jobs_sections"))
    n = 0
    for p in keep[:args.sections]:
        if p.arxiv:
            sec = reader.read(p.arxiv); p.sections = {k: v for k, v in sec.items() if not k.startswith("_")}
            n += 1 if p.sections else 0
    save_jsonl(keep, os.path.join(args.out, "papers.jsonl"))
    print(f"sections read directly: {n}/{min(len(keep), args.sections)}; the rest as WebSearch jobs in {args.out}/jobs_sections/")


def cards(args, be: Backend):
    papers = load_jsonl(os.path.join(args.out, "papers.jsonl"))
    axes = json.load(open(args.axes))["axes"] if args.axes else []
    axes_txt = "; ".join(f"{a['name']}: {a['definition']}" for a in axes)
    jobs = []
    for b in range(0, len(papers), args.batch):
        chunk = papers[b:b + args.batch]
        blocks = []
        for p in chunk:
            blocks.append(f"### ID: {p.id}\nTitle: {p.title}\nDate: {p.date or p.year}\nVenue: {p.venue}\n"
                          f"Abstract: {p.abstract}\nTL;DR: {p.tldr}\n"
                          f"Limitations text: {p.sections.get('limitations','not available')}\n"
                          f"Conclusion text: {p.sections.get('conclusion','not available')}")
        user = (f"Axes: {axes_txt}\n\nWrite one card per paper below. Return a JSON ARRAY of card objects, in the same order.\n\n"
                + "\n\n".join(blocks))
        jobs.append(be.call("prescan_card", f"batch{b // args.batch:02d}", P.PRESCAN_CARD_SYSTEM, user, model="sonnet"))
    print(f"{len(jobs)} card jobs ({args.batch} papers each) -> {be.jobs_dir}")


def synth(args, be: Backend):
    cards_ = [json.loads(l) for l in open(os.path.join(args.out, "cards.jsonl"))]
    by_axis: dict[str, list] = {}
    for c in cards_:
        for a in c.get("axes") or ["unassigned"]:
            by_axis.setdefault(a, []).append(c)
    for a, cs in by_axis.items():
        be.call("prescan_synth", a, P.PRESCAN_SYNTH_SYSTEM, json.dumps(cs, ensure_ascii=False, indent=1))
    print(f"{len(by_axis)} synth jobs -> {be.jobs_dir}")


def digest(args):
    cards_ = [json.loads(l) for l in open(os.path.join(args.out, "cards.jsonl"))]
    gaps = json.load(open(os.path.join(args.out, "gaps.json")))  # list of {"axis","gaps":[...]}
    today = datetime.date.today().isoformat()
    L = [f"## Recent literature digest (auto, {today}; {len(cards_)} cards)\n"]
    gid = 0
    for g in gaps:
        L.append(f"### Axis: {g['axis']}")
        for x in g["gaps"]:
            gid += 1
            L.append(f"- **G{gid}** {x['gap']} (cards: {', '.join(x['card_ids'])}) — evidence needed: {x['evidence_needed']}")
        L.append("")
    L.append("### Cards")
    for c in cards_:
        L.append(f"- **{c['id']}** ({c.get('date','')}) claim: {c['claim']} | method: {c['method']} | evidence: {c['evidence']} "
                 f"| limitations: {c['stated_limitations']} | not tested: {c['not_tested']}")
    md = "\n".join(L) + "\n"
    open(os.path.join(args.out, "digest.md"), "w").write(md)
    if args.brief:
        b = open(args.brief).read()
        open(os.path.join(args.out, "brief_with_digest.md"), "w").write(md + "\n---\n\n" + b)
    print(f"digest.md written ({len(cards_)} cards, {gid} gaps)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["plan", "collect", "cards", "synth", "digest"])
    ap.add_argument("--slug", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--brief"); ap.add_argument("--axes")
    ap.add_argument("--backend", default="harness"); ap.add_argument("--model", default="opus")
    ap.add_argument("--per-query", type=int, default=8); ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--sections", type=int, default=15)
    ap.add_argument("--rerank", action="store_true", help="add an embedding relevance term (needs sentence-transformers)")
    ap.add_argument("--batch", type=int, default=10, help="papers per card job (harness economy)")
    a = ap.parse_args()
    be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model) if a.stage in ("plan", "cards", "synth") else None
    {"plan": lambda: plan(a, be), "collect": lambda: collect(a), "cards": lambda: cards(a, be),
     "synth": lambda: synth(a, be), "digest": lambda: digest(a)}[a.stage]()
