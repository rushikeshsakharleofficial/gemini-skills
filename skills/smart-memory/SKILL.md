---
name: smart-memory
description: Use when managing agent context, token limits, or designing memory architectures.
---

# Smart Memory Management

Guide for agent memory. Goal = avoid context rot, save tokens, keep reasoning high.

## Memory Architecture (4 Tiers)

1. **Short-Term (Working):** Last 5-10 turns + active task state. In context window.
2. **Episodic:** Past interactions + tool results. Vector DB with recency decay.
3. **Semantic:** Knowledge base, facts, preferences (e.g., `MEMORY.md`, SQL).
4. **Procedural:** Core skills, persona, rules (system prompts).

## Context Optimization

- **Reduction:** Summarize history. Keep last N turns full, compress older turns recursively.
- **Offloading:** Move large tool outputs (HTML, big JSON) to disk. Keep structured pointer in context.
- **Selection:** RAG (Retrieval-Augmented Generation). Pull only relevant snippets.
- **Isolation:** Split tasks to sub-agents. Prevent context drowning.

## Advanced Tactics

- **Strategic Forgetting:** Prune noise (false starts, errors) after task done.
- **Structured Note-taking:** Use scratchpad (`NOTES.md`) for long-horizon state tracking.
- **Tool Condensation:** Tools return pre-processed data (row counts, keys), not raw payloads.
- **Prompt Caching:** Cache stable system prompts + large reference docs.

## Implementation Limits

- **Threshold Compaction:** Trigger summarize/offload when context hits 80-90%.
- **Recoverability:** Test if agent can find needle-in-haystack after compression.
