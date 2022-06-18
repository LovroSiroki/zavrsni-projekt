#!/usr/bin/env python3
from bluedot.btcomm import BluetoothClient
from datetime import datetime
from time import sleep
from signal import pause
def data_received(data):
    print("client: send_time {}, received_time{}".format(data, str(datetime.now())))
print("Connecting")
c = BluetoothClient("rpi4", data_received)
simbols = "jedan dva tri cetiri pet sest sedam osam devet deset jedanaest dvanaest trinaest cetrnaest petnaest sesnaest sedamnaest osamnaest devetnaest dvadeset 1234567891011121314151617181920"
print("Sending")
try:
    for i in range(1, 31):
        c.send("msg: {} {} \n".format(i, str(datetime.now())))
        sleep(1)
    for j in range(31, 61):
        c.send("msg: {} {} {} \n".format(j, simbols, str(datetime.now())))
        sleep(1)
finally:
    c.disconnect()
    
    
