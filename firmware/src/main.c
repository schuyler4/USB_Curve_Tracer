#include <avr/io.h>
#include "UART.h"

int main(void)
{
    setup_UART();
    UART_transmit_string("USB Curve Tracer Starting\n\r");

    while(1)
    {

    }

    // The program should never return. 
    return 0;
}