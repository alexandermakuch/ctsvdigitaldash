import obd
import time

connection = obd.OBD() # auto-connects to USB or RF port

x=0

while x==0:

    t = time.time()

    # c = obd.commands['RPM']
    # print(c)

    elapsed_time = time.time() - t

    print(elapsed_time)
