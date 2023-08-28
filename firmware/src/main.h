#ifndef MAIN_H
#define MAIN_H

void setup_IO(void);
void setup_SPI(void);
void DAC_CS_toggle(void);
void set_DAC(uint16_t code);
void SPI_transmit(uint8_t data);

#endif