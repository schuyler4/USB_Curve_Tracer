import sys

sys.path.append('../../')

from software.IV import IV_data
from software.plot import get_codes_from_file

import matplotlib.pyplot as plt
import pandas as pd

HARDWARE_REV = 3

def get_manual_measurements(filename):
    manual = pd.read_csv(filename).to_numpy()
    return manual[:,0], manual[:,1]

current_codes, voltage_codes = get_codes_from_file('1N4001_CT.csv')
currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

manual_currents, manual_voltages = get_manual_measurements('1N4001_manual.csv')

plt.title('1N4001 Comparison Test')
plt.scatter(voltages, currents, label='Curve Tracer Measurement')
plt.scatter(manual_voltages, manual_currents, color='red', label='Manual Measurement')
plt.legend()
plt.show()

current_codes, voltage_codes = get_codes_from_file('1N4148_CT.csv')
currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

manual_currents, manual_voltages = get_manual_measurements('1N4148_manual.csv')

print(manual_currents, manual_voltages)

plt.title('1N4148 Comparison Test')
plt.scatter(voltages, currents, label='Curve Tracer Measurement')
plt.scatter(manual_voltages, manual_currents, color='red', label='Manual Measurement')
plt.legend()
plt.show()

