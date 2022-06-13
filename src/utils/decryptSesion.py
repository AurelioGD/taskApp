
def decryptSesion(sesion):
    separator = " "
    ascii_values = sesion.split(separator)
    char_values = []
    for character in ascii_values:
        char_values.append(str(chr(int(character))))
    sesionJoint = "".join(char_values)
    return sesionJoint