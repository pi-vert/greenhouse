#include <wiringPi.h>  
#include <wiringPiI2C.h>
#include <stdio.h>

#define SEC    0x02  
#define MIN    0x03 
#define HOUR   0x04 
#define DAY    0x05 
#define WEEK   0x06 
#define MONTH  0x07 
#define YEAR   0x08 

#define PCF8563_Address 0x51
#define reg 0x02
//seconds,minutes,hours,days,weekdays,months,yeas
char  buf[]={0x00,0x47,0x11,0x19,0x05,0x06,0x15};
char  *str[]  ={"SUN","Mon","Tues","Wed","Thur","Fri","Sat"};
int fd,i;
void pcf8563SetTime()
{
	for(i = 0;i < 7;i++)
    {   
        wiringPiI2CWriteReg8(fd,reg + i,buf[i]);
    } 
}

void pcf8563ReadTime() 
{   
	for(i = 0;i < 7;i++)
    {   
        buf[i] = (char)wiringPiI2CReadReg8(fd,reg + i);
    }
} 

int main()  
{  
	if (wiringPiSetup() < 0)return 1;  
	fd = wiringPiI2CSetup(PCF8563_Address); 
    printf("PCF8564 Test Program ...\n"); 
   	
    pcf8563SetTime(); 
    while(1)  
    {  
       	pcf8563ReadTime();
		buf[0] = buf[0]&0x7F; //sec
		buf[1] = buf[1]&0x7F; //min
		buf[2] = buf[2]&0x3F; //hour
		buf[3] = buf[3]&0x3F; //day
		buf[4] = buf[4]&0x07; //week
		buf[5] = buf[5]&0x1F; //mouth
		//year/month/day
		printf("20%02x/%02x/%02x  ",buf[6],buf[5],buf[3]);
		//hour:minute/second
		printf("%02x:%02x:%02x  ",buf[2],buf[1],buf[0]);
		//weekday
		printf("%s\n",str[(unsigned char)buf[4]]);
		delay(1000); 
	} 
}  
