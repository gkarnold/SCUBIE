#include <Servo.h>

Servo esc;

int sensorPin = 2;    // The potentiometer is connected to
                      // analog pin 0
                      
int ledPin = 11;      // The LED is connected to digital pin 13

void setup() // this function runs once when the sketch starts up
{
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
//  esc.attach(ledPin);
}


void loop() 
{

  int sensorValue;
  int servoValue;

  sensorValue = analogRead(sensorPin);    
  
  Serial.print("Value: ");
//  Serial.println(sensorValue/4);
  
  analogWrite(ledPin, sensorValue/4);     // Turn the LED on
//  analogWrite(ledPin, 255);     // Turn the LED on

//  servoValue = map(sensorValue, 0, 1023, 0, 179);
//  esc.write(servoValue);


}

