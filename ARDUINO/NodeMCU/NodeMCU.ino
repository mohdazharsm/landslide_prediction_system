#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "your_auth_code";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "ssid";
char pass[] = "password";

WidgetTerminal terminal(V0);
WidgetLED led1(V1);

 BlynkTimer timer;  
   
   
 BLYNK_CONNECTED() {  
   
  Blynk.syncAll();  
 } 

char dataIn = 'w';
char determinant;
char det;


int check(){
  if (Serial.available() > 0){// if there is valid data in the serial port
    dataIn = Serial.read();// stores data into a varialbe

    //check the code
    if (dataIn == 'w'){
      determinant = 'w';
    }
    else if (dataIn == 'g'){
      determinant = 'g';
    }
    else if (dataIn == 'y'){
      determinant = 'y';
    }
    else if (dataIn == 'o'){
      determinant = 'o';
    }
    else if (dataIn == 'r'){
      determinant = 'r';
    }
    else if (dataIn == 'm'){
      determinant = 'm';
    }
    }
  return determinant;
}




void myTimerEvent()  
 { 
  det = check(); //call check() subrotine to get the serial code
  //serial code analysis
  switch (det){
    case 'w':
    led1.on();
    Blynk.setProperty(V1, "color", "#FFFFFF");
    terminal.println("No rain fall");
    det = check();
    break;
   //------- 

    case 'g':
    led1.on();
    Blynk.setProperty(V1, "color", "#02A108");
    terminal.println("Normal rain fall");
    det = check();
    break;

    case 'y':
    led1.on();
    Blynk.setProperty(V1, "color", "#F9FF00");
    terminal.println("Be aware");
    det = check();
    break;

    case 'o':
    led1.on();
    Blynk.setProperty(V1, "color", "#F3631C");
    terminal.println("Take precaution, flood chance");
    det = check();
    break;

    case 'r':
    led1.on();
    Blynk.setProperty(V1, "color", "#FF0004");
    terminal.println("Landslide chance, evacuate");
    det = check();
    break;

    case 'm':
    led1.on();
    Blynk.setProperty(V1, "color", "#FF00A6");
    terminal.println("Landslide occures");
    det = check();
    break;

    default:  {
    led1.off();
    terminal.flush();
   }
  }
 }

void setup()
{
  // Debug console
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(1000L, myTimerEvent);  
}





void loop()
{  
  Blynk.run();
  timer.run(); // Initiates BlynkTimer  
}
