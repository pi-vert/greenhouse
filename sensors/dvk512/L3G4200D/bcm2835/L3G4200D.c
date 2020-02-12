#include <bcm2835.h>
#include <stdio.h>
#include "L3G4200D.h"


void L3G4200D_Write(char add,char *data,unsigned char len)
{
	unsigned char i;
	bcm2835_gpio_write(CS,LOW);
    bcm2835_spi_transfer(add|0x40);
   	for(i = 0;i < len;i++)
		bcm2835_spi_transfer(data[i]);
	bcm2835_gpio_write(CS,HIGH); 
}
void L3G4200D_Read(char add,char *data,unsigned char len)
{
    unsigned char i;
	bcm2835_gpio_write(CS,LOW);
    bcm2835_spi_transfer(add|0xc0);
  	for(i = 0;i < len;i++)
    	data[i]=bcm2835_spi_transfer(0xff);
	bcm2835_gpio_write(CS,HIGH);
}

void L3G4200D_Init(void)
{
	char data[5]={0xcf,0x01,0x08,0x00,0x02};
    L3G4200D_Write(CTRL_REG1,data,5);
}
void Read_L3G4200D(float *data)
{
	float Sensitivity;
	char buf[6];
	L3G4200D_Read(CTRL_REG4,buf,1);
	printf("%d %d %d %d %d %d\n",buf[0],buf[1],buf[2],buf[3],buf[4],buf[5]);
	switch(buf[0]&0x30)
	{
		case 0x00:Sensitivity = 8.75;break;
		case 0x10:Sensitivity = 17.5;break;
		case 0x20:Sensitivity =  70;break;
		case 0x30:Sensitivity =  70;break;
	}
	L3G4200D_Read(OUT_X_L,buf,6);
	data[0] =(short)(buf[0]+((short)buf[1]<<8))*Sensitivity/1000;
	data[1] =(short)(buf[2]+((short)buf[3]<<8))*Sensitivity/1000;
	data[2] =(short)(buf[4]+((short)buf[5]<<8))*Sensitivity/1000;
	//printf("1: %3.3f %3.3f %3.3f \n",data[0],data[1],data[2]);
}

void data_int(float *buf)
{
  	unsigned char i;
	float dat[3];
	for(i=0;i<100;i++)
	{ 
		
		Read_L3G4200D(dat);
		bcm2835_delay(10);
		buf[0]+=dat[0];
		buf[2]+=dat[1];
		buf[1]+=dat[2];
 	 }
  	for(i=0;i<3;i++)
	 	buf[i]=buf[i]/100;
	printf ("%3.3f %3.3f %3.3f\n",buf[0],buf[1],buf[2]);	
}

int main(void)
{
	float data[3]={0.0,0.0,0.0};
	float bet[3]={0.0,0.0,0.0};
	float angle_x=0,angle_y=0,angle_z=0;
	char t;

	if (!bcm2835_init())return 1;
	bcm2835_spi_begin();
    bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);   //default
    bcm2835_spi_setDataMode(BCM2835_SPI_MODE3);                //default
    bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_256);//default
    bcm2835_gpio_fsel(CS, BCM2835_GPIO_FSEL_OUTP);//    
    bcm2835_gpio_write(CS, HIGH);

	L3G4200D_Init();
	printf("****** L3G4200D *****\n");
	data_int(bet);

	while(1)
	{
		
		Read_L3G4200D(data);
		data[0]=(int)(data[0]-bet[0]);
		data[1]=(int)(data[1]-bet[1]);
		data[2]=(int)(data[2]-bet[2]);    
    
        data[0]=(int)(data[0]); 
        data[1]=(int)(data[1]); 
        data[2]=(int)(data[2]);    
        
		data[0]/=100;
        data[1]/=100;
        data[2]/=100;
       
		angle_x=(data[0])+angle_x;  if(angle_x>=360)angle_x-=360;
		angle_y=(data[1])+angle_y;  if(angle_y>=360)angle_y-=360;
		angle_z=(data[2])+angle_z;  if(angle_z>=360)angle_z-=360;	
		t++;
		if(t==100)t=0;
		if(t==10)
		{
			printf("\nx=%f rad/s\r\n",data[0]); 
        	printf("y=%f rad/s\r\n",data[1]);
        	printf("z=%f rad/s\r\n",data[2]);    
			bcm2835_delay(1000);
		}
	}
	bcm2835_spi_end();
	bcm2835_close();
	return 0;
}

