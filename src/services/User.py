from config.firebaseAdminConfig import db

def createUser(userData):
    doc_ref = db.collection('users').document()
    doc_ref.set({
        'id': userData.get("id"),
        'username': userData.get("username"),
        'password': userData.get("password")
    })