// Prototype controls test program
/*
   This Arduino script will be used to test the movement controls of the ROV.
   It can handle forward and backwards for the horizontal thrusters as well as the vertical thrusters.
   It will also take readings from the pressure sensor and report those to the user.
*/

// Includes
#include <Wire.h>
#include "MS5837.h"
#include <Servo.h>

// Sets up the pressure sensor which will use inputs A4 and A5
MS5837 pressureSensor;

// Sets up the vertical esc servo
Servo leftESC;
Servo rightESC;

// Sets up the ESC control ports
int leftPin = 10;
int rightPin = 11;
int verticalPin = 9;
int reversePin = 3;

// Initial setup
void setup() {
  // Begins the serial connection
  Serial.begin(9600);
  Serial.println("Ready");

  // Begins wire
  Wire.begin();

  // Initializes the pressure sensor
  pressureSensor.init();

  // Sets the fluid density
  pressureSensor.setFluidDensity(980);

  // Sets up the ESC control pin outputs
//  pinMode(leftPin, OUTPUT);
//  pinMode(rightPin, OUTPUT);
  pinMode(verticalPin,OUTPUT);
  pinMode(reversePin,OUTPUT);

  // Sets up the left and right ESC Servos
  leftESC.attach(leftPin);
  rightESC.attach(rightPin);

}

// Main Loop
void loop() {

//  // Sets the input size
//  int inputSize = 4;
//
//  // Sets up the character inputs
//  char input[inputSize];

  // Checks to see if there are any commands coming down the serial connection
  if (Serial.available()) {

    // Char that will be used to read from the serial port
    char inChar = Serial.read();

    // Creates a character for the header
    String headerChar;
    // Creates a character for the left esc
    String leftChar;
    // Creates a character for the right esc
    String rightChar;
    // Creates a character for the vertical esc
    String verticalChar;
 
    // Reads from serial until the selected character is read, this is the ESC control information
    headerChar = Serial.readStringUntil('H');
    leftChar = Serial.readStringUntil('L');
    rightChar = Serial.readStringUntil('R');
    verticalChar = Serial.readStringUntil('V');

    // Convers the strings to integers (-1 is since the axis are fliped on the controller)
    float leftValue = 1 * atoi(leftChar.c_str());
    float rightValue = 1 * atoi(rightChar.c_str());
    float verticalValue = 1 * atoi(verticalChar.c_str());

    // Combines the data read together so that it can be sent back to Python to confirm the loop
        String combinedChar = leftChar + 'L' + rightChar + 'R' + verticalChar + 'V';

    // Sends the desired throttle percentage to the horizontal ESCs
    int leftValueMap= map(leftValue, -100, 100, 0, 179);
    int rightValueMap= map(rightValue, -100, 100, 0, 179);
    leftESC.write(leftValueMap);
    rightESC.write(rightValueMap);
    Serial.println(leftValueMap);

//    analogWrite(leftPin, 255 / 2 + 255 / 2 * abs(leftValue) / 100);
//    analogWrite(rightPin, 255 / 2 + 255 / 2 * abs(rightValue) / 100);

    // Vertical ESC controls
//    analogWrite(verticalPin,255/2 + 255/2*abs(verticalValue) / 100);
//    Serial.println(255/2 + 255/2*abs(verticalValue) / 100);
//    analogWrite(verticalPin,255);
//    Serial.println(255);

//    // Code for forwward and reverse
//    if (verticalValue >= 0)
//    {
//      analogWrite(reversePin, 0);
//      analogWrite(verticalPin,255/2 + 255/2*abs(verticalValue) / 100);
//      Serial.println(0);
//    }
//    else
//    {
//      analogWrite(reversePin, 255);
//      analogWrite(verticalPin,255/2 + 255/2*abs(verticalValue) / 100);
//      Serial.println(255);
//    } 

  }


  //  // Reads the data from the pressure sensor
  //  pressureSensor.read();
  //  // Reads the pressure from the pressure sensor
  //  int pressure = pressureSensor.pressure();
  //  String pressureString = String(pressure);
  //  // Reads the depth from the pressure sensor
  //  float depth = pressureSensor.depth();
  //  String depthString = String(depth);
  //  // Reads the temperature from the pressure sensor
  //  float temperature = pressureSensor.temperature();
  //  String temperatureString = String(temperature);
  //  // Combines the data from the pressure sensor for sending through the serial connection
  //  String pressureSensorData = pressureString + 'P' + depthString + 'D' + temperatureString + 'T';
  //  // Sends the data from the pressure sensor through the serial connection
  //  Serial.println(pressure);


}

