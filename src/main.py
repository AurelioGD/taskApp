
from choices.PrincipalMenu import PRINCIPAL_MENU_CHOICES
from choices.requestAuthentication import requestAuthentication
from services.cacheManager import authenticateSession, checkSession, saveSession
from utils.Graphics import drawMessage, drawPrincipalMenu
from utils.cleanTerminal import cleanTerminal



def main():
    cleanTerminal()
    session = checkSession()
    if not session:
        drawMessage("Login")
        requestAuthentication()
        cleanTerminal()
    userData = authenticateSession()
    if not userData:
        drawMessage("Login")
        requestAuthentication()
        cleanTerminal()
    userData = authenticateSession()
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
