
from services.cacheManager import checkSesion
from utils.cleanTerminal import cleanTerminal
from utils.decryptSesion import decryptSesion
from utils.encryptPassword import encryptPassword
from utils.encryptSesion import encryptSesion

def main():
    cleanTerminal()
    print(checkSesion())
main()
