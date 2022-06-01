def handleCreateTeam():
    print("CreateTeam")
def handleSeeNotifications():
    print("SeeNotifications")
def handleSeeTeams():
    print("see teams")
def handleAddFriend():
    print("add friend")
    
MANAGE_TEAMS_CHOICES = {
    "1": handleCreateTeam,
    "2": handleSeeNotifications,
    "3": handleSeeTeams,
    "4": handleAddFriend
}
