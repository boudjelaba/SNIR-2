```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

t_v=np.linspace(0,1,200)
sin_v=np.sin(2*np.pi*10*t_v)
cos_v=1.5*np.cos(2*np.pi*10*t_v)

data=np.zeros((len(t_v),3))
data[:,0]=t_v
data[:,1]=sin_v
data[:,2]=cos_v

plt.figure()
plt.plot(t_v,sin_v)
plt.plot(t_v,cos_v)
plt.grid()
plt.show()

np.savetxt("sin_cos_latex.csv",data,delimiter=",",header="t,sin,cos",comments="")
```


```python
import picamera
with picamera.PiCamera() as camera:
     camera.start_preview()
     camera.capture('/home/pi/Images/photo.jpg')
     camera.stop_preview()
```



http://abyz.me.uk/rpi/pigpio/index.html

---

https://randomnerdtutorials.com/esp32-microsd-card-arduino/

https://microcontrollerslab.com/microsd-card-esp32-arduino-ide/

https://www.mischianti.org/2021/03/28/how-to-use-sd-card-with-esp32-2/

```cpp


#include <pigpio.h>
#include <unistd.h>

#define GPIO 14

int main(int argc, char *argv[])
{
       if (gpioInitialise() <0 ) {
             return -1;
       }

       gpioSetMode(GPIO , PI_OUTPUT);
       
       for(int compteur = 0; compteur < 60; compteur++) {
             gpioWrite(GPIO, 1);
             sleep(1);
             gpioWrite(GPIO, 0);
             sleep(1);
       }
       gpioTerminate();
}

```

```python
gcc -o progc progc.c -lpigpio -lrt -lpthread
```

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
