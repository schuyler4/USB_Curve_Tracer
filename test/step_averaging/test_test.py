import sys

import matplotlib.pyplot as plt 

sys.path.append('../../')

from software.plot import plot_data, get_codes_from_file
from software.IV import IV_data
from software.step_average import Step_Average
import software.constants as constants

HARDWARE_REV = 3

current_codes, voltage_codes = get_codes_from_file('470.csv')
currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

step_filter = Step_Average(currents, 
                           voltages, 
                           constants.ADC_BIT_RESOLUTION, 
                           constants.DAC_BIT_RESOLUTION)

step_filter()
averaged_voltages = step_filter.averaged_voltages
averaged_currents = step_filter.averaged_currents
step_voltages = step_filter.step_voltages
step_currents = step_filter.step_currents

for i, step_voltage in enumerate(step_voltages):
    step_current = step_currents[i]
    plt.plot(step_voltage, step_current)

plt.scatter(averaged_voltages, averaged_currents)
plt.show()

