#include<stdio.h>
#include<bcm2835.h>

unsigned char KEY[]={4,25,24,23};
unsigned char LED[]={22,27,18,17};
unsigned char i;

int main()
{
	if(!bcm2835_init())return 1;
	for(i=0;i<4;i++)
	{
		bcm2835_gpio_fsel (LED[i],BCM2835_GPIO_FSEL_OUTP);
		bcm2835_gpio_write (LED[i],0);
		bcm2835_gpio_fsel(KEY[i],BCM2835_GPIO_FSEL_INPT) ;
		bcm2835_gpio_set_pud(KEY[i],BCM2835_GPIO_PUD_UP);
	}
	
	while(1)
	{
  		for(i=0;i<4;i++)
		{
			if (bcm2835_gpio_lev(KEY[i]) == 0)  
				bcm2835_gpio_write (LED[i],1);
			else 
    			bcm2835_gpio_write (LED[i],0);
  		}
		delay(10);

	}	
}
