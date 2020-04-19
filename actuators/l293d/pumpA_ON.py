import RPi.GPIO as GPIO
import time
import SendData

Relay = 24 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.HIGH)

SendData.state('relays/l293d', 'pump A', 1)
