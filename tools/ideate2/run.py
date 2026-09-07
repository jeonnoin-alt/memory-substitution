#!/usr/bin/env python3
"""ideate2 orchestrator (thin). Stages are separate scripts so each can be run and tested alone.

  run.py status  --work W                      # list pending/finished jobs
  run.py collect --work W --job <job_id> --task <claude_task_id>   # ingest one subagent result
  run.py results --work W --kind <kind>        # merge finished results of a kind into one JSON

Typical harness flow for a slug S under work dir W=runs_ideate2/S:
  prescan.py plan/collect/cards/synth/digest  → brief_with_digest.md
  axes generation: one job per axis (axes.py emit) → collect → merge → ideas.json
  gate.py → adjudication jobs → collect → gate.py apply
  novelty_check.py → cards
  review.py emit (n=1) → collect → aggregate → escalate? → emit (n=2, start=2)
Python: use /home/work/neuro/alfworld-env/bin/python for gate/novelty (sentence-transformers) and
S2_PIN_IP=18.244.60.91 for the collectors on this node.
"""
from __future__ import annotations
import os, sys, json, glob, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import Backend, TASKS_DIR


def find_job(work: str, jid: str) -> tuple[str, dict]:
    for p in glob.glob(os.path.join(work, "**", "jobs", jid + ".json"), recursive=True):
        return p, json.load(open(p))
    raise SystemExit(f"job {jid} not found under {work}")


def status(a):
    for p in sorted(glob.glob(os.path.join(a.work, "**", "jobs", "*.json"), recursive=True)):
        j = json.load(open(p)); print(f"{j['status']:9s} {j['kind']:16s} {j['id']}")


def collect(a):
    p, j = find_job(a.work, a.job)
    be = Backend("harness", os.path.dirname(p))
    res = be.collect(j, a.task)
    rp = p.replace(".json", ".result.json")
    json.dump(res, open(rp, "w"), indent=1, ensure_ascii=False)
    j["status"] = "done"; j["task"] = a.task; j["result_file"] = rp
    json.dump(j, open(p, "w"), indent=1)
    print("collected", j["id"], "->", rp)


def results(a):
    out = {}
    for p in sorted(glob.glob(os.path.join(a.work, "**", "jobs", f"{a.kind}__*.result.json"), recursive=True)):
        name = os.path.basename(p)[len(a.kind) + 2:-len(".result.json")]
        out[name] = json.load(open(p))
    dst = os.path.join(a.work, f"{a.kind}_results.json")
    json.dump(out, open(dst, "w"), indent=1, ensure_ascii=False)
    print(f"{len(out)} results -> {dst}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status"); s.add_argument("--work", required=True)
    c = sub.add_parser("collect"); c.add_argument("--work", required=True); c.add_argument("--job", required=True); c.add_argument("--task", required=True)
    r = sub.add_parser("results"); r.add_argument("--work", required=True); r.add_argument("--kind", required=True)
    a = ap.parse_args()
    {"status": status, "collect": collect, "results": results}[a.cmd](a)
