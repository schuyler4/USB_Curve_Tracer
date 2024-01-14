import sys

sys.path.append('../../')

import os
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit

from software.IV import IV_data
from software.plot import plot_data, get_codes_from_file

import matplotlib.pyplot as plt

HARDWARE_REV = 3

MAXIMUM_OFFSET = 0.005
PERCENT_CONVERTER = 100 
MAXIMUM_SLOPE_DIFFERENCE = 15

TEST_RESISTOR_VALUES = [39.4, 220, 330, 470]

percent_error = lambda theoretical, experimental: np.abs((experimental - theoretical)/theoretical * PERCENT_CONVERTER)
conductance = lambda resistance: 1/resistance


def find_data_files():
    files = []
    for file in os.listdir():
        if file.endswith(".csv"):
            files.append(file)
    files.sort(key=lambda name: int(''.join(list(filter(lambda c: c.isdigit(), [c for c in name])))))
    return files


def get_theoretical_data(voltages, resistance_value):
    theoretical_currents = voltages/resistance_value
    return theoretical_currents


for index, data_file in enumerate(find_data_files()):
    resistance_value = TEST_RESISTOR_VALUES[index]
    current_codes, voltage_codes = get_codes_from_file(data_file)
    currents, voltages = IV_data(voltage_codes, current_codes, HARDWARE_REV)

    plt = plot_data(
        current_codes, 
        voltage_codes,
        str(resistance_value) + 'Ω', 
        HARDWARE_REV,
        theoretical_currents=get_theoretical_data(voltages, resistance_value))
    plt.savefig('test_plot/' + str(resistance_value) + '.png')
    plt.clf()

    b, m = polyfit(voltages, currents, 1)
    
    percent_error_resistance = percent_error(resistance_value, conductance(m))
    assert b < MAXIMUM_OFFSET, "The offset is too large."
    assert percent_error_resistance < MAXIMUM_SLOPE_DIFFERENCE, str(resistance_value) + " not close enough to theoretical resistor."

    print(str(resistance_value) + " ohms PASS")
