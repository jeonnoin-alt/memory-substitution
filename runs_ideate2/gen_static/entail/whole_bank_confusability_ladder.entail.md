=== ENTAILMENT CHECK (automated pre-review; evidence, not a verdict) ===
For each prediction: what would falsify it, and whether the stated arms can produce that outcome at the stated power.

Proposal: whole_bank_confusability_ladder — headline P4 is **entailed**; open 3 / entailed 1 / near-entailed 1 / unresolvable 1; verdict revise

- P1 [open] falsifier: WB(R-80) or WB(F-80) at least 8 net below WB(S6) on the paired cells.
  reason: Plain long-context degradation of an 80-item prefix is an outcome nothing in the design precludes and a drop past the +/-8 floor would be visible on paired cells, though the 8-net falsifier and the 9-net confirmatory bar leave an 8-to-9 dead band.
- P2 [open] falsifier: WB(N-80) within +/-8 of WB(N-6), or a decline not accompanied by a rise in twin-procedure errors.
  reason: Flatness on the N ladder and a generic length-failure error signature are both attainable, and the conjunctive falsifier (success drop AND error-signature rise) makes falsification easier rather than harder.
- P3 [near_entailed] falsifier: RET(N-48) within +/-8 of RET(R-48), or RET declining with size at fixed share.
  reason: Twins are built to share exactly the object and receptacle words the goal-sentence retriever scores on while carrying the wrong procedure, and the run is pre-gated on wrong-type exemplars already costing at least 8 net, so RET(N-48) below RET(R-48) re-describes the pool construction plus the gate; the falsifier survives only through the retriever failing to rank twins highly, which is never logged or controlled.
  fix: Log the type composition of the retrieved top-3 (twin-retrieval rate) per cell and add a type-conditioned retrieval arm on the N ladder, so the prediction is about retriever behaviour rather than about the twin construction the bank guarantees.
- P4 [entailed] falsifier: the two routes decline by the same amount (within 8 net) on the N ladder.
  reason: P4's estimand is arithmetically P2's WB decline minus P3's RET decline over identical measured cells, so once P2 asserts the WB term is at or below -9 and P3 asserts the RET term is within +/-8, the interaction is pinned at or below -9 and no independent outcome can contradict it.
  fix: Estimate the route x composition interaction on cells not used by P2/P3 (for example the R-ladder route difference as the comparison contrast, or a second independent bank draw per size), or drop P4 as a restatement.
- P5 [unresolvable] falsifier: 8B crosses at the same size as or later than 32B, or 8B shows no crossover while 32B does.
  reason: Crossover is a threshold placed exactly at the +/-8 noise floor with no interval on the crossing size, the two readers are compared on different size grids (an 8B crossover at 24 is unobservable and would be recorded as 48), and the pre-registered escape clause converts the commonest falsifying outcome into uninformative.
  fix: Run 8B on the same 12/24/48/80 grid, define crossover with a paired-bootstrap interval on WB minus RET at the confirmatory 9-net margin rather than at the floor, and add seeds so the crossing size itself carries a CI.
- P6 [open] falsifier: WB(U-80) at least 8 net below Measurement A k=3.
  reason: A uniformly random 80-subset carries a natural near-miss share that, on the proposal's own mechanism, could push WB well below the full-pool retrieval number, so the falsifier is reachable and visible past the +/-8 floor, although only the below-direction is stated as falsifying.
- shared terms: P1-P2: WB(S6) is the same measured cell as WB(N-6), so a low seed cell simultaneously widens P1's flat band and shrinks P2's asserted decline.; P2-P4: WB(N-80) and WB(N-6) are the identical measured cells in both; P4 is P2's estimand minus P3's.; P3-P4: RET(N-80) and RET(N-12) are the identical measured cells in both; P3's asserted null pins P4 to P2's value.; P2-P5, P3-P5: the 32B crossover in P5 is read off the same WB and RET N-48/N-80 cells used by P2, P3 and P4.; P6-baselines: Measurement A k=3 is both P6's comparator and the normalizer against which every retrieval number in the proposal is reported.
