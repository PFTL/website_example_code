import serial
from time import sleep


dev = serial.Serial("COM4", baudrate=19200)
sleep(1)
dev.write(b'1')
print(dev.readline())
dev.write(b'0')
print(dev.readline())
dev.write(b'1')
print(dev.readline())

