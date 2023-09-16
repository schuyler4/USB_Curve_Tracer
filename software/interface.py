import serial
import time
import matplotlib.pyplot as plt

# This function sets up the serial object.
def init_serial():
    baudrate = 9600
    serial_port = 'COM6'

    try:
        my_serial = serial.Serial()
        my_serial.port = serial_port
        my_serial.baudrate = baudrate
        my_serial.timeout = 1
        
        my_serial.open()
        # For some reason, a delay is required before flushing the serial buffer.
        time.sleep(1)
        my_serial.flush()
        # Another delay is required after flushing the serial buffer before using the serial port.
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

    return received_data


# This function decodes the decoded binary integer. 
def sanitize_integer(string):
    cleaned_string = string.replace('\x00', '').replace('\n', '')
    decoded_integer = int(cleaned_string)
    return decoded_integer


# This function separates the stream of x and y data into two lists.
def separate_data(data):
    x = []
    y = []

    sampling_x = False
    sampling_y = False

    for data_str in data:
        if('X' in data_str):
            sampling_x = True
            sampling_y = False
        elif('Y' in data_str):
            sampling_y = True
            sampling_x = False
        else:
            if(sampling_x):
                x.append(sanitize_integer(data_str))
            elif(sampling_y):
                y.append(sanitize_integer(data_str))

    return x, y


# This function plots the random data for the user to see.
def plot_data(x, y):
    plt.scatter(x, y)
    plt.title('A Scatter Plot of the Numerical Data')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def random_numbers(my_serial):
    my_serial.write(b'2')
    time.sleep(0.1)
    data = read_serial_data(my_serial)

    if(len(data) > 0):
        # Print the data without the newline character.
        return separate_data(data)
    else:
        return None


def sweep_device(my_serial):
    my_serial.write(b's')
    time.sleep(0.1)
    data = read_serial_data(my_serial)


# This function runs the basic command line user interface.
def user_interface(my_serial):
    while True:
        user_input = input('Enter a command: ')

        if(user_input == 'random'):
            x, y = random_numbers(my_serial)
            plot_data(x, y)

        elif(user_input == 'exit'):
            break
        else:
            print('Invalid command')