# Author brief — write proposal v5.2 (2026-09-04, minimal freeze amendment; NOT a new round)

Same role, rules and constraints as `tools/author_brief_v5.md` and `tools/author_brief_v5.1.md` — read both first.
You are amending **your own v5.1** (`reference/proposal_v5.1.md`) after its Opus round (`reviews/v5.1_opus/SUMMARY.md`,
`r1.json`, `r2.json`, `r3.json`). The design is **freezing on this file**: it will not be judged again inside the
loop, and DESIGN.md (the pre-registration) will be written from it. Therefore: change only what the items below
require, keep every other sentence of v5.1 as it is, and keep Tier 0 within ≈ 3.5 days on 2×A100 at the calls/hour
you already use (state the new total in episodes, calls and hours). Direction A (ALFWorld primary, no API key, local
models only) is unchanged.

## Items (resolve each in a decision-log row 82+ AND in the affected section text)

1. **Denominator neutrality (3/3 — the one new design-blocking finding).** Inner(I_oth) is measured at an instruction
   mis-specified for own-type games; B_own repairs the mis-specification and the repair inflates A. Do all of:
   (a) Pre-register **A0 = 1 − Inner(I_own)/Inner(I0\*)** as a **co-primary** endpoint from the cells already in rows 1
   and 2 (no new cost), with the same 0.5 / lower-bound-0.2 rule, and state that the absorption claim requires A and
   A0 to **agree** (both pass, or the paper reports the disagreement as the finding).
   (b) Pre-register the **denominator-inflation check**: if Inner(I_oth) exceeds Inner(I0\*) by more than a stated
   margin (choose it from your own SE arithmetic, e.g. > 1.5 × SE of the difference and > 2pt), A is declared not
   interpretable as absorption and A0 is the reported number.
   (c) Pre-register the **item-level diagnostic**: the share of games that B_own fixes at I_oth which I0\* (M0) already
   solves; state the rule that turns that share into "repair of mis-specification" versus "absorption".
   (d) Add **I_all × {B_own, B_oth}** at Tier 0 (n = 800, 2 optimizer seeds — I_all is already built for the pooled
   row), giving A_all = 1 − Inner(I_own)/Inner(I_all) as the third, optimizer-exposed but provenance-neutral
   denominator, reported alongside A and A0.
   (e) Revisit G3b: it currently *requires* the mis-specification. Either drop it, or restate it as an instruction-
   provenance main effect measured at the own-type games without a floor that forces I_oth to be harmful, and say why.
   (f) Address R2's internal edge in one paragraph: G3 (Inner(I0\*) ≥ 9pt) together with G1 (help ≥ 5pt) pushes the
   off-type bank toward harm, and a large off term is what Rule M routes to distractor-robustness. State how the two
   rules coexist (e.g. Rule M is applied to ΔInner between instructions, not to the level of off(I0\*)), or relax G3.
2. **One operational confirmatory bar.** State exactly which statistic gates the confirmatory claim (A and A0 with
   the ratio rule) and demote A_epi/A_type to a pre-registered **secondary decomposition** with its own MDE row: give
   SE(A_epi) from row 4's n and seed count, and either (i) raise row 4 to the scale that makes the 0.2 lower bound
   testable, funding it as in item 5, or (ii) keep row 4 as is and state in Predictions that A_epi is reported with a
   CI and not thresholded. Remove the "A − A_h ≥ 0.30" wording if it is not the bar.
3. **Reserve arithmetic.** Fix the allocation table so S_screen is either its own line or drawn from the reserve, not
   both; list the reserve's uses in **priority order** with the game counts each consumes, and state what happens when
   it is exhausted (T_B binds at ≈ 116 games). Do not promise the same games twice.
4. **Partition rationale.** look_at_obj_in_light toggles a desklamp, so "no object state change" is wrong. Keep the
   pre-registered retrieval-overlap criterion as the *only* rule that fixes the split, keep the procedural split as the
   named expected winner, and correct the description (fetch-and-place-or-illuminate vs appliance-operate), or move
   the type and re-derive counts — your choice, stated.
5. **Budget moves.** Move row 13 (I2_own coupling) and row 15 (step control) to Tier 1; use the freed episodes for
   item 1(d) and for **B′_own** (one distillation from P′_train, run at I_own and I_oth, n = 800, 1 seed) so episode
   provenance is manipulated on the bank side too; pre-register its reading (Inner(B′_own) ≈ Inner(B_own) ⇒ the bank
   carries type-level content only). If budget remains, buy the third optimizer seed on row 2; otherwise keep two
   seeds and add one sentence acknowledging that the crossed optimizer-run effect is then not separately estimable
   and the bootstrap is over games with seeds as fixed strata.
6. **Cheap promotions or refusals, each with one reason:** I_type to Tier 0 (it is a hand-written prompt; cost is one
   cell at I_type × {M0, B_own, B_oth}, n = 500) — recommended; M_shuf at I_own and I_oth (n = 500) as the within-domain
   distractor control — recommended, since X_dist is out-of-domain; {C_own, C_oth} × {B_own, B_oth} — Tier 1 with the
   reason that the compile-once arm is a consequence, not the endpoint; R_raw — Tier 1.
7. **Prediction 6.** Replace the "90% CI below 3pt" bound with a pre-registered **equivalence test** (TOST) against a
   stated margin at the n row 5/11 provides, or state the margin the current n can actually support.
8. **"Same episodes" by identity.** State that I_own and B_own are built from the identical episode set (by episode
   id, hashed), that the rollout cap is a consequence of that identity and not a fairness knob, and that Ladder T's
   larger budgets are on P′_train only.
9. **Related Work — two pre-2026 ALFWorld precedents, added (they are verifiable, pre-cutoff papers):** AutoManual
   (arXiv 2405.16247, NeurIPS 2024: interaction-derived rules compiled into a single manual) and AutoGuide (arXiv
   2403.08978: state-aware guidelines extracted from offline experience and retrieved). State plainly that they
   already show, in this environment, that episodic experience can be rewritten as instruction text and that a compiled
   manual competes with retrieval — so prediction 6 is closer to a replication than a surprise — and that neither
   performs the provenance crossover. Add them to the collision check under a "looking back, not only forward" line.
   No other citations.
10. **Refused by constraint, restated:** frontier reflector (no API key; bias direction conservative); official
   valid_seen/valid_unseen stay Tier 1 (they hold 140 + 134 games and cannot carry the n the endpoint needs; state
   that G1's 5–15pt prior came from those splits and the held-out-training-game measurement is therefore the
   bridging assumption, listed in Risk Factors); obligation (2) remains freeze-blocking and unrun — say so.

## Output

Write `/home/work/neuro/memory-substitution/reference/proposal_v5.2.md` in exactly v5.1's structure: the cumulative
decision-log table (rows 1–81 verbatim from v5.1, then rows 82+ for this amendment), a `---` separator, then the 11
`## <field>` sections. Lineage line: append " → v5.1 5.57 (opus) → **v5.2 (this file, frozen)**". Name stays
`memory_or_instruction`. Do not write code. When the file is written, reply with a 10-line summary of what changed
and what you refused — nothing else.
