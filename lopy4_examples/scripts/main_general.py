# main.py -- put your code here!
import lib.mplib.firsttest as ft
import lib.mplib.lorawan_otaa as lr
import lib.mplib.signals as sig
import lib.mplib.sleep_and_upload as sl
import time

print("---------- now runs main ----------")
def data_provider():
    return "publishstring"

sleeper = sl.interval_uploader(20, '70B3D57ED000FD2F', '59DECAE556AF25C0BA58C1C6BC942C9E', data_provider)



'''
print("connecting to app:")
lr.connect_to_app('70B3D57ED000FD2F', '59DECAE556AF25C0BA58C1C6BC942C9E')

for i in range(100):
    lr.send_data_to_app("{}".format(i))
    print("after {} seconds still able to send data".format(i))
    time.sleep(i)
'''