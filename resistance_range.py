import matplotlib.pyplot as plt

voltage_reference = 2.5 # Volts
ADC_bits = 12 
shunt_value = 0.1 # Ohms
current_amp_gain = 25 # Volts/Volt
maximum_voltage = 6 # Volts

LSB = voltage_reference/(2**ADC_bits)

# V = I*R*Gain
min_current = LSB/(shunt_value*current_amp_gain)

maximum_resistance = maximum_voltage/min_current
maximum_current = voltage_reference/(shunt_value*current_amp_gain)

print(maximum_resistance)
print(maximum_current)