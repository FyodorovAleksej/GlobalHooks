import time
from hookManage import HookManager


if __name__ == "__main__":
    # Create hookmanager
    hook = HookManager()
    # Create a loop to keep the application running
    while hook.isactive():
        time.sleep(0.1)