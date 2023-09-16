import sys

sys.path.append("../")

import os
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
from software.IV import IV_data

percent_error = lambda theoretical, experimental: np.abs((experimental - theoretical)/theoretical * 100)
conductance = lambda resistance: 1/resistance

def find_data_files():
    files = []
    for file in os.listdir():
        if file.endswith(".csv"):
            files.append(file)
    return files

def get_codes_from_file(filename):
    data = np.array(pd.read_csv(filename))
    current_codes = data[:, 0]
    voltage_codes = data[:, 1]
    return current_codes, voltage_codes

for data_file in find_data_files():
    current_codes, voltage_codes = get_codes_from_file(data_file)
    currents, voltages = IV_data(voltage_codes, current_codes)
    #b, m = polyfit(voltage_output, current_output, 1)


# Find the line of best fit




print(find_data_files())