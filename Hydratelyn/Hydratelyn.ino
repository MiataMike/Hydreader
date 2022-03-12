#include "Arduino.h"
#include "heltec.h"
#include "String.h"
#include "DHT.h"

#define DHTPIN 5
#define DHTTYPE DHT11
DHT dhtsensor = DHT(DHTPIN, DHTTYPE);
float h = 0;
float t = 0;

#define hydraPin 4
int incomingByte = 0;
String output1, output2; 
float Vout;
void setup() {
  // put your setup code here, to run once:
  Heltec.begin(true /*DisplayEnable Enable*/, false /*LoRa Disable*/, true /*Serial Enable*/);
  Heltec.display->flipScreenVertically();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_10);
  ledcSetup(0,1000, 8);
  ledcAttachPin(0,0);
  ledcWrite(0,255);
  dhtsensor.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
    // Font Demo1
    // create more fonts at http://oleddisplay.squix.ch/
    Heltec.display->clear();
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    h = dhtsensor.readHumidity();
    delay(500);
    // Read temperature as Celsius (the default)
    t = dhtsensor.readTemperature();
    delay(500);
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
    if (Serial.available() > 0) 
    {
    // read the incoming byte:
    incomingByte = Serial.read();
    }
    else {incomingByte = 0;}

    if(incomingByte == 115) // letter 's'
    {
      Serial.print(t);
      Serial.print(",");
      Serial.print(h);
      Serial.print(",");
      Serial.println(output1);
    }

}

float calculateVolts()
{
  float sum = 0;
  for(int i = 0; i < 100; i++)
  {
    sum += analogRead(hydraPin); // oversampling 100 times
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
    sum += analogRead(hydraPin); // oversampling 100 times
  }
  
  Vout = sum/100 /4096.0 * 3.3;
  float Vin = 3.3;
  float R2 = 1000000;
  int R1 = (Vin/Vout * R2) - R2; // derived from resistor divider equation

  return R1;
}
