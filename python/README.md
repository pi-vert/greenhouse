# Python

Bon à savoir:
- Tous les scripts sont en Python3
- Les modules sont dans /home/pi/greenhouse/python
- donc, ne pas oublier de mettre quelque part: export PYTHONPATH=/home/pi/greenhouse/python 

crontab
PYTHONPATH=/home/pi/greenhouse/python

* *  * * * python3 /home/pi/greenhouse/system/temperature.py
* *  * * * python3 /home/pi/greenhouse/system/wifi.py

/etc/profile
PYTHONPATH=/home/pi/greenhouse/python
export PYTHONPATH

## Rest API

Imaginons des web services en RestApi accessible par un magifique swagger...

On peut tout imaginer quand on a un peu de temps mais pour le moment on va se contenter d'un script en Python flasque qui se contente du script minimum.

python3 /home/pi/greenhouse/python/rest/a.py

