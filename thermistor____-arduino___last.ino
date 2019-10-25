//int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;
char userInput;   
void setup() {
Serial.begin(9600);
}

void loop() {
// read the input on analog pin 12:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  Serial.println(voltage);





 // Vo = analogRead(ThermistorPin);
  //R2 = R1 * (1023.0 / (float)Vo - 1.0);
  //logR2 = log(R2);
  //T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  //Tc = T - 273.15;
  //Tf = (Tc * 9.0)/ 5.0 + 32.0; 

  //Serial.print("Temperature: "); 
 // Serial.print(Tf);
  //Serial.print(" F; ");
  Serial.println(Vo);
 // Serial.println(" C");   

  delay(1000);
}
