############################
# Gcode generator for 5axis 3d printer (X,Y,Z,A,C)
# Dominique Humbert
# 13.04.2022
############################
 
from cmath import pi
import math
import tkinter as tk
from tkinter import *





def cylinder_C(E, data, Enorm):
##############
# R = external radius
# r = internal radius
# h = heigt
# lineheight
# linewidth
# Gfile = filename
##############
    
    print('cylindre C')                         # Debugging code
    R = float(data[1].get())                    # Gets passed cylinder and print parameters
    r = float(data[2].get())
    h = float(data[3].get())
    lineheight = float(data[4].get())
    linewidth = float(data[5].get())
    Gfile = open(data[6].get(),'w')

    data[0].destroy()                           # closes previous window

    NhStep = h/lineheight                       # calculates nbr of Zmoves to make
    
    NrStep = (R-r)/linewidth                    # calculates nbr of Radiusmoves to make

    #stepPerUnit = 5                            # steps/deg
    setupString1 = 'M92 C5'                     # sets step nbr/unit
    setupString2 = 'M92 A5'                     # sets step nbr/unit
    Gfile.write(setupString1 + setupString2)

    C = 360
    F = 1800                                    # std feedrate
    Fl = 1800*180./math.pi                      # F = Fdeg*180/(pi*r)
    r_postition = R


    Gfile.write(';Cylinder around C\n')

    Start_point = 'G0 X'+str(R) +'\n'
    Gfile.write(Start_point)
    invert = -1                                                 # used to invert X axis direction
    for i in range(int(NhStep)):                                       
        for j in range(int(NrStep)):
            r_postition = R-linewidth*j                         # Calculates extruder's next radius position
            f = 'G1 F'+str(math.ceil(Fl/abs(r_postition)))      # Sets extruder speed on next radius position
            E = E + 2 * abs(r_postition) * 3.14 * Enorm         # Calculates extruder go to next radius position
            c = ' C'+str(C)                                     # writes calculated values into string 
            e = ' E'+str(E)
            Gfile.write(f+c+e)
            Gfile.write('\n')
            x = 'G1 X'+str(pow(invert, i)*linewidth)            # starts from outside-in, then inside-out on the next layer. repeat
            Gfile.write(x)
            Gfile.write('\n')
        Gfile.write(';New layer')
        Gfile.write('\n')
        z = 'G0 Z'+str(lineheight)
        Gfile.write(z)
        Gfile.write('\n')
        
    Gfile.close


    return


def cylinder_A(E, data, Enorm):
##############
# R = external radius
# r = internal radius
# h = heigt
# lineheight
# linewidth
# Gfile = filename
##############

    print('cylindre A')                         # Debugging code
    R = float(data[1].get())                    # Gets passed cylinder and print parameters
    r = float(data[2].get())
    h = float(data[3].get())
    lineheight = float(data[4].get())
    linewidth = float(data[5].get())
    Gfile = open(data[6].get(),'w')

    data[0].destroy()                           # closes previous window

    NhStep = h/linewidth                        # calculates nbr of Zmoves to make
    
    NrStep = (R-r)/lineheight                   # calculates nbr of Radiusmoves to make

    #stepPerUnit = 5                            # steps/deg
    setupString1 = 'M92 Y200'                   # sets step nbr/unit
    setupString2 = 'M92 A200'                   # sets step nbr/unit
    Gfile.write(setupString1 + setupString2)

    C = 360
    F = 1800                                    #std feedrate
    Fl = 1800*180./math.pi                      # F = Fdeg*180/(pi*r)
    r_postition = R


    Gfile.write(';Cylinder around A\n')

    Start_point = 'G0 X'+str(R) +'\n'
    Gfile.write(Start_point)
    invert = -1                                                 # used to inver X axis direction

    for i in range(int(NrStep)):
        r_postition = r+linewidth*i                             # Calculates extruder's next radius position
        f = 'G1 F'+str(math.ceil(Fl/abs(r_postition)))          # Sets extruder speed on next radius position
        E = E + 2 * abs(r_postition) * 3.14 * Enorm             # Calculates extruder go to next radius position

        for j in range(int(NhStep)):    
            c = ' C'+str(C)                                     # writes calculated values into sting 
            e = ' E'+str(E)
            Gfile.write(f+c+e)
            Gfile.write('\n')
            x = 'G1 X'+str(pow(invert, i)*linewidth)            # starts from the extremety, then the other on the next layer. repeat
            Gfile.write(x)
            Gfile.write('\n')
        Gfile.write(';New layer')
        Gfile.write('\n')
        z = 'G0 Z'+str(lineheight)
        Gfile.write(z)
        Gfile.write('\n')
        

    return 1