import pyvisa as visa
import numpy as np
import pylab
from struct import unpack

rm = visa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('USB0::0x0699::0x0368::C027917::INSTR')
print(inst.query("*IDN?"))


inst.write('Data:SOU CH1')
inst.write('DATA:WIDTH 1')
inst.write('DATA:ENC RPB')


ymult = float(inst.ask('WFMPRE:YMULT?'))
yzero = float(inst.ask('WFMPRE:YZERO?'))
yoff = float(inst.ask('WFMPRE:YOFF?'))
xincr = float(inst.ask('WFMPRE:XINCR?'))

inst.write('CURVE?')
data= inst.read_raw()


headerlen = 2 + int (data[1])
header = data[:headerlen]
ADC_wave = data[headerlen:-1]


ADC_wave=np.array(unpack('%sB' % len(ADC_wave),ADC_wave))
Volts = (ADC_wave - yoff)* ymult + yzero
Time = np.arange(0, xincr* len(Volts),xincr)


inst.write('Data:SOU CH2')
inst.write('DATA:WIDTH 1')
inst.write('DATA:ENC RPB')


ymult2 = float(inst.ask('WFMPRE:YMULT?'))
yzero2 = float(inst.ask('WFMPRE:YZERO?'))
yoff2 = float(inst.ask('WFMPRE:YOFF?'))
xincr2 = float(inst.ask('WFMPRE:XINCR?'))

inst.write('CURVE?')
data2= inst.read_raw()


headerlen2 = 2 + int (data[1])
header2 = data[:headerlen2]
ADC_wave2 = data[headerlen2:-1]


ADC_wave2=np.array(unpack('%sB' % len(ADC_wave2),ADC_wave2))
Volts2 = (ADC_wave2 - yoff2)* ymult2 + yzero2
Time2 = np.arange(0, xincr2* len(Volts2),xincr2)

pylab.plot(Time,Volts)
pylab.plot(Time2,Volts2)
pylab.show()
