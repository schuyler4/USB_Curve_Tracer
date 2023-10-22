import serial
import time
import csv
import numpy as np

from . import constants
from .plot import plot_data


def init_serial():
    try:
        my_serial = serial.Serial()
        my_serial.port = constants.SERIAL_PORT
        my_serial.baudrate = constants.BAUDRATE
        my_serial.timeout = constants.SECOND_DELAY
        
        my_serial.open()
        # For some reason, a delay is required before flushing the serial buffer.
        time.sleep(constants.SECOND_DELAY)
        my_serial.flush()
        # Another delay is required after flushing the serial buffer, before using the serial port.
        time.sleep(constants.SECOND_DELAY)
        return my_serial
    except:
        print(constants.OPENING_ERROR)
        return None


def read_serial_data(my_serial):
    no_data_count = 0
    received_data = []
    logging_data = False

    while True: 
        try:
            data_str = my_serial.readline().decode(constants.DECODING_SCHEME)

            if(data_str == ''):
                no_data_count += 1

                if(no_data_count > constants.NO_DATA_ERROR_COUNT):
                    print(constants.NO_DATA_ERROR)
                    break
            elif(constants.DATA_END_COMMAND in data_str):
                logging_data = False
                break
            elif(constants.DATA_START_COMMAND in data_str):
                logging_data = True
            elif(logging_data):
                received_data.append(data_str)
                no_data_count = 0
        except:
            print(constants.DATA_READ_ERROR)
            break   

    time.sleep(constants.SECOND_DELAY)

    return received_data


def sanitize_string(string):
    cleaned_string = string.replace(constants.TRANSMIT_STRING_GARBAGE, '').replace(constants.NEWLINE, '')
    return cleaned_string

 
def get_data_codes(data):
    if(constants.POWER_DISCONNECTED in sanitize_string(data)):
        return None, None
    else:
        codes = []
        for datum in data:
            point = datum.split(constants.COMMA)
            point[0] = int(sanitize_string(point[0]))
            point[1] = int(sanitize_string(point[1]))
            codes.append(point)
        codes = np.array(codes)
        current_codes = codes[:,0]
        voltage_codes = codes[:,1]
        return current_codes, voltage_codes


def sweep_device_command(my_serial):
    my_serial.write(constants.SWEEP_PROCESSOR_COMMAND)
    time.sleep(constants.DATA_RECEIVE_DELAY)
    data = read_serial_data(my_serial)
    return data


def change_mode_command(my_serial, processor_mode):
    my_serial.write(processor_mode)
    time.sleep(constants.DATA_RECEIVE_DELAY)


def write_data_to_CSV(current_codes, voltage_codes, title):
    csv_filename = title + constants.CSV_EXTENSION
    csv_data = []
    for index, current_code in enumerate(current_codes):
        csv_data.append([current_code, voltage_codes[index]])
    
    with open(csv_filename, constants.FILE_WRITE) as fp:
        writer = csv.writer(fp, delimiter = constants.COMMA)
        writer.writerows(csv_data)


def user_interface(my_serial):
    current_codes = []
    voltage_codes = []
    title = None

    while True:
        user_input = input(constants.COMMAND_PROMPT)

        if(constants.SWEEP_USER_COMMAND in user_input and user_input != constants.SWEEP_USER_COMMAND):
            command_and_title = user_input.split(constants.COMMA)
            if(len(command_and_title) != constants.TITLE_COMMAND_LIST_LENGTH):
                print(constants.INVALID_COMMAND_ERROR)
                continue
            data = sweep_device_command(my_serial)
            current_codes, voltage_codes = get_data_codes(data)
            if(current_codes == None and voltage_codes == None):
                print(constants.POWER_DISCONNECTED_ERROR)
            else:
                plot_data(current_codes, voltage_codes, command_and_title[1]).show()
        elif(user_input == constants.SWEEP_USER_COMMAND):
            data = sweep_device_command(my_serial)
            current_codes, voltage_codes = get_data_codes(data)
            if(current_codes == None and voltage_codes == None):
                print(constants.POWER_DISCONNECTED_ERROR)
            else:
                plot_data(current_codes, voltage_codes, constants.IV_TRACE_TITLE).show()
        elif(user_input == constants.CSV_USER_COMMAND):
            if(len(current_codes) == 0 and len(voltage_codes) == 0):
                print(constants.STORED_SWEEPS_ERROR)
                continue
            else:
                title = input(constants.TITLE_PROMPT)
                write_data_to_CSV(current_codes, voltage_codes, title)
        elif(user_input == constants.UNIDIRECTIONAL_USER_COMMAND):
            change_mode_command(my_serial, constants.UNIDIRECTIONAL_PROCESSOR_COMMAND)
        elif(user_input == constants.BIDIRECTIONAL_USER_COMMAND):
            change_mode_command(my_serial, constants.BIDIRECTIONAL_PROCESSOR_COMMAND)
        elif(user_input == constants.EXIT_USER_COMMAND):
            break
        else:
            print(constants.INVALID_COMMAND_ERROR)