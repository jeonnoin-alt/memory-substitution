#!/usr/bin/env python3
"""Paired k-sweep: every (game, seed) is run at every k with the same retrieved items prefix (top-k of the same ranking).
Resumable, append-only JSONL. Usage:
  run_sweep.py --splits valid_seen,valid_unseen --ks 0,1,3,7 --seeds 11,23 --bank runs/bank/expert_shard*.jsonl --out runs/sweep/k_sweep.jsonl --workers 16"""
import os, sys, json, glob, argparse, random
from multiprocessing import Pool          # TextWorld's tatsu grammar parser is not thread-safe: one process per episode worker
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alf_env import list_games, task_of, goal_of, make_env
from agent import Agent
from bank import Bank

ap = argparse.ArgumentParser()
ap.add_argument("--splits", default="valid_seen,valid_unseen"); ap.add_argument("--ks", default="0,1,3,7")
ap.add_argument("--seeds", default="11,23"); ap.add_argument("--bank", default="runs/bank/expert_shard*.jsonl")
ap.add_argument("--out", required=True); ap.add_argument("--workers", type=int, default=16)
ap.add_argument("--servers", default="http://localhost:8000/v1,http://localhost:8001/v1")
ap.add_argument("--limit", type=int, default=0, help="first N games per split (smoke)")
ap.add_argument("--instruction", default=None)
a = ap.parse_args()
ks = [int(x) for x in a.ks.split(",")]; seeds = [int(x) for x in a.seeds.split(",")]
games = []
for s in a.splits.split(","):
    g = list_games(s); games += [(s, x) for x in (g[:a.limit] if a.limit else g)]
bank = Bank(sorted(glob.glob(a.bank))); print(f"bank items: {len(bank.items)}", flush=True)
os.makedirs(os.path.dirname(a.out), exist_ok=True)
done = set()
if os.path.exists(a.out):
    for l in open(a.out):
        d = json.loads(l)
        if not d.get("error"): done.add((d["game_file"], d["seed"], d["k"]))   # errored episodes are re-run
fout = open(a.out, "a")
# goal text for retrieval comes from the game's initial observation (cheap: reset once per game)
GOAL_CACHE = os.path.join(os.path.dirname(a.out), "goals.json")
goal_cache = json.load(open(GOAL_CACHE)) if os.path.exists(GOAL_CACHE) else {}
def goal_for(gf):
    if gf not in goal_cache:
        env = make_env(gf); obs, _ = env.reset(); env.close()
        goal_cache[gf] = goal_of(obs[0] if isinstance(obs, (list, tuple)) else obs)
        json.dump(goal_cache, open(GOAL_CACHE, "w"))
    return goal_cache[gf]
jobs = [(s, gf, seed, k) for (s, gf) in games for seed in seeds for k in ks if (gf, seed, k) not in done]
random.Random(0).shuffle(jobs)
print(f"jobs: {len(jobs)} (skipping {len(done)} done)", flush=True)
_agent = None
def _init(servers, instruction):
    global _agent, _instruction
    _agent = Agent(servers); _instruction = instruction
def work(job):
    s, gf, seed, k, items = job
    r = _agent.run_episode(gf, seed, memory_items=items, instruction=_instruction); r["split"] = s
    return r
# retrieval in the parent (one MiniLM), episodes in worker processes
jobs2 = []
for (s, gf, seed, k) in jobs:
    items = bank.retrieve(goal_for(gf), max(ks), exclude_task=task_of(gf))[:k] if k > 0 else []
    jobs2.append((s, gf, seed, k, items))
n = 0; won = 0
with Pool(a.workers, initializer=_init, initargs=(a.servers.split(","), a.instruction)) as pool:
    for r in pool.imap_unordered(work, jobs2):
        fout.write(json.dumps(r) + "\n"); fout.flush(); n += 1; won += int(r["won"])
        if n % 20 == 0 or n == len(jobs2):
            print(f"{n}/{len(jobs2)} done, running success {won/n:.3f}", flush=True)
print("finished", flush=True)
