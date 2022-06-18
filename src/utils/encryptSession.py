
def encryptSession(session):
    separator = " "
    ascii_values = []
    for character in session:
        ascii_values.append(str(ord(character)))
    sesionSeparated = separator.join(ascii_values)
    return sesionSeparated