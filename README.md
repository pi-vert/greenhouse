# Serre automatisée v2

Le but de ce projet est d'obtenir des poivrons tout au long de l'année en fournissant automatiquement l'intégralité des besoins de la plante.

_Evolutions:_

La V1 était une maquette qui a permis d'identifier des erreurs plus ou moins flagrantes:
- Le montage électrique est installè à l'extérieur de la serre. Outre un problème évident de sécurité, l'avantage est de fournir plus d'espace aux plantes.
- L'utilisation de InfluxDB/Granfana en mode cloud épargne les ressources du raspberry et permet d'avoir un accès internet sans ouvrir son routeur
- Les relais dédiés 12V/220V simplifient le cablage en permettant une connexion directe des composants
- Les files des breadboards qui partent dans tous les sens vont être remplacés par des concentrateurs et/ou des multiplexeurs
- L'écran tactile est totalement inutile car trop petit et trop consommateur

## Montage

_En résumé:_
- Achat de l'aquarium 
- Montage du cadre en bois
- Cablage électrique
- Alimentation 12V
- Capteurs I2C
- Capteurs 1-Wire
- Remontées de données
- Pompe à eau
- Pompe à air
- Régulation thermique
- Eclairage
- Brumisateur
- Règles de gestion
- Circuit d'eau 
- Tableau de bord
- Alarmes

## Budget 

| Composant           | Prix | Référence   |
|-----------          |------|-----------  |
| Aquarium            |20    | Anibis      |
| Bois pour cadre     | 4,80 | Brico-coop  |
| Raspberry           |      | Microspot   |
| Capteur temperature |
| DVK512              |    0 | (optionnel) |
| Piface              |    0 | (optionnel) |
| Relai GPIO          | 
| Relai I2C           | 


## Technique
 
### Structure

La structure est en deux niveaux séparés par un cadre en bois contenant le système électrique. Le niveau bas est un aquarium pour assurer l'étanchéité et le niveau supérieur est en plexiglas pour un démontage facile.

[Plus d'infos sur la structure](docs/structureV2.md)

### Montage électrique

[Plus d'infos sur la partie électrique](docs/branchement.md)

## Capteurs

[Plus d'infos sur les capteurs](sensors/README.md)

## Raspberry
```
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
```

| GPIO | PinOut      | Utilisation |
| ---- | ----------- | ---------- |
|    1 | + 3.3V      |            |
|    2 | + 5V        |            |
|    3 | I2C (Data)  |            |
|    4 | + 5V        |            |
|    5 |             |            |
|    6 |             |            |
|    7 | GCLK        |            |
|    8 | UART TXD -->|            |
|    9 | - GND       |            |
|   10 | UART RXD <--|            |
|   11 |             |            |
|   12 | PWM0        |            |
|   13 |             |            |
|   14 |             |            |
|   15 |             |            |
|   16 |             |            |
|   17 | + 3.3V      |            |
|   18 |             |            |
|   19 | Relai GPIO  |            |
|   20 | Relai GPIO  |            |
|   21 | Relai GPIO  |            |
|   22 |             |            |
|   23 |             |            |
|   24 |             |            |
|   25 | - GND       |            |
|   26 | Relai GPIO  |            |
|------|-------------|------------|
|      | PIFACE      |            |
|------|-------------|------------|
|   27 | I2C/EEPROM  |            |
|   28 | I2C/EEPROM  |            |
|   29 |             |            |
|   30 |             |            |
|   31 |             |            |
|   32 | PWM0     -->|  WS2812    |
|   33 |             |            |
|   34 |             |            |
|   35 |             |            |
|   36 |             |            |
|   37 |             |            |
|   38 |             |            |
|   39 | - GND       |            |
|   40 |             |            |

## I2C

| Adresse | Description         |
| ------- | -----------         |
| 10      | Relai 12V           |            
| 29      | TSL                 |
| 51      | PCF8563/DVK512      |
| 76      | BME280              |

### Relais

[Plus d'infos sur les relais](relays/README.md)

### Logiciels

[Plus d'infos sur les logiciels](softwares/README.md)

## Botanique

[Plus d'infos sur les plantes](botanical/README.md)

