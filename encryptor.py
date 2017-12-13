def encrypt(raw):
    result = ""
    for i in range(0, len(raw)):
        result = result + chr(ord(raw[i]) + 14)
    return result

def decrypt(raw):
    result = ""
    for i in range(0, len(raw)):
        result = result + chr(ord(raw[i]) - 14)
    return result