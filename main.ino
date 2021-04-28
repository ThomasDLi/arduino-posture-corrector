//libaries
#include <SharpIR.h>
#include <math.h>

//pins
#define topir A0
#define middleir A3
#define bottomir A5

//model of sharpir
#define model 20150
// ir: the pin where your sensor is attached
// model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y
//                                            (working distance range according to the datasheets)

//defining the sensors themselves withing the libarry
SharpIR SharpIR1(topir, model);
SharpIR SharpIR2(middleir, model);
SharpIR SharpIR3(bottomir, model);
void setup() {
  //starting the serial
  Serial.begin(9600);
}

void loop() {
  //something that the libary needs, idk what this does
  unsigned long pepe1=millis();

  //distance getting
  int dis1=SharpIR1.distance();
  int dis2=SharpIR2.distance();
  int dis3=SharpIR3.distance();

  //distances between each sensor
  int botmid = 190; //distance in mm between bottom sensor and middle sensor
  int midtop = 190; //distance in mm between middle sensor and top sensor

  //upper back angle
  float distancetop = dis1 - dis2;
  float anglebeforetop = atan(distancetop / midtop);
  float angletop = anglebeforetop * 100;

  //lower back angle
  float distancelow = dis2 - dis3;
  float anglebeforelow = atan(distancelow / botmid);
  float anglelow = anglebeforelow * 100;

  //delay bcuz why not
  delay(100);

  //checking for bad posture
  if (angletop > 9 or anglelow < -6){
    //beeping the buzzer for one second if user has bad posturer
    tone(8, 440, 1000);    
    }
}
