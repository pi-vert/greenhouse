import time
import sys
import os
import SendData
import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()
# sensor.SET_InterruptThreshold(0xff00, 0x0010)
lux = sensor.Lux
print('Lux: %d'%lux)
sensor.TSL2591_SET_LuxInterrupt(50, 200)
infrared = sensor.Read_Infrared
print('Infrared light: %d'%infrared)
visible = sensor.Read_Visible
print('Visible light: %d'%visible)
full_spectrum = sensor.Read_FullSpectrum
print('Full spectrum (IR + visible) light: %d\r\n'%full_spectrum)
sensor.Disable()

SendData.state('sensors/tsl2591', 'light/visible', visible)
SendData.state('sensors/tsl2591', 'light/infrared', infrared)
SendData.state('sensors/tsl2591', 'light/lux', lux)

