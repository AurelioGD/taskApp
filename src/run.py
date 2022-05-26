from utils.Graphics import drawLogin, drawRegister, drawAuthenticationMenu, drawPrincipalMenu
from utils.cleanTerminal import cleanTerminal
from services.User import createUser

def main():
    cleanTerminal()
    drawPrincipalMenu()
main()
