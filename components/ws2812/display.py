import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.01, auto_write=False)

def getPixel(x,y):
    if (x % 2):
        p = 255 - ((x+1)*8) + y +1
    else: 
        p = 255 - (x*8) - y  
    return p

def clear():
    pixels.fill((0, 0, 0))

matrix = [
[ 0, 1, 1, 1, 1, 1, 1, 0, 
  1, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 1,
  0, 1, 1, 1, 1, 1, 1, 0
], #1
[ 0, 0, 0, 0, 0, 1, 0, 0,
  0, 1, 0, 0, 0, 0, 0, 1,
  1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 0, 0, 0, 0, 1,
  0, 0, 0, 0, 0, 0, 0, 0
], #2
[ 1, 1, 0, 0, 0, 0, 1, 0,
  1, 0, 0, 0, 0, 1, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 1, 1, 0
], #3
[ 0, 1, 0, 0, 0, 0, 1, 0,
  1, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 0, 0, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  0, 1, 1, 1, 0, 1, 1, 0
], #4
[ 0, 0, 0, 1, 1, 0, 0, 0, 
  0, 0, 1, 0, 1, 0, 0, 0,
  0, 0, 0, 1, 0, 0, 1, 0,
  1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 1, 0, 0, 0, 0
], #5
[ 0, 1, 0, 0, 0, 1, 1, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 0, 1, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  0, 1, 1, 1, 0, 0, 0, 1
], #6
[ 0, 1, 1, 1, 1, 1, 1, 0,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 0, 1, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  0, 1, 1, 1, 0, 0, 1, 0
], #7
[ 0, 0, 0, 0, 0, 0, 1, 0,
  1, 0, 0, 0, 1, 1, 1, 1,
  0, 0, 0, 0, 1, 0, 0, 1,
  1, 0, 1, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 1, 1
], #8
[  0, 1, 1, 1, 0, 1, 1, 0,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 0, 1, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  0, 1, 1, 1, 0, 1, 1, 0
], #9
[ 0, 0, 0, 0, 0, 1, 1, 0,
  1, 0, 0, 1, 0, 0, 0, 1,
  1, 0, 0, 0, 1, 0, 0, 1,
  1, 0, 0, 1, 0, 0, 0, 1,
  0, 1, 1, 1, 1, 1, 1, 0
], #%
[ 0, 1, 0, 0, 0, 1, 1, 0,
  0, 1, 1, 0, 0, 1, 0, 0,
  0, 0, 0, 1, 0, 0, 0, 0,
  0, 0, 0, 1, 0, 0, 1, 1,
  1, 1, 0, 0, 0, 1, 0, 0
]
]

def Letter(l,p,color):
    for i in range(40):
        if (matrix[l][i]):
            pixels[255-(p*48)-i] =  color

dir = "/home/pi/greenhouse/states/sensors/bme280/1"

def getValue(filename):
    f = open(dir + "/" + filename)
    value = f.read()
    f.close()
    return value

def putValue(filename,value):
    f = open(dir + "/" + filename , "w")
    f.write(value)
    f.close()

clear()
humidity = getValue("humidity.txt");
last = getValue("humidity.cache");
if (humidity<last):
    color=(255,0,0)
elif (humidity>last):
    color=(0,255,0)
else:
    color=(255,255,0)
putValue("humidity.cache",humidity)

Letter(int(humidity[0]),0,color)
Letter(int(humidity[1]),1,color)
if (humidity[0]==100):
    Letter(0,2,color)    
else:
    Letter(10,2,color)

temperature = getValue("temperature.txt");
last = getValue("temperature.cache");
if (temperature<last):
    color=(255,0,0)
elif (temperature>last):
    color=(0,255,0)
else:
    color=(255,255,0)
putValue("temperature.cache",temperature)

color=(0,255,0)
Letter(int(temperature[0]),3,color)
Letter(int(temperature[1]),4,color)

pixels[5] = (color)
pixels[6] = (color)
pixels[10] = (color)
pixels[9] = (color)
pixels.show()

