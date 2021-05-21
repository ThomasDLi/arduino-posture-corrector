import serial
from tkinter import Tk, Label, IntVar, Canvas, Frame
import time

#serial port
port = serial.Serial('COM5', 9600, timeout=1)
# width of the animation window
animation_window_width = 600
# height of the animation window
animation_window_height = 600

# delay between successive frames in seconds
animation_refresh_seconds = 20

# x start
x_start = 20
distance = 0
# x end
x_end = 20
x_end1 = 20
x_end2 = 20

# y start
y_start = 20

# y end
y_end = 20

spacing = 40 # this is the distance between the sensors in mm

def dataCome():
    while True:
        time_new = 0.0
        time_new = time.time() + 1
        while time.time() <= time_new:
            time.sleep(0.01)
            data = port.readline()
            received = data.decode("ascii").strip().split(",")

            if len(received) > 2:
                data1 = received[0]
                data2 = received[1]
                data3 = received[2]
                return data1, data2, data3

            else:
                continue


# distance = dataCome()


def create_animation_window():
    window = Tk()
    window.title("Tkinter Animation Demo")
    # Uses python 3.6+ string interpolation
    window.geometry(f'{animation_window_width}x{animation_window_height}')
    return window


def create_animation_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="white")
    canvas.pack(fill="both", expand=True)
    return canvas


def animate_line(window, canvas):
    # arguments orderly x_start,y_start,x_end,y_end
    line = canvas.create_line(x_start, y_start, x_end, y_end, fill="red", width=4)
    line2 = canvas.create_line(x_start, y_start + spacing, x_end, y_end + spacing, fill="green", width=4)
    line3 = canvas.create_line(x_start, y_start + spacing * 2, x_end, y_end + spacing * 2, fill="yellow", width=4)
    connect1 = canvas.create_line(x_end, y_end, x_end, y_end + spacing, fill="blue", width=4)
    connect2 = canvas.create_line(x_end, y_end + spacing, x_end, y_end + spacing * 2, fill="blue", width=4)
    xend = 20
    xend2 = 20
    xend3 = 20

    while True:
        # xend = x_start + distance sensor value
        canvas.coords(line, x_start, y_start, xend, y_end)
        canvas.coords(line2, x_start, y_start + spacing, xend2, y_end + spacing)
        canvas.coords(line3, x_start, y_start + spacing * 2, xend3, y_end + spacing * 2)
        canvas.coords(connect1, xend, y_end, xend2, y_end + spacing)
        canvas.coords(connect2, xend2, y_end + spacing, xend3, y_end + spacing * 2)

        distance1 = dataCome()[0]
        distance2 = dataCome()[1]
        distance3 = dataCome()[2]
        distance1 = int(distance1 + "0") // 10
        distance2 = int(distance2 + "0") // 10
        distance3 = int(distance3 + "0") // 10
        #print("distance value:", str(distance1))
        xend = (20 + distance1)
        xend2 = (20 + distance2)
        xend3 = (20 + distance3)
        print(xend)
        print(xend2)
        print(xend3)
        window.update()
        # window.after(animation_refresh_seconds)
        # window.after(animation_refresh_seconds, dataCome)


animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_line(animation_window, animation_canvas)
# animation_window.mainloop()
