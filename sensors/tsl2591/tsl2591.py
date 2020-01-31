import time
import sys
import os
import paho.mqtt.client as mqtt
import json

libdir = '/home/pi/greenhouse/sensors/tsl2591/lib'
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()
# sensor.SET_InterruptThreshold(0xff00, 0x0010)
lux = sensor.Lux
print('Lux: %d'%lux)
sensor.TSL2591_SET_LuxInterrupt(50, 200)
infrared = sensor.Read_Infrared
print('Infrared light: %d'%infrared)
visible = sensor.Read_Visible
print('Visible light: %d'%visible)
full_spectrum = sensor.Read_FullSpectrum
print('Full spectrum (IR + visible) light: %d\r\n'%full_spectrum)
sensor.Disable()

# Send to Mosquitto

sensor_data = {'light/visible': 0, 'light/infrared': 0, 'light/lux': 0}

client = mqtt.Client()
client.connect('localhost', 1883, 30)
client.loop_start()

sensor_data['light/visible'] = visible
sensor_data['light/infrared'] = infrared
sensor_data['light/lux'] = infrared
 
client.publish('sensors/tsl2591', json.dumps(sensor_data), 1)
client.loop_stop()
client.disconnect()

