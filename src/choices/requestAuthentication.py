from services.user import getUserByUsernameAndPassword
from services.cacheManager import saveSession
from utils.AuthenticationGraphics import drawLogin
from utils.Graphics import drawMessage
from utils.cleanTerminal import cleanTerminal

def requestAuthentication():
    while True:
        userLoginData = drawLogin()
        user = getUserByUsernameAndPassword(userLoginData[0], userLoginData[1])
        if len(user) == 0:
            cleanTerminal()
            drawMessage("Usuario o contraseña incorrectos.")
        if len(user) == 1:
            saveSession(user[0].get("idDoc"))
            break;