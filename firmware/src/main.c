#include <avr/io.h>
#include <stdint.h>

#include "main.h"

#include "UART.h"
#include "spi.h"
#include "MCP3204.h"
#include "MCP4911.h"

static uint16_t DAC_voltage_setting = 0;
static Mode mode;
static uint8_t sweeping = 0;

int main(void)
{
    setup_UART();
    setup_IO();
    setup_SPI();

    mode = BIDIRECTIONAL;
    zero_device_voltage();

    while(1)
    {
        device_operation();
        if(!sweeping)
        {
            zero_device_voltage();
            turn_on_green_LED();
        }
    }

    // The program should never return. 
    return 0;
}

void device_operation(void)
{
    zero_device_voltage();
    turn_off_red_LED();
    turn_on_green_LED();
    uint8_t command = UART_receive_character();

    if(!external_voltage_supply_detected())
    {
        power_disconnected(command);
    }
    else
    {
        switch(command)
        {
            case SWEEP_COMMAND_CHARACTER:
                turn_off_green_LED();
                turn_on_red_LED();
                sweep_device();
                turn_off_red_LED();
                turn_on_green_LED();
                break;
            case UNIDIRECTIONAL_COMMAND_CHARACTER:
                mode = UNIDIRECTIONAL;
                break;
            case BIDIRECTIONAL_COMMAND_CHARACTER:
                mode = BIDIRECTIONAL;
                break;
            default:
                break;
        }
    }
}

void power_disconnected(uint8_t command)
{
    turn_on_red_LED();
    turn_off_green_LED();

    if(command == SWEEP_COMMAND_CHARACTER || 
    command == UNIDIRECTIONAL_COMMAND_CHARACTER || 
    command == BIDIRECTIONAL_COMMAND_CHARACTER)
    {
        print_starting_command();
        print_power_disconnected();
        print_ending_command();
    }
}

void turn_on_green_LED(void)
{
    PORTB |= (1 << PORTB0);
}

void turn_off_green_LED(void)
{
    PORTB &= ~(1 << PORTB0);
}   

void turn_on_red_LED(void)
{
    PORTD |= (1 << PORTD7);
}

void turn_off_red_LED(void)
{
    PORTD &= ~(1 << PORTD7);
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
    // Set the supply voltage detect to input.
    DDRD &= ~(1 << DDD6);
}

uint8_t external_voltage_supply_detected(void)
{
    return (PIND & (1 << PIND6)) != 0;
}

void zero_device_voltage(void)
{
    uint16_t reference_voltage = get_ADC_reading(SINGLE_ENDED, REFERENCE_ADC_CHANNEL);

    while(1)
    {
        uint16_t voltage_reading = get_ADC_reading(SINGLE_ENDED, VOLTAGE_ADC_CHANNEL);

        if(voltage_reading > reference_voltage && DAC_voltage_setting > 0)
        {
            DAC_voltage_setting--;
        }
        else if(voltage_reading < reference_voltage && DAC_voltage_setting <= DAC_RESOLUTION)
        {
            DAC_voltage_setting++;
        }

        set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);

        uint8_t above_range = voltage_reading > reference_voltage + ZERO_DEVICE_MARGIN;
        uint8_t below_range = voltage_reading < reference_voltage - ZERO_DEVICE_MARGIN;

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

uint8_t over_current(IV_Sample sample)
{
    return sample.current_code > MAX_POSITIVE_CURRENT_CODE || sample.current_code < MAX_NEGATIVE_CURRENT_CODE;
}

void print_starting_command(void)
{
    UART_transmit_string(START_COMMAND);
    UART_transmit_string(NEW_LINE);
}

void print_ending_command(void)
{
    UART_transmit_string(END_COMMAND);
    UART_transmit_string(NEW_LINE);
}

void print_power_disconnected(void)
{
    UART_transmit_string(POWER_DISCONNECTED);
    UART_transmit_string(NEW_LINE);
}

void print_sample(IV_Sample sample)
{
    UART_transmit_uint16_t(sample.current_code);
    UART_transmit_string(DELIMINATOR);
    UART_transmit_uint16_t(sample.voltage_code);
    UART_transmit_string(NEW_LINE);
}

void sweep_device(void)
{
    print_starting_command();
    zero_device_voltage();

    while(DAC_voltage_setting <= MAXIMUM_DAC_CODE)
    {
        DAC_voltage_setting++;
        set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);
        IV_Sample sample;
        sample = sample_IV();
        print_sample(sample);

        if(over_current(sample))
        {
            break;
        }
    }

    zero_device_voltage();

    if(mode == BIDIRECTIONAL)
    {
        while(DAC_voltage_setting > MINIMUM_DAC_CODE)
        {
            DAC_voltage_setting--;
            set_DAC(DAC_voltage_setting, GAIN_1X, BUFFERED);
            IV_Sample sample;
            sample = sample_IV();
            print_sample(sample);

            if(over_current(sample))
            {
                break;
            }
        }

        zero_device_voltage();
    }
    
    print_ending_command();
}