import RPi.GPIO as GPIO
import time
import SendData

Relay = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay,GPIO.OUT)
GPIO.output(Relay,GPIO.LOW)

SendData.state('relays/gpio', 'heater', 0)
