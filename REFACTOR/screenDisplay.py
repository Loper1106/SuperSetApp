from tkinter import *
import __main__, workoutInit, data

global gui


class Gui:
    def __init__(self):

        # Window Config
        self.window = Tk()
        self.window.title("Super-Set: The App")
        self.screenWidth = 800
        self.screenHeight = 800
        self.window.geometry(f"{self.screenWidth}x{self.screenHeight}")

        # Button Init
        self.intro = Label(self.window, bg="white", text="WELCOME TO THE SUPER-SET APP!")
        self.intro.grid(row=0, column=3, columnspan=2, sticky="n")

        button_yes = Button(self.window, text="Workout", width=10,
                            command=lambda: workoutInit.workout(data.WorkoutDictionary.allWorkouts,
                                                                data.WorkoutDictionary.incompleteWorkouts))
        button_yes.grid(row=8, column=1)

        button_no = Button(self.window, text="Exit", width=10, command=quit)
        button_no.grid(row=8, column=7)

        button_save = Button(self.window, text="Save", width=10,
                             command=lambda: data.saveProgress(self.window, self.Workout.completeWorkouts))
        button_save.grid(row=9, column=1)

        button_load = Button(self.window, text="Load", width=10, command=lambda: data.loadProgress(self.intro))
        button_load.grid(row=9, column=7)

        button_progress = Button(self.window, text="Progress", width=10, command=lambda: data.progress(self.intro))
        button_progress.grid(row=8, column=3, rowspan=2, columnspan=2, padx=100)

        numSetsReps_Label = Label(self.window, bg="white", text="Sets / Reps")
        numSetsReps_Label.grid(row=3, column=1, columnspan=2, sticky="new")

        numSetsReps_Box = Label(self.window, width="20", bg="black", fg="white")
        numSetsReps_Box.grid(row=3, column=2, columnspan=2, sticky="new")
        # self.screen = Label(self.screen, image="")
        # self.screen.pack()


def runHub():
    global gui

    gui = Gui()

    workoutInit.programInit()

    gui.window.mainloop()

