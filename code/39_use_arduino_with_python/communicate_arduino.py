import serial
from time import sleep


class Arduino:
    def __init__(self, port):
        self.dev = serial.Serial(port, baudrate=19200)
        sleep(1)

    def query(self, message):
        self.dev.write(message.encode('ascii'))
        line = self.dev.readline().decode('ascii').strip()
        return line


ard = Arduino('COM4')

for _ in range(10):
    print(ard.query('1'))
    sleep(0.5)
    print(ard.query('0'))
    sleep(0.5)

data = []
for _ in range(10):
    data.append(ard.query('2'))

print(data)
