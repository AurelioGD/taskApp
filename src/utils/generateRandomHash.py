from random import choice

def generateRandomHash():
    length = 18
    values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    randomHash = ""
    randomHash = randomHash.join([choice(values) for i in range(length)])
    return randomHash