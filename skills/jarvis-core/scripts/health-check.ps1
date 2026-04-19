# J.A.R.V.I.S. System Health Check
# Purpose: Proactive monitoring of disk and process state.

$Health = [PSCustomObject]@{
    Timestamp = Get-Date -Format "HH:mm:ss"
    DiskStatus = Get-PSDrive C | Select-Object @{Name="FreeGB";Expression={[Math]::Round($_.Free/1GB,2)}}, @{Name="UsedGB";Expression={[Math]::Round($_.Used/1GB,2)}}
    ProcessCount = (Get-Process).Count
    TopMemoryProcs = Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 3 Name, @{Name="MB";Expression={[Math]::Round($_.WorkingSet64/1MB,2)}}
}

$Health | ConvertTo-Json
