#ifndef MAIN_H
#define MAIN_H

void setup_IO(void);
void setup_SPI(void);
void DAC_CS_toggle(void);
void set_DAC(uint16_t code);
void ADC_CS_toggle(void);
uint8_t SPI_transceiver(uint8_t data);
uint16_t get_ADC_reading(uint8_t channel);
uint32_t average_ADC_reading(uint8_t channel);
void zero_device_voltage(void);
void sweep_device(void);

#endif