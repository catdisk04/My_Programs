#define BLYNK_TEMPLATE_ID "TMPLe2jgCcnA"
#define BLYNK_DEVICE_NAME "blink"
#define BLYNK_AUTH_TOKEN "0D9Q46TQm3Qwih4ANyhoGpD8UDuyl0Fr"
#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char ssid[]="sweet home";
char pass[] = "9790886577";
char auth[] = BLYNK_AUTH_TOKEN;

//BlynkTimer timer;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  //timer.setInterval(1000L, myTimerEvent);
  pinMode(5, OUTPUT);
}

void myTimerEvent(){
  
}

BLYNK_WRITE(V0)
{
  // any code you place here will execute when the virtual pin value changes
  Serial.print("Blynk.Cloud is writing something to V1\n");
  int virtual_pin_value = param.asInt();
  if(1 == virtual_pin_value){
    digitalWrite(5, HIGH);
  }
  else{
    digitalWrite(5, LOW);

  }
}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();
  //timer.run();
  
}
