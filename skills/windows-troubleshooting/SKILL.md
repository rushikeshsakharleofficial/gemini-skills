---
name: windows-troubleshooting
description: Use when diagnosing system errors, blue screens (BSOD), performance bottlenecks, or application crashes on Windows.
---

# Windows Troubleshooting Skill

Systematic diagnosis for Windows issues.

## Workflow

1.  **Symptom Mapping:** Recent changes? Exact error?
2.  **Resource Check:** CPU/Mem (`get-process-list`), Disk (`check-disk-space`).
3.  **Log Deep Dive:**
    - `Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2} -MaxEvents 50`
    - Look for Event IDs: 1001 (BugCheck), 6008 (Dirty Shutdown), 7031 (Service crash).
4.  **Hardware/Drivers:** `Get-PnpDevice | Where Status -ne 'OK'`.
5.  **Corruptions:** `sfc /scannow`, `dism /online /cleanup-image /restorehealth`.

## Rules

- Never guess. Use logs.
- Isolate: disable 3rd party services (Clean Boot) if cause is unknown.
- Document findings: Root Cause, Evidence, Fix, Prevention.
