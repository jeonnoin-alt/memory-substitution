=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: success_filter_lockin_under_shift — Locked In by Its Own Successes: Success-Filtered Self-Collected Experience after a Hidden Rule Change, in Context and in Weights

- arxiv:2608.04003 · 2026-08-04 · preprint · sim 0.65 · hf · found via agent
  PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-
- arxiv:2608.25553 · 2026-08-28 · preprint · sim 0.62 · hf · found via mechanism_home
  When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
  Provenance links keep the evidence behind an inherited belief reachable; an agent with a verification budget must still choose which links to inspect. We study a consolidated memory that states a decision constraint and whose source record has since been superseded by a record that withdraws it: provenance is immutable, the current record has changed, and the memory is stale. In a controlled six-memory scenario with a budget of two records, sixteen language models rarely re-verified a constraint
- arxiv:2605.06132 · 2026-05-07 · preprint · sim 0.61 · hf · found via baseline
  MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval
  In agent memory systems, the reranking model serves as the critical bridge connecting user queries with long-term memory. Most systems adopt the "retrieve-then-rerank" two-stage paradigm, but generic reranking models rely on semantic similarity matching and lack genuine reasoning capabilities, leading to a problem where recalled results are semantically highly relevant yet do not contain the key information needed to answer the question. This deficiency manifests in memory scenarios as three spe
- arxiv:2607.10608 · 2026-07-12 · preprint · sim 0.58 · hf · found via agent
  The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
  Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determ
- arxiv:2606.10241 · 2026-06-08 · preprint · sim 0.57 · hf · found via mechanism_home
  Regimes: An Auditable, Held-Out-Gated Improvement Loop Demonstrated on LongMemEval with ActiveGraph
  Autonomous improvement loops are hard to trust because the improvement process is usually external scaffolding bolted onto the agent: failures go unlogged, diagnoses cannot be replayed, and promote-or-discard decisions land in a side database rather than the agent's own history. We show that an event-sourced agent runtime removes that friction and turns controlled improvement into a first-class workflow. When the agent's state is a deterministic projection of an append-only event log, failures a
- arxiv:2606.06448 · 2026-06-04 · preprint · sim 0.56 · hf · found via agent
  Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
  LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza
- arxiv:2606.17591 · 2026-06-16 · preprint · sim 0.55 · hf · found via agent/mechanism_home
  Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning
  Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic for
- arxiv:2606.26511 · 2026-06-25 · preprint · sim 0.54 · hf · found via adjacent
  Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge
  Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), a
- arxiv:2606.00408 · 2026-05-29 · preprint · sim 0.54 · hf · found via mechanism_home
  Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism
  Long-horizon search agents accumulate large amounts of retrieved content across many tool calls, making context-budget efficiency increasingly important. A minimal intervention is to mask stale observations from the context as the trajectory progresses, but it remains unclear when this form of context management helps and why. We study observation masking through a systematic sweep over various agent backbones (4B to 284B parameters) and three retrievers on offline and live-web agentic search be
- arxiv:2605.26252 · 2026-05-25 · preprint · sim 0.53 · hf · found via agent
  Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory
  Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and

Returned only by the home-literature / adjacent-field / baseline queries (low similarity is expected; check them):
- arxiv:2607.17427 · 2026-07-19 · sim 0.50 · via mechanism_home — Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families
- arxiv:2604.21432 · 2026-04-23 · sim 0.49 · via mechanism_home — A single algorithm for both restless and rested rotting bandits
- arxiv:2608.04574 · 2026-08-05 · sim 0.48 · via agent/mechanism_home — When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
- arxiv:2605.14473 · 2026-05-14 · sim 0.42 · via mechanism_home — Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict
- arxiv:2212.01340 · 2022-12-02 · sim 0.40 · via baseline — Moving Beyond Downstream Task Accuracy for Information Retrieval
  Benchmarking

Queries run are listed in the accompanying JSON with their class. Absence from this card is not evidence of novelty.
