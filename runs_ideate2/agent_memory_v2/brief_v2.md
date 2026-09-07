# Title: Experience Memory and Prompt Optimization in LLM Agents: Where the Value Sits, When It Turns into Harm, and How to Measure Either

Author: Fable 5.1, 2026-09-07. Stage-1 brief for the ideate2 pipeline, written after the Stage-0 pre-scan
(8 axes, 480 papers collected, 103 carded, 28 read at section level, 40 gaps synthesized; see `digest.md`).
The pilot findings and constraints of the 2026-08 brief (`reference/track_brief.md`) are carried over unchanged.

## Keywords
LLM agents, agentic memory, experience reuse, prompt optimization, GEPA, instruction vs demonstration, injection budget,
negative transfer, memory admission, context compaction, parametric vs in-context experience, measurement methodology, ICLR

## TL;DR
Two lines of work still have not met. Prompt optimizers (MIPRO, GEPA, TextGrad successors) search over an instruction;
experience memories (ExpeL, ReMe, MemRL, skill libraries, cheatsheets) accumulate episodes and inject them at inference time.
The 2026 literature now contains dozens of systems that couple the two, compile memory into the prompt, learn when to retrieve,
or distill experience into weights, and almost none of them isolates which channel produced the gain, at what dose the gain
becomes harm, what their admission gates actually admit, or whether the headline number clears run-to-run noise. This track
looks for the sharp, falsifiable claim inside that space, on public agent benchmarks, with local open-weight models.

## What this program has already measured (starting position, not to be rediscovered)
- **Memory can be one-sidedly harmful.** In a controlled paired evaluation, injecting a full retrieved memory bank fixed zero
  items and broke six to seven (McNemar p=0.031 and p=0.016, replicated across independent runs). Noise scatters both ways; this did not.
- **Injection volume, not memory content, was the causal lever.** Cutting injection from seven retrieved items to three
  eliminated the harm from the same bank. Restricting injection to one reasoning stage did not help.
- **Write-path repairs neutralized the harm but did not convert it to gain.** Contradiction pruning and call-balance
  rebalancing moved the effect to indistinguishable-from-zero.
- **The optimizer's apparent gain was redistribution, not accuracy.** Prompt evolution fixed as many items as it broke;
  only the class-balanced metric moved. Evolving one module of a three-stage cascade was end-to-end useless.
- **Noise swallowed most claims.** Re-scoring the same candidate on the same held-out set moved the headline metric by
  0.05-0.14; a null replicate with no treatment produced the same apparent gain as the best real treatment.
- **The two components failed on disjoint slices.** The optimizer was strong where memory was weak and vice versa.
- **From the proposal rounds (v1-v6):** ExpeL's own ALFWorld table already contains the joint cell (full 59 / retrieve-only 55 /
  insights-only 50), so "memory adds value on top of an instruction" is published at about +9 points; the honest question is
  how much of the retrieval channel's value survives when the instruction is optimized on the same episodes, and under what
  budget. Twenty-seven ideas were already generated in this program (appendix); three of them sit on exactly this
  substitution question and a new proposal must go past them, not restate them.

## What the Stage-0 scan changes about the five original open questions
1. *Division of labour (instruction vs memory).* Now has published neighbours that compile experience straight into the
   system prompt (Compiled Memory / Atlas, arXiv:2603.15666; REVERE cheatsheet+prompt edits, 2603.20667; MemAPO, 2603.21520)
   and couple a memory bank with prompt evolution (MEMO, 2603.09022; MAGE, 2607.11944). None runs the 2x2
   (optimized instruction on/off x experience store on/off) at matched tokens, none reports the interaction term, and MAGE
   shows that coupling the two raises the mean while multiplying variance. The gap is confirmed independently by four of
   the eight axes. It is still open, but only as a controlled attribution, not as a demonstration.
2. *Injection budget as a decision variable.* A learned bandit over when/what/how much to retrieve now exists
   (arXiv:2607.13591, "up to 15.2 points", no static-heuristic control, no variance); mid-episode retrieval exists (AdaMEM,
   2606.05684); the dose-response of injected experience on agent traces is still uncharacterized. The length-alone effect
   (2510.05381), the nonlinear hard-distractor effect (2605.10828) and "attentional dilution" (survey 2603.07670) were shown or
   asserted on static text, never on tool-use traces.
3. *Predicting and preventing negative transfer.* The Entry-Propagation-Recovery analysis (2607.10608) shows harm begins at
   the first exposed decision and that stronger agents lose more once they comply; contextual drag (2602.04288) shows failed
   attempts in context bias later generations. Both use injected conflicts or in-task failures. No read-time control
   (utility filtering as in MemRL, provenance gating, abstention, steerable reliance) has been shown to prevent either in task
   execution, and harm from organically accumulated banks is unmeasured.
4. *Co-adaptation and drift.* Capability erosion under workflow/skill/model/memory evolution is now documented with a fix
   (Capability-Preserving Evolution, 2605.09315), and retrieval competition between old and new experience is framed as a
   stability-plasticity problem (2604.27003). "Erosion exists" is no longer a contribution; what survives is the interaction
   between an evolving instruction and an evolving store, and staleness over long streams.
5. *Measurement standards.* Still open and now has concrete targets: single-seed peak reporting is the norm (MAGE names it),
   QA-style memory scores are not shown to predict task-execution success (MemoryArena 2602.16313, LongMemEval-V2
   2605.12493), cost accounting is absent, and several benchmarks are synthetic merges with unvalidated gates.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Channel attribution at matched budget.** For one training episode set, materialize its value three ways: an instruction
  optimized on it, a retrievable store built from it, and both. Measure each channel's marginal gain and the interaction
  term with paired statistics at matched injected tokens, and report how much of the store's value survives the optimized
  instruction as a function of k. Must go beyond the archived substitution proposals (appendix) by fixing something they left
  open: the k-regime, the clause-level mechanism, the interaction sign across backbones, or the cost axis.
- **Q2 Dose-response of injected experience on agent traces.** Is the pilot's harm a function of item count, token count,
  or prompt position; does a swept static k beat a learned budget; does the curve keep its shape across backbones and across
  raw-trajectory vs distilled items? Length-only and relevance-matched decoy controls separate content from load.
- **Q3 Natural harm and read-time controls.** Accumulate a bank organically over a task stream, label each retrieved item
  post hoc (right / stale / wrong / conflicting), estimate per-item harm with entry-propagation-recovery traces, then run
  the candidate controls head to head (utility filtering, provenance gating, abstention, reliance steering) on the same
  seeds, including their clean-setting cost.
- **Q4 Write-gate audit.** Admission gates (LLM-judge validation in ReMe, five-factor admission in A-MAC 2603.04549, utility
  tagging in CraniMem 2603.15642, the three-step promotion gate in Atlas) are never audited for what they admit. Plant wrong,
  obsolete and injected records in the write stream; report per-gate precision/recall against ground truth and the downstream
  success delta versus an ungated store.
- **Q5 Abstraction level under a matched token budget.** SkillEvolBench (2605.24117) finds raw-trajectory reuse often beats
  distilled skills; SEC (four-field records) reports +7.7 points over raw trajectories on ALFWorld; AdaMEM hybridizes. Take one
  trajectory pool, materialize it at several abstraction levels (raw, indexed summary, insight, skill, graph), inject under
  the same token budget, and find where abstraction wins and which contextual cues it discards.
- **Q6 Same pool, in context versus in weights.** SIRI (2606.02355), PMD (2607.01480) and PEAM (2605.27762) internalize
  experience into weights; MemRL and ReMe keep it in context; no paper compares the two on the same pool at matched compute.
  Measure the retained value after distillation, per-task inference cost, and adaptability after a distribution shift.
- **Q7 Cross-episode persistence and staleness.** Folds, summaries and indexed state (Context-Folding, ReSum, Memex) live
  inside one episode. Carry condensed state across episodes against fresh-session and raw-trajectory controls, inject stale
  or failed prior episodes deliberately, and quantify drag versus reuse benefit over a stream with a mid-stream shift.
- **Q8 Measurement standards with named targets.** A protocol (paired designs, null replicates, minimum detectable effect,
  cost-matched baselines, QA-vs-execution validity) applied to specific published claims (e.g. ReMe's 8B-with-memory beats
  14B-memoryless, SEC's +7.7 on ALFWorld, the memory bandit's up-to-15.2, MAGE's variance multiplication). Judged as a methods
  contribution: it must overturn or qualify a specific result.

## In scope
- Domain-general agent benchmarks with public data: ALFWorld (primary; 1,465 unique tasks are available locally), WebShop,
  multi-hop QA, tool/web agents, text games. Public datasets only.
- Open-weight models served locally (27B dense and 120B MoE classes have been run in this program). The interesting result
  must not depend on frontier-scale models.
- Reimplementation of published memory and prompt-optimization methods as baselines; negative or null results when the
  measurement makes the null informative.

## Out of scope
- Any private, clinical or patient data; medical framing is excluded.
- Claims that require training or fine-tuning frontier models. LoRA-scale adaptation of local models is in scope for Q6.
- "We combined A and B and the number went up" without isolating the mechanism.
- Effects that would fall below the run-to-run noise of the setup (0.05-0.14 on the headline metric here).

## Resource constraints
One node with 4xA100 80GB; self-hosted inference only, no API model at experiment time (the optimizer/reflection role must
run locally). Experiments must fit in days: assume a few thousand evaluation episodes per configuration and design the
statistics around that. Pre-registration (thresholds, gates, amendments) is expected before the first confirmatory run.

## Appendix: the 27 ideas already generated in this program (do not restate; differentiate or move on)
Scores are the 3-judge Opus mean (0-10) from `reviews/ideation/RANKING.md`; none reached 6.5.

- memory_item_value_reliability (6.12): Item Value Is Not an Item Property: A Generalizability Audit of Per-Item Utility Estimates in Self-Editing Agent Memory
- provenance_gap_selection_not_authorship (6.07): Selection, Not Authorship: The Signed Writer–Reader Capability Gap in Agent Memory, and Why Prompt Optimization Hides It
- compile_dont_retrieve (6.0): Compile, Don't Retrieve: The Query-Conditioned Read in Agentic Experience Memory Is Inert
- memory_or_instruction (5.92): Is Your Agent's Memory Just an Un-Optimized Prompt? Measuring the Residual Value of Retrieved Experience After Instruction Optimization
- failure_signature_routing (5.87): Transfer Is Predicted by How Tasks Fail, Not by What Tasks Are About: A Routing Study for Textual Prompt Transfer
- collection_policy_coupling_collapse (5.85): Rich Get Richer, Twice: The Collection Policy — Not Content Quality — Drives Diversity Collapse When Self-Editing Memory and Prompt Optimiza
- instruction_conditioned_complementarity (5.82): What Does the Prompt Already Say? Instruction-Conditioned Complementarity Decides When Retrieved Experience Helps, Hurts, or Just Costs Toke
- coadaptation_transplant_ccr (5.77): Who Broke It, the Instruction or the Memory? A Transplant Diagnostic for Prompt–Memory Co-Adaptation, and a Counterfactual Routing Fix
- decorative_retriever (5.75): When Is a Retriever Decorative? Retrieval-Set Overlap Predicts Whether Procedural Agent Memory Must Be Retrieved or Can Be Frozen
- memory_induced_shortcutting (5.72): Memory Makes Agents Stop Looking: Premature Termination of Evidence Gathering Mediates Memory Harm, and Instruction Optimization Cannot Repa
- memory_vetoes_instruction_slot (5.72): The Instruction Slot Is Not Independent of the Memory Slot: Answer-Bearing Experience Suppresses Instruction Compliance Even Without Imitati
- coverage_currency_coupling (5.68): Concentration Is the Common Currency: Self-Editing Memory and Prompt Optimization Both Buy pass@1 by Spending Solve-Set Coverage, and Stacki
- memory_budget_confound (5.63): One Item Is the Budget: Token Volume, Not Memory Content, Explains Both the Harm and the Apparent Gains of Agentic Memory Curation
- substitutes_not_complements (5.47): Substitutes, Not Complements: Clause-Level Evidence That Optimized Instructions Shrink an Agent's Useful Memory-Injection Budget
- counterfactual_memory_screening_under_selection_noise (5.45): Does Counterfactual Screening of Agent Memory Survive Its Own Noise? Neighborhood-Conditional Utility, Winner's Curse, and Interference
- memory_dropout_coadaptation (5.45): Don't Co-Adapt: A Bank-Swap Diagnostic for Prompt Optimizers Coupled to Self-Editing Memory, and Which Fix Actually Survives Bank Turnover
- coverage_selection_division_of_labour (5.4): Coverage Failures Are the Only Thing Memory Can Sell: A Stratified Division of Labour Between Self-Editing Memory and Prompt Optimization, J
- clause_level_portability (5.38): Prompt Optimizers Discover Two Kinds of Text: A Clause-Level Attribution Study of What Transfers Across Domains
- commit_then_consult_slot_discipline (5.38): Anchoring, Not Overload: Commitment Order Explains Why Optimized Instructions and Agent Experience Memory Fight Each Other
- breadth_routed_memory (5.35): Consolidate the Broad, Retrieve the Narrow: Coverage — Not Utility, Not Usage — Decides Where Agent Experience Should Live
- playbook_transfer (5.33): Transfer the Optimizer, Not the Prompt: A Domain-General Failure→Edit Playbook for Sample-Efficient Reflective Prompt Optimization
- meta_prompt_generalization (5.3): How Many Tasks Does It Take to Optimize an Optimizer? Meta-Generalization of Learned Reflection Prompts
- action_prior_imprinting (5.27): Majority-Action Bias in Retrieved Agent Memory: A Query-Independent Action Prior, and Why Removing It Requires Per-Retrieval Calibration
- optimizer_substitutes_for_memory_scaffold (5.22): Instructions Already Say It: Optimized and Hand-Written Instructions Substitute for Agent Memory's Scaffold and Leave Only Its Content Harm
- query_agnostic_curation_ceiling (5.18): Bounded Before the Query: A Measured Ceiling on Query-Agnostic Memory Curation in LLM Agents
- memory_volume_amplifies_optimizer_curse (5.05): Does Retrieved Memory Inflate the Optimizer's Curse? Injection Budget as a Lever on Selection Bias in Agent Prompt Search
- allocation_prior_transfer (5.0): What Actually Transfers Is the Noise Model: Cross-Task Priors on Candidate Quality Make Reflective Prompt Optimization Sample-Efficient
