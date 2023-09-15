#include <avr/io.h>
#include <stdint.h>

#include "main.h"
#include "UART.h"
#include "spi.h"
#include "MCP3204.h"
#include "MCP4911.h"

#define AVERAGING_SAMPLE_COUNT 10

#define VOLTAGE_ADC_CHANNEL 0
#define CURRENT_ADC_CHANNEL 1
#define REFERENCE_ADC_CHANNEL 2

#define MAXIMUM_ADC_READING 4095

#define CURRENT_SENSOR_ADC_BIAS 2331    

#define ZERO_DEVICE_VOLTAGE_CODE 1725
#define ZERO_DEVICE_MARGIN 5

#define MAX_POSITIVE_CURRENT_CODE 0
#define MAX_NEGATIVE_CURRENT_CODE 0

#define MAXIMUM_DAC_CODE 1023
#define MINIMUM_DAC_CODE 0

static uint16_t DAC_voltage_setting = 0;

int main(void)
{
    setup_UART();
    setup_IO();
    setup_SPI();
    UART_transmit_string("USB Curve Tracer Starting\n\r");

    zero_device_voltage();
    sweep_device();

    while(1)
    {   
        PORTB |= (1 << PORTB0);
        PORTD |= (1 << PORTD7);

        //set_DAC(400);
        //set_DAC(0);
        //set_DAC(1024);

        //uint32_t zero_current_reading = average_ADC_reading(CURRENT_ADC_CHANNEL);
    }

    // The program should never return. 
    return 0;
}

void setup_IO(void)
{
    // Set MOSI and SCK to output for SPI.
    DDRB |= (1 << DDB3);
    DDRB |= (1 << DDB5);
    // Set both CS pins to output. 
    DDRB |= (1 << DDB1);
    DDRB |= (1 << DDB2);
    // Set the LED pins to outputs. 
    DDRB |= (1 << DDB0);
    DDRD |= (1 << DDD7);
}

void zero_device_voltage(void)
{
    while(1)
    {
        uint16_t voltage_reading = get_ADC_reading(SINGLE_ENDED, VOLTAGE_ADC_CHANNEL);

        if(voltage_reading > ZERO_DEVICE_VOLTAGE_CODE)
        {
            DAC_voltage_setting--;
        }
        else if(voltage_reading < ZERO_DEVICE_VOLTAGE_CODE)
        {
            DAC_voltage_setting++;
        }

        set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);

        uint8_t above_range = voltage_reading > ZERO_DEVICE_VOLTAGE_CODE + ZERO_DEVICE_MARGIN;
        uint8_t below_range = voltage_reading < ZERO_DEVICE_VOLTAGE_CODE - ZERO_DEVICE_MARGIN;

        if(!above_range && !below_range)
        {
            break;
        }
    }
}

IV_Sample sample_IV(void)
{
    IV_Sample iv_sample;
    iv_sample.voltage_code = get_ADC_reading(SINGLE_ENDED, VOLTAGE_ADC_CHANNEL);
    iv_sample.current_code = get_ADC_reading(SINGLE_ENDED, CURRENT_ADC_CHANNEL);
    return iv_sample;
}

void sweep_device(void)
{
    while(DAC_voltage_setting <= MAXIMUM_DAC_CODE)
    {
        DAC_voltage_setting++;
        set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);
    }

    zero_device_voltage();

    while(DAC_voltage_setting >= MINIMUM_DAC_CODE)
    {
        DAC_voltage_setting--;
        set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);
    }

    zero_device_voltage();
}