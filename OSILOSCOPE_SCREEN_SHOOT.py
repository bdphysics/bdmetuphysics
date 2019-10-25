import pyvisa as visa
rm = visa.ResourceManager()
scope = rm.open_resource('USB0::0x0699::0x0368::C027917::INSTR')
print (scope.query('*IDN?'))

scope.write('SAVE:IMAG:FILEF PNG')
scope.write('HARDCOPY START')
raw_data=scope.read_raw()

fid = open('osiloscope one channell.png','wb')
fid.write(raw_data)
fid.close()
print ('Done')

