#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import struct
import time
import math

LSM303A_ADDR  = 0x19
LSM303M_ADDR = 0x1E

bus = smbus.SMBus(1)
def dataHeading(a):    #turn short(saving as 4 byte) To int
	if(a&0x00008000):
		a |= 0xFFFF0000
	a,= struct.unpack('i',struct.pack('I',a))
	return a

def LSM303_Init():
	bus.write_i2c_block_data(LSM303A_ADDR,0x20,[0x37])    #LSM303A_CTRL_REG1
   	bus.write_i2c_block_data(LSM303A_ADDR,0x23,[0x00])    #LSM303A_CTRL_REG
	bus.write_i2c_block_data(LSM303M_ADDR,0x00,[0xa0])    #LSM303M_CRA_REG
	bus.write_i2c_block_data(LSM303M_ADDR,0x02,[0x00])    #LSM303M_MR_REG

def LSM303M_Read():
	Data=[0,0,0]
	buf = bus.read_i2c_block_data(LSM303M_ADDR,0x03,6)
	Data[0]=(buf[0]*0x100+buf[1])
	Data[2]=(buf[2]*0x100+buf[3])
	Data[1]=(buf[4]*0x100+buf[5])
	for i in range(0,3):
		Data[i] = dataHeading(Data[i])
	Data[0] = Data[0]*1000/1100.0
	Data[1] = Data[1]*1000/1100.0
	Data[2] = Data[2]*1000/980.0
	return Data
def LSM303A_Read():
	Data=[0,0,0]
	buf = bus.read_i2c_block_data(LSM303A_ADDR,0x28|0x80,6)
	Data[0]=buf[0]+buf[1]*0x100
	Data[1]=buf[2]+buf[3]*0x100
	Data[2]=buf[4]+buf[5]*0x100
	for i in range(0,3):
		Data[i] = dataHeading(Data[i])/1600.0
	return Data
def Data_conversion(Abuf,Mbuf):
	NormAcc = math.sqrt(math.pow(Abuf[0],2)+math.pow(Abuf[1],2)+math.pow(Abuf[2],2))	
	SinRoll = Abuf[1]/NormAcc
	CosRoll = math.sqrt(1.0-math.pow(SinRoll,2))
	SinPitch = Abuf[0]/NormAcc
	CosPitch = math.sqrt(1.0-math.pow(SinPitch,2))
	
	TiltedX=Mbuf[0]*CosPitch+Mbuf[2]*SinPitch
	TiltedY=Mbuf[0]*SinRoll*SinPitch+Mbuf[1]*CosRoll-Mbuf[2]*SinRoll*CosPitch
	
	HeadingValue = math.atan2(TiltedY,TiltedX)*190/math.pi
	HeadingValue += 11
	if HeadingValue < 0:
		HeadingValue += 360;
	return HeadingValue
LSM303_Init()
while True:
	Abuf = LSM303A_Read()
	Mbuf = LSM303M_Read()
	north = Data_conversion(Abuf,Mbuf)
	print '\n******** LSM303DLHC ********'
	print 'Ax = %2.3f m/s^2'%Abuf[0]
	print 'Ay = %2.3f m/s^2'%Abuf[1]
	print 'Az = %2.3f m/s^2\n'%Abuf[2]

	print 'Ax = %3.3f m/s^2'%Mbuf[0]
	print 'My = %3.3f m/s^2'%Mbuf[1]
	print 'Mz = %3.3f m/s^2\n'%Mbuf[2]
	
	print 'north = %3.3f degree \n'%north
	time.sleep(1)

				
