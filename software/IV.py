'''
FILENAME: IV.py

PURPOSE: This file contains functions that convert ADC codes into current and voltage values.

WRITTEN BY: Marek Newton
'''

ADC_RESOLUTION = 4096
REFERENCE_VOLTAGE = 2.5 # V
COMMON_VOLTAGE = 6 # V
CURRENT_AMPLIFIER_GAIN = 250 # V/V
LSB = REFERENCE_VOLTAGE/ADC_RESOLUTION # V

VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR = 4700 # Ohms
CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR = 3240 # Ohms
CURRENT_SENSOR_ZERO_VOLTAGE = 1.322 # V
LOWER_STEP_DOWN_RESISTOR = 1000 # Ohms
SHUNT_RESISTANCE = 0.1 # Ohms

output_voltage = lambda code: code * LSB
gain_division = lambda voltage, gain: voltage/gain


# This gets the input voltage of a voltage divider given its output voltage. 
def divided_voltage(divider_voltage, upper_resistor):
    return (divider_voltage/LOWER_STEP_DOWN_RESISTOR)*(upper_resistor+LOWER_STEP_DOWN_RESISTOR)


def IV_data(voltage_codes, current_codes):
    voltages = divided_voltage(output_voltage(voltage_codes), VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR) - COMMON_VOLTAGE
    currents = (divided_voltage(output_voltage(current_codes) - CURRENT_SENSOR_ZERO_VOLTAGE, 
                                    CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR)/CURRENT_AMPLIFIER_GAIN)/SHUNT_RESISTANCE 
    return currents, voltages