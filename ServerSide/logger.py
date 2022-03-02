import serial
import time
import csv

print("Hello World!")
with serial.Serial('/dev/ttyUSB0', timeout = 1, baudrate=115200) as ser:  # open serial port
    x = ser.readline()
    y = x.decode() #translate bytes to string
    z = y[:-2] #removes last two characters, in this case, /r/n
    print(z)
    ser.close()

timestamp = time.time()

try:
    with open('cloverLog.csv', 'a', newline='')as csvfile:
        append2file = csv.writer(csvfile, delimiter=' ')
        append2file.writerow([timestamp,z])
except Exception as e:
    print(e)
