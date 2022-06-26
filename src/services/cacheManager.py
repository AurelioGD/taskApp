from os import path, getcwd
from services.user import getUserByDocId
from utils.checkIfExistFile import checkIfExistFile

from utils.decryptSession import decryptSession
from utils.encryptSession import encryptSession

rootPath = getcwd()
cacheFilePath = path.join(rootPath,"src","cache", "session.as")

def createCacheFile():
    cacheFile = open(cacheFilePath, "w")
    cacheFile.write("")
    cacheFile.close()
def readCacheFile():
    cacheFile = open(cacheFilePath, encoding = 'utf-8')
    return cacheFile.read()
def overwriteCacheFile(session = ""):
    cacheFile = open(cacheFilePath, "w")
    cacheFile.write(session)
    cacheFile.close()
    return True
def checkSession():
    existFileSession = checkIfExistFile(cacheFilePath)
    if not existFileSession:
        createCacheFile()
        return existFileSession
    session = readCacheFile()
    if not session:
        return False
    sessionDecryped = decryptSession(session)
    return sessionDecryped
def saveSession(userDocId = ""):
    session = encryptSession(userDocId)
    overwriteCacheFile(session)
    return True
def authenticateSession():
    session = checkSession()
    if not session:
        return False
    userData = getUserByDocId(session)
    return userData