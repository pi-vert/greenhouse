# Relais

Les relais vont permettre de commander les différents composants de la serre:
* Pompes à eau et à air
* Ventilateurs
* Module peltier
* Brumisateurs

## GPIO

Ce type de relai est basique car déclenché par l'activation d'un signal. Il sert principalement à commander des appareils en 220V.
L'inconvénient du système est de consommer des GPIO alors que ceux-ci sont en quntité limitée sur le raspberry.

## I2C

Comme pour les capteurs, il est préférable d'utliser l'I2C afin de chaîner les composants et éviter les GPIO.

## SN754410

Ce processeur est un pont en H, il permet généralement de commander des moteurs dans les 2 sens. Il est très pratique pour un moteur de 5V qu'on voudrait faire tourner dans un sens ou dans l'autre, par exemple pour équilibrer la température et l'humidité avec l'extérieur.
L'ampérage est aux environs des 500mA, ce qui limite à une puissance de 6W pour du 12v.

