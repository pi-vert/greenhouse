/* blink.c
 * you can build this like: 
 * gcc -Wall blink.c -o blink -lwiringPi
 * sudo ./flash
*/
#include<wiringPi.h>

char LED[]={25,26,27,28};
unsigned char i;

int main(void)
{
	wiringPiSetup();
	for(i=0;i<4;i++)
	{
		pinMode (LED[i],OUTPUT) ;
	}

	while(1)
	{
  		for(i=0;i<4;i++)
		{
  			digitalWrite (LED[i], 1) ;
    		delay (200);
  			digitalWrite (LED[i], 0) ;
    		delay (200);
  		}
	}
}
