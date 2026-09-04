#!/usr/bin/env python3
"""Fetch ALFWorld game.tw-pddl files from the HF dataset awawa-agi/alfworld-raw via the
datasets-server row API (the only HF file channel reachable from this node) and materialise
them under $ALFWORLD_DATA/json_2.1.1/{train,valid_seen,valid_unseen}/<task>/<trial>/game.tw-pddl.
Resumable: raw rows are cached per split in raw/<split>.jsonl."""
import json, os, sys, time, urllib.request, urllib.parse

DATASET = "awawa-agi/alfworld-raw"
ROOT = os.environ.get("ALFWORLD_DATA", "/home/work/neuro/alfworld-data")
SPLITS = {"train": "train", "eval_in_distribution": "valid_seen", "eval_out_of_distribution": "valid_unseen"}
PAGE = 50

HOST = "datasets-server.huggingface.co"
_PINNED = None

def reachable_ip():
    """DNS hands out several CloudFront IPs and this network blocks some of them (the same
    pattern as api.semanticscholar.org here): probe each with a 3 s TCP connect and pin the
    first that answers, so curl never waits on a black-holed address."""
    global _PINNED
    if _PINNED:
        return _PINNED
    import socket
    ips = sorted({ai[4][0] for ai in socket.getaddrinfo(HOST, 443, socket.AF_INET, socket.SOCK_STREAM)})
    for ip in ips:
        try:
            s = socket.create_connection((ip, 443), timeout=3); s.close()
            _PINNED = ip; print(f"  pinned {HOST} -> {ip} (of {ips})", flush=True)
            return ip
        except OSError:
            print(f"  {ip} unreachable", flush=True)
    raise SystemExit("no reachable IP for " + HOST)

def rows(split, offset, length):
    q = urllib.parse.urlencode({"dataset": DATASET, "config": "default", "split": split, "offset": offset, "length": length})
    url = f"https://{HOST}/rows?" + q
    # urllib hung indefinitely against this server (twice, after a few pages) while curl kept
    # answering in ~1 s, so pages are fetched with curl in a subprocess, pinned to a reachable IP.
    import subprocess, tempfile
    for attempt in range(6):
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json").name
        try:
            p = subprocess.run(["curl", "-sS", "-m", "300", "--compressed", "--resolve", f"{HOST}:443:{reachable_ip()}",
                                "-o", tmp, url], capture_output=True, text=True)
            if p.returncode == 0:
                with open(tmp) as f:
                    d = json.load(f)
                if "rows" in d:
                    return d
                print(f"  server said: {str(d)[:120]}", flush=True)
            else:
                print(f"  curl rc={p.returncode}: {p.stderr.strip()[:100]}", flush=True)
        except Exception as e:
            print(f"  retry {attempt+1} ({type(e).__name__}: {str(e)[:80]})", flush=True)
        finally:
            try: os.unlink(tmp)
            except OSError: pass
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
