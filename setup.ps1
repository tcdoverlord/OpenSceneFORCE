# =========================
# OpenSceneFORCE V7 Bootstrapper
# =========================

cd "C:\DevTools\FullBuilds_Unsigned\OpenSceneFORCE"

Write-Host "=== OpenSceneFORCE V7 Bootstrap Starting ==="

# 1. Check Python
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "Python not found. Install Python 3.13+ first."
    exit 1
}

# 2. Create venv if missing
if (!(Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# 3. Activate venv
Write-Host "Activating virtual environment..."
.\.venv\Scripts\Activate.ps1

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install dependencies
Write-Host "Installing requirements..."
pip install -r requirements.txt

# 6. Verify install
Write-Host "Installed packages:"
pip list

Write-Host "=== Bootstrap Complete ==="
Write-Host "Run app with: python app\main.py"