#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>

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
        
        /*uint16_t i;
        for(i = 0; i < 1024; i+=1)
        {
            set_DAC(i);
            //_delay_ms(10);
        }*/
        set_DAC(1023);
    }

    // The program should never return. 
    return 0;
}

void DAC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB2);
}

void ADC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB1);
}

// set the DAC to the given code
void set_DAC(uint16_t code)
{
    if(code <= DAC_RESOLUTION - 1)
    {
        uint16_t configuration_bits = 0x7000;
        uint16_t command_bits = configuration_bits | (code << 0x4);
        //uint16_t command_bits = 0b0111111111111111;
        uint8_t first_command_byte = command_bits >> 8;
        uint8_t second_command_byte = command_bits && 0xFF;
        DAC_CS_toggle();
        SPI_transceiver(first_command_byte);
        SPI_transceiver(second_command_byte);
        DAC_CS_toggle();
    } 
    // In all other cases, the code is out of range, so do nothing. 
}

uint16_t get_ADC_reading(uint8_t channel)
{
    SPI_transceiver(0b00000110);
    uint8_t first_byte = SPI_transceiver(0b00000000);
    uint8_t second_byte = SPI_transceiver(0b00000000);
    return (first_byte << 8) | second_byte;
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

uint8_t SPI_transceiver(uint8_t data)
{
    // Start the transmission.
    SPDR = data; 
    // Wait for the transmission to finish. 
    while(!(SPSR & (1<<SPIF)));
    // Return the data that was received. 
    return SPDR;
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