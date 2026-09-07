=== NOVELTY CARD (automated search; evidence, not a verdict) ===
For each candidate: id · date · venue · similarity of its abstract to the proposal's hypothesis · channel.

Proposal: amortization_horizon_ranking_flip — Cheaper Than What? The Cost Definition and the Amortization Horizon Decide Whether an 8B Agent With Memory Beats a 14B Agent Without It

- arxiv:2606.18144 · 2026-06-16 · preprint · sim 0.62 · hf
  Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So
  A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories are worth an erase cycle. We treat embodied memory as depreciating capital and price that stock with a single endurance shadow price η, which makes cost-minimizing placement across a RAM / on-board NVM / cloud hierarchy a threshold in a wear-augmented per-byte index. The index is cost-optimal whatev
- arxiv:2607.01071 · 2026-07-01 · preprint · sim 0.52 · hf
  MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
  Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlo
- arxiv:2607.27919 · 2026-07-30 · preprint · sim 0.51 · hf
  Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory
  Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently. Memory Decoder introduces a parametric long-term memory module but only studies it at a relatively small scale. In this work, we present Memory Decoder at Scale, scaling memory models up to 6.9B parameters and pretraining them on 300B tokens. At this data scale, the combined cost of indexing and search makes a standard Faiss pipeline infeasib
- arxiv:2607.13157 · 2026-07-14 · preprint · sim 0.50 · hf
  Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents
  Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. These requirements extend beyond document retrieval: a memory layer must determine which interactions become durable state, how that state is scoped, how it is retrieved under latency constraints, and how it is revised or removed
- arxiv:2606.24775 · 2026-06-23 · preprint · sim 0.47 · hf
  Are We Ready For An Agent-Native Memory System?
  Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution. Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box. As a result, criti
- arxiv:2607.02255 · 2026-07-02 · preprint · sim 0.46 · hf
  AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
  Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw 
- arxiv:2606.06448 · 2026-06-04 · preprint · sim 0.46 · hf
  Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
  LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characteriza
- arxiv:2605.09104 · 2026-05-09 · preprint · sim 0.46 · hf
  Token Economics for LLM Agents: A Dual-View Study from Computing and Economics
  As LLM agents evolve, tokens have emerged as the core economic primitives of Agentic AI. However, their exponential consumption introduces severe computational, collaborative, and security bottlenecks. Current surveys remain fragmented across system optimization, architecture design, and trust, lacking a unified framework to evaluate the fundamental trade-off between output quality and economic cost. To bridge this gap, this survey presents the first comprehensive survey of Token Economics. By u
- arxiv:2606.12329 · 2026-06-10 · preprint · sim 0.44 · hf
  PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents
  AI coding assistants now support a growing share of software work, from quick scripts to production applications. Yet these agents remain largely stateless: each new session re-reads project files, re-derives prior decisions, and - most costly - may repeat debugging attempts that already failed. Reconstructing this context can consume an estimated 5,000-20,000 tokens per session; the bottleneck is often not model capability but missing project memory. We present projectmem, an open-source, local
- arxiv:2607.15105 · 2026-07-16 · preprint · sim 0.44 · hf
  Long-Context Fine-Tuning with Limited VRAM
  Parameter-efficient fine-tuning reduces model and optimizer memory, but dense attention still makes long training sequences expensive. We combine Hierarchical Global Attention (HGA) with segment-wise backpropagation and tiered KV storage. Only the active segment remains differentiable in VRAM; older KV is detached into RAM or NVMe, and HGA loads a bounded set of exact historical tokens for each query block. On Qwen3-8B with 4-bit QLoRA and PG19, dense training on a 16 GB Quadro RTX 5000 fits 2,0

Queries run are listed in the accompanying JSON. Absence from this card is not evidence of novelty.
