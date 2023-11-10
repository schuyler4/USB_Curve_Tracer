NEWLINE = '\n'
COMMA = ','

BAUDRATE = 9600
SERIAL_PORT = 'COM4'

DATA_START_COMMAND = 'START'
DATA_END_COMMAND = 'END'

TRANSMIT_STRING_GARBAGE = '\x00'

SWEEP_PROCESSOR_COMMAND = b's'
UNIDIRECTIONAL_PROCESSOR_COMMAND = b'u'
BIDIRECTIONAL_PROCESSOR_COMMAND = b'b'

POWER_DISCONNECTED = 'P'

DATA_RECEIVE_DELAY = 0.1
SECOND_DELAY = 1
TITLE_COMMAND_LIST_LENGTH = 2

# Plotting Settings
GRAPH_DECIMAL_DIGIT_COUNT = 2
SCATTER_PLOT_DOT_SIZE = 4
BASE_CURRENT_LABEL = 'Base Current'
BASE_EMITTER_VOLTAGE_LABEL = 'Base Emitter Voltage'
PREFIX_STRINGS = ['mA', 'uA']

DECODING_SCHEME = 'utf8'

FILE_WRITE = 'wt'

CSV_EXTENSION = '.csv'

IV_TRACE_TITLE = 'IV Trace'

NO_DATA_ERROR_COUNT = 10

# Messages
COMPONENT_CONNECTION_MESSAGE = 'Safe to connect component to curve tracer.'
OPENING_ERROR = 'Serial port could not be opened.'
NO_DATA_ERROR = 'No data received.'
DATA_READ_ERROR = 'Data could not be read'
COMMAND_PROMPT = 'Enter a command: '
TITLE_PROMPT = 'Enter a title:'
INVALID_COMMAND_ERROR = 'Invalid command'
STORED_SWEEPS_ERROR = 'No Stored Sweeps'
POWER_DISCONNECTED_ERROR = '12V Power is disconnected from the curve tracer.'
CURRENT_LIMIT_UNIDIRECTIONAL = 'A custom current limit can only be set in unidirectional mode.'
INVALID_CURRENT_LIMIT = 'Invalid Current limit Entered'
CURRENT_LIMIT_PROMPT = 'Enter a new current limit:'

# User Commands
SWEEP_USER_COMMAND = 'sweep'
CSV_USER_COMMAND = 'csv'
EXIT_USER_COMMAND = 'exit'
UNIDIRECTIONAL_USER_COMMAND = 'unidirectional'
BIDIRECTIONAL_USER_COMMAND = 'bidirectional'
REV2_USER_COMMAND = 'rev2'
REV1_USER_COMMAND = 'rev1'
CURRENT_LIMIT_COMMAND = 'current_limit'

# Plots
THEORETICAL_TRACE_COLOR = 'red'
MEASURED_LABEL = 'measured'
THEORETICAL_LABEL = 'theoretical'

VOLTAGE_AXIS_LABEL = 'Voltage (V)'
CURRENT_AXIS_LABEL = 'Current (A)'
