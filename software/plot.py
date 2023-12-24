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

class Control_Signal_Type(Enum):
    VOLTAGE = 0
    CURRENT = 1


class Transistor_Type(Enum):
    MOSFET = 1
    BJT = 2


class Prefix(Enum):
    NONE = 0
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


def legend_label_text(number, prefix, unit):
    number_string = str(round(number/prefix_multiplier(prefix), constants.GRAPH_DECIMAL_DIGIT_COUNT))
    return number_string + constants.PREFIX_STRINGS[prefix.value] + constants.UNIT_STRINGS[unit.value]


def remove_negative(IV_data):
    currents, voltages = IV_data
    filtered_currents = []
    filtered_voltages = []
    for i in range(0, len(currents)):
        current = currents[i]
        voltage = voltages[i]
        if(current >= 0 and voltage >=0):
            filtered_currents.append(current)
            filtered_voltages.append(voltage)
    return filtered_currents, filtered_voltages


def plot_transistor_data(IV_codes, transistor_type, control_pin_data, 
                        control_signal, control_signal_prefix, title, hardware_rev, scatter=True, negative_values=True):
    plt.title(title)
    for index, curve_codes in enumerate(IV_codes):
        current_codes, voltage_codes = curve_codes
        currents = None
        voltages = None 
        if(negative_values):
            currents, voltages = IV_data(voltage_codes, current_codes, hardware_rev)
        else:
            currents, voltages = remove_negative(IV_data(voltage_codes, current_codes, hardware_rev))
        legend_label = legend_label_text(control_pin_data[index], control_signal_prefix, control_signal)
        if(scatter):
            plt.scatter(voltages, currents, label=legend_label, s=constants.SCATTER_PLOT_DOT_SIZE)
        else:
            plt.plot(voltages, currents, label=legend_label)
    plt.xlabel(constants.VOLTAGE_AXIS_LABEL)
    plt.ylabel(constants.CURRENT_AXIS_LABEL)
    if(transistor_type == Transistor_Type.BJT):
        if(control_signal  == Control_Signal_Type.CURRENT):
            plt.legend(title=constants.BASE_CURRENT_LABEL)
        elif(control_signal == Control_Signal_Type.VOLTAGE):
            plt.legend(title=constants.BASE_EMITTER_VOLTAGE_LABEL)
    elif(transistor_type == Transistor_Type.MOSFET):
        if(control_signal == Control_Signal_Type.VOLTAGE):
            plt.legend(title=constants.GATE_SOURCE_VOLTAGE_LABEL)
    return plt
