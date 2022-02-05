from asyncio import set_event_loop
import obd
import pickle
import numpy as np



data = []

connection = obd.OBD('COM4')
rpm_command = obd.commands.RPM
speed_command = obd.commands.SPEED
temp_command = obd.commands.OIL_TEMP
four = obd.commands.COOLANT_TEMP
five = obd.commands.FUEL_LEVEL
# six = obd.commands.
# seven = obd.commands.
# eight = obd.commands.
# nine = obd.commands.




data.append(connection.query(rpm_command))
data.append(connection.query(speed_command))
data.append(connection.query(temp_command))
data.append(connection.query(four))
data.append(connection.query(five))


file = open('data_save2','wb')
pickle.dump(data, file)
file.close()