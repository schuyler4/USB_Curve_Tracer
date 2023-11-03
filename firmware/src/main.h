#ifndef MAIN_H
#define MAIN_H

#include <stdint.h>

#define HARDWARE_REVISION 2

#define AVERAGING_SAMPLE_COUNT 10

#define VOLTAGE_ADC_CHANNEL 0
#define CURRENT_ADC_CHANNEL 1
#define REFERENCE_ADC_CHANNEL 2

#define MAXIMUM_ADC_READING 4095

#if HARDWARE_REVISION == 2
   
#define MAX_POSITIVE_CURRENT_CODE 4090
#define MAX_NEGATIVE_CURRENT_CODE 500

#elif HARDWARE_REVISION == 3

// Maximum current is +/- 0.75A

#define MAX_POSITIVE_CURRENT_CODE 0 // THIS NEEDS TO BE CALCULATED ONCE THE REFERENCE VOLTAGE IS MEASURED
#define MAX_NEGATIVE_CURRENT_CODE 0 // THIS NEEDS TO BE CALCULATED ONCE THE REFERENCE VOLTAGE IS MEASURED

#endif

#define ZERO_DEVICE_MARGIN 3

#define MAXIMUM_DAC_CODE 1024
#define MINIMUM_DAC_CODE 0

// PC Communication Protocol.
#define DELIMINATOR ","

#define SWEEP_COMMAND_CHARACTER 's'

#define UNIDIRECTIONAL_COMMAND_CHARACTER 'u'
#define BIDIRECTIONAL_COMMAND_CHARACTER 'b'

#define START_COMMAND "START"
#define END_COMMAND "END"
#define POWER_DISCONNECTED "P"

typedef struct 
{
    uint16_t voltage_code;
    uint16_t current_code;
} IV_Sample;

typedef enum
{
    UNIDIRECTIONAL,
    BIDIRECTIONAL
} Mode;

void device_operation(void);

void setup_IO(void);
void DAC_CS_toggle(void);
void ADC_CS_toggle(void);
uint32_t average_ADC_reading(uint8_t channel);
void zero_device_voltage(void);
void sweep_device(void);
uint8_t external_voltage_supply_detected(void);
void print_power_disconnected(void);
void power_disconnected(void);

void print_starting_command(void);
void print_ending_command(void);

// LED Control
void turn_on_green_LED(void);
void turn_off_green_LED(void);
void turn_on_red_LED(void);
void turn_off_red_LED(void);

#endif