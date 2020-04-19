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

ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

import SendData
SendData.state('sensors/ads1115', 'tdsmeter', chan.value)
print ( chan.value, chan.voltage )
