export PYTHONPATH=$PYTHONPATH:~/greenhouse/python 
python3 ~/greenhouse/relays/i2c/sink_ON.py
sleep 30
python3 ~/greenhouse/relays/i2c/sink_OFF.py
