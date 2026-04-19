# Parallel Agent Prompt Templates

## Independent Feature Implementation
"Act as a specialized feature agent. Implement the interface defined in [PATH] following the plan in [PLAN_PATH]. Focus strictly on [MODULE_NAME]. Ensure TDD compliance."

## Batch Refactoring
"Act as a refactoring agent. Update all calls to [OLD_FN] to [NEW_FN] in the following files: [FILE_LIST]. Preserve existing behavior and type safety."

## Documentation Update
"Act as a technical writer. Update [DOC_PATH] to reflect architectural changes in [CODE_PATH]. Maintain consistency with existing documentation style."
