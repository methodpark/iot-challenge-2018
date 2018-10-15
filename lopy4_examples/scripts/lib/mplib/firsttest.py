import pycom
import time
import _thread

binsem = None

def rundemo():
    binsem = _thread.allocate_lock()
    tids = []

    for i in range(5):
        tids.append(_thread.start_new_thread(blink_colors, ()))
    print("number of threads: {}".format(len(tids)))

def blink_colors():
    tid = _thread.get_ident()
    with binsem:
        pycom.heartbeat(False)
    while(True):
        with binsem:
            pycom.rgbled(0xff0000)
        time.sleep(1)
        with binsem:
            pycom.rgbled(0x00ff00)
        time.sleep(1)
        with binsem:
            pycom.rgbled(0x0000ff)
        time.sleep(1)
        print("tid {}: iteration done".format(tid))


        
#testcomment