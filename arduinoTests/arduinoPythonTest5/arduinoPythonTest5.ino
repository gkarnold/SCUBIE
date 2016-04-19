// Test 5
// Python will be sending the value input form the left vertical controller axis to arduino
// Arduino will read this value and send it back to python
void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
}

void loop(){
  // Sets the input size
  int inputSize = 4;

  // Sets up the character inputs
  char input[inputSize];

  // Checks to see if there are any commands coming down the serial connection
  if (Serial.available()){

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

    // Convers the strings to integers
    int leftValue;
    int rightValue;
    int verticalValue;

    leftValue = atoi(leftChar.c_str());
 
    // Combines the data read together so that it can be sent back to Python to confirm the loop
    String combinedChar = leftChar + 'L' + rightChar + 'R' + verticalChar + 'V';
    Serial.println(combinedChar);

  }
  // Waits 100 ms before checking again
  //delay(100);

  
}
/*
void loop() {
  char inByte = ' ';
  if(Serial.available()){ // Checks to see if there is data to be received
    String inByte = Serial.readString(); // Reads the data as a string if there is data to be received
    Serial.println(inByte); // Sends the data back to the serial connection
  }
  delay(100); // Waits for 1/10 of a second before checking again
}

void loop(){
  int INPUT_SIZE = 30
  // Reads the next command from Serial (add 1 slot to the end so we can put a character to terminate the looping)
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input,INPUT_SIZE);
  // Add the final character to end the C string
  input[size] = 0;

  // Reads the controller input axes
  char* command = strtok(input,",");
  while (command != 0)
  {
    // Spits the string
    int leftAxis = atoi(command);
  }
  
}
*/

