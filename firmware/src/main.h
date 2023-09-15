#ifndef MAIN_H
#define MAIN_H

#include <stdint.h>

typedef struct 
{
    uint16_t voltage_code;
    uint16_t current_code;
} IV_Sample;

void setup_IO(void);
void DAC_CS_toggle(void);
void ADC_CS_toggle(void);
uint32_t average_ADC_reading(uint8_t channel);
void zero_device_voltage(void);
void sweep_device(void);

#endif