#do pip3 install pyserial before running
import serial
import time
import tkinter as tk
from tkinter import ttk, IntVar
import threading
port = serial.Serial("COM3", 9600, timeout=1)
def deeta():
    while 1:
        time_new = 0.0
        time_new = time.time() + 1
        while time.time() <= time_new:
            time.sleep(0.1)
            data = port.readline()
            recived = data.decode("ascii").strip().split(",")
            if len(recived) > 1:
                global value1
                global value2
                data1 = recived[0]
                data2 = recived[1]
                value1.set(data1)
                value2.set(data2)
                print(data1, data2)
            else:
                continue


readdata = threading.Thread(target=deeta)

root = tk.Tk()

root.geometry("400x400")

root.title("Sensor display with tkinter")

value1 = IntVar()
value2 = IntVar()

label_sensor_1 = tk.Label(text="Angle top=")
label_sensor_1.grid(row=0, column=0)
label_sensor_top_value = tk.Label(textvariable=value1)
label_sensor_top_value.grid(row=0, column=1)

label_sensor_2 = tk.Label(text="Angle bottom=")
label_sensor_2.grid(row=1, column=0)
label_sensor_middle_value = tk.Label(textvariable=value2)
label_sensor_middle_value.grid(row=1, column=1)

readdata.start()

root.mainloop()
