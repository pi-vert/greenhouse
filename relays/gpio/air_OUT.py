##################################################

#           P26 ----> Relay_Ch1
#			P20 ----> Relay_Ch2
#			P21 ----> Relay_Ch3

##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import paho.mqtt.client as mqtt
import json

Relay1= 19
Relay2= 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay1,GPIO.OUT)
GPIO.setup(Relay2,GPIO.OUT)

GPIO.output(Relay1,GPIO.LOW)
GPIO.output(Relay2,GPIO.LOW)

sensor_data = {'air': 1}

client = mqtt.Client()
client.connect('localhost', 1883, 30)
client.loop_start()

client.publish('sensors/light', json.dumps(sensor_data), 1)
client.loop_stop()
client.disconnect()

