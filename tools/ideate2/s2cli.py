#!/usr/bin/env python3
"""Semantic Scholar search for subagents (keyed, IP-pinned). Use this BEFORE any web search.
  s2cli.py search "<query>" [--limit 8] [--recent]     # --recent = last 12 months only
  s2cli.py paper <arXiv id | S2 id | DOI>              # verify an id / get abstract
Prints one paper per block: id, arXiv, date, venue, citations, title, TL;DR or abstract head.
Exit code 0 even when nothing is found (prints 'no results'). Never prints the key."""
import sys, os, datetime, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("S2_PIN_IP", "18.244.60.91")
from lit import S2Client

def show(p):
    print(f"- {p.id} | arXiv:{p.arxiv or '-'} | {p.date or p.year or '?'} | {p.venue or 'preprint'} | cit {p.citations or 0}\n  {p.title}\n  {(p.tldr or p.abstract or '')[:400]}")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["search", "paper"]); ap.add_argument("arg")
    ap.add_argument("--limit", type=int, default=8); ap.add_argument("--recent", action="store_true")
    a = ap.parse_args(); s2 = S2Client()
    if not s2.ok: print("S2 unavailable (key or network)"); return
    if a.cmd == "search":
        yf = datetime.date.today().year - 1 if a.recent else None
        res = s2.search(a.arg, a.limit, year_from=yf)
        if not res: print("no results"); return
        for p in res: show(p)
    else:
        ident = a.arg if ":" in a.arg or len(a.arg) == 40 else f"arXiv:{a.arg}"
        p = s2.paper(ident)
        print("not found (S2 may lag arXiv by days to weeks; verify with a web search only if needed)") if not (p and p.title) else show(p)

if __name__ == "__main__":
    main()
