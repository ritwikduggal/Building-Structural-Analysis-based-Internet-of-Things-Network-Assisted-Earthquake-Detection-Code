#include<Wire.h>
const int MPU6050_addr = 0x68;
#define sensor1 2
#define sensor2 3
#define sensor3 4
int16_t aX, aY, aZ, gX, gY, gZ;
void setup() 
{
  pinMode(sensor1, OUTPUT);
  pinMode(sensor2, OUTPUT);
  pinMode(sensor3, OUTPUT);
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
}
void loop() 
{
  digitalWrite(sensor1, LOW);
  digitalWrite(sensor2, HIGH);
  digitalWrite(sensor3, HIGH);
  Wire.beginTransmission(MPU6050_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_addr,14,true);
  aX=Wire.read()<<8|Wire.read();
  aY=Wire.read()<<8|Wire.read();
  aZ=Wire.read()<<8|Wire.read();
  gX=Wire.read()<<8|Wire.read();
  gY=Wire.read()<<8|Wire.read();
  gZ=Wire.read()<<8|Wire.read();
  delay(50);
  Serial.print("aX = "); Serial.print(aX);
  Serial.print(" || aY = "); Serial.print(aY);
  Serial.print(" || aZ = "); Serial.print(aZ);
  Serial.print(" || gX = "); Serial.print(gX);
  Serial.print(" || gY = "); Serial.print(gY);
  Serial.print(" || gMZ = "); Serial.println(gZ);
  delay(20);
  Wire.endTransmission(true);
}
