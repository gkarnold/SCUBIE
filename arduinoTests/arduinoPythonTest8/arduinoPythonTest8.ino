#include <Servo.h>
 
Servo motor;
int throttlePin = 2;
int escPin = 10;
 
void setup()
{
  Serial.begin(38400);
  Serial.println("Program begin...");
  Serial.println("This program will calibrate the ESC.");

//  // Servo Method
//  motor.attach(escPin); 
  
  // Non-Serbo Method
  pinMode(escPin,OUTPUT);
  
}
 
void loop()
{

//  // Servo Method
//  int throttle = analogRead(throttlePin);
//  int throttleMap = map(throttle, 0, 1023, 18, 160);
//  motor.write(throttleMap);
//  Serial.println(throttle);
//  Serial.println(throttleMap);

  // Non-Servo Method
  int throttle = analogRead(throttlePin);
  analogWrite(escPin,255/2 + 255/2*abs(throttle)/1023);
  
}
