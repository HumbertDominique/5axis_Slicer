from inspect import Parameter
from ProjMultiTypes import programmState
import tkinter as tk
from tkinter import *
import cylinders    

def select_geometry_C(E, Enorm):
    programm_State = programmState.geometry_cylinder_C
    print(programm_State)                            # Debugging code
    print('Data cylindre C')                         # Debugging code

    parameterWin = tk.Toplevel()                     # New window ontop of the other
    parameterWin.grab_set()                          # Old window disabled for as long as this one is open
    parameterWin.title('Cylinder geometry')
    label = tk.Label(parameterWin,
            text = "Input your cylinder geometry around C",
            fg = "black",
            bg = "white",
            width = 30,
            height = 1
        )
    label.pack(expand=True)

    canvas = Canvas(parameterWin, width = 600, height = 800)        # make space for a image, text and textboxes 
         

    frame_image = Frame(parameterWin, borderwidth=2, bg="white", relief=SUNKEN)
    frame_image.pack(side=TOP, fill="x")

    frame_image.picture = PhotoImage(file="geom1.gif")              # Load the picture
    frame_image.label = Label(frame_image, image=frame_image.picture)
    frame_image.label.pack()                                        # Send the pic

    L1 = tk.Label(parameterWin,text="R",)                           # Creating all needed labels, warnings and input boxes
    L2 = tk.Label(parameterWin,text="r",)
    L3 = tk.Label(parameterWin,text="h",)
    L4 = tk.Label(parameterWin,text="Lineheight",)
    L5 = tk.Label(parameterWin,text="linewidth",)
    L6 = tk.Label(parameterWin,text="Filename",)
    L_Warning = tk.Label(parameterWin,text="Only positive values in [mm] and 0 <= r < R",)
    E1 = tk.Entry(parameterWin)
    E2 = tk.Entry(parameterWin)
    E3 = tk.Entry(parameterWin)
    E4 = tk.Entry(parameterWin)
    E5 = tk.Entry(parameterWin)
    E6 = tk.Entry(parameterWin)
    #
    L1.pack()                       # sending everything in the right order to display properly
    E1.pack()
    L2.pack()

    E2.pack()
    L3.pack()
    E3.pack()
    L_Warning.pack()
    L4.pack()
    E4.pack()
    L5.pack()
    E5.pack()
    L6.pack()
    E6.pack()

    data = [parameterWin, E1, E2, E3, E4, E5, E6]   # Packing all parameter to send it to function (could be done when 1st declared)

    button_validate = tk.Button(parameterWin,       # Will validate data an go onto nex programm state
        text='Generate',command=lambda: cylinders.cylinder_C(E, data, Enorm), width=25, height=5, bg="white", fg="black",)
    button_validate.pack()
    parameterWin.mainloop()

    return


############################
# Gcode generator for 5axis 3d printer (X,Y,Z,A,C)
# Dominique Humbert
# 13.04.2022
############################

def select_geometry_A(E, Enorm):
    programm_State = programmState.geometry_cylinder_A
    print(programm_State)                            # Debugging code
    print('Data cylindre A')                         # Debugging code


    parameterWin = tk.Toplevel()                     # New window ontop of the other
    parameterWin.grab_set()                          # Old window disabled for as long as this one is open
    parameterWin.title('Cylinder geometry around A')
    label = tk.Label(parameterWin,
            text = "Input your cylinder geometry",
            fg = "black",
            bg = "white",
            width = 30,
            height = 1
        )
    label.pack(expand=True)

    canvas = Canvas(parameterWin, width = 600, height = 800)        # make space for a image, text and textboxes      
         

    frame_image = Frame(parameterWin, borderwidth=2, bg="white", relief=SUNKEN)
    frame_image.pack(side=TOP, fill="x")

    frame_image.picture = PhotoImage(file="geom1.gif")              # Load the picture
    frame_image.label = Label(frame_image, image=frame_image.picture)
    frame_image.label.pack()                                        # Send the pic

    L1 = tk.Label(parameterWin,text="R",)                           # Creating all needed labels, warnings and input boxes
    L2 = tk.Label(parameterWin,text="r",)
    L3 = tk.Label(parameterWin,text="h",)
    L4 = tk.Label(parameterWin,text="Lineheight",)
    L5 = tk.Label(parameterWin,text="linewidth",)
    L6 = tk.Label(parameterWin,text="Filename",)
    L_Warning = tk.Label(parameterWin,text="Only positive values in [mm] and 0 <= r < R",)
    E1 = tk.Entry(parameterWin)
    E2 = tk.Entry(parameterWin)
    E3 = tk.Entry(parameterWin)
    E4 = tk.Entry(parameterWin)
    E5 = tk.Entry(parameterWin)
    E6 = tk.Entry(parameterWin)
    #
    L1.pack()
    E1.pack()
    L2.pack()

    E2.pack()
    L3.pack()
    E3.pack()
    L_Warning.pack()
    L4.pack()
    E4.pack()
    L5.pack()
    E5.pack()
    L6.pack()
    E6.pack()

    data = [parameterWin, E1, E2, E3, E4, E5, E6]   # Packing all parameter to send it to function (could be done when 1st declared)

    button_validate = tk.Button(parameterWin,       # Will validate data an go onto nex programm state
        text='Generate',command=lambda: cylinders.cylinder_A(E, data, Enorm), width=25, height=5, bg="white", fg="black",)
    button_validate.pack()
    parameterWin.mainloop()
