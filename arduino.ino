int ledPin = 13; // Pin connected to the LED
int state = 0;  // Initial state (LED is off)

void setup() {
  pinMode(ledPin, OUTPUT);  // Set the LED pin as an output
  Serial.begin(9600);      // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
      state = 1;
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);   // Turn off the LED
      state = 0;
    }
  }
}