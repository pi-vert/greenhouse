import spidev
import time

WHO_AM_I = 0x0F
CTRL_REG1 = 0x20
CTRL_REG2 = 0x21
CTRL_REG3 = 0x22
CTRL_REG4 = 0x23
CTRL_REG5 = 0x24
REFERENCE = 0x25
OUT_TEMP = 0x26
STATUS_REG = 0x27
OUT_X_L = 0x28
OUT_X_H = 0x29
OUT_Y_L = 0x2A
OUT_Y_H = 0x2B
OUT_Z_L = 0x2C
OUT_Z_H = 0x2D
FIFO_CTRL_REG = 0x2E
FIFO_SRC_REG  = 0x2F
INT1_CFG = 0x30
INT1_SRC = 0x31
INT1_TSH_XH = 0x32
INT1_TSH_XL = 0x33
INT1_TSH_YH = 0x34
INT1_TSH_YL = 0x35
INT1_TSH_ZH = 0x36
INT1_TSH_ZL = 0x37
INT1_DURATION = 0x38

bus = 0
device = 0
spi= spidev.SpiDev(bus,device)

def L3G4200D_write(add,data=[]):
	data = [add|0x40]+data
	spi.xfer(data)

def L3G4200D_read(add,n):
	data = [add|0xC0]+[0xFF]*n
	data = spi.xfer(data)
	data = data[1:]
	return data

def L3G4200D_init():
	L3G4200D_write(CTRL_REG1,[0xCF,0x01,0x08,0x00,0x02])

def read_L3G4200D():
	data = [0,0,0]
	buf = L3G4200D_read(CTRL_REG4,1)
	fs = buf[0] & 0x30
	if fs  == 0x00:
		Sensitivity = 8.75
	elif fs == 0x10:
		Sensitivity = 17.5
	elif fs == 0x20:
		sensitivity = 70
	else :
		sensitivity = 70
	buf = L3G4200D_read(OUT_X_L,6)
	data[0] = (buf[0] + buf[1] * 0x100)
	data[1] = (buf[2] + buf[3] * 0x100)
	data[2] = (buf[4] + buf[5] * 0x100)
	for i in range(0,3):
		if data[i] > 0x7FFF:
			data[i] -= 0x10000
		data[i] = data[i]*Sensitivity/1000
	return data

def data_int():
	buf = [0,0,0]
	for i in range(0,100):
		data = read_L3G4200D()
		time.sleep(0.01)
		buf[0] += data[0]
		buf[1] += data[1]
		buf[2] += data[2]
	for i in range(0,3):
		buf[i] = buf[i]/100
	print("%3.3f %3.3f %3.3f\n" %(buf[0],buf[1],buf[2]))
	return buf

print("****** L3G4200D ******")
L3G4200D_init()
bet = data_int() 

while True:
	data = read_L3G4200D()
	data[0] = (data[0]-bet[0])/100
	data[1] = (data[1]-bet[1])/100
	data[2] = (data[2]-bet[2])/100
	
	print("\nx=%.3f rad/s" %data[0]) 
	print("y=%.3f rad/s" %data[1])
	print("z=%.3f rad/s" %data[2])
	time.sleep(1)
