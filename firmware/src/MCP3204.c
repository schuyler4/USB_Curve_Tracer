#include <avr/io.h>
#include <stdint.h>

#include "MCP3204.h"

#include "spi.h"

static void ADC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB1);
}

uint16_t get_ADC_reading(uint8_t single_or_diff, uint8_t channel)
{
    uint8_t d0 = channel & D0_MASK;
    uint8_t d1 = channel & D1_MASK;
    uint8_t d2 = channel & D2_MASK;
    uint8_t configuration_byte1 = (1 << START_BIT) | (single_or_diff << SGL_OR_DIFF) | (d2 << D2);
    uint8_t configuration_byte2 = (d1 << D1) | (d0 << D0);

    ADC_CS_toggle();
    // The first byte is only for configuration.
    SPI_transceiver(configuration_byte1);
    // The second byte is for configuration and receiving.
    uint8_t first_receive_byte = SPI_transceiver(configuration_byte2) & FIRST_RECEIVE_BYTE_MASK;
    // The third byte is only for receiving
    uint8_t second_receive_byte = SPI_transceiver(0);

    ADC_CS_toggle();
    uint16_t combined_bytes = (uint16_t)((first_receive_byte << BITS_PER_BYTE) | second_receive_byte);
    return combined_bytes;
}