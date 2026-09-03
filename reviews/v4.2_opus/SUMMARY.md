# v4.2 judging, Opus 5 round — 2026-09-03

## Aggregate
**6.40 — borderline** (nov 6.0 / sig 6.0 / snd 6.7 / fea 7.0 / cla 7.3). R1 6/6/6/7/8, R2 6/6/7/7/7, R3 6/6/7/7/7.
Trajectory (Opus): v4 5.93 → v4.2 6.40. The identification objection is gone; all three now describe the crossover as "the new thing" and object to power, scope and missing full-data arms.

## Objections and v4.3 answers
| Objection | Who | v4.3 |
|---|---|---|
| Δ_info reduces to acc(I1a×M_b) − acc(I1a×M_a); S_info's ratio is unpowered (delta-method CI ≈ [0.23, 0.89] at the median scenario); no MDE for S_info; SE 0.7 optimistic because instances are shared across the 8 contrasts | R1, R2 | Δ_info is the sole confirmatory endpoint (threshold 2pt, one-sided); S_info descriptive with delta-method CI; SE bound recomputed with shared instances (0.7–1.24pt → MDE 1.8–3.1pt), fitted ρ reported |
| The gate is at I0 but the endpoint lives at I1; modal outcome is other ≈ 1–4pt → undefined primary after 44k episodes | R2, R3 | New gate G7 on S_dev: memory gain from the unseen half's bank at the optimized instruction ≥4pt (lower 80% CI ≥2pt); fail → pre-registered reframe as the headroom paper before S_test |
| Full-data arms missing: I1_ab×M0, I0×M_ab, I1_ab×M_ab, I1_ab×C_ab — the practitioner's question | R1, R2, R3 | Added, Tier 0; cell 18 replaced by I1_ab×C_ab |
| Joint instruction+demonstration optimizer (MIPROv2 as published) is the true prompt-container ceiling; D_opt buried in Tier 2 | R2, R3 | J (joint) Tier 1 at 2 seeds; D_opt promoted to Tier 1 |
| Own-vs-other may be textual redundancy (same distiller, same episodes), not information | R1 | Re-distilled bank B_a^re by a different distiller (local Qwen3-32B): Tier 1 cells |
| Substitution vs interference licence opposite headlines; pre-register the fix/break signature | R3 | Prediction 1b: substitution = fewer fixes at equal breaks; interference = more breaks |
| G6 balance gate has no power; both-directions requirement splits a true effect | R1 | G6 dropped; balance reported on S_test; direction×half interaction fitted; per-direction reported |
| E2 floor (3.8–4.6pt at n=274) exceeds the claim threshold | R3 | E2 explicitly directional; floor stated |
| Near-duplicate positive control is non-substitutable by construction; need a procedural one | R1 | B_a+proc10: instance-specific procedural rule without the answer, Tier 0; dup10 → Tier 1 |
| Title claims the field; robustness is two Qwen checkpoints | R3 | Scope named in title/abstract; memory-null pairings co-equal; cross-family in-scope candidate (medgemma-27b-it, Gemma-3 family) added to screening |
| E1 (BM25 multi-hop QA) is a poor place for procedural memory | R2 | Refused with reasons: the program's measured priors (bank effects, seed variance) exist only there; corpus fixed and public; E2 is the template-repetitive complement; limitation stated |
| EvoAgentBench absence claim unverified | R1, R2, R3 | **Resolved from the PDF (PI-supplied, 15 pp).** Conditions: Vanilla, +Memento, +RB, +GEPA, +Anchor†; "GEPA evolves one prompt on D_train and broadcasts it … the only no-retrieval evolution condition"; results "averaged over three independent runs per instance … standard error"; no paired test, no bootstrap, the word "token" does not occur; Support@10 is the retrieval budget for skill/case methods. **Correction:** ReasoningBank on Qwen3.5-27B is +3.6 (avg 41.1 vs 37.5), not "+7" as the August web snippet said; GEPA +1.2 there, +5.7 on Gemma-4-31B, −12.3 on OpenClaw/Qwen3.5-27B/KW |

## Freeze rule
Per the program's T-A rule (freeze after round 3 with round-3 blockers resolved or descoped), v4.3 is the resolution text. One confirmatory Opus round is run for the record; a new design-blocking finding there reopens the loop, anything else is logged and the design proceeds to DESIGN.md.
