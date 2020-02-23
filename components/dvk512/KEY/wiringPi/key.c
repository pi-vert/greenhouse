/* key.c
 * you can build this like: 
 * gcc -Wall key.c -o key -lwiringPi
 * sudo ./key
*/
#include <stdio.h>
#include <string.h> 
#include <errno.h>

#include<wiringPi.h>


char KEY[]={21,22,23,24};
unsigned char i;

int main(){
	if (wiringPiSetup() < 0)return 1 ;
	for(i=0;i<4;i++)
	{
		pinMode (KEY[i],INPUT) ;//pinMode (LED, OUTPUT) ;
		pullUpDnControl(KEY[i], PUD_UP);
	}

	while(1)
	{
 		for(i=0;i<4;i++)
		{
			if (digitalRead (KEY[i]) == 0)  
    			{
				printf ("press the key : %d\n",i) ;
    			delay(500);
			}
  		}
	}
}
