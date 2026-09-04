#!/usr/bin/env python3
"""Fetch ALFWorld game.tw-pddl files from the HF dataset awawa-agi/alfworld-raw via the
datasets-server row API (the only HF file channel reachable from this node) and materialise
them under $ALFWORLD_DATA/json_2.1.1/{train,valid_seen,valid_unseen}/<task>/<trial>/game.tw-pddl.
Resumable: raw rows are cached per split in raw/<split>.jsonl."""
import json, os, sys, time, urllib.request, urllib.parse

DATASET = "awawa-agi/alfworld-raw"
ROOT = os.environ.get("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
SPLITS = {"train": "train", "eval_in_distribution": "valid_seen", "eval_out_of_distribution": "valid_unseen"}
PAGE = 100

def rows(split, offset, length):
    q = urllib.parse.urlencode({"dataset": DATASET, "config": "default", "split": split, "offset": offset, "length": length})
    url = "https://datasets-server.huggingface.co/rows?" + q
    for attempt in range(6):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.load(r)
        except Exception as e:
            print(f"  retry {attempt+1} ({type(e).__name__}: {str(e)[:80]})", flush=True)
            time.sleep(5 * (attempt + 1))
    raise SystemExit(f"giving up on {split}@{offset}")

os.makedirs(f"{ROOT}/raw", exist_ok=True)
for split, outdir in SPLITS.items():
    cache = f"{ROOT}/raw/{split}.jsonl"
    have = sum(1 for _ in open(cache)) if os.path.exists(cache) else 0
    first = rows(split, 0, 1)
    total = first["num_rows_total"]
    print(f"[{split}] total {total}, cached {have}", flush=True)
    with open(cache, "a") as f:
        off = have
        while off < total:
            d = rows(split, off, PAGE)
            for r in d["rows"]:
                f.write(json.dumps(r["row"], ensure_ascii=False) + "\n")
            off += len(d["rows"])
            f.flush()
            print(f"  {split}: {off}/{total}", flush=True)
            time.sleep(0.5)
    # materialise
    n = 0
    for line in open(cache):
        r = json.loads(line)
        path = os.path.join(ROOT, "json_2.1.1", outdir, r["game_file_path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, "w") as g:
                g.write(r["game_content"])
        n += 1
    print(f"[{split}] materialised {n} games under json_2.1.1/{outdir}", flush=True)
print("DONE", flush=True)
