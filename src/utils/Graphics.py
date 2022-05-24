from utils.cleanTerminal import cleanTerminal
from utils.encryptPassword import encryptPassword
from utils.getRandomInt import getRandomInt
from consts.errorMessages import errorPasswordIncorrect
from getpass import getpass

def drawLogin():
    user = input("Ingresa el usuario: ")
    password = getpass("Ingresa la contraseña: ")
    return { "user": user, "password": password }
    
def drawRegister():
    username = input("Ingresa un nombre de usuario: ")
    while(True):
        password = getpass("Ingresa una nueva contraseña: ")
        passwordSecond = getpass("Ingresa la contraseña de nuevo: ")
        if password == passwordSecond:
            break
        cleanTerminal()
        drawMessage(errorPasswordIncorrect)
    return { "id": str(getRandomInt()), "username": username, "password": encryptPassword(password) }
    
def drawAuthenticationMenu():
    print("1.-Iniciar sesion")
    print("2.-Registrarme")
    choice = int(input("Selecciona una opcion: "))
    return choice

def drawMessage(message):
    print("------------------------------------------------------------------")
    print(message)
    print("------------------------------------------------------------------")