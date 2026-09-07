#!/usr/bin/env python3
"""Stage 2 — Axial generation: one generator job per axis (fresh context), then merge.

  axes.py emit  --axes axes.json --brief brief_with_digest.md --cards cards.jsonl --gaps gaps.json --n 3 --out W/gen
  axes.py merge --out W/gen  → W/gen/ideas.json  (after `run.py collect` for every job)
"""
from __future__ import annotations
import os, sys, json, argparse, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import Backend
import prompts as P


def emit(a):
    axes = json.load(open(a.axes))["axes"]; brief = open(a.brief).read()
    cards = [json.loads(l) for l in open(a.cards)] if a.cards and os.path.exists(a.cards) else []
    gaps = json.load(open(a.gaps)) if a.gaps and os.path.exists(a.gaps) else []
    multi = [c for c in cards if len(c.get("axes") or []) >= 2]
    be = Backend(a.backend, os.path.join(a.out, "jobs"), a.model)
    gid = 0; gap_ids = {}
    for g in gaps:
        for x in g["gaps"]:
            gid += 1; gap_ids.setdefault(g["axis"], []).append(f"G{gid}: {x['gap']} (cards {', '.join(x['card_ids'])})")
    for ax in axes:
        own = [c for c in cards if ax["name"] in (c.get("axes") or [])]
        cards_txt = "\n".join(f"- {c['id']} ({c.get('date','')}): {c['claim']} | limitations: {c['stated_limitations']} | not tested: {c['not_tested']}"
                              for c in own + [m for m in multi if m not in own]) or "(no digest cards for this axis)"
        gaps_txt = "\n".join("- " + g for g in gap_ids.get(ax["name"], [])) or "(none)"
        user = P.AXIS_GENERATION_USER.format(brief=brief, axis_name=ax["name"], axis_definition=ax["definition"],
                                             gaps=gaps_txt, cards=cards_txt, n=a.n)
        be.emit("axis_gen", ax["name"], P.AXIS_GENERATION_SYSTEM, user, tools=["WebSearch"], model=a.model)
    print(f"{len(axes)} generator jobs -> {be.jobs_dir}")


def merge(a):
    ideas = []
    for p in sorted(glob.glob(os.path.join(a.out, "jobs", "axis_gen__*.result.json"))):
        r = json.load(open(p)); axis = os.path.basename(p)[len("axis_gen__"):-len(".result.json")]
        for i in r.get("proposals", []):
            i["_axis"] = axis; ideas.append(i)
    json.dump(ideas, open(os.path.join(a.out, "ideas.json"), "w"), indent=1, ensure_ascii=False)
    print(f"merged {len(ideas)} ideas -> {a.out}/ideas.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["emit", "merge"])
    ap.add_argument("--axes"); ap.add_argument("--brief"); ap.add_argument("--cards"); ap.add_argument("--gaps")
    ap.add_argument("--n", type=int, default=3); ap.add_argument("--out", required=True)
    ap.add_argument("--backend", default="harness"); ap.add_argument("--model", default="fable", help="generation model; PI policy 2026-09-07: Fable 5.1 generates, Opus judges, Sonnet prohibited")
    a = ap.parse_args(); emit(a) if a.cmd == "emit" else merge(a)
