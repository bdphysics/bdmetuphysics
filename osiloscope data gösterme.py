import visa
import numpy as np
import pylab
from struct import unpack

rm=visa.ResourceManager(r'C:\WINDOWS\system32\visa32.dll')
print(rm.list_resources())
inst=rm.open_resource('USB0::0x0699::0x0368::C027917::INSTR')
print(inst.query("*IDN?"))


inst.write('Data:SOU CH1')
inst.write('DATA:WIDTH 1')
inst.write('DATA:ENC RPB')

ymult= float(inst.ask('WFMPRE:YMULT?'))
yzero= float(inst.ask('WFMPRE:YZERO?'))
yoff= float(inst.ask('WFMPRE:YOFF?'))
xincr= float(inst.ask('WFMPRE:XINCR?'))


inst.write('CURVE?')
data =inst.read_raw()
headerlen= 2 + int(data[1])
header=data[:headerlen]
ADC_wave= data[headerlen:-1]

ADC_wave =np.array(unpack('%sB' % len(ADC_wave),ADC_wave))
Volts =(ADC_wave - yoff) * ymult +yzero
Time= np.arrange(0,xincr * len(Volts),xincr)

pylab.plot(Time,Volts)
pylab.show()
