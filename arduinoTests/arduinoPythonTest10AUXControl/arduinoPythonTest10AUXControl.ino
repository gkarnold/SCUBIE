// Test 5
// Python will be sending the value input form the left vertical controller axis to arduino
// Arduino will read this value and send it back to python and use it to control the intensity of and LED

// Sets up the LED/motor control ports
int leftPin = 10;
int rightPin = 11;
int verticalPin = 9;

int sensorPin = 2; 

void setup() {
  // Begins the serial connection
  Serial.begin(9600);
  Serial.println("Ready");

  // Sets up the pin outputs
  pinMode(leftPin,OUTPUT);
  pinMode(rightPin,OUTPUT);
  pinMode(verticalPin,OUTPUT);
  pinMode(sensorPin,INPUT);
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
    // Chars for the index buttons
    String indexLeftChar;
    String indexRightChar;

    // Reads from serial until L is read, this is the left motor control information
    headerChar = Serial.readStringUntil('H');
    leftChar = Serial.readStringUntil('L');
    rightChar = Serial.readStringUntil('R');
    verticalChar = Serial.readStringUntil('V');
    indexLeftChar = Serial.readStringUntil('Q');
    indexRightChar = Serial.readStringUntil('W');

    // Convers the strings to integers (-1 is since the axis are fliped on the controller)
    int leftValue = 1*atoi(leftChar.c_str());
    int rightValue = 1*atoi(rightChar.c_str());
    int verticalValue = 1*atoi(verticalChar.c_str());
    int indexLeftValue = 1*atoi(indexLeftChar.c_str());
    int indexRightValue = 1*atoi(indexRightChar.c_str());
 
    // Combines the data read together so that it can be sent back to Python to confirm the loop
    String combinedChar = leftChar + 'L' + rightChar + 'R' + verticalChar + 'V' + indexLeftChar + 'Q' + indexRightChar + 'W';
    // Controls the left motor 
    /*(We want an output between 100 and 250. This keeps a constant voltage of about 
     * 2V on the ES when no trottle is applied so that the ESC doesn't disconnect.
     * 250 provides approximately 5 volts to the ESC which is effectively max throttle
     */

    
    // Working  code for right trigger
//    if (indexRightValue > 50)
//    {
//      analogWrite(rightPin,230);
//      Serial.println(230);
//    }
//    else
//    {
//      analogWrite(rightPin,150);
//      Serial.println(150);
//    }

    // Attempt to get it working with left stick only
    if (leftValue >= 0)
    {
      analogWrite(rightPin,150);
      Serial.println(150);
    }
    else
    {
      analogWrite(rightPin,230);
      Serial.println(230);
    }
    
//    analogWrite(rightPin,1024/4*indexRightValue/100);
    analogWrite(leftPin,255/2 + 255/2*abs(leftValue)/100);
    
      
    
//    analogWrite(rightPin,1024/4*rightValue/100);
    // Turns on the vertical light
    analogWrite(verticalPin,250*verticalValue/100);
//    analogWrite(verticalPin,sensorValue);

  }
  // Waits 100 ms before checking again
  //delay(100);


  
}

