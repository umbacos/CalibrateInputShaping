# Copyright (c) 2023 umbacos
#
# if you have a PC, place this script in C:\USERS\<user name>\AppData\Roaming\cura\scripts
# or if you have a Mac, place it here /Users/<user name>/Library/Application Scripts/cura/<latest cura version>/scripts
#
# to be used with the ringing_tower.stl as explained in https://marlinfw.org/docs/gcode/M593.html
#
from ..Script import Script

class CalibrateInputShaping(Script):
    version = "1.0.0"

    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Calibrate Input Shaping",
            "key": "CalibrateInputShaping",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "layer_start":
                {
                    "label": "Start Layer",
                    "description": "At what layer should the Input Shaping test start.",
                    "unit": "",
                    "type": "int",
                    "default_value": 2
                },
                "layer_stop":
                {
                    "label": "Stop Layer",
                    "description": "At what layer should the Input Shaping test stop.",
                    "unit": "",
                    "type": "int",
                    "default_value": 298
                },
                "value_start":
                {
                    "label": "initial value",
                    "description": "Initial value for the Input Shaping parameter.",
                    "type": "float",
                    "default_value": 15.0
                },
                "value_stop":
                {
                    "label": "Final value",
                    "description": "Final value for the Input Shaping parameter.",
                    "type": "float",
                    "default_value": 60.0
                }
            }
        }"""

    def execute(self, data):
        layer_start = self.getSettingValueByKey("layer_start")
        layer_stop = self.getSettingValueByKey("layer_stop")
        value_start = self.getSettingValueByKey("value_start")
        value_stop = self.getSettingValueByKey("value_stop")

        layer_num = 0

        for block in data:
            
            lines = block.strip().split("\n")
            gcode = ""

            for line in lines:

                gcode += line + "\n"

                if ";LAYER_COUNT:" in line:
                    total_layers = int(line[line.index(':')+1 : len(line)])
                    if layer_stop > total_layers:
                        layer_stop = total_layers

                elif ";LAYER:" in line:
                    if layer_num < layer_start:
                        freq = 0.0
                    else:
                        freq = value_start + ((value_stop-value_start) * (layer_num - layer_start)) / (layer_stop - layer_start)
                    gcode += "M593 F" + "{:.2f}".format(freq) + " ; Hz Input Shaping Test layer: " + str(layer_num) + "\n"
                    layer_num += 1

            data[layer_num] = gcode

        return data