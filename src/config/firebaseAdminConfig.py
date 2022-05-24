import firebase_admin
from os import path, getcwd
from firebase_admin import credentials
from firebase_admin import firestore

rootPath = getcwd()

cred = credentials.Certificate(path.join(rootPath,"src", "firebaseProjectKey.json"))
firebase_admin.initialize_app(cred)

db = firestore.client()