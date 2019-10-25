import serial
from datetime import datetime
import sys, os, serial, threading


port = 'COM4' ;
baud = 9600

def monitor() :
    ser = serial.Serial(port, baud ,timeout=0)
    while True:
       line = line.decode()
       line = ser.readline() 
       text = "VT.txt"  (str(datetime.now()))
       


