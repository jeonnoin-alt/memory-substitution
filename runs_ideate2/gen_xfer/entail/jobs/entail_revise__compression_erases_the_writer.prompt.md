=== SYSTEM ===
You are revising your own research proposal after review.

The reviewers' objections are the specification. Answer each one concretely — not by adding reassuring prose, but by changing the design: cut experiments that do not carry a claim, drop target tasks, shrink the grid, narrow the claim to what the sample size can actually detect, add the baseline they named.

Two rules:

- **Do not abandon the core hypothesis.** A proposal that answers every objection by becoming   generic is worse than one that keeps a sharp claim and scopes it honestly. If an objection   can only be answered by giving up the contribution, keep the contribution and say in   changes_made why you refused.
- **Novelty is the thing you are most likely to lose.** Measured across revision rounds,   answering reviewers reliably raises soundness and feasibility and *lowers* novelty: the   claim gets hedged, the scope narrows, and what was surprising becomes safe. Guard against   that. Do not soften the central claim into something a reviewer could not disagree with, do   not replace a sharp mechanism with a measurement study, and do not add qualifiers that make   the prediction unfalsifiable. If a reviewer's objection is really "this is risky", the right   answer is a better test of the risky claim, not a smaller claim. State in changes_made what   you did to keep the claim as sharp as it was.
- **The resource envelope is hard.** Every experiment must fit the stated compute and budget.   If the full matrix does not fit, cut it to a primary experiment that decides the main claim   plus the minimum ablations that isolate the mechanism, and state the arithmetic: number of   runs x rollouts per run, and why that fits. A smaller study that can be run beats a large   one that cannot.

=== USER ===
=== PROPOSAL ===
{
 "Name": "compression_erases_the_writer",
 "Title": "Compression Erases the Writer, Not the Gain: Abstraction Level of Transferred Experience Helps Only When Writer != Reader",
 "Short Hypothesis": "The benefit of compressing agent experience before transfer is an interaction with writer identity, not a main effect. For a reader consuming its own success-filtered pool, raw trajectories beat writer-compressed summaries and procedures at matched injected tokens; for a pool written by a different backbone the order reverses, because compression strips the writer-specific search, phrasing and binding content that the reader cannot imitate. The survey claim 'transferability rises with compression' (2604.15877) and the finding 'raw beats distilled skills' (2605.24117) are the two cells of one interaction, and the sign of the raw-minus-compressed contrast is predicted by whether the writer is the reader.",
 "Related Work": "2604.15877 states the compression axis (memory -> skills -> rules) and asserts transferability rises with compression, with no experiment. 2605.24117 (SkillEvolBench) shows raw-trajectory reuse often beats distilled skills, but writer and reader are the same backbone and tokens are not matched. 2604.14004 (memory transfer learning, coding agents) finds high-level insights transfer and low-level traces cause negative transfer across domains, without naming model pairs, without a self-pool control and without token matching. 2605.12978 finds consolidated memories degrade relative to raw episodic ones, again same backbone. 2606.23127 (procedural memory benchmark, 382 enterprise tasks) reports that some skills transfer across backbones and others specialise, but does not manipulate abstraction level or compare against raw traces. 2608.07169 distils a teacher's trajectories into one hierarchical level for small students with no raw-trace or self-pool arm. Home literature: 2509.22230 (reasoning traces tailored to the student by filtering tokens improbable under it) gives the distributional-misalignment mechanism at training time; this proposal tests its in-context analogue. Archived abstraction_discards_bindings_and_repairs (5.95) varied abstraction within one writer; here the writer is the manipulated variable and the claim is that the contrast flips sign with it.",
 "Abstract": "Two published positions on how experience should be stored for reuse contradict each other: a survey argues that transferability rises with compression, while a benchmark finds that raw trajectories beat distilled skills because abstraction discards state-contingent cues. Neither manipulates who wrote the experience. We propose that both are right in different cells of one design. On ALFWorld we build three pools from the same training games -- expert walkthroughs, Qwen3-32B's own successes, and EXAONE-4.0-32B's own successes (collected at the same episode budget) -- and have each writer compress its own pool to three levels: raw trajectories, per-item summaries, and per-type procedures, each injected at about 420 tokens. Two 32B readers of different families read every level of every pool through one fixed retriever, so the self cells and the foreign cells differ only in writer identity at matched capability. The estimand is the interaction: (raw - compressed) for the reader's own pool minus (raw - compressed) for a foreign pool, with the retained-gain ratio per writer x reader x level, all net of a static expert-written procedure prompt and a memory-free baseline. We predict raw wins in self cells and compression wins in foreign cells, an interaction of at least 8 net points, that re-compressing the foreign pool with the reader itself does not change the result (what matters is what compression removes, not who words it), and that at the procedure level no writer beats the static prompt. A null interaction, or raw winning everywhere, falsifies the account and settles the survey's claim negatively for this domain.",
 "Experiments": "Domain and partition: ALFWorld. Bank = training games minus a held-out slice of 400 training games excluded from every pool; evaluation = 274 validation games (140 seen, 134 unseen) + the 400 held-out training games = 674 games x 2 seeds per cell (about 1,350 episodes/cell). Retriever fixed (Measurement A's). Writers: E = expert walkthroughs (1,465, minus held-out); Q = Qwen3-32B self pool (1,892 successes, minus held-out); X = EXAONE-4.0-32B self pool, collected on the same 3,553 training games at the same scaffold and temperature (about 3 GPU-hours), success-filtered. Levels, produced by the writer model itself from its own pool: L0 raw trajectory (k=3, about 430 tokens, as measured); L1 per-item summary (4-6 lines keeping object and receptacle names, about 70 tokens, k=6); L2 per-type procedure (one paragraph per task type distilled from the writer's own pool, all six injected, about 420 tokens). For E, which has no writer model, the compressor is the non-reader backbone (X-compressed E for the Qwen3 reader, Q-compressed E for the EXAONE reader) so E stays fully foreign; the reader-compressed version is the compressor-identity ablation. Readers: Qwen3-32B and EXAONE-4.0-32B (both 32B: family mismatch at approximately matched capability; both serving to be verified in vLLM before the first confirmatory cell). Cells: 3 levels x 3 writers x 2 readers = 18, plus per reader k=0, the static expert procedure prompt (Measurement C), and 4 compressor-identity ablation cells (foreign pool and E re-compressed by the reader at L1 and L2) = 26 cells, about 35k episodes; at about 18 episodes/min per replica on two replicas about 16 h, plus 3 GPU-h for the X pool and about 1 h of batched compression. Scheduling: GPU0 serves the Qwen3 reader cells while GPU1 collects X then serves EXAONE reader cells; about 1.5 days. Estimands per cell: net success gain over k=0 paired by game and seed; D(w,r,L) = gain(L0) - gain(L) for L in {L1, L2}; interaction I(r) = D(self) - D(foreign); retained-gain ratio = foreign gain / reader's self-pool gain at the same level; everything also reported net of the static prompt. Manipulation checks (not predictions): token counts per level within +-10%; textual divergence between writers' L1/L2 sets (embedding and edit distance) so that a null at L2 caused by textual convergence is recognised and L1 becomes the primary compressed level; per-type composition of each pool. Type-balanced subsampling of pools (equal per-type counts) as an ablation because the self pools are type-skewed. Pre-registration of gates, margins and amendments before the first confirmatory cell.",
 "Baselines and Ablations": "Memory-free k=0 per reader. Static expert-written six-procedure prompt (Measurement C) per reader: every gain reported net of it. Self-pool control at matched collection cost is built in (Q->Qwen3 and X->EXAONE, both from the same 3,553-game budget). Compressor identity: foreign pool re-compressed by the reader vs by the writer, and the E pool compressed by either backbone. Format-only placebo: L0 with thoughts stripped to actions and observations only (template-normalised), to separate the writer's phrasing from its content. k-matched (k=3 at every level) vs token-matched (primary). Type-stratified results (clean/heat/cool vs pick/look/pick-two) and seen vs unseen. Type-balanced pools. Optional capability arm if GPU time permits: gpt-oss-120b as a third writer at L0 and L2 for the Qwen3 reader (capability gap at fixed scaffold).",
 "Falsifiable Predictions": "P1 (self cells, raw wins): D(self, L2) = gain(raw) - gain(writer-written procedures) >= +4 net at matched tokens in both self cells (Q->Qwen3, X->EXAONE). Falsified if the 95% CI of D(self) lies entirely below +4 in either self cell; produced by the Q->Qwen3 L0 vs L2 cells (and X->EXAONE). P2 (foreign cells, compression wins): D(foreign, L1) <= -4 net and D(foreign, L2) <= -4 net in X->Qwen3 and Q->EXAONE. Falsified if raw foreign is at least as good as compressed foreign (CI of D(foreign) entirely above -4) in both foreign cells; produced by the X->Qwen3 L0 vs L1/L2 cells. P3 (headline interaction): I(r) = D(self) - D(foreign) >= +8 net with a 95% CI excluding 0 for each reader. Falsified if the CI includes 0 or I is negative; produced by the four cells self-L0, self-L2, foreign-L0, foreign-L2 for that reader. P4 (what is removed, not who words it): re-compressing the foreign pool with the reader itself changes the foreign compressed gain by less than 4 net relative to the writer-compressed version. Falsified if reader-compressed exceeds writer-compressed by >= 4 net with CI excluding 0; produced by the compressor-identity ablation cells. P5 (procedures are writer-agnostic): at L2 no writer's procedures exceed the static expert procedure prompt by >= 4 net for a given reader. Falsified if X-written or Q-written procedures beat the static prompt by >= 4 net with CI excluding 0; produced by the L2 cells against the Measurement C cell. P6 (retained-gain ratio rises with level): for each foreign writer x reader, ratio(L2) > ratio(L0) by >= 0.2. Falsified if ratio(L2) <= ratio(L0); produced by the foreign L0 and L2 cells with the self-pool denominators.",
 "Measurement and Noise Control": "Paired design: every cell runs the same 674 games x 2 seeds with the same retriever and sampling settings as Measurement A; cells differ only in writer, level and reader. Per-cell net gain half-width about +-5 net at 674 x 2 seeds (scaled from the measured +-8 at 274 x 2); the interaction contrast of four cells has half-width about +-8, so the +8 margin of P3 is at the detection edge and the pre-registered amendment is escalation to 4 seeds on the four headline cells per reader if the CI half-width exceeds 6. Mixed-effects logistic model with game random effects and cluster bootstrap over games for all contrasts; type-stratified estimates reported alongside. Injected token counts logged per episode and matched within +-10%; retrieval results logged so that every cell at a level sees the same retrieved game ids. Margins as fractions of the Gate-0 effect: Measurement A's +27 net is the reference; +4 is 0.15 of it, +8 is 0.3. Unseen-only claims carry the 134-game CI and are reported as secondary.",
 "Preprint Collision Check": "(1) mechanism, last 12 months, query 'abstraction level of transferred experience raw trajectories versus summaries versus procedures cross-model agent memory' --recent, channel s2+hf: MemHarness 2607.28272 (reconstruction, same writer), 2606.23127 (procedural memory transfer across backbones, no level manipulation), 2605.24117 (raw beats skills, same backbone), 2605.12978 (consolidation degrades vs raw episodic, same backbone), 2604.27003, 2604.14004, 2601.07470 (MCMA learned memory abstraction), 2506.07398; none manipulates writer identity against abstraction level at matched tokens. (2) closest named method, query 'cross-model transfer agent skills model-dependent negative transfer abstraction' --recent, channel s2+hf: 2608.22610 (coalition-aware skill reliability: cross-domain utility reversal), 2608.01149 PATH-Bench, 2606.03565, 2605.30723 (model-aware skill alignment), 2605.23899; none compares raw vs compressed by writer; id 2606.23127 verified with 's2cli.py paper' (382 enterprise tasks, 22 skills, transfer across roles and backbones). (3) home: query 'demonstration abstraction level transfer across learners: concrete traces versus abstract plans, negative transfer with mismatched demonstrator', channel s2+hf: 2509.22230 (student-tailored reasoning traces, distributional misalignment at training time), 2605.12798 (data-mediated transfer), 2604.14004; no in-context result on abstraction x demonstrator identity. No collision found; the nearest, 2604.14004 and 2605.24117, occupy one cell each of the proposed interaction.",
 "Risk Factors and Limitations": "EXAONE-4.0-32B serving in vLLM is unverified; fallback is gpt-oss-120b as the second backbone (then family and capability are confounded and the claim is reported as foreign-writer only) or a second Qwen3-32B scaffold as a proximity-only foreign writer. P1 may fail (compression free even for the reader's own pool), which refutes 2605.24117 in this domain and is reportable, but then the interaction is a main effect of level and the title claim falls. L2 texts from different writers may converge, making L2 uninformative; L1 is pre-registered as the primary compressed level in that case. The self pools are type-skewed towards easy types; the type-balanced ablation guards against a composition artefact. ALFWorld procedures are short and the ceiling at k=3 is near 0.87 on unseen, so gains are bounded above; margins are set as fractions of the measured +27. Two 32B families approximate matched capability but their k=0 rates will differ; the retained-gain ratio uses each reader's own self-pool gain as denominator to absorb this. Capability at fixed proximity is only an optional arm here; the design manipulates proximity (family) at approximately fixed capability.",
 "Addresses gap": "G10 (compression-transferability claim untested against raw-beats-skills at matched inference cost), with G6 (same-backbone evaluation) as the manipulated variable.",
 "Not a restatement of": "Brief prior-result bullet Measurement A (expert raw k=3 gives +27/+32 net; unseen approx seen, procedure-bound): it measured one foreign writer at one level; this idea claims the sign of the raw-vs-compressed contrast depends on whether the writer is the reader, which no single-writer measurement can show. Digest card arxiv:2604.14004 (high-level insights transfer, low-level traces cause negative transfer): it reports a cross-domain main effect of abstraction with unnamed model pairs and no self-pool; this idea claims the low-level harm exists only for foreign-written traces and reverses into a benefit for the reader's own traces at matched tokens. Archived abstraction_discards_bindings_and_repairs (5.95) varied level within one writer; this idea fixes level and swaps the writer, and the interaction is the estimand."
}

=== ENTAILMENT CHECK (pre-review) ===
{
 "name": "compression_erases_the_writer",
 "predictions": [
  {
   "id": "P1",
   "depends_on": "Self cells Q->Qwen3 and X->EXAONE, L0 vs L2 at matched injected tokens, paired by game and seed over 674 games x 2 seeds; stated per-cell half-width ~+-5 net, so a two-cell contrast is ~+-6.",
   "falsifier": "The 95% CI of D(self) lies entirely below +4 in either self cell (the writer's own procedures are at least as good as its raw trajectories).",
   "label": "unresolvable",
   "reason": "The +4 margin sits inside the design's own noise (two-cell contrast half-width ~+-6, and the pre-registered seed escalation only triggers above +-6), so the natural anti-hypothesis outcome D(self)~0 gives a CI straddling +4 and falsifies nothing.",
   "fix": "Restate the falsifier as 'CI excludes +4 from below' so a null falsifies, and pre-register 4+ seeds on both self L0/L2 cells until the contrast half-width is <= 2."
  },
  {
   "id": "P2",
   "depends_on": "Foreign cells X->Qwen3 and Q->EXAONE, L0 vs L1 and L0 vs L2, token-matched, same fixed retriever and same paired games; L1 cells are outside the four headline cells the escalation amendment covers.",
   "falsifier": "CI of D(foreign) entirely above -4 in BOTH foreign cells (raw foreign at least as good as compressed foreign).",
   "label": "unresolvable",
   "reason": "-4 is inside the ~+-6 contrast noise and the falsifier is conjunctive over both foreign cells, so a flat D(foreign)~0, or one cell in which raw foreign wins, refutes nothing.",
   "fix": "Make falsification per-cell with a CI that must exclude 0 in the predicted direction, and extend the seed escalation to the L1 cells so every contrast has half-width <= 2."
  },
  {
   "id": "P3",
   "depends_on": "The four cells self-L0, self-L2, foreign-L0, foreign-L2 for each reader; interaction half-width ~+-8, ~+-6 after the pre-registered 4-seed escalation.",
   "falsifier": "The 95% CI of I(r) includes 0, or I(r) is negative, for either reader.",
   "label": "open",
   "reason": "Nothing in the design fixes the sign of D(self)-D(foreign): both readers, both self pools and both foreign pools are actually run, so a null or reversed interaction is a directly measurable outcome and the 'CI includes 0' falsifier is easy to reach at the stated power.",
   "fix": ""
  },
  {
   "id": "P4",
   "depends_on": "Compressor-identity ablation cells: the foreign pool (and E) re-compressed by the reader vs by the writer at L1 and L2, same reader, same retrieval.",
   "falsifier": "Reader-compressed exceeds writer-compressed by >= 4 net with CI excluding 0.",
   "label": "unresolvable",
   "reason": "This is an equivalence claim with a 4-point bound tested against a ~+-6 contrast half-width, so any failure to detect confirms it, and the falsifier is one-sided: a reader-compressed version 4+ points WORSE also contradicts 'changes by less than 4' without falsifying.",
   "fix": "Two-sided TOST at +-4 with seeds giving a contrast half-width <= 2, and count a large negative difference as falsifying too."
  },
  {
   "id": "P5",
   "depends_on": "L2 cells for each writer versus the Measurement C static six-procedure prompt per reader; all gains are already reported net of that prompt, so this contrast is the L2 net gain itself.",
   "falsifier": "X-written or Q-written procedures beat the static prompt by >= 4 net with CI excluding 0.",
   "label": "unresolvable",
   "reason": "Another 4-point bound against ~+-6 noise, stated as a universal null over several L2 cells, so non-detection confirms it and only an implausibly large single-cell effect could falsify.",
   "fix": "Recast as an equivalence test with a pre-registered bound and power (half-width <= 2), or pre-register that any single L2 cell whose CI lies above 0 falsifies."
  },
  {
   "id": "P6",
   "depends_on": "Foreign L0 and L2 gains divided by the same reader's self-pool gains at the same level - i.e. exactly the four cell means that already produce P1, P2 and P3; no CI or noise figure is stated for the ratio.",
   "falsifier": "ratio(L2) <= ratio(L0) for some foreign writer x reader pair.",
   "label": "entailed",
   "reason": "If P1 holds (g_self(L0) > g_self(L2)) and P2 holds (g_for(L2) > g_for(L0)), then ratio(L2)=g_for(L2)/g_self(L2) exceeds ratio(L0) by arithmetic on shared measured terms, so the falsifier is just the negation of P1/P2 and P6 tests nothing new.",
   "fix": "Replace with an estimand not built from the same four means (e.g. absolute foreign gain against an independent expert or third-writer denominator) reported with its own bootstrap CI and a margin larger than that CI."
  }
 ],
 "shared_terms": [
  "P1-P3: D(self) is one term of I(r)=D(self)-D(foreign); the same self-L0 and self-L2 means determine both.",
  "P2-P3: D(foreign) is the other term of I(r), so P3 is fixed once P1 and P2 are measured on the same four cells.",
  "P1-P2-P6: ratio(L)=g_foreign(L)/g_self(L) is a ratio of those same four cell means, so P6 is an arithmetic consequence of P1 and P2.",
  "P4-P5: both are scored on the foreign L2 gain net of the static prompt, so a single cell mean moves both."
 ],
 "headline": "P3",
 "headline_status": "open",
 "n_open": 1,
 "n_entailed": 1,
 "n_near": 0,
 "n_unresolvable": 4,
 "verdict": "revise"
}

=== BINDING RULES FROM THE BRIEF ===
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

- **Measurement C, finished 2026-09-09 (paired per game with the k-sweep, 274 games × 2 seeds):** the best static arm is `static3` (3 fixed type-conditioned expert exemplars, ~430 tokens, cached). static3 − k0 = **+12.4 net** [+7.7, +17.3]; k3 − static3 = **+17.2 net** [+11.9, +22.4] (seen +14.3, unseen +20.1; clean +26.7 / heat +25.6 / cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1. The type-agnostic six-procedure prompt (`instr_all`) is +9.5 over k0 and −20.1 under k3; the wrong-type placebo (`blind1`) is −3 under k0. **Binding:** any prediction about the retrieval residual over the best static arm at the natural bank must be stated against this measured +17.2 (CI half-width ≈ ±5), not against an assumed null; a claim that the residual vanishes must name the manipulation that removes it. Full table in `runs/STEP0_RESULTS.md`.



Every prediction labelled entailed, near_entailed or unresolvable must be either made open (change the arms, split, estimand or seeds as the 'fix' suggests, or add the arm that can produce the falsifying outcome) or removed. The headline prediction must be open. Keep the same Name and keep the core claim. Return ONLY the revised IDEA JSON with all standard fields plus 'Addresses gap', 'Not a restatement of' and 'Changes made' (a short list: which prediction, what changed).
