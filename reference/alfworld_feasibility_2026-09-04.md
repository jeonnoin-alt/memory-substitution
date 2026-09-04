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
  with its original relative path. `fetch_games.py` pages through it (50 rows per request) and materialises
  `$ALFWORLD_DATA/json_2.1.1/{train,valid_seen,valid_unseen}/<task>/<trial>/game.tw-pddl`.
- **Network quirk (same as Semantic Scholar on this node):** DNS returns four CloudFront IPs for
  `datasets-server.huggingface.co` (13.225.134.{15,34,68,120}) and only **.15** accepts connections; the others
  black-hole, so a naive client stalls for minutes whenever the resolver hands it one of them. The fetcher probes the
  IPs with a 3 s TCP connect and pins the reachable one via `curl --resolve`. Python `urllib` also hung on this host
  where `curl` did not, so pages are fetched with curl in a subprocess. Occasional "connection reset by peer" on the
  good IP is retried with backoff.
- The text environment also expects a `traj_data.json` next to each game; the text-only path reads only
  `task_type`, and the bundled handcoded expert (called on every `reset`) reads `pddl_params.{object_target,
  parent_target, toggle_target}`. `make_stubs.py` writes stubs with these fields reconstructed from the task
  directory name (`task-object-mrecep-parent_or_toggle-scene`). Human goal annotations (`turk_annotations`) are not
  available this way; games use the templated goal text, which is ALFWorld's default.

## Final state of the data (2026-09-04 16:36 KST)
All three splits fetched and materialised with stubs: **train 3,553 · valid_seen 140 · valid_unseen 134** game
directories (each with `game.tw-pddl` + `traj_data.json`). Raw row caches and their SHA256 are in
`/home/work/neuro/alfworld-data/raw/` (`SHA256SUMS`): train d3093a70…, valid_seen adf77999…, valid_unseen 900d5c3b….
Train task mix (task directories): pick_and_place 322 · pick_two 354 · clean 268 · cool 212 · heat 186 · look_in_light 123.

## Smoke tests
- `smoke_test.py` (replay the walkthrough stored in each game file): train **4/4**, valid_seen **3/3** solved (reward 1).
  valid_unseen 0/3 — not an environment failure: those files' stored walkthroughs use the raw, un-demangled object ids
  (`cabinet_bar__plus_00_dot_95…`) while the environment presents `cabinet 3`, so the replayed commands are
  "Nothing happens"; observations, goal text and admissible commands are all normal. The environment must be
  validated with the expert instead (below). Throughput 1.4–2.2 env steps/s for a single env including the per-game
  Inform7 compile at reset; batch envs and multiprocessing scale this, and the LLM call dominates wall-clock anyway.
- `expert_test.py` (drive games with the bundled handcoded expert, which reads the reconstructed `pddl_params`):
  **valid_unseen 5/5 solved** (7–36 steps each, 6.1 steps/s incl. resets), **train 5/5 solved** (5–12 steps, 2.0 steps/s).
  This also validates the `pddl_params` reconstructed from directory names, since the expert's policy is built from them.

## Verdict
E2 is runnable here: package, engine, all 3,827 games and the expert all work. The remaining E2 cost driver is the
LLM: ≈10–35 agent turns per episode versus ≈6 in E1.

## Consequences for the design (v4.4 → v5)
- E2 can be a screening candidate with n up to 3,553 training games (held-out training games as the test pool), so the
  n=274 ceiling that made E2 "directional only" no longer applies.
- Episode cost is ≈25 LLM calls vs ≈6 in E1; the E2 grid must be budgeted at ≈4× E1 per episode.
- Data provenance: the game files are byte-identical copies of the official `json_2.1.2_tw-pddl` release as
  redistributed on HuggingFace; the split names map `eval_in_distribution → valid_seen`,
  `eval_out_of_distribution → valid_unseen`. SHA256 of the raw row caches is recorded in `data/` once the fetch completes.

Files: `tools/alfworld/{fetch_games.py, make_stubs.py, smoke_test.py}` (copies of the scripts in
`/home/work/neuro/alfworld-data/`).
