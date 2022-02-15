

# CLASS FOR WORKOUT DATA
def saveProgress(dialog, complete):
    # Removes boxes when out of workout function
    numSetsReps_Box.grid_remove()
    numSetsReps_Label.grid_remove()
    img.grid_remove()

    saveData = open("resources/data/.workoutPicker_SAVE.tsv", "w+", newline="\n")
    # Saves completed workouts to file
    for i in complete:
        saveData.writelines(i + "\n")
    button_yes["text"] = "Yes"
    button_no["text"] = "No"
    dialog["text"] = "Progress saved! Would you like to continue your workout?"
    button_yes["command"] = lambda: Workout.workout(intro, Workout.incompleteWorkouts)
    button_no["command"] = quit


def loadProgress(dialog):
    # Removes boxes when out of workout function
    numSetsReps_Box.grid_remove()
    numSetsReps_Label.grid_remove()
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