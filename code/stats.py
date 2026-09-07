#!/usr/bin/env python3
"""Paired analysis of a k-sweep JSONL: per split and k>0 vs k=0 on identical (game, seed): fixed/broken counts, exact
McNemar p, net gain per 100, task-cluster bootstrap 80%/95% CI; plus timeout/invalid decomposition. Usage: stats.py <jsonl>"""
import sys, json, math, random
from collections import defaultdict
from itertools import groupby
rows = [json.loads(l) for l in open(sys.argv[1])]
rows = [r for r in rows if not r.get("error")]
by = defaultdict(dict)   # (split, game, seed) -> {k: row}
for r in rows: by[(r["split"], r["game_file"], r["seed"])][r["k"]] = r
splits = sorted({r["split"] for r in rows}); ks = sorted({r["k"] for r in rows})

def mcnemar_exact(b, c):
    n = b + c
    if n == 0: return 1.0
    k = min(b, c); p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * p)

def boot_ci(pairs, task_of, iters=2000, seed=0):
    tasks = defaultdict(list)
    for (t, d) in pairs: tasks[t].append(d)
    keys = list(tasks); rng = random.Random(seed); stats = []
    for _ in range(iters):
        sample = [d for t in rng.choices(keys, k=len(keys)) for d in tasks[t]]
        stats.append(100 * sum(sample) / len(sample))
    stats.sort(); q = lambda p: stats[int(p * (len(stats) - 1))]
    return q(0.10), q(0.90), q(0.025), q(0.975)

for s in splits:
    print(f"\n== split {s}")
    base = {key: v[0] for key, v in by.items() if key[0] == s and 0 in v}
    print(f"k=0: n={len(base)} success={sum(r['won'] for r in base.values())/max(1,len(base)):.3f} timeout={sum(r['timeout'] for r in base.values())/max(1,len(base)):.3f} "
          f"invalid/ep={sum(r['invalid'] for r in base.values())/max(1,len(base)):.2f}")
    for k in ks:
        if k == 0: continue
        pairs = [(key, v[0], v[k]) for key, v in by.items() if key[0] == s and 0 in v and k in v]
        if not pairs: continue
        fixed = sum(1 for _, a, b in pairs if (not a["won"]) and b["won"]); broken = sum(1 for _, a, b in pairs if a["won"] and (not b["won"]))
        net = [(key[1], int(b["won"]) - int(a["won"])) for key, a, b in pairs]
        lo80, hi80, lo95, hi95 = boot_ci([(json.loads(json.dumps(t)), d) for t, d in [(a_["task"], d) for (a_, d) in [(by[key][0], d) for (key, _, _), (t, d) in zip(pairs, net)]]], None)
        succ = sum(b["won"] for _, _, b in pairs) / len(pairs)
        print(f"k={k}: n={len(pairs)} success={succ:.3f} fixed={fixed} broken={broken} net/100={100*(fixed-broken)/len(pairs):+.1f} "
              f"[80% {lo80:+.1f},{hi80:+.1f}] [95% {lo95:+.1f},{hi95:+.1f}] McNemar p={mcnemar_exact(fixed, broken):.3f} "
              f"timeout={sum(b['timeout'] for _,_,b in pairs)/len(pairs):.3f} invalid/ep={sum(b['invalid'] for _,_,b in pairs)/len(pairs):.2f} "
              f"mem_tok~{sum(b['mem_tokens_est'] for _,_,b in pairs)/len(pairs):.0f}")
