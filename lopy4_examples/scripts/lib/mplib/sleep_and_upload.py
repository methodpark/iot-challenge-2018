from machine import Timer
from network import LoRa
import socket 
import time
import ubinascii
import machine
import pycom
import lib.mplib.lorawan_otaa as lr

'''
sleeps for interval seconds, then uploads a message to app
@param interval:    time in seconds to sleep between messages
@param app_eui:     hex-idetifier
@param app_key:     hex-auth
@paran dp_callback: data providing callback to return a json-string or bytes to be sent
'''
class interval_uploader():
    def __init__(self, interval, app_eui, app_key, dp_callback):
        self.interval = interval                                            # num secs to sleep
        self.callback = dp_callback
        self.app_eui = ubinascii.unhexlify(app_eui)                         # determines app to connect to
        self.app_key = ubinascii.unhexlify(app_key)                         # grants access
        self.lora =  LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)             # used to join a network
        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)             # used to send data to joined network

        self.connect()              # joins application specified through app_eui

        self.__alarm = Timer.Alarm(self._uploader, interval, periodic=True)
    

    def _uploader(self, alarm):       
        pycom.rgbled(0x0000ff)
        print("now uploading:")
        if not self.lora.has_joined():
            self.connect()
        self.s.setblocking(True)
        self.s.send(self.callback())
        self.s.setblocking(False)
        response = self.s.recv(64)
        print("server response: {}".format(response))
        pycom.rgbled(0x0)

    def connect(self):
        self.lora.join(activation=LoRa.OTAA, auth=(self.app_eui, self.app_key), timeout=0)
        while not self.lora.has_joined():
            print("(re)connecting to app...")
            time.sleep(2)
        print("yoined network!")
    
    def stop_upload(self):
        self.__alarm.cancel()