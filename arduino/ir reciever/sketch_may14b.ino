//IR Remote

#include <IRremote.h>
int IRpin = 12;
int pins[4]={4, 5, 6, 7};
IRrecv irrecv(IRpin);
decode_results result;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i=0; i++; i<=3){
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
  Serial.println("Starting IR");
  irrecv.enableIRIn();
  Serial.println("Start successful");
  digitalWrite(1, LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(irrecv.decode(&result)){
    Serial.println(result.value, HEX);
    if(result.value == 0x52120F2){
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(4, LOW);
    }
    if(result.value == 0xDE3AA631){
      digitalWrite(5, HIGH);
      delay(1000);
      digitalWrite(5, LOW);
    }    if(result.value == 0x8753BA5C){
      digitalWrite(6, HIGH);
      delay(1000);
      digitalWrite(6, LOW);
    }    if(result.value == 0x69893291){
      digitalWrite(7, HIGH);
      delay(1000);
      digitalWrite(7, LOW);
    }
    irrecv.resume();
  }
}
