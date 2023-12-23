import sys

sys.path.append('../../')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from software.plot import get_codes_from_file, IV_data

HARDWARE_REV = 3

scope_data_1N4001 = np.array(pd.read_csv('1N4001.csv'))
scope_data_1N4148 = np.array(pd.read_csv('1N4148.csv'))

time = scope_data_1N4001[:,0]

N = 1
print(N)

channel1 = scope_data_1N4001[:,1]
channel2 = scope_data_1N4001[:,2]

channel2 = np.convolve(channel2, np.ones(N)/N, mode='valid')

current_codes, voltage_codes = get_codes_from_file('1N4148_CT.csv')
currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

channel1 = scope_data_1N4148[:,1]
channel2 = scope_data_1N4148[:,2]

channel2 = np.convolve(channel2, np.ones(N)/N, mode='valid')

current_codes, voltage_codes = get_codes_from_file('1N4148_CT.csv')
currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

plt.plot(channel1, channel2)
plt.show()