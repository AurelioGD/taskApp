
from choices.PrincipalMenu import PRINCIPAL_MENU_CHOICES
from services.cacheManager import checkSession, saveSession
from services.user import getUserByDocId, getUserByUsernameAndPassword
from utils.AuthenticationGraphics import drawLogin
from utils.Graphics import drawMessage, drawPrincipalMenu
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

def main():
    cleanTerminal()
    session = checkSession()
    if not session:
        drawMessage("Login")
        requestAuthentication()
        cleanTerminal()
    session = checkSession()
    userData = getUserByDocId(session)
    if not userData:
        drawMessage("Login")
        requestAuthentication()
        cleanTerminal()
    session = checkSession()
    userData = getUserByDocId(session)
    if userData:
        while True:
            choice = drawPrincipalMenu()
            if choice == "7":
                cleanTerminal()
                break
            if choice == "6":
                cleanTerminal()
                saveSession()
                break
            PRINCIPAL_MENU_CHOICES.get(choice)()
main()
