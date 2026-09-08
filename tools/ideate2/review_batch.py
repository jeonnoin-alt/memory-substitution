#!/usr/bin/env python3
"""Stage 3 driver over a pool: emit one open-book judge job per idea, collect the harness results, aggregate, rank.

  review_batch.py emit    --ideas G/ideas.json --brief brief.md --novelty G/novelty --out G/review [--round 1] [--names a,b]
  review_batch.py collect --out G/review --mapping map.json          # map = {"<name>_r<k>": "<task id>", ...}
  review_batch.py rank    --out G/review                              # RANKING.md / RANKING.json
"""
from __future__ import annotations
import os, sys, json, argparse, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import Backend, parse_json, TASKS_DIR
from ingest_sections import assistant_texts
import review as R
import prompts as P


def emit(a):
    ideas = json.load(open(a.ideas)); brief = open(a.brief).read()
    names = set(a.names.split(",")) if a.names else None
    be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model)
    n = 0
    for idea in ideas:
        name = idea.get("Name", "idea")
        if names and name not in names: continue
        card_path = os.path.join(a.novelty, f"{name}.card.md") if a.novelty else None
        card = open(card_path).read() if card_path and os.path.exists(card_path) else None
        ent_path = os.path.join(a.entail, f"{name}.entail.md") if getattr(a, "entail", None) else None
        if ent_path and os.path.exists(ent_path):                   # Stage 2.8 report travels with the novelty card
            card = (card or "") + "\n\n" + open(ent_path).read()
        system, user = R.build(idea, brief, card)
        for k in range(a.round, a.round + a.n):
            be.emit("review", f"{name}_r{k}", system, user, tools=["Bash", "WebSearch"], model=a.model); n += 1
    print(f"{n} judge jobs -> {be.jobs_dir}")


def collect(a):
    mapping = json.load(open(a.mapping)); got, missing = [], []
    for job, tid in mapping.items():
        name, rk = job.rsplit("_r", 1)
        path = os.path.join(TASKS_DIR, tid + ".output"); d = None
        if os.path.exists(path):
            for t in reversed(assistant_texts(path)):
                try: x = parse_json(t)
                except Exception: continue
                if isinstance(x, dict) and "verdict" in x and "novelty" in x: d = x; break
        if d is None: missing.append(job); continue
        os.makedirs(os.path.join(a.out, name), exist_ok=True)
        json.dump(d, open(os.path.join(a.out, name, f"r{rk}.json"), "w"), indent=1, ensure_ascii=False); got.append(job)
    print(f"collected {len(got)}; missing {missing}")


def rank(a):
    rows = []
    for d in sorted(glob.glob(os.path.join(a.out, "*", "r1.json"))):
        name = os.path.basename(os.path.dirname(d))
        revs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(a.out, name, "r*.json")))]
        try: agg = R.aggregate(revs)
        except Exception as e: print("aggregate failed", name, e); continue
        json.dump({"aggregate": agg, "reviews": revs}, open(os.path.join(a.out, name, "aggregate.json"), "w"), indent=1, ensure_ascii=False)
        rows.append({"name": name, **agg, "closest": revs[0].get("closest_prior_work", "")[:160]})
    rows.sort(key=lambda r: -r["score"])
    json.dump(rows, open(os.path.join(a.out, "RANKING.json"), "w"), indent=1, ensure_ascii=False)
    W = P.SCORE_WEIGHTS
    L = ["# Ranking (open-book Opus judges; weights " + ", ".join(f"{k} {v}" for k, v in W.items()) + "; worst verdict wins)", "",
         "| # | idea | n | score | verdict | nov | sig | snd | fea | cla | collision | escalate |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        m = r["means"]
        L.append(f"| {i} | {r['name']} | {r['n_reviews']} | {r['score']} | {r['verdict']} | {m['novelty']} | {m['significance']} | {m['soundness']} | {m['feasibility']} | {m['clarity']} | "
                 f"{'; '.join(r['verified_collisions']) or '-'} | {'yes' if r['escalate'] else '-'} |")
    open(os.path.join(a.out, "RANKING.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("emit"); e.add_argument("--ideas", required=True); e.add_argument("--brief", required=True); e.add_argument("--novelty")
    e.add_argument("--out", required=True); e.add_argument("--round", type=int, default=1); e.add_argument("--n", type=int, default=1)
    e.add_argument("--names"); e.add_argument("--backend", default="harness"); e.add_argument("--model", default="opus")
    e.add_argument("--entail", help="dir with <name>.entail.md from entail.py collect (attached after the novelty card)")
    c = sub.add_parser("collect"); c.add_argument("--out", required=True); c.add_argument("--mapping", required=True)
    r = sub.add_parser("rank"); r.add_argument("--out", required=True)
    a = ap.parse_args(); {"emit": emit, "collect": collect, "rank": rank}[a.cmd](a)
