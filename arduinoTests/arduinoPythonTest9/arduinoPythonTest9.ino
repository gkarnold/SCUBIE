// Test 5
// Python will be sending the value input form the left vertical controller axis to arduino
// Arduino will read this value and send it back to python and use it to control the intensity of and LED

// Sets up the LED/motor control ports
int leftPin = 10;
int rightPin = 11;
int verticalPin = 9;

int sensorPin = 2; 

#include <Servo.h>
Servo esc;

void setup() {
  // Begins the serial connection
  Serial.begin(9600);
  Serial.println("Ready");

  // Sets up the pin outputs
  pinMode(rightPin,OUTPUT);
  pinMode(verticalPin,OUTPUT);
  pinMode(sensorPin,INPUT);

  esc.attach(verticalPin);
}

void loop(){
  // Sets up the input value
  int sensorValue;
  
  // Sets the input size
  int inputSize = 4;

  // Sets up the character inputs
  char input[inputSize];

  // Checks to see if there are any commands coming down the serial connection
  if (Serial.available()){

    // Reads the sensor value
    sensorValue = analogRead(sensorPin);

    // Char that will be used to read from the serial port
    char inChar = Serial.read();

    // Char for the header
    String headerChar;
    // Char for the left motor
    String leftChar;
    // Char for the right motor
    String rightChar;
    // Char for the vertical motors
    String verticalChar;

    // Reads from serial until L is read, this is the left motor control information
    headerChar = Serial.readStringUntil('H');
    leftChar = Serial.readStringUntil('L');
    rightChar = Serial.readStringUntil('R');
    verticalChar = Serial.readStringUntil('V');

    // Convers the strings to integers (-1 is since the axis are fliped on the controller)
    int leftValue = 1*atoi(leftChar.c_str());
    int rightValue = 1*atoi(rightChar.c_str());
    int verticalValue = 1*atoi(verticalChar.c_str());
 
    // Combines the data read together so that it can be sent back to Python to confirm the loop
    String combinedChar = leftChar + 'L' + rightChar + 'R' + verticalChar + 'V';
    
    // Controls the left motor
    int verticalValueMap = map(verticalValue,-100,100,18,160); 
    esc.write(verticalValueMap);
    Serial.println(verticalValueMap);
    
    
  }
  
//  esc.write(leftThrottle);
  
  
  // Waits 100 ms before checking again
  //delay(100); 
}
