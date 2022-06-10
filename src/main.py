from utils.cleanTerminal import cleanTerminal
from utils.AuthenticationGraphics import drawLogin, drawRegister
from services.User import createUserService, getUserByUsernameAndPassword
from utils.encryptPassword import encryptPassword

def main():
    cleanTerminal()
    userDataAuthentication = drawLogin()
    Data = getUserByUsernameAndPassword(userDataAuthentication[0], encryptPassword(userDataAuthentication[1]))
    print(Data)
main()
