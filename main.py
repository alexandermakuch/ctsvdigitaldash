import obd
import time
from Calculations import vehicle

connection = obd.OBD()
rpm_command = obd.commands.RPM
speed_command = obd.commands.SPEED
temp_command = obd.commands.OIL_TEMP


# queries = 1000
# times = np.zeros(queries)

# for i in range(queries):
#     t=time.time()
#     rpm = connection.query(rpm_command)
#     times[i] = time.time()-t

# mean_time = np.mean(times)
# print('Average query time was {} seconds for 1000 iterations ({} ms)'.format(mean_time, mean_time*1000))

car = vehicle()


def calcSpeed(rpm_prev,speed_prev,rpm_current):
    '''
    inputs: rpm at last recorded speed, previous speed, current rpm
    output: speed at current rpm
    '''
    if rpm_prev > rpm_current:
        return speed_prev
    else:
        return (speed_prev*rpm_current / rpm_prev)


def routine1():
    t=time.time()
    rpm = connection.query(rpm_command)
    speed = connection.query(rpm_command)
    temp = connection.query(rpm_command)
    print(rpm,speed,temp)
    print('Query took {} ms'.format(1000*(time.time()-t)))
    try:
        car.findgear(rpm.value.magnitude,speed.value.magnitude)
    except AttributeError:
        print('error calculating gear!')
    try:
        return rpm.value.magnitude,speed.value.magnitude,temp.value.magnitude,vehicle.gear
    except:
        print('failed returning values!')
        return 0, 0, 0, 0
        


# def routine2():
#     pass


#     return 