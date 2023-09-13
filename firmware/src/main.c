#include <avr/io.h>
#include <stdint.h>

#include "main.h"
#include "UART.h"
#include "spi.h"
#include "MCP3204.h"

#define DAC_RESOLUTION 1024

#define AVERAGING_SAMPLE_COUNT 10

#define VOLTAGE_ADC_CHANNEL 0
#define CURRENT_ADC_CHANNEL 1
#define REFERENCE_ADC_CHANNEL 2

#define MAXIMUM_ADC_READING 4095

#define CURRENT_SENSOR_ADC_BIAS 2331    

#define ZERO_DEVICE_VOLTAGE_CODE 1725

#define SAMPLE_COUNT 256

int main(void)
{
    setup_UART();
    setup_IO();
    setup_SPI();
    UART_transmit_string("USB Curve Tracer Starting\n\r");

    sweep_device();
    while(1)
    {
        PORTB |= (1 << PORTB0);
        PORTD |= (1 << PORTD7);

        //zero_device_voltage();
        //set_DAC(400);
        //set_DAC(0);
        //set_DAC(1024);

        /*uint32_t zero_current_reading = average_ADC_reading(CURRENT_ADC_CHANNEL);
        for(uint16_t i = 0; i < 256; i++)
        {
            set_DAC(i);
        }*/

    }

    // The program should never return. 
    return 0;
}

void DAC_CS_toggle(void)
{
    PORTB ^= (1 << PORTB2);
}

// set the DAC to the given code
void set_DAC(uint16_t code)
{
    if(code <= DAC_RESOLUTION - 1)
    {
        uint16_t configuration_bits = 0x7000;
        uint16_t command_bits = configuration_bits | (code << 0x4);
        //uint16_t command_bits = configuration_bits | (code << 0x4);
        //uint16_t command_bits = 0b0111111111111111;
        uint8_t first_command_byte = command_bits >> 8;
        uint8_t second_command_byte = command_bits && 0xFF;
        DAC_CS_toggle();
        SPI_transceiver(first_command_byte);
        SPI_transceiver(second_command_byte);
        DAC_CS_toggle();
    } 
    // In all other cases, the code is out of range, so do nothing. 
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

/*uint32_t average_ADC_reading(uint8_t channel)
{
    uint16_t i;
    uint32_t sum = 0;
    for(i = 0; i < AVERAGING_SAMPLE_COUNT; i++)
    {
        uint16_t reading = get_ADC_reading(channel);
        while(reading > MAXIMUM_ADC_READING)
        {
            reading = get_ADC_reading(channel);
        }
        sum += reading;
    }

    return sum/AVERAGING_SAMPLE_COUNT;
}*/

uint16_t DAC_voltage_setting = 500;

/*void zero_device_voltage(void)
{
    uint32_t device_voltage = average_ADC_reading(VOLTAGE_ADC_CHANNEL);

    if(DAC_voltage_setting >= 0 && DAC_voltage_setting < 1024)
    {
        if(device_voltage > ZERO_DEVICE_VOLTAGE_CODE)
        {
            DAC_voltage_setting--;
        }
        else if(device_voltage < ZERO_DEVICE_VOLTAGE_CODE)
        {
            DAC_voltage_setting++;
        }
    }

    set_DAC(DAC_voltage_setting);
    UART_transmit_uint16_t(DAC_voltage_setting);
    UART_transmit_string("\n\r");
}*/

void sweep_device(void)
{
    uint16_t i;
   
    UART_transmit_string("Starting Sweep\n\r");
    for(i = 0; i < SAMPLE_COUNT; i++)
    {
        set_DAC(i);
        uint16_t voltage_reading = get_ADC_reading(CURRENT_ADC_CHANNEL, SINGLE_ENDED);
        uint16_t current_reading = get_ADC_reading(VOLTAGE_ADC_CHANNEL, SINGLE_ENDED);
    
        UART_transmit_uint16_t(voltage_reading);
        UART_transmit_string(" , ");
        UART_transmit_uint16_t(current_reading);
        UART_transmit_string("\n\r");
    }
    UART_transmit_string("Ending Sweep\n\r");
}