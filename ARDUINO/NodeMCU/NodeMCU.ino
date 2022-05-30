#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "tbgtBoJ8OJjkRfHszJhP8Pk4mbSOWMwn";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "alfii";
char pass[] = "alfiiiii";

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
    if (dataIn == 'w'){//Forward
      determinant = 'w';
    }
    else if (dataIn == 'g'){//Backward
      determinant = 'g';
    }
    else if (dataIn == 'y'){//Left
      determinant = 'y';
    }
    else if (dataIn == 'o'){//Right
      determinant = 'o';
    }
    else if (dataIn == 'r'){//Froward Right
      determinant = 'r';
    }
    else if (dataIn == 'm'){//Froward Right
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
    case 'w': // F, move forward
    led1.on();
    Blynk.setProperty(V1, "color", "#FFFFFF");
    terminal.println("No rain fall");
    det = check();
    break;
   //------- 

    case 'g': // B, move back
    led1.on();
    Blynk.setProperty(V1, "color", "#02A108");
    terminal.println("Normal rain fall");
    det = check();
    break;

    case 'y': // B, move back
    led1.on();
    Blynk.setProperty(V1, "color", "#F9FF00");
    terminal.println("Be aware");
    det = check();
    break;

    case 'o': // B, move back
    led1.on();
    Blynk.setProperty(V1, "color", "#F3631C");
    terminal.println("Take precaution, flood chance");
    det = check();
    break;

    case 'r': // B, move back
    led1.on();
    Blynk.setProperty(V1, "color", "#FF0004");
    terminal.println("Landslide chance, evacuate");
    det = check();
    break;

    case 'm': // B, move back
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
  // You can also specify server:
  //Blynk.begin(auth, ssid, pass, "blynk-cloud.com", 8442);
  //Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,100), 8442);
}





void loop()
{  
  Blynk.run();
  timer.run(); // Initiates BlynkTimer  
}
