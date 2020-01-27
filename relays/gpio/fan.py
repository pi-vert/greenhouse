##################################################

#           P26 ----> Relay_Ch1
#			P20 ----> Relay_Ch2
#			P21 ----> Relay_Ch3

##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

Relay = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)

print("Setup The Relay Module is [success]")

GPIO.output(Relay,GPIO.HIGH)
print("Channel 1:The Common Contact is access to the Normal Open Contact!")
		
