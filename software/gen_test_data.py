import numpy as np
import matplotlib.pyplot as plot

VT = 25.852e-3
IS = 25e-9
n = 1

def diode_current(forward_voltage):
    return IS*(exp(forward_voltage/(n*VT)) - 1)

forward_voltages = np.linspace(0, 2, 1000)

vectorized_diode_current = np.vectorize(diode_current)
print(vectorized_diode_current(forward_voltages))

print(currents)
