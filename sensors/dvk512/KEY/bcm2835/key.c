/* key.c
 * you can build this like: 
 * gcc -Wall key.c -o key -lbcm2835
 * sudo ./key
*/
#include <bcm2835.h>
#include <stdio.h>

char KEY[] = {5,6,13,19};
unsigned char i;
int main(int argc, char **argv)
{
	if (!bcm2835_init())return 1;
	for(i=0;i<4;i++)
	{
		bcm2835_gpio_fsel(KEY[i], BCM2835_GPIO_FSEL_INPT);
		bcm2835_gpio_set_pud(KEY[i], BCM2835_GPIO_PUD_UP);
	}
	
	while (1)
	{
		for(i=0;i<4;i++)
		{
			if(bcm2835_gpio_lev (KEY[i]) == 0)  
    			{
				printf ("press the key : %d\n",i) ;
    			delay(500);
			}
  		}
	}
	bcm2835_close();
	return 0;
}
