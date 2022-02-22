import data
import screenDisplay


class WorkoutLists:

    def __init__(self):
        self.allWorkouts = []
        self.incompleteWorkouts = []
        self.completeWorkouts = []


def programInit():

    dictionary = WorkoutLists()
    data.importAllWorkouts(dictionary.allWorkouts)

    # DEBUG
    for i in dictionary.allWorkouts:
        print("NEW ITERATION")
        print("Name: ", i.workoutName)
        print("Description: ",i.workoutDesc)
        print("File Location: ", i.imgLocation)
        print()

    ##############
    # DIALOG BOX #
    ##############
    screenDisplay.gui.intro["text"] = "Would you like to workout?"
