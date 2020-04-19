import pifacedigitalio
import time

pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object

pfd.leds[0].turn_on()
pfd.output_pins[0].value = 1
time.sleep(1)
pfd.output_pins[0].value = 0
pfd.leds[0].turn_off()

