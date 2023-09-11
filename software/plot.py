import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

adc_resolution = 4096
reference_voltage = 2.5
common_voltage = 6 #V
current_amplifier_gain = 250
lsb = reference_voltage/adc_resolution

voltage_sensor_upper_step_down_resistor = 4700
current_sensor_upper_step_down_resistor = 3240
lower_step_down_resistor = 1000

# Load in the data as a pandas dataframe
df = pd.read_csv('./data.csv')

# Get a list from the second column of the dataframe
voltage_code = df.iloc[:, 0].tolist()
# Get a list from the third column of the dataframe
current_code = df.iloc[:, 1].tolist()

voltage_code = np.array(voltage_code)
current_code = np.array(current_code)

output_voltage = lambda code: code * lsb

def divided_voltage(divider_voltage, upper_resistor):
    return (divider_voltage/lower_step_down_resistor)*(upper_resistor+lower_step_down_resistor)

gain_division = lambda voltage, gain: voltage/gain

voltage_output = divided_voltage(output_voltage(voltage_code), voltage_sensor_upper_step_down_resistor) - common_voltage
current_output = gain_division( divided_voltage(output_voltage(current_code), 
                                                current_sensor_upper_step_down_resistor), 
                                                current_amplifier_gain)

# Plot the data
plt.scatter(voltage_output, current_output)
plt.show()