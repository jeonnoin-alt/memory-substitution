#!/usr/bin/env python3
"""LLM backends for ideate2.

api     : Anthropic API via AI-Scientist-v2's client (needs ANTHROPIC_API_KEY).
harness : write a job file; the driving Claude Code session launches a subagent per job and
          `collect()` ingests the subagent's final JSON from the tasks directory.
Both backends use the same prompt strings, so results are comparable.
"""
from __future__ import annotations
import os, re, json, glob, hashlib, sys
from typing import Any, Optional

AI_SCI = "/home/work/neuro/AI-Scientist-v2"
TASKS_DIR = os.environ.get("IDEATE2_TASKS_DIR",
                           "/tmp/claude-1100/-home-work/e733781c-e436-47c6-a8ef-f6847c3d8c54/tasks")


def job_id(kind: str, name: str) -> str:
    return f"{kind}__{re.sub(r'[^A-Za-z0-9_.-]', '_', name)[:60]}"


class Backend:
    def __init__(self, mode: str, jobs_dir: str, model: str = "opus"):
        assert mode in ("api", "harness")
        self.mode, self.jobs_dir, self.model = mode, jobs_dir, model
        os.makedirs(jobs_dir, exist_ok=True)
        self._client = None
        if mode == "api":
            sys.path.insert(0, AI_SCI)
            from ai_scientist.llm import create_client
            from ai_scientist import model_registry
            m = model_registry.resolve(model, "ideation")
            self._client, self._model_name = create_client(m)

    # ---- api ------------------------------------------------------------ #
    def _api_json(self, system: str, user: str, tools: list | None = None, max_tokens: int = 8000) -> Any:
        from ai_scientist import anthropic_compat
        kw = anthropic_compat.message_kwargs(self._model_name, max_tokens=max_tokens)
        if tools:
            kw["tools"] = tools
        msg = self._client.messages.create(system=system, messages=[{"role": "user", "content": user}], **kw)
        anthropic_compat.record_usage(msg)
        text = anthropic_compat.extract_text(msg)
        return parse_json(text)

    # ---- harness -------------------------------------------------------- #
    def emit(self, kind: str, name: str, system: str, user: str, tools: list[str] | None = None,
             model: str | None = None, expects: str = "json") -> dict:
        jid = job_id(kind, name)
        prompt_path = os.path.join(self.jobs_dir, jid + ".prompt.md")
        with open(prompt_path, "w") as f:
            f.write(f"=== SYSTEM ===\n{system}\n\n=== USER ===\n{user}\n")
        job = {"id": jid, "kind": kind, "name": name, "prompt_file": prompt_path,
               "tools": tools or [], "model": model or self.model, "expects": expects, "status": "pending"}
        with open(os.path.join(self.jobs_dir, jid + ".json"), "w") as f:
            json.dump(job, f, indent=1)
        return job

    def call(self, kind: str, name: str, system: str, user: str, tools: list[str] | None = None,
             model: str | None = None) -> Any:
        """api: returns parsed JSON now. harness: returns the job dict (result later via collect)."""
        if self.mode == "api":
            return self._api_json(system, user)
        return self.emit(kind, name, system, user, tools, model)

    def agent_prompt(self, job: dict) -> str:
        """The text to hand to a Claude Code subagent for this job."""
        tools_line = ("You MAY use the WebSearch tool (server-side); at most 6 searches. "
                      if "WebSearch" in job["tools"] else "Do not search the web. ")
        return (f"Read the file {job['prompt_file']} in full with the Read tool. It has a SYSTEM section and a USER "
                f"section. Follow the SYSTEM instructions exactly. Do not read any other local files. {tools_line}"
                f"Produce your final answer as ONLY a single {'JSON object' if job['expects']=='json' else 'markdown document'}"
                f"{' that validates against any schema in the SYSTEM section' if job['expects']=='json' else ''}; "
                f"no prose before or after, no code fences.")

    def collect(self, job: dict, task_id: str) -> Any:
        """Ingest a finished subagent's final JSON by its task id."""
        path = os.path.join(TASKS_DIR, task_id + ".output")
        texts = []
        for line in open(path):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            msg = rec.get("message", rec)
            if (msg.get("role") or rec.get("type")) != "assistant":
                continue
            c = msg.get("content")
            if isinstance(c, str):
                texts.append(c)
            elif isinstance(c, list):
                texts += [b["text"] for b in c if isinstance(b, dict) and b.get("type") == "text" and b.get("text")]
        for t in reversed(texts):
            try:
                return parse_json(t) if job["expects"] == "json" else t
            except Exception:
                continue
        raise ValueError(f"no parseable result in {path}")


def parse_json(s: str) -> Any:
    """Return the last balanced JSON object/array in s."""
    s = re.sub(r"^```(?:json)?\s*", "", s.strip()); s = re.sub(r"\s*```$", "", s)
    cands = []
    skip_to = -1
    for i, ch in enumerate(s):
        if ch not in "{[" or i < skip_to:   # only top-level spans: nested brackets are inside an earlier span
            continue
        depth, instr, esc = 0, False, False
        for j in range(i, len(s)):
            c = s[j]
            if instr:
                if esc: esc = False
                elif c == "\\": esc = True
                elif c == '"': instr = False
                continue
            if c == '"': instr = True
            elif c in "{[": depth += 1
            elif c in "}]":
                depth -= 1
                if depth == 0:
                    cands.append(s[i:j + 1]); skip_to = j + 1; break
    for c in reversed(cands):
        try:
            return json.loads(c)
        except Exception:
            pass
    # Truncated tail (subagent transcripts have been observed to drop the final closing brace):
    # find the last top-level opener, replay the bracket stack and append the missing closers.
    starts = [i for i, ch in enumerate(s) if ch in "{["]
    if starts:
        i = starts[0]; stack = []; instr = esc = False
        for c in s[i:]:
            if instr:
                if esc: esc = False
                elif c == "\\": esc = True
                elif c == '"': instr = False
                continue
            if c == '"': instr = True
            elif c in "{[": stack.append("}" if c == "{" else "]")
            elif c in "}]" and stack: stack.pop()
        if stack:
            try:
                return json.loads(s[i:] + "".join(reversed(stack)))
            except Exception:
                pass
    raise ValueError("no JSON found")
