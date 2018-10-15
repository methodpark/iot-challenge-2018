from network import LoRa
import socket
import time
import ubinascii
import lib.mplib.signals

'''
create a LoRaWAN socket
'''
def setup_socket():
    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    return s

'''
OTAA through app_eui and app_key from TTN
'''
def connect_to_app(app_eui, app_key):
    print("start connecting")
    # Initialise LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    # create an OTAA authentication parameters
    app_eui = ubinascii.unhexlify(app_eui)
    app_key = ubinascii.unhexlify(app_key)
    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')
    print("has joined network. Ready to send data...")

'''
forward user inputs to testapp on ttn using device lopy
'''
def input_to_app():
    if not s: 
        setup_socket()
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
    # send some data
    while(True):
        d = input("type text to be sent: (type \"stop\" to terminate program)")
        if d == "stop": break
        print("sending data...")
        s.send(d)
        #s.send(bytes([2,9,0,1,1,9,9,8]))
        #s.send(bytes(data, 'utf8'))
        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
        # get any data received (if any...)
        print("checking for server response...")
        response = s.recv(64)
        print(response)


'''
send data ONCE to ttn app
'''
def send_data_to_app(data):
    s = setup_socket()
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
    # send some data
    print("sending data[{}]...".format(data))
    s.send(data)
    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)
    # get any data received (if any...)
    print("checking for server response:")
    response = s.recv(64)
    print(str(response))