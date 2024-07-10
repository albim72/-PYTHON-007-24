from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

print("_____ klasa OldResistor _____")
r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(160)
print(r0.get_ohms())

print("_____ klasa Resistor _____")
r1 = Resistor(690)
print(r1.ohms)
r1.ohms = 45
print(r1.ohms)

print("_____ klasa VoltageResistance _____")
r2 = VoltageResistance(1.2E3)
print(f'początkowe natężenie prądu: {r2.current} A')
r2.voltage = 50
print(f'napięcie prądu = {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
