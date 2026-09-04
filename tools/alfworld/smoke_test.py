#!/usr/bin/env python3
"""Smoke test: load AlfredTWEnv on the reconstructed data, reset a few games, replay each game's
stored walkthrough and check that the episode completes with reward 1. Reports steps/sec."""
import json, os, sys, time, glob
os.environ.setdefault("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
import yaml
from alfworld.agents.environment.alfred_tw_env import AlfredTWEnv

cfg = yaml.safe_load(open("/home/work/neuro/alfworld-src/configs/base_config.yaml"))
def expand(o):
    if isinstance(o, dict): return {k: expand(v) for k, v in o.items()}
    if isinstance(o, list): return [expand(v) for v in o]
    if isinstance(o, str): return os.path.expandvars(o)
    return o
cfg = expand(cfg)
cfg["general"]["use_cuda"] = False
split = sys.argv[1] if len(sys.argv) > 1 else "train"
n_games = int(sys.argv[2]) if len(sys.argv) > 2 else 5

t0 = time.time()
env = AlfredTWEnv(cfg, train_eval=split)
print(f"collected {env.num_games} games for split={split} in {time.time()-t0:.1f}s")
env = env.init_env(batch_size=1)

ok, total_steps, t1 = 0, 0, time.time()
for i in range(n_games):
    obs, info = env.reset()
    gf = info["extra.gamefile"][0]
    walk = json.load(open(gf)).get("walkthrough") or []
    done, reward, steps = False, 0.0, 0
    for a in walk:
        obs, scores, dones, infos = env.step([a]); steps += 1
        done = dones[0]; reward = scores[0]
        if done: break
    total_steps += steps
    tag = "OK" if (done and reward >= 1) else "FAIL"
    if tag == "OK": ok += 1
    print(f"  game {i+1}: {os.path.basename(os.path.dirname(os.path.dirname(gf)))[:52]:52s} walkthrough {len(walk):2d} steps -> done={done} reward={reward} {tag}")
dt = time.time() - t1
print(f"solved {ok}/{n_games} by walkthrough; {total_steps} env steps in {dt:.1f}s ({total_steps/dt:.1f} steps/s, single env)")
print("first observation sample:", obs[0][:300].replace("\n", " ") if isinstance(obs, list) else str(obs)[:300])
