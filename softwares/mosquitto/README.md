# Mosquitto

## Installation

```shell
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key 
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-buster.list
sudo apt-get update 
sudo apt-get install mosquitto 
sudo apt-get install mosquitto-clients
```

_Correction pour tmpfs_

Edition du fichier /etc/systemd/system/multi-user.target.wants/mosquitto.service

```
[Service]
...
PermissionsStartOnly=true
ExecStartPre=-/bin/mkdir -p /var/log/mosquitto
ExecStartPre=-/bin/chown mosquitto:adm /var/log/mosquitto
ExecStartPre=-/bin/chmod 740 /var/log/mosquitto
...
```
