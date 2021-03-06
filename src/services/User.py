from config.firebaseAdminConfig import db
from utils.encryptToSha256 import encryptToSha256

def createUserService(userData):
    doc_ref = db.collection('users').document()
    passwordEncrypted = encryptToSha256(userData.get("password"))
    doc_ref.set({
        'username': userData.get("username"),
        'password': passwordEncrypted,
        'keyword': userData.get("keyword"),
        'tasks': [],
        'friends': [],
        'teams': [],
    })
    
def getUserByUsernameAndPassword(username, password):
    query = db.collection('users').where("username", "==", username).where("password", "==", password)
    dbResponse = query.stream()
    userData = []
    for doc in dbResponse:
        data = doc.to_dict()
        data["idDoc"] = doc.id
        userData.append(data)
    return userData
def getUserByDocId(userDocId):
    query = db.collection('users').document(userDocId)
    user = query.get()
    userData = user.to_dict()
    if userData == None:
        return False
    userData["idDoc"] = user.id
    return userData
    
def getPasswordHashByUsername(username):
    query = db.collection('users').where("username", "==", username)
    dbResponse = query.stream()
    userData = []
    for doc in dbResponse:
        data = doc.to_dict()
        data["idDoc"] = doc.id
        userData.append(data)
    if len(userData) == 0: return userData
    return userData[0].get("passwordHash")
