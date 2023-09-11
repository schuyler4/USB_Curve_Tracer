//
// FILENAME: UART.h
//
// description: this file contains the prototypes for the UART functions. 
//
// Written by: Marek Newton
//

#ifndef UART_H
#define UART_H

// This function should be called before any UART functions are used.
void setup_UART(void);

void UART_transmit_char(char data);
void UART_transmit_string(char *string);
void UART_transmit_uint8_t(uint8_t number);
void UART_transmit_uint16_t(uint16_t number);
void UART_transmit_uint32_t(uint32_t number);
char UART_receive_character(void);

#endif