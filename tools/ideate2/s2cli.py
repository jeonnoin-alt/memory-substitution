#!/usr/bin/env python3
"""Literature lookup for subagents: Semantic Scholar (keyed, IP-pinned, throttled) + HuggingFace papers (unkeyed,
indexes arXiv within a day). Use this BEFORE any web search.
  s2cli.py search "<query>" [--limit 8] [--recent]     # both channels, merged and deduped; --recent = last 12 months
  s2cli.py paper <arXiv id>                             # verify an id / get the abstract (S2, then HF)
One paper per block: source ids, date, venue, citations, title, TL;DR or abstract head. Never prints the key."""
import sys, os, datetime, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("S2_PIN_IP", "18.244.60.91")
from lit import S2Client, HFClient, dedupe


def show(p):
    src = "/".join(p.sources) if p.sources else "?"
    print(f"- [{src}] arXiv:{p.arxiv or '-'} | {p.date or p.year or '?'} | {p.venue or 'preprint'} | cit {p.citations or 0}\n"
          f"  {p.title}\n  {(p.tldr or p.abstract or '')[:400]}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["search", "paper"]); ap.add_argument("arg")
    ap.add_argument("--limit", type=int, default=8); ap.add_argument("--recent", action="store_true")
    a = ap.parse_args(); s2, hf = S2Client(), HFClient()
    if a.cmd == "search":
        yf = datetime.date.today().year - 1 if a.recent else None
        res = []
        if hf.ok:
            res += hf.search(a.arg, a.limit)
        if s2.ok:
            res += s2.search(a.arg, a.limit, year_from=yf)
        res = dedupe(res)
        if a.recent:
            res = [p for p in res if (p.year or 0) >= yf or (p.date or "") >= f"{yf}-"]
        res.sort(key=lambda p: (p.date or str(p.year or "")), reverse=True)
        if not res: print("no results on S2 or HF (try a shorter, more literal query; then WebSearch)"); return
        for p in res[:a.limit]: show(p)
        print(f"({len(res)} unique; channels: s2={'ok' if s2.ok else 'down'} hf={'ok' if hf.ok else 'down'})")
    else:
        arx = a.arg.replace("arXiv:", "").strip()
        p = s2.paper(f"arXiv:{arx}") if s2.ok else None
        if not (p and p.title) and hf.ok:
            p = hf.paper(arx)
        print("not found on S2 or HF (check the id; if it is days old, try WebSearch)") if not (p and p.title) else show(p)


if __name__ == "__main__":
    main()
