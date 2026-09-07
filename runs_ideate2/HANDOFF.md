# HANDOFF — ideate2 next round: "same experience pool, in weights vs in context" (2026-09-07)

Read `tools/ideate2/README.md` and `tools/ideate2/DESIGN.md` §8–9 first. Model policy (PI): Fable 5.1 for Stage 0/1/2
subagents, Opus for gate and judges, **no Sonnet**. Literature: `tools/ideate2/s2cli.py` (S2 + HF) first; WebSearch only
for section text (200 calls per session) and never WebFetch. Env: `/home/work/neuro/alfworld-env/bin/python`,
`export S2_PIN_IP=18.244.60.91`. Commit with the attribution trailer in CLAUDE.md; never print keys.

## State at handoff
- Stage 0 collection for the new topic is done (network only): `runs_ideate2/parametric/` — `axes.json` (5 axes),
  `papers.jsonl` (79 papers: 67 ranked + 12 key papers force-added), `section_targets.json` (34 papers),
  `jobs_sections/section_<arxiv>.json` (34 WebSearch job specs). Nothing has been read at section level yet.
- Step 0 measurement (GPU) is running or finished: `runs/sweep/k_sweep.jsonl` (paired k-sweep, Qwen3-32B,
  expert bank), analysed by `code/stats.py`; LoRA feasibility via `code/lora_sft.py` (QLoRA, vllm-env). See `runs/STEP0_PROTOCOL.md`.
- Previous round (old brief) fully judged: `runs_ideate2/gen_v2/review/RANKING.md`; top 5.95. Its 24 ideas plus the 27
  archived ones are the "do not restate" set for the gate.

## Step A — section reads (needs a fresh WebSearch quota; ~17 subagent calls)
Launch one **Fable** subagent per pair below (`model: fable`, general-purpose). Prompt template:

> Read these two job files with the Read tool: <file1> and <file2>. Each has a "prompt" field describing one arXiv paper
> and the JSON record to produce. Carry out each prompt using WebSearch only (at most 4 searches per paper; arxiv.org/html/<id>
> and alphaxiv/HF pages often appear in results and their snippets carry section text). Quote verbatim where you can and mark
> paraphrase as such; write "not found" rather than inventing. Do not read any other local files. Return ONLY a JSON array
> containing the two result objects (each with "arxiv","limitations","conclusion","method","sources"); no prose, no code fences.

Record each subagent's task id in a mapping file `{"tasks": [<task id>, ...]}` and ingest:
```
/home/work/neuro/alfworld-env/bin/python tools/ideate2/ingest_sections.py runs_ideate2/parametric/papers.jsonl <mapping.json>
```
Pairs:
1. pair ['2602.04942', '2507.14805']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2602.04942.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2507.14805.json`
2. pair ['2604.27003', '2603.12056']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2604.27003.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2603.12056.json`
3. pair ['2601.03938', '2608.09228']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2601.03938.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2608.09228.json`
4. pair ['2604.15559', '2601.03641']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2604.15559.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2601.03641.json`
5. pair ['2606.22019', '2509.06100']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.22019.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2509.06100.json`
6. pair ['2606.11559', '2608.02508']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.11559.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2608.02508.json`
7. pair ['2603.09517', '2608.05219']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2603.09517.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2608.05219.json`
8. pair ['2606.00995', '2505.24842']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.00995.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2505.24842.json`
9. pair ['2606.04703', '2602.12275']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.04703.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2602.12275.json`
10. pair ['2603.18272', '2606.29502']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2603.18272.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.29502.json`
11. pair ['2607.29468', '2512.02543']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2607.29468.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2512.02543.json`
12. pair ['2607.21051', '2607.01480']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2607.21051.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2607.01480.json`
13. pair ['2606.02355', '2605.27762']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.02355.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2605.27762.json`
14. pair ['2607.28272', '2608.01735']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2607.28272.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2608.01735.json`
15. pair ['2606.30626', '2605.09315']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2606.30626.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2605.09315.json`
16. pair ['2601.03192', '2512.10696']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2601.03192.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2512.10696.json`
17. pair ['2607.10608', '2608.12218']: `/home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2607.10608.json and /home/work/neuro/memory-substitution/runs_ideate2/parametric/jobs_sections/section_2608.12218.json`
## Step B — cards, gaps, digest (Fable subagents; no web needed)
```
P=/home/work/neuro/alfworld-env/bin/python; W=runs_ideate2/parametric
$P tools/ideate2/prescan.py cards --slug parametric --out $W --axes $W/axes.json --batch 10 --model fable   # → jobs/prescan_card__batchNN
#   launch one Fable subagent per card job (read the .prompt.md, return ONLY the JSON array), record ids in {"batchNN": id}
$P tools/ideate2/cards_collect.py $W <card_map.json> $W/axes.json                                          # → cards.jsonl
$P tools/ideate2/prescan.py synth --slug parametric --out $W --model fable                                # → jobs/prescan_synth__<axis>
#   one Fable subagent per axis job, record ids in {"<axis name>": id}
$P tools/ideate2/synth_collect.py $W <synth_map.json>                                                     # → gaps.json
$P tools/ideate2/prescan.py digest --slug parametric --out $W --brief runs_ideate2/parametric/brief_v3.md  # after Step C
```

## Step C — brief (Fable, in-session, not a subagent)
Write `runs_ideate2/parametric/brief_v3.md` in the shape of `runs_ideate2/agent_memory_v2/brief_v2.md`: starting facts
from `runs/sweep` (k where retrieval helps/harms on Qwen3-32B, CIs) and `runs/lora/*/train_log.json` (LoRA cost, memory);
node constraints from `runs/STEP0_PROTOCOL.md` (2 GPUs, no 7–8B model, Qwen3-32B as agent and LoRA target); brief-level
rules that the 28 reviews of the previous round demanded (DESIGN.md §9: rate-/token-matched placebo arms for any
injection-reducing intervention, power gates on ratio predictions, positive control for dispositional transfer, no
predictions entailed by definitions); 5–6 open questions along the axes; appendix = the 51 archived ideas with Opus scores
(`reviews/ideation/RANKING.json`, `runs_ideate2/gen_v2/review/RANKING.json`), plus the three parametric-axis ideas'
strongest objections (`runs_ideate2/gen_v2/review/{harm_does_not_distill,memory_in_the_loop_training_decomposition,opposite_sided_failure_under_shift}/r1.json`).

## Step D — generation → gate → novelty → review
```
$P tools/ideate2/axes.py emit --axes $W/axes.json --brief $W/brief_v3.md --cards $W/cards.jsonl --gaps $W/gaps.json --n 3 --out runs_ideate2/gen_v3 --model fable
#   5 Fable generators (Bash for s2cli + WebSearch if quota remains); collect with tools/ideate2/gen_collect.py; axes.py merge
$P tools/ideate2/gate.py --ideas runs_ideate2/gen_v3/ideas.json --brief $W/brief_v3.md --cards $W/cards.jsonl --archive <51 archived ideas json> --out runs_ideate2/gen_v3/gate --backend harness --model opus
#   Opus adjudication subagents per batch; gate_collect.py
$P tools/ideate2/novelty_check.py --ideas runs_ideate2/gen_v3/ideas.json --out runs_ideate2/gen_v3/novelty --s2-queries 2
$P tools/ideate2/review_batch.py emit --ideas runs_ideate2/gen_v3/ideas.json --brief $W/brief_v3.md --novelty runs_ideate2/gen_v3/novelty --out runs_ideate2/gen_v3/review --model opus
#   one Opus judge per idea (Bash for s2cli); review_batch.py collect / rank; escalate the top 2–3 with --round 2 --n 2
```
Then proposal v7 (Fable) → 1 Opus judge → +2 if promising; freeze on "no design-blocking finding".
