import serial
import time
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as md
mpl.use('Agg')
print("Hello World!")
with serial.Serial('/dev/ttyUSB0', timeout = 10, baudrate=115200) as ser:  # open serial port
    ser.write(b's')#send command to output data
    encodedData = ser.readline()
    greenhouseData = encodedData.decode() #translate bytes to string
    greenhouseData = greenhouseData[:-2] #removes last 3 characters, in this case, "/r/n and first "
    print(greenhouseData)
    greenhouseDataList = greenhouseData.split(',')
    temp = greenhouseDataList[0]
    humi = greenhouseDataList[1]
    res = greenhouseDataList[2]
    ser.close()

timestamp = time.time()

try:
    with open('cloverLog.csv', 'a', newline='')as csvfile:
        append2file = csv.writer(csvfile, delimiter=',')
        append2file.writerow([timestamp,res,temp,humi])
except Exception as e:
    print(e)

x = []
resData = []
humiData = []
tempData = []
with open('cloverLog.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        x.append(datetime.datetime.fromtimestamp(float(row[0])))
        resData.append(int(row[1]))
        tempData.append(float(row[2]))
        humiData.append(float(row[3]))
#    plt.ylim(100000,6000000)
    plt.xticks( rotation=25 )
    plt.ylabel('Ohms')
#    plt.style.use('dark_background')
    plt.subplots_adjust(bottom=0.2,left=0.2)
    xfmt = md.DateFormatter('%m-%d %H:%M')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    plt.title('Soil Resistance')
    plt.plot(x[-500:],resData[-500:],'g')
    plt.savefig('cloverPlot.png')
    plt.clf()

    plt.xticks( rotation=25 )
    plt.ylabel('%RH')
#    plt.style.use('dark_background')
    plt.subplots_adjust(bottom=0.2,left=0.2)
    xfmt = md.DateFormatter('%m-%d %H:%M')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    plt.title('Humidity')
    plt.plot(x[-500:],humiData[-500:],'g')
    plt.savefig('humiPlot.png')
    plt.clf()

    plt.xticks( rotation=25 )
    plt.ylabel('*C')
#    plt.style.use('dark_background')
    plt.subplots_adjust(bottom=0.2,left=0.2)
    xfmt = md.DateFormatter('%m-%d %H:%M')
    ax=plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    plt.title('Temperature')
    plt.plot(x[-500:],tempData[-500:],'g')
    plt.savefig('tempPlot.png')


