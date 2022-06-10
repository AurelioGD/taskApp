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

def drawMessage(message):
    print("------------------------------------------------------------------")
    print(message)
    print("------------------------------------------------------------------")