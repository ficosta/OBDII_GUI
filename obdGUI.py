from Tkinter import *
import serial
import time
import random

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#Uncomment the line below to allow full screen.
#root.overrideredirect(1)
root.focus_set()
root.geometry("%dx%d+0+0" % (w, h))
root.bind("<Escape>", lambda e: e.widget.quit())


def getRPM():
    #ser = serial.Serial('/dev/ttyUSB0',
    #                    baudrate = 38400,
    #                    parity = serial.PARITY_NONE,
    #                    stopbits = serial.STOPBITS_ONE,
    #                    bytesize = serial.EIGHTBITS,
    #                    timeout = 0)
    #ser.flushInput()
    #ser.flushOutput()
    #serial.write("010C\r")
    #time.sleep(.15)
    #data = ser.readline()
    console.delete(1.0, END)
    console.insert(INSERT, str(random.randint(1000, 10000)))
    #console.insert(INSERT, str(data))
    #ser.close()
    root.after(500, getRPM)

def getMPH():
    #ser = serial.Serial('/dev/ttyUSB0',
    #                    baudrate = 38400,
    #                    parity = serial.PARITY_NONE,
    #                    stopbits = serial.STOPBITS_ONE,
    #                    bytesize = serial.EIGHTBITS,
    #                    timeout = 0)
    #ser.flushInput()
    #ser.flushOutput()
    #serial.write("010C\r")
    #time.sleep(.15)
    #data = ser.readline()
    console2.delete(1.0, END)
    console2.insert(INSERT, str(random.randint(0, 120)))
    #console.insert(INSERT, str(data))
    #ser.close()
    root.after(500, getMPH)

#RPM Widget creation
console = Text(root, width=5, height=1, font=("Helvetica", 64))
label = Label(root, text="RPM", font=("Helvetica", 32))

#RPM Widget layout
console.grid(row=0, column=0, columnspan=3)
label.grid(row=1, column=1, padx=5, pady=5)

#MPH Widget creation
console2 = Text(root, width=4, height=1, font=("Helvetica", 64))
label2 = Label(root, text="MPH", font=("Helvetica", 32))

#MPH Widget layout
console2.grid(row=0, column=4, columnspan=3)
label2.grid(row=1, column=5, padx=5, pady=5)

root.after(500, getRPM)
root.after(500, getMPH)

root.mainloop()