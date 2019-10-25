import serial
from drawnow import *


VOLT = []

arduinodata = serial.Serial('COM4', 9600)
plt.ion()
count = 0

def makeFig():
    plt.ylim(0, 5)
    plt.xlabel('Time')
    plt.title('Voltage vs Time')
    plt.grid(True)
    plt.ylabel('Voltage v')
    plt.plot(VOLT, 'r', label='voltage')
    plt.legend (loc='lower left')


while True:
    while (arduinodata.inWaiting() == 0):
        pass
    arduinostring = arduinodata.readline().decode()
    dataarray = arduinostring.split('\n')
    sensorvalue = float(arduinostring)
    VOLT.append(sensorvalue)
    drawnow(makeFig)
    plt.pause(.0000001)
    count = count + 1
    if (count > 500):
        VOLT.pop(0)


