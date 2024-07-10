from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

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

print("_____ klasa BoundedResistance _____")
try:
    r3 = BoundedResistance(3.4E2)
    print(f'opór początkowy: {r3.ohms} omów')
    r3.ohms = -90
    print(f'opór: {r3.ohms} omów')
except ValueError as ve:
    print(ve)
