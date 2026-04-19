# Skill Enhancement: Systematic & Interactive Shell Execution

## Overview
This skill enhances the usage of the standard `run_shell_command` tool. It transforms "dumb" command execution into a resilient, interactive-aware workflow.

## 1. The Resilience Protocol (OODA Loop)
Every time you use `run_shell_command`, you MUST follow this cycle:
- **OBSERVE:** Run the command. Capture stdout, stderr, and the exit code.
- **ORIENT:** If exit code != 0, stop immediately. Do not ignore the error.
- **DECIDE:** Read the stderr. Formulate a hypothesis (e.g., "Missing directory," "Permission denied").
- **ACT:** Run a targeted fix (e.g., `mkdir`, `chmod`) BEFORE retrying the original task.

## 2. Enhancing Interactivity (The Piped Response Pattern)
If a command requires user input (e.g., `[Y/n]`, `Enter name:`), do NOT run it normally (it will hang). Instead, enhance the `run_shell_command` call using these patterns:

### A. The "Yes" Pipe (Universal)
```powershell
# Instead of: npm init
# Use:
powershell -Command "'\r' | npm init --yes"
```

### B. The "Multi-Prompt" Answerer (PowerShell)
For complex prompts, use a Here-String piped into the command:
```powershell
$answers = @"
my-project
1.0.0
MIT
"@
$answers | npm init
```

## 3. Handling "Hanging" Processes (Background Polling)
If a command must stay open (e.g., a server or long-running build):
1.  Set `is_background: true`.
2.  Immediately follow up with `read_background_output` using a delay (e.g., `delay_ms: 2000`).
3.  If the output shows a prompt or an error, use `run_shell_command` to send a "Signal" or a "Stop" command rather than letting it sit.

## 4. Environment Sanitization
Before any major execution, always run:
`powershell -Command "Get-Location; Get-ChildItem -Name"`
This ensures you are acting on the "True State" of the filesystem, not your "Memory" of it.
