#!/usr/bin/env python3
"""ReAct agent over ALFWorld text games against a local vLLM OpenAI endpoint, with an optional retrieved-experience
memory slot. Scaffold per DESIGN.md §5: goal + history + latest observation + admissible list; reply 'Thought: …'
(optional) then 'Action: <admissible action verbatim>'; one re-prompt on a non-admissible reply, then a no-op step."""
from __future__ import annotations
import os, sys, json, re, time, random, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai import OpenAI
from alf_env import make_env, goal_of, task_of, task_type_of

SYSTEM = ("You are an agent acting in a household text environment. At each turn you receive the goal, the history of your "
          "actions and observations, the latest observation and the list of admissible actions. Choose exactly one "
          "admissible action that makes progress toward the goal. Reply with an optional single line 'Thought: ...' "
          "followed by a line 'Action: <one admissible action, copied verbatim from the list>'.")
MEMORY_SLOT = "\n\nRetrieved experience from past tasks (may or may not help):\n{items}"
INSTRUCTION_SLOT = "\n\nIMPORTANT INSTRUCTION: {instruction}"
STEP_LIMIT = 30
MAX_HISTORY = 30


def format_item(it: dict, max_obs: int = 90) -> str:
    lines = [f"Past task: {it['goal']}"]
    for i, s in enumerate(it["steps"], 1):
        o = s["obs"].replace("\n", " ")
        lines.append(f"  {i}. {s['action']} -> {o[:max_obs]}")
    return "\n".join(lines)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def parse_action(text: str, admissible: list[str]) -> str | None:
    m = re.findall(r"Action:\s*(.+)", text)
    if not m: return None
    cand = norm(m[-1].strip().strip("`'\"."))
    table = {norm(a): a for a in admissible}
    if cand in table: return table[cand]
    for k, a in table.items():          # tolerate trailing punctuation / 'action: go to X.'
        if cand.startswith(k) and len(cand) - len(k) <= 2: return a
    return None


class Agent:
    def __init__(self, base_urls: list[str], model: str = "agent", temperature: float = 0.7, max_tokens: int = 160,
                 enable_thinking: bool = False):
        self.clients = [OpenAI(base_url=u, api_key="none", timeout=180, max_retries=3) for u in base_urls]
        self.model, self.temperature, self.max_tokens = model, temperature, max_tokens
        self.extra = {"chat_template_kwargs": {"enable_thinking": enable_thinking}}
        self._i = os.getpid() % max(1, len(base_urls)); self._lock = threading.Lock()   # stagger replicas across worker processes

    def _client(self):
        # one replica per worker process (pid-hashed): balances load without lock-step, and keeps each episode's
        # growing prefix on one server so vLLM prefix caching hits
        return self.clients[os.getpid() % len(self.clients)]

    def call(self, messages: list[dict], seed: int) -> tuple[str, int, int]:
        r = self._client().chat.completions.create(model=self.model, messages=messages, temperature=self.temperature,
                                                   max_tokens=self.max_tokens, seed=seed, extra_body=self.extra)
        u = r.usage
        return (r.choices[0].message.content or ""), (u.prompt_tokens if u else 0), (u.completion_tokens if u else 0)

    def run_episode(self, game_file: str, seed: int, memory_items: list[dict] | None = None, instruction: str | None = None,
                    step_limit: int = STEP_LIMIT) -> dict:
        env = make_env(game_file, max_steps=step_limit + 5)
        obs, info = env.reset(); obs = obs[0] if isinstance(obs, (list, tuple)) else obs
        goal = goal_of(obs)
        system = SYSTEM
        if instruction: system += INSTRUCTION_SLOT.format(instruction=instruction)
        mem_tokens_est = 0
        if memory_items:
            items = "\n\n".join(format_item(it) for it in memory_items)
            system += MEMORY_SLOT.format(items=items); mem_tokens_est = len(items) // 4
        history: list[tuple[str, str]] = []
        log = {"game_file": game_file, "task": task_of(game_file), "type": task_type_of(game_file), "goal": goal, "seed": seed,
               "k": len(memory_items or []), "memory_ids": [it.get("task") for it in (memory_items or [])],
               "mem_tokens_est": mem_tokens_est, "instruction": bool(instruction), "actions": [], "steps": 0, "calls": 0,
               "invalid": 0, "prompt_tokens": 0, "completion_tokens": 0, "won": False, "timeout": False, "error": None}
        won, cur_obs, t0 = False, obs, time.time()
        try:
            for step in range(step_limit):
                adm = info["admissible_commands"]; adm = adm[0] if adm and isinstance(adm[0], list) else adm
                hist_txt = "\n".join(f"> {a}\n{o[:300]}" for a, o in history[-MAX_HISTORY:]) or "(none yet)"
                user = (f"Goal: {goal}\n\nHistory:\n{hist_txt}\n\nLatest observation:\n{cur_obs[:600]}\n\n"
                        f"Admissible actions: {' | '.join(adm)}\n\nReply with 'Thought: ...' (optional) then 'Action: <one admissible action>'.")
                messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
                text, pt, ct = self.call(messages, seed * 100003 + step * 2)
                log["calls"] += 1; log["prompt_tokens"] += pt; log["completion_tokens"] += ct
                act = parse_action(text, adm)
                if act is None:
                    messages.append({"role": "assistant", "content": text})
                    messages.append({"role": "user", "content": "That is not admissible. Reply with 'Action: <one action copied verbatim from the admissible list>'."})
                    text, pt, ct = self.call(messages, seed * 100003 + step * 2 + 1)
                    log["calls"] += 1; log["prompt_tokens"] += pt; log["completion_tokens"] += ct
                    act = parse_action(text, adm)
                if act is None:
                    log["invalid"] += 1; log["actions"].append(None); history.append(("(invalid)", "Nothing happens."))
                    cur_obs = "Nothing happens."; log["steps"] += 1; continue
                o, score, dones, info = env.step([act]); o = o[0] if isinstance(o, (list, tuple)) else o
                log["actions"].append(act); log["steps"] += 1; history.append((act, o)); cur_obs = o
                d = dones[0] if isinstance(dones, (list, tuple)) else dones
                w = info["won"][0] if isinstance(info["won"], (list, tuple)) else info["won"]
                if d or w:
                    won = bool(w); break
            log["timeout"] = (not won) and log["steps"] >= step_limit
        except Exception as e:
            log["error"] = repr(e)[:300]
        finally:
            try: env.close()
            except Exception: pass
        log["won"] = won; log["wall_s"] = round(time.time() - t0, 1)
        return log
