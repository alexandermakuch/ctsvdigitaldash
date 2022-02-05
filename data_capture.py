from asyncio import set_event_loop
import obd
import pickle
import numpy as np



data = np.zeros(9)

connection = obd.OBD()
rpm_command = obd.commands.RPM
speed_command = obd.commands.SPEED
temp_command = obd.commands.OIL_TEMP
four = obd.commands.COOLANT_TEMP
five = obd.commands.FUEL_LEVEL
# six = obd.commands.
# seven = obd.commands.
# eight = obd.commands.
# nine = obd.commands.




data[0] = connection.query(rpm_command)
data[1] = connection.query(speed_command)
data[2] = connection.query(temp_command)
data[3] = connection.query(four)
data[4] = connection.query(five)
# data[5] = connection.query(six)
# data[6] = connection.query(seven)
# data[7] = connection.query(eight)
# data[8] = connection.query(nine)

file = open('data_save','wb')
pickle.dump(data, file)
file.close()