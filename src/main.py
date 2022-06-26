
from choices.PrincipalMenu import PRINCIPAL_MENU_CHOICES
from choices.requestRegister import requestRegister
from services.cacheManager import authenticateSession, saveSession
from utils.Graphics import drawPrincipalMenu
from utils.cleanTerminal import cleanTerminal

def main():
    cleanTerminal()
    userData = authenticateSession()
    if not userData:
        requestRegister()
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
