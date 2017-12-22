import time

import sys
from PyQt5.QtWidgets import QApplication
from propertiesWindow import MyWin
from hookManage import HookManager


if __name__ == "__main__":
    # Create hookmanager

    hook = HookManager()
   # window = MyWin()qww
   # window.show()
    #Create a loop to keep the application runningq12wqQQQQQsdasdsawqewqewzxzxczZZZ

    while hook.isactive():
        time.sleep(0.6)