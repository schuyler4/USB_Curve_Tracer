//
//      FILENAME: MCP3002_arduino_test.ino
//
// description: Code to test the SPI interface for the MCP3002 
// using an arduino. This is done before implementing with bare metal C code
// on an ATtiny. 
//

#include <SPI.h>

#define CHIP_SELECT 10
#define ADC_RESOLUTION 1024
#define VOLTAGE_REFERENCE 5.064

// header for read code
int read_code(void);
float get_voltage(int code);

void setup() 
{
  pinMode(CHIP_SELECT, OUTPUT);
  
  SPI.begin();
  SPI.beginTransaction(SPISettings(10000, MSBFIRST, SPI_MODE1));
  

  Serial.begin(9600);
}

void loop() 
{
  int code = read_code();
  float voltage = get_voltage(code);
  delay(100);

  Serial.println(voltage);
}

int read_code(void)
{
  int recieved_code;
  
  digitalWrite(CHIP_SELECT, LOW);
  delay(10);
  recieved_code = SPI.transfer16(0x6000);
  delay(10);
  digitalWrite(CHIP_SELECT, HIGH);

  return recieved_code;
}

float get_voltage(int code)
{
  float LSB = VOLTAGE_REFERENCE/ADC_RESOLUTION;
  return (float)(LSB*code);
}
