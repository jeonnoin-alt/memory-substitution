# Title: Who Wrote the Experience, Who Reads It: Transfer of Agent Memory Across Backbones, Agents and Populations

Author: Fable 5.1, 2026-09-09. Stage-1 brief for the ideate2 pipeline, after the Stage-0 pre-scan on this topic (5 axes,
62 papers carded from S2 + HF, 25 gaps; `digest.md`; no section reads) and after Step 0 on this node (`runs/STEP0_RESULTS.md`).
Third topic of the program; the two earlier topics (memory vs prompt optimization; weights vs context) and their 51 archived
ideas are the prior this brief must move past.

## Keywords
LLM agents, experience memory, cross-model transfer, producer-consumer mismatch, shared memory, skill libraries, negative
transfer, memory contamination, provenance, matched-cost evaluation, ALFWorld

## TL;DR
Every agent-memory result the program has measured so far was written and read by the same policy or by an expert
planner. The 2026 literature now transfers experience across models routinely: teacher trajectories distilled into memories
for 4B–8B students (2608.07169), cross-domain memory pools moved between models (2604.14004), skill libraries reused by other
agents (2607.26643, 2606.01139), population stores written by many agents (2606.19911, 2603.14312), and portable memory
formats (2605.11032). The scan finds one hole under all five axes: nobody reports what fraction of the writer's own gain
the reader keeps, nobody compares foreign experience against a pool the reader collects for itself at the same cost, and
nobody tests whether the reader can tell a helpful foreign item from a contaminated one. Skill utility is already known to
be strongly model-dependent (2605.30723, 2605.23899), so the question is not whether transfer exists but what governs it.
This track asks for the sharp claim about who can read whose experience, and at what cost.

## Starting position (measured here; not to be rediscovered)
- **Two writers for one task set exist on disk.** Expert walkthroughs (1,465 train tasks, off-policy planner text) and
  Qwen3-32B's own k=0 successes (3,553 train games → 1,892 won, 0.533; on-policy, success-filtered, type-skewed: pick-and-place
  0.81, look-at-in-light 0.76, pick-two 0.51, cool 0.41, clean 0.40, heat 0.26). Collection cost of the self pool: about 3
  GPU-hours on two A100s; the expert pool cost nothing.
- **Measurement A (expert writer → Qwen3-32B reader):** k=0 0.536/0.549 → k=3 0.807/0.869 (valid_seen/valid_unseen), net
  +27.1 [+18.6, +35.6] / +32.1 [+22.9, +41.0]; k=7 no harm; gain carried by clean/heat/cool procedures (+39 to +55); unseen ≈
  seen (procedure-bound). Injected tokens ~140/430/1,010 at k=1/3/7. Look-at-in-light is the one negative type (−4.8).
- **Not yet measured, and what this brief exists to enable:** the self pool as bank (writer = reader); a second and third
  backbone as reader and as writer; the writer × reader matrix. Candidate readers/writers on this node: Qwen3-32B (verified
  in vLLM 0.13), EXAONE-4.0-32B and gpt-oss-120b (present on disk, serving to be verified before any confirmatory run),
  medgemma-27b (out of scope: medical). No 7–8B instruct model is available (weight downloads blocked).
- **Measurement B:** QLoRA rank 32 on Qwen3-32B, one epoch of the expert pool ≈ 2 GPU-hours; relevant if a proposal wants
  the parametric route as an arm, not required.
- **Measurement C (running, results appended before generation if finished):** static per-type procedure prompts (fixed
  exemplars 1/3, one-sentence procedures, all six procedures) paired against k=1/3 retrieval on the same games. It is the
  cheap baseline four judges asked for in the previous round: a reader that already knows the procedure gains nothing from
  any writer, so every transfer claim must show its gain survives this baseline.
- **Carried over:** noise floor of a paired 274-game × 2-seed cell ≈ ±8 net points; the 51 archived ideas (appendix), three of
  which sit on this topic.

## What the Stage-0 scan says, by axis (gap ids as in `digest.md`)
1. **Producer–consumer mismatch** (20 cards). Teacher→student memory without training gives +27 pp on AppWorld for 4B–8B
   students with a GPT-5-mini teacher, "teacher effectiveness depends on both teacher capability and student compatibility"
   (2608.07169); memory moves between models with abstraction level deciding transfer (2604.14004); skill utility is
   model-dependent and a model-conditioned rewriter fixes it (2605.30723); extractor and consumer roles are non-uniform and
   independent of scale (2605.23899); SkillRevise skills transfer across five LLMs (2606.01139); frozen memory tables need a
   target-side reader (2608.17050). Gaps G1–G5: retained-gain ratio unmeasured; no matched-cost self-pool control; capability
   gap and family mismatch unswept; error propagation unmeasured; interface mismatch untested.
2. **What transfers and what contaminates** (29 cards). Raw trajectories often beat distilled skills (2605.24117) while a
   survey claims transferability rises with compression (2604.15877); loaded skills cause 307 documented failures, mostly
   from seemingly relevant skills (2608.11888); grafted experience poisons stores (2512.16962), trust laundering across
   sessions (2605.22842), collective false memories (2602.00428). Gaps G6–G10: same-backbone evaluation everywhere; no
   read-time detection of harmful foreign entries; provenance defenses costed only on adversarial workloads; the
   compression–transfer claim untested at matched cost.
3. **Shared and population memory** (24 cards). Transactive memory across producers and consumers (2606.19911), learned
   admission to a global bank (2602.05965), conflict-preserving replicated memory (2607.05844), provenance as control signal
   (2608.10509), 300-skill scientific populations (2603.14312), memory sharing across agents (2404.09982). Gaps G11–G15:
   trust weighting by writer capability untested; value and contamination vs number and diversity of writers unmeasured;
   benign-looking poisoned experience records untested; governance overhead not in the same units as gains.
4. **Adapting foreign experience to the reader** (19 cards). Reconstruction before acting (MemHarness 2607.28272), analogical
   adaptation (Echo 2604.05533), abstraction with human feedback (2406.14596), context-augmentation models (CLEAR
   2604.07487), latent memory composers (2602.03036), KV-cache transfer across Qwen3 sizes (2606.13594), skill patches from
   student–teacher contrast (SKILL-KD 2607.28048). Gaps G16–G20: adaptation validated only on self-written experience;
   learned transfer components not tested on held-out backbones; retained-benefit ratio across capability gaps unmeasured;
   adaptation may propagate contamination; adaptation cost never matched against plain retrieval or self-collection.
5. **Evaluation and cost of transfer** (17 cards). PAST-Bench toggles retained experience (2608.04003); S3Gym compares
   history ICL, summaries and training (2608.31100); memory-system profiling attributes cost to phases (2606.24775,
   2606.06448); in-context distillation amortization (2512.02543). Gaps G21–G25: no self-collected control at matched cost;
   consumer-side tokens not reported with gains; single-writer single-reader benchmarks; no reader-side filter evaluated;
   parametric memory portability asserted.

## Rules for every proposal in this round (binding; the entailment check and the judges enforce them)
- **Writer identity is manipulated, not observed.** The same task set, the same bank construction and the same retriever,
  with only the writer swapped (expert / self / other backbone / mixed); and the same store read by several readers.
- **Self-pool control at matched collection cost.** Any foreign-experience arm is compared with a pool the reader collected
  itself at the same episode or token budget; "foreign memory helps" without this arm is the gain of having any memory.
- **Retained-gain ratio is the estimand,** reported per writer × reader cell with seeds: reader's gain from the writer's pool
  divided by the writer's own gain from the same pool (or divided by the reader's self-pool gain), with CIs.
- **Static-procedure baseline (Measurement C) in every design.** A reader that gains nothing from any writer beyond a fixed
  procedure prompt has nothing to transfer; report every transfer gain net of it.
- **Contamination arms are manufactured, gated and positively controlled.** Planted wrong items at controlled rates, by
  writer identity; Gate 0 requires the harm to be ≥ 6 net points at some rate; a read-time detector is scored by precision
  and recall, not by the downstream success change alone.
- **Capability and proximity are separated.** The archived idea closer_beats_stronger (5.75) claimed policy proximity, not
  capability, predicts transfer; a new proposal must vary proximity at fixed capability (same backbone, different scaffold,
  temperature or training) and capability at fixed proximity, or it is a restatement.
- **Every trained or adapted component is evaluated memory-absent, matched and mismatched**; an adaptation step is compared
  with direct injection of the unmodified item at matched tokens.
- **Per prediction: the falsifying outcome and the arm that can produce it.** A prediction whose falsifier no arm can
  produce (a split that never gives the reader the information; an append-only store; a warm start; an identity between
  estimands; a falsifier inside the stated CI) is sent back before review.
- **One literature search in the home vocabulary** of the mechanism (knowledge distillation, transfer learning negative
  transfer, data poisoning, imitation from suboptimal demonstrations, ensemble diversity), no agent/memory/benchmark words.
- **Power and budget:** paired cells, ±8 net at 274 × 2 seeds; margins as fractions of the Gate-0 effect; cell-by-cell episode
  counts; both A100s busy (one serves a reader while the other serves a writer or trains); days, not weeks.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 The writer × reader matrix and its self-pool control (G1, G2, G7, G21, G23).** Three writers (expert, Qwen3-32B self,
  a second backbone's self pool) × two or three readers, one retriever, k=3 and k=1; retained-gain ratio per cell against
  the reader's own pool at matched collection cost and against the static-procedure prompt. The sharp claim is a
  prediction about which cells are above 1 (a foreign writer beats the reader's own pool) and why.
- **Q2 Direction and size of the capability gap (G3, G18).** Strong→weak vs weak→strong at matched pool cost; does a weaker
  reader keep a larger fraction of a stronger writer's gain than the reverse, and is the ordering by capability or by
  proximity (archived closer_beats_stronger must be surpassed by manipulating both).
- **Q3 What contaminates, and can the reader tell (G4, G8, G13, G19, G24).** Writer errors (self pool failures relabelled
  as successes, wrong-procedure grafts, benign-looking poisoned records) at controlled rates, by writer identity; the
  reader's read-time detection precision and recall; whether adaptation (reconstruction, rewriting) propagates or filters.
- **Q4 Abstraction level × writer (G10, G22).** Raw trajectories vs summaries vs procedures, at matched tokens, for
  same-writer and foreign-writer readers; the compression-raises-transferability claim (2604.15877) against
  raw-beats-skills (2605.24117) with the reader identity as the manipulated variable.
- **Q5 The adaptation step (G16, G17, G20).** Does reader-side reconstruction or rewriting help only when writer ≠ reader,
  and does a rewriter learned against one reader transfer to another; cost against plain retrieval and self-collection.
- **Q6 Population scaling and governance cost (G11, G12, G14, G15).** Number and diversity of writers (1, 2, 4, 8 policies:
  backbones × scaffolds × temperatures) into one store; reader gain, conflict rate and contamination as curves; provenance
  or trust-weighting gates costed on non-adversarial content.

## In scope
- ALFWorld primary (two pools on disk, 274 validation games, procedure-typed tasks); WebShop or a text-game second domain
  only if the claim needs it. Public data only.
- Readers and writers: Qwen3-32B verified; EXAONE-4.0-32B and gpt-oss-120b to be verified in vLLM before use; scaffold and
  temperature variants of one backbone count as distinct writers for proximity manipulations.
- Reimplementation of one published transfer method per family as a named baseline (Agent Memory Distillation 2608.07169;
  MemHarness-style reconstruction 2607.28272; a model-conditioned skill rewriter 2605.30723).

## Out of scope
- Frontier-model teachers (no API at experiment time); clinical or private data.
- Security framing beyond manufactured contamination (no attacks on external systems).
- Restating the archived ideas (appendix); a proposal near one must name it and state what it fixes.

## Resource constraints
Two A100 80GB; one vLLM replica per GPU; a second backbone occupies one GPU while it serves, so writer-pool collection for
a second backbone (~3,553 games, ~3 GPU-hours at ~20 episodes/min) and reader evaluation (274 × 2 seeds ≈ 550 episodes per
cell, ~30 min per cell per replica) must be scheduled so both GPUs stay busy. A full Q1 matrix (3 writers × 3 readers × 2 k
× self-pool controls) is roughly 25 cells ≈ 14,000 episodes plus one pool collection per new backbone: about two days.
Pre-registration of gates, margins and amendments before the first confirmatory cell.

## Appendix A: archived ideas nearest this topic (do not restate; the gate compares against all 51)
- closer_beats_stronger (5.75, round 2): consumer-side policy proximity, not builder capability, predicts whether shared
  agent experience transfers across backbones. Judges: proximity and capability were not separated; no self-pool control.
- contributor_conflict_not_size (4.85): cross-contributor conflict, not library size, degrades shared skill libraries;
  activation-time reconciliation. Judges: conflict rate was a property of the construction.
- lineage_blast_radius (4.75): consolidation launders low-trust experience into shared memory; provenance enforcement pays
  for it in fan-in. Judges: entailed by the consolidation rule.
- Also adjacent: memory_in_the_loop_training_decomposition (5.65), abstraction_discards_bindings_and_repairs (5.95,
  abstraction level within one writer), order_randomized_leakage_audit (5.7, near-duplicate leakage), the three
  weights-vs-context ideas of round 3 (memory_carried_traits_need_tokens 6.10, success_filter_lockin 5.85,
  context_wins_substrate_conflict 5.55).

## Appendix B: what the previous rounds' judges demanded (binding)
Same pool / same backbone / one cost axis; partition bank and targets; self-distillation or self-pool controls; memory-free,
matched and mismatched evaluation; token- and rate-matched placebos; margins tied to the measured effect; positive controls
before any "does not transfer" claim; no prediction entailed by a definition; the cheapest baseline (a sentence, a static
prompt) run first; searches in the mechanism's home literature.
