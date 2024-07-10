from oldresistor import OldResistor

print("_____ klasa OldResistor _____")
r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(160)
print(r0.get_ohms())
