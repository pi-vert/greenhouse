# PCF8591

Ce convertisseur analogique <-> numérique embarque 3 capteurs qu'on peut désctiver en otant les jumpers.

| Canal | Utilisation |
| ----- | ----------- |
| 0     | Entrée analogique |
| 1     | 
| 2     |
| 3     |
| 4     | Sortie analogique (LED) |

Le photoresistor est utilisé pour connaitre la luminosité à l'extérieur de la serre, on n'a pas vraiment besoin de connaître la valeur car on ne s'en servira que comme interrupteur pour les leds agricoles. 

Par contre, le tsl à l'intérieur de la serre devra nous donner des valeurs plus précises afin de connaître les niveaux de lumière apporté aux plantes.

On n'utilisera évidemment pas la led embarquée car elle fausserait les valeurs du photoresistor.

