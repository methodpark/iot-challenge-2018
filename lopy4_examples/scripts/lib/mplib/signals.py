import pycom
import time



def blink_fast(color=0xaaaaaa):
    pycom.heartbeat(False)
    while(True):
        pycom.rgbled(color)
        time.sleep(0.2)
        pycom.rgbled(0x0)
        time.sleep(0.2)
    
def blink_slow(color=0xaaaaaa):
    pycom.heartbeat(False)
    while(True):
        pycom.rgbled(color)
        time.sleep(1)
        pycom.rgbled(0x0)
        time.sleep(1)

def blink_color(colors=[0xaa0000, 0x00aa00, 0x0000aa]):
    pycom.heartbeat(False)
    while(True):
        for c in colors:
            pycom.rgbled(c)
            time.sleep(0.5)
            pycom.rgbled(0x0)
            time.sleep(0.5)
    
def blink_n_times(n, color=0xaaaaaa):
    for _ in range(n):
        pycom.rgbled(color)
        time.sleep(0.5)
        pycom.rgbled(0x0)
        time.sleep(0.5)
