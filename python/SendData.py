USER_DIR='/home/pi'
STATES_DIR='/home/pi/greenhouse/states'

def mqtt (sensor, measurement, value) :
    import paho.mqtt.client as mqtt
    import json
    client = mqtt.Client()
    client.connect('localhost', 1883, 30)
    client.loop_start()
    client.publish( sensor, json.dumps( {measurement: value }), 1)
    client.loop_stop()
    client.disconnect()
    return

def influxDB (sensor, measurement, value) :
    from influxdb_client import InfluxDBClient, Point
    from influxdb_client.client.write_api import SYNCHRONOUS
    client = InfluxDBClient.from_config_file(USER_DIR + "/influxdb.ini")
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    p = Point(measurement).tag("source", "vert").field(sensor, value)
    write_api.write(bucket="greenhouse", org="eric@angenault.net", record=p)
    return 

def file (sensor, measurement, value) :
    f = open(STATES_DIR + '/' + sensor + '/' +  measurement + '.txt', "w")
    f.write( str(value) )
    f.close()   
 
def state (sensor, measurement, value) :
    mqtt (sensor, measurement, value)
    influxDB (sensor, measurement, value) 
    file (sensor, measurement, value)

