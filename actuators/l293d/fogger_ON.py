import RPi.GPIO as GPIO
import time
import SendData

Relay = 27

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.HIGH)
GPIO.cleanup()

SendData.state('relays/l293d', 'fogger', 1)
