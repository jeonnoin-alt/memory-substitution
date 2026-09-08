#!/usr/bin/env python3
"""Measurement C: static procedure prompts vs retrieval (the cheap baseline four judges asked for).
Arms (all paired on the same (game, seed) as the k-sweep):
  static1   one FIXED expert exemplar of the task's type in the memory slot (no retriever; token-matched to k=1)
  static3   three fixed exemplars of the type (token-matched to k=3)
  blind1    one fixed exemplar of a DIFFERENT type (length placebo)
  instr     a hand-written one-paragraph procedure for the task's type in the instruction slot (no memory)
  instr_all all six procedures in the instruction slot (type-agnostic static prompt, no memory)
Usage: run_static.py --arms static1,static3,blind1,instr,instr_all --out runs/static/static_c.jsonl --workers 32"""
import os, sys, json, glob, argparse, random
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alf_env import list_games, task_type_of
from agent import Agent

TYPES = ["pick_and_place_simple", "pick_two_obj_and_place", "look_at_obj_in_light",
         "pick_clean_then_place_in_recep", "pick_heat_then_place_in_recep", "pick_cool_then_place_in_recep"]
PROC = {
 "pick_and_place_simple": "Procedure for 'put X in/on Y': objects sit in or on receptacles. Go to the likeliest receptacle for X, open it if it is closed, take X, then go to Y and put X in/on Y.",
 "pick_two_obj_and_place": "Procedure for 'put two X in Y': you can carry one object at a time. Find and take the first X, go to Y, put it in/on Y; then find and take the second X and put it in/on Y as well.",
 "look_at_obj_in_light": "Procedure for 'look at X under the lamp': find and take X, go to the desklamp/floorlamp, then use the lamp while holding X.",
 "pick_clean_then_place_in_recep": "Procedure for 'put a clean X in Y': find and take X, go to the sinkbasin, clean X with the sinkbasin, then go to Y and put X in/on Y.",
 "pick_heat_then_place_in_recep": "Procedure for 'put a hot X in Y': find and take X, go to the microwave, heat X with the microwave, then go to Y and put X in/on Y.",
 "pick_cool_then_place_in_recep": "Procedure for 'put a cool X in Y': find and take X, go to the fridge, cool X with the fridge, then go to Y and put X in/on Y.",
}
ALL = "Task procedures. " + " ".join(PROC[t] for t in TYPES)

ap = argparse.ArgumentParser()
ap.add_argument("--splits", default="valid_seen,valid_unseen"); ap.add_argument("--arms", default="static1,static3,blind1,instr,instr_all")
ap.add_argument("--seeds", default="11,23"); ap.add_argument("--bank", default="runs/bank/expert_shard*.jsonl")
ap.add_argument("--out", required=True); ap.add_argument("--workers", type=int, default=32)
ap.add_argument("--servers", default="http://localhost:8000/v1,http://localhost:8001/v1"); ap.add_argument("--limit", type=int, default=0)
a = ap.parse_args()
arms = a.arms.split(","); seeds = [int(x) for x in a.seeds.split(",")]
# fixed exemplars: per type, the three shortest won expert trajectories (deterministic)
items = [json.loads(l) for p in sorted(glob.glob(a.bank)) for l in open(p)]
by_type = {}
for it in items:
    if it.get("won"): by_type.setdefault(it["type"], []).append(it)
EX = {t: sorted(v, key=lambda it: (len(it["steps"]), it["task"]))[:3] for t, v in by_type.items()}
print({t: [x["task"] for x in v] for t, v in EX.items()}, flush=True)
def arm_inputs(t, arm):
    nxt = TYPES[(TYPES.index(t) + 1) % len(TYPES)]
    return {"static1": (EX[t][:1], None), "static3": (EX[t][:3], None), "blind1": (EX[nxt][:1], None),
            "instr": ([], PROC[t]), "instr_all": ([], ALL)}[arm]
games = []
for s in a.splits.split(","):
    g = list_games(s); games += [(s, x) for x in (g[:a.limit] if a.limit else g)]
os.makedirs(os.path.dirname(a.out), exist_ok=True); done = set()
if os.path.exists(a.out):
    for l in open(a.out):
        d = json.loads(l)
        if not d.get("error"): done.add((d["game_file"], d["seed"], d["arm"]))
fout = open(a.out, "a")
jobs = [(s, gf, seed, arm) for (s, gf) in games for seed in seeds for arm in arms if (gf, seed, arm) not in done]
random.Random(0).shuffle(jobs); print(f"jobs: {len(jobs)} (skipping {len(done)} done)", flush=True)
_agent = None
def _init(servers):
    global _agent; _agent = Agent(servers)
def work(job):
    s, gf, seed, arm = job
    mem, ins = arm_inputs(task_type_of(gf), arm)
    r = _agent.run_episode(gf, seed, memory_items=mem, instruction=ins); r["split"] = s; r["arm"] = arm; r["type"] = task_type_of(gf)
    return r
n = won = 0
with Pool(a.workers, initializer=_init, initargs=(a.servers.split(","),)) as pool:
    for r in pool.imap_unordered(work, jobs):
        fout.write(json.dumps(r) + "\n"); fout.flush(); n += 1; won += int(r["won"])
        if n % 20 == 0 or n == len(jobs): print(f"{n}/{len(jobs)} done, running success {won/n:.3f}", flush=True)
print("finished", flush=True)
