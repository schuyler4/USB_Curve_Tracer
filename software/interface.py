import serial
import time
import matplotlib.pyplot as plt

# This function sets up the serial object.
def init_serial():
    baudrate = 9600
    serial_port = 'COM7'

    try:
        my_serial = serial.Serial()
        my_serial.port = serial_port
        my_serial.baudrate = baudrate
        my_serial.timeout = 1
        
        my_serial.open()
        # For some reason, a delay is required before flushing the serial buffer.
        time.sleep(1)
        my_serial.flush()
        # Another delay is required after flushing the serial buffer, before using the serial port.
        time.sleep(1)
        return my_serial
    except:
        print('Serial port could not be opened.')
        return None


# This function loops through the serial data stream, reads it, and returns the data.
def read_serial_data(my_serial):
    no_data_count = 0
    received_data = []
    logging_data = False

    DATA_START_COMMAND = 'START'
    DATA_END_COMMAND = 'END'

    no_data_error = 10

    while True: 
        try:
            data_str = my_serial.readline().decode('utf8')

            # Check if the string contains a sub string.
            if(data_str == ''):
                no_data_count += 1

                if(no_data_count > no_data_error):
                    print('No data received.')
                    break
            elif(DATA_END_COMMAND in data_str):
                logging_data = False
                break
            elif(DATA_START_COMMAND in data_str):
                logging_data = True
            else:
                received_data.append(data_str)
                no_data_count = 0

        # Catch the exception and print it.
        except:
            print('Data could not be read')
            break   

    time.sleep(1)

    return received_data


# This function decodes the decoded binary integer. 
def sanitize_integer(string):
    cleaned_string = string.replace('\x00', '').replace('\n', '')
    decoded_integer = int(cleaned_string)
    return decoded_integer


# This function decodes the actual codes from the data. 
def get_data_codes(data):
    codes = []
    for datum in data:
        point = datum.split(',')
        point[0] = int(sanitize_integer(point[0]))
        point[1] = int(sanitize_integer(point[1]))
        codes.append(point)
    return np.array(codes)


def sweep_device(my_serial):
    my_serial.write(b's')
    time.sleep(0.1)
    data = read_serial_data(my_serial)
    return data
    

# This function runs the basic command line user interface.
def user_interface(my_serial):
    while True:
        user_input = input('Enter a command: ')

        if(user_input == 'sweep'):
            data = sweep_device(my_serial)
            print(data)
        elif(user_input == 'exit'):
            break
        else:
            print('Invalid command')