#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <stdio.h>
#include <math.h>
#include "LSM303DLHC.h"   

int fdA,fdM;

void LSM303A_Init( void )
{
  	wiringPiI2CWriteReg8(fdA,LSM303A_CTRL_REG1, 0x37);   //25HZ
  	wiringPiI2CWriteReg8(fdA,LSM303A_CTRL_REG4, 0x00);   //LSB,+/-2G
}

void LSM303M_Init( void )
{
	wiringPiI2CWriteReg8(fdM,LSM303M_CRB_REG, 0xa0);	
	wiringPiI2CWriteReg8(fdM,LSM303M_MR_REG, 0x00);
}

void LAM303M_Raed(float *Data)
{
  	char buf[6]={0},reg;
	unsigned char i;
	int Magn_Sensitivity_XY = 0, Magn_Sensitivity_Z = 0;
	
	reg = LSM303M_CRB_REG;
	buf[0] = (char)wiringPiI2CReadReg8(fdM,reg);

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
 
	reg = LSM303M_OUT_X_H;
	for(i = 0;i < 6;i++)
	{
		buf[i] = (char)wiringPiI2CReadReg8(fdM,reg++);
	}

	Data[0]=(float)(short)(buf[0]*0x100+buf[1])*1000/Magn_Sensitivity_XY;
	Data[2]=(float)(short)(buf[2]*0x100+buf[3])*1000/Magn_Sensitivity_Z;
	Data[1]=(float)(short)(buf[4]*0x100+buf[5])*1000/Magn_Sensitivity_XY;
}

void LAM303A_Raed(float *Data)
{
	char buf[6],ctrlx[2];
	unsigned char i,reg;
	float LSM_Acc_Sensitivity = LSM_Acc_Sensitivity_2g;

	reg = LSM303A_OUT_X_L|0x80;
    for(i = 0;i < 6;i++)
    {   
        buf[i] = (char)wiringPiI2CReadReg8(fdA,reg++);
    }  
    reg = LSM303A_CTRL_REG4|0x80;
    for(i = 0;i < 2;i++)
    {   
        ctrlx[i] = (char)wiringPiI2CReadReg8(fdA,reg++);
    }  	
 	
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

	if (wiringPiSetup() < 0)return 1;
	fdA = wiringPiI2CSetup(LSM303A_I2C_ADDR);
	fdM = wiringPiI2CSetup(LSM303M_I2C_ADDR);  
  	printf("start..........\n"); 
  	while (1)
	{
    	LSM303A_Init();
		LAM303A_Raed(Abuf);
     	  
    
     	LSM303M_Init();
		LAM303M_Raed(Mbuf);        
		
		
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

		delay(1000); 
	}
}
