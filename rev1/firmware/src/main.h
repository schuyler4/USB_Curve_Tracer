// header file for main

#ifndef MAIN_H
#define MAIN_H

void set_DAC(uint16_t code);
void set_relays(void);
int read_ADC(void);
void split_number(uint16_t number, uint8_t *high, uint8_t *low);
void set_DAC_code(uint16_t code);
void toggle_DAC_CS(void);
void DAC_CS_toggle(void);
void set_DAC(uint16_t code);
void test_DAC(void);
void ADC_CS_toggle(void);

#endif
