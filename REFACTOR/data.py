import screenDisplay
import workoutInit
import pandas as pd
import numpy as np


class AddNewWorkout:

    # Initialize all Workout Information
    def __init__(self):
        self.workoutName = self
        self.workoutDesc = self
        self.imgLocation = self
        # self.muscleGroup = self


class AllWorkoutLists:

    def __init__(self):
        self.allWorkouts = []
        self.incompleteWorkouts = []
        self.completeWorkouts = []


def importAllWorkouts(dictionary):

    # Opens Workout Spreadsheet as pdArray
    workoutSpreadsheet = pd.read_csv("../resources/data/workoutPicker_R.tsv", sep="\t")
    workoutArray = workoutSpreadsheet.to_numpy()

    #  TURNING ROWS INTO DICTIONARY ENTRIES
    for row in workoutArray:
        np.split(row, 3)
        name, desc, imgLocation = row
        print(name, desc, imgLocation)

        addWorkout = AddNewWorkout()
        addWorkout.workoutName = name
        addWorkout.workoutDesc = desc
        addWorkout.imgLocation = imgLocation

        dictionary.append(addWorkout)


# CLASS FOR WORKOUT DATA
def saveProgress(dialog, complete):

    # Remove boxes when out of workout function
    # screenDisplay.gui.numSetsReps_Box.grid_remove()
    # screenDisplay.gui.numSetsReps_Label.grid_remove()
    # img.grid_remove()
    #
    # saveData = open("resources/data/.workoutPicker_SAVE.tsv", "w+", newline="\n")
    # # Saves completed workouts to file
    # for i in complete:
    #     saveData.writelines(i + "\n")
    # screenDisplay.gui.button_yes["text"] = "Yes"
    # screenDisplay.gui.button_no["text"] = "No"
    # dialog["text"] = "Progress saved! Would you like to continue your workout?"
    # screenDisplay.gui.button_yes["command"] = lambda: Workout.workout(screenDisplay.gui.intro,
    #                                                                   Workout.incompleteWorkouts)
    # screenDisplay.gui.button_no["command"] = quit
    pass


# Generates workout if incomplete workout list is empty
def generateWorkout(allWorkouts, incompleteWorkouts):

    for i in allWorkouts:
        print(i)
        incompleteWorkouts.append(i)
    return


def loadProgress(dialog):

    # Remove boxes when out of workout function
    # screenDisplay.gui.numSetsReps_Box.grid_remove()
    # screenDisplay.gui.numSetsReps_Label.grid_remove()
    # img.grid_remove()
    #
    # Workout.incompleteWorkouts = Workout.newFile()
    # Workout.completeWorkouts = []
    # dialog["text"] = "Load Complete!"
    #
    # # load list of all complete exercises
    # for i in open("resources/data/.workoutPicker_SAVE.tsv"):
    #     exercise = i.strip()
    #     # Ignores workouts if already completed before
    #     if exercise not in Workout.completeWorkouts:
    #         Workout.completeWorkouts.append(exercise)
    #
    # # compares lists to create list of incomplete exercises
    # for x in Workout.completeWorkouts:
    #     for y in Workout.incompleteWorkouts:
    #         if x == y:
    #             Workout.incompleteWorkouts.remove(y)
    #     # Displays complete/incomplete workouts (displays new row of information)
    #     screenDisplay.gui.currentWorkout_Label["text"] = "Complete Workouts: "
    #     screenDisplay.gui.currentWorkout_Box["text"] = Workout.completeWorkouts
    #     screenDisplay.gui.incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
    #     screenDisplay.gui.incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
    #     screenDisplay.gui.incompleteWorkout_Box["text"] = Workout.incompleteWorkouts
    pass


def progress(dialog):

    # Removes boxes when out of workout function
    # screenDisplay.gui.numSetsReps_Box.grid_remove()
    # screenDisplay.gui.numSetsReps_Label.grid_remove()
    # img.grid_remove()
    #
    # dialog["text"] = "Progress Loaded..."
    # screenDisplay.gui.currentWorkout_Label["text"] = "Complete Workouts: "
    # screenDisplay.gui.currentWorkout_Box["text"] = Workout.completeWorkouts
    # screenDisplay.gui.incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
    # screenDisplay.gui.incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
    # screenDisplay.gui.incompleteWorkout_Box["text"] = Workout.incompleteWorkouts
    #
    # # checks if list of incomplete workouts is empty
    # if len(Workout.incompleteWorkouts) == 0:
    #     dialog["text"] = "You have completed all your workouts!"
    print("Test")
    return


NewWorkout = AddNewWorkout()
WorkoutDictionary = AllWorkoutLists()
