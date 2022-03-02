#include "Arduino.h"
#include "heltec.h"
#include "String.h"
String output1, output2; 
float Vout;
void setup() {
  // put your setup code here, to run once:
  Heltec.begin(true /*DisplayEnable Enable*/, false /*LoRa Disable*/, true /*Serial Enable*/);
  Heltec.display->flipScreenVertically();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_10);
}

void loop() {
  // put your main code here, to run repeatedly:
    // Font Demo1
    // create more fonts at http://oleddisplay.squix.ch/
    Heltec.display->clear();

      Heltec.display->setFont(ArialMT_Plain_10);
      Heltec.display->drawString(0,0,"Howdy!");
      output1 = calculateScore();
      output2 = calculateVolts();

    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);
    Heltec.display->drawString(0, 12, output1); // Score
    Heltec.display->display();

    //Display resistance
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);
    Heltec.display->drawString(0, 36, output2);// volts
    Heltec.display->display();
    delay(1000);// Every Second
    Serial.println(output1);
}

float calculateVolts()
{
  float sum = 0;
  for(int i = 0; i < 100; i++)
  {
    sum += analogRead(2); // oversampling 100 times
  }
  
  Vout = sum/100 /4096.0 * 3.3;
  float Vin = 3.3;
  float R2 = 1000000;
  int R1 = (Vin/Vout * R2) - R2; // derived from resistor divider equation

  return Vout;
}

int calculateScore()
{
  float sum = 0;
  for(int i = 0; i < 100; i++)
  {
    sum += analogRead(2); // oversampling 100 times
  }
  
  Vout = sum/100 /4096.0 * 3.3;
  float Vin = 3.3;
  float R2 = 1000000;
  int R1 = (Vin/Vout * R2) - R2; // derived from resistor divider equation

  return R1;
}
