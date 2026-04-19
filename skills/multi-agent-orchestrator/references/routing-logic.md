# Complexity Detection & Routing

## Indicators for Multi-Agent Orchestration
Invoke this skill if 2+ of the following are true:
- **File Count**: `grep` or `glob` results indicate >3 files need modification.
- **Keywords**: Request contains 'refactor', 'migrate', 'architecture', 'port', 're-implement'.
- **Dependency Depth**: Changes affect core interfaces used by multiple modules.
- **Task Independence**: The plan has 2+ tasks that can be performed without shared state.

## Routing Heuristics
| Metric | Threshold | Action |
|--------|-----------|--------|
| New Files | >5 | Dispatch Batch Creator |
| Refactor | System-wide | Dispatch Orchestrator |
| Bug Fix | Single File | Direct Execution |
