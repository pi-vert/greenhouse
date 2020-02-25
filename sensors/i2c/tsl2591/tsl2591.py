import time
import sys
import os

libdir = '/home/pi/greenhouse/sensors/i2c/tsl2591/lib'
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

def publish (sensor, measurement, value) :
    import paho.mqtt.client as mqtt
    import json
    client = mqtt.Client()
    client.connect('localhost', 1883, 30)
    client.loop_start()
    client.publish( sensor, json.dumps( {measurement: value }), 1)
    client.loop_stop()
    client.disconnect()
    return

def store (sensor, measurement, value) :
    from influxdb_client import InfluxDBClient, Point
    from influxdb_client.client.write_api import SYNCHRONOUS
    client = InfluxDBClient.from_config_file("/home/pi/influxdb.ini")
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    p = Point(measurement).tag("source", "vert").field(sensor, value)
    write_api.write(bucket="greenhouse", org="eric@angenault.net", record=p)
    return 

publish('sensors/tsl2591', 'light/visible', visible)
store('sensors/tsl2591', 'light/visible', visible)
publish('sensors/tsl2591', 'light/infrared', infrared)
store('sensors/tsl2591', 'light/infrared', infrared)
publish('sensors/tsl2591', 'light/lux', lux)
store('sensors/tsl2591', 'light/lux', lux)

