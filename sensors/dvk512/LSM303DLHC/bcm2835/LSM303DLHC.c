/*LSM303DLHC.c
 * you can build this like:
 * gcc -Wall LSM303DLHC.c -o LSM303DLHC -lbcm2835 -lm
 * sudo ./LSM303DLHC
 */
#include <bcm2835.h>  
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <math.h>

#include "LSM303.h"   

void I2C_WriteByte(unsigned char reg,unsigned data)
{
	char buf[2];
	buf[0]=reg;
	buf[1]=data;
	bcm2835_i2c_write(buf,2);
}

void LSM303A_Init( void )
{
  	I2C_WriteByte(LSM303A_CTRL_REG1, 0x37);   //25HZ
  	I2C_WriteByte(LSM303A_CTRL_REG4, 0x00);   //LSB,+/-2G
}

void LSM303M_Init( void )
{
	I2C_WriteByte(LSM303M_CRB_REG, 0xa0);	
	I2C_WriteByte(LSM303M_MR_REG, 0x00);
}

void LAM303M_Raed(float *Data)
{
  	char buf[6]={0};   
	int Magn_Sensitivity_XY = 0, Magn_Sensitivity_Z = 0;
	
	buf[0] = LSM303M_CRB_REG;
	bcm2835_i2c_write_read_rs(buf,1,buf,1);

	switch(buf[0] & 0xE0)
  	{
  		case LSM303DLHC_FS_1_3_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_1_3Ga;  //1100
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_1_3Ga;    //980
    		break;
  		case LSM303DLHC_FS_1_9_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_1_9Ga;  //855
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_1_9Ga;    //760
    		break;
  		case LSM303DLHC_FS_2_5_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_2_5Ga;  //670
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_2_5Ga;    //600
    		break;
  		case LSM303DLHC_FS_4_0_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_4Ga;    //450
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_4Ga;      //400
    		break;
  		case LSM303DLHC_FS_4_7_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_4_7Ga;  //400
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_4_7Ga;    //355
    		break;
  		case LSM303DLHC_FS_5_6_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_5_6Ga;  //330
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_5_6Ga;    //295
    		break;
  		case LSM303DLHC_FS_8_1_GA:
    		Magn_Sensitivity_XY = LSM303DLHC_M_SENSITIVITY_XY_8_1Ga;  //230
    		Magn_Sensitivity_Z = LSM303DLHC_M_SENSITIVITY_Z_8_1Ga;    //205
    		break;
  	}
 
	buf[0] = LSM303M_OUT_X_H;
	bcm2835_i2c_write_read_rs(buf,1,buf,6);

	Data[0]=(float)(short)(buf[0]*0x100+buf[1])*1000/Magn_Sensitivity_XY;
	Data[2]=(float)(short)(buf[2]*0x100+buf[3])*1000/Magn_Sensitivity_Z;
	Data[1]=(float)(short)(buf[4]*0x100+buf[5])*1000/Magn_Sensitivity_XY;
}

void LAM303A_Raed(float *Data)
{
	char buf[6],ctrlx[2];
	unsigned char i;
	float LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_2g;
	
	buf[0] = LSM303A_OUT_X_L|0x80;
	bcm2835_i2c_write_read_rs(buf,1,buf,6);
	ctrlx[0] = LSM303A_CTRL_REG4|0x80;
	bcm2835_i2c_write_read_rs(ctrlx,1,ctrlx,2);
 	
    switch(ctrlx[0] & 0x30)
    {
    	case LSM303DLHC_FULLSCALE_2G:
      		LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_2g;
      		break;
    	case LSM303DLHC_FULLSCALE_4G:
      		LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_4g;
      		break;
   		case LSM303DLHC_FULLSCALE_8G:
   			LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_8g;
			break;
    	case LSM303DLHC_FULLSCALE_16G:
   			LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_16g;
			break;
  	}
  	/* check in the control register4 the data alignment*/
  	if(ctrlx[0] & 0x40) 
	{
		/* MSB */
    	for(i=0; i<3; i++)
    	{
			Data[i]=(short)(buf[2*i]*0x100+buf[2*i+1])
							*LSM_Acc_Sensitivity/16;
     	}
  	}
  	else /* LSB */
  	{
    	for(i=0; i<3; i++)
		{
			Data[i]=(short)(buf[2*i+1]*0x100+buf[2*i])
							*LSM_Acc_Sensitivity/16;
		}
  	}
}

float Data_conversion(float *AccBuf,float *MagBuf)
{
	unsigned char i;
	float HeadingValue = 0.0f;
	float fNormAcc,fSinRoll,fCosRoll,fSinPitch,fCosPitch;
  	float fTiltedX,fTiltedY;
	for(i=0;i<3;i++)
    	AccBuf[i] /= 100.0f;
      
	fNormAcc = sqrt((AccBuf[0]*AccBuf[0])+(AccBuf[1]*AccBuf[1])
					+(AccBuf[2]*AccBuf[2]));
      
    fSinRoll = AccBuf[1]/fNormAcc;
    fCosRoll = sqrt(1.0-(fSinRoll * fSinRoll));
    fSinPitch = AccBuf[0]/fNormAcc;
    fCosPitch = sqrt(1.0-(fSinPitch * fSinPitch));

      
    fTiltedX = MagBuf[0]*fCosPitch + MagBuf[2]*fSinPitch;
    fTiltedY = MagBuf[0]*fSinRoll*fSinPitch + MagBuf[1]*fCosRoll 
				- MagBuf[2]*fSinRoll*fCosPitch;
			
    HeadingValue = (float) ((atan2f((float)fTiltedY,(float)fTiltedX))*180)/PI;
	HeadingValue +=11;
	if(HeadingValue < 0)
		HeadingValue=HeadingValue+360;
   
	return HeadingValue ;
	
}


int main(void)
{
	float Abuf[3],Mbuf[3];
	float HeadingValue;

	if (!bcm2835_init())return 1;  
  	printf("start..........\n"); 
  	while (1)
	{
     	bcm2835_i2c_begin();  
     	bcm2835_i2c_setSlaveAddress(LSM303A_I2C_ADDR);  
     	bcm2835_i2c_set_baudrate(10000);  

    	LSM303A_Init();
		LAM303A_Raed(Abuf);
    	bcm2835_i2c_end();  
     	
		bcm2835_i2c_begin();  
     	bcm2835_i2c_setSlaveAddress(LSM303M_I2C_ADDR);  
     	bcm2835_i2c_set_baudrate(10000);       
    
     	LSM303M_Init();
		LAM303M_Raed(Mbuf);       
		bcm2835_i2c_end();  
		
		
		HeadingValue = Data_conversion(Abuf,Mbuf);//
		
		printf("\r\n************ LSM303DLHC *********************\r\n");
		
		printf("Ax = %f m/s^2\r\n",Abuf[0]);
		printf("Ay = %f m/s^2\r\n",Abuf[1]);
		printf("Az = %f m/s^2\r\n",Abuf[2]);

		printf("Mx = %f mG\r\n",Mbuf[0] );
		printf("My = %f mG\r\n",Mbuf[1]);
		printf("Mx = %f mG\r\n",Mbuf[2]);
		printf("north=%f degree \r\n",HeadingValue);
		printf("\r\n");

		bcm2835_delay(1000); 
	}
	bcm2835_close();  
    return 0;  
}
