import SendData
import os

ret = os.system('echo "rf e5 on" | nc -q 0 localhost 1099')
print(ret)
SendData.state('relays/x10', 'waterpump', 1)
