#!/usr/bin/env python3
"""Build one harness judge prompt per ideation-pool idea, using ideate.py's own REVIEW_SYSTEM /
REVIEW_SCHEMA / REVIEW_USER and the idea's own research-area brief. Same construction as
build_judge_prompt.py, so the resulting scores are comparable to the v2/v5.x rounds.
Ideas are deduplicated by Name, keeping the longest (most complete) version across pools."""
import sys, os, json, glob
sys.path.insert(0, "/home/work/neuro/AI-Scientist-v2")
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-dummy-for-construction")
import ideate  # noqa: E402

R = "/home/work/neuro/memory-substitution"
B = "/home/work/neuro/AI-Scientist-v2/ai_scientist/ideas/"
VENUE = "ICLR 2027 main track"
POOLS = [("agent_memory_optimizer_reviews.json", "agent_memory_optimizer.md"),
         ("agent_memory_v2_reviews.json", "agent_memory_optimizer.md"),
         ("agent_memory_top4_reviews.json", "agent_memory_optimizer.md"),
         ("transferable_prompt_optimization_reviews.json", "transferable_prompt_optimization.md"),
         ("transferable_prompt_optimization_rev_reviews.json", "transferable_prompt_optimization.md")]

best = {}
for f, brief in POOLS:
    p = B + f
    if not os.path.exists(p):
        continue
    for e in json.load(open(p)).get("scored", []):
        idea = e["idea"]; nm = idea.get("Name")
        size = len(json.dumps(idea))
        rec = {"idea": idea, "brief": brief, "pool": f,
               "sonnet_score": e.get("aggregate", {}).get("score"),
               "sonnet_verdict": e.get("aggregate", {}).get("verdict"), "size": size}
        if nm not in best or size > best[nm]["size"]:
            if nm in best:   # keep the earlier (higher) sonnet score alongside if this is a revision
                rec["sonnet_score_other"] = best[nm]["sonnet_score"]
            best[nm] = rec

index = {}
for nm, rec in sorted(best.items()):
    fields = {k: rec["idea"].get(k, "") for k in ideate.IDEA_FIELDS}
    missing = [k for k, v in fields.items() if not v]
    json.dump(fields, open(f"{R}/reference/ideation/{nm}.json", "w"), indent=1, ensure_ascii=False)
    brief = open(B + rec["brief"]).read()
    prompt = f"""You are one of three independent reviewers. Read everything below, then output ONLY a single JSON object that validates against the schema — no prose before or after, no markdown fences.

=== SYSTEM ===
{ideate.REVIEW_SYSTEM.format(venue=VENUE)}

=== OUTPUT SCHEMA (return ONLY JSON matching this) ===
{json.dumps(ideate.REVIEW_SCHEMA, indent=1)}

=== USER ===
{ideate.REVIEW_USER.format(idea_json=json.dumps(fields, indent=1, ensure_ascii=False), brief=brief)}
"""
    open(f"{R}/tools/ideation_prompts/{nm}.md", "w").write(prompt)
    os.makedirs(f"{R}/reviews/ideation/{nm}_opus", exist_ok=True)
    index[nm] = {"title": fields["Title"], "pool": rec["pool"], "brief": rec["brief"],
                 "sonnet_score": rec["sonnet_score"], "sonnet_verdict": rec["sonnet_verdict"],
                 "prompt_chars": len(prompt), "missing_fields": missing}
json.dump(index, open(f"{R}/reference/ideation/INDEX.json", "w"), indent=1, ensure_ascii=False)
print(f"{len(index)} ideas -> tools/ideation_prompts/")
for nm, v in sorted(index.items(), key=lambda kv: -(kv[1]["sonnet_score"] or 0)):
    print(f"  {v['sonnet_score']:>5} {nm:<52s} {v['prompt_chars']//1000:>3d}KB" + (f"  MISSING {v['missing_fields']}" if v["missing_fields"] else ""))
