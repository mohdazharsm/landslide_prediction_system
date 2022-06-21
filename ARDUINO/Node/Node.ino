#include <RF24.h>
#include <RF24Network.h>
#include <SPI.h>
RF24 radio(7, 8);               // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t this_node = 01;   // Address of this node in Octal format ( 04,031, etc)
const uint16_t GateWay = 00;      
  

uint8_t data[5];

const bool debugg = true;

void setup() {
  SPI.begin();
  if(debugg)Serial.begin(9600);
  radio.begin();
  network.begin(90, this_node);  //(channel, node address)
}
void loop() {
  network.update();
  data[0] = get_sensor_value(A3, 1024, 700);
  data[1] = get_sensor_value(A7, 1024, 700);
  data[2] = get_sensor_value(A4, 150, 700);
  data[3] = get_sensor_value(A5, 150, 700);
  data[4] = get_sensor_value(A6, 150, 700);

  RF24NetworkHeader header(GateWay);
  bool ok = network.write(header, &data, sizeof(data)); // Send the data
  }

uint8_t get_sensor_value(int pin,int initial,int Final)
  {
    unsigned long potValue = analogRead(pin);  // Read the potentiometer value
    uint8_t mapedVal = map(potValue, initial, Final, 0, 255);
    return mapedVal;
    }
