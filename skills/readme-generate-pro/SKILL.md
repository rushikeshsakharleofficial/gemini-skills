---
name: readme-generate-pro
description: Create, audit, rewrite, or improve a high-quality README.md for any software project. Use when the user asks for a README, project documentation, setup instructions, installation steps, usage examples, API docs, configuration docs, contributor docs, repository onboarding, or documentation polish.
---

# README Generate Pro

Use this skill to create or improve a README that is accurate, complete, maintainable, and useful to the project's intended audience.

## Requested README task

$ARGUMENTS

If no explicit arguments are provided, infer the task from the user's message and the project state.

## Operating principles

1. Ground every claim in the repository or in information the user explicitly provided.
2. Do not invent project purpose, production status, URLs, badges, screenshots, performance numbers, license terms, package names, API behavior, or deployment steps.
3. Prefer verified commands from manifests, scripts, Makefiles, CI files, Docker files, examples, tests, and existing docs.
4. If a fact is important but cannot be verified, either omit it or place it in a short `Maintainer TODOs` section with a precise question.
5. Preserve useful existing README content, but remove stale, duplicated, contradictory, placeholder, or marketing-heavy text.
6. Make commands copy-pasteable, scoped to the correct directory, and safe. Do not suggest destructive commands unless the project explicitly documents them.
7. Optimize for the target audience first: users need quick start and usage; contributors need setup, test, architecture, and contribution flow; API/library users need installation, imports, examples, and API surface.

## First-pass repository inspection

Before writing or editing README content, inspect the repository. Use normal Claude Code file tools and, when helpful, run the bundled metadata script:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/infer_project_metadata.py" .
```

Inspect at least the following when they exist:

- Existing `README*`, `docs/`, examples, demo files, screenshots, changelog, license, contributing guide, security policy.
- Manifests and build files: `package.json`, `pyproject.toml`, `requirements*.txt`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle*`, `Gemfile`, `composer.json`, `pubspec.yaml`, `mix.exs`, `.csproj`, `Dockerfile`, `docker-compose*.yml`, `Makefile`, `justfile`, `Taskfile.yml`.
- Entry points and app structure: `src/`, `app/`, `lib/`, `bin/`, `cmd/`, `packages/`, `examples/`, `tests/`, `spec/`.
- CI and automation files: `.github/workflows/`, `.gitlab-ci.yml`, `azure-pipelines.yml`, `Jenkinsfile`.
- Configuration examples: `.env.example`, `.env.sample`, config templates, CLI help, schema files.

For a monorepo, identify the root purpose and major packages. Decide whether the task needs one root README, package-specific READMEs, or both. Do not flatten distinct packages into one misleading setup path.

## README creation workflow

1. **Classify the project**
   - Application, library, CLI, API service, template/starter, plugin/extension, data/science project, infra/IaC, docs site, monorepo, or mixed.
   - Identify primary languages, frameworks, runtime versions, package managers, and launch/test commands.

2. **Determine audience and promise**
   - Write the opening for the most likely reader.
   - State what the project does in one clear paragraph.
   - If purpose cannot be verified, add a `Maintainer TODOs` item instead of guessing.

3. **Select the right sections**
   Use `templates/README.template.md` as a menu, not a rigid form. Include only sections that are useful and verifiable.

4. **Generate or update content**
   - Prefer short, direct explanations.
   - Include realistic examples copied or adapted from actual code, tests, examples, CLI definitions, or API routes.
   - Include environment variables only when found in repo files; document defaults and whether each value is required when verifiable.
   - For package scripts, list the most important commands with one-line purpose statements.
   - Link to local docs/files only if those paths exist.

5. **Verify the README**
   Run the bundled lint script when practical:

   ```bash
   python3 "${CLAUDE_SKILL_DIR}/scripts/readme_lint.py" README.md --root .
   ```

   Also manually check:
   - No unresolved placeholders such as `TODO`, `TBD`, `your-project`, `lorem`, or fake badge URLs unless confined to `Maintainer TODOs`.
   - Commands correspond to actual scripts, Make targets, documented tooling, or obvious language defaults.
   - Local links resolve.
   - The README does not contradict manifests, existing docs, or CI.
   - License wording matches the actual `LICENSE` file when present.

6. **Deliver clearly**
   - If editing the repository, write the README file directly.
   - Summarize what changed and list any unverifiable items separately.
   - If the user asked for review only, provide a prioritized audit with fixes.

## Section guidance

### Strong default README outline

Use this default order for most projects, adjusting as needed:

1. Project title
2. One-paragraph description
3. Optional badges, only if real and appropriate
4. Features or capabilities
5. Demo/screenshot, only if assets exist or user asked for a placeholder
6. Table of contents, only for long READMEs
7. Requirements/prerequisites
8. Installation
9. Quick start
10. Usage examples
11. Configuration
12. Scripts/commands
13. Testing
14. Project structure
15. API/reference, only for libraries/services with discoverable interfaces
16. Deployment/operations, only if documented or inferable from repo automation
17. Troubleshooting
18. Contributing
19. Security
20. License
21. Acknowledgements, only if present or requested

### Project-type adaptations

- **CLI**: include install command, executable name, `--help` output summary, common commands, examples, exit/config behavior if discoverable.
- **Library/package**: include package manager install, minimal import/example, public API summary, compatibility, versioning notes if present.
- **Web app**: include runtime, env setup, dev server, build, preview/start, key routes if discoverable, deployment notes only if present.
- **API service**: include local setup, env vars, database/cache dependencies, run command, endpoints or OpenAPI links, auth notes, testing.
- **Monorepo**: include workspace manager, package map, root commands, package-specific instructions, and dependency boundaries when clear.
- **Data/ML project**: include dataset expectations, environment setup, reproduce/run steps, outputs, notebooks/scripts, hardware requirements only if stated.
- **Infrastructure/IaC**: include providers/tools, plan/apply flow, required variables, state/backends, safety warnings, environments.

## Writing standards

- Use a concise, confident tone.
- Prefer present tense.
- Keep section headings conventional so readers can scan quickly.
- Use fenced code blocks with language tags.
- Use relative links for repository files.
- Avoid excessive emoji, hype, and vague adjectives.
- Avoid long generated tables unless they improve scanability.
- Explain assumptions explicitly.
- Keep `Maintainer TODOs` short and actionable; remove the section entirely if there are no TODOs.

## Accuracy rules for common README content

- **Badges**: Add only when the repo already has badge URLs or CI/package URLs can be verified from files. Never fabricate badge IDs.
- **License**: If `LICENSE` exists, name it accurately. If not, say no license file was found only when useful; do not assume MIT.
- **Install commands**: Match the package manager lockfile when possible (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`, `uv.lock`, `poetry.lock`, etc.).
- **Environment variables**: Prefer `.env.example` and schema/config files. Do not expose secrets from `.env` files.
- **Screenshots**: Use only existing image assets or documented URLs. Do not add broken image references.
- **Deployment**: Include only if Docker, CI, platform config, deploy scripts, or existing docs support it.
- **API docs**: Derive from route files, OpenAPI specs, controllers, exported functions, typed interfaces, or examples.
- **Security**: Do not publish secrets, tokens, internal hostnames, or private endpoints found in local files.

## Built-in resources

Read these supporting files when helpful:

- `templates/README.template.md` — adaptable README skeleton.
- `resources/readme-quality-rubric.md` — quality checklist and scoring guide.
- `resources/readme-audit-checklist.md` — review checklist for existing READMEs.
- `tests/eval_prompts.md` — prompts to test whether the skill behaves correctly across project types.

## Completion criteria

A README is done only when it:

- Explains what the project is and who it is for.
- Gets a new user from clone to first successful run as quickly as the repo permits.
- Documents configuration, common commands, tests, and contribution flow when discoverable.
- Contains no fabricated claims or broken local links.
- Separates verified facts from questions for maintainers.
- Is easy to scan and maintain.
