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
temperature = recupTemp (contenuFich)*1.035
print ("Temperature_Y: ", temperature)

SendData.state('sensors/ds18b20', 'temperature1', temperature)

contenuFich = lireFichier("/sys/bus/w1/devices/28-01191ae5edd9/w1_slave")
temperature = recupTemp (contenuFich)*1.035
print ("Temperature_G: ", temperature)

SendData.state('sensors/ds18b20', 'temperature1', temperature)

contenuFich = lireFichier("/sys/bus/w1/devices/28-011921255a5b/w1_slave")
temperature = recupTemp (contenuFich)*1.025
print ("Temperature_R: ", temperature)

SendData.state('sensors/ds18b20', 'temperature3', temperature)
