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
