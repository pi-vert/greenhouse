#include <wiringPi.h>
#include <stdio.h>

int main()
{
    unsigned char i;
    if (wiringPiSetup() < 0)return 1;
    for(i=0;i<5;i++)
    {
    	pinMode(i,INPUT);
   		pullUpDnControl(i,PUD_UP);
    }

    while (1)
    {
        for(i=0;i<5;i++)
		{
			if(digitalRead(i) == 0)        
            {
            	printf("press the key: %d\n", i);
            	delay(500);
            }
		}
    }
}
