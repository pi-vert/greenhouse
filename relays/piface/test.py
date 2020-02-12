from time import sleep
import piface.pfio as pfio
pfio.init()
while( True ):
        pfio.digital_write( 6, 1 )
        sleep( 1 )
        pfio.digital_write( 6, 0 )
        sleep( 1 )
