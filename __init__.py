##
# Created By Anil Soni
# Interfacing OBD through python
##

import obd

from . import commands

__version__ = 0.1


# we are assuming it will auto connect to obd available under
# Bluetooth or USB
car = obd.OBD()

#car.supported_commands.add(vin)

# check weather the command is running or not
# add to supported commands if th VIN command(0902), is avail under this car
if car.query(commands.vin_command, force=True):
    car.supported_commands.add(commands.vin)
    commands["vin"] = obd.commands.VIN
