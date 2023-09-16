import pandas as pd
import numpy as np

adc_resolution = 4096
reference_voltage = 2.5 # V
common_voltage = 6 # V
current_amplifier_gain = 350 # V/V
lsb = reference_voltage/adc_resolution

voltage_sensor_upper_step_down_resistor = 4700 # Ohms
current_sensor_upper_step_down_resistor = 3240 # Ohms
current_sensor_zero_voltage = 1.322 # V
lower_step_down_resistor = 1000 # Ohms
shunt_resistance = 0.1 # Ohms

output_voltage = lambda code: code * lsb

# This gets the input voltage of a voltage divider given its output voltage. 
def divided_voltage(divider_voltage, upper_resistor):
    return (divider_voltage/lower_step_down_resistor)*(upper_resistor+lower_step_down_resistor)

gain_division = lambda voltage, gain: voltage/gain

voltage_output = divided_voltage(output_voltage(voltage_code), voltage_sensor_upper_step_down_resistor) - common_voltage
current_output = (divided_voltage(output_voltage(current_code) - current_sensor_zero_voltage, 
                                voltage_sensor_upper_step_down_resistor)/current_amplifier_gain)/shunt_resistance 