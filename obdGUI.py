from Tkinter import *
import serial
import time
root = Tk()
#The window size
#root.geometry("800x600")

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
    console.insert(INSERT, "Test data" + "\n")
    #ser.close()
#Widget creation
console = Text(root, width=50, height=20)
bu = Button(root, text="GetRPM", command=getRPM)
#Widget layout
console.grid(row=0, column=0, columnspan=3)
bu.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()