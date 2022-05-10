import serial
import os

while True:
    try:
        ser = serial.Serial('COM4', 9600, timeout=0.1)
    except:
        continue
    finally:
        print('Successfully connected to Serial device')
        break

while True:
    try:
        line = ser.readline().decode()[:-1]
    except:
        os._exit(1)
    print(line)