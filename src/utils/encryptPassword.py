from hashlib import sha256

def encryptPassword(password):
    encryptedPassword = sha256(password.decode('utf-8')).hexdigest()
    return encryptedPassword