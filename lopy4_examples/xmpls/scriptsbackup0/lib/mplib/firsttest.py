import pycom
import time

def rundemo():
    pycom.heartbeat(False)
    while(True):
        pycom.rgbled(0xff0000)
        time.sleep(1)
        pycom.rgbled(0x00ff00)
        time.sleep(1)
        pycom.rgbled(0x0000ff)
        time.sleep(1)
        print("iteration done")
        
#testcomment