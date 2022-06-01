from utils.Graphics import drawPrincipalMenu
from utils.cleanTerminal import cleanTerminal
from choices.PrincipalMenu import PRINCIPAL_MENU_CHOICES

def main():
    cleanTerminal()
    while True:
        choice = drawPrincipalMenu()
        cleanTerminal()
        if choice == "6": break;
        PRINCIPAL_MENU_CHOICES.get(choice)()
main()
