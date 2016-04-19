// Test application to try and get the blue robotics pressure sensor working
#include <Wire.h>
#include "MS5837.h"

MS5837 sensor;

void setup() {
  // Initialize the Serial connections
  Serial.begin(9600);

  // Sending information down the Serial connection information the user the Arduino is starting
  Serial.println("Starting");

  // Begining wire
  Wire.begin();

  // Initializing the sensor
  sensor.init();

  // Setting the fluid density
  sensor.setFluidDensity(1000);

}

void loop() {
  sensor.read();

  Serial.print("Pressure: ");
  Serial.print(sensor.pressure());
  Serial.println(" mbar");

  Serial.print("Temperature: "); 
  Serial.print(sensor.temperature()); 
  Serial.println(" deg C");

  Serial.print("Depth: ");
  Serial.print(sensor.depth());
  Serial.println(" m");

  delay(1000);

}
