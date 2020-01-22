import serial
from time import sleep


dev = serial.Serial("COM4", baudrate=19200)
sleep(1)

data = []
for _ in range(10):
    dev.write(b'2')
    line = dev.readline()
    line = int(line.decode('ascii'))
    data.append(line)

print(data)
