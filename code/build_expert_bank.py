#!/usr/bin/env python3
"""Replay each train game's stored walkthrough once and record (goal, task, actions, observations) as a bank item.
Usage: build_expert_bank.py <shard> <nshards> <out.jsonl>   (one trial per task; shard by task index)"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alf_env import list_games, task_of, task_type_of, make_env, goal_of, walkthrough_of

shard, nsh, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
games = list_games("train")
first = {}
for g in games:                       # one trial per task: the lexicographically first trial dir
    first.setdefault(task_of(g), g)
tasks = sorted(first)
mine = [first[t] for i, t in enumerate(tasks) if i % nsh == shard]
done = set()
if os.path.exists(out):
    done = {json.loads(l)["task"] for l in open(out)}
f = open(out, "a"); t0 = time.time(); n = 0
for gf in mine:
    task = task_of(gf)
    if task in done: continue
    try:
        env = make_env(gf)
        obs, info = env.reset(); obs = obs[0] if isinstance(obs, (list, tuple)) else obs
        goal = goal_of(obs); init_obs = obs
        steps = []; won = False
        for a in walkthrough_of(gf):
            obs, score, dones, info = env.step([a]); obs = obs[0] if isinstance(obs, (list, tuple)) else obs
            steps.append({"action": a, "obs": obs})
            if dones[0] if isinstance(dones, (list, tuple)) else dones:
                won = bool(info["won"][0] if isinstance(info["won"], (list, tuple)) else info["won"]); break
        env.close()
        f.write(json.dumps({"task": task, "type": task_type_of(gf), "game_file": gf, "goal": goal, "init_obs": init_obs,
                            "steps": steps, "won": won}) + "\n"); f.flush(); n += 1
    except Exception as e:
        f.write(json.dumps({"task": task, "game_file": gf, "error": repr(e)[:200]}) + "\n"); f.flush()
print(f"shard {shard}: {n} items in {time.time()-t0:.0f}s")
