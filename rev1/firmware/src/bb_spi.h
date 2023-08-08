#ifndef SPI_H
#define SPI_H

#include <stdint.h>

void setup(void);
int spi8(char byte);
int spi16(uint16_t data);

#endif
