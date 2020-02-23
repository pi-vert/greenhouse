#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

KEY = [17,18,27,22,23]

GPIO.setmode(GPIO.BCM)
for i in KEY:
	GPIO.setup(i,GPIO.IN,GPIO.PUD_UP)
while True:
	for i in range(0,5):
		time.sleep(0.05)
		if GPIO.input(KEY[i]) == 0:
			print("KEY %d PRESS" %i)
			while GPIO.input(KEY[i]) == 0:
				time.sleep(0.01)
