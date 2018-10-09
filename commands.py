##
# Created By Anil Soni
# Interfacing OBD through python
##

import obd
#from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int

__version__ = 0.1
__all__ = ["vin", ]
# supported commands for ADAVD
commands = {"rpm": obd.commands.RPM,
            "maf": obd.commands.MAF,
            "speed": obd.commands.SPEED,
            "fuel": obd.commands.FUEL_STATUS,
            "fuel_type": obd.commands.FUEL_TYPE,
            "fuel_level": obd.commands.FUEL_LEVEL,
            "intake_temp": obd.commands.INTAKE_TEMP,
            "engine_load": obd.commands.ENGINE_LOAD,
            "engine_run_time": obd.commands.RUN_TIME,
            "coolant_temp": obd.commands.COOLANT_TEMP,
            "absolute_load": obd.commands.ABSOLUTE_LOAD
            "distance_travel": obd.commands.DISTANCE_W_MIL,
            "battery_status": obd.commands.HYBRID_BATTERY_REMAINING,
            }

def vin(messages):
    """ Decoder for VIN messages """
    data = messages[0].data
    data = data[2:]
    v = bytes_to_int(data) / 4.0
    return v * OBD.Unit.VIN

vin_command = OBD.OBDCommand("VIN",         # command name
                             "VIN NUMBER",  # description
                             b"0902",       # obd command
                             17,            # number of return bytes to except
                             vin,           # decoding function
                             ECU.ENGINE,    # ECU filter
                             False)         # we don't allow "01" to be added for speed
