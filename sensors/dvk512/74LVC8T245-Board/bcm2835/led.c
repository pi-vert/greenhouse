#include <bcm2835.h>

#define LED0 RPI_GPIO_P1_11
#define LED1 RPI_GPIO_P1_12
#define LED2 RPI_V2_GPIO_P1_13
#define LED3 RPI_GPIO_P1_15
#define LED4 RPI_GPIO_P1_16
#define LED5 RPI_GPIO_P1_18
#define LED6 RPI_GPIO_P1_22
#define LED7 RPI_GPIO_P1_07
char LED[8]={LED0,LED1,LED2,LED3,LED4,LED5,LED6,LED7};
int main(int argc, char **argv)
{
    if (!bcm2835_init())return 1;
    unsigned char i;
    while (1)
    {
		for(i=0;i<8;i++)
		{	
			bcm2835_gpio_fsel(LED[i], BCM2835_GPIO_FSEL_OUTP);
			bcm2835_gpio_write(LED[i],HIGH);
			bcm2835_delay(100);
			bcm2835_gpio_write(LED[i],LOW);
			bcm2835_delay(100);
		}
    }
    bcm2835_close();
    return 0;
}
