import obd
import time
import numpy as np

connection = obd.OBD()
com = obd.commands.RPM
queries = 1000
times = np.zeros(queries)

for i in range(queries):
    t=time.time()
    rpm = connection.query(com)
    times[i] = time.time()-t

mean_time = np.mean(times)
print('Average query time was {} seconds for 1000 iterations ({} ms)'.format(mean_time, mean_time*1000))


