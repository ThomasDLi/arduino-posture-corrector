 # arduino-posture-corrector
the slightly messy Arduino code needed for Thomas Li's science fair Arduino posture corrector.


## what the files do
Main project is main.ino

If you don't have a buzzer, use the nobuzzer.ino file instead of main.ino

Download the SharpIR libary for arduino included or it won't work

Optional: the python part. This will display real time 2d graphics that will show what the arduino thinks you're sitting like. COM3 MIGHT NOT BE YOUR USB PORT. REPLACE PORT BEFORE RUNNING SCRIPT.

## how to build the physical device
First wire your sensors up like so (breadboard is for more clear diagram, it's better to just solder the sensors on):

![image](https://user-images.githubusercontent.com/77999105/119068706-940dcf80-b999-11eb-8a6c-7d8de5d66559.png)

If you have a buzzer, and want a buzzer:

![image](https://user-images.githubusercontent.com/77999105/119069048-37f77b00-b99a-11eb-8faf-8f3cac9375ee.png)


Next, download eiter **Main.ino** or **nobuzzer.ino**

After you're done doing thhat, change the pins according to where you attach the sensors

Finally, upload the code to your arduino, and download the **pythonpart.py** file if you want to see real-time graphics regarding your spine
