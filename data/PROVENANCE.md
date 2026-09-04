# Data provenance
Source: ALFWorld (Shridhar et al., ICLR 2021) text games, `json_2.1.1` split, reconstructed from the public Hugging Face
dataset `awawa-agi/alfworld-raw` via `datasets-server.huggingface.co/rows` (the only reachable channel; GitHub release
assets and the HF file CDN are blocked here). Fetch script: `tools/alfworld/fetch_games.py`; stubs: `make_stubs.py`.
Location: `/home/work/neuro/alfworld-data/json_2.1.1/{train,valid_seen,valid_unseen}/<task>/<trial>/{game.tw-pddl,traj_data.json}`
Integrity: `/home/work/neuro/alfworld-data/raw/SHA256SUMS` (train d3093a70…, valid_seen adf77999…, valid_unseen 900d5c3b…).
Counts: train 3,553 trials / 1,465 tasks; valid_seen 140 / 136; valid_unseen 134 / 46. Logic: `alfworld-data/logic/`.
Public benchmark data only. No NACC/patient data may ever enter this directory (lab DUA).
