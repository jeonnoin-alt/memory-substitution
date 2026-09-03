# Judging constants — verbatim from AI-Scientist-v2/ideate.py (claude5-backend, 2026-09-03)

## REVIEW_SCHEMA

```python
REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "novelty": {"type": "integer", "description": "1-10"},
        "significance": {"type": "integer", "description": "1-10"},
        "soundness": {
            "type": "integer",
            "description": "1-10: would the proposed experiments actually test the claim?",
        },
        "feasibility": {
            "type": "integer",
            "description": "1-10: runnable on an academic budget as described",
        },
        "clarity": {"type": "integer", "description": "1-10"},
        "verdict": {
            "type": "string",
            "enum": ["accept-worthy", "borderline", "reject"],
        },
        "one_line_contribution": {
            "type": "string",
            "description": "The new thing, in one sentence, in your own words. If you cannot state it, say so.",
        },
        "closest_prior_work": {
            "type": "string",
            "description": "The work that most threatens novelty, and why it does or does not.",
        },
        "strongest_objection": {
            "type": "string",
            "description": "The objection most likely to sink this in review.",
        },
        "what_would_fix_it": {"type": "string"},
        "missing_baseline": {
            "type": "string",
            "description": "A baseline a reviewer would demand that the plan omits, or 'none'.",
        },
        "preprint_collision": {
            "type": "string",
            "description": (
                "Judge the proposal's Preprint Collision Check. Is there a recent arXiv "
                "preprint that already makes this claim? Name it if so. If the check is "
                "thin, vague, or reports no searches, say that — an unsearched claim of "
                "novelty is a weakness, not a neutral."
            ),
        },
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
        "preprint_collision",
    ],
    "additionalProperties": False,
```

## REVIEW_SYSTEM

```python
REVIEW_SYSTEM = """You are reviewing a research proposal for {venue}. Review it the way \
```

## REVIEW_USER

```python
REVIEW_USER = """Proposal under review:
```

## SCORE_WEIGHTS

```python
SCORE_WEIGHTS = {
    "novelty": 0.3,
    "significance": 0.25,
    "soundness": 0.25,
    "feasibility": 0.1,
    "clarity": 0.1,
```

## IDEA_FIELDS

```python
IDEA_FIELDS = [
    "Name",
    "Title",
    "Short Hypothesis",
    "Related Work",
    "Abstract",
    "Experiments",
    "Baselines and Ablations",
    "Falsifiable Predictions",
    "Measurement and Noise Control",
    "Preprint Collision Check",
    "Risk Factors and Limitations",
```

