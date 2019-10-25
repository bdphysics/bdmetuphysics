import serial
from drawnow import *

Resistance = []

arduinodata = serial.Serial('/dev/cu.usbmodem14301', 9600)
plt.ion()
count = 0

def makeFig():
    plt.ylim(0, 2000)
    plt.xlabel('Time')
    plt.title('My LDR data')
    plt.grid(True)
    plt.ylabel('Resistance')
    plt.plot(Resistance, '-bo', label='Resistance ohm')
    plt.legend (loc='lower left')


while True:
    while (arduinodata.inWaiting() == 0):
        pass
    arduinostring = arduinodata.readline().decode()
    dataarray = arduinostring.split('\n')
    sensorvalue = float(arduinostring)
    Resistance.append(sensorvalue)
    drawnow(makeFig)
    plt.pause(.0000001)
    count = count + 1
    if (count > 500):
        Resistance.pop(0)


port = '/dev/cu.usbmodem14301';
baud = 9600

def monitor():
    ser = serial.Serial(port, baud, timeout=0)
    while (1):
        line = ser.readline()
        if (line != ""):
            line = line.decode()
            text = open("ldrdata1.txt","a")
            text.write(line)
            text.close()

monitor()