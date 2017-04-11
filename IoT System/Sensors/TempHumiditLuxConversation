void setup(void) {
  Serial.begin(9600);   
  pinMode (soundDetectedPin, INPUT) ; 
}


void loop(void) {
  photocellReading = analogRead(photocellPin);  
 
  //Serial.print("Illuminance = ");
  Serial.print(photocellReading);     // the analog reading of Illuminance
  Serial.print(",");
  int chk = DHT.read11(DHT11_PIN);
  //Serial.print("Temperature = ");
  Serial.print(DHT.temperature);  //the digital reading of Temp
  Serial.print(",");
  //Serial.print("Humidity = ");
  Serial.print(DHT.humidity);   // the digital reading of humidity
  Serial.print(",");
  int sta = digitalRead (soundDetectedPin);
  if (sta == 1)
  {
     Serial.print("Y");
  }
  else
  {
    Serial.print("N");
  }
  Serial.println();
  delay(1000);
}
