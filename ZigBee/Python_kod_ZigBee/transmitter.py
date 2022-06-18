import serial
from datetime import datetime
from time import sleep


ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

print('starting')

for i in range(1, 31):
    print(i)
    ser.write(str(i)+' '+str(datetime.now())+'\n')
    sleep(1)
for j in range(31, 61):
    print(j)
    ser.write(str(j)+' '+'jedan dva tri cetiri pet sest sedam osam devet deset jedanaest dvanaest trinaest cetrnaest petnaest sesnaest sedamnaest osamnaest devetnaest dvadeset 1234567891011121314151617181920 '+str(datetime.now())+'\n')
    sleep(1)

ser.close()
