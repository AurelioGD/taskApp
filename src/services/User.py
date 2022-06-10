from config.firebaseAdminConfig import db

def createUserService(userData):
    doc_ref = db.collection('users').document()
    doc_ref.set({
        'id': userData.get("id"),
        'username': userData.get("username"),
        'password': userData.get("password"),
        'keyword': userData.get("keyword"),
        'tasks': [],
        'friends': [],
        'teams': [],
    })
    
def getUserByUsernameAndPassword(username, password):
    coll_ref = db.collection('users').where("username", "==", username).where("password", "==", password)
    dbResponse = coll_ref.stream()
    userData = []
    for doc in dbResponse:
        data = doc.to_dict()
        data["idDoc"] = doc.id
        userData.append(data)
    return userData