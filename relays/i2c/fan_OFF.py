import time as t
import smbus
import sys

DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)

bus.write_byte_data(DEVICE_ADDR, 1, 0x00)
