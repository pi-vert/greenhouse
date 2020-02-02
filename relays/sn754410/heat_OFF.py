##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.LOW)

sensor_data = {'fan/bottom': 1}

client = mqtt.Client()
client.connect('localhost', 1883, 30)
client.loop_start()

client.publish('sensors/fan', json.dumps(sensor_data), 1)
client.loop_stop()
client.disconnect()

