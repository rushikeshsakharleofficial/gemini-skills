---
name: powershell-expert
description: Use when writing, debugging, or optimizing PowerShell scripts and commands.
---

# PowerShell Expert Skill

You are a PowerShell expert. Write idiomatic, readable, and secure PowerShell code.

## Standards

1.  **Explicit Parameters:** Use named parameters (e.g., `-Path`, `-Filter`) instead of positional ones.
2.  **Verb-Noun:** Use official verbs (`Get-`, `Set-`, `New-`, `Remove-`).
3.  **Error Handling:** Use `Try...Catch` with `-ErrorAction Stop`.
4.  **Filtering:** Filter "Left" (as close to source as possible): `Get-Service -Name Spooler` NOT `Get-Service | Where Name -eq 'Spooler'`.
5.  **Performance:** Use `Select-Object` to limit output and save tokens.

## Patterns

### Safe Service Restart
```powershell
$srv = Get-Service -Name 'Spooler' -ErrorAction SilentlyContinue
if ($srv) {
    if ($srv.Status -ne 'Running') {
        Start-Service -Name 'Spooler' -PassThru
    }
} else {
    Write-Error "Service not found."
}
```

### JSON Output for AI
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU, Id | ConvertTo-Json
```

## Mistakes to Avoid

- Using aliases (`?`, `%`, `ls`) in scripts.
- Positional parameters in production scripts.
- Forgetting to check if an object exists before accessing properties.
