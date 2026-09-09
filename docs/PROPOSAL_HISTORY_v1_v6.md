# Proposal ③ — version history, v1 → v6

**What this is.** The full record of the research proposal the `memory-substitution` repo was built to execute, from its first draft to where it stopped. Thirteen versions were written and eleven were judged. This file exists so that someone picking the work up can see what was tried, what each round of review actually broke, and why the loop is currently paused.

**Repo:** `/home/work/neuro/memory-substitution` (GitHub `jeonnoin-alt/memory-substitution`).
**Proposal texts:** `reference/proposal_v*.md` and `.json`.
**Reviews:** `reviews/v*_opus/`, `reviews/v*_sonnet/`, plus `reference/reviews_v1.md` and `reference/reviews_v3.md`.
**Author briefs:** `tools/author_brief_v5*.md`. **Judge prompts:** `tools/judge_prompt_v*.md`.

---

## 1. The thesis that never changed

> A memory bank and an optimized instruction are two containers for the same training episodes, and published memory gains are measured with the instruction container empty.

Every title from v1 to v6 opens with some form of *"Is your agent's memory just an un-optimized prompt?"* except v3. What changed across thirteen versions was never the question. It was the instrument used to answer it, and every round of review broke the current instrument in the same place.

---

## 2. Version table

Scores are weighted: novelty .3, significance .25, soundness .25, feasibility .1, clarity .1. Aggregation is worst-verdict-wins.

| Version | Date | Score | Verdict | The change |
|---|---|---|---|---|
| v1 | 2026-08 | 6.73 → **6.70** (n=2) | borderline | Original: substitution ratio S, GEPA against an ExpeL bank on the same episodes |
| v2 | 2026-08 | **6.97**; re-judged 2026-09-04 as 7.10 Sonnet / 6.02 Opus | not stored / both borderline | Scoping cuts only; text otherwise identical to v1 |
| v3 | 2026-08 | **5.73** (n=3) | borderline | The "decorative retriever" pivot: every optimizer arm deleted |
| v4 | 2026-09-03 | **6.02** Sonnet / **5.93** Opus | borderline | Back to v2's design with the v1/v3 objections answered |
| v4.1 | 2026-09-03 | not judged | — | Scope fixes: screening over in-scope 27–32B agents, Tier 0/1/2 |
| v4.2 | 2026-09-03 | **6.40** | borderline | Crossover identification: own-bank vs other-half bank at the same instruction |
| v4.3 | 2026-09-03 | **6.05** | borderline | Δ_info becomes the sole confirmatory endpoint |
| v4.4 | 2026-09-04 | **5.83** | borderline | Claim moves from "substitution" to "absorption beyond headroom" |
| v5 | 2026-09-04 | **5.25** | borderline | **Environment changes to ALFWorld**; task-type provenance square |
| v5.1 | 2026-09-04 | **5.57** | borderline | Endpoint becomes a ratio; compute re-costed in calls |
| v5.2 | 2026-09-04 | **5.12** | **reject** | Co-primary endpoint added; TOST; several arms promoted to Tier 0 |
| v5.3 | 2026-09-04 | **4.83** | **reject** | Residual gain joins the confirmatory family; 14-row decision table |
| v6 | 2026-09-07 | **5.23** | **reject** | The cut: partition deleted, primary is a residual with TOST |

**Do not read this column as one series.** v1–v4 were judged by a different model than v4.2 onward. See §5.

---

## 3. Version by version

### v1 — the original
Substitution ratio `S = 1 − [acc(I1×M1) − acc(I1×M0)] / [acc(I0×M1) − acc(I0×M0)]`, predicted to collapse by ≥60 %, with a frozen offline-compiled instruction matching per-instance top-k retrieval at matched tokens.

Scored 6.70 borderline (novelty 6.0 / significance 7.0 / soundness 7.0 / feasibility 6.5 / clarity 7.5).

Two blockers. First, the co-adaptation arm I2 (optimize the instruction *with* memory in context) was cut, and that is the deployed configuration the parent track is named for; one reviewer wrote that an area chair could reasonably call the omission self-serving. Second, the fairness constraint was not enforced: the bank distils all training episodes while the optimizer's rollouts touch only a sample, so a low S could reflect unequal exposure rather than non-substitutability. Both reviewers also asked for a fine-tuning arm as a third container, and flagged citation verifiability after an earlier draft had fabricated five arXiv IDs.

### v2 — the text the repo was built on
Scored **6.97**, the highest number in the lineage. The tooling that produced it did not persist the reviews, so there is no verdict and no per-criterion breakdown for that run.

The actual edit is smaller than it looks: `diff` of v1 and v2 shows the two texts are identical apart from a `changes_made` field. That field records a scoping pass which cut one benchmark, one dataset, one model, **and the I2 arm** — the opposite of what v1's first reviewer asked for — while adding the raw-few-shot control both reviewers had demanded and retracting the five unverifiable IDs.

v2 was re-judged in September under both models with a byte-identical prompt, as a calibration exercise, not a revival. Opus gave it **6.02 borderline** and found collisions v2's own check had missed: Agent Workflow Memory, ACE, Dynamic Cheatsheet, MIPROv2's instruction-vs-demonstration ablations, and ExpeL's own insights-vs-trajectories ablation. Sonnet gave it **7.10**.

### v3 — the pivot that went the wrong way
Every optimizer arm was deleted in response to a "the compiler is doing the work" objection. The primary arm became a frozen subset injected identically for every query, and the headline was a law: retrieval-set overlap predicts whether retrieval is decorative.

Scored **5.73 borderline**. All three reviewers made the same scope objection: the parent track is about coupling memory with prompt optimization, and v3 runs zero optimizer arms. All three also named the same prior work as a partial collision, which the proposal itself conceded.

The repo's own post-mortem is worth quoting, because it is the lesson the later rounds were run under: *"v2 → v3 was over-compliance. Refusing with reasons was never the problem; obeying in the wrong direction was."*

### v4 — the reversion
v2's design with the v1 and v3 objections answered: one training pool feeding both containers with optimizer coverage instrumented, a coverage-matched bank, **I2 reinstated**, fine-tuning as a descriptive third container, whole-bank-in-context, every citation re-verified, and gates re-derived from measured effects.

Scored 6.02 (Sonnet) and 5.93 (Opus), both borderline.

Two blockers dominated. All six judges across both models flagged a **scope violation**: the primary agent sat outside the track's model-size envelope, while the in-scope agent was pre-registered as the regime where the endpoint is undefined. And all three Opus judges showed that **S is not identified**: if the optimizer works at all, the pool of instances memory can still fix is smaller before memory is injected, so the memory gain shrinks mechanically. S ≥ 0.6 can be recorded with zero information transferred between containers.

### v4.1 — not judged
Scope fixes only: a pre-registered screening stage over in-scope agents and two bank formats, the out-of-envelope agent demoted to a scale check, and an explicit Tier 0/1/2 structure. `reviews/v4.1_opus/` is empty.

### v4.2 — the high-water mark
The **crossover identification**. Split the training pool into disjoint halves, build a bank from each, optimize an instruction on each with the same seeds, then at the *same* instruction and the *same* instances compare the gain of the "own" bank against the other half's. Headroom is identical by construction, which kills v4's confound.

Scored **6.40**, the best Opus number in the lineage.

Three blockers. The ratio endpoint was unpowered, with a confidence interval spanning roughly 0.23 to 0.89 at the median scenario and no minimum detectable effect stated. The gate was in the wrong place — set at one instruction while the endpoint is measured at another — so the modal outcome was an undefined primary after 44,000 episodes. And the joint instruction-plus-demonstration optimizer, which is the true prompt-container ceiling, was buried in the lowest tier.

### v4.3 — the endpoint narrows
Δ_info becomes the sole confirmatory endpoint, a new gate is placed at the optimized instruction, full-data arms are promoted, and a supplied PDF corrects a web snippet the proposal had been relying on: the real published effects are +3.6 and +1.2 points, not +7.

Scored **6.05**. Significance fell to 5.0 across all three judges, and clarity dropped: 25 arms, 16 predictions and five test families read as "a program, not a result".

The round-3 finding was design-blocking: **the confirmatory endpoint sits where the phenomenon is least likely to exist.** Δ_info is a difference of two small quantities, the proposal's own priors run from +0.6 to +3.6 points, and the gate needs ≥4 points before the endpoint needs ≥2 more on top. The modal outcome is the fallback branch. Two judges also pointed out that random stratified halves are exchangeable, so the two banks carry near-identical generic content and the endpoint can be zero whether or not substitution is real.

### v4.4 — the claim changes, and the loop reopens
The claim moves from *substitution* to **absorption beyond headroom**: memory's gain at the optimized instruction versus at an accuracy-matched, information-free instruction. The grid is cut from 25 rows to 14.

Scored **5.83 borderline**, and the new blockers were serious enough to reopen the loop under the freeze rule.

All three judges rejected the headroom curve as an identification: the three control instructions are three different interventions, not one curve indexed by accuracy, and two prompts at equal accuracy leave different residual unsolved sets. Two judges named an **off-policy bank confound**: every bank was distilled from episodes run under the bare instruction and injected under the optimized one, so shrinkage is equally explained by staleness. And the 2-point claim threshold sat below the study's own minimum detectable effect, making the result inconclusive at its own threshold by construction.

**This round produced the direction decision.** Three options went to the PI, who chose **A**: move the confirmatory environment to one with recurring procedural structure.

### v5 — ALFWorld
The environment changes to ALFWorld, where published memory effects are 5–15 points rather than 0–4. The identifying instrument becomes a **task-type provenance square**: two disjoint task-type sets, banks and instructions built from each, run in both directions. An on-policy bank is promoted to Tier 0. All model roles become local.

Scored **5.25 borderline**. This is also the first version written by an author agent from a brief rather than by hand.

The blockers were arithmetic. The gate admits a pairing on a 4-point relevance advantage, but the claim threshold requires near-total absorption of something larger, so a true 60–70 % absorption of a 4–6 point advantage lands at 2–3 points, below the study's own detectable effect. The level control was shown not to be information-free with respect to the correction it makes. The compute arithmetic was wrong by a factor of 2–3. And the chosen partition splits near-isomorphic task types, which maximizes cross-type transfer and minimizes the very advantage the gate needs.

### v5.1 — the only rise
The endpoint becomes a ratio, the level control is replaced, the missing arms are added, and compute is re-costed in calls.

Scored **5.57**, the only increase after v4.2. No judge re-raised the ratio endpoint, the new level control, the compute arithmetic or any of the added arms, and all three praised the collision check in unusually strong terms.

The new blocker was unanimous and design-blocking: **the denominator is not neutral.** The comparison instruction is optimized on the *other* task types, so it does not merely perform worse, it actively pushes the wrong procedure. The own-type bank then repairs that damage, and the repair is scored as relevance advantage — inflating the endpoint with zero content transfer. One gate made it worse by *requiring* the comparison instruction to be worse. The clean denominator was already being measured in row 1 and never used.

Two pre-2026 collisions were also supplied by a reviewer that the recency-weighted literature scan could not have caught.

### v5.2 — declared frozen, then judged, then rejected
A co-primary endpoint using the clean denominator is added, several arms are promoted to Tier 0, and one prediction becomes an equivalence test.

Scored **5.12 — reject**. Novelty fell to **4.0**.

There is a process lesson attached to this version. v5.2 had been declared frozen *without* judging, on a reading of the freeze rule. The PI challenged that, the round was run, and it failed. Judging costs no credits on this setup, so skipping it was wrong on its own terms.

The blockers: all three judges showed that **the confirmatory endpoint does not test the title.** The quantity being measured is the bank's task-type *discriminability*, not its value, so the endpoint can pass while the bank still adds 4–6 points over no memory at the very instruction in question — the paper's own question answered "no" while the pre-registered bar reads *pass*. The pre-registration also contradicted itself, one gate conditioned the denominator on the same test set that computes the endpoint, and the new co-primary traded one bias for another whose floor was at or above the bound it had to clear.

From here on, **novelty is the binding ceiling and no further design round moves it.**

### v5.3 — the low point
The residual gain joins the confirmatory family as a conjunction, a 14-row decision truth table maps every outcome to one of six pre-registered titles, and the ExpeL concession is made explicit.

Scored **4.83 — reject**, the lineage low. Feasibility 4.7 and clarity 5.0 are both the worst recorded.

No judge re-raised the truth table, the gate fix, the residual gain or the concession, and soundness held. The blockers were about where the power went: the study is **powered where it is not novel and under-powered where it is**. The rows carrying what prior work already publishes run at full sample; the three arms carrying the new identification are all descriptive. And the retrieval budget k was pinned across instructions of very different lengths, while the program's own headline prior is that **injection volume, not memory content, was the causal lever** — so the study risked printing its headline title for a budget artifact.

### v6 — the cut
The task-type partition is deleted entirely, and with it the ratio apparatus, three denominators and the truth table. The primary becomes the residual memory value at an episode-disjoint, level-matched optimized instruction, tested for equivalence to zero. The retrieval budget is re-tuned per instruction. The grid drops from 20 Tier-0 rows to 9, and the compute from ~57k episodes to ~38k.

Scored **5.23 — reject**. Against v5.3: feasibility **+2.0**, clarity **+2.0**, soundness, significance and novelty all **flat**. The cut bought exactly what the calibration predicted and nothing else.

The blockers: all three judges showed the confirmatory family is **arithmetically unlikely to fire** — the equivalence branch is declarable only at a tighter bound than the priors allow, and the other branch is powered at 4 points but thresholded at 3, so the modal outcome is two intervals and no claim. The new comparator is confounded with optimizer maturity: an early snapshot matched only on accuracy is thinner and less specific, so a larger residual there is explained by "less instruction leaves more for the bank to say." And the per-instruction budget tuning was done at sample sizes where the selection is noise.

**The finding that reframes the whole thesis** came from the second judge: **ExpeL's own published table already contains the joint cell.** Full system 59 % versus insights-only 50 % on ALFWorld *is* the residual value of the retrieval container at an instruction-shaped container written from the same pool — **+9 points, not ≈ 0.** The "unpublished number" v6 was built to produce is published, and its published value contradicts the hypothesis. The honest question becomes *how much a search optimizer reduces that residual* — a retention ratio, not equivalence to zero.

Per PI instruction the loop then **paused**. The next version, if any, is v7.

---

## 4. Direction changes

1. **v2 → v3** — the decorative-retriever pivot. All optimizer arms deleted. Cost 1.24 points, diagnosed as over-compliance.
2. **v3 → v4** — the reversion to the substitution core.
3. **v4 → v4.1** — primary agent moved inside the track's model-size envelope.
4. **v4 → v4.2** — identification changes from the substitution ratio to the crossover, because the ratio was shown not to identify substitution.
5. **v4.3 → v4.4** — the claim changes from "substitution" to "absorption beyond headroom."
6. **v4.4 → v5** — **the environment change, decided by the PI.** Reviewers had said for three rounds running that on mid-size agents in multi-hop QA the effect sits at the noise floor and no amount of design will change that. Confirmatory work moves to ALFWorld.
7. **v5 → v5.1** — endpoint changes from a difference to a ratio.
8. **v5.2 → v5.3** — the absorbed share alone was shown not to test the title, so the residual gain joins as a conjunction.
9. **v5.3 → v6** — the partition and every ratio built on it are deleted; provenance is re-operationalized as same-distribution, disjoint-episodes.
10. **After v6** — paused. The pending reframe is the retention ratio against ExpeL's published +9 points.

---

## 5. Judging protocol, and a warning about the score column

| Phase | Judges | Model | Substrate | Books |
|---|---|---|---|---|
| v1 | 2 | see caveat below | `ideate.py`, API | closed |
| v2 | not stored | see caveat | API | closed |
| v3 | 3 | see caveat | API | closed |
| v4 | 3 + 3 | **Sonnet and Opus on the same text** | harness subagents | closed |
| v4.1 | 0 — not judged | — | — | — |
| v4.2 → v5.3 | 3 per round | **Opus only** | harness subagents | closed |
| v6 | **1 first, +2 after it came back borderline** | Opus (author: Fable 5.1) | harness | **open — WebSearch, told to verify IDs and hunt collisions** |

Constant throughout: the same review system prompt, schema and user template verbatim from `ideate.py`; venue "ICLR 2027 main track"; the weights above; worst-verdict-wins; judging on the 11 idea fields only, with the decision log as context rather than judged material.

**Caveat on v1–v3.** `reference/reviews_v1.md` records the judge model as `claude-opus-5`, while the later Sonnet control describes v1–v4 as "the lineage's Sonnet-era numbers." The repo contradicts itself and the files do not settle it.

**Why the series is Opus-only from v4.2 on.** The same v2 text scored 6.97 on the API, 7.10 on the harness under Sonnet, and 6.02 on the harness under Opus. The harness reproduces the API to within 0.13, so **the judge model is the cause, not the substrate**. The gap is 1.08 on v2 but 0.09 on v4 and is concentrated in soundness, so it cannot be applied as a single offset.

**The clean Opus-only series:** v2 6.02, v4 5.93, v4.2 6.40, v4.3 6.05, v4.4 5.83, v5 5.25, v5.1 5.57, v5.2 5.12, v5.3 4.83, v6 5.23.

**Author side:** v1–v3 by `ideate.py`; v4–v4.4 by Claude Code; v5–v5.3 by an Opus author agent driven from a brief; v6 by Fable 5.1 directly with no brief.

**The freeze rule (freeze after round 3 with round-3 blockers resolved) was applied and repeatedly overridden** — v4.3 was the "resolution text" until v4.4's round produced new design-blocking findings; v5.1 was "for the record" and produced a new blocker; v5.2 was declared frozen without judging and then failed when judged.

---

## 6. The arc

**What the score did.** The Opus-only series plateaued near 6 for four rounds and then declined. Comparing v2 against v5.3, Opus against Opus:

| criterion | v2 | v5.3 | Δ | weighted Δ |
|---|---|---|---|---|
| novelty | 5.3 | 4.0 | −1.3 | −0.39 |
| significance | 6.3 | 5.0 | −1.3 | −0.33 |
| **soundness** | 5.3 | **5.7** | **+0.4** | **+0.10** |
| feasibility | 7.0 | 4.7 | −2.3 | −0.23 |
| clarity | 8.0 | 5.0 | −3.0 | −0.30 |

**Soundness is the only criterion that improved across eight rounds of work.** Clarity and feasibility together lost nearly as much as novelty did. The judge prompt grew from 36 KB to 153 KB. v6's cut recovered exactly feasibility +2.0 and clarity +2.0 and moved nothing else — which is the cleanest evidence in the record that the decline was a complexity cost, not a substance one.

**Three recurring blocker families.**

1. **Identification, solved and re-broken every round.** Each round the reviewers accepted the previous fix and found the next gap in the same place: the ratio is confounded by headroom → the crossover's halves are exchangeable → the headroom curve is three different interventions → the level ladder is not information-free → the denominator is mis-specified rather than merely lower → the endpoint measures discriminability rather than value → the threshold sits inside the inconclusive band → the new comparator is confounded with optimizer maturity. The v4.4 summary named it at the time: *"each round removes the previous round's objection and the reviewers find the next identification gap. That pattern is itself a finding about the proposal."*

2. **Effect size against the noise floor.** The program's own priors put the quantity being decomposed at or below the minimum detectable effect. Moving to ALFWorld raised the effect but never enough; v6's confirmatory family is still arithmetically unlikely to fire.

3. **Novelty, the binding ceiling from v5.2 on — 4.0, unanimous, three rounds running.** The collisions were mostly conceded by the proposal itself, and the disclosure was repeatedly praised. The v2 calibration is the uncomfortable part: v2 scored 1.3 novelty points *higher* while carrying *more* undisclosed collisions. The gap is largely the price of disclosure, not a difference in originality.

**One control four independent judges asked for across two rounds and never got:** an arm on the retrieval budget k — the program's own measured lever, since injection volume rather than memory content was what mattered in its prior work. It was finally added in v6, where it immediately became a selection-noise objection instead.

---

## 7. Where it stands

- `DESIGN.md` still reads *"DESIGN v1 — Proposal ③ v5.2 (frozen text). This file is the single authority"*, written 2026-09-04. It was never hashed into `prereg/FREEZE.sha256`, because that is gated on a literature search that every version from v4.3 to v6 records as **unrun**.
- `README.md`'s status log also stops at v5.2 and does not reflect v5.3 or v6.
- The loop is **paused** by PI instruction. Per the PI, only a major bump would justify a v7.
- If a v7 is ever written, the record says what it would have to do: drop equivalence-to-zero and make the **retention ratio against ExpeL's published +9 points** the primary, fix the comparator's maturity confound, and stop selecting the retrieval budget at sample sizes where the selection is noise.

**What replaced it.** The program moved to a different mode of work: instead of iterating one proposal against judges, an ideation pipeline now generates and screens proposals in batches. Three topics are in flight — per-item credit assignment, cross-backbone experience transfer, and retriever versus static prompt — with 45 proposals produced and screened. See `docs/ideation_status.html` and `tools/ideate2/DESIGN.md`.
