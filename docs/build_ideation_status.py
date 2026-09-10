#!/usr/bin/env python3
"""Regenerate docs/ideation_status.html from the runs_ideate2 state (three-topic ideation run).

Usage: python docs/build_ideation_status.py [--sim scratch/ideas_summary.json]
Keeps the existing <head>/CSS of docs/ideation_status.html and rebuilds the body from:
  runs_ideate2/gen_<topic>/ideas_final.json      titles
  runs_ideate2/gen_<topic>/review/RANKING.json    Opus scores (all rounds folded in)
  runs_ideate2/gen_<topic>/review/<idea>/r1.json  first judge's strongest objection
  runs_ideate2/gen_<topic>/entail*/entail_report.json  latest entailment labels
"""
import json, os, re, sys, html, glob
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "ideation_status.html")
TOPICS = [
    ("credit", "Per-item credit assignment",
     "When a retrieved memory item helps or harms an episode, can you say which item did it, and what does that attribution cost?"),
    ("xfer", "Cross-backbone experience transfer",
     "Experience written by one agent, read by another: what travels, what the reader pays, and whether the writer's identity is the variable."),
    ("static", "Retriever versus static prompt",
     "When does a query-time retriever earn its keep over the best prompt you could compile once from the same experience bank?"),
]
LABEL_TIP = {"open": "Falsifier reachable at the stated noise", "near_entailed": "Falsification needs a mechanism the design never names",
             "entailed": "Falsifying outcome cannot occur", "unresolvable": "Decision band inside the stated noise"}
LABEL_SHORT = {"open": "open", "near_entailed": "near", "entailed": "entailed", "unresolvable": "unresolv."}
CLS = {"open": "s-open", "near_entailed": "s-near", "entailed": "s-ent", "unresolvable": "s-unres"}

def load(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return default

def esc(s): return html.escape(str(s), quote=True)

def first_sentence(t, n=230):
    t = re.sub(r"\s+", " ", t or "").strip()
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    s = m.group(1) if m and len(m.group(1)) >= 40 else t
    return (s[: n - 1] + "…") if len(s) > n else s

def latest_entail(g):
    rounds = [d for d in ("entail", "entail_r2", "entail_r3") if os.path.exists(os.path.join(g, d, "entail_report.json"))]
    per = {}
    for d in rounds:
        rep = load(os.path.join(g, d, "entail_report.json"), {})
        items = rep if isinstance(rep, list) else rep.get("ideas", rep.get("results", []))
        if isinstance(rep, dict) and not items:
            items = [v for v in rep.values() if isinstance(v, dict) and "predictions" in v]
        for it in items:
            per[it["name"]] = (d, it)
    return per

def topic_data(topic, sims):
    g = os.path.join(ROOT, "runs_ideate2", f"gen_{topic}")
    ideas = {i["Name"]: i for i in load(os.path.join(g, "ideas_final.json"), [])}
    rank = load(os.path.join(g, "review", "RANKING.json"), [])
    ent = latest_entail(g)
    rows = []
    for r in rank:
        n = r["name"]
        e = ent.get(n)
        labels = [p.get("label", "open") for p in e[1]["predictions"]] if e else []
        counts = {k: labels.count(k) for k in CLS}
        r1 = load(os.path.join(g, "review", n, "r1.json"), {})
        rows.append(dict(name=n, title=ideas.get(n, {}).get("Title", n), score=r["score"], verdict=r["verdict"],
                         n=r["n_reviews"], means=r["means"], escalate=r.get("escalate"),
                         eround=e[0] if e else "", everdict=e[1].get("verdict", "") if e else "",
                         eheadline=e[1].get("headline_status", "") if e else "", counts=counts, npred=len(labels),
                         sim=sims.get(n, 0.0), objection=first_sentence(r1.get("strongest_objection", ""))))
    rows.sort(key=lambda x: -x["score"])
    return rows

def pbar(counts, npred):
    if not npred: return ""
    segs = "".join(f'<i class="{CLS[k]}" style="flex:{counts[k]}"></i>' for k in ("open", "near_entailed", "entailed", "unresolvable") if counts[k])
    return f'<span class="pbar" title="Predictions by label: open / near-entailed / entailed / unresolvable">{segs}<span class="bar-n">{npred}</span></span>'

def idea_li(r):
    v = r["verdict"]
    chip = f'<span class="chip chip-{v}" title="Opus verdict; weighted score novelty .3, significance .25, soundness .25, feasibility .1, clarity .1">{r["score"]:.2f} · {v}</span>'
    nj = f'<span class="nj" title="Number of Opus judges">{r["n"]} judge{"s" if r["n"] > 1 else ""}</span>'
    m = r["means"]
    axes = f'<span class="axes" title="novelty / significance / soundness / feasibility / clarity">{m["novelty"]:.0f}·{m["significance"]:.0f}·{m["soundness"]:.0f}·{m["feasibility"]:.0f}·{m["clarity"]:.0f}</span>'
    eh = r["eheadline"] or "open"
    ent = f'<span class="chip chip-h chip-{eh}" title="Latest entailment check ({r["eround"] or "r1"}): headline prediction is {LABEL_TIP.get(eh, eh)}">{LABEL_SHORT.get(eh, eh)}</span>' if r["eround"] else ""
    rev = {"entail": "r1", "entail_r2": "r2", "entail_r3": "r3"}.get(r["eround"], "")
    revtag = f'<span class="rev" title="Text version that was judged: r1 = original, r2 = one Fable revision, r3 = two">{rev}</span>' if rev else ""
    obj = f'<p class="obj">{esc(r["objection"])}</p>' if r["objection"] else ""
    return (f'<li class="idea"><div class="idea-id"><code>{esc(r["name"])}</code></div><h4>{esc(r["title"])}</h4>{obj}'
            f'<div class="idea-meta">{chip}{nj}{axes}{ent}{pbar(r["counts"], r["npred"])}'
            f'<span class="sim" title="Highest cosine similarity to a paper found by the classed literature search">sim&nbsp;{r["sim"]:.2f}</span>{revtag}</div></li>')

def topic_section(topic, h3, lede, rows):
    nb = sum(r["verdict"] == "borderline" for r in rows); nr = sum(r["verdict"] == "reject" for r in rows)
    esc_n = sum(r["n"] > 1 for r in rows); top = max(r["score"] for r in rows) if rows else 0
    stats = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in
                    [("proposals", len(rows)), ("judged", len(rows)), ("borderline", nb), ("reject", nr), ("escalated", esc_n), ("top score", f"{top:.2f}")])
    return (f'<section class="topic" id="{topic}"><header class="topic-head"><div><p class="eyebrow">Topic · <code>{topic}</code></p><h3>{esc(h3)}</h3>'
            f'<p class="lede">{esc(lede)}</p></div><dl class="topic-stats">{stats}</dl></header><ol class="ideas">' + "".join(idea_li(r) for r in rows) + "</ol></section>")

def main():
    sims = {}
    for a in sys.argv[1:]:
        if a.startswith("--sim="):
            d = load(a[6:], {})
            for t in d.values():
                for it in t: sims[it["name"]] = it.get("sim", 0.0)
    old = open(OUT).read()
    head = old.split('<header class="masthead">')[0]
    extra_css = ('.chip-borderline{background:var(--near-bg);color:var(--near)} .chip-reject{background:var(--unres-bg,#f6e4e4);color:var(--unres)}'
                 '.nj,.axes{font-family:"IBM Plex Mono",monospace;font-size:.68rem;color:var(--muted);font-variant-numeric:tabular-nums}'
                 '.obj{grid-column:1;margin:0;font-size:.86rem;color:var(--muted);line-height:1.45}'
                 '.fn.good .fn-fill{background:var(--accent)}')
    if ".chip-borderline{" not in head:
        head = head.replace("</style>", extra_css + "\n</style>", 1)
    data = {t: topic_data(t, sims) for t, _, _ in TOPICS}
    allrows = [r for rows in data.values() for r in rows]
    n = len(allrows); nb = sum(r["verdict"] == "borderline" for r in allrows); nr = n - nb
    esc_n = sum(r["n"] > 1 for r in allrows); top = max(r["score"] for r in allrows)
    pass_latest = sum(r["everdict"] == "pass" for r in allrows)
    today = date.today().isoformat()
    tops = sorted(allrows, key=lambda r: -r["score"])[:3]
    toplist = ", ".join(f'<code>{esc(r["name"])}</code> ({r["score"]:.2f})' for r in tops)

    body1 = f'''<header class="masthead"><div class="wrap">
<div class="mast-top">
<div><p class="eyebrow">Handoff · memory-substitution</p><h1>Memory Substitution Ideation</h1></div>
<div class="mast-meta"><span>run <b>2026-09-08 → {today[5:].replace("-", "-")}</b></span><span>topics <b>3</b></span><span>proposals <b>{n}</b></span><span>status <b>review done</b></span></div>
</div>
<p class="standfirst">Three research topics were taken through the full ideation pipeline in parallel, producing <strong>{n} experiment proposals</strong> for LLM-agent memory. Every proposal was screened for repackaging, checked against the literature, put through an automated entailment check, revised where a prediction could not fail, and then judged open-book by Opus. <strong>All {n} have a first-round verdict: {nb} borderline, {nr} reject, none accept.</strong> The {esc_n} most promising received two further judges. The ceiling is again about six out of ten; the top three are {toplist}.</p>
<div class="blockers">
<div class="blocker"><h4>Where it stands</h4><p>The judges' recurring objection is the same across all three topics: the headline prediction is either forced by how the experiment was built (a manufactured class, a selection rule, a definitional reference) or its decision band sits inside the stated noise, and the mechanism is usually already in print in an adjacent literature the proposal did not search. Measurement C's paired residual (+17.2 net) contradicted the premise of several static-topic proposals outright.</p></div>
<div class="blocker warn"><h4>Idle · both GPUs</h4><p>Measurement C finished; both A100s are at 0 % utilisation with the vLLM replicas still up. No follow-on GPU job is assigned.</p></div>
</div>
</div></header>
<main>
<section id="pipeline"><div class="wrap">
<div class="sec-head measure"><p class="eyebrow">How it runs</p><h2>One pipeline, three topics, run in parallel</h2>
<p>Each stage is a filter with its own model. Generation and revision run on Fable, every judgement runs on Opus. The stages are ordered because each one consumes the previous one's output.</p></div>
<ol class="rail">
<li><span class="st-n">Stage 0</span><span class="st-name">Literature pre-scan</span><span class="st-note">Five axes per topic, papers carded and synthesised into gaps</span><span class="st-out">182 papers</span></li>
<li><span class="st-n">Stage 1</span><span class="st-name">Brief</span><span class="st-note">Starting numbers, binding rules, open questions, nearest archived ideas; Measurement C folded in before review</span><span class="st-out">3 briefs</span></li>
<li><span class="st-n">Stage 2</span><span class="st-name">Generation</span><span class="st-note">One Fable agent per axis, three proposals each</span><span class="st-out">45 ideas</span></li>
<li><span class="st-n">Stage 2.5</span><span class="st-name">Repackaging gate</span><span class="st-note">Every near pair adjudicated against the brief, the digest and the archive</span><span class="st-out">119 pairs</span></li>
<li><span class="st-n">Stage 2.7</span><span class="st-name">Novelty search</span><span class="st-note">Classed queries, including the mechanism's home vocabulary</span><span class="st-out">45 cards</span></li>
<li><span class="st-n">Stage 2.8</span><span class="st-name">Entailment check</span><span class="st-note">Can each prediction's falsifier actually occur, at the stated noise?</span><span class="st-out">33 revise</span></li>
<li><span class="st-n">Stage 2.9</span><span class="st-name">Revision</span><span class="st-note">Fable rewrites every flagged prediction; re-checked by Opus; at most two passes</span><span class="st-out">33 + 4</span></li>
<li><span class="st-n">Stage 3</span><span class="st-name">Opus review</span><span class="st-note">One open-book judge each, then two more for the promising ones</span><span class="st-out">{n} + {esc_n}×2</span></li>
</ol>
<div class="funnel">
<div class="fn"><span class="fn-lab">generated</span><span class="fn-track"><span class="fn-fill" style="width:100%"><span>45</span></span></span></div>
<div class="fn"><span class="fn-lab">cleared the gate clean</span><span class="fn-track"><span class="fn-fill" style="width:97.8%"><span>44 · 1 flagged duplicate</span></span></span></div>
<div class="fn"><span class="fn-lab">entailment: falsifiable as written</span><span class="fn-track"><span class="fn-fill" style="width:26.7%"><span>12</span></span></span></div>
<div class="fn"><span class="fn-lab">falsifiable after revision</span><span class="fn-track"><span class="fn-fill" style="width:{100*pass_latest/n:.1f}%"><span>{pass_latest} · rest judged with the report attached</span></span></span></div>
<div class="fn good"><span class="fn-lab">judged by Opus</span><span class="fn-track"><span class="fn-fill" style="width:100%"><span>{n}</span></span></span></div>
<div class="fn"><span class="fn-lab">borderline (none accepted)</span><span class="fn-track"><span class="fn-fill" style="width:{100*nb/n:.1f}%"><span>{nb}</span></span></span></div>
<div class="fn"><span class="fn-lab">escalated to three judges</span><span class="fn-track"><span class="fn-fill" style="width:{100*esc_n/n:.1f}%"><span>{esc_n}</span></span></span></div>
</div>
<p class="tnote">Nothing was withdrawn. Revision was capped at two passes; proposals still flagged after that went to review with the latest entailment report attached, so the judges saw the flags.</p>
</div></section>
<section id="check"><div class="wrap">
<div class="sec-head measure"><p class="eyebrow">The filter</p><h2>What the entailment check looks for</h2>
<p>An Opus checker reads every prediction and asks two literal questions: is the falsifying outcome reachable under the arms the proposal actually names, and is it distinguishable at the noise the proposal itself states? Each prediction gets one of four labels; the proposal is sent back if its headline prediction is anything but open.</p></div>
<div class="legend">
<div class="lg lg-open"><b>open</b><span>The falsifier can happen and the design could see it.</span></div>
<div class="lg lg-near"><b>near</b><span>Falsification needs a mechanism the design never names, controls, or measures.</span></div>
<div class="lg lg-ent"><b>entailed</b><span>The falsifying outcome cannot occur. The prediction restates how the experiment was built.</span></div>
<div class="lg lg-unres"><b>unresolv.</b><span>The decision band is narrower than the stated confidence interval.</span></div>
</div>
<p class="tnote">Each proposal below shows its Opus score and verdict, the number of judges, the five axis means (novelty · significance · soundness · feasibility · clarity), the latest entailment headline label, the four-colour prediction bar, the literature similarity, and which text version was judged. The grey line under the title is the first judge's strongest objection.</p>
</div></section>
<section id="topics"><div class="wrap">
<div class="sec-head measure"><p class="eyebrow">The work</p><h2>Forty-five proposals, ranked</h2>
<p>Each topic got a separate literature scan and brief, then five generation axes of three proposals each. Within a topic the proposals are ordered by Opus score. The identifier under every title is the name used in the repository.</p></div>
</div></section>
<div class="wrap">'''
    sections = "".join(topic_section(t, h, l, data[t]) for t, h, l in TOPICS)
    body2 = f'''</div>
<section id="measc"><div class="wrap">
<div class="sec-head measure"><p class="eyebrow">Node result</p><h2>Measurement C: the retrieval residual over the best static prompt</h2>
<p>The cheapest baseline four earlier judges had demanded: a prompt compiled once from the same experience, competing against query-time retrieval. Five arms, 2,740 episodes, ALFWorld with Qwen3-32B, paired per game with the k-sweep already on disk.</p></div>
<div class="tbl-scroll"><table>
<thead><tr><th>Arm</th><th>What it puts in the prompt</th><th class="num">Episodes</th><th class="num">Success</th><th class="num">Seen</th><th class="num">Unseen</th></tr></thead>
<tbody>
<tr class="best"><td class="name">static3</td><td>Three fixed expert exemplars of the task's type</td><td class="num">548</td><td class="num">0.666</td><td class="num">0.664</td><td class="num">0.668</td></tr>
<tr><td class="name">instr_all</td><td>All six task-type procedures, no type selection</td><td class="num">548</td><td class="num">0.637</td><td class="num">0.600</td><td class="num">0.675</td></tr>
<tr><td class="name">static1</td><td>One fixed expert exemplar of the task's type</td><td class="num">548</td><td class="num">0.615</td><td class="num">0.607</td><td class="num">0.623</td></tr>
<tr><td class="name">instr</td><td>One procedure sentence for the task's type</td><td class="num">548</td><td class="num">0.615</td><td class="num">0.582</td><td class="num">0.649</td></tr>
<tr><td class="name">blind1</td><td>One exemplar of the wrong type (length placebo)</td><td class="num">548</td><td class="num">0.513</td><td class="num">0.507</td><td class="num">0.519</td></tr>
</tbody></table></div>
<p class="tnote">Paired per game (2,000-draw game bootstrap): static3 − k0 = +12.4 net [+7.7, +17.3]; <strong>k3 − static3 = +17.2 net [+11.9, +22.4]</strong> (seen +14.3, unseen +20.1; clean +26.7, heat +25.6, cool +19.6, pick types +10 to +12, look-at +4.8 with CI including 0); k7 − static3 = +19.5; k1 − static3 = +9.1; instr_all is 20.1 under k3. This number was written into all three briefs as binding before review, and the judges used it: several static-topic proposals assumed a null residual and were rejected on that basis.</p>
</div></section>
<section id="next"><div class="wrap">
<div class="sec-head measure"><p class="eyebrow">Handover</p><h2>Picking this up</h2>
<p>Everything is committed to the repository. Agent identifiers for every stage are stored next to the outputs, so any stage can be re-collected without re-running it.</p></div>
<ol class="steps">
<li><span class="sn">01</span><div><b>Read the three rankings.</b><p>Each topic has a RANKING.md with the score table and a per-idea directory holding every judge's full JSON: one-line contribution, closest prior work with verified arXiv ids, strongest objection, what would fix it, missing baseline, and the judge's own literature search.</p></div></li>
<li><span class="sn">02</span><div><b>Decide whether anything at about six is worth a draft.</b><p>No proposal was accepted. The pattern matches the earlier v1 to v6 history: soundness and framing improve with revision, novelty does not, because the mechanisms live in adjacent literatures (self-correction blind spots, data valuation, ICL demonstration selection, RAG corruption) that the generators do not search.</p></div></li>
<li><span class="sn">03</span><div><b>If a next round is run, change the brief, not the filter.</b><p>The judges' fixes are concrete and repeated: manipulate the moderator instead of observing it across environments, add the within-class positive control, state margins against the measured +17.2, and search the mechanism's home vocabulary before claiming a gap.</p></div></li>
<li><span class="sn">04</span><div><b>Decide the next GPU job.</b><p>Both A100s have been idle since Measurement C finished. The standing rule is to keep them saturated, so this needs an assignment.</p></div></li>
</ol>
<div class="paths"><h4>Where things live</h4><dl>
<div><dt>runs_ideate2/gen_{{credit,xfer,static}}/review/RANKING.md</dt><dd>Score table per topic; RANKING.json is the machine form; &lt;idea&gt;/r1.json, r2.json, r3.json are the judges' full reviews.</dd></div>
<div><dt>*/ideas_final.json · */entail_final/</dt><dd>The exact text each judge saw and the entailment report that was attached to it.</dd></div>
<div><dt>*/entail*/ENTAIL_REPORT.md · */revise/*.r2.json, *.r3.json</dt><dd>Entailment verdicts per round and the Fable revisions with their change logs.</dd></div>
<div><dt>runs/STEP0_RESULTS.md · runs/static/static_c.jsonl</dt><dd>Measurement C paired analysis and the per-episode rows.</dd></div>
<div><dt>docs/PROPOSAL_HISTORY_v1_v6.md</dt><dd>The earlier single-proposal track, v1 to v6, with every judge round and why each version was sent back.</dd></div>
<div><dt>tools/ideate2/ · docs/build_ideation_status.py</dt><dd>The pipeline, one script per stage, and the generator for this page.</dd></div>
</dl></div>
</div></section>
</main>
<footer><div class="wrap"><span>memory-substitution · ideation run of 2026-09-08 → {today}</span><span>Generation and revision on Fable, all judging on Opus</span></div></footer>
'''
    open(OUT, "w").write(head + body1 + sections + body2)
    print(f"wrote {OUT}: {n} ideas, {nb} borderline, {nr} reject, {esc_n} escalated, top {top:.2f}")

if __name__ == "__main__":
    main()
