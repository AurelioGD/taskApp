from utils.cleanTerminal import cleanTerminal
from utils.encryptPassword import encryptPassword
from utils.getRandomId import getRandomId
from consts.errorMessages import errorPasswordIncorrect
from getpass import getpass

def drawPrincipalMenu():
    print("1.-Filtrar por")
    print("2.-Agregar una nueva tarea")
    print("3.-Modificar tarea")
    print("4.-Eliminar tarea")
    print("5.-Gestion de equipos")
    print("6.-Salir")
    choice = int(input("Selecciona una opcion: "))
    return choice

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
    return { "id": str(getRandomId()), "username": username, "password": encryptPassword(password) }
    
def drawAuthenticationMenu():
    print("1.-Iniciar sesion")
    print("2.-Registrarme")
    choice = int(input("Selecciona una opcion: "))
    return choice

def drawMessage(message):
    print("------------------------------------------------------------------")
    print(message)
    print("------------------------------------------------------------------")