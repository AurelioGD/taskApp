from utils.Graphics import drawMessage
from utils.cleanTerminal import cleanTerminal
from utils.getRandomId import getRandomId
from consts.errorMessages import errorPasswordIncorrect
from getpass import getpass

def drawLogin():
    username = input("Ingresa tu usuario: ")
    password = getpass("Ingresa tu contraseña: ")
    return (username, password )

def drawRegister():
    username = input("Ingresa un nombre de usuario: ")
    keyword = input("Ingresa una palabra clave(Requerida para cambiar contraseña):")
    while(True):
        password = getpass("Ingresa una nueva contraseña: ")
        passwordSecond = getpass("Ingresa la contraseña de nuevo: ")
        if password == passwordSecond:
            break
        cleanTerminal()
        drawMessage(errorPasswordIncorrect)
    return { "id": str(getRandomId()), "username": username,"keyword": keyword, "password": password }

def drawAuthenticationMenu():
    print("1.-Iniciar sesion")
    print("2.-Registrarme")
    choice = int(input("Selecciona una opcion: "))
    return choice