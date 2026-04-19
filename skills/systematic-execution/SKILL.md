---
name: systematic-execution
description: Enforces an Observe-Orient-Decide-Act (OODA) loop for resilient command execution and handles interactive prompts using PTY tools.
---

# Systematic Execution Skill

This skill transforms the agent's interaction with the system shell into a resilient, high-fidelity engineering workflow.

## 1. The OODA Loop
- **Observe:** Check the current environment (CWD, files) before running commands.
- **Orient:** Analyze previous command failures. Read stderr completely.
- **Decide:** Formulate a hypothesis and a targeted remediation plan.
- **Act:** Execute the fix before retrying.

## 2. Native Interactive Handshake
- **Interactivity:** Use the `interactive: true` flag for all commands that may prompt (e.g. `npm init`, `ssh`).
- **Input:** Use `send_shell_input` for all password or confirmation prompts.
- **Security:** Use `is_sensitive: true` for sensitive data to keep it redacted from logs.
