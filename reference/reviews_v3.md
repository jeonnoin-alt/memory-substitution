# Reviews of v3 (3 reviewers) — source: agent_memory_top4_reviews.json

Aggregate: `{"score": 5.73, "verdict": "borderline", "means": {"novelty": 5.3, "significance": 5.7, "soundness": 6.3, "feasibility": 5.0, "clarity": 6.3}, "n_reviews": 3}`

## Reviewer 1 — borderline — {'novelty': 5, 'significance': 5, 'soundness': 7, 'feasibility': 4, 'clarity': 7}

**one_line_contribution**

A large controlled study proposing that per-instance retrieval in procedural agent memory can be replaced by a frozen, dev-frequency-selected subset without accuracy loss once a cheaply-measured top-k retrieval-set Jaccard overlap exceeds ~0.5, with that same overlap statistic predicting the retrieval premium out-of-sample and the sign of the 'more memory hurts' volume effect — run entirely without any prompt optimizer.

**closest_prior_work**

arXiv:2511.21730 ('A Benchmark for Procedural Memory Retrieval in Language Agents') isolates retrieval quality from execution on ALFWorld and identifies the bag-of-words embedding failure mode that would mechanistically produce the high-overlap retrieval sets this proposal measures. The proposal's own collision check correctly notes this paper never freezes a subset, never token-matches, and offers no pre-deployment predictor — so the specific end-to-end ablation is not scooped — but the directional claim (static/compiled content can match or beat per-instance retrieval in procedural settings) is clearly convergent across several cited 2025-26 preprints, which the proposal itself concedes.

**strongest_objection**

The track is explicitly framed around coupling self-editing memory with prompt optimization (GEPA/MIPRO-style division of labor, co-adaptation, injection budget under optimization), and this proposal deliberately runs zero optimizer arms, justifying the omission as noise reduction. As written, the study answers 'is per-instance retrieval necessary at all in procedural memory' rather than the track's central question of how memory and an optimizer should interact — a track-focused AC could reasonably judge this out of scope regardless of its internal rigor.

**what_would_fix_it**

Add at least one cell where a real prompt optimizer (e.g., GEPA) is run over the instruction container while memory is held frozen vs. retrieved per-instance, testing whether optimization shifts the overlap threshold at which retrieval becomes necessary — this would preserve the frozen-subset machinery already designed while directly answering the track's coupling mandate instead of sidestepping it.

**missing_baseline**

A prompt-optimizer-tuned instruction baseline (GEPA or MIPRO applied to the compiled/frozen memory content) is the baseline the track's own framing would demand, since the stated research question is specifically about memory-optimizer interaction and the proposal contains no arm involving an optimizer at all.

**preprint_collision**

The Preprint Collision Check is unusually thorough in structure — it lists withdrawn citations from a prior draft, engages the closest work (2511.21730) with quoted text, and states explicit refutation conditions if the direction turns out to be already established. However, it rests heavily on a large number of very recent (2026) arXiv IDs with precise quotations that cannot be independently verified here, and the check itself admits an earlier draft 'was caught citing arXiv IDs I could not see in a search result' — a red flag about the reliability of the evidence base even after the stated correction. Given the pace of this subfield, the check's own stated residual risk (an appendix ablation in a combined-system preprint) is plausible and not fully closed off.

## Reviewer 2 — borderline — {'novelty': 5, 'significance': 6, 'soundness': 7, 'feasibility': 5, 'clarity': 6}

**one_line_contribution**

Propose that per-instance retrieval in procedural agent memory is often 'decorative' — replaceable by a fixed, query-independent subset of the bank with negligible accuracy loss — and that a cheap, pre-deployment statistic (top-k retrieval-set Jaccard overlap across queries) predicts out-of-sample when this holds versus when retrieval actually matters.

**closest_prior_work**

arXiv:2511.21730 ('A Benchmark for Procedural Memory Retrieval in Language Agents') already isolates retrieval quality from execution on ALFWorld and finds that embedding-based retrieval collapses procedures to near-identical bag-of-words sets while LLM-abstracted procedures transfer — exactly the mechanism this proposal needs for its overlap mediator. The proposal concedes this is a 'real partial collision' and differentiates on the end-to-end frozen-subset swap, token-matching, and the predictive diagnostic, which is a fair but narrow novelty wedge given how much of the underlying direction is already stated by that paper and by several other cited 2026 preprints.

**strongest_objection**

The call this proposal was solicited for is explicitly titled 'Coupling Self-Editing Memory with Prompt Optimization,' and the proposal deliberately runs zero optimizer arms, no coupled-optimization comparison, and no substitution-ratio analysis — the exact composition question the track frames as central. Studying memory retrieval in total isolation from any optimizer is a reasonable and well-executed study on its own terms, but it does not address 'coupling' at all, and a program committee reading against the call would likely see this as a scope mismatch rather than a sharpened instance of the assigned problem.

**what_would_fix_it**

Add at least one genuine coupled arm — run a real reflective/evolutionary prompt optimizer (GEPA-style) jointly with the frozen-vs-retrieved memory conditions on a subset of cells — to test whether the 'decorative retriever' finding and the overlap law survive or change when the instruction container is itself being optimized against the memory bank, which would tie the contribution back to the track's actual ask instead of treating the optimizer as an orthogonal, cuttable arm.

**missing_baseline**

A 'stuff the entire bank into context, unretrieved and uncompiled' baseline (feasible at the smaller N values, e.g. N=100) to separate 'the frontier-model compilation is doing the work' from 'the model just needs the content available at all'; the current design only contrasts frozen-top-k, compiled, and per-instance retrieval, never raw full-context injection.

**preprint_collision**

The check is unusually long and self-critical — it explicitly states that an earlier draft cited arXiv IDs (MemDelta, Memory-R2, A-Mem, MemAPO, EvoClinician, etc.) that could not be verified in a search and were subsequently withdrawn. That admission is honest, but it also means the remaining collision analysis leans on a long list of very recent (2601–2607.2026) preprints with suspiciously tidy supporting quotes that cannot be independently checked here. The one collision that reads as credible and well-engaged (arXiv:2511.21730) is conceded as a genuine partial overlap in direction; the proposal's own quoted 'search verdict' states the direction is already converging across several 2025–2026 papers, which weakens rather than establishes the novelty claim and leaves the paper's contribution resting narrowly on the predictive-diagnostic framing rather than a genuinely new finding.

## Reviewer 3 — borderline — {'novelty': 6, 'significance': 6, 'soundness': 5, 'feasibility': 6, 'clarity': 6}

**one_line_contribution**

A large, statistically elaborate empirical program that replaces per-instance top-k retrieval with a frozen/compiled subset of the same procedural memory bank, and proposes a cheap pre-deployment statistic (top-k retrieval-set Jaccard overlap) that predicts when retrieval can be safely deleted without accuracy loss.

**closest_prior_work**

arXiv:2511.21730 ('A Benchmark for Procedural Memory Retrieval in Language Agents'), which already shows embedding-based procedural retrieval collapses to near-identical top-k sets and that LLM-abstracted procedures transfer better — the mechanistic precursor to this proposal's overlap statistic. The authors concede this directly and try to differentiate on the end-to-end frozen-subset swap and the predictive law, which is a real but narrow gap since the 'direction' is explicitly acknowledged as already converging across 2511.21730, 2602.02751, and 2606.23127.

**strongest_objection**

The track is explicitly about coupling self-editing memory with prompt optimization, yet this proposal runs zero prompt optimizer and treats a single frontier-model, non-iterated compilation (A_comp) as a 'lower bound' on what an optimizer could extract from the memory bank — an assumption that is never tested. If a real reflective optimizer (GEPA/MIPRO-style) could squeeze substantially more value out of the bank into instructions than one-shot compilation, the central 'retrieval is decorative / can be frozen' conclusion would not transfer to the actual coupled setting the call is soliciting, and the paper's claim to be a 'service to the track' by naming where coupling research should occur is undercut by never checking whether coupling helps where the naive compiled arm ties with retrieval.

**what_would_fix_it**

Add at least one cheap, budget-preserving optimizer arm (e.g., a small number of reflective self-refinement passes on the compiled instruction, or a lightweight GEPA-lite run at fixed rollout budget) to test whether real optimization closes the gap the naive A_comp leaves open, directly engaging the track's coupling question; additionally, strengthen the 20-cell regression with hierarchical/mixed-effects pooling that accounts for cells sharing banks/environments (many cells are not independent draws), since the headline 'law' claim currently rests on a small, likely-correlated, possibly bimodal sample.

**missing_baseline**

A genuine prompt-optimizer arm (even a minimal one) that iteratively refines the compiled instruction against dev performance, rather than relying solely on a single frontier-model one-shot compilation as the 'deployment' and 'lower bound' arm — this is the baseline a track reviewer focused on memory-optimizer coupling would most directly demand.

**preprint_collision**

Unusually thorough and self-critical: the authors explicitly retract several arXiv IDs from a prior draft that reviewers flagged as unverifiable/hallucinated, and restrict current claims to items 'returned by the current search,' naming 2511.21730 as the closest threat and conceding the 'direction' is already established by several 2025-2026 preprints. This diligence is commendable, but the admitted history of citing non-existent or unverifiable arXiv IDs in an earlier version is itself a red flag — it means the current set of citations (several with unusual 2026 IDs) cannot be fully trusted without independent verification, and the check's residual-risk paragraph ('I could not sweep OpenReview 2026 submissions') concedes the search is incomplete rather than exhaustive.

