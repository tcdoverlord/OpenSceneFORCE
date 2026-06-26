# =========================
# OpenSceneFORCE Dev Launcher V1
# =========================

Clear-Host

$projects = @{
    "1" = "C:\DevTools\FullBuilds_Unsigned\OpenSceneFORCE"
}

Write-Host "====================================="
Write-Host "   OPENSCENEFORCE DEV LAUNCHER V1"
Write-Host "====================================="
Write-Host ""

Write-Host "Available Projects:"
foreach ($key in $projects.Keys) {
    Write-Host "[$key] $($projects[$key])"
}

Write-Host ""
$choice = Read-Host "Select project"

if (-not $projects.ContainsKey($choice)) {
    Write-Host "Invalid selection. Exiting..." -ForegroundColor Red
    exit
}

$path = $projects[$choice]

if (!(Test-Path $path)) {
    Write-Host "Project path not found!" -ForegroundColor Red
    exit
}

Set-Location $path

Write-Host ""
Write-Host "Entering project: $path" -ForegroundColor Green

# Activate venv if it exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Cyan
    .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "No virtual environment found." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "READY ✔ You are now inside OpenSceneFORCE" -ForegroundColor Green