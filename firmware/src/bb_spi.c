#ifndef F_CPU
#define F_CPU 1000000UL
#endif

#define CLOCK_DELAY_MS 5

#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>
#include "UART.h"

#include "bb_spi.h"

int spi8(char byte)
{
    uint8_t i;
    // Obviously, there are 8 bits in a byte
    for(i = 0; i < 8; i++)
    {
        // set MOSI
        if(byte & 0x80)
        {
            PORTB |= (1 << PORTB5);
        }
        else
        {
            PORTB &= ~(1 << PORTB5);
        }


        PORTB |= (1<<PORTB7); //pulse clock

        _delay_us(20);

        PORTB &= ~(1<<PORTB7);

        byte <<= 1;
    }

    return 0;
}

int spi16(uint16_t data)
{
    uint16_t input_data = 0;
    uint8_t i;
    int captured_data = 0;
    // Obviously, there are 8 bits in a byte
    for(i = 0; i < 16; i++)
    {
        // set MOSI
        if(data & 0b1000000000000000)
        {
            PORTB |= (1 << PORTB5);
        }
        else
        {
            PORTB &= ~(1 << PORTB5);
        }

        PORTB |= (1<<PORTB7); //pulse clock

        //_delay_us(10);
        // check data input
        //if(PINB & PINB6)
        //{
        //    return 10;
        //}

        //  _delay_us(10);

        PORTB &= ~(1<<PORTB7);

        data <<= 1;
    }

    return 5;
}
