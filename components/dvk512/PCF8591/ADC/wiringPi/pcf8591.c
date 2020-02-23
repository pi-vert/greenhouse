#include <wiringPi.h>
#include <pcf8591.h>
#include <stdio.h>

#define Address 0x48
#define BASE 64
#define A0 BASE+0
#define A1 BASE+1
#define A2 BASE+2
#define A3 BASE+3

int main(void)
{
	int value,i;
	wiringPiSetup();
	pcf8591Setup(BASE,Address);

	while(1)
	{
		for(i = 0;i < 4;i++)
		{
			value = analogRead(BASE+i);
			printf("AIN%d:%5.2f   ",i,(double)value*3.3/255);
		}
		printf("\n");
		delay(1000);
	}

}
