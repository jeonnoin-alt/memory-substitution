# Frontier gold-validation audit — Claude Fable 5 via harness (D6), 2026-08-31
Seeded sample (rng 20260831), judged by the frontier model reading items directly.

## Audit 1 — redaction semantic leakage (25/199 items)
Mechanical G-6 check (exact substring) was 0/199. Semantic judgment on 25 sampled items:
23 clean; 1 SEMANTIC LEAK (item for gold 'Mexican War on Drugs' names the movement as "Mexican Drug War" —
word-order variant defeats the substring check but is the answer); 1 borderline (procedure quotes the
question's unique birthdate identifier for Bob Dylan — no string leak, but identifying for a knowledgeable
model). Estimated semantic leak rate ~4-8% — within the pre-registered <=10% G-6 threshold. PASS, with the
semantic-leak caveat to be reported alongside the mechanical rate.

## Audit 2 — EM scorer validity (15 sampled EM=0 & F1>=0.5 episodes, M1 s11)
15/15 are semantically CORRECT answers penalized by gold formatting inconsistency ('Detroit' vs 'Detroit,
Michigan'; '22,500' vs '22,500 acres'; missing alias lists). Implications, pre-registered V5 reading:
(a) absolute EM understates true accuracy; (b) paired deltas remain internally valid (same scorer, both sides);
(c) the GEPA/MIPRO minibatch gains that came from surface-form rules are largely SCORER ADAPTATION, consistent
with their convergence to the I* ceiling on the full S_test (G1 .543 / MIPRO .548 vs Fs .540, both ns).
