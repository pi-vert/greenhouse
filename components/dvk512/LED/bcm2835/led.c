/* blink.c
 * you can build this with something like:
 * gcc -Wall blink.c -o blink -lbcm2835
 * sudo ./blink
*/
#include <bcm2835.h>

char LED[] = {26,12,16,20};
unsigned char i;
int main(int argc, char **argv)
{
    if (!bcm2835_init())return 1;
	for(i = 0; i < 4; i++)
    {
		bcm2835_gpio_fsel(LED[i], BCM2835_GPIO_FSEL_OUTP);
	}

    while (1)
    {
        for(i = 0; i < 4; i++)
		{	
			bcm2835_gpio_write(LED[i], HIGH);
        	bcm2835_delay(500);
        	bcm2835_gpio_write(LED[i], LOW);
        	bcm2835_delay(500);
		}
    }
    bcm2835_close();
    return 0;
}
