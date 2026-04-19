---
name: token-optimizer
description: Use when the session is reaching high token counts, or to ensure maximum efficiency in long-running tasks.
---

# Token Optimizer Skill

Maintain context hygiene and minimize token consumption for faster, cheaper, and more accurate interactions.

## Core Principles

1.  **Surgical Reads:** Never read a whole file if you only need a specific section. Use `start_line` and `end_line` in `read_file`.
2.  **Surgical Context:** Use the `@` symbol to reference specific files or folders. Avoid loading the entire workspace.
3.  **Patch-First:** Favor `replace` (patches) over `write_file` (full overwrites) for large files to reduce input/output tokens.
4.  **Caveman Style:** For mechanical or high-frequency tasks, adopt a terse, article-free style.
5.  **Context Hygiene:**
    - If a task is complete, start a fresh session with `gemini reset` or `/clear`.
    - Use `/rewind` (or `Esc` twice) to remove failed attempts or redundant context from history.

## Workflow

1.  **Audit:** Periodically check token usage with `/stats`.
2.  **Prune:** Identify redundant history and suggest `/rewind`.
3.  **Optimize:** Use the most specific tool possible (e.g., `grep_search` instead of reading multiple files to find a string).

## Rationalization Table

| Excuse | Reality |
|--------|---------|
| "Reading the whole file is easier" | Wasteful context makes the model slower and more prone to "hallucinations" or forgetting. |
| "Verbose explanations are clearer" | Smart agents understand fragments. Save tokens for the code. |
| "I'll just keep this session going" | "Context drift" occurs in long sessions. Fresh sessions = fresh thinking. |

## Red Flags

- Outputting full files when only a few lines changed.
- Reading non-relevant files just because they are in the same directory.
- Not using `/rewind` after a major tool failure or correction.
