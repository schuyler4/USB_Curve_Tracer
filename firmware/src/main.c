#include <avr/io.h>
#include <stdint.h>

#include "main.h"
#include "UART.h"

#define DAC_RESOLUTION 1024

int main(void)
{
    setup_UART();
    setup_IO();
    setup_SPI();
    UART_transmit_string("USB Curve Tracer Starting\n\r");

    while(1)
    {
        PORTB |= (1 << PORTB0);
        PORTD |= (1 << PORTD7);
        set_DAC(500);
    }

    // The program should never return. 
    return 0;
}

void DAC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB2);
}

// set the DAC to the given code
void set_DAC(uint16_t code)
{
    if(code <= DAC_RESOLUTION - 1)
    {
        uint16_t configuration_bits = 0x6000;
        uint16_t command_bits = configuration_bits | code;
        DAC_CS_toggle();
        SPI_transmit(0b01110011);
        SPI_transmit(0b11111111);
        DAC_CS_toggle();
    } 
    // In all other cases, the code is out of range, so do nothing. 
}

void setup_SPI(void)
{
    // Set up the SPI peripheral.   
    // Obviously, the microcontroller is being used as a master. 
    SPCR = (1<<SPE) | (1<<MSTR) | (1<<SPR0);
    // Start both CS pins high.
    PORTB |= (1 << PORTB1);
    PORTB |= (1 << PORTB2);
}

void SPI_transmit(uint8_t data)
{
    // Start the transmission.
    SPDR = data; 
    // Wait for the transmission to finish. 
    while(!(SPSR & (1<<SPIF)));
}

void setup_IO(void)
{
    // Set SPI MOSI, SCK to output.
    DDRB |= (1 << DDB3);
    DDRB |= (1 << DDB5);
    // Set both CS pins to output. 
    DDRB |= (1 << DDB1);
    DDRB |= (1 << DDB2);
    // Set the LED pins to outputs. 
    DDRB |= (1 << DDB0);
    DDRD |= (1 << DDD7);
}