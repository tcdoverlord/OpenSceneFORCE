from system.obs_controller import is_obs_running, close_obs
from safety.system_check import system_check
from core.backup_engine import backup
from core.restore_engine import restore
from core.update_engine import update_app
from core.repair_engine import repair_obs

def dispatch(route: str):

    state = system_check()
    if not state.get("safe", True):
        print("[BLOCKED] System unsafe - aborting:", route)
        return

    ROUTES = {
        "SAFE_MODE": safe_mode_route,
        "BACKUP": backup_route,
        "RESTORE": restore_route,
        "UPDATE_APP": update_route,
        "REPAIR_OBS": repair_route
    }

    handler = ROUTES.get(route)

    if handler:
        handler()
    else:
        print("[ERROR] Unknown route:", route)


def safe_mode_route():
    print("[SAFE MODE] Starting...")
    if is_obs_running():
        close_obs()
    print("[SAFE MODE] Ready")


def backup_route():
    print("[BACKUP] Starting...")
    backup()


def restore_route():
    print("[RESTORE] Starting...")
    restore()


def update_route():
    print("[UPDATE APP] Starting...")
    update_app()


def repair_route():
    print("[REPAIR OBS] Starting...")
    repair_obs()
