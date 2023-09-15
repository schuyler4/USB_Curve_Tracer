#ifndef MCP3204_H
#define MCP3204_H

#include <stdint.h>

#ifndef BITS_PER_BYTE
#define BITS_PER_BYTE 8
#endif

#define SINGLE_ENDED 1
#define DIFFERENTIAL 0

// FIRST TRANSMIT BYTE
#define D2 0
#define SGL_OR_DIFF 1
#define START_BIT 2

// SECOND TRANSMIT BYTE
#define D1 7
#define D0 6

#define D0_MASK 1
#define D1_MASK 2
#define D2_MASK 4

#define FIRST_RECEIVE_BYTE_MASK 0x0F

uint16_t get_ADC_reading(uint8_t single_or_diff, uint8_t channel);

#endif