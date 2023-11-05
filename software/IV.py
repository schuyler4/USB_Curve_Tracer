'''
FILENAME: IV.py

PURPOSE: This file contains functions that convert ADC codes into current and voltage values.

WRITTEN BY: Marek Newton
'''

ADC_RESOLUTION = 4096
REFERENCE_VOLTAGE = 2.5 # V
LSB = REFERENCE_VOLTAGE/ADC_RESOLUTION # V

LOWER_STEP_DOWN_RESISTOR = 1000 # Ohms

# REVISION 2 HARDWARE VALUES
CURRENT_AMPLIFIER_GAIN_REV2 = 250 # V/V
VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV2 = 4700 # Ohms
CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV2 = 3240 # Ohms
CURRENT_SENSOR_ZERO_VOLTAGE_REV2 = 1.322 # V
SHUNT_RESISTANCE_REV2 = 0.1 # Ohms
COMMON_VOLTAGE_REV2 = 6 # V

# REVISION 3 HARDWARE VALUES
VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV3 = 4020 # Ohms
CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV3 = 4020 # Ohms
CURRENT_SENSOR_ZERO_VOLTAGE_REV3 = 1.16 # V
SHUNT_RESISTANCE_REV3 = 0.5 # Ohms
COMMON_VOLTAGE_REV3 = 5.836 # V
CURRENT_AMPLIFIER_GAIN_REV3 = 11.8

output_voltage = lambda code: code * LSB
gain_division = lambda voltage, gain: voltage/gain

# This gets the input voltage of a voltage divider given its output voltage. 
def divided_voltage(divider_voltage, upper_resistor):
    return (divider_voltage/LOWER_STEP_DOWN_RESISTOR)*(upper_resistor+LOWER_STEP_DOWN_RESISTOR)


# This gets the output voltage of a voltage divider given its input voltage. 
def divider_voltage(input_voltage, upper_resistor):
    return (input_voltage/(upper_resistor + LOWER_STEP_DOWN_RESISTOR))*LOWER_STEP_DOWN_RESISTOR


def IV_data(voltage_codes, current_codes, hardware_rev):
    if(hardware_rev == 2):
        voltages = divided_voltage(output_voltage(voltage_codes), 
                                   VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV2) - COMMON_VOLTAGE_REV2
        currents = (divided_voltage(output_voltage(current_codes) - CURRENT_SENSOR_ZERO_VOLTAGE_REV2, 
                                CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV2)/CURRENT_AMPLIFIER_GAIN_REV2)/SHUNT_RESISTANCE_REV2
    else:
        voltages = divided_voltage(output_voltage(voltage_codes), 
                                   VOLTAGE_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV3) - COMMON_VOLTAGE_REV3
        currents = ((
                    divided_voltage(output_voltage(current_codes) - CURRENT_SENSOR_ZERO_VOLTAGE_REV3, 
        CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV3)/CURRENT_AMPLIFIER_GAIN_REV3)/SHUNT_RESISTANCE_REV3)

    return currents, voltages


def calculate_max_current_code(max_current, hardware_rev):
    if(hardware_rev == 2):
        adc_input_voltage = divider_voltage(max_current*SHUNT_RESISTANCE_REV3*CURRENT_AMPLIFIER_GAIN_REV3, 
                                            CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV3)
        return int(adc_input_voltage/LSB)
    else:
        adc_input_voltage = divider_voltage(max_current*SHUNT_RESISTANCE_REV2*CURRENT_AMPLIFIER_GAIN_REV2, 
                                            CURRENT_SENSOR_UPPER_STEP_DOWN_RESISTOR_REV2)
        return int(adc_input_voltage/LSB)



