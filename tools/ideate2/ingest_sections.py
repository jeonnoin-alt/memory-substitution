#!/usr/bin/env python3
"""Merge harness section-read results (subagent task outputs) into a prescan papers.jsonl.

Usage: ingest_sections.py <papers.jsonl> <mapping.json>
  mapping.json = {"<arxiv id>": "<task id>", ...}   (written by hand or by run.py when jobs are launched)
Each task output is a JSONL transcript; the last assistant text block that parses as a JSON object
with an "arxiv" key is taken as the section record {limitations, conclusion, method, sources}.
"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend import parse_json, TASKS_DIR
from lit import load_jsonl, save_jsonl


def assistant_texts(path: str) -> list[str]:
    texts = []
    for line in open(path):
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
    return texts


def main():
    papers = load_jsonl(sys.argv[1]); mapping = json.load(open(sys.argv[2]))
    by = {p.arxiv: p for p in papers if p.arxiv}
    n = 0
    for arx, tid in mapping.items():
        path = os.path.join(TASKS_DIR, tid + ".output")
        if not os.path.exists(path) or arx not in by:
            continue
        for t in reversed(assistant_texts(path)):
            try:
                d = parse_json(t)
            except Exception:
                continue
            if isinstance(d, dict) and "arxiv" in d:
                by[arx].sections = {k: d.get(k, "") for k in ("limitations", "conclusion", "method") if d.get(k)}
                by[arx].sections["_sources"] = d.get("sources", [])
                n += 1
                break
    save_jsonl(papers, sys.argv[1])
    print(f"ingested sections for {n}/{len(mapping)} papers")


if __name__ == "__main__":
    main()
