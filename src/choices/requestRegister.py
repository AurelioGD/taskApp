from choices.InitialMenu import MANAGE_INITIAL_MENU_CHOICES
from utils.AuthenticationGraphics import drawMenuAuthenticate
from utils.cleanTerminal import cleanTerminal

def requestRegister():
    while True:
        choice = drawMenuAuthenticate()
        cleanTerminal()
        if choice == "3":
            break
        MANAGE_INITIAL_MENU_CHOICES.get(choice)()
        break