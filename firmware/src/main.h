#ifndef MAIN_H
#define MAIN_H

#include <stdint.h>

#define AVERAGING_SAMPLE_COUNT 10

#define VOLTAGE_ADC_CHANNEL 0
#define CURRENT_ADC_CHANNEL 1
#define REFERENCE_ADC_CHANNEL 2

#define MAXIMUM_ADC_READING 4095

#define CURRENT_SENSOR_ADC_BIAS 2331    

#define ZERO_DEVICE_VOLTAGE_CODE 1725
#define ZERO_DEVICE_MARGIN 5

#define MAX_POSITIVE_CURRENT_CODE 4090
#define MAX_NEGATIVE_CURRENT_CODE 500

#define MAXIMUM_DAC_CODE 1024
#define MINIMUM_DAC_CODE 0

#define DELIMINATOR ","

#define SWEEP_COMMAND_CHARACTER 's'

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

// LED Control
void turn_on_green_LED(void);
void turn_off_green_LED(void);
void turn_on_red_LED(void);
void turn_off_red_LED(void);

#endif