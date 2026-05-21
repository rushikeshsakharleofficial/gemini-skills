# README Generate Pro Skill

A Claude Code skill for creating, auditing, and improving robust `README.md` files for software projects.

## Marketplace URL

GitHub marketplace-style URL:

```text
https://github.com/rushikeshsakharleofficial/gemini-skills/tree/main/skills/readme-generate-pro
```

## What it does

- Inspects the repository before writing.
- Grounds README content in actual project files.
- Avoids hallucinated badges, licenses, commands, screenshots, and deployment claims.
- Adapts the README structure to apps, libraries, CLIs, API services, monorepos, data projects, and infrastructure projects.
- Includes helper scripts for project metadata inference and README linting.

## Install as a personal Claude Code skill

```bash
git clone https://github.com/rushikeshsakharleofficial/gemini-skills.git /tmp/gemini-skills
mkdir -p ~/.claude/skills
cp -R /tmp/gemini-skills/skills/readme-generate-pro ~/.claude/skills/
```

Then run Claude Code in any project and invoke:

```text
/readme-generate-pro Create a README for this project
```

## Install as a project skill

From your repository root:

```bash
git clone https://github.com/rushikeshsakharleofficial/gemini-skills.git /tmp/gemini-skills
mkdir -p .claude/skills
cp -R /tmp/gemini-skills/skills/readme-generate-pro .claude/skills/
```

Commit `.claude/skills/readme-generate-pro/` if you want the skill shared with the project.

## Example prompts

```text
/readme-generate-pro Create a README for this repo. Do not invent anything; add maintainer TODOs for missing facts.
```

```text
/readme-generate-pro Audit README.md and give me prioritized fixes without editing files.
```

```text
/readme-generate-pro Rewrite the README for new contributors: setup, run, test, project structure, and contribution flow.
```

## Files

- `SKILL.md` — main Claude Code skill instructions.
- `templates/README.template.md` — adaptable README skeleton.
- `resources/readme-quality-rubric.md` — scoring and review rubric.
- `resources/readme-audit-checklist.md` — checklist for existing README review.
- `scripts/infer_project_metadata.py` — dependency-free project metadata scanner.
- `scripts/readme_lint.py` — dependency-free README sanity checker.
- `tests/eval_prompts.md` — sample prompts for testing the skill.

## Compatibility notes

Claude Code skills are directories with a required `SKILL.md` entrypoint. Install this folder as `readme-generate-pro` so the command is available as `/readme-generate-pro`.
