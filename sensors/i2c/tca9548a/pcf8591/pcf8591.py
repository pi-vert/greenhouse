#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Lecture de l'entrée analogique A0 d'un module
PCF8591 branché au Raspberry Pi.
Plus d'infos:
https://electroniqueamateur.blogspot.com/2019/01/pcf8591-et-raspberry-pi.html
'''

import smbus  # nécessaire pour la communication i2c
import time   # nécessaire pour le délai
import paho.mqtt.client as mqtt
import json
import tca9548a
import SendData

# Multiplexer
address=0x70
plexer = tca9548a.multiplex(1)
plexer.channel(address,0)

addresse = 0x48 # adresse i2c du module PCF8691

bus = smbus.SMBus(1) # définition du bus i2c (parfois 0 ou 2)

# utiliser 0x40 pour A0, 0x41 pour A1, 0x42 pour A2 et 0x43 pour A3
bus.write_byte(addresse,0x41)
value = bus.read_byte(addresse)
print("Potentiometer: %3d" %(value))
SendData.state('sensors/pcf8591', 'analog', value)

bus.write_byte(addresse,0x40)
value = bus.read_byte(addresse)
print("Analog: %3d" %(value))
SendData.state('sensors/pcf8591', 'analog', value)

bus.write_byte(addresse,0x42)
value = bus.read_byte(addresse)
print("Photoresistor: %3d" %(value))
SendData.state('sensors/pcf8591', 'photoresistor', value)

bus.write_byte(addresse,0x43)
value = bus.read_byte(addresse)
print("Thermistor: %3d" %(value))
SendData.state('sensors/pcf8591', 'thermistor', value)


