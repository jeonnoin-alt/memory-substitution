#!/usr/bin/env python3
"""Stage 3 — Open-book review with escalation and a verified-collision cap.

  review.py emit --idea idea.json --brief brief.md [--card card.md] --n 1 --out reviews/<name>
  review.py aggregate --out reviews/<name> r1.json [r2.json r3.json]
"""
from __future__ import annotations
import os, sys, json, argparse, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import Backend
import prompts as P

VENUE = "ICLR 2027 main track"
ORDER = {"reject": 0, "borderline": 1, "accept-worthy": 2}


def build(idea: dict, brief: str, card: str | None) -> tuple[str, str]:
    fields = {k: idea.get(k, "") for k in P.IDEA_FIELDS}
    system = P.REVIEW_SYSTEM.format(venue=VENUE) + P.REVIEW_SYSTEM_OPENBOOK_SUFFIX
    system += "\n\n=== OUTPUT SCHEMA (return ONLY JSON matching this) ===\n" + json.dumps(P.REVIEW_SCHEMA, indent=1)
    user = P.REVIEW_USER.format(idea_json=json.dumps(fields, indent=1, ensure_ascii=False), brief=brief)
    if card:
        user += "\n\n" + card
    return system, user


def emit(args):
    idea = json.load(open(args.idea)); brief = open(args.brief).read()
    card = open(args.card).read() if args.card else None
    be = Backend(args.backend, os.path.join(args.out, "jobs"), args.model)
    system, user = build(idea, brief, card)
    jobs = [be.emit("review", f"{idea.get('Name','idea')}_r{k}", system, user, tools=["Bash", "WebSearch"], model=args.model)
            for k in range(args.start, args.start + args.n)]
    for j in jobs:
        print(j["id"], "->", j["prompt_file"])
    print("\nagent prompt template:\n" + be.agent_prompt(jobs[0]))


def aggregate(reviews: list[dict]) -> dict:
    W = P.SCORE_WEIGHTS
    means = {k: round(sum(r[k] for r in reviews) / len(reviews), 2) for k in W}
    collisions = [m.group(1) for r in reviews for m in [re.search(r"VERIFIED COLLISION:\s*([^\s,;]+)", r.get("preprint_collision", ""))] if m]
    capped = False
    if collisions and means["novelty"] > 4:
        means["novelty"] = 4.0; capped = True
    score = round(sum(W[k] * means[k] for k in W), 2)
    verdict = min((r["verdict"] for r in reviews), key=lambda v: ORDER.get(v, 1))
    return {"score": score, "verdict": verdict, "means": means, "n_reviews": len(reviews),
            "verified_collisions": collisions, "novelty_capped": capped,
            "escalate": (len(reviews) == 1 and verdict != "reject" and not collisions)}


def do_aggregate(args):
    revs = [json.load(open(p)) for p in args.files]
    agg = aggregate(revs)
    os.makedirs(args.out, exist_ok=True)
    json.dump({"aggregate": agg, "reviews": revs}, open(os.path.join(args.out, "aggregate.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(agg))
    if agg["escalate"]:
        print("→ escalate: launch two more judges")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("emit"); e.add_argument("--idea", required=True); e.add_argument("--brief", required=True)
    e.add_argument("--card"); e.add_argument("--n", type=int, default=1); e.add_argument("--start", type=int, default=1)
    e.add_argument("--out", required=True); e.add_argument("--backend", default="harness"); e.add_argument("--model", default="opus")
    g = sub.add_parser("aggregate"); g.add_argument("--out", required=True); g.add_argument("files", nargs="+")
    a = ap.parse_args()
    emit(a) if a.cmd == "emit" else do_aggregate(a)
