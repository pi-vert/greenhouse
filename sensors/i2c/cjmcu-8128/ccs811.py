#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simpel example script for getting the data from the CCS811 module of a
CJMCU 8128 or 8118 breakout board.
"""

import sys
from Adafruit_CCS811 import Adafruit_CCS811

def ccs811example():
    """Main execution function for this scriptfile
    """
    c02, tvoc, temp = getdata()
    printdata(c02, tvoc, temp)


def getdata():
    """Get the data from the CCS811 sensor module and return it"""
    ccs = Adafruit_CCS811()
    temp = ccs.calculateTemperature()
    ccs.tempOffset = temp - 25.0
    if ccs.available():
        temp = ccs.calculateTemperature()
    if not ccs.readData():
        c02 = ccs.geteCO2()
        tvoc = ccs.getTVOC()
    else:
        print("Error reading data and getting values")
        sys.exit(-1)

    return c02, tvoc, temp

def printdata(c02, tvoc, temp):
    """Given the 3 main variables provided by the sensor it will print them out
    in a nicely formatted way
    """
    print('CO2: {1} ppm, TVOC: {2} Temp: {3}'.format(c02, tvoc, temp))

if __name__ == '__main__':
    ccs811example()
