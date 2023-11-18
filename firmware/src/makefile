# This make file uploads pure C programs to an arduino

# the frequency of the arduino board
F_CPU = 16000000UL

# the port that the board is connected to
PORT =  /dev/ttyUSB0

# the directory where all the compiled files go
BIN_DIRECTORY = ../bin

# the c files to be linked and compiled
# add file to line as the number of files in the program grows
SOURCE_FILES = main.c UART.c spi.c MCP3204.c MCP4911.c

# the name of the output file that will be compiled
OUTPUT_FILE = program

# the uC that is being used
MCU = atmega328p

# the avrdude part number for the MCU being programmed
MCU_PART_NUM = m328

make: main.c
	@echo \n
	#Create a binary .o file from the c source files
	avr-gcc -std=gnu99 -mmcu=$(MCU) -Os -o $(BIN_DIRECTORY)/$(OUTPUT_FILE).o $(SOURCE_FILES)
	@echo \n
	#create a hex file from the .o binary file
	avr-objcopy -j .text -j .data -O ihex $(BIN_DIRECTORY)/$(OUTPUT_FILE).o $(BIN_DIRECTORY)/program.hex
	@echo \n
	#upload program
	avrdude -F -V -c arduino -p ATMEGA328P -P ${PORT} -b 115200 -U flash:w:$(BIN_DIRECTORY)/$(OUTPUT_FILE).hex

compile:
	@echo \n
	#Create a binary .o file from the c source files
	avr-gcc -std=gnu99 -mmcu=$(MCU) -Os -o $(BIN_DIRECTORY)/$(OUTPUT_FILE).o $(SOURCE_FILES)
	@echo \n
	#create a hex file from the .o binary file
	avr-objcopy -j .text -j .data -O ihex $(BIN_DIRECTORY)/$(OUTPUT_FILE).o $(BIN_DIRECTORY)/program.hex
	@echo \n
