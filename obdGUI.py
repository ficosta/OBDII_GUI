from Tkinter import *
import serial
import time
import random
root = Tk()
#The window size
root.geometry("320x240")

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

#Widget creation
console = Text(root, width=5, height=1, font=("Helvetica", 32))
bu = Label(root, text="RPM")

#Widget layout
console.grid(row=0, column=0, columnspan=3)
bu.grid(row=1, column=1, padx=5, pady=5)

root.after(500, getRPM)
root.mainloop()