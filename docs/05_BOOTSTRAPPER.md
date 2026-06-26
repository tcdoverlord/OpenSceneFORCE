# ⚡ OpenSceneFORCE V7 Bootstrapper

## Overview

The OpenSceneFORCE V7 system includes a PowerShell bootstrapper designed to fully automate environment setup.

This ensures that any developer (or future system rebuild) can initialize the project with a single command.

---

## 🚀 What the Bootstrapper Does

When you run:

```powershell
.\setup.ps1
```

It automatically:

1. Checks Python installation
2. Creates a virtual environment (.venv)
3. Activates the environment
4. Upgrades pip
5. Installs all dependencies from requirements.txt
6. Validates installed packages

---

## 🧠 Why This Exists

This project is designed to be:

- Self-contained
- Reproducible
- Easy to deploy
- Easy to recover after system failure

The bootstrapper removes manual setup errors.

---

## ⚡ Usage

```powershell
cd "C:\DevTools\FullBuilds_Unsigned\OpenSceneFORCE"
.\setup.ps1
```

---

## 🔗 Related Files

- setup.ps1 → Bootstrap automation script
- requirements.txt → Runtime dependencies
- app/main.py → Application entry point
