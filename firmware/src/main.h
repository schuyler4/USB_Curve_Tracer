#ifndef MAIN_H
#define MAIN_H

void setup_IO(void);
void DAC_CS_toggle(void);
void ADC_CS_toggle(void);
uint32_t average_ADC_reading(uint8_t channel);
void zero_device_voltage(void);
void sweep_device(void);

#endif