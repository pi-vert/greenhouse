#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print GPIO.input(4)
