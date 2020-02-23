#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
buzzer = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.PWM(buzzer,GPIO.LOW)

p = GPIO.PWM(buzzer,50)
p.start(0)
try:
	while True:
		for dc in range(0,101,5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100,-1,-5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardImterrupt:
	pass
p.stop()
GPIO.cleanup()
