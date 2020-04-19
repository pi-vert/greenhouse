import lcddriver
from time import *

def getValue(filename):
    f = open(filename)
    value = f.read()
    f.close()
    return value

lcd = lcddriver.lcd()

humidity = getValue("/home/pi/greenhouse/states/sensors/aht10/humidity.txt")
temperature = getValue("/home/pi/greenhouse/states/sensors/aht10/temperature.txt")

temperatureG = getValue("/home/pi/greenhouse/states/sensors/ds18b20/temperatureG.txt")
temperatureY = getValue("/home/pi/greenhouse/states/sensors/ds18b20/temperatureY.txt")
temperatureR = getValue("/home/pi/greenhouse/states/sensors/ds18b20/temperatureR.txt")

lcd.lcd_display_string("H: "+humidity+"% T: "+str(round(float(temperature),1))+chr(223), 1)
lcd.lcd_display_string(str(round(float(temperatureG),1))+chr(223)+str(round(float(temperatureY),1))+chr(223)+str(round(float(temperatureR),1))+chr(223),2)

#lcd.backlight(0)
 
