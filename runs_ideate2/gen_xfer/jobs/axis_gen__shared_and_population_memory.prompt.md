=== SYSTEM ===
You are an experienced researcher proposing work that could be published at a top-tier venue. You are assigned ONE
axis of the research area below; propose ideas that take a position on that axis. You will not see ideas from other
axes; do not try to cover the whole area.

Bar to clear: contribution stateable in one sentence; positioning that names the closest prior work and what it does
not do; a central claim with an experiment that could come out against it; a measurement plan that separates an
effect from run-to-run noise; feasibility on small open models and single-node compute.

Use the literature digest you were given. Two fields are mandatory in your IDEA JSON in addition to the standard
ones: "Addresses gap": the digest gap ID this idea attacks, or "none" with one sentence on why the digest missed it;
"Not a restatement of": the nearest prior-result bullet in the brief and the nearest digest card, each with one
sentence on what this idea claims that they do not. If you cannot write those sentences, the idea is a restatement
and you must change it.

Before finalizing you must run at least two literature searches: one on the mechanism you are claiming, restricted
to the last twelve months, and one on the closest named method. Report what came back in "Preprint Collision Check",
including empty results, the query strings and the channel that answered. Do not write experiment code.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.

Two further requirements, both checked mechanically before review:
- Falsifiable Predictions: for every prediction write the outcome that would falsify it AND the arm or cell that can
  produce that outcome. If no arm can produce it (the split never gives the model that information; an append-only
  store cannot forget; a warm-started adapter always relearns faster than a cold one; the estimand is an identity of
  another quantity you compare it to; the falsifier lies inside your stated confidence interval), the prediction is
  entailed by the design and must be removed or the design changed. A proposal whose headline prediction is entailed
  is sent back before any judge sees it.
- One of your literature searches must be phrased in the home vocabulary of the mechanism, with no agent, memory,
  retrieval, experience or benchmark words (e.g. "data poisoning number of poison samples threshold" rather than
  "stale items in the agent's memory bank"); label it `home:` in the Preprint Collision Check. Papers that pre-empt
  a claim are usually found there, not under the agent-memory phrasing.

Standard IDEA JSON fields: Name, Title, Short Hypothesis, Related Work, Abstract, Experiments, Baselines and Ablations,
Falsifiable Predictions, Measurement and Noise Control, Preprint Collision Check, Risk Factors and Limitations.

=== USER ===
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


## Your axis
shared and population memory: one store written by many agents or contributors: conflicts among contributions, provenance and trust, deduplication, consolidation across writers, and how the store's value changes with the number and diversity of writers

## Digest gaps on your axis (cite by ID)
- G11: It is unresolved whether contributions from writers of differing capability should be trusted or weighted differently, and whether a weaker consumer actually gains from a stronger producer's memory, because nearly every shared store is evaluated with copies of the same model or a single backbone. (cards arxiv:2607.05844, arxiv:2606.19911, arxiv:2606.25115, arxiv:2605.20563, arxiv:2605.18401, arxiv:2602.00428, arxiv:2605.22842, arxiv:2606.24775, arxiv:2605.06130, arxiv:2605.11032)
- G12: How the value and the contamination of a shared store change with the number and diversity of contributing agents is untested, since multi-writer deployments are reported as designs or with few writers and no scaling curves. (cards arxiv:2603.14312, arxiv:2607.05844, arxiv:2505.18279, arxiv:2404.09982, arxiv:2605.20563, arxiv:2607.24759, arxiv:2601.07004)
- G13: Whether provenance, trust-gating, and information-flow defenses hold when the poisoned entry is a benign-looking successful-experience record rather than a policy-formatted document or synthetic adversarial task, and what those gates cost on legitimate non-adversarial reuse, is unmeasured. (cards arxiv:2512.16962, arxiv:2605.22842, arxiv:2608.10509, arxiv:2608.11436, arxiv:2602.05965, arxiv:2605.18401, arxiv:2602.03036, arxiv:2605.11032, arxiv:2602.00428)
- G14: Reported gains from shared or governed memory are never compared against a self-collected or unbudgeted memory pool at matched cost, and the overhead of the governance machinery (curation, policy checks, TEE-protected retrieval, controller training, atomization) is not reported in the same units as the gains. (cards arxiv:2606.25115, arxiv:2606.19911, arxiv:2608.10509, arxiv:2601.07004, arxiv:2505.18279, arxiv:2602.05965, arxiv:2605.18401, arxiv:2605.25869, arxiv:2602.03036)
- G15: It is unknown whether surfacing conflicts, negative results, and recorded dead ends changes reader behavior (fewer repeated failures, correct abstention) beyond making them visible, since conflict-preserving stores tie on accuracy, the wiki substrate's failure-avoidance is untested, and the curation loop is shown in one domain with a single writer. (cards arxiv:2607.24759, arxiv:2607.05844, arxiv:2606.17591, arxiv:2603.14312)

## Digest cards for your axis and the cross-axis papers
- arxiv:2608.10509 (2026-08-11): Provenance can serve as an operational control signal in shared multi-agent memory, so that permission-ineligible, untrusted, or revoked sources are excluded and risky actions are gated before execution rather than only audited afterward. | limitations: Results support provenance as an operational control signal 'within the evaluated setting'; otherwise not stated. | not tested: Evaluation is on synthetic tasks only, with no real multi-agent workflows or naturally arising conflicts between writers; no measurement of whether trust-weighted reranking changes downstream task performance relative to a plain semantic retriever on non-adversarial content, and no report of collection or inference cost.
- arxiv:2606.25115 (2026-06-23): Governing an on-device agent's experience memory by a single net-value-per-byte score (value minus harm, per byte) reduces footprint, energy, uplink, and injection success together without reducing accuracy, so forgetting by net value improves the agent. | limitations: 'In this setting, forgetting by net value improves the agent rather than weakening it'; otherwise not stated. | not tested: How the value and harm terms are estimated and whether they hold beyond the small testbed; whether provenance-gated peer entries from a more capable or differently configured node still transfer useful content or are simply blocked; no comparison against a matched-cost unbudgeted memory.
- arxiv:2605.11032 (2026-05-10): Persistent agent memory can be made portable across vendor-specific runtimes through a structured, tamper-evident, access-controlled protocol with an injection-resistant rehydration step that adapts recalled content to heterogeneous target models. | limitations: not stated | not tested: No measurement of whether transferred memory improves the receiving model's task performance or how much of the source agent's benefit the target keeps; the rehydration adaptation is described but not evaluated against a no-adaptation baseline; injection resistance is asserted without reported attack-success numbers.
- arxiv:2603.14312 (2026-03-15): Independent autonomous scientific agents deployed by many contributors can coordinate without a central planner by exchanging immutable, lineage-tracked artifacts and broadcasting unsatisfied information needs to a shared index, yielding heterogeneous tool chaining, emergent convergence, and traceable reasoning. | limitations: not stated | not tested: No controlled comparison against a single agent or a centrally planned system, no measure of how output quality changes with the number or diversity of contributing agents, and no evaluation of how the mutation layer's conflict resolution affects correctness.
- arxiv:2602.05965 (2026-02-05): A learned controller that selectively admits intermediate agent steps into a global memory bank lets parallel agent teams reuse each other's computation, cutting runtime while matching or improving task performance. | limitations: not stated | not tested: Teams appear to share the same underlying model and run on the same task, so cross-model or cross-task reuse is not examined; no analysis of whether admitted entries from a wrong-track team harm others, and the controller's training cost is not reported against the runtime savings.
- arxiv:2606.19911 (2026-06-18): Population-level storage and retrieval of agent-generated trajectories lets consumer agents improve task performance and reduce interaction steps without coordination or joint training, positioning transactive memory as a design pattern for open agent ecosystems. | limitations: not stated | not tested: The abstract does not say how heterogeneous the producers and consumers actually were or whether a weaker consumer gains from a stronger producer's trajectories; no treatment of conflicting or erroneous contributions in the repository, and no comparison against a self-collected pool of matched cost.
- arxiv:2607.24759 (2026-05-29): An append-only, LLM-maintained interlinked wiki template can serve as a shared substrate for heterogeneous collaborative knowledge work across multiple humans, multiple AI agents and multiple domains, preserving negative results that publications and shared code structurally lose. | limitations: not stated | not tested: The multi-agent (multi-writer) deployment is reported as a design rather than evaluated; no quantitative comparison against RAG or no-wiki baselines, and no test of whether agents reading the wiki actually avoid repeating recorded failures.
- arxiv:2601.07004 (2026-01-11): A hardware-backed zero-trust architecture applying TEE protection to each of five functional layers of an AI memory system can deliver local-equivalent security while enabling cross-agent collaboration and cross-application sharing. | limitations: not stated | not tested: No measured performance or latency overhead of TEE-protected retrieval, and no empirical evaluation of the porting cost or of collaboration quality under the architecture.
- arxiv:2607.05844 (2026-07-07): A conflict-preserving replicated memory contract keeps contradictions from multiple agent branches, retries and replicas visible and auditable, enabling safer abstention and correction than memory layers that collapse disagreement behind overwrite rules, without claiming a universal accuracy gain. | limitations: The resulting claim is narrow: StateFuse is best supported as a safer public memory contract for contradiction surfacing, abstention, and auditable correction, not as a universal accuracy gain. | not tested: How the store behaves as the number and diversity of writing agents grows; whether contributions from writers of differing capability should be trusted differently rather than merged uniformly.
- arxiv:2608.11436 (2026-08-11): A honeytoken cannot be simultaneously harmless to trusted agents and unrecognisable to an attacker who shares the trusted agents' information and can implement their policy, and shared agent memory adds a second leakage channel by pooling weak fingerprints, so token identity must be kept in a private reference monitor with a provenance-enforcing broker. | limitations: not stated | not tested: No empirical evaluation of the proposed reference-monitor/broker architecture against agent coalitions is described; the rate at which pooled fingerprints in shared memory actually drive detection error to zero in practice, or how quickly containment interrupts learning, is not measured.
- arxiv:2606.17591 (2026-06-16): In non-stationary environments, training-free verbal reinforcement learning agents need insight governance (outcome-driven evaluation, persistent structured evidence, a non-monotonic knowledge lifecycle, and compositional governance) in addition to experience extraction, and the same accumulated experience either degrades or dramatically improves performance depending on whether a curation loop is present. | limitations: not stated | not tested: Only a single domain (financial forecasting) is used, so generality to other agentic or interactive environments is not shown; whether the governed rule store transfers across different agent backbones or across multiple writers is not examined.
- arxiv:2602.03036 (2026-02-03): Multi-agent memory suffers from role-agnostic homogenization and information overload, and a learnable composer that synthesizes compact, agent-specific latent memories from a shared experience bank improves multi-agent system performance without changing the underlying frameworks. | limitations: not stated | not tested: Whether the composer trained for one set of agent roles or backbones transfers to a different MAS or model is not described; token cost of the latent memories versus retrieval baselines, and robustness to conflicting or erroneous experience in the shared bank, are not reported in the abstract.
- arxiv:2512.16962 (2025-12-18): An attacker who can supply benign-looking ingestion-level artifacts can implant malicious 'successful experiences' into an agent's long-term memory, and the agent's tendency to imitate retrieved successful patterns turns experience-based self-improvement into a vector for persistent behavioral drift across sessions. | limitations: not stated | not tested: Only one agent framework and one backbone are tested, so susceptibility of other models or retrieval designs is unknown; defenses such as provenance tracking, reader-side critique, or filtering of retrieved experience are not evaluated in the abstract.
- arxiv:2605.18401 (2026-05-18): Governed external skill libraries, with controlled exposure, credit attribution, and evidence-gated preservation, can improve frozen agents without model updates, whereas indiscriminate updates from open skill ecosystems can pollute future context. | limitations: not stated | not tested: Results are reported for a single backbone (GPT-5.2), so whether skills curated with one model help or harm other backbones is not shown; the cost of profiling, task synthesis and library search relative to the gains, and robustness to adversarial contributions in the open ecosystem, are not quantified in the abstract.
- arxiv:2605.25869 (2026-05-25): Storing long-term agent memory as flat unstructured text causes provenance-role collapse (source-monitoring errors), and a typed memory representation that structurally separates evidence, cues and claims resolves this at the architectural level. | limitations: not stated | not tested: Evaluation is on conversational QA benchmarks, not on memory written by one agent and consumed by another or by multiple writers; cost overhead of atomization and projection relative to flat-text baselines is not reported in the abstract.
- arxiv:2603.07670 (2026-03-08): Agent memory is best understood as a write-manage-read loop coupled with perception and action, organized by a three-dimensional taxonomy (temporal scope, representational substrate, control policy), and current benchmarks expose stubborn gaps in memory systems. | limitations: not stated | not tested: No original empirical comparison of mechanisms; cross-agent or cross-model memory transfer is not a named dimension of the taxonomy in the abstract.
- arxiv:2605.06130 (2026-05-07): Skill selection, utilization and distillation should be co-evolved by a single policy under one task-outcome objective rather than optimized in isolation with separate reward sources. | limitations: not stated | not tested: The skill library is written and read by the same policy, so reuse of the library by a different model or a population of agents is not tested; only two environments are evaluated.
- arxiv:2607.10113 (2026-07-11): Skill libraries for LLM agents should be understood and evaluated as lifecycle-managed, verified, evolving artifact stores rather than static prompt or tool collections. | limitations: not stated | not tested: No original experiments; patterns are synthesized from the literature with explicit caveats rather than verified empirically.
- arxiv:2605.20563 (2026-05-19): Explicit state management that mediates agents' interactions with a shared codebase and resolves conflicting edits at write time is a more effective foundation for multi-agent collaboration than git-worktree workspace isolation. | limitations: not stated | not tested: Whether the gain holds when the collaborating agents are heterogeneous models of different capability rather than copies of the same LLM; how STORM scales with the number of concurrent agents and how much of the +18.7 comes from conflict avoidance versus cost/token effects; the PaperBench gain (+1.4) is small and no variance across seeds is reported.
- arxiv:2606.24775 (2026-06-23): No single agent-memory architecture dominates across workloads; effectiveness depends on how well the memory structure aligns with the workload bottleneck, and localized maintenance is more cost-efficient than global reorganization. | limitations: not stated | not tested: Memory written by one model or agent and consumed by a different one (all systems appear to be evaluated in a single-agent, single-writer setting); multi-writer stores with conflicting contributions or provenance; the abstract does not say which underlying LLMs were used or whether results vary with the reader model.
- arxiv:2605.22842 (2026-05-12): Memory-layer attacks on shared vector stores produce agent misconduct that is indistinguishable from model failure (the Misattribution Gap), so defenders misdiagnose the cause; Semantic Norm Drift via a Trust Laundering Chain is a third path to misconduct, and provenance-aware information-flow control at the cross-session boundary blocks most of it. | limitations: not stated | not tested: Whether the defense holds when the poisoned entry is a benign-looking experience note rather than a policy-formatted document; whether models of different capability are equally susceptible to trust-laundered memory; costs of the information-flow control on legitimate cross-session memory reuse are not stated in the abstract.
- arxiv:2505.18279 (2025-05-23): A two-tier (private and shared) memory with immutable provenance attributes and policy-driven read/write transformations enables safe, efficient, and interpretable cross-user knowledge sharing among multiple agents under asymmetric, time-evolving access controls, with provable policy adherence and full auditability. | limitations: not stated | not tested: No empirical measurement of whether shared fragments actually improve other users' or agents' task performance, or how the shared store's value changes with the number and diversity of contributors; no handling of conflicting or erroneous contributions beyond permission filtering; no cost or latency evaluation of the policy machinery.
- arxiv:2602.00428 (2026-03-01): LLM-based multi-agent systems are susceptible to a collective memory bias analogous to the Mandela effect, in which false details reinforced through social influence and internalized misinformation are collectively misremembered, and this effect can be measured and substantially mitigated. | limitations: not stated | not tested: Whether the contamination effect appears in task-solving experience or memory stores rather than factual-recall tasks, and whether the capability gap between the agent introducing the false detail and the agents adopting it changes the rate at which it spreads.
- arxiv:2404.09982 (2024-04-15): Sharing memories among multiple LLM agents through real-time filtering, storage and retrieval increases the diversity of in-context memories and significantly improves performance on open-ended questions, moving from individual to collective intelligence. | limitations: not stated | not tested: Conflicts or contamination between contributions from different agents, provenance or trust of shared memories, and how the gain scales with the number and diversity of contributing agents.
- arxiv:2604.15877 (2026-04-17): Agent memory, skills, and rules are points on a single axis of increasing experience compression, existing systems each operate at one fixed compression level (the 'missing diagonal'), and transferability rises with compression at the cost of specificity. | limitations: not stated | not tested: No empirical experiment verifies that transferability actually increases with compression or that adaptive cross-level compression helps; the claimed compression ratios and their effect on latency and compute are not measured under matched conditions.
- arxiv:2604.14004 (2026-04-15): A unified memory pool drawn from heterogeneous coding domains improves coding-agent performance, chiefly by transferring meta-knowledge such as validation routines, and abstraction level dictates transferability: high-level insights transfer while low-level traces can cause negative transfer. | limitations: not stated | not tested: The abstract gives no detail on which model pairs were tested for cross-model transfer or how much of the writer's gain the reader keeps; no comparison against a same-cost self-collected pool, no seed or noise reporting, and no analysis of whether the reader can detect the harmful low-level traces.
- arxiv:2607.28272 (2026-07-30): Verbatim replay of retrieved experience causes negative transfer, and agents that critique and reconstruct retrieved experience conditioned on the current state outperform pure RL and static memory-augmented baselines, especially out of distribution. | limitations: not stated | not tested: Whether reconstruction still helps when the retrieved experience was written by a different or weaker model rather than the agent's own; how much of the gain comes from the RL training itself versus the reconstruction step at inference; per-step inference token cost of reconstructing at every decision.
- arxiv:2608.07169 (2026-08-07): Small LLM agents that cannot generate enough successful trajectories on their own can be substantially improved, without training, by hierarchical memory distilled from a large teacher agent's successful trajectories. | limitations: not stated | not tested: No comparison against memory built from the student's own (or a same-size model's) trajectories at matched collection cost, so the gain from the teacher's capability is not separated from the gain from having any memory; only one teacher is named, and the student-side inference token overhead of proactive injection is not reported.
- arxiv:2607.28048 (2026-08-04): Skills should be treated as an explicit distillation medium between agents of different capability, because a weaker student's failed trajectory and a teacher's implicit trajectory each alone are insufficient to convey the missing behaviour. | limitations: not stated | not tested: Whether the distilled skill patches transfer to a third student not used during patch refinement, or to tasks outside those where the teacher trajectory was available; the cost of the teacher runs and repeated student re-runs relative to the baselines.
- arxiv:2509.14257 (2025-09-12): Student-centred distillation, in which the teacher intervenes only at the student's first critical error and short-horizon RL starts from the verified prefix, avoids the compounding errors of imitating full teacher trajectories and lets a small student match a much larger teacher. | limitations: not stated | not tested: The cost of teacher intervention per trajectory relative to full-trajectory distillation; whether the gains hold when the teacher's action space or tool format differs from the student's.
- arxiv:2608.17050 (2026-08-17): When an Engram-style hashed memory table trained on one model is frozen and attached to a different target model, its usefulness depends primarily on a target-side reader aligned to the target backbone rather than on the memory content alone. | limitations: not stated | not tested: Transfer across larger capability gaps or across architecture families beyond the backbones studied is not described; whether the frozen table also carries the source model's errors into the target (contamination) is not examined in the abstract; evaluation is limited to question answering rather than agentic or interactive tasks.
- arxiv:2605.30723 (2026-05-29): Skill effectiveness for LLM agents is strongly model-dependent, with a skill that benefits one backbone able to harm another, and skills should therefore be adapted to each target backbone rather than treated as model-agnostic. | limitations: not stated | not tested: Which backbone families, environments and the origin of the initial skill library are not stated in the abstract; the cost of the evolution search relative to the baseline skill libraries, and whether adaptation still helps when the skill writer is much stronger than the reader, are not quantified.
- arxiv:2608.26730 (2026-08-27): In autonomous LLM post-training, past update evidence should be reused only conditionally, because an update's effect depends on its parent model, data and training stage, and context-free reuse wastes compute and can degrade the training trajectory. | limitations: not stated | not tested: Only a single 4B model is evaluated, so whether authorization conditions learned on one model transfer to a different or larger model is not tested; the abstract gives no headline numbers or comparison against simply re-running trials without the memory.
- arxiv:2605.23899 (2026-05-22): Model-generated agent skills are beneficial on average but show non-trivial negative transfer, and extractor and consumer models behave non-uniformly, with skill utility independent of model scale or baseline task strength. | limitations: not stated | not tested: The abstract does not state whether consumers can detect harmful skills at read time, nor whether extraction cost is matched against the cost of the consumer collecting its own experience.
- arxiv:2606.13594 (2026-06-11): Heterogeneous LLM agents can be aligned to communicate directly through KV-cache transfer, conveying both what one agent sees and how it reasons, matching or beating text communication at lower compute. | limitations: not stated | not tested: Only models within a single family (Qwen3) are paired, so alignment across different architectures or tokenizers is not tested; transfer is of transient activations, not persistent stored experience, so accumulation over time is not examined.
- arxiv:2607.26643 (2026-08-19): Data-driven skill self-evolution overfits to limited trajectories, and framing it as a constrained exploration-exploitation search with verified acceptance mitigates overfitting while producing skills that other agents can reuse. | limitations: not stated | not tested: The abstract does not quantify how much of the optimizing agent's gain a different reader retains, nor whether transfer holds across dissimilar tasks or action spaces; cost of the verification loop versus simpler skill generation is not stated.
- arxiv:2605.11695 (2026-05-12): Shared symbols can emerge between agents with different private visual representations from local perceptual evaluation alone, and the similarity of the agents' visual spaces shapes both the content and the symmetry of the resulting language, with all cross-agent metrics declining as encoder mismatch grows. | limitations: not stated | not tested: Only two agents and three encoder pairings are studied, so how the emergent language scales to populations of many heterogeneous agents is untested; no downstream task in which a listener must act on the shared symbols, and no LLM-based agents or textual experience transfer.
- arxiv:2606.18216 (2026-06-16): Keeping a stronger teacher inside the student's prompts rather than in the policy gradient avoids the brittleness of logit distillation and the off-policy drift of injecting teacher responses into RL, yielding better small-student generalization than off/on-policy distillation and GRPO, with the largest gains at the smallest scale. | limitations: not stated | not tested: Only a single teacher (27B) from the same model family is used, so the effect of teacher-student family mismatch or of a much larger capability gap is untested; the abstract does not report how much of the teacher's competence the student retains, nor training cost relative to the distillation baselines.
- arxiv:2512.11485 (2025-12-12): Distilling batch-clustered failures into structured, generalizable mistake notes stored in external memory lets training-free LLM agents stop repeating errors and achieve competitive effectiveness and efficiency versus existing memory and in-context methods. | limitations: not stated | not tested: Whether mistake notes written by one model help or harm a different model that does not make the same mistakes; how notes from many agents would be merged or deduplicated in a shared notebook; the abstract reports only 'competitive' performance without stating which models were used or the size of any gain.
- arxiv:2606.01139 (2026-06-02): Iteratively revising an initial imperfect agent skill using execution evidence substantially outperforms one-shot LLM-authored skills in the cold-start setting, and the revised skills capture generalized procedural knowledge that transfers across models. | limitations: not stated | not tested: Whether a skill revised on a weaker model transfers to a stronger one or vice versa, and how much of the revising model's gain the receiving model keeps, are not quantified in the abstract; the cost of the iterative re-execution loop is not compared to expert authoring on a matched budget; robustness of the retrieved repair principles across task domains beyond the three benchmarks.
- arxiv:2608.11888 (2026-08-12): Loaded agent skills frequently cause task failures and cost regressions, and these are rarely due to obviously irrelevant skills; instead seemingly relevant skills make agents mis-implement or omit required elements and turn validation checklists and construction recipes into mandatory work, with efficiency regressions not explained by prompt length alone. | limitations: not stated | not tested: Whether the harmful skills were authored by a different model than the executing agent and whether harm correlates with author-reader mismatch is not examined in the abstract; no proposed reader-side filter is evaluated for its ability to reject harmful skills before execution; the abstract does not state which agent models were used or whether findings replicate across models.
- arxiv:2605.24117 (2026-05-22): Current LLM agents rarely distill episodic experience into robust reusable procedural skills: skill-based gains are unstable under frozen deployment and raw-trajectory reuse frequently outperforms distilled skills because abstraction discards contextual and procedural cues that remain useful. | limitations: not stated | not tested: Whether a skill library written by one model or harness helps a different model reading it, and whether raw-trajectory and skill conditions are compared at matched per-reader inference token cost.
- arxiv:2608.31100 (2026-08-31): Self-improvement from interaction experience is neither automatic nor uniform: the best pathway for incorporating experience depends strongly on task structure, and recognizing successful actions is insufficient unless feedback is transformed into executable and transferable policies. | limitations: not stated | not tested: Whether histories or summaries collected by one model help a different model reading them, and whether the three pathways are compared at matched collection and inference cost.
- arxiv:2506.14728 (2025-06-17): Student agents built on small language models can reach performance comparable to large-LLM systems without training by directly reusing MCPs, structured reusable task-solving modules autonomously generated by teacher agents. | limitations: not stated | not tested: Whether errors in teacher-generated MCPs propagate to students, how performance changes as the teacher-student capability gap widens, and the teacher generation cost amortized over students.
- arxiv:2406.14596 (2024-06-20): LLMs and VLMs can generate their own high-quality in-context exemplars by abstracting generic, sub-optimal demonstrations into actionable insights refined with human feedback, and these abstractions significantly improve decision-making in retrieval-augmented LLM and VLM agents. | limitations: not stated | not tested: Whether abstractions written by one VLM transfer to a different or weaker reader model is not examined; the cost of the human-in-the-loop refinement is not matched against the cost of expert-crafted examples, and the separate contribution of human feedback versus VLM abstraction alone is not isolated in the abstract.
- arxiv:2306.09082 (2023-06-15): Control can be formulated as a search problem over a latent-indexed dataset of expert demonstrations, so that copying actions from the most similar retrieved situation yields performance comparable to trained models while enabling zero-shot task adaptation by changing the demonstration examples. | limitations: not stated | not tested: No quantitative headline figures are given, so the size of the gap to trained models is unclear; the method copies human actions verbatim and is not tested with demonstrations from other agents, lower-quality demonstrators, or a mismatched action space, nor is sensitivity to the size and diversity of the demonstration set reported.

Propose 3 proposals on this axis, each as a complete IDEA JSON with the two extra fields. Return JSON:
{"proposals":[{...}, ...]}.
