import psutil

def is_obs_running():
    for p in psutil.process_iter(['name']):
        if p.info['name'] and "obs" in p.info['name'].lower():
            return True
    return False

def close_obs():
    print("[SYSTEM] Closing OBS safely (stub)")
