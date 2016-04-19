void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
}

void loop() {
  char inByte = ' ';
  if(Serial.available()){ // Checks to see if there is data to be received
    char inByte = Serial.read(); // Reads the data if there is data to be received
    Serial.println(inByte); // Sends the data back to the serial connection
  }
  delay(100); // Waits for 1/10 of a second before checking again
}
