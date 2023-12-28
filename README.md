**This project is no Longer active**

# 5axis_Slicer
5 axis semi automatic gcode generator

This piece of software is meant to generate 5axis gcode for cylindrical geometry using aditional A and C axis on a Ultimaker + 3D printer


Here is a list of things to address on the gcode generator

1. bed and nozzle set temperatures are not embedded into the gcode
    I. bed : M140
    II. nozzle : M104

2. Homing is not embedded into the gcode and is to be done beforehand. The print table (C axis) is centred in the middle of the cartesian build table. Z height may vary form machine to machine due to variations form a printer to a same model one.

3. C to A cylinder transition is not handled and is to be done manually through the printer GUI. The code can also embedded into the generated gcode.
    I. Move print head up
    II. Pivot A axis
    III. Move printhead to the EXTREMETY of the cylinder (IS A MUST)
    IV. Move printhead down to printing height over cylinder
    V. Give hand to the generated gcode

4. Collisions between the printhead and buildplate are not handled. Regular Support should be printed on the buildplate to elevate C cylinder geometry.

5. A cylinder Gcode should be printed at 45° (when possible) to reduce:
    I. Risk of the print falling down
    II. A axis moves 
