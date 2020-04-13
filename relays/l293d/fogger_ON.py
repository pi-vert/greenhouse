import RPi.GPIO as GPIO
import time
import SendData

Relay = 23 

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.HIGH)

SendData.state('relays/l293d', 'fogger', 1)
