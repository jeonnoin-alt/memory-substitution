# Reviews of v1 (2 reviewers, claude-opus-5 via ideate.py, 2026-08) — source: agent_memory_v2_reviews.json

Aggregate: `{"score": 6.7, "verdict": "borderline", "means": {"novelty": 6.0, "significance": 7.0, "soundness": 7.0, "feasibility": 6.5, "clarity": 7.5}, "n_reviews": 2}`

## Reviewer 1 — borderline — {'novelty': 6, 'significance': 7, 'soundness': 8, 'feasibility': 6, 'clarity': 7}

**one_line_contribution**

A paired, noise-controlled measurement protocol that tests whether the reported value of ExpeL/ReasoningBank-style procedural memory disappears once a reflective prompt optimizer (GEPA) is trained on the same episodes, and whether per-instance retrieval can be replaced by a single frozen, offline-compiled instruction at matched token budget.

**closest_prior_work**

MemDelta (arXiv 2606.29914) is correctly identified by the proposal itself as the nearest work: it also shows headline memory-vs-baseline deltas are artifacts of uncontrolled comparisons (there, embedding choice). It does not, however, treat prompt optimization as a rival container for the same information, does not equalize training episodes across memory and optimizer, and never proposes deleting retrieval via static compilation — so the specific substitution-ratio object and the compiled-instruction prediction are not pre-empted, only the general 'memory baselines are confounded' framing is. EvoClinician's baseline table is a weaker collision for the reasons the proposal states.

**strongest_objection**

The design deliberately excludes the co-adaptation condition (I2: optimizing the instruction *with* memory in context), which is precisely the deployed configuration the parent track is titled around ('Coupling Self-Editing Memory with Prompt Optimization'). By construction the study can only ever conclude 'memory is redundant with optimization' or 'memory adds something optimization alone can't reach' — it cannot speak to whether jointly co-adapting the two containers outperforms either alone, which is arguably the more actionable question for practitioners who are already bolting memory onto GEPA-style pipelines. A reviewer sympathetic to the track's actual motivating question (does coupling help, and how should labor be divided) could reasonably say this proposal answers a well-controlled but adjacent question and call the omission of I2 self-serving, since it removes the condition most likely to complicate a clean substitution story.

**what_would_fix_it**

Add a compact I2 arm (optimize with memory present, then ablate the memory to test dependence) on at least the primary environment, even at reduced seed count, so the study can report not just substitution but whether co-adaptation produces gains that neither pure condition reaches — directly engaging the track's stated interest in coupling rather than only in the redundancy question. Also replicate the bank-construction method with an actual ReasoningBank-style self-judged distillation (not only ExpeL-style) on at least a reduced subsample, since ReasoningBank is explicitly named as a target of the hypothesis and its distillation mechanism differs enough from ExpeL's that the compilability finding may not transfer.

**missing_baseline**

The co-adaptation condition I2 (prompt optimized while memory is present in context), which the proposal explicitly cuts; this is the condition a reviewer aligned with the parent track's 'coupling' framing would most want to see, since it is the only arm that tests synergy rather than substitutability.

**preprint_collision**

The check is unusually thorough for a proposal template: it names MemDelta as the closest work and gives a specific, falsifiable differentiation; it flags EvoClinician's three-way baseline table as a partial precedent; and — notably — it self-corrects an earlier version that cited several unverifiable arXiv IDs (ActMem, MAS-PromptBench, TERMS-Bench, MemAPO, 2602.11243), explicitly retracting reliance on them and stating a reviewer-flagged precedent (TERMS-Bench) could not be verified. This kind of visible correction is a genuine strength of the check rather than a weakness, but the residual risk section honestly admits an unswept OpenReview 2026 could contain a 'memory + prompt optimizer' ablation buried in an appendix, which the authors cannot rule out. Given the honesty of the process, I judge the check as thin only in the sense that it could not be exhaustive, not in the sense of being lazy or unperformed.

## Reviewer 2 — borderline — {'novelty': 6, 'significance': 7, 'soundness': 6, 'feasibility': 7, 'clarity': 8}

**one_line_contribution**

A measurement protocol (the 'substitution ratio' S, a frozen-compiled-instruction arm, and a non-compilable positive control) for testing whether a GEPA-optimized instruction trained on the same episodes as an ExpeL-style memory bank absorbs most of the memory's benefit, implying retrieval can often be replaced by a one-time compiled prompt.

**closest_prior_work**

MemDelta (arXiv 2606.29914), which the proposal itself identifies and engages honestly: it shows memory-vs-RAG comparisons are confounded by retrieval-pipeline choices (embeddings etc.), but audits confounds *inside* the memory pipeline rather than positing a rival container (an optimized instruction) that can absorb the same information. If real, it is genuinely adjacent but not identical; EvoClinician (2601.22964) is a weaker collision since its three-way table is incidental, not a hypothesis. The bigger issue is that several of the cited 'closest' works (MemDelta, EvoClinician, Memory-R2, the retrieval-vs-utilization paper) carry 2026 arXiv IDs and cannot be independently verified, and the proposal's own admission that a prior version of this same check cited multiple fabricated papers (ActMem, MAS-PromptBench, TERMS-Bench, MemAPO, 2602.11243) undermines confidence that the remaining citations are real rather than a partially-corrected hallucination chain.

**strongest_objection**

The core 'fairness constraint' — that the memory bank and the GEPA-optimized instruction I1 see 'exactly the same training episodes' — is not actually enforced. The bank distills from all 500/200 training episodes; GEPA's reflective optimizer only touches whatever subset its 300 rollouts happen to sample (with likely repetition and non-uniform coverage). If I1 systematically sees less of the training distribution than the bank does, a low substitution ratio S could simply reflect unequal information exposure rather than genuine non-substitutability, which is precisely the confound the study claims to have eliminated. The proposal never reports or bounds GEPA's training-episode coverage, so the central quantitative claim (S≥0.6, etc.) rests on an unverified equal-exposure assumption.

**what_would_fix_it**

Instrument and report GEPA's actual training-episode coverage per run (fraction of the 500/200 episodes touched, and how many times each is revisited), and either (a) force GEPA rollouts to sweep the full training set at least once before terminating, or (b) build a second bank restricted to only the episodes GEPA's rollouts actually touched, to isolate whether S changes when exposure is truly matched. Also add a same-size LoRA fine-tuning arm on the open-weight model as a third container, since the proposal's own related-work section notes memory papers are also compared against fine-tuning, making its omission conspicuous for a paper about competing containers for the same information.

**missing_baseline**

A fine-tuning (e.g., LoRA) arm on the same open-weight agent trained on the identical training episodes, as a third candidate 'container' for the training-episode information — explicitly motivated by the proposal's own claim that published memory papers compare against either a fixed instruction or fine-tuning.

**preprint_collision**

The check is unusually self-aware (it flags and retracts a prior version's hallucinated citations), which is a mark of honesty, but this honesty itself is a red flag: it shows the underlying literature search process has already produced fabricated arXiv IDs once, and the remaining citations (MemDelta 2606.29914, EvoClinician 2601.22964, Memory-R2 2605.21768, 'Diagnosing Retrieval vs. Utilization' 2603.02473) all carry similarly patterned 2026 IDs that cannot be verified from the material given. The check reads as thin on methodology (no description of what was searched, when, or how) despite its length, so the novelty claim relative to MemDelta in particular should be treated as unconfirmed rather than established.

