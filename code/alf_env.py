#!/usr/bin/env python3
"""Single-game ALFWorld text environment helper (reconstructed json_2.1.1 data at $ALFWORLD_DATA).
make_env(game_file) -> textworld gym env; reset() -> (obs, info) with info['admissible_commands'], info['won'].
list_games(split) -> sorted list of game.tw-pddl paths (one per trial); task_of(path) -> task directory name."""
import os, glob, json, re
os.environ.setdefault("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
import textworld, textworld.gym
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos

DATA = os.environ["ALFWORLD_DATA"]
TASK_TYPES = ["pick_and_place_simple", "look_at_obj_in_light", "pick_clean_then_place_in_recep",
              "pick_heat_then_place_in_recep", "pick_cool_then_place_in_recep", "pick_two_obj_and_place"]


def list_games(split: str) -> list[str]:
    return sorted(glob.glob(os.path.join(DATA, "json_2.1.1", split, "*", "*", "game.tw-pddl")))


def task_of(game_file: str) -> str:
    return os.path.basename(os.path.dirname(os.path.dirname(game_file)))


def task_type_of(game_file: str) -> str:
    t = task_of(game_file)
    for tt in TASK_TYPES:
        if t.startswith(tt): return tt
    return "unknown"


def make_env(game_file: str, max_steps: int = 50):
    req = textworld.EnvInfos(won=True, admissible_commands=True, extras=["gamefile"])
    env_id = textworld.gym.register_games([game_file], req, batch_size=1, asynchronous=False,
                                          max_episode_steps=max_steps, wrappers=[AlfredDemangler(shuffle=False), AlfredInfos])
    return textworld.gym.make(env_id)


def goal_of(obs: str) -> str:
    m = re.search(r"Your task is to:\s*(.+)", obs)
    return m.group(1).strip() if m else obs.strip()[-200:]


def walkthrough_of(game_file: str) -> list[str]:
    return json.load(open(game_file)).get("walkthrough") or []
