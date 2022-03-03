from cv2 import *
import cv2
import serial
import time
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as md
mpl.use('Agg')
print("Hello World!")
with serial.Serial('/dev/ttyUSB0', timeout = 2, baudrate=115200) as ser:  # open serial port
    x = ser.readline()
    y = x.decode() #translate bytes to string
    z = y[:-2] #removes last two characters, in this case, /r/n
    print(z)
    ser.close()

timestamp = time.time()

try:
    with open('cloverLog.csv', 'a', newline='')as csvfile:
        append2file = csv.writer(csvfile, delimiter=',')
        append2file.writerow([timestamp,z])
except Exception as e:
    print(e)

x = []
y = []
with open('cloverLog.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        x.append(datetime.datetime.fromtimestamp(float(row[0])))
        y.append(int(row[1]))

    plt.xticks( rotation=25 )
    plt.ylabel('Ohms')
#    plt.style.use('dark_background')
    plt.subplots_adjust(bottom=0.2,left=0.2)
    xfmt = md.DateFormatter('%m-%d %H:%M')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    plt.title('Clover sand conductivity')
    plt.plot(x[-1000:],y[-1000:],'g')
    plt.savefig('cloverPlot.png')

cam = VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cam.set(cv2.CAP_PROP_FOCUS,0)
s, img = cam.read()
if s:    # frame captured without any errors
#    namedWindow("cam-test")
#    imshow("cam-test",img)
    waitKey(0)
#    destroyWindow("cam-test")
    cropped = img[:,200:1720]
    rotated = cv2.rotate(cropped,cv2.ROTATE_90_CLOCKWISE)
    imwrite("livecam.jpg",rotated) #save image
