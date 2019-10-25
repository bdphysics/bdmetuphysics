import visa
rm = visa.ResourceManager(r'C:Windows\System32\visa32.dll')
rm.list_resources()
print(rm.list_resources()[0])

('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::14::INSTR')
my_instrument = rm.open_resource('GPIB0::14::INSTR')
print(my_instrument.query('*IDN?'))
my_instrument(rm.list_resource()[0])
my_instrument.write("*RST")
