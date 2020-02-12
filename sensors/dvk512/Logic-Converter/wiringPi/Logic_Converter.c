/* Logic_Converter.c
 * you can build this like: 
 * gcc -Wall Logic_Converter.c -o Logic_Converter -lwiringPi
 * sudo ./Logic_Converter
*/
#include<stdio.h>
#include<wiringPi.h>

unsigned char KEY[]={7,6,5,4};
unsigned char LED[]={3,2,1,0};
unsigned char i;

int main()
{
	if(wiringPiSetup() < 0)return 1;
	for(i=0;i<4;i++)
	{
		pinMode (LED[i],OUTPUT);
		digitalWrite (LED[i],0);
		pinMode (KEY[i],INPUT) ;
		pullUpDnControl(KEY[i], PUD_UP);
	}
	
	while(1)
	{
  		for(i=0;i<4;i++)
		{
			if (digitalRead (KEY[i]) == 0)  
				digitalWrite (LED[i],1);
			else 
    			digitalWrite (LED[i],0);
  		}
		delay(10);

	}	
}
