import sys

sys.path.append('../../../')


from software.plot import get_codes_from_file, plot_transistor_data, Transistor_Type, Prefix, Control_Signal_Type

CURVE_COUNT = 5
HARDWARE_REV = 3
PLOT_TITLE = 'ZVN3301A Sweep'

GATE_VOLTAGES = [3.707, 4.033, 5.001, 8.11, 10.16]

transistor_IV_codes = []
for i in range(1, CURVE_COUNT+1):
    current_codes, voltage_codes = get_codes_from_file('#' + str(i) + '.csv')
    transistor_IV_codes.append((current_codes, voltage_codes))
    
plot_transistor_data(
    transistor_IV_codes,
    Transistor_Type.MOSFET,
    GATE_VOLTAGES,
    Control_Signal_Type.VOLTAGE, 
    Prefix.NONE,
    PLOT_TITLE,
    HARDWARE_REV, negative_values=False).show()
