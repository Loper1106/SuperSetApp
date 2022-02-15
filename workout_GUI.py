from tkinter import *
from PIL import Image, ImageTk
import random, time

gui = Tk()

# WINDOW CONFIGURATION
gui.title("Workout Picker By: Ben Loper")
gui.iconbitmap("resources/image/iconn.ico")
gui.configure(bg="#FFFDD0")
gui.resizable(False, False)  # Removes ability to adjust window size
gui.geometry("750x750")
gui.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
gui.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

# Live time update(Military Time)
time_string = time.strftime('%H:%M:%S')
time_label = Label(gui, text=time_string, bg="White")
time_label.grid(row=0, column=0, columnspan=3, sticky="n")

##############
# DIALOG BOX #
##############
intro = Label(gui, bg="white", text="Would you like to workout?")
intro.grid(row=0, column=3, columnspan=2, sticky="n")

# CURRENT WORKOUT LINE (LABEL AND TEXTBOX)
currentWorkout_Label = Label(gui, bg="white", text="Current Workout: ")
currentWorkout_Label.grid(row=2, column=0, columnspan=2, sticky="ew")
currentWorkout_Box = Label(gui, width="20", bg="black", fg="white", borderwidth="5")
currentWorkout_Box.grid(row=2, column=2, columnspan=2, sticky="ew")

# INCOMPLETE WORKOUT LINE (LABEL AND TEXTBOX) (DISPLAYS ONLY IN WORKOUT FUNCTION)
incompleteWorkout_Label = Label(gui, bg="white", text="Incomplete Workouts: ")
incompleteWorkout_Box = Label(gui, width="20", bg="black", fg="white", borderwidth="5")

# NUMBER OF REPS AND SETS (LABEL AND TEXTBOX) (DISPLAYS ONLY IN WORKOUT FUNCTION)
numSetsReps_Label = Label(gui, bg="white", text="Sets / Reps")
numSetsReps_Box = Label(gui, width="20", bg="black", fg="white")

# INITIALIZING IMAGE LABEL
img = Label(gui)


# DISPLAYS TIME WITHIN WINDOW
def updateTime():
    newTime = time.strftime('%H:%M:%S')
    time_label.configure(text=newTime)

    # Repeats function every second
    gui.after(1000, updateTime)


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

    # Displays complete/incomplete workouts (displays new row of information)
    currentWorkout_Label["text"] = "Complete Workouts: "
    currentWorkout_Box["text"] = Workout.completeWorkouts
    incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
    incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
    incompleteWorkout_Box["text"] = Workout.incompleteWorkouts


def progress(dialog):
    # Removes boxes when out of workout function
    numSetsReps_Box.grid_remove()
    numSetsReps_Label.grid_remove()
    img.grid_remove()

    dialog["text"] = "Progress Loaded..."
    currentWorkout_Label["text"] = "Complete Workouts: "
    currentWorkout_Box["text"] = Workout.completeWorkouts
    incompleteWorkout_Label.grid(row=3, column=0, columnspan=2, sticky="new")
    incompleteWorkout_Box.grid(row=3, column=2, columnspan=2, sticky="new")
    incompleteWorkout_Box["text"] = Workout.incompleteWorkouts

    # checks if list of incomplete workouts is empty
    if len(Workout.incompleteWorkouts) == 0:
        dialog["text"] = "You have completed all your workouts!"


class Workout:

    # Initializes Variables
    def __init__(self):
        self.workoutDictionary = {}
        self.incompleteWorkouts = []
        self.completeWorkouts = []

    # Creates new lists on start of program
    def newFile(self):
        self.incompleteWorkouts = []
        self.completeWorkouts = []
        with open("resources/data/workoutPicker_R.tsv") as file:
            for i in file:
                line = i.strip().split("\t")
                key, value = line
                self.workoutDictionary[key] = value
                self.incompleteWorkouts.append(key)
        return self.incompleteWorkouts

    # GENERATES A WORKOUT FROM CLASS WORKOUT DATA
    def workout(self, dialog, complete):
        incompleteWorkout_Label.grid_remove()
        incompleteWorkout_Box.grid_remove()
        currentWorkout_Label["text"] = "Current Workout: "
        button_yes["text"] = "Workout"
        button_no["text"] = "Exit"

        # checks if list of incomplete workouts is empty
        if len(complete) == 0:
            currentWorkout_Box["text"] = "Workouts Complete!"
            img.configure(image=ImageTk.PhotoImage(Image.open("resources/image/null.jpg")))
            dialog["text"] = "Would you like more workouts?"
            button_yes["text"] = "Yes"
            button_no["text"] = "No"
            button_yes["command"] = complete = Workout.newFile()
            button_yes["command"] = lambda: self.workout(intro, complete)
            return

        # Pulls random workout from list
        workoutNum = random.randint(0, len(complete) - 1)  # generates random index to select workout
        dialog["text"] = "Selected Workout: " + complete[workoutNum]

        numSetsReps_Label.grid(row=3, column=1, columnspan=2, sticky="new")
        numSetsReps_Box.grid(row=3, column=2, columnspan=2, sticky="new")
        img.grid(row=6, column=3)

        # Generates random number of sets (3-4) and reps (12-15) (HARDCODED)
        numsets = random.randint(3, 4)
        numreps = random.randint(12, 15)
        numSetsReps_Box["text"] = str(numsets) + " / " + str(numreps)

        # Changes image to directory of image from workout dictionary key (based on workout chosen)
        desc = ImageTk.PhotoImage(Image.open(Workout.workoutDictionary.get(complete[workoutNum])))
        try:
            img.configure(image=desc)
            img.image = desc
        except TclError:
            img.configure(image=ImageTk.PhotoImage(Image.open("resources/image/null.jpg")))

        Workout.completeWorkouts.append(complete[workoutNum])
        complete.pop(workoutNum)

        currentWorkout_Box["text"] = complete


# Initialize Class
Workout = Workout()

# CREATES WORKOUT DICTIONARY FROM .TSV FILE
Workout.incompleteWorkouts = Workout.newFile()

# STANDARD YES/NO BUTTONS (FOR ALL PROGRAM)
button_yes = Button(gui, text="Workout", width=10, command=lambda: Workout.workout(intro, Workout.incompleteWorkouts))
button_yes.grid(row=8, column=1)
button_no = Button(gui, text="Exit", width=10, command=quit)
button_no.grid(row=8, column=7)
button_save = Button(gui, text="Save", width=10, command=lambda: saveProgress(intro, Workout.completeWorkouts))
button_save.grid(row=9, column=1)
button_load = Button(gui, text="Load", width=10, command=lambda: loadProgress(intro))
button_load.grid(row=9, column=7)
button_progress = Button(gui, text="Progress", width=10, command=lambda: progress(intro))
button_progress.grid(row=8, column=3, rowspan=2, columnspan=2, padx=100)

# RUNS THE 'updateTime' INDEFINITELY
gui.after(0, updateTime)
gui.mainloop()
