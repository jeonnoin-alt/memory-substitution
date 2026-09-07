#!/usr/bin/env python3
"""Experience bank: JSONL items {task,type,goal,steps[{action,obs}],won}; MiniLM retrieval on the goal text."""
from __future__ import annotations
import os, json, numpy as np
MINILM = "/home/work/neuro/models/paraphrase-multilingual-MiniLM-L12-v2"


class Bank:
    def __init__(self, paths: list[str], only_won: bool = True):
        self.items = []
        for p in paths:
            for l in open(p):
                d = json.loads(l)
                if d.get("error") or (only_won and not d.get("won")): continue
                self.items.append(d)
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(MINILM, device="cpu")
        self.E = self.model.encode([it["goal"] for it in self.items], normalize_embeddings=True, show_progress_bar=False)

    def retrieve(self, goal: str, k: int, exclude_task: str | None = None) -> list[dict]:
        if k <= 0: return []
        q = self.model.encode([goal], normalize_embeddings=True)[0]
        sims = self.E @ q
        order = np.argsort(-sims)
        out = []
        for i in order:
            it = self.items[int(i)]
            if exclude_task and it["task"] == exclude_task: continue
            out.append(it)
            if len(out) >= k: break
        return out
