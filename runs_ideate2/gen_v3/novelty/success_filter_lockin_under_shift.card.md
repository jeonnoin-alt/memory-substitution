=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: success_filter_lockin_under_shift — Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights

- arxiv:2608.04003 · 2026-08-04 · preprint · sim 0.65 · hf
  PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-
- arxiv:2607.10526 · 2026-07-14 · preprint · sim 0.63 · hf
  Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents
  Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills. This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original conversation is gone. We call this persistent sycophancy and introduce the Personal Agent Sycophancy Benchmark (PASB), a 1,600-task benchmark that traces whether a conversa
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2607.13396 · 2026-07-15 · preprint · sim 0.57 · hf
  Set-shifting Behavioral Test for Harnessed Agents
  What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. Our benchmark mounts tool-skill libraries with redundancies, where many tools solve the same task but differ in hidden reliability. In our evaluation framework, a branched schedule shifts the reliable tool group at hidden boundaries and pairs every shift with a no-shift control. 
- arxiv:2606.06448 · 2026-06-04 · preprint · sim 0.56 · hf
  Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
  LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza
- arxiv:2606.17591 · 2026-06-16 · preprint · sim 0.55 · hf
  Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning
  Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic for
- arxiv:2608.18852 · 2026-08-19 · preprint · sim 0.54 · hf
  SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
  Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve
- arxiv:2605.26252 · 2026-05-25 · preprint · sim 0.53 · hf
  Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory
  Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and
- arxiv:2608.26730 · 2026-08-27 · preprint · sim 0.51 · hf
  Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training
  Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, 
- arxiv:2412.17256 · 2024-12-23 · preprint · sim 0.49 · hf
  B-STaR: Monitoring and Balancing Exploration and Exploitation in
  Self-Taught Reasoners
  In the absence of extensive human-annotated data for complex reasoning tasks, self-improvement -- where models are trained on their own outputs -- has emerged as a primary method for enhancing performance. However, the critical factors underlying the mechanism of these iterative self-improving methods remain poorly understood, such as under what conditions self-improvement is effective, and what are the bottlenecks in the current iterations. In this work, we identify and propose methods to monit

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
