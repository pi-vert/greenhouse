#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time

address = 0x48

bus = smbus.SMBus(1)
while True:
	#for i in range(0,4):
	bus.write_byte(address,0x40)	
	value = bus.read_byte(address)
	print("AOUT:%1.3f  " %(value*3.3/255))
	time.sleep(0.1)


