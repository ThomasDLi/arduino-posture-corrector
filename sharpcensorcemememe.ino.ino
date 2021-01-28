#include <SharpIR.h>
#include <math.h>
#include <Button.h>

// if you're using different pins than the ones shown here, change the pins.

#define ir A0
#define irb A5
#define model 20150
#define irq A3
// ir: the pin where your sensor is attached
// model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y
//                                            (working distance range according to the datasheets)

SharpIR SharpIR1(ir, model);  // middle sensor
SharpIR SharpIR2(irb, model); // lower sensor
SharpIR SharpIR3(irq, model); // upper sensor
Button button1(12);
void setup() {
  Serial.begin(9600);
  button1.begin();
}
void loop() {
  delay(500);   

  unsigned long pepe1=millis();

  int dis=SharpIR1.distance();
  int dis1=SharpIR2.distance();
  int dis2=SharpIR3.distance();

// start of debugging code. this was just code that I used while debugging the program. You can remove it if you want.
  Serial.print("Mean distance 1: ");
  Serial.println(dis); 

  Serial.print("Mean distance 2: ");
  Serial.println(dis1); 

  Serial.print("Mean distance 3: ");
  Serial.println(dis2); 
  // end of debugging code
  int x=190;
  int ex=190; 
  // start of 2nd debugging code block
  Serial.println("lower back angle");
  float y=dis1 - dis;
  float ans=atan(y/x);
  Serial.println(ans * 100);
  Serial.println("upper back angle");
  float ey=dis2 - dis;
  float anss=atan(ey/ex);
  Serial.println(anss * 100);
  // end of 2nd debugging code block
  
  // change the ">15" and "< -3" to adjust the threshhold (how far you can lean without it beeping)
  if ((anss * 100) > 15 or (ans * 100) < -3){
    Serial.println("bad posture");
      tone(8, 440, 1000);
}
}
