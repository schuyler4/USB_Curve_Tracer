#ifndef SPI_H
#define SPI_H

#include <stdint.h>

void setup_SPI(void);
uint8_t SPI_transceiver(uint8_t data);

#endif