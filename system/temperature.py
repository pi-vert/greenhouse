import SendData

def get_cpu_temperature():
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())
    return temp/1000

temperature = get_cpu_temperature()
print(temperature)

SendData.mqtt("system", "cpu/temperature", temperature)
SendData.influxDB("system", "cpu/temperature", temperature)

