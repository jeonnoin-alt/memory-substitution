#!/usr/bin/env python3
"""Write the minimal traj_data.json the text-only AlfredTWEnv needs next to every game.tw-pddl
(collect_game_files reads only traj_data['task_type']). Task type and id come from the HF rows."""
import json, os
ROOT = os.environ.get("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
SPLITS = {"train": "train", "eval_in_distribution": "valid_seen", "eval_out_of_distribution": "valid_unseen"}
n = 0
for split, outdir in SPLITS.items():
    cache = f"{ROOT}/raw/{split}.jsonl"
    if not os.path.exists(cache):
        print("missing", cache); continue
    for line in open(cache):
        r = json.loads(line)
        d = os.path.join(ROOT, "json_2.1.1", outdir, os.path.dirname(r["game_file_path"]))
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "traj_data.json")
        if not os.path.exists(p):
            # pddl_params reconstructed from the task directory name
            # (task_type-object_target-mrecep_target-parent_or_toggle_target-scene); the handcoded
            # expert reads object_target / parent_target / toggle_target and nothing else.
            task_dir = os.path.basename(os.path.dirname(os.path.dirname(r["game_file_path"])))  # <task>/<trial>/game.tw-pddl
            tt, obj, mrecep, third, scene = task_dir.rsplit("-", 4)
            pp = {"object_target": obj, "mrecep_target": "" if mrecep == "None" else mrecep,
                  "parent_target": "", "toggle_target": "", "object_sliced": obj.endswith("Sliced")}
            if tt == "look_at_obj_in_light":
                pp["toggle_target"] = third
            else:
                pp["parent_target"] = "" if third == "None" else third
            json.dump({"task_type": r["task_type"], "task_id": r["id"], "pddl_params": pp,
                       "scene": {"scene_num": int(scene)}, "turk_annotations": {"anns": []},
                       "source": "awawa-agi/alfworld-raw via datasets-server; traj_data stub"}, open(p, "w"))
        n += 1
print("stubs written/checked:", n)
for outdir in SPLITS.values():
    games = sum(1 for root, _, files in os.walk(os.path.join(ROOT, "json_2.1.1", outdir)) if "game.tw-pddl" in files)
    print(f"  {outdir}: {games} game dirs")
