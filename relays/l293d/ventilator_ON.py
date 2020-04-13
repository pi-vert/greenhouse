import RPi.GPIO as GPIO
import time
import SendData

Relay = 22 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.HIGH)

SendData.state('relays/l293d', 'ventilator', 1)
