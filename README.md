# CalibrateInputShaping
A script for Cura to calibrate input shaping
Tested on Cura 5.2.1

To be used with the ringing_tower.stl as explained in https://marlinfw.org/docs/gcode/M593.html

If you have a PC, place this python script in C:\USERS\ <user name>\AppData\Roaming\cura\scripts
or if you have a Mac, place it here /Users/ <user name>/Library/Application Scripts/cura/<latest cura version>/scripts

then:

- open Cura
- import the ringing_tower.stl
- from the menu select Extensions -> Post Processing -> Modify G-Code
- click "Add a Script"
- select "Calibrate Input Shaping"
- do not change the values in case you are using Marlin's ringing_tower, or unless you know what you are doing
- press "Close"
- slice and print your file
- follow the Marlin guide to tune your input shaper parameters

Ciao!
u.
