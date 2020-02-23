#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

LED = [26,12,16,20]
GPIO.setmode(GPIO.BCM)
#define a easy way to set pin value
def ledWrite(pin,value):
	if value:
		GPIO.output(pin,GPIO.HIGH)
	else:
		GPIO.output(pin,GPIO.LOW)
for i in LED:
	GPIO.setup(i,GPIO.OUT)
	ledWrite(i,0)

try:
	while True:
		for i in LED:
			ledWrite(i,1)
			time.sleep(0.5)
			ledWrite(i,0)
			time.sleep(0.5)
except:
    print("except")
    GPIO.cleanup()
