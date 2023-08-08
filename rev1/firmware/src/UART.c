#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
//#include <math.h>

#ifndef F_CPU
#define F_CPU 1000000UL
#endif

#define BAUD 9600
#define MYUBRR (((F_CPU / (BAUD * 16UL))) - 1)

//char* int_to_string(int number)
//{
    //int max_digits = (int)log10(number) + 2;
    //char* string = malloc(max_digits + 2 * sizeof(char));
    //sprintf(string, "%d", number);
    //return string;
//}

// sets all the registers that are needed for UART communication
void setup_UART(void)
{
    // set baud rate
    UBRRH = (unsigned char)(MYUBRR>>8);
    UBRRL = (unsigned char)MYUBRR;
    // enable receiver and transmitter
    UCSRB = (1<<RXEN)|(1<<TXEN);
    // Set frame format: 8data, 2stop bit
    UCSRC = (1<<USBS)|(3<<UCSZ0);
}

// transmits a single character on the UART stream
void UART_transmit_char(char data)
{
    // Wait for empty transmit buffer
    while (!( UCSRA & (1<<UDRE)));
    // Put data into buffer, sends the data
    UDR = data;
}

// transimits an array of characters over UART
void UART_transmit_string(char *string)
{
    unsigned int i;
    while(1)
    {
        char character = *(string + i);
        UART_transmit_char(character);

        if(character == '\0')
        {
            break;
        }
        i++;
    }
}

void UART_transmit_int(int number)
{
    /*int max_digits = (int)log10(number) + 2;
    char* string = malloc(max_digits + 2 * sizeof(char));
    sprintf(string, "%d", number);

    for(int i = 0; i < max_digits; i++)
    {
        UART_transmit_char(*(string + i));
    }

    free(string);*/
}
