https://www.engineersgarage.com/micropython-esp32-microsd-card/


```python
# import EAN13 from barcode module
from barcode import EAN13
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter
  
# Make sure to pass the number as string
number = '5901234123457'
  
# Now, let's create an object of EAN13 class and 
# pass the number with the ImageWriter() as the 
# writer
my_code = EAN13(number, writer=ImageWriter())
  
# Our barcode is ready. Let's save it.
my_code.save("new_code1")



```python
# Lecture du fichier et courbe
import csv

def lecture_Exo1(fichier, sep, n) : 
    file = open( fichier, "r")
    reader = csv.reader(file, delimiter = sep)
    col = []
    for row in reader:
        try:
            sep_decimal = row[n].replace(",", ".")
            col.append(float(sep_decimal))
        except:
            pass
    file.close()
    return col

# On récupère les deux dernières colonnes (2ème et 3ème) du fichier
x = lecture_Exo1("Exo1.csv", ",", 1)
y = lecture_Exo1("Exo1.csv", ",", 2)
print("Titre 2 = ", x)
print("Titre 3 = ", y)

# On trace la courbe demandée
import matplotlib.pyplot as plt
%matplotlib inline
plt.figure()
plt.plot(x, y, lw=2)

plt.ylabel('[A]')
plt.title('Courant')
plt.grid(True)
plt.show()

```

https://www.instructables.com/NEO-7M-U-BLOX-GPS-Module-Experiment/


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
