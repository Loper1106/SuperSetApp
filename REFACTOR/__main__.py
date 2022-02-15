import sys
import os
from tkinter import *
from PIL import Image, ImageTk
import data
import workoutInit


class Gui:
    def __init__(self):

        # Window Config
        self.window = Tk()
        self.window.title("Super-Set: The App")
        self.screenWidth = 800
        self.screenHeight = 800
        self.window.geometry(f"{self.screenWidth}x{self.screenHeight}")

        # Button Init
        self.intro = Label(self.window, bg="white", text="")
        self.intro.grid(row=0, column=3, columnspan=2, sticky="n")

        button_yes = Button(gui, text="Workout", width=10,
                            command=lambda: self.workout(self.window, self.incompleteWorkouts))
        button_yes.grid(row=8, column=1)

        button_no = Button(gui, text="Exit", width=10, command=quit)
        button_no.grid(row=8, column=7)

        button_save = Button(gui, text="Save", width=10, command=lambda: data.saveProgress(self.window, Workout.completeWorkouts))
        button_save.grid(row=9, column=1)

        button_load = Button(gui, text="Load", width=10, command=lambda: data.loadProgress(self.intro))
        button_load.grid(row=9, column=7)

        button_progress = Button(gui, text="Progress", width=10, command=lambda: data.progress(intro))
        button_progress.grid(row=8, column=3, rowspan=2, columnspan=2, padx=100)

        numSetsReps_Label = Label(gui, bg="white", text="Sets / Reps")
        numSetsReps_Label.grid(row=3, column=1, columnspan=2, sticky="new")

        numSetsReps_Box = Label(gui, width="20", bg="black", fg="white")
        numSetsReps_Box.grid(row=3, column=2, columnspan=2, sticky="new")
        # self.screen = Label(self.screen, image="")
        # self.screen.pack()


if __name__ == "__main__":
    gui = Gui()
    workoutInit.programInit()
    gui.window.mainloop()

sys.exit()
