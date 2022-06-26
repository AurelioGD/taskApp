from choices.requestAuthentication import requestAuthentication
from services.user import createUserService
from utils.AuthenticationGraphics import drawRegister
from utils.Graphics import drawMessage
from utils.cleanTerminal import cleanTerminal

def handleLogIn():
    drawMessage("Login")
    requestAuthentication()
    cleanTerminal()
def handleSignUp():
    userData = drawRegister()
    createUserService(userData)
    cleanTerminal()

MANAGE_INITIAL_MENU_CHOICES = {
    "1": handleLogIn,
    "2": handleSignUp,
}