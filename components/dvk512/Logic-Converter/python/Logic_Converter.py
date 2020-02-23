#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

LED = [17,18,27,22]
KEY = [23,24,25,4]
GPIO.setmode(GPIO.BCM)
for i in range(0,4):
	GPIO.setup(KEY[i],GPIO.IN,GPIO.PUD_UP)

for i in range(0,4):
	GPIO.setup(LED[i],GPIO.OUT)
	GPIO.output(LED[i],GPIO.LOW)

try:
	while True:
		for i in range(0,4):
			if GPIO.input(KEY[i]) == 0:
				GPIO.output(LED[i],GPIO.HIGH)
			else:
				GPIO.output(LED[i],GPIO.LOW)
			time.sleep(0.05)
except:
    print("except")
    GPIO.cleanup()

