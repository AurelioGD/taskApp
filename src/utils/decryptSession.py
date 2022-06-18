
def decryptSession(session):
    separator = " "
    ascii_values = session.split(separator)
    char_values = []
    for character in ascii_values:
        intCharacter = False
        try:
            intCharacter = int(character)
        except:
            intCharacter = False
        if intCharacter == False:
            return False
        char_values.append(str(chr(intCharacter)))
    sesionJoint = "".join(char_values)
    return sesionJoint