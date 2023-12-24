import sys

sys.path.append('../../../')

from software.plot import get_codes_from_file, plot_transistor_data, Control_Signal_Type, Transistor_Type, Prefix

CURVE_COUNT = 5
HARDWARE_REV = 3
PLOT_TITLE = '2N3904 Sweep'

BASE_CURRENTS = [8.9/10e3, 8.9/20e3, 8.9/30e3, 8.7/1e3, 8.8/3e3]

transistor_IV_codes = []
for i in range(1, CURVE_COUNT+1):
    if(i != 4):
        current_codes, voltage_codes = get_codes_from_file('#' + str(i) + '.csv')
        transistor_IV_codes.append((current_codes, voltage_codes))

plot_transistor_data(
    transistor_IV_codes, 
    Transistor_Type.BJT,
    BASE_CURRENTS, 
    Control_Signal_Type.CURRENT,
    Prefix.MILLI,
    PLOT_TITLE, 
    HARDWARE_REV).show()
