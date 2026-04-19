---
name: model-advisor
description: Use when needing to select optimal Gemini model based on cost, latency, and task complexity.
---

# Model Advisor

Guide for switching Gemini models smartly. Optimization = cost ↓ speed ↑ quality ↔.

## Model Fleet

| Model | Best For | Strength |
|-------|----------|----------|
| **Gemini 2.5 Flash** | Chat, extraction, classification, rapid iteration. | Low cost, sub-sec latency. |
| **Gemini 2.5 Pro** | Deep reasoning, complex code, multi-step logic. | High accuracy for "messy" tasks. |
| **Flash-Lite** | Batch summaries, simple text gen, high volume. | Max efficiency. |

## Selection Logic

1. **Default: Flash.** Use for research, simple fixes, exploration.
2. **Escalate: Pro.** Use if Flash fails, logic complex, or final high-fidelity review needed.
3. **Batch: Flash-Lite.** Use for non-urgent high-volume tasks.

## Optimization Strategies

- **Dynamic Routing:** Start Flash. If logic wall hit → Switch Pro.
- **Context Caching:** Use for large static codebases/docs. Save 60%+ cost.
- **Flex Tier:** Background tasks. 50% discount for idle capacity usage.
- **Tokens:** Keep output short. Output tokens cost > input tokens.

## Commands (Web UI)

- Start prompt with `@thinking` or `@fast` to swap instantly.

## Fallback Pattern

Task fail on Pro (quota/error) → retry Flash. Keep service alive.
