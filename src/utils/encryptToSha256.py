from hashlib import sha256

def encryptToSha256(text):
    encryptedPassword = sha256(text.encode('utf-8')).hexdigest()
    return encryptedPassword