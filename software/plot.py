import matplotlib.pyplot as plt

from .IV import IV_data
from . import constants

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
