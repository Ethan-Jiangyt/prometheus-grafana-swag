import time
import socket
import random

# not used in serial version since arduino is what sends the data
def getTime():
    return time.time_ns()

# Initialize stuff
measurement = 'sensorvals'
field_keys = ["pt1", "pt2", "pt3", "pt4", "tc1", "tc2", "tc3", "tc4", "lc"]
field_values = [100 for i in range(9)]

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ('127.0.0.1', 4000)

while True:
    
    # Update data (we'd read from serial here)
    timestamp = getTime()
    for i in range(9):
        field_values[i] = field_values[i] + random.uniform(-1, 1)
    
    # update field string
    fields = ''
    for i in range(9):
        fields += f'{field_keys[i]}={field_values[i]}'
        if i != 8:
            fields += ','
    
    # influx string to send to telegraf
    data = measurement + ' ' + fields + ' ' + str(timestamp)
    UDPClientSocket.sendto(data.encode(), serverAddressPort)


    # to simulate arduino delay
    time.sleep(0.0001)
