#!/usr/bin/env python3
"""Parallel goal-sentence cache for the eval games (avoids serial env resets in the sweep runner). Usage: build_goals.py <shard> <n> <out>"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alf_env import list_games, make_env, goal_of
shard, n, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
splits = sys.argv[4].split(",") if len(sys.argv) > 4 else ["valid_seen", "valid_unseen"]
games = [g for s in splits for g in list_games(s)]
res = {}
for i, gf in enumerate(games):
    if i % n != shard: continue
    env = make_env(gf); obs, _ = env.reset(); env.close()
    res[gf] = goal_of(obs[0] if isinstance(obs, (list, tuple)) else obs)
json.dump(res, open(out, "w"))
