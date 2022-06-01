from config.firebaseAdminConfig import db

def createTeam(teamData):
    ownerId = teamData.get("ownerId")
    title = teamData.get("title")
    description = teamData.get("description")

    doc_ref_teams = db.collection('teams').document(f"{title}-{ownerId}")
    doc_ref_teams.set({
        'ownerId': ownerId,
        'title': title,
        'description': description,
        'tasks': []
    })
def getTeamInfoById(teamId):
    doc_ref_team = db.collection('teams').document(teamId)
    doc = doc_ref_team.get()
    return doc.to_dict()

