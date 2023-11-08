import sys

sys.path.append('../../../')

from software.plot import get_codes_from_file, plot_transistor_data, BJT_Current_Setting_Indicator, Prefix

CURVE_COUNT = 4
HARDWARE_REV = 3
PLOT_TITLE = 'TIP122G Sweep'

BASE_CURRENTS = [8.4/120e3, 8.4/130e3, 8.4/140e3, 8.5/150e3]

transistor_IV_codes = []
for i in range(1, CURVE_COUNT+1):
    current_codes, voltage_codes = get_codes_from_file('#' + str(i) + '.csv')
    transistor_IV_codes.append((current_codes, voltage_codes))

plot_transistor_data(
    transistor_IV_codes, 
    BASE_CURRENTS, 
    BJT_Current_Setting_Indicator.BASE_CURRENT, 
    Prefix.MICRO,
    PLOT_TITLE, 
    HARDWARE_REV).show()