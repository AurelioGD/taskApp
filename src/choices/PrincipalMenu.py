from utils.cleanTerminal import cleanTerminal
from utils.Graphics import drawManageTeamsMenu
from choices.ManageTeams import MANAGE_TEAMS_CHOICES

def handlefilterBy():
    print("FilterMenu")

def handleAddNewTask():
    print("AddNewTask")

def handleEditTask():
    print("EditTask")

def handleDeleteTask():
    print("DeleteTask")

def handleManageTeams():
    cleanTerminal()
    while True:
        choice = drawManageTeamsMenu()
        cleanTerminal()
        if choice == "5": break;
        MANAGE_TEAMS_CHOICES.get(choice)()


PRINCIPAL_MENU_CHOICES = {
    "1": handlefilterBy,
    "2": handleAddNewTask,
    "3": handleEditTask,
    "4": handleDeleteTask,
    "5": handleManageTeams
}