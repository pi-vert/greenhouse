# -*- coding: utf-8 -*-
import smbus
import time
import SendData
import tca9548a

# Get I2C bus
bus = smbus.SMBus(1)

# Multiplexer
address=0x70
plexer = tca9548a.multiplex(1)
plexer.channel(address,1)

config = [0x08, 0x00]
bus.write_i2c_block_data(0x38, 0xE1, config)

time.sleep(0.5)
byt = bus.read_byte(0x38)

#print(byt&0x68)
MeasureCmd = [0x33, 0x00]
bus.write_i2c_block_data(0x38, 0xAC, MeasureCmd)

time.sleep(0.5)
data = bus.read_i2c_block_data(0x38,0x00)

temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
ctemp = ((temp*200) / 1048576) - 50

print(u'Temperature: {0:.1f}C'.format(ctemp))
tmp = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4

humidity = int(tmp * 100 / 1048576)
print(u'Humidity: {0}%'.format(humidity))

SendData.states("sensors/aht10",{ "temperature": ctemp, "humidity": humidity })

