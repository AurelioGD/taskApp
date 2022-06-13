
def encryptSesion(sesion):
    separator = " "
    ascii_values = []
    for character in sesion:
        ascii_values.append(str(ord(character)))
    sesionSeparated = separator.join(ascii_values)
    return sesionSeparated