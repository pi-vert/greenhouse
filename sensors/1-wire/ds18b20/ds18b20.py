import sys
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

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

def publish (sensor, measurement, value) :
    import paho.mqtt.client as mqtt
    import json
    client = mqtt.Client()
    client.connect('localhost', 1883, 30)
    client.loop_start()
    client.publish( sensor, json.dumps( {measurement: value }), 1)
    client.loop_stop()
    client.disconnect()
    return

def store (sensor, measurement, value) :
    from influxdb_client import InfluxDBClient, Point
    from influxdb_client.client.write_api import SYNCHRONOUS
    client = InfluxDBClient.from_config_file("/home/pi/influxdb.ini")
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    p = Point(measurement).tag("source", "vert").field(sensor, value)
    write_api.write(bucket="greenhouse", org="eric@angenault.net", record=p)
    return 

contenuFich = lireFichier("/sys/bus/w1/devices/28-01192108919d/w1_slave")
temperature = recupTemp (contenuFich)
print ("Temperature: ", temperature)

publish('sensors/ds18b20/1', 'temperature', temperature)
store('sensors/ds18b20/1', 'temperature', temperature)
 
