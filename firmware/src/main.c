#ifndef F_CPU
#define F_CPU 1000000UL
#endif

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include <stdint.h>

#include "UART.h"
#include "main.h"
#include "bb_spi.h"

#define SECOND_PACKET_MASK 0x0300
#define DAC_VOLTAGE_REFERENCE 0.7
#define CURRENT_SOURCE_RESISTANCE 0.1
#define DAC_RESOLUTION 1024
#define LSB DAC_VOLTAGE_REFERENCE/DAC_RESOLUTION

int main(void)
{
    cli();
    setup_UART();
    //USICR = (1<<USIWM0)|(1<<USICS1)|(1<<USICLK);
    sei();

    //PORTD |= (1 << PORTD5) | (1 << PORTD6);
    DDRB |= (1 << DDB0) | (1 << DDB5) | (1 << DDB7) | (1 << DDB1);
    DDRB &= ~(1 << DDB6);

    DDRD |= (1 << DDD3) | (1 << DDD4) | (1 << DDD5) | (1 << DDD6);

    PORTB |= (1 << PORTB0);
    PORTB |= (1 << PORTB1);

    //set_current();

    while(1) // program should never return
    {
        //set_current();
        //read_ADC();
        //test_DAC();
        PORTB |= (1 << PORTB5);
        test_DAC();
        _delay_ms(5);
        //set_current();
        //int data = read_ADC();
        //char str[10];
        //itoa(data, str, 10);
        //UART_transmit_string("data: ");
        //UART_transmit_string(str);
        //UART_transmit_string("\n\r");
        //_delay_ms(500);
    }
}

int read_ADC(void)
{
    ADC_CS_toggle();

    _delay_us(10);
    spi8(0x60);
    spi8(0x00);
    _delay_us(10);

    ADC_CS_toggle();
}

void set_relays(void)
{
    // set to the lowest current possible during switchover
    set_DAC(0);
}

// set the DAC to the given code
void set_DAC(uint16_t code)
{
    if(code <= DAC_RESOLUTION - 1)
    {
        uint16_t configuration_bits = 0x6000;
        uint16_t command_bits = configuration_bits | code;
        DAC_CS_toggle();
        spi8(0x60);
        DAC_CS_toggle();
    } 
    // else, code is out of range, do nothing
}

// generate a sawtooth waveform with the DAC
void test_DAC(void)
{
    static uint16_t code = 0;
    set_DAC(code);
    if(code < DAC_RESOLUTION - 1)
    {
        code++;
    }
    else
    {
        code = 0;
    }
}

void DAC_CS_toggle(void)
{
    // xor equals to toggle
    PORTB ^= (1 << PORTB0);
}

void ADC_CS_toggle(void)
{
    // xor equals to toggle
    PORTB ^= (1 << PORTB1);
}
