=== SYSTEM ===
You are reviewing a research proposal for ICLR 2027 main track. Review it the way an experienced, skeptical area chair would: assume it will be rejected unless it earns acceptance, and look for the reason it would be.

Score honestly and use the full range — most submitted ideas are borderline or below, and a 9 means you would fight for it in discussion. Do not reward ambition, fluent writing, or a long experiment list; reward a claim that is new, testable, and actually tested by the plan as written.

Be specific: name the prior work that threatens novelty, name the baseline the plan omits, name the interleaving of results that would make the central claim collapse. "More experiments needed" is not an objection.

This field moves fast, so weigh recency: the work most likely to have scooped a proposal is an arXiv preprint from the last few months, not an indexed paper. Treat the proposal's Preprint Collision Check as part of the submission and judge it — a proposal that claims novelty without having looked for recent preprints has not established novelty.

The proposal is not supposed to contain code. Do not penalize the absence of implementation detail; judge the experimental design.

You have two literature search channels and a novelty card listing the closest candidates an automated search found.
Search channels, in this order: (a) the literature command, which queries Semantic Scholar and HuggingFace
Papers together (HF indexes arXiv within a day, so recency is covered):
  /home/work/neuro/alfworld-env/bin/python /home/work/neuro/memory-substitution/tools/ideate2/s2cli.py search "<query>" [--recent] [--limit N]
  (run it with the Bash tool; `--recent` restricts to the last twelve months; `s2cli.py paper <arXiv id>` verifies an id;
  it may take a few seconds because requests are rate-limited across agents);
(b) WebSearch only when the command returns nothing relevant or when you need section text (limitations, conclusion).
Never use WebFetch (blocked on this node). Report for every query which channel answered it.
Rules for this review: (1) Run at least two searches on the proposal's claimed mechanism, one restricted to the last
twelve months, and at least one on its closest named method. (2) Verify every arXiv ID the proposal relies on for its
novelty argument; say which you verified and which you could not. (3) In "closest_prior_work" name a paper you found
or verified, with its ID; if the strongest threat you know is from memory and you could not verify it, say so and
label it unverified. (4) In "preprint_collision" report the queries you ran and what they returned, with IDs; an empty
search is reported as empty, not as evidence of novelty. (5) If a search finds a paper that already makes the central
claim, say "VERIFIED COLLISION: <id>" as the first words of "preprint_collision"; the aggregate will cap novelty. Score
novelty on what you verified, not on what the proposal asserts.

=== OUTPUT SCHEMA (return ONLY JSON matching this) ===
{
 "type": "object",
 "properties": {
  "novelty": {
   "type": "integer",
   "description": "1-10"
  },
  "significance": {
   "type": "integer",
   "description": "1-10"
  },
  "soundness": {
   "type": "integer",
   "description": "1-10: would the proposed experiments actually test the claim?"
  },
  "feasibility": {
   "type": "integer",
   "description": "1-10: runnable on an academic budget as described"
  },
  "clarity": {
   "type": "integer",
   "description": "1-10"
  },
  "verdict": {
   "type": "string",
   "enum": [
    "accept-worthy",
    "borderline",
    "reject"
   ]
  },
  "one_line_contribution": {
   "type": "string",
   "description": "The new thing, in one sentence, in your own words. If you cannot state it, say so."
  },
  "closest_prior_work": {
   "type": "string",
   "description": "The work that most threatens novelty, and why it does or does not."
  },
  "strongest_objection": {
   "type": "string",
   "description": "The objection most likely to sink this in review."
  },
  "what_would_fix_it": {
   "type": "string"
  },
  "missing_baseline": {
   "type": "string",
   "description": "A baseline a reviewer would demand that the plan omits, or 'none'."
  },
  "preprint_collision": {
   "type": "string",
   "description": "Judge the proposal's Preprint Collision Check. Is there a recent arXiv preprint that already makes this claim? Name it if so. If the check is thin, vague, or reports no searches, say that \u2014 an unsearched claim of novelty is a weakness, not a neutral."
  }
 },
 "required": [
  "novelty",
  "significance",
  "soundness",
  "feasibility",
  "clarity",
  "verdict",
  "one_line_contribution",
  "closest_prior_work",
  "strongest_objection",
  "what_would_fix_it",
  "missing_baseline",
  "preprint_collision"
 ],
 "additionalProperties": false
}

=== USER ===
Proposal under review:

```json
{
 "Name": "context_wins_substrate_conflict",
 "Title": "When Weights and Memory Disagree: Which Substrate an Agent Follows After a Rule Change, Before and After the Environment Says No",
 "Short Hypothesis": "In a hybrid, a conflict between a procedure trained into the weights and a procedure retrieved into context is resolved in favour of the context item, and the resolution survives environmental contradiction: after a manufactured precondition change, weights trained on the new procedure at every dose reachable on this node (2 to 8 epochs, rank 32 to 128, the full target pool) fail to raise the rate at which the agent produces the new step within six actions of its first appliance decision under a stale same-task demonstration by more than 0.4x the gain those same weights produce alone, even after the environment has answered 'Nothing happens.'; the reverse is not symmetric: one fresh item or one rule sentence in context fully repairs stale weights, and stale weights, unlike stale context, do not trap the agent after feedback. Staleness is therefore a property of the context channel, set by the stale fraction of the retrieved set and resolved among items by majority, so the post-shift lever is what is retrieved (a validity filter or eviction), or the rule sentence when the change is known, not retraining.",
 "Related Work": "The compliance trap (arXiv:2607.10608) shows untrained agents adopt task-wrong retrieved memory at the first exposed decision point, recover weakly, and that stronger agents are hurt more; it is the W_none column of this design and never trains the correct procedure into the weights. When Memory Lies (arXiv:2608.04574) conflicts stale spatial memory with contradicting observations on FrozenLake, again without a trained-weights arm; STALE (arXiv:2605.06527) benchmarks whether agents notice invalid personal memories; MemStrata (arXiv:2606.26511) removes 15-40% stale-fact errors in RAG with temporal-validity filtering of retrieval, the non-destructive alternative to eviction that this design realises as C_mix+filter. On the knowledge-injection side, the QA literature already shows that parametric content loses to explicit context at a single answer: arXiv:2506.06485 finds contextual conflict disruptive and internal reliance hard to suppress, CK-PLUG (arXiv:2503.15888) tunes the reliance knob at inference, Establishing Knowledge Preference (arXiv:2407.13048) fine-tunes a parametric-versus-contextual-versus-instruction preference order into a 7B model, Gekhman et al. (arXiv:2405.05904) show fine-tuning learns new facts slowly and raises hallucination, and From Style to Facts (arXiv:2503.05919) maps where fine-tuning injection works at all. Those results concern one answer with no environmental feedback and a few-thousand-example injection; none asks whether a procedure trained to saturation re-asserts itself once the environment contradicts the context item, nor whether a stale parametric procedure traps the agent the way a stale context item does. UniMem (arXiv:2607.26017) consolidates recurring patterns into parameters and keeps sparse tasks episodic, COVE (arXiv:2608.01234) routes between harness and parameter channels under changing environments, and continual-learning-as-retrieval (arXiv:2604.27003) evaluates only non-parametric memory on streams; none runs the disagreement between a consolidated pattern and a fresh or stale episodic item. Faulty consolidation (arXiv:2605.12978), insight governance in verbal RL (arXiv:2606.17591) and Honest Lying (arXiv:2605.29463) document negative transfer and persistent wrong reflections inside the context channel; Do Self-Evolving Agents Forget (arXiv:2605.09315) documents erosion across channels without a head-to-head; interactive ICL from feedback (arXiv:2602.16066) trains models to use corrective feedback but never pits that training against a conflicting retrieved item. In this program, opposite_sided_failure_under_shift (round 2) asserted the definitional version and was rejected; round 1 of this idea carried a stream horse race that the reviewer showed to be the same definitional claim, now removed.",
 "Abstract": "Hybrid memory systems assume that consolidating experience into weights buys robustness and that keeping items in context buys currency; the QA literature already says that a freshly injected fact loses to an explicit sentence in context at the first answer, and the compliance trap says an untrained agent follows a conflicting retrieved trajectory at its first exposed decision. Neither result says what happens after the environment contradicts the context item, nor whether any amount of training on the correct procedure changes the answer. We manufacture the collision on ALFWorld with a wrapper-level precondition (an 'activate' action before heat, cool and clean), regenerate the expert pool under the new rule, and cross a parametric dose ladder (QLoRA on post-rule targets at 2, 4 and 8 epochs and rank 128, plus pre-rule and continually trained weights) with stale, fresh, mixed, decoy and empty retrieved sets at fixed k and tokens, a one-sentence rule statement, and a temporal-validity filter over a mixed bank. The primary estimand is activation within six actions of the first appliance decision, which counts the new step whether it comes before or after 'Nothing happens.'; the entry-point action, which prior work makes nearly a foregone conclusion, is demoted to a manipulation check. The sharp claim is that no reachable dose buys more than 0.4x of its own stand-alone gain against a stale demonstration, that a lone stale item still beats the strongest rung, that within context a stale minority is outvoted but a stale majority is followed, and that the asymmetry is real: stale weights are harmless after feedback where stale context is not. One task type is held out of both targets and bank, every trained student is evaluated memory-free, matched and mismatched, and every arm sits on one cost axis of training GPU-hours plus per-episode tokens. The result decides a routing question no hybrid paper has costed: after a shift, whether the useful lever is the rule sentence, the retrieved set, or retraining, and at what dose, if any, retraining starts to matter.",
 "Experiments": "Environment: ALFWorld train/valid games behind a command wrapper; Qwen3-32B served by vLLM, one replica per A100; wrapper, prompt, temperature and vLLM version pinned. Pre-rule = standard game. Post-rule: heat, cool and clean commands return the native 'Nothing happens.' unless 'activate <receptacle>' was issued for that appliance earlier in the episode; 'activate' is listed among the admissible commands in the prompt and kept there, so post-feedback discovery is possible and the harm metric is not floor-bound; pick_and_place_simple and pick_two_obj are untouched (probe types). Pools: E_pre = the 1,465 expert walkthroughs; E_post = the same walkthroughs with 'activate <receptacle>' inserted before each heat/cool/clean step, verified by replay to success under the post rule. Partition both identically by task id into T targets (55%), B bank (35%), H (10%); the entire pick_cool_then_place type is removed from T and B in both pools (procedure-held-out type) and kept for evaluation only. Evaluation games: in-distribution (ID) shifted types = heat and clean games from valid-seen, valid-unseen and H (~180 games); held-out type = cool games from the same sources (~90); probe = pick-and-place games from the valid splits (~150); exact counts fixed at pre-registration. Weights (QLoRA on Qwen3-32B, targets = T walkthroughs, empty retrieval block in the training prompt): W_none; W_pre = 2 epochs rank 32 on T of E_pre (1.1 GPU-h); post-rule dose ladder on T of E_post: W_post-2 (2 ep, r32, 1.1 GPU-h), W_post-4 (4 ep, r32, 2.2), W_post-8 (8 ep, r32, 4.4), W_post-8r128 (8 ep, rank 128, ~5.5); W_cont = W_pre trained a further 2 ep on T of E_post (1.1). Total training 15.4 GPU-h, run on whichever A100 is not serving during Gate 0 and the W_none phases. Context (k=3, same MiniLM query in every cell, item lengths matched within 5%): C_none; C_pre = B of E_pre; C_post = B of E_post; C_decoy = k=3 items of pick-and-place types from B of E_post, token-matched to C_post (the brief's mismatched-memory condition: length and format without any appliance procedure); C_s = k=3 with s in {1,2} stale items among fresh ones, positions randomized per episode and logged; C_k1 = a single stale item; C_mix = similarity retrieval from the union of B_pre and B_post with per-item timestamps (post-rule items newer), unfiltered, realised stale count logged per episode; C_mix+filter = the same retrieval followed by a temporal-validity filter dropping items dated before the rule change; R = one system-prompt sentence 'You must issue activate <receptacle> before heat, cool or clean.' (~15 tokens); R_placebo = a neutral sentence of the same length. All evaluation under the post rule. Per-episode log: reach (first heat/cool/clean decision with the target object in hand), entry-point action (activate first; appliance action without activate; other), feedback, activation within 6 actions after the entry point (AR@6, primary: counts activation at the entry point and after 'Nothing happens.'), steps to activation, eventual activation, success, tokens. Step 1, Gate 0 on ID types, cells W_none x {C_none, C_pre, C_post} and W_post-2 x C_none at 4 seeds: (0a) AR@6(W_none, C_pre) <= AR@6(W_none, C_none) - 15 (stale context harms after feedback); (0b) AR@6(W_none, C_post) >= AR@6(W_none, C_none) + 25 and entry-point activate >= 60% (context induces the step); (0c) AR@6(W_post-2, C_none) >= AR@6(W_none, C_none) + 25 and entry-point activate >= 60% (weights induce the step); (0d) entry-point spontaneous activate at (W_none, C_none) <= 20% (the shift is real before feedback) while AR@6(W_none, C_none), the post-feedback discovery rate, lies in [15, 60]% (room on both sides); (0e) reach >= 60% in every Gate-0 cell. success(W_none, C_none) is not gated. Pre-registered amendments, each usable once: if the discovery rate is below 15%, the feedback text becomes 'The <receptacle> is not active.' (still not naming the action) and Gate 0 is re-run; if 0a fails with discovery in range, the compliance trap does not reproduce on this shift and the conflict claim is declared untestable here, reporting Gate 0. Step 2, conflict grid on ID types (primary tier, 13,320 episodes): remaining headline cells W_post-2 x C_pre and {W_post-8, W_post-8r128} x {C_none, C_pre} at 4 seeds; W_pre x {C_none, C_pre, C_post} at 3 seeds; R x C_pre for W_none and W_pre at 3 seeds and for W_post-2 at 2 seeds, R x C_none for W_none at 2 seeds; matched-memory cells W_post-2 x C_post at 3 seeds and {W_post-8, W_post-8r128} x C_post at 2 seeds; C_decoy for W_none and W_post-2 at 3 seeds and for W_pre, W_post-8, W_post-8r128 at 2 seeds. Step 3, mechanism tier (11,070 episodes): C_s (s=1,2) and C_k1 for W_none and W_post-8 at 3 seeds; C_mix and C_mix+filter for W_none at 3 seeds and W_post-8 at 2 seeds; R_placebo x C_pre x W_none at 2 seeds; W_post-4 and W_cont x {C_none, C_pre, C_post, C_decoy} at 2 seeds; held-out cool type: {W_none, W_post-8} x {C_none, C_pre, C_post} and R x C_pre x W_none at 3 seeds (~90 games); probe types: {W_none, W_post-8, W_post-8r128} x C_none at 2 seeds (~150 games). Budget: 24,390 episodes; at >= 100 episodes per GPU-hour (two vLLM replicas with >= 8 running sequences each and prefix caching over the shared k=3 prefix) this is ~245 GPU-h, ~5 days wall-clock on both A100s with training overlapped. The rate is measured during Gate 0; if it is below 70 episodes per GPU-hour the pre-registered cut order is probe, W_cont, W_post-4, C_mix at W_post-8, C_k1, then the fourth seed, so that the primary tier is protected. Cost axis: every arm is placed on one plot of training GPU-hours plus per-episode tokens against AR@6 and success under C_pre (the just-shifted state) and under C_post (the refreshed state), with R and the validity filter at ~0 GPU-h.",
 "Baselines and Ablations": "Single-substrate arms at matched cost: (W_none, C_post) all-context fresh; (W_post-e, C_none) all-weights fresh for every rung; and their stale counterparts (W_none, C_pre) and (W_pre, C_none). Missing baseline named by the reviewer: the rule-sentence arm R crossed with C_pre for W_none, W_pre and W_post-2, plus R alone; if R repairs the stale-context cells, the routing answer when the change is known is 'state it', and the Pareto plot says so; R_placebo (same length, no rule) separates the sentence's content from its tokens. Second named baseline: the temporal-validity filter (C_mix+filter, after arXiv:2606.26511) against the unfiltered mixed bank C_mix, so that 'what is retrieved is the lever' is tested against a non-destructive policy and not only against eviction. Placebo: C_decoy (mismatched memory per the brief: other task types, token-matched) for every trained student, showing that any weights effect is not merely ignoring a long prefix; no training-time placebo is needed because no arm trains with a retrieval block. Memory-free evaluation for every trained student: C_none (absent), C_post (matched), C_decoy (mismatched); the privileged-versus-unprivileged gap is reported per rung. P-CD0 is not applicable: there is no context-distillation or on-policy arm, all SFT targets are expert walkthroughs with an empty retrieval block. Positive controls for the dispositional reading are Gate 0b and 0c: context alone and weights alone must each induce the new step at the entry point (>= 60%) before 'context is followed even against weights' is claimed. Ablations: parametric dose ladder W_post-2/4/8/8r128 crossed with C_pre (does any reachable strength protect?); W_cont versus W_post-2 (does old-procedure residue in the weights raise compliance with stale context?); stale-dose rungs s=1,2 and the single-item cell C_k1 (majority versus lone-item resolution, and whether a lone item still beats the strongest rung); the held-out cool type, absent from both targets and bank in both pools, evaluated in the conflict cells with cross-type retrieval; probe types under the strongest rungs to show competence on untouched types is intact before 'no protection' is attributed to the substrate rather than to over-training.",
 "Falsifiable Predictions": "Margins are fractions of E0 = min(Gate-0b effect, Gate-0c effect), each required >= 25 points: non-inferiority 0.4 E0 (>= 10), harm 0.6 E0 (>= 15), superiority 1.0 E0 (>= 25). P1 (headline, context dominance survives feedback): for every post-rule rung e in {2, 4, 8, 8r128}, the protection contrast D_e = AR@6(W_post-e, C_pre) - AR@6(W_none, C_pre) has point estimate <= 10 with 95% CI excluding 25, while AR@6(W_post-e, C_none) >= AR@6(W_none, C_none) + 25; that is, the stale demonstration removes at least 60% of the gain the weights produce alone, even after the environment has said 'Nothing happens.' Falsified if any rung has D_e >= 25 with CI excluding 10 (parametric strength buys protection; the routing conclusion then reads 'retrain to dose e' and the ladder reports the dose at which protection appears). Recovery among entry-point failures (steps to activation) is reported per rung as the mechanism-level secondary, with the selection caveat. P2a (fresh context repairs stale weights): AR@6(W_pre, C_post) >= AR@6(W_none, C_post) - 10 and >= AR@6(W_pre, C_none) + 25. P2b (staleness asymmetry after feedback): AR@6(W_pre, C_none) >= AR@6(W_none, C_none) - 10, i.e. stale weights do not trap the agent after feedback, while by Gate 0a stale context does; falsified if stale weights cost >= 15 on AR@6. P3 (within-context resolution is by majority, and a lone item still beats the weights): with s=1 stale item among three, AR@6 is within 10 of C_post in both W_none and W_post-8; with s=2, AR@6 <= C_post - 15 in both; the protection contrast W_post-8 minus W_none at s=2 is <= 10; in the single-item cell, D = AR@6(W_post-8, C_k1) - AR@6(W_none, C_k1) <= 10. Falsified if s=1 already costs >= 15 (rank or recency, not majority, resolves within-context conflict) or if the k=1 cell shows D >= 25 (the weights beat a lone stale item). P4 (rule sentence beats demonstration within context): AR@6(W_none, R + C_pre) >= AR@6(W_none, C_post) - 10 with entry-point activate >= 60%, and R + C_pre repairs W_pre as well (>= AR@6(W_pre, C_post) - 10); R_placebo is within 10 of C_pre. Falsified if R + C_pre <= AR@6(W_none, C_pre) + 15 (the demonstration overrides the rule, which would make the compliance trap immune to instruction and put the sentence off the Pareto front). P5 (policy realisation on a mixed bank): AR@6(C_mix) is within 10 of the ladder's prediction at C_mix's realised stale-count distribution, and AR@6(C_mix+filter) >= AR@6(C_post) - 10 for both weights arms; falsified if the filter leaves a deficit >= 15 (fewer surviving relevant items cost more than staleness saves) or if C_mix departs from the ladder by >= 15. P6 (residue, secondary): AR@6(W_cont, C_pre) >= AR@6(W_post-2, C_pre) - 10; if W_cont is >= 15 below W_post-2 under C_pre while within 10 of it under C_none, old-procedure residue amplifies compliance (co-dominance), reported as a partial falsification of pure context dominance. Cost is reported, not predicted: the Pareto plot places R (~0 GPU-h, +15 tokens), the validity filter (0 GPU-h, C_mix's tokens), each retraining rung (1.1 to 5.5 GPU-h) and the context arms (+~3k tokens per episode) against AR@6 and success under C_pre and C_post. Round 1's P5, P6 and P7 are removed as entailed, under-powered and arithmetic respectively.",
 "Measurement and Noise Control": "Paired (game, seed) design: every cell on the same games with the same seeds; contrasts as paired differences per 100 episodes; cluster bootstrap over games (2,000 resamples); analysis code and thresholds frozen before the confirmatory run. Noise floor from the brief: a paired cell of 274 games x 2 seeds gives about +/-8 net points at 95%; scaling by 1/sqrt(n): ID cells at 180 games x 3 seeds (540 episodes) give +/-8 on success; AR@6 is analysed on the pairs in which both arms reach the appliance, so with reach >= 60% n >= 324 at 3 seeds (+/-10) and n >= 432 at 4 seeds (+/-9); held-out cool at 90 x 3 gives +/-12 on success and +/-14 on AR@6; probe at 150 x 2 gives +/-11. MDEs stated before confirmation: 10 points on AR@6 for ID cells at 3 seeds, 9 at 4 seeds, 8 net on success, 14 on AR@6 for the held-out type; contrasts below these are reported as unresolved, never as equivalence. Margins are the fractions of E0 given above; no fixed 3-point margin anywhere; if Gate 0 fails after its one amendment the claim is declared untestable. Unconditional AR@6 (non-reach counted as no activation), reach rate, success and tokens are reported for every cell so the selection induced by conditioning on reach is visible; the paired estimate on the intersection of reaching pairs and the unconditional estimate must agree in sign, otherwise the contrast is reported as unresolved. The AR@6 detector is deterministic (activate for the target receptacle at or within 6 actions after the first heat/cool/clean decision with the object in hand), validated on 100 hand-checked episodes before the confirmatory run. Stale-item positions and realised stale counts are randomized per episode with the seed logged; item lengths matched within 5%; the same MiniLM query in all cells; evaluation order interleaved across cells and across both replicas; training seeds, LoRA hyper-parameters and per-rung GPU-hours logged as the cost axis; probe results per rung published alongside P1 so that a rung failing the probe is visibly excluded.",
 "Preprint Collision Check": "All searches via the literature command (s2cli: Semantic Scholar + HuggingFace Papers, both 'ok' this session); WebSearch not used (quota exhausted); WebFetch never used. Round-1 queries retained: Q1 (--recent) 'agent follows stale retrieved memory over fine-tuned knowledge conflict parametric versus contextual after environment rule change' -> 2607.10608, 2606.17591, 2605.18565, 2605.06527, 2601.11653, 2506.06485, 2503.15888; Q2 (--recent) 'self-routing episodic buffer parametric memory consolidation recurring tasks stability plasticity agent stream' -> 2607.26017, 2607.03726, 2606.02461, 2605.31557, 2605.12978, 2605.13438, 2604.27003, 2605.20189; Q3 (--recent) 'knowledge conflict fine-tuned agent versus retrieved memory which wins' -> 2607.10608, 2603.07670, 2601.02151, 2506.06485. New this round, on the knowledge-injection side the reviewer found missing: Q4 (--recent) 'fine-tuned injected knowledge overridden by in-context evidence context dominance recovery after feedback agent' -> 2604.07487 (CLEAR), 2602.16066 (interactive ICL from feedback), 2601.08747 (ACE), 2505.18917, 2503.15888 (CK-PLUG), 2503.09032, 2503.05919 (From Style to Facts): none conflicts a trained procedure with a retrieved item under environmental feedback. Q5 (--recent), on the new headline: 'agent recovery after environment feedback contradicts retrieved memory stale demonstration fine-tuned procedure steps to recovery' -> 2608.24794 (CAFE), 2607.28272 (MemHarness), 2607.19749, 2607.10608, 2606.24595, 2606.17591, 2605.29463 (Honest Lying), 2601.11653: the compliance trap remains nearest and has no trained-weights arm; MemHarness reconstructs retrieved experience with a GRPO-trained policy but does not measure conflict with a parametric procedure. Resolved individually by 'paper <id>' this round: 2407.13048 (Establishing Knowledge Preference: a 7B model fine-tuned on a few thousand generated examples adheres to a knowledge-preference hierarchy), 2606.26511 (Temporal Validity in Retrieval Memory / MemStrata: RAG serves superseded values 15-40% of the time, validity filtering drives it to ~0%), 2405.05904 (fine-tuning on new knowledge is learned slowly and raises hallucination), 2503.15888 (CK-PLUG). The reviewer resolved 2607.10608, 2607.26017, 2608.01234, 2605.09315, 2605.06527, 2506.06485 and 2608.04574. Round 1's stream-only citations (2606.02461, 2603.07392, 2601.03938, 2601.03641, 2605.26097) and 2601.02151 were not individually resolved and are no longer load-bearing, so they are dropped. Verdict: no collision. The QA-side results (2506.06485, 2407.13048, 2405.05904) make the entry-point direction expected, which is why the headline moved to the post-feedback window and the dose ladder, where none of them has a result.",
 "Risk Factors and Limitations": "The shift is a wrapper-level synthetic precondition and one shift type only; an object-renaming shift is not budgeted. The entry-point contrast is close to pre-determined by the QA-side literature and by the compliance trap and is therefore demoted to a manipulation check; the headline is the post-feedback window and the dose ladder, but if 'Nothing happens.' is too weak a signal for any arm the discovery gate fails, the single pre-registered amendment (more informative feedback text) is the only rescue, and a second failure declares the claim untestable on ALFWorld. Conditioning on reach selects episodes; the paired intersection and the unconditional estimate are both reported and must agree in sign, otherwise the contrast is unresolved. The parametric ladder covers doses reachable on this node (2-8 epochs, rank 32-128, ~800 target walkthroughs) and does not include preference training of the kind in arXiv:2407.13048, which fine-tunes the model to rank parametric over contextual knowledge, nor full fine-tuning; 'no reachable dose protects' is a claim about procedure dose, not about every parametric intervention, and a preference-trained arm is the natural next experiment if P1 holds. Over-trained rungs may lose general competence (arXiv:2405.05904); the probe checks this at +/-11 only, so erosion below that is unresolved, and a rung that fails the probe is excluded from the 'no protection' claim rather than counted for it. The held-out cool type is powered at +/-14 on AR@6, so it replicates direction only, and its cross-type retrieval (heat/clean items for cool tasks) makes its context arms weaker than in-distribution ones by construction. The stream horse race of round 1 is removed rather than fixed: recovery time in a live post-shift stream is not measured this round, and the policy-level statement rests on the ladder plus the C_mix/C_mix+filter realisation on a static mixed bank; a stream comparing the validity filter, eviction and retraining at matched cost is the follow-up, and the definitional FIFO-flush prediction is not carried forward. The rule sentence R is an oracle that requires knowing the change; its win would show that stating a known change dominates both levers, which bounds the routing question rather than the mechanism. Context dominance, if found, may be specific to procedures that appear as explicit action sequences in items; guideline-style memories are not tested. The QLoRA rank-128 8-epoch cost is an estimate (+/-30%) and is logged as measured. Only the expert pool is used; the self-rollout variant of the same design is untested this round."
}
```

Research area this was proposed for:

# Title: The Same Experience Pool in Weights and in Context: What Transfers, What It Costs, and Where the Two Substrates Fail

Author: Fable 5.1, 2026-09-07. Stage-1 brief for the ideate2 pipeline, written after the Stage-0 pre-scan on this topic
(5 axes, 79 papers carded from S2 + HF, 26 gaps synthesized; see `digest.md`; no section-level reads this round, the
WebSearch quota was spent on the previous topic) and after Step 0, a measurement pass on this node that replaces the old
pilot's numbers with numbers from the backbone the experiments will actually use (`runs/STEP0_RESULTS.md`).

## Keywords
LLM agents, experience memory, in-context experience, parametric memory, context distillation, on-policy self-distillation,
privileged information, privilege illusion, LoRA, continual adaptation, amortization, cost-matched evaluation, ALFWorld

## TL;DR
An agent's past episodes can be reused two ways: retrieved into the prompt at inference, or trained into the weights. The
2026 literature has dozens of systems on each side and a growing family of hybrids, and the Stage-0 scan finds the same
hole under every axis: almost no paper builds both routes from the same experience pool on the same backbone and reports
them on one cost axis, almost none evaluates the trained student strictly without the memory it was trained with, and the
few memory-free margins that exist are 0.5–3 points without seeds. The program now has a measured starting position on
one node: with an expert pool, in-context retrieval on Qwen3-32B is worth +20 to +33 points on ALFWorld and does not turn
harmful up to k=7, and one epoch of QLoRA on the same pool costs about two GPU-hours. This track asks for the sharp,
falsifiable claim about what moves between the two substrates, at what cost, and where each one breaks.

## Starting position (measured here; not to be rediscovered)
**Measurement A, in-context retrieval on this node** (Qwen3-32B, thinking off, ReAct, expert bank of 1,465 replayed
walkthroughs, MiniLM retrieval on the goal sentence, paired over identical (game, seed), 274 games × 2 seeds per cell):

| split | k=0 | k=1 | k=3 | k=7 | net/100 at k=3 [95 % CI] |
|---|---|---|---|---|---|
| valid_seen | 0.536 | 0.739 | 0.807 | 0.846 | +27.1 [+18.6, +35.6] |
| valid_unseen | 0.549 | 0.776 | 0.869 | 0.877 | +32.1 [+22.9, +41.0] |

- The gain is procedure-bound, not scene-bound: unseen ≈ seen, and it is carried by the three multi-step types
  (clean/heat/cool then place: +39 to +55 net) whose procedure the k=0 agent fails to finish in 30 steps; most fixes
  convert timeouts. This is also the near-duplicate-template concern: same task type ⇒ near-identical procedure in the pool.
- No high-dose harm: k=7 ≥ k=3 ≥ k=1 on both splits, broken counts fall with k. The old pilot's one-sided harm (27B,
  self-built bank, "broke six or seven, fixed none") does not reproduce with an expert pool on this backbone.
- One type nets negative under retrieval: look-at-object-in-light (−4.8 net/100, n=62). It is the only natural harm regime
  on this node and it is small; any harm-side question needs a manufactured regime (see rules).
- Injected tokens: ~140 at k=1, ~430 at k=3, ~1,010 at k=7 per episode.

**Measurement B, parametric route cost** (QLoRA nf4 rank 32 on Qwen3-32B, step-level SFT on the same pool, 8,854 examples
of ~300 tokens): 385 tok/s at batch 4, 31.5 GB peak, 0.8 s per example, one epoch ≈ 2 GPU-hours on one A100; loss fits
the procedure within tens of steps. Serving a trained arm costs one vLLM restart (~3 min). Feasible; accuracy untested.

**In progress:** the agent's own k=0 successes on the 1,465 train tasks are being collected as a second, on-policy pool
(`runs/bank/own_rollouts_train.jsonl`). Every question below must be answerable on both pools, because the expert pool
is off-policy text and the literature's largest parametric gains come from self-generated data.

**Carried over from earlier rounds:** the 2026-08 pilot findings (memory can be one-sidedly harmful at high injection
volume; volume, not content, was the lever; noise of 0.05–0.14 on a headline metric swallowed most claims) and 51 archived
ideas (appendix). Three of the 51 already sit on this topic and were rejected or left borderline; their objections are
binding on the next round (appendix B).

## What the Stage-0 scan says, by axis
1. **Internalization objectives** (39 cards). The objective menu is now large and well studied on math: on-policy
   self-distillation from a privileged teacher (OPSD 2601.18734; π-Distill 2602.04942; OPCD 2602.12275), its repairs for
   multi-turn agents (HERO 2606.11559; SMRC-SD 2608.05219; Skill-SD 2604.10674; SGCD 2606.12634), skill and memory
   internalization on ALFWorld/WebShop (SKILL0 2604.02268; SIRI 2606.02355; PMD 2607.01480; Skill0.5 2605.28424; UCOB
   2606.29502), and context distillation of interaction histories (Experience Distillation 2607.21051: ≥64.8 % of the
   in-context gain retained memory-free, direct SFT 3.8 %). The gap named by every synth: none of them runs the
   keep-it-in-context arm at matched training compute and inference tokens, so "distilling beats RL/SFT" is established and
   "distilling beats context" is not. A multi-iteration study reports progressive collapse, not compounding (2606.04703).
2. **What survives internalization** (26 cards). Two literatures that do not talk to each other: the privilege-illusion
   family (DAPD 2608.01735; DOPD 2606.30626; OP²SD 2608.09228 shows OPSD gains come partly from context-induced teacher
   behaviour, not the reference) and the subliminal-transfer family (2507.14805; steering-vector account 2606.00995; LoRA
   artefact claim 2606.00831 vs natural-language transfer 2603.09517; corridor regularization 2609.01091; unsafe agent
   trajectories 2604.15559). Nobody has asked either question with retrieved agent memory as the privileged information, and
   nobody has run the paired condition "same material kept in context vs distilled" for harm, bias, or conflicting memory
   (compliance trap 2607.10608).
3. **Hybrids and routing** (26 cards). Routers exist (UniMem 2607.26017; COVE 2608.01234; Skill0.5; substrate benchmark
   2608.15008 concludes "no substrate dominates, routing is necessary") and memory-free deployment margins are reported
   (SESA 2607.29468: 1.8–2.2 memory-free, +0.5–1.0 with the bank back). The train-by-infer 2×2 (trained with/without memory
   × deployed with/without) is never reported with seeds; the information-abundance effect (abundant train-time context
   reduces what is encoded parametrically, 2608.12218) is shown only on documents and generic SFT, never on trajectories.
4. **Continual adaptation and shift** (27 cards). Erosion under self-evolution is documented across memory and model
   channels (2605.09315), stability–plasticity is re-framed as a retrieval problem (2604.27003), and benchmarks exist
   (AgentCL 2606.02461; OAKS 2603.07392; SWE-Bench-CL 2507.00014) but each evaluates only non-parametric memories; the
   parametric CL papers (FOREVER 2601.03938; Agent-Dice 2601.03641; self-generated replay 2605.26097) evaluate only weights.
   No paper puts both substrates on one stream with the same backbone and reports forgetting, transfer and recovery time.
5. **Evaluation and cost** (24 cards). Inference tokens of retrieval, reconstruction and guideline compilation are left out
   of accuracy comparisons (ReMe's 8B-with-memory > 14B-memoryless, 2512.10696; MemHarness 2607.28272); training compute of
   internalization is never amortized against memory-free inference; the one amortization analysis is for in-context
   distillation only (2512.02543: break-even after 843 episodes). Reported substrate differences are 1–5 points, usually
   single-seed.

## Rules for every proposal in this round (from 28 judge reviews of the previous round and the three archived objections)
- **Same pool, same backbone, one cost axis.** Every arm is built from one named experience pool (expert or self-rollout,
  both if possible) on Qwen3-32B and reported on a shared axis: training GPU-hours plus per-episode inference tokens, with
  a cumulative-cost curve or an explicit Pareto plot. "Weights beat context" without the context arm is not a finding.
- **Partition the pool.** No item that is an SFT/distillation target may also be a retrievable bank item at evaluation
  (bank pool ≠ target pool); otherwise own-bank vs swapped-bank contrasts measure memorization, not a read policy.
- **Self-distillation control (P-CD0).** Any context-distillation or on-policy arm needs the same objective run with an empty
  retrieval block, because self-training on ALFWorld train tasks is itself a large effect and generation format and
  on-policy-ness are confounded with the retrieved content.
- **Memory-free evaluation is mandatory** for every trained student, with three prompt conditions at test: memory absent,
  matched memory, mismatched memory (other task's items, token-matched). Report the privileged-vs-unprivileged gap.
- **Placebo arms for anything that injects less.** Token-matched and rate-matched decoys (relevance-destroyed, same length)
  at training time and at inference, since volume was the causal lever in the pilot.
- **Power gates tied to the measured effect.** Equivalence margins are pre-registered as a fraction of the effect measured at
  Gate 0, never a fixed 3 points; on this node a paired cell of 274 games × 2 seeds gives about ±8 net points at 95 %, so
  claims below ~6 points need more seeds, the held-out train split, or a manufactured regime. State the minimum detectable
  effect before the confirmatory run; if Gate 0 fails, the claim is declared untestable, not "confirmed by TOST".
- **Positive control for any dispositional claim.** A teacher context known to induce a disposition (e.g. a majority-action
  prior) must be shown to transfer under the same distillation before "X does not transfer" is asserted.
- **No prediction entailed by a definition.** An append-only bank cannot forget; a LoRA trained only on post-shift data
  cannot keep a renamed mapping. Stream designs need a bounded evicting bank, a reset-LoRA arm, and an off-stream capability
  probe that the shift did not relabel.
- **Procedure-held-out split.** Because the in-context gain is procedure-bound, at least one evaluation holds out an entire
  task type from both the bank and the training targets; scene-level "unseen" is not enough.
- **Public data, local models, days not weeks;** pre-registration of thresholds and amendments before the first
  confirmatory run; the noise floor of the setup (paired CI above) is part of the proposal.

## Open questions this track should attack (pick one and make it sharp)
- **Q1 Retained fraction and its cost.** For one pool, build (a) retrieval at k∈{1,3,7}, (b) QLoRA on the pool, (c) context
  distillation from the k=3-conditioned teacher, (d) P-CD0, and evaluate every trained arm memory-free and with memory back.
  What fraction of the +27/+32 in-context gain survives in weights, how does it scale with pool size (10 %, 30 %, 100 % of
  1,465 tasks) and with the procedure-held-out split, and where on the cumulative-cost curve do weights become cheaper
  than ~430 tokens per episode? Must go past `harm_does_not_distill` (asymmetric-filter framing, underpowered) and
  `amortization_horizon_ranking_flip` (8B-vs-14B, different backbones): same backbone, retained fraction as the estimand.
- **Q2 Which objective transfers what, and is the retrieved memory a privilege illusion?** With retrieved episodes as the
  privileged information, compare SFT on trajectories, off-policy context distillation, and on-policy self-distillation
  (reverse-KL to the memory-conditioned teacher) on the same pool; decompose the gain into reference-attributable and
  context-induced parts (OP²SD-style shuffled-memory teacher), and test whether the student's memory-free accuracy tracks
  the teacher's memory-conditioned accuracy or its memory-free one. Prediction must be stated per objective and per task type.
- **Q3 Training-time context dose and context reliance.** Vary k in the prompt during SFT/distillation (0, 1, 3, 7, decoy);
  evaluate with context present, absent, and misleading. Does abundant train-time experience reduce what is encoded
  (2608.12218's information-abundance effect) on agent trajectories, is the optimum intermediate, and does the effect
  reverse on the self-rollout pool? Must differ from `memory_in_the_loop_training_decomposition` by the dose ladder, the
  pool partition, and a training-time decoy arm (its named missing baseline).
- **Q4 Harm and dispositions across substrates.** Only in a manufactured high-harm regime (Gate 0: in-context harm ≥ 6 net
  points, e.g. planted wrong-procedure items or the compliance-trap construction) with a positive control: does the same
  harmful material harm more when distilled than when read, does the entry-propagation-recovery signature change form, and
  does the corridor-regularization defence (2609.01091) have an in-context analogue? Also the subliminal question the field
  left open: do agent-trajectory traits transfer under on-policy distillation, or only under SFT/LoRA?
- **Q5 Same stream, both substrates, symmetric design.** A stream with a mid-stream rule change; arms: bounded evicting bank,
  unbounded bank, continual LoRA, reset LoRA, LoRA with self-generated replay; a randomized dose ladder of pre-shift items in
  the retrieved set at fixed k and tokens; off-stream capability probe. The honest hypothesis is "both erode, at different
  rates and with different recovery times"; `opposite_sided_failure_under_shift` was rejected for asserting the definitional
  version.
- **Q6 The memory-free margin and the 2×2.** Trained with/without memory × deployed with/without memory, on both pools, with
  seeds and per-step tokens: is the in-context channel still additive after internalization (SESA's +0.5–1.0), is it
  substitutive, or does training with memory make the memory-free policy worse (the crutch)? Small margins are expected,
  so the proposal must show the design can resolve 2 points.

## In scope
- ALFWorld (primary; 1,465 train tasks, 274 validation games, expert and self-rollout pools already on disk); WebShop or a
  text-game second environment if the claim needs a second domain; public data only.
- Qwen3-32B as agent, teacher and student (QLoRA rank 32 fits one A100); other local models only as a robustness check.
- Reimplementation of one published objective per family (OPSD/OPCD, Experience Distillation, SIRI-style skill
  internalization) as named baselines; null results when the measurement makes the null informative.

## Out of scope
- Frontier-model training; anything with private or clinical data.
- "We routed between memory and weights and the number went up" without the single-substrate arms at matched cost.
- Effects the setup cannot resolve (below the paired CI without a stated plan to shrink it).
- Restating any of the 51 archived ideas (appendix); a proposal near one of them must name the archived idea and state what
  it fixes.

## Resource constraints
Two A100 80GB on one node (not four); vLLM serves one Qwen3-32B replica per GPU; both GPUs must stay busy (a training arm
runs on one GPU while the other serves). Budget per confirmatory cell: 274 games × 2–3 seeds ≈ 550–820 episodes;
one QLoRA epoch on the full pool ≈ 2 GPU-hours (0.2–0.6 h for 10–30 % pools); one distillation arm additionally needs one
teacher pass over the target pool (~1,465 episodes with memory). A full Q1 on one pool is roughly 6 trained arms plus 4
retrieval cells, i.e. two to three days; plan seeds and gates accordingly.

## Appendix A: the 51 ideas already generated in this program (do not restate; differentiate or move on)
Round 1 (27, 3-judge Opus mean, `reviews/ideation/RANKING.md`): memory_item_value_reliability 6.12,
provenance_gap_selection_not_authorship 6.07, compile_dont_retrieve 6.0, memory_or_instruction 5.92,
failure_signature_routing 5.87, collection_policy_coupling_collapse 5.85, instruction_conditioned_complementarity 5.82,
coadaptation_transplant_ccr 5.77, decorative_retriever 5.75, memory_induced_shortcutting 5.72,
memory_vetoes_instruction_slot 5.72, coverage_currency_coupling 5.68, memory_budget_confound 5.63,
substitutes_not_complements 5.47, counterfactual_memory_screening_under_selection_noise 5.45,
memory_dropout_coadaptation 5.45, coverage_selection_division_of_labour 5.4, clause_level_portability 5.38,
commit_then_consult_slot_discipline 5.38, breadth_routed_memory 5.35, playbook_transfer 5.33,
meta_prompt_generalization 5.3, action_prior_imprinting 5.27, optimizer_substitutes_for_memory_scaffold 5.22,
query_agnostic_curation_ceiling 5.18, memory_volume_amplifies_optimizer_curse 5.05, allocation_prior_transfer 5.0.

Round 2 (24, open-book Opus, `runs_ideate2/gen_v2/review/RANKING.md`):
- abstraction_discards_bindings_and_repairs 5.95: scene bindings and failure-to-repair pairs explain when distilled experience beats raw trajectories
- closer_beats_stronger 5.75: consumer-side policy proximity, not builder capability, predicts cross-backbone transfer of shared experience
- model_shaped_instruction_task_shaped_store 5.75: the memory–instruction substitution does not survive a backbone swap
- failure_memory_framing_drag 5.72: cross-episode failure notes induce contextual drag; positive rewriting removes it
- order_randomized_leakage_audit 5.7: memory gains concentrate on tasks with a near-duplicate solved earlier in the stream
- memory_in_the_loop_training_decomposition 5.65: train-by-infer 2×2 with bank swap (crutch / content / read skill)
- optimizer_writes_the_read_policy 5.6: joint instruction–memory gains are carried by evolved clauses governing memory use
- gate_reads_style_not_truth 5.55: planted-record audit of write-time validation
- dormant_is_not_dead 5.45; need_blind_compaction_audit 5.45; stall_triggered_injection 5.45
- amortization_horizon_ranking_flip 5.35: cost definition and horizon decide whether 8B+memory beats 14B
- harm_does_not_distill 5.35: context distillation as an asymmetric filter on agent experience
- stale_true_state_facts_redaction 5.3; state_load_not_length 5.2; memory_surrogate_validity 5.15
- opposite_sided_failure_under_shift 5.05: in-context and parametric experience fail on opposite sides of a shift
- utility_pruning_is_frequency_pruning 4.9; contributor_conflict_not_size 4.85; wrong_action_fraction_dose 4.85;
  cross_episode_drag_content_not_label 4.8; lineage_blast_radius 4.75; coupling_variance_components 4.65;
  retrieved_set_disagreement_gate 4.65

## Appendix B: why the three parametric-axis ideas did not pass (binding objections)
- **harm_does_not_distill.** The equivalence margin (3 points) exceeded the harm being probed (~1.3 points on the held-out
  set), so "harm does not distill" and "harm distills but is invisible" were not separated; the second half of the claim was a
  failure-to-reject read as a null. Missing baseline: P-CD0 (context distillation from an empty-retrieval teacher), without
  which the retained-value fraction is confounded with generation format and on-policy-ness. Closest work: Experience
  Distillation 2607.21051 for the retained-gain half; DAPD 2608.01735 / DOPD 2606.30626 / 2608.05219 for the mechanism half.
- **memory_in_the_loop_training_decomposition.** Bank A items were also SFT targets, so the own-bank vs swapped-bank drop
  measured memorization and the co-adaptation claim was pre-determined. Missing baseline: a training-time relevance-destroyed
  decoy block of matched length, without which "crutch" is confounded with "long irrelevant prefix hurts SFT"; the GRPO arm
  had to be a named published objective (MemHarness reconstruction reward or UCOB). Closest work: UCOB 2606.29502 (credit-aware
  bidirectional self-distillation between skill-conditioned and no-skill prompts, ALFWorld/WebShop) and SESA 2607.29468.
- **opposite_sided_failure_under_shift.** The headline was definitional (an append-only bank cannot forget; a LoRA trained
  only on post-shift data cannot retain a renamed mapping); the stale-fraction regression was observational and collinear with
  probe index and bank size; no probe of a capability the shift did not relabel. Fix demanded: randomized dose ladder of
  pre-shift items at fixed k and tokens, bounded evicting bank, reset-LoRA arm, off-stream probe. Closest work: UniMem
  2607.26017 (contents unverified on either channel) and Do Self-Evolving Agents Forget 2605.09315.


Review it now.

=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: context_wins_substrate_conflict — When Weights and Memory Disagree: Which Substrate an Agent Follows After a Rule Change, and What It Means for Hybrid Memory Under Shift

- arxiv:2608.02508 · 2026-08-10 · preprint · sim 0.61 · hf
  RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
  Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory R
- arxiv:2608.04574 · 2026-08-05 · preprint · sim 0.59 · hf
  When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
  Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake. Using a dynamic FrozenLake testbed, we pair a staleness-detection task with a downstream navigation task across three closed-source models and three open-weight VLMs
- arxiv:2608.15008 · 2026-08-15 · preprint · sim 0.58 · hf
  Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents
  Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and ac
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2601.11653 · 2026-01-15 · preprint · sim 0.55 · hf
  AI Agents Need Memory Control Over More Context
  AI agents are increasingly used in long, multi-turn workflows in both research and enterprise settings. As interactions grow, agent behavior often degrades due to loss of constraint focus, error accumulation, and memory-induced drift. This problem is especially visible in real-world deployments where context evolves, distractions are introduced, and decisions must remain consistent over time. A common practice is to equip agents with persistent memory through transcript replay or retrieval-based
- arxiv:2606.25449 · 2026-07-21 · preprint · sim 0.53 · hf
  Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One
  A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain. We call this brittle memory. The information loss is definitional; the finding is behavioral, and it turns on one thing, whether the memory kept a re-derivation basis (the source) rather than the answer. We
- arxiv:2601.07470 · 2026-01-12 · preprint · sim 0.53 · hf
  Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory
  Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed desi
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.51 · hf
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2605.06527 · 2026-05-07 · preprint · sim 0.49 · hf
  STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?
  Large Language Model (LLM) agents are increasingly expected to maintain coherent, long-term personalized memory, yet current benchmarks primarily measure static fact retrieval, overlooking the ability to revise stored beliefs when new evidence emerges. We identify a critical and underexplored failure mode, Implicit Conflict: a later observation invalidates an earlier memory without explicit negation, requiring contextual inference and commonsense reasoning to detect. To rigorously evaluate this 
- arxiv:2606.25161 · 2026-06-23 · preprint · sim 0.49 · hf
  TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory
  Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content. Once stored, such errors become persistent system-state failures that can affect future reasoning and generation. In

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.

