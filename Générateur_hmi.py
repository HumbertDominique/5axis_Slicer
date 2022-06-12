############################
# Gcode generator for 5axis 3d printer (X,Y,Z,A,C)
# Dominique Humbert
# 13.04.2022
############################

# Step angle = 1.8°
# layer height = 0.15mm
# line width = 0.35mm

import tkinter as tk
from tkinter import ttk

from ast import If
from pickle import TRUE
from turtle import end_fill
from xml.etree.ElementTree import PI

####### FUNCTIONS ######
import select_geometry  # Handles cylinder and print parameters recovery
import cylinders        # Draws the actual cylinder


####### TYPES####
import ProjMultiTypes   # Is meant to use the program as a state machine - is not implemented that way for mow
##############################


Enorm = 0.0945          # Extrusion rate normalised [1/mm]

##############################
# Variables initializations
X=0
Y=0
Z=0
A=0
C=0
E=0

####SETUP#####

#global programm_State
programm_State = ProjMultiTypes.programmState.startup   # Meant to serve as state machine state (not relly implemented)


print(ProjMultiTypes.programmState.startup)
if programm_State == ProjMultiTypes.programmState.startup :
    #STARTUP CODE

    window = tk.Tk()                # Opens a GUI window
    # label = tk.Label(
    #     text = "startup",
    #     fg = "black",
    #     bg = "white",
    #     width = 30,
    #     height = 15
    # )
    # label.pack()

    print("Startup")                # Debugging code
    programm_State = ProjMultiTypes.programmState.geometry_selection

if programm_State == ProjMultiTypes.programmState.geometry_selection :      # initalisation of 3 buttons going to next program level or exit
    print("Geometry selection")
    buttonCylinder_C = tk.Button(
        text="Cylinder around C",
            command=lambda: select_geometry.select_geometry_C(E, Enorm),    
            width=25,
            height=5,
            bg="white",
            fg="black",
            )
    buttonCylinder_A = tk.Button(
        text="Cylinder around A",
            command=lambda: select_geometry.select_geometry_A(E, Enorm),
            width=25,
            height=5,
            bg="white",
            fg="black",
            )
    buttonExit = tk.Button(
            text='Exit',
            command=window.destroy,
            width=25,
            height=5,
            bg="white",
            fg="black",
            )
    buttonCylinder_C.pack() #.pack() sends command/button/teyt/... to GUI window
    buttonCylinder_A.pack()
    buttonExit.pack()       
    window.mainloop()       # Makes the programm wait on a button press
      
print('Exit')