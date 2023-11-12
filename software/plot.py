'''
FILENAME: plot.py

description: This file contains all the functions necessary to plot data and get it from a CSV files. 

Written by Marek Newton
'''

from enum import Enum

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .IV import IV_data
from . import constants

class BJT_Current_Setting_Indicator(Enum):
    BASE_EMITTER_VOLTAGE = 1
    BASE_CURRENT = 2


class Prefix(Enum):
    MILLI = 1
    MICRO = 2


def prefix_multiplier(prefix):
    return 10**(-1*prefix.value*3)


def get_codes_from_file(filename):
    data = np.array(pd.read_csv(filename))
    current_codes = data[:, 0]
    voltage_codes = data[:, 1]
    return current_codes, voltage_codes


def plot_data(current_codes, voltage_codes, title, hardware_rev, theoretical_currents=[]):
    currents, voltages = IV_data(voltage_codes, current_codes, hardware_rev)
    plt.title(title)
    plt.scatter(voltages, currents, label=constants.MEASURED_LABEL)
    if(len(theoretical_currents) > 0):
        plt.plot(voltages, theoretical_currents, color=constants.THEORETICAL_TRACE_COLOR, label=constants.THEORETICAL_LABEL)
        plt.legend()
    plt.xlabel(constants.VOLTAGE_AXIS_LABEL)
    plt.ylabel(constants.CURRENT_AXIS_LABEL)
    return plt


def legend_label_text(number, prefix):
    number_string = str(round(number/prefix_multiplier(prefix), constants.GRAPH_DECIMAL_DIGIT_COUNT))
    return number_string + constants.PREFIX_STRINGS[prefix.value - 1]


def plot_transistor_data(IV_codes, base_data, current_setting, current_setting_prefix, title, hardware_rev):
    plt.title(title)
    for index, curve_codes in enumerate(IV_codes):
        current_codes, voltage_codes = curve_codes
        currents, voltages = IV_data(voltage_codes, current_codes, hardware_rev)
        legend_label = legend_label_text(base_data[index], current_setting_prefix)
        plt.scatter(voltages, currents, label=legend_label, s=constants.SCATTER_PLOT_DOT_SIZE)
    plt.xlabel(constants.VOLTAGE_AXIS_LABEL)
    plt.ylabel(constants.CURRENT_AXIS_LABEL)
    if(current_setting == BJT_Current_Setting_Indicator.BASE_CURRENT):
        plt.legend(title=constants.BASE_CURRENT_LABEL)
    elif(current_setting == BJT_Current_Setting_Indicator.BASE_EMITTER_VOLTAGE):
        plt.legend(title=constants.BASE_EMITTER_VOLTAGE_LABEL)
    return plt