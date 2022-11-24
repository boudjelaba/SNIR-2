https://randomnerdtutorials.com/esp32-microsd-card-arduino/

https://microcontrollerslab.com/microsd-card-esp32-arduino-ide/

https://www.mischianti.org/2021/03/28/how-to-use-sd-card-with-esp32-2/

## Code TP5


```cpp

#include <WiFi.h>

const char* ssid = "NomDuRéseau";
const char* password = "MotDePasse";

// Port 80
WiFiServer server(80);

// Variable pour sauvegarder la requête HTTP
String header;

String output26State = "off";
String output27State = "off";

const int output26 = 26;
const int output27 = 27;

unsigned long currentTime = millis();
unsigned long previousTime = 0;
const long timeoutTime = 2000;

void setup() {
  Serial.begin(115200);
  pinMode(output26, OUTPUT);
  pinMode(output27, OUTPUT);
  digitalWrite(output26, LOW);
  digitalWrite(output27, LOW);

  // Connexion au réseau Wi-Fi
  Serial.print("Connecté au réseau ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Affichage de l'adresse IP et démarrage du serveur web
  Serial.println("");
  Serial.println("Connecté en WiFi.");
  Serial.println("Adresse IP : ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();  // Ecoute les clients entrants

  if (client) {  // Si un nouveau client se connecte,
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("Nouveau Client.");
    String currentLine = "";
    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        header += c;
        //header += c;
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Type de contenu : text/html");
            client.println("Connexion : fermée");
            client.println();

            if (header.indexOf("GET /26/on") >= 0) {
              Serial.println("GPIO 26 on");
              output26State = "on";
              digitalWrite(output26, HIGH);
            } else if (header.indexOf("GET /26/off") >= 0) {
              Serial.println("GPIO 26 off");
              output26State = "off";
              digitalWrite(output26, LOW);
            } else if (header.indexOf("GET /27/on") >= 0) {
              Serial.println("GPIO 27 on");
              output27State = "on";
              digitalWrite(output27, HIGH);
            } else if (header.indexOf("GET /27/off") >= 0) {
              Serial.println("GPIO 27 off");
              output27State = "off";
              digitalWrite(output27, LOW);
            }

            // Affichage de la page HTML
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, 
            			initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            // CSS : boutons on/off
            client.println("<style>html { font-family: Helvetica; display: inline-block; 
            			margin: 0px auto; text-align: center;}");
            client.println(".button { background-color: #4CAF50; border: none; 
            			color: white; padding: 16px 40px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; 
            			cursor: pointer;}");
            client.println(".button2 {background-color: #555555;}</style></head>");

            // En-tête page Web
            client.println("<body><h1>ESP32 Web Server</h1>");

            // Affichage de l'état actuel et les boutons ON/OFF pour GPIO 26
            client.println("<p>GPIO 26 - State " + output26State + "</p>");
            // Si output26State est éteint, il affiche le bouton ON
            if (output26State == "off") {
              client.println("<p><a href=\"/26/on\"><button class=\"button\">
              			ON</button></a></p>");
            } else {
              client.println("<p><a href=\"/26/off\"><button class=\"button button2\">
              			OFF</button></a></p>");
            }

            // Affichage de l'état actuel et les boutons ON/OFF pour GPIO 27
            client.println("<p>GPIO 27 - State " + output27State + "</p>");
            // Si output27State est éteint, il affiche le bouton ON
            if (output27State == "off") {
              client.println("<p><a href=\"/27/on\"><button class=\"button\">
              			ON</button></a></p>");
            } else {
              client.println("<p><a href=\"/27/off\"><button class=\"button button2\">
              			OFF</button></a></p>");
            }
            client.println("</body></html>");
            //client.println("</body></html>");

            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    // Effacer la variable d'en-tête	
    header = "";
    // Fermer la connexion
    client.stop();
    Serial.println("Client déconnecté.");																						
    Serial.println("");
  }
}
```

---

## Code TP8

```cpp
#include <WiFi.h>
#include <Servo.h>

Servo myservo;

static const int servoPin = 13;

const char* ssid = "NomDuRéseau";
const char* password = "MotDePasse";

WiFiServer server(80);

String header;

String valueString = String(5);
int pos1 = 0;
int pos2 = 0;

unsigned long currentTime = millis();
unsigned long previousTime = 0;
const long timeoutTime = 2000;

void setup() {
  Serial.begin(115200);

  myservo.attach(servoPin);

  Serial.print("Connecté au réseau ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Connecté au WiFi.");
  Serial.println("Adresse IP : ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {  
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("New Client.");
    String currentLine = "";
    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        header += c;
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Type de contenu :text/html");
            client.println("Connexion: fermée");
            client.println();

            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, 
            			initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            client.println("<style>body { text-align: center; font-family: \"Trebuchet MS\", 
            			Arial; margin-left:auto; margin-right:auto;}");
            //client.println("<style>body { text-align: center; font-family: \"Trebuchet MS\", 
            //			Arial; margin-left:auto; margin-right:auto;}");
            client.println(".slider { width: 300px; }</style>");
            client.println("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/
            			3.3.1/jquery.min.js\"></script>");

            client.println("</head><body><h1>ESP32 with Servo</h1>");
            client.println("<p>Position: <span id=\"servoPos\"></span></p>");
            client.println("<input type=\"range\" min=\"0\" max=\"180\" 
            			class=\"slider\" id=\"servoSlider\" onchange=\"servo(this.value)\" 
				value=\"" + valueString + "\"/>");

            client.println("<script>var slider = document.getElementById(\"servoSlider\");");
            client.println("var servoP = document.getElementById(\"servoPos\"); 
            			servoP.innerHTML = slider.value;");
            client.println("slider.oninput = function() { slider.value = this.value; 
            						servoP.innerHTML = this.value; }");
            client.println("$.ajaxSetup({timeout:1000}); function servo(pos) { ");
            client.println("$.get(\"/?value=\" + pos + \"&\"); {Connection: close};}</script>");

            client.println("</body></html>");

            if (header.indexOf("GET /?value=") >= 0) {
              pos1 = header.indexOf('=');
              pos2 = header.indexOf('&');
              valueString = header.substring(pos1 + 1, pos2);

              //Rotation servo
              myservo.write(valueString.toInt());
              Serial.println(valueString);
            }
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    header = "";
    client.stop();
    Serial.println("Client déconnecté.");
    Serial.println("");
  }
}

```


# SNIR-2

---
## QT Creator

https://www.youtube.com/watch?v=LGDNkMNYXus&list=PL5DhqvQVfsYXt_DAs07lZm6g0ASux6Q5l

---

## Code::Blocks

https://www.youtube.com/watch?v=cHGIIp3rGO8

https://www.youtube.com/watch?v=rpipDcG8GMg

https://www.youtube.com/watch?v=L_0ila8gzpI

---
