int array[] = {2,3,4,5,6,7,8,9,10,11,12,13};
 int i = 0;
void setup() { 
 pinMode(1, OUTPUT);
 pinMode(2, OUTPUT);
 pinMode(3, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
 pinMode(6, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(8, OUTPUT);
 pinMode(9, OUTPUT);
 pinMode(10, OUTPUT);
 pinMode(11, OUTPUT);
 pinMode(12, OUTPUT);
 pinMode(13, OUTPUT);
 
 
 

 Serial.begin(9600);
}

void loop() {
 byte byteRead;
/* check if data has been sent from the computer: */
 if (Serial.available()) { 
    

 /* read the most recent byte */
 byteRead = Serial.read();
 //You have to subtract '0' from the read Byte to convert from text to a number.
 //byteRead=byteRead-'0';
 //Turn off all LEDs if the byte Read = 0
   if(byteRead=='0'){
  digitalWrite(array[i], LOW);
  //delay(1000);
   }
 //Turn LED ON depending on the byte Read.
   else{
   digitalWrite(array[i], HIGH);
   //delay(1000);// set the LED on
   }
   i=i+1;
  if(i==12){
    delay(5000);
     i=0;
   }
 }}
