import sys
import SendData

def lireFichier (emplacement) :
    fichTemp = open(emplacement)
    contenu = fichTemp.read()
    fichTemp.close()
    return contenu

def recupTemp (contenuFich) :
    secondeLigne = contenuFich.split("\n")[1]
    temperatureData = secondeLigne.split(" ")[9]
    temperature = float(temperatureData[2:])
    temperature = temperature / 1000
    return temperature

contenuFich = lireFichier("/sys/bus/w1/devices/28-0119113a3b60/w1_slave")
temperatureY = recupTemp (contenuFich)*1.035
print ("Temperature_Y: ", temperatureY)

SendData.state('sensors/ds18b20', 'temperatureY', temperatureY)

contenuFich = lireFichier("/sys/bus/w1/devices/28-01191ae5edd9/w1_slave")
temperatureG = recupTemp (contenuFich)*1.035
print ("Temperature_G: ", temperatureG)

SendData.state('sensors/ds18b20', 'temperatureG', temperatureG)

contenuFich = lireFichier("/sys/bus/w1/devices/28-011921255a5b/w1_slave")
temperatureR = recupTemp (contenuFich)*1.025
print ("Temperature_R: ", temperatureR)

SendData.state('sensors/ds18b20', 'temperatureR', temperatureR)

