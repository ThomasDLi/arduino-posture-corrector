#do pip3 install pyserial before running
import serial
import time
port = serial.Serial("COM3", 9600, timeout=1)
while 1:
    time.sleep(0.1)
    data = port.readline()
    recived = data.decode("ascii").strip().split(",")
    if len(recived) > 1:
        data1 = recived[0]
        data2 = recived[1]
        print(data1, data2)
