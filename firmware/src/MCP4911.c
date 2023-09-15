#include <stdint.h>
#include <avr/io.h>

#include "MCP4911.h"

#include "spi.h"

static void DAC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB2);
}

// Set the DAC to the given code
void set_DAC(uint16_t code, uint8_t gain, uint8_t buffer)
{
    if(code <= DAC_RESOLUTION - 1)
    {
        uint16_t configuration = (1 << SHDN) | (gain << GA) | (buffer << BUF) | (0 << START);
        DAC_CS_toggle();
        SPI_transceiver(configuration | (code >> CODE_BYTE0_OFFSET));
        SPI_transceiver((uint8_t) code << CODE_BYTE1_OFFSET);
        DAC_CS_toggle();
    } 
    // In all other cases, the code is out of range, so do nothing. 
}