#include <bcm2835.h>
#include <stdio.h>

//key
#define KEY0 17
#define KEY1 18
#define KEY2 27
#define KEY3 22
#define KEY4 23
char KEY[]={KEY0,KEY1,KEY2,KEY3,KEY4};

int main(int argc, char **argv)
{
    unsigned char i;
    if (!bcm2835_init())return 1;
    for(i=0;i<5;i++)
    {
    	bcm2835_gpio_fsel(KEY[i], BCM2835_GPIO_FSEL_INPT);
    	bcm2835_gpio_set_pud(KEY[i], BCM2835_GPIO_PUD_UP);
    }

    while (1)
    {
        for(i=0;i<5;i++)
		{
			if(bcm2835_gpio_lev(KEY[i])==0)        
            {
            	printf("press the key: %d\n", i);
            	delay(500);
            }
		}
    }
	bcm2835_close();
    return 0;
}
