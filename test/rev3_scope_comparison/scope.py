import sys

sys.path.append('../../')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from software.plot import get_codes_from_file, IV_data

HARDWARE_REV = 3
SENSE_RESISTOR_VALUE = 10.8 # ohms

scope_data_1N4001 = np.array(pd.read_csv('1N4001_AD3.csv'))
scope_data_1N4148 = np.array(pd.read_csv('1N4148_AD3.csv'))


channel1_1N4001 = scope_data_1N4001[:,1]
channel2_1N4001 = scope_data_1N4001[:,2]
channel1_1N4001 = channel1_1N4001/SENSE_RESISTOR_VALUE

current_codes_1N4001, voltage_codes_1N4001 = get_codes_from_file('1N4001_CT.csv')
currents_1N4001, voltages_1N4001 = IV_data(voltage_codes_1N4001, current_codes_1N4001, HARDWARE_REV)

plt.scatter(voltages_1N4001, currents_1N4001, label='Curve Tracer')
plt.plot(channel2_1N4001, channel1_1N4001, color='red', label='AD3 Scope Curve Trace')
plt.legend()
plt.title('1N4001 Scope Comparison')
plt.xlabel('Diode Voltage (V)')
plt.ylabel('Diode Current (A)')
plt.show()

channel1_1N4148 = scope_data_1N4148[:,1]
channel2_1N4148 = scope_data_1N4148[:,2]
channel1_1N4148 = channel1_1N4148/SENSE_RESISTOR_VALUE

current_codes_1N4148, voltage_codes_1N4148 = get_codes_from_file('1N4148_CT.csv')
currents_1N4148, voltages_1N4148 = IV_data(voltage_codes_1N4148, current_codes_1N4148, HARDWARE_REV)

plt.scatter(voltages_1N4148, currents_1N4148, label='Curve Tracer')
plt.plot(channel2_1N4148, channel1_1N4148, color='red', label='AD3 Scope Curve Trace')
plt.legend()
plt.title('1N4148 Scope Comparison')
plt.xlabel('Diode Voltage (V)')
plt.ylabel('Diode Current (A)')
plt.show()
