void setup() {
  Serial.begin(9600);
}

void loop() {
  int val_pot = analogRead(A1);
  Serial.println(val_pot);
  delay(100);
}