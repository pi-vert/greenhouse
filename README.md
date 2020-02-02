# Serre automatisée

Le but de ce projet est d'obtenir des poivrons tout au long de l'année en fournissant automatiquement l'intégralité des besoins de la plante.

## Base
 
### Structure

La structure est en deux niveaux séparés par un cadre en bois contenant le système électrique. Le niveau bas est un aquarium pour assurere l'étanchéité et le niveau supérieur est en plexiglas pour un démontage facile.

[Plus d'infos sur la structure](docs/structure.md)

### Montage électrique

[Plus d'infos sur la partie électrique](docs/branchement.md)

## Capteurs

[Plus d'infos sur les capteurs](sensors/README.md)

## Raspberry

             3V |  | 1 --(o o)-- 2 |  | 5V 
            I2C | 2| 3 --(o o)-- 4 |  | 5V
            I2C | 3| 5 --(o o)-- 6 |  | GND
      GPIO_GCLK | 4| 7 --(o o)-- 8 |14| UART Tx
            GND |  | 9 --(o o)--10 |15| UART Rx
      GPIO_GEN0 |17|11 --(o o)--12 |18| GPIO_GEN1
      GPIO_GEN2 |27|13 --(o o)--14 |  | GND
      GPIO_GEN3 |22|15 --(o o)--16 |23| GPIO_GEN4
             3V |  |17 --(o o)--18 |24| GPIO_GEN5
      SPID_MOSI |10|19 --(o o)--20 |  | GND
      SPIO_MISO | 9|21 --(o o)--22 |25| GPIO_GEN6
      SPIO_CLK  |11|23 --(o o)--24 | 8| SPI_CEO_N
            GND |  |25 --(o o)--26 | 7| SPI_CE1_N 
      I2C EEPROM|  |27 --(o o)--28 |  | I2C EEPROM
                | 5|29 --(o o)--30 |  | GND
                | 6|31 --(o o)--32 |12| 
                |13|33 --(o o)--34 |  | GND 
                |19|35 --(o o)--36 |16|
                |26|37 --(o o)--38 |20| GND
            GND |  |39 --(o o)--40 |21| GND
 

GPIO | Utilisation
---- | -----------
   2 | I2C
   3 | I2C
   5 | Aération bas de serre
   6 | Aération haut de serre
  12 | Plus chaud
  13 | Plus froid 
  19 | Relai
  20 | Relai
  21 | Relai
  26 | Relai
 



### Relais

[Plus d'infos sur les relais](relays/README.md)

### Logiciels

[Plus d'infos sur les logiciels](softwares/README.md)

## Botanique

[Plus d'infos sur les plantes](botanical/README.md)

