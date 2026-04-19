# Interactive Patterns Reference

## Prompt Detection & Response
Use these patterns when you encounter interactive blocks via `run_shell_command`.

### 1. Confirmations [Y/n]
**Pattern:** `echo 'y' | command`
**Windows Native:** `powershell -Command "'y' | command"`

### 2. Password Prompts (Non-Secure)
*Note: Only use for local dev setups.*
**Pattern:** `echo 'mypassword' | sudo -S command`

### 3. NPM / Init Tools
Always prefer non-interactive flags if available:
- `npm init -y`
- `git commit -m "message"` (Avoids opening Vim)
- `apt-get install -y`

### 4. SSH / Remote
Use `-o BatchMode=yes` to force SSH to fail instead of hanging on a password prompt, allowing you to catch the error and handle it via the OODA loop.

### 5. Manual Stepping
If a tool has no "Auto" mode, use `run_shell_command` to create a temporary "Response Script":
```powershell
Set-Content -Path response.txt -Value "Answer 1`nAnswer 2`nAnswer 3"
Get-Content response.txt | command
Remove-Item response.txt
```
