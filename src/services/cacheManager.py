import jwt
from os import path, getcwd
from utils.checkIfExistFile import checkIfExistFile

from utils.decryptSesion import decryptSesion

rootPath = getcwd()
cacheFilePath = path.join(rootPath,"src","cache", "sesion.as")

def createCacheFile():
    cacheFile = open(cacheFilePath, "w")
    cacheFile.write("")
    cacheFile.close()
def readCacheFile():
    cacheFile = open(cacheFilePath, encoding = 'utf-8')
    return cacheFile.read()
def checkSesion():
    existFileSesion = checkIfExistFile(cacheFilePath)
    if not existFileSesion:
        createCacheFile()
        return existFileSesion
    sesion = readCacheFile()
    if not sesion:
        return False
    print(sesion)