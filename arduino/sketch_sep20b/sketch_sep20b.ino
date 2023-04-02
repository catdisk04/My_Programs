#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

void _delay(float seconds) {
  long endTime = millis() + seconds * 1000;
  while(millis() < endTime) _loop();
}

void setup() {
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  while(1) {
      if((digitalRead(7) == 1) || (digitalRead(8) == 1)){
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
      digitalWrite(9,LOW);
      digitalWrite(10,HIGH);
      }
      else{
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      digitalWrite(9,HIGH);
      digitalWrite(10,LOW);
      _delay(1);
      }

      _loop();
  }

}

void _loop() {
}

void loop() {
  _loop();
}
