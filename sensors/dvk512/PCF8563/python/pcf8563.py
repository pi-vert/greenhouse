#!/usr/bin/python
# -*- coding: utf-8 -*-
import smbus
import time

address = 0x51
register = 0x02
NowTime = [0x00,0x31,0x10,0x23,0x06,0x01,0x15]
w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"];
#/dev/i2c-1
bus = smbus.SMBus(1)
def pcf8563SetTime():
	bus.write_i2c_block_data(address,register,NowTime)

def pcf8563ReadTime():
	return bus.read_i2c_block_data(address,register,7);

pcf8563SetTime()
while 1:
	t = pcf8563ReadTime()
	t[0] = t[0]&0x7F  #sec
	t[1] = t[1]&0x7F  #min
	t[2] = t[2]&0x3F  #hour
	t[3] = t[3]&0x3F  #day
	t[4] = t[4]&0x07  #week
	t[5] = t[5]&0x1F  #mouth
	print("20%x/%x/%x %x:%x:%x  %s" %(t[6],t[4],t[3],t[2],t[1],t[0],w[t[5]]))
	time.sleep(1)
