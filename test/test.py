import sys

sys.path.append("../")

import os
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
from software.IV import IV_data

import matplotlib.pyplot as plt

MAXIMUM_OFFSET = 0.001
PERCENT_CONVERTER = 100 
MAXIMUM_SLOPE_DIFFERENCE = 15

percent_error = lambda theoretical, experimental: np.abs((experimental - theoretical)/theoretical * PERCENT_CONVERTER)
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
    # https://stackoverflow.com/questions/2499966/python-a-smarter-way-of-string-to-integer-conversion/2500023#2500023
    resistance_value = int(''.join([x for x in data_file if x.isdigit()]))
    current_codes, voltage_codes = get_codes_from_file(data_file)
    currents, voltages = IV_data(voltage_codes, current_codes)
    b, m = polyfit(voltages, currents, 1)
    
    percent_error_resistance = percent_error(resistance_value, conductance(m))
    assert b < MAXIMUM_OFFSET, "The offset is too large."
    assert percent_error_resistance < MAXIMUM_SLOPE_DIFFERENCE, "Not close enough to theoretical resistor."

    print(str(resistance_value) + " ohms PASS")
