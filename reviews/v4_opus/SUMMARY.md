# v4 judging, Opus 5 round — 2026-09-03

Same prompt/schema/weights as the sonnet round (`tools/judge_prompt_v4.md`), three independent general-purpose subagents, **model opus**. Requested by the PI after the sonnet round; the sonnet reviews are kept in `reviews/v4_sonnet/` for comparison.

## Aggregate
**5.93 — borderline** (nov 5.0 / sig 5.7 / snd 6.3 / fea 6.3 / cla 8.0). R1 5/6/7/6/8, R2 5/5/6/7/8, R3 5/6/6/6/8.
Sonnet round on the same text: 6.02 (nov 5.3 / sig 6.0 / snd 7.0 / fea 5.0 / cla 6.7). Similar totals, different content: Opus found a design flaw sonnet missed and rated clarity higher, feasibility higher, soundness lower.

## Unanimous (3/3): S is not identified as substitution — headroom / saturation compression
If GEPA works at all (G2 requires it), acc(I1×M0) > acc(I0×M0); the pool of instances memory can still fix is smaller at I1 before memory is injected, so the memory gain shrinks mechanically on a bounded scale. S ≥ 0.6 can be recorded with zero information transferred between containers. Fix/break decomposition, I3 (length) and B-dup (leakage-sized effect) do not separate the two mechanisms. All three name the same missing arm: an **accuracy-matched, information-disjoint instruction** (GEPA on a disjoint episode pool, or a titrated hand-written instruction) at which memory's gain is re-measured; plus headroom-normalized S (error-reduction or logit scale, conditional on remaining errors).

## Other objections
| Objection | Who | Status for v4.2 |
|---|---|---|
| 120B out of scope; in-scope agent pre-declared null | R1(d), R2(d), R3 | already fixed in v4.1 (screening) |
| TOST ±4pt and S≥0.6 are misaligned (H2 passes at S≈0.48) | R2 | replace with a ratio CI on the identified quantity |
| Supervision asymmetry: bank from solved episodes only, reflector sees failures | R2 | B_rb (success+failure) is primary-eligible; both formats screened |
| Denominator selection / regression to mean; no branch for S_test denominator < gate | R2, R3 | denominator estimated on S_test; pre-registered branch |
| Gates at n=150 sit below the documented noise floor | R1, R3 | S_dev → 300, CI-based gate |
| I1×C (optimized instruction + compiled block) never measured, the recommended deployment | R1, R3 | added |
| I2 under-seeded; numerator should use best memory-fair instruction | R1 | I2 to 4 seeds (n=500), S reported with both |
| Positive control is leakage-sized; need a graded control at 3–8pt | R1, R2 | graded: 10% near-duplicates diluted into the ordinary bank |
| Bank side gets no search budget while GEPA gets 1,400 rollouts | R3 | B_tuned: k/dedup/format tuned on S_dev with one run's budget |
| "Token-matched per instance" is undefined for a static block | R2 | C fixed at median M1 injection length; comparator padded |
| MIPROv2 instruction-vs-demonstration ablations are the older framing collision; add an optimized static demo set | R1 | cite as prior on S; D_opt arm Tier 2 |
| Re-measure a published memory result under the protocol | R2 | refused: targets' settings (WebArena etc.) not reproducible here; the paper audits the evaluation template, not a number |
| EvoAgentBench absence claim rests on snippets; list the 15 queries; state which table was inspected | R1, R2, R3 | queries listed in litscan; absence claim qualified; PDF check requested from the PI (node cannot open arXiv) |

## Design decision for v4.2: crossover identification
Split the training pool into two disjoint halves a/b. Build B_a and B_b (same format, same size) and optimize I1a(s), I1b(s) with the same seeds. At the **same instruction and the same instances**, compare the gain of the bank whose episodes the instruction was optimized on ("own") against the gain of the other half's bank ("other"). Headroom is identical by construction; the optimizer-seed variance that dominated the old S cancels within instruction; the bank-half content difference cancels across the crossover. Primary quantity: S_info = 1 − g(own)/g(other). The old S (vs I0) is kept as the descriptive headline with a headroom-normalized version alongside.
