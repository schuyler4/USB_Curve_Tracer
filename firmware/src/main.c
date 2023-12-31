//
// FILENAME: main.c
//
// description: This is main file for the USB curve tracer program. This file contains
// most of the control, zeroing, and sweeping of the device. 
//
// Written by Marek Newton
//

#include <avr/io.h>
#include <stdint.h>

#include "main.h"

#include "UART.h"
#include "spi.h"
#include "MCP3204.h"
#include "MCP4911.h"

static uint16_t DAC_voltage_setting;
static Mode mode;
static uint8_t sweeping;
static uint8_t user_programmed_current_limit_used;
static uint16_t user_programmed_current_limit;

int main(void)
{
    DAC_voltage_setting = 0;
    sweeping = 0;
    user_programmed_current_limit_used = 0;

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
            case CURRENT_LIMIT_COMMAND_CHARACTER:
                user_programmed_current_limit = receive_current_code();
                user_programmed_current_limit_used = 1;
                UART_transmit_uint16_t(user_programmed_current_limit);
                UART_transmit_string(CURRENT_LIMIT_SET);
                break;
            case MAX_CURRENT_LIMIT_COMMAND_CHARACTER:
                user_programmed_current_limit_used = 0;
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

uint16_t receive_current_code(void)
{
    // most significant byte first
    uint8_t bytes[CURRENT_CODE_BYTE_COUNT];
    uint8_t byte_count = 0;

    while(1)
    {
        uint8_t byte = (uint8_t)UART_receive_character();
        if(byte != 0)
        {
            bytes[byte_count] = byte;
            byte_count++;
            if(byte_count == CURRENT_CODE_BYTE_COUNT)
            {
                break;
            }
        }
    }

    return bytes[0] << BYTE_SIZE | bytes[1];
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
    if(user_programmed_current_limit_used && user_programmed_current_limit > 900)
    {
        return sample.current_code > user_programmed_current_limit;
    }
    else
    {
        return sample.current_code > MAX_POSITIVE_CURRENT_CODE || sample.current_code < MAX_NEGATIVE_CURRENT_CODE;
    }
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
    UART_transmit_string(NEW_LINE_AND_CARRIAGE_RETURN);
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