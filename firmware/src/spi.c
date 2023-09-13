#include <avr/io.h>
#include <stdint.h>

void setup_SPI(void)
{
    // Set up the SPI peripheral.   
    // Obviously, the microcontroller is being used as a master. 
    SPCR = (1<<SPE) | (1<<MSTR) | (1<<SPR0) | (1 << SPR1);
    // Start both CS pins high.
    PORTB |= (1 << PORTB1);
    PORTB |= (1 << PORTB2);
}

uint8_t SPI_transceiver(uint8_t data)
{
    // Start the transmission.
    SPDR = data; 
    // Wait for the transmission to finish. 
    while(!(SPSR & (1<<SPIF)));
    // Return the data that was received. 
    return SPDR;
}