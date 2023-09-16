import sys

sys.path.append("../")

import os
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
from software.IV import IV_data

def find_data_files():
    files = []
    for file in os.listdir():
        if file.endswith(".csv"):
            files.append(file)
    return files


# Find the line of best fit
#b, m = polyfit(voltage_output, current_output, 1)

percent_error = lambda theoretical, experimental: np.abs((experimental - theoretical)/theoretical * 100)
conductance = lambda resistance: 1/resistance

print(find_data_files())