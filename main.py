import time

import sys
from PyQt5.QtWidgets import QApplication
from propertiesWindow import MyWin
from hookManage import HookManager


if __name__ == "__main__":
    # Create hookmanager

    hook = HookManager()
   # window = MyWin()
   # window.show()
    #Create a loop to keep the application runningq12wqQQQQQ

    while hook.isactive():
        time.sleep(0.6)