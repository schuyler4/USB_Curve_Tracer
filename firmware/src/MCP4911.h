#ifndef MCP4911
#define MCP4911

#define DAC_RESOLUTION 1024

#define BUFFERED 1
#define UNBUFFERED 0

#define GAIN_1X 1
#define GAIN_2X 0

#define SHDN 4
#define GA 5
#define BUF 6
#define START 7

#define CODE_BYTE1_OFFSET 2
#define CODE_BYTE0_OFFSET 6

void set_DAC(uint16_t code, uint8_t gain, uint8_t buffer);

#endif