// Simple program that will turn on one of four lights based on an input from python

// Sets the LED pin numbers
int ledPins[] = {13,12,11,10};
int mode = 0;
void setup() {
  int index;
  // Sets up the pin outputs
  for(index = 0; index <= 3; index++)
  {
    pinMode(ledPins[index],OUTPUT);
  }
  
  // Starts the serial connection with baud rate of 9600
  Serial.begin(9600);
  // Outputs that Arduino is ready
  Serial.println("Ready");
}

void loop() {
  // Sets up an integer variable
  int inByte;
  
  // If loop that checks for avaialbe serial data to read
  if(Serial.available())
  {
    // Reads the data from the serial connection
   int inByte = Serial.read()-48;
   Serial.println(inByte);

     // Set of if statements that check the input from python lights up the appropriate LED
    if(inByte == 0)
    {
     digitalWrite(ledPins[0],LOW);
     digitalWrite(ledPins[1],LOW);
     digitalWrite(ledPins[2],LOW);
     digitalWrite(ledPins[3],LOW); 
    }
    else if (inByte == 1)
    {
     digitalWrite(ledPins[0],HIGH);
     digitalWrite(ledPins[1],LOW);
     digitalWrite(ledPins[2],LOW);
     digitalWrite(ledPins[3],LOW); 
    }
    else if (inByte == 2)
    {
     digitalWrite(ledPins[0],LOW);
     digitalWrite(ledPins[1],HIGH);
     digitalWrite(ledPins[2],LOW);
     digitalWrite(ledPins[3],LOW); 
    }
    else if (inByte == 3)
    {
     digitalWrite(ledPins[0],LOW);
     digitalWrite(ledPins[1],LOW);
     digitalWrite(ledPins[2],HIGH);
     digitalWrite(ledPins[3],LOW); 
    }
    else if (inByte == 4)
    {
     digitalWrite(ledPins[0],LOW);
     digitalWrite(ledPins[1],LOW);
     digitalWrite(ledPins[2],LOW);
     digitalWrite(ledPins[3],HIGH); 
    }
    else
    {
     digitalWrite(ledPins[0],LOW);
     digitalWrite(ledPins[1],LOW);
     digitalWrite(ledPins[2],LOW);
     digitalWrite(ledPins[3],LOW); 
    }
  } 
}
