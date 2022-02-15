import sys
import os
from tkinter import *
from PIL import Image, ImageTk


class Gui:
    def __init__(self):
        self.screen = Tk()
        self.screen.title("Super-Set: The App")
        self.screenWidth = 800
        self.screenHeight = 800
        self.screen.geometry(f"{self.screenWidth}x{self.screenHeight}")

        self.window = Label(self.screen, image="")
        self.window.pack()


if __name__ == "__main__":
    gui = Gui()

    gui.screen.mainloop()

sys.exit()
