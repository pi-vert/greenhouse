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

addresse = 0x48 # adresse i2c du module PCF8691
entree = 0x42  # utiliser 0x40 pour A0, 0x41 pour A1, 0x42 pour A2 et 0x43 pour A3

bus = smbus.SMBus(1) # définition du bus i2c (parfois 0 ou 2)

while True:
    bus.write_byte(addresse,entree) # directive: lire l'entrée A0
    value = bus.read_byte(addresse) # lecture du résultat
    print("Lecture: %1.2f V" %(value*3.3/255)) # transformation en volts et affichage a l'écran
    time.sleep(0.5) # délai avant la prochaine mesure
