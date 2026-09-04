#!/usr/bin/env python3
"""Build the harness judge prompt for a proposal version from ideate.py's constants.
Usage (inside AI-Scientist-v2's venv): build_judge_prompt.py v5  -> tools/judge_prompt_v5.md, reference/proposal_v5.json
The judges see only the 11 IDEA_FIELDS (the decision log above the '---' separator is stripped)."""
import sys, os, re, json
sys.path.insert(0, "/home/work/neuro/AI-Scientist-v2")
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-dummy-for-construction")
import ideate  # noqa: E402

R = "/home/work/neuro/memory-substitution"
ver = sys.argv[1]
md = open(f"{R}/reference/proposal_{ver}.md").read()
body = md.split("\n---\n", 1)[1] if "\n---\n" in md else md
fields = {}
for name in ideate.IDEA_FIELDS:
    m = re.search(rf"^## {re.escape(name)}\n+(.*?)(?=^## |\Z)", body, re.S | re.M)
    assert m, f"missing field: {name}"
    fields[name] = m.group(1).strip()
print({k: len(v) for k, v in fields.items()})
json.dump(fields, open(f"{R}/reference/proposal_{ver}.json", "w"), indent=1, ensure_ascii=False)
brief = open(f"{R}/reference/track_brief.md").read()
venue = "ICLR 2027 main track"
prompt = f"""You are one of three independent reviewers. Read everything below, then output ONLY a single JSON object that validates against the schema — no prose before or after, no markdown fences.

=== SYSTEM ===
{ideate.REVIEW_SYSTEM.format(venue=venue)}

=== OUTPUT SCHEMA (return ONLY JSON matching this) ===
{json.dumps(ideate.REVIEW_SCHEMA, indent=1)}

=== USER ===
{ideate.REVIEW_USER.format(idea_json=json.dumps(fields, indent=1, ensure_ascii=False), brief=brief)}
"""
open(f"{R}/tools/judge_prompt_{ver}.md", "w").write(prompt)
os.makedirs(f"{R}/reviews/{ver}_opus", exist_ok=True)
print("prompt chars", len(prompt), "->", f"tools/judge_prompt_{ver}.md")
