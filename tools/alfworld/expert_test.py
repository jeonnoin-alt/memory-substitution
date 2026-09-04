#!/usr/bin/env python3
"""Expert-driven smoke test: drive games with ALFWorld's bundled handcoded expert (which needs the
pddl_params in our traj_data stubs) instead of the stored walkthrough. Works on any split by pointing
the 'train' data path at that split, because the env only exposes extra.expert_plan in train mode."""
import os, sys, time, yaml
os.environ.setdefault("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
from alfworld.agents.environment.alfred_tw_env import AlfredTWEnv

split = sys.argv[1] if len(sys.argv) > 1 else "valid_unseen"
n_games = int(sys.argv[2]) if len(sys.argv) > 2 else 5
cfg = yaml.safe_load(open("/home/work/neuro/alfworld-src/configs/base_config.yaml"))
def ex(o):
    return {k: ex(v) for k, v in o.items()} if isinstance(o, dict) else ([ex(v) for v in o] if isinstance(o, list) else (os.path.expandvars(o) if isinstance(o, str) else o))
cfg = ex(cfg); cfg["general"]["use_cuda"] = False
cfg["dataset"]["data_path"] = os.path.join(os.environ["ALFWORLD_DATA"], "json_2.1.1", split)
cfg["env"]["domain_randomization"] = False
env = AlfredTWEnv(cfg, train_eval="train").init_env(batch_size=1)
ok, steps_total, t0 = 0, 0, time.time()
for i in range(n_games):
    obs, info = env.reset(); gf = info["extra.gamefile"][0]
    done, score, steps = False, 0, 0
    while not done and steps < 60:
        plan = info["extra.expert_plan"][0]            # batch env: one plan (list of commands) per env
        a = plan[0] if isinstance(plan, list) else plan
        obs, scores, dones, info = env.step([a]); steps += 1; done = dones[0]; score = scores[0]
    steps_total += steps; ok += int(done and score >= 1)
    print(f"  game {i+1}: {gf.split('/')[-3][:50]:50s} expert {steps:2d} steps -> {'OK' if done and score>=1 else 'FAIL'}")
dt = time.time() - t0
print(f"expert solved {ok}/{n_games}; {steps_total} steps in {dt:.1f}s ({steps_total/dt:.1f} steps/s incl. resets)")
