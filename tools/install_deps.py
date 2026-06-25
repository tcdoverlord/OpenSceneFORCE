import subprocess, sys

for p in ["PySide6", "psutil", "requests"]:
    subprocess.check_call([sys.executable, "-m", "pip", "install", p])

print("Dependencies installed")
