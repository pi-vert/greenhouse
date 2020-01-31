##################################################

#           P26 ----> Relay_Ch1
#			P20 ----> Relay_Ch2
#			P21 ----> Relay_Ch3

##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

Relay = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.LOW)

sensor_data = {'waterpump': 1}

client = mqtt.Client()
client.connect('localhost', 1883, 30)
client.loop_start()

client.publish('sensors/waterpump', json.dumps(sensor_data), 1)
client.loop_stop()
client.disconnect()

