import board
import busio
import tca9548a

# Multiplexer
address=0x70
plexer = tca9548a.multiplex(1)
plexer.channel(address,3)

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import SendData
ads = ADS.ADS1115(i2c)
P0 = AnalogIn(ads, ADS.P0)
#print ( chan.value, chan.voltage )
P1 = AnalogIn(ads, ADS.P1)
P2 = AnalogIn(ads, ADS.P2)
P3 = AnalogIn(ads, ADS.P3)

SendData.states('sensors/ads1115', { 'EC': P0.value, 'Po': P1.value, 'Do': P2.value, 'To': P3.value })
