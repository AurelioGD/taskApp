from utils.cleanTerminal import cleanTerminal
from utils.encryptPassword import encryptPassword
from utils.getRandomId import getRandomId
from consts.errorMessages import errorPasswordIncorrect
from getpass import getpass

def drawPrincipalMenu():
    print("1.-Gestionar tareas")
    print("2.-Gestionar equipos")
    print("3.-Ver perfil")
    print("4.-Ver notificaciones")
    print("5.-Gestionar amigos")
    print("6.-Salir")
    choice = input("Selecciona una opcion: ")
    return choice
    
def drawManageTeamsMenu():
    print("1.-Crear equipo")
    print("2.-Ver notificaciones")
    print("3.-Ver equipos")
    print("4.-Agregar amigo")
    print("5.-Salir")
    choice = input("Selecciona una opcion: ")
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