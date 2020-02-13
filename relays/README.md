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

## L293D

# Inverseur

Lorsque la puissance est trop élevée pour pouvoir utiliser un micro-contrôleur, on peut utiliser 2 relais et les cabler sur un principe proche du va et vient.
Chaque relai est indiqué comme suit:
```
____I____
a   b   c
---  \---
```
Ce qui signifie que les bornes a et b sont connectées lors de l'activation du relai. Le cablage du moteur sera le suivant:
```
      ____I____
      a   b   c
      ---  \---
      !   !   
 +  --+	  +---------+  +
                   (M)   
GND ----------------+  -
```
L'activation du relai démarre le moteur dans un sens, disons horaire, le schéma suivant va permettre d'ajouter le sens inverse en ajoutant un deuxième relai.
```
      ____I____      ____II___   
      a   b   c      a   b   c
      ---  \---      ---  \---
      !   !   !      !   !   !
 +  --+---)---)------)---)---+
          !   !      !   !
GND ------)---+------+   !
          !              !
          +-----(M)------+
```
## Cas possibles
Pour mieux comprendre l'utilisation des relais, on représente les 4 cas possibles:
```
| Relai I  | Relai II | Résultat            |
| -------- | -------- | --------            |
| OFF      | OFF      | Sens anti-horaire   |
```
      ____I____      ____II___   
      a   b   c      a   b   c
      ---  \---      ---  \---
          !   !          !   !
 +  ------)---)----------)---+
          !   !          !
GND ------)---+          !
          !    -   +     !
          +-----(M)------+
```
| Relai I  | Relai II | Résultat       |
| -------- | -------- | --------       |
| ON       | ON       | Sens horaire   |
```
      ____I____      ____II___   
      a   b   c      a   b   c
      ---/           ---/     
      !   !          !   !    
 +  --+   !          !   !    
          !          !   !
GND ------)----------+   !
          !    +   -     !
          +-----(M)------+
```
| Relai I  | Relai II | Résultat |
| -------- | -------- | -------- | 
| ON       | OFF      | STOP     |
```
      ____I____      ____II___   
      a   b   c      a   b   c
      ---/  ---      ---  \---
      !   !              !   !
 +  --+---)--------------)---+
          !              !
GND --    !              !
          !    +   +     !
          +-----(M)------+
```
| Relai I  | Relai II | Résultat |
| -------- | -------- | -------- |
| OFF      | ON       | STOP     |
```
      ____I____      ____II___   
      a   b   c      a   b   c
      ---  \---      ---/  ---
          !   !      !   !    
 +  --    !   !      !   !    
          !   !      !   !
GND ------)---+------+   !
          !    -   -     !
          +-----(M)------+
```