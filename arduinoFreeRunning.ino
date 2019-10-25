  
int analogPin = A0;     
int data = 0; 
char userInput;          

void setup(){

  Serial.begin(9600);          //  setup serial

}

void loop(){
// read the input on analog pin 12:

       float voltage = analogPin * (5.0 / 1023.0);

      
      data = analogRead(analogPin);    // read the input pin
      Serial.println(voltage);
      delay(1);

} // Void Loop
