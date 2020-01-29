import sys
import paho.mqtt.client as mqtt
import json

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

contenuFich1 = lireFichier("/sys/bus/w1/devices/28-01192108919d/w1_slave")
contenuFich2 = lireFichier("/sys/bus/w1/devices/28-0000061e147a/w1_slave")

temperature1 = recupTemp (contenuFich1)
temperature2 = recupTemp (contenuFich2)

print "Temperature Capteur EAU: " ,
print temperature1
print "Temperature Capteur AIR: " ,
print temperature2

# Send to Mosquitto

sensor_data = {'temperature/air': 0, 'temperature/eau': 0}

client = mqtt.Client()
client.connect('localhost', 1883, 30)
client.loop_start()

sensor_data['temperature/air'] = temperature1
sensor_data['pressure/eau'] = temperature2

client.publish('sensors/ds18b20', json.dumps(sensor_data), 1)
client.loop_stop()
client.disconnect()

