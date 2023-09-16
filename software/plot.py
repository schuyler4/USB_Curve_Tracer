import sys
sys.path.append("../")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from software.IV import IV_data

# Load in a file using pandas
data = np.array(pd.read_csv("data470.csv"))

current_codes = data[:, 0]
voltage_codes = data[:, 1]

currents, voltages = IV_data(voltage_codes, current_codes)

plt.scatter(voltages, currents)
plt.title("470 Ohm Resistor IV Curve")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.show()