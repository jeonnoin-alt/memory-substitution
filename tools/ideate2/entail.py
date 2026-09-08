#!/usr/bin/env python3
"""Stage 2.8 — Entailment check (pre-review).

For every prediction of every idea an LLM (Opus; gate-class task) states the falsifying outcome and decides whether the
stated arms can produce it, and whether it is distinguishable at the stated power. Ideas whose headline prediction is
entailed / near-entailed / unresolvable are sent back to the generator (revise jobs) before any judge sees them, and the
per-idea report is attached to the review prompt as evidence.

  entail.py emit    --ideas ideas.json --out <dir> [--batch 3] [--model opus] [--names a,b]
  entail.py collect --out <dir> --mapping '{"batchNN": task_id}'      -> entail_report.json, ENTAIL_REPORT.md, <name>.entail.md
  entail.py revise  --ideas ideas.json --out <dir> --brief brief.md [--model fable]   -> jobs/entail_revise__<name>
"""
from __future__ import annotations
import os, sys, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import Backend, parse_json, TASKS_DIR
from ingest_sections import assistant_texts
import prompts as P

HEADER = "=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===\nFor each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.\n"


def _s(v, n=6000):
    v = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    return v[:n]


def idea_block(i: dict) -> str:
    return P.ENTAIL_USER.format(name=i.get("Name", ""), title=_s(i.get("Title", ""), 400), hypothesis=_s(i.get("Short Hypothesis", ""), 2500),
                                experiments=_s(i.get("Experiments", "")), baselines=_s(i.get("Baselines and Ablations", ""), 3000),
                                predictions=_s(i.get("Falsifiable Predictions", "")), noise=_s(i.get("Measurement and Noise Control", ""), 3000))


def emit(a):
    ideas = json.load(open(a.ideas)); names = set(a.names.split(",")) if a.names else None
    ideas = [i for i in ideas if not names or i.get("Name") in names]
    be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model); n = 0
    for b in range(0, len(ideas), a.batch):
        chunk = ideas[b:b + a.batch]
        user = ("Check each proposal below independently. Return a JSON ARRAY of per-proposal objects in the same order.\n\n"
                + "\n\n".join(idea_block(i) for i in chunk))
        be.call("entail", f"batch{b // a.batch:02d}", P.ENTAIL_SYSTEM, user); n += 1
    print(f"{n} entailment jobs ({len(ideas)} ideas, batch {a.batch}) -> {be.jobs_dir}")


def _md(d: dict) -> str:
    L = [HEADER, f"Proposal: {d.get('name','')} — headline {d.get('headline','?')} is **{d.get('headline_status','?')}**; "
         f"open {d.get('n_open',0)} / entailed {d.get('n_entailed',0)} / near-entailed {d.get('n_near',0)} / unresolvable {d.get('n_unresolvable',0)}; verdict {d.get('verdict','?')}", ""]
    for p in d.get("predictions", []):
        L.append(f"- {p.get('id','?')} [{p.get('label','?')}] falsifier: {p.get('falsifier','')}")
        L.append(f"  reason: {p.get('reason','')}" + (f"\n  fix: {p['fix']}" if p.get("fix") else ""))
    if d.get("shared_terms"):
        L.append("- shared terms: " + "; ".join(d["shared_terms"]))
    return "\n".join(L) + "\n"


def collect(a):
    mapping = json.load(open(a.mapping)); reports: dict[str, dict] = {}; missing = []
    for b, tid in sorted(mapping.items()):
        path = os.path.join(TASKS_DIR, tid + ".output")
        if not os.path.exists(path): missing.append(b); continue
        arr = None
        for t in reversed(assistant_texts(path)):
            try: x = parse_json(t)
            except Exception: continue
            if isinstance(x, list) and x and isinstance(x[0], dict) and "predictions" in x[0]: arr = x; break
            if isinstance(x, dict) and "predictions" in x: arr = [x]; break
        if arr is None: missing.append(b); continue
        for d in arr:
            labels = [p.get("label", "") for p in d.get("predictions", [])]
            d["n_open"] = labels.count("open"); d["n_entailed"] = labels.count("entailed")
            d["n_near"] = labels.count("near_entailed"); d["n_unresolvable"] = labels.count("unresolvable")
            if d.get("headline_status") not in ("open", "entailed", "near_entailed", "unresolvable"):
                hid = d.get("headline"); d["headline_status"] = next((p.get("label") for p in d.get("predictions", []) if p.get("id") == hid), "open")
            d["verdict"] = "revise" if (d["headline_status"] != "open" or d["n_open"] * 2 < len(labels)) else "pass"
            reports[d["name"]] = d
            open(os.path.join(a.out, f"{d['name']}.entail.md"), "w").write(_md(d))
    json.dump(reports, open(os.path.join(a.out, "entail_report.json"), "w"), indent=1, ensure_ascii=False)
    L = ["# Entailment check report", "", "| idea | headline | status | open | entailed | near | unresolvable | verdict |", "|---|---|---|---|---|---|---|---|"]
    for n, d in sorted(reports.items(), key=lambda kv: (kv[1]["verdict"] != "revise", kv[0])):
        L.append(f"| {n} | {d.get('headline','?')} | {d['headline_status']} | {d['n_open']} | {d['n_entailed']} | {d['n_near']} | {d['n_unresolvable']} | {d['verdict']} |")
    L.append("\n## Flagged predictions\n")
    for n, d in reports.items():
        for p in d.get("predictions", []):
            if p.get("label") != "open":
                L.append(f"- **{n} {p.get('id')}** [{p.get('label')}]: {p.get('reason','')[:300]}")
    open(os.path.join(a.out, "ENTAIL_REPORT.md"), "w").write("\n".join(L) + "\n")
    nrev = sum(1 for d in reports.values() if d["verdict"] == "revise")
    print(f"entailment: {len(reports)} ideas, {nrev} to revise; missing batches {missing} -> {a.out}/ENTAIL_REPORT.md")


def revise(a):
    ideas = {i["Name"]: i for i in json.load(open(a.ideas))}
    rep = json.load(open(os.path.join(a.out, "entail_report.json")))
    brief = open(a.brief).read() if a.brief else ""
    rules = brief[brief.index("## Rules"):brief.index("## Open questions")] if "## Rules" in brief and "## Open questions" in brief else ""
    be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model); n = 0
    for name, d in rep.items():
        if d.get("verdict") != "revise" or name not in ideas: continue
        idea = {k: v for k, v in ideas[name].items() if not k.startswith("_")}
        user = ("=== PROPOSAL ===\n" + json.dumps(idea, ensure_ascii=False, indent=1) +
                "\n\n=== ENTAILMENT CHECK (pre-review) ===\n" + json.dumps(d, ensure_ascii=False, indent=1) +
                ("\n\n=== BINDING RULES FROM THE BRIEF ===\n" + rules if rules else "") +
                "\n\nEvery prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand "
                "or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. "
                "Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', "
                "'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).")
        be.call("entail_revise", name, P.REVISE_SYSTEM, user, tools=["Bash"]); n += 1
    print(f"{n} revision jobs -> {be.jobs_dir}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("emit"); e.add_argument("--ideas", required=True); e.add_argument("--out", required=True)
    e.add_argument("--batch", type=int, default=3); e.add_argument("--model", default="opus"); e.add_argument("--backend", default="harness"); e.add_argument("--names")
    c = sub.add_parser("collect"); c.add_argument("--out", required=True); c.add_argument("--mapping", required=True)
    r = sub.add_parser("revise"); r.add_argument("--ideas", required=True); r.add_argument("--out", required=True); r.add_argument("--brief")
    r.add_argument("--model", default="fable"); r.add_argument("--backend", default="harness")
    a = ap.parse_args(); {"emit": emit, "collect": collect, "revise": revise}[a.cmd](a)
