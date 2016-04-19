int count = 0;

void setup() {
  Serial.begin(9600);
}
void loop() {
  
  Serial.print("I am counting to: ");
  Serial.print(count);
  Serial.println(" Mississippi.");
  count = count + 1;
  delay(1000);
  
}
