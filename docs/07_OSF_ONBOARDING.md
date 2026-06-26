# 📘 OpenSceneFORCE V7 — Beginner → Pro Onboarding Flow

---

## 🧠 Step 1 — What OSF Is (Simple Explanation)

OpenSceneFORCE (OSF) is a development startup system.

Instead of manually setting up your project every time, OSF automatically prepares everything for you.

### What it does in simple terms:

- Opens your project folder
- Turns on the Python environment (.venv)
- Gets your system ready for coding
- Removes all setup steps you normally repeat

### Simple idea:

> OSF = “Open terminal → ready to code instantly”

---

## 🖼️ Visual Workflow

![OSF VSCode Integration](../engineering/assets/ui/vscodeosflauncher.png)

---

## ⚡ Step 2 — How to Run OSF

### Step 1 — Open PowerShell

### Step 2 — Go to project folder:

```powershell
cd "C:\DevTools\FullBuilds_Unsigned\OpenSceneFORCE"
```

### Step 3 — Run the launcher:

```powershell
.\tools\osf.ps1
```

### Step 4 — Select your project

Type:

```
1
```

### Result:

- You are moved into the project folder
- Your .venv activates automatically
- You are ready to code immediately

---

## ⚙️ Step 3 — What OSF Changes on Your System

OSF does NOT modify your code.

It only changes your current terminal session.

### It temporarily:

- Changes directory to your project
- Activates .venv (Python environment)
- Sets up your development workspace

### It does NOT:

- Delete files
- Modify project code
- Change system settings permanently

---

## 🔁 Step 4 — How to Undo / Reset OSF

### Option 1 — Close terminal
Just close PowerShell.

### Option 2 — Deactivate environment
```powershell
deactivate
```

### Option 3 — Reset directory
```powershell
cd ~
```

---

## 🧠 Summary

| Step | Meaning |
|------|--------|
| 1 | Understand OSF |
| 2 | Run OSF tool |
| 3 | Auto environment setup |
| 4 | Safe exit anytime |

---

> OSF makes development feel like: open terminal → instantly ready to build.
