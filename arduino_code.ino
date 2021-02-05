#include <Servo.h>
int servo=9;
int servo_pos1=90;
int servo_pos2=0;
Servo my_servo;
void setup() {
String b;
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);

Serial.begin(9600);
my_servo.attach(servo);
}

void loop() {
        my_servo.write(servo_pos2);

if(Serial.available()){
    digitalWrite(12,HIGH);
  delay(6000);
  digitalWrite(12,LOW);

  delay(2000);

if(Serial.readString()!="unknown")
{
  digitalWrite(13,HIGH);
    my_servo.write(servo_pos1);

  delay(5000);
  digitalWrite(13,LOW);
      my_servo.write(servo_pos2);

  
 Serial.println("unknown");


 }
  else{
    digitalWrite(13,LOW);
    }
}
}
