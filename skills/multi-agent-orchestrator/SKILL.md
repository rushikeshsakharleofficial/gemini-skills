---
name: multi-agent-orchestrator
description: Orchestrates multi-agent task distribution and planning. Use when a task involves 3+ files, architectural changes, or complex dependencies.
---

# Multi-Agent Orchestrator Skill

This skill allows you to operate as a high-level manager, delegating work to specialized subagents and coordinating their progress via a shared "Blackboard" (agent-coordinator-mcp).

## 1. Task Decomposition
When a user provides a complex request (e.g., "Build a full-stack auth system"), you MUST:
- **Analyze:** Identify independent components (Frontend, Backend, DB Schema, Tests).
- **Register:** Use `add_task` for each component.
- **Dependency Mapping:** Use `register_subtask` to define which tasks must finish before others start.

## 2. Delegation & Concurrency
- **Invoke:** Use `invoke_agent` to spawn subagents for each "Claimable" task.
- **Parallelism:** You can run multiple `invoke_agent` calls in parallel if they are independent.
- **Locking:** Instruct subagents to use `lock_resource` before editing any file to prevent race conditions.

## 3. Blackboard Coordination
- **Status Updates:** Check `list_tasks` frequently to monitor progress.
- **Completion:** Ensure subagents use `complete_task` when their part is finished.
- **Synthesis:** Once all subtasks are complete, merge their results and provide a final summary to the user.

## 4. Claude-Style Interaction
- **Non-Blocking:** If a subagent is working on a long-task, continue to listen for new user messages.
- **The Non-Blocking Mandate:** You MUST NOT allow subagents to occupy the main interaction loop for more than a few seconds. If a subagent needs to perform a long-running task, it MUST use `is_background: true` and report its PID to the blackboard.
- **Queueing:** Add new user requests as tasks to the queue rather than trying to handle them synchronously.

## Rules
- NEVER let two agents edit the same file without a lock.
- ALWAYS use `read_blackboard` to check if a global configuration (e.g., base URL) has changed.
- If a subagent fails, retry or re-assign the task via the blackboard.
