`cpp
#include <csignal>
#include <iostream>
#include <pigpio.h>

const int RedLED = 21;
volatile sig_atomic_t signal_received = 0;

void sigint_handler(int signal) {
   signal_received = signal;
}

int main() {
   if (gpioInitialise() == PI_INIT_FAILED) {
      std::cout << "ERROR: Failed to initialize the GPIO interface." << std::endl;
      return 1;
   }
   gpioSetMode(RedLED, PI_OUTPUT);
   signal(SIGINT, sigint_handler);
   std::cout << "Press CTRL-C to exit." << std::endl;
   while (!signal_received) {
      gpioWrite(RedLED, PI_HIGH);
      time_sleep(1);
      gpioWrite(RedLED, PI_LOW);
      time_sleep(1);
   }
   gpioSetMode(RedLED, PI_INPUT);
   gpioTerminate();
   std::cout << std::endl;
   return 0;
}
`

---
---



## XBEE

https://www.youtube.com/watch?v=a6W4kspM6NQ

https://www.youtube.com/watch?v=C6qsuudji_E

https://www.youtube.com/watch?v=sq9Twvs6N-0

___
## UML :

https://www.youtube.com/watch?v=m_MQYyJpIjg

---

https://www.youtube.com/watch?v=UI6lqHOVHic

https://www.youtube.com/watch?v=WnMQ8HlmeXc

---
---

https://www.engineersgarage.com/micropython-esp32-microsd-card/

---

# SNIR 2

---
## QT Creator

https://www.youtube.com/watch?v=LGDNkMNYXus&list=PL5DhqvQVfsYXt_DAs07lZm6g0ASux6Q5l

---

## Code::Blocks

https://www.youtube.com/watch?v=cHGIIp3rGO8

https://www.youtube.com/watch?v=rpipDcG8GMg

https://www.youtube.com/watch?v=L_0ila8gzpI

---
