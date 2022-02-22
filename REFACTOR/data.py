import __main__, screenDisplay
import pandas as pd
import numpy as np


def test():
    workoutSpreadsheet = pd.read_csv("../resources/data/workoutPicker_R.tsv", sep="\t")

    tips1 = workoutSpreadsheet.to_numpy()
    print(workoutSpreadsheet)

    for row in tips1:
        np.split(row, 3)
        # DIVIDE ROWS INTO DICT. KEYS
        for item in row:
            print(item)


# CLASS FOR WORKOUT DATA
def saveProgress(dialog, complete):
    # Removes boxes when out of workout function
    screenDisplay.gui.numSetsReps_Box.grid_remove()
    screenDisplay.gui.numSetsReps_Label.grid_remove()
    img.grid_remove()

    saveData = open("resources/data/.workoutPicker_SAVE.tsv", "w+", newline="\n")
    # Saves completed workouts to file
    for i in complete:
        saveData.writelines(i + "\n")
    screenDisplay.gui.button_yes["text"] = "Yes"
    screenDisplay.gui.button_no["text"] = "No"
    dialog["text"] = "Progress saved! Would you like to continue your workout?"
    screenDisplay.gui.button_yes["command"] = lambda: Workout.workout(screenDisplay.gui.intro, Workout.incompleteWorkouts)
    screenDisplay.gui.button_no["command"] = quit


def loadProgress(dialog):
    # Removes boxes when out of workout function
    screenDisplay.gui.numSetsReps_Box.grid_remove()
    screenDisplay.gui.numSetsReps_Label.grid_remove()
    img.grid_remove()

    Workout.incompleteWorkouts = Workout.newFile()
    Workout.completeWorkouts = []
    dialog["text"] = "Load Complete!"

    # load list of all complete exercises
    for i in open("resources/data/.workoutPicker_SAVE.tsv"):
        exercise = i.strip()
        # Ignores workouts if already completed before
        if exercise not in Workout.completeWorkouts:
            Workout.completeWorkouts.append(exercise)

    # compares lists to create list of incomplete exercises
    for x in Workout.completeWorkouts:
        for y in Workout.incompleteWorkouts:
            if x == y:
                Workout.incompleteWorkouts.remove(y)
        # Displays complete/incomplete workouts (displays new row of information)
        screenDisplay.gui.currentWorkout_Label["text"] = "Complete Workouts: "
        screenDisplay.gui.currentWorkout_Box["text"] = Workout.completeWorkouts
        screenDisplay.gui.incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
        screenDisplay.gui.incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
        screenDisplay.gui.incompleteWorkout_Box["text"] = Workout.incompleteWorkouts


def progress(dialog):
    # Removes boxes when out of workout function
    screenDisplay.gui.numSetsReps_Box.grid_remove()
    screenDisplay.gui.numSetsReps_Label.grid_remove()
    img.grid_remove()

    dialog["text"] = "Progress Loaded..."
    screenDisplay.gui.currentWorkout_Label["text"] = "Complete Workouts: "
    screenDisplay.gui.currentWorkout_Box["text"] = Workout.completeWorkouts
    screenDisplay.gui.incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
    screenDisplay.gui.incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
    screenDisplay.gui.incompleteWorkout_Box["text"] = Workout.incompleteWorkouts

    # checks if list of incomplete workouts is empty
    if len(Workout.incompleteWorkouts) == 0:
        dialog["text"] = "You have completed all your workouts!"
