# memory-substitution — standing rules for Claude Code sessions

## GPU use (PI rule, 2026-09-07): keep both A100s busy, never leave a bottleneck standing
- Before any GPU job: `nvidia-smi` (2× A100 80GB on this node; `gpu_burst` keep-alive holds ~1.2 GB and may stay on).
- Serving: one vLLM replica per GPU (ports 8000/8001, `--gpu-memory-utilization 0.90`), clients spread across both.
- Concurrency is tuned to the vLLM queue, not guessed: sample `Running:`/`Waiting:` in `runs/serve/vllm_agent_gpu*.log`
  and `nvidia-smi` utilization during the run; if a replica's running queue sits below ~8 or utilization below ~50 %,
  raise the episode workers (`run_sweep.py --workers`) until CPU (env stepping) or the queue saturates; watch `uptime` load.
- While one GPU is idle (e.g. a single-replica phase, or between phases) put the next arm or the LoRA job on it;
  do not serialize work that can overlap. Long jobs run under `nohup` with a pid file and resumable append-only JSONL,
  so they can be restarted with more workers without losing completed episodes (errored rows are re-run).
- Prefer restarting a runner with better concurrency over waiting; prefer prefix caching / no `--enforce-eager` when the
  workload is prefill-heavy and memory allows. Report throughput (episodes/min, tok/s per GPU) with every status update.

## Other standing rules
- Models: Fable 5.1 generates/scans/briefs, Opus judges and gates, Sonnet is prohibited (see memory `model-policy-no-sonnet`).
- Literature: `tools/ideate2/s2cli.py` (S2 + HF) first; WebSearch only for section text (200/session); never WebFetch.
- Keys live in chmod-600 files (`/home/work/.s2_env`); never print or commit them. Public data only; no NACC/patient data.
- Commit trailer: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` + `Claude-Session: <session url>`.
