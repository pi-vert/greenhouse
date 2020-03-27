import os
import SendData

q =  round( float (os.popen("awk 'NR==3 {print $3 }' /proc/net/wireless").read().replace(' ','').replace('\n', '').replace('\r', '')) )
print(q)

SendData.mqtt("system", "wifi/quality", q)
SendData.influxDB("system", "wifi/quality", q)
