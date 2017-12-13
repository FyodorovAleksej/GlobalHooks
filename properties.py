import os
import encryptor

class Properties:
    silenceMode = True
    address = ""
    size = 0
    def __init__(self, silenceMode, address, size):
        print(silenceMode)
        print(address)
        print(size)
        self.silenceMode = silenceMode
        self.address = address
        self.size = size

    def save(self):
        file = open(os.getcwd() + "/prop.prp", "w+")
        file.write(encryptor.encrypt(str(self.silenceMode)) + "\n")
        file.write(encryptor.encrypt(self.address) + "\n")
        file.write(encryptor.encrypt(str(self.size) + "\n"))
        file.close()


class NullProperties(Properties):

    def __init__(self):
        super().__init__(True, "Fyodorov.aleksej@gmail.com", 1024)
    def save(self):
        super().save()

def load():
    try:
        file = open(os.getcwd() + "/prop.prp", "r+")
    except FileNotFoundError:
        print("Not founded")
        return NullProperties()
    lines = file.readlines()
    if (len(lines) < 2):
        print("Not enough")
        file.close()
        return NullProperties()
    file.close()
    silM = False
    if (encryptor.decrypt(lines[0][:-1]) == "True"):
        silM = True
    adres = encryptor.decrypt(lines[1][:-1])
    size = int(encryptor.decrypt(lines[2][:-1]))
    return Properties(silM, adres, size)



