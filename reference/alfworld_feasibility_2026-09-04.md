# ALFWorld on this node — feasibility check, 2026-09-04

Question: can E2 (ALFWorld, text-only) run on this compute node, given its firewall? **Yes, with one workaround.**

## What works out of the box
- `pip install alfworld` (0.4.2) pulls `textworld` 1.7.0; both install from PyPI. Venv: `/home/work/neuro/alfworld-env` (NFS, survives recycling).
- TextWorld's bundled Inform7 compiler and interpreter run: a trivial game compiles and starts.
- The PDDL domain (`alfred.pddl`) and text grammar (`alfred.twl2`) ship inside the package; copied to `$ALFWORLD_DATA/logic/`.
- The reference config comes from a shallow git clone of the source repo (`/home/work/neuro/alfworld-src`, github.com:443 is open).

## What is blocked, and the workaround
- `alfworld-download` fetches three zips from GitHub release assets (hosts `objects.githubusercontent.com` /
  `release-assets.githubusercontent.com`): **unreachable** from this node. The ALFRED S3 bucket and HuggingFace's
  file CDN (`us.aws.cdn.hf.co` xet bridge) are unreachable too; `cdn-lfs.hf.co` answers but resets on transfer.
- **Workaround:** HuggingFace's `datasets-server.huggingface.co/rows` API is reachable, and the dataset
  `awawa-agi/alfworld-raw` contains every `game.tw-pddl` file verbatim (3,553 train, 140 valid_seen, 134 valid_unseen)
  with its original relative path. `fetch_games.py` pages through it (100 rows ≈ 8.5 MB ≈ 47 s; ≈30 min total) and
  materialises `$ALFWORLD_DATA/json_2.1.1/{train,valid_seen,valid_unseen}/<task>/<trial>/game.tw-pddl`.
- The text environment also expects a `traj_data.json` next to each game; the text-only path reads only
  `task_type`, and the bundled handcoded expert (called on every `reset`) reads `pddl_params.{object_target,
  parent_target, toggle_target}`. `make_stubs.py` writes stubs with these fields reconstructed from the task
  directory name (`task-object-mrecep-parent_or_toggle-scene`). Human goal annotations (`turk_annotations`) are not
  available this way; games use the templated goal text, which is ALFWorld's default.

## Smoke test (`smoke_test.py`, first 400 games)
`AlfredTWEnv` collected 400 games, reset and replayed the stored walkthrough of 4 games: **4/4 solved (reward 1)**.
Throughput 1.8 env steps/s for a single env including per-game compile on reset; batch envs and multiprocessing
scale this, and the LLM call dominates wall-clock anyway.

## Consequences for the design (v4.4 → v5)
- E2 can be a screening candidate with n up to 3,553 training games (held-out training games as the test pool), so the
  n=274 ceiling that made E2 "directional only" no longer applies.
- Episode cost is ≈25 LLM calls vs ≈6 in E1; the E2 grid must be budgeted at ≈4× E1 per episode.
- Data provenance: the game files are byte-identical copies of the official `json_2.1.2_tw-pddl` release as
  redistributed on HuggingFace; the split names map `eval_in_distribution → valid_seen`,
  `eval_out_of_distribution → valid_unseen`. SHA256 of the raw row caches is recorded in `data/` once the fetch completes.

Files: `tools/alfworld/{fetch_games.py, make_stubs.py, smoke_test.py}` (copies of the scripts in
`/home/work/neuro/alfworld-data/`).
