import matplotlib.pyplot as plt
from .IV import IV_data

def plot_data(current_codes, voltage_codes, title, theoretical_currents=[]):
    currents, voltages = IV_data(voltage_codes, current_codes)
    plt.title(title)
    plt.scatter(voltages, currents, label='measured')
    if(len(theoretical_currents) > 0):
        plt.plot(voltages, theoretical_currents, color='red', label='theoretical')
        plt.legend()
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    return plt
