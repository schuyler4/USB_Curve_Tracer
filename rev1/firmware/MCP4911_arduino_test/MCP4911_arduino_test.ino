//
//    FILENAME: MCP4911_arduino_test.ino
//
// description: Test of the MCP4911 chip using arduino. The main test is making
// sure that the whole refence can be optained. 
//
// Written By: Marek Newton
//

#include <SPI.h>

#define CHIP_SELECT 10

void setup() 
{
  pinMode(CHIP_SELECT, OUTPUT);

  SPI.begin();
  SPI.beginTransaction(SPISettings(10000, MSBFIRST, SPI_MODE1))

  Serial.begin(9600);

}

void loop() 
{


}
