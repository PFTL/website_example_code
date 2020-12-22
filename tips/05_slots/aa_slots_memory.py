import numpy as np


class Slot:
    # __slots__ = ['var1',]

    def __init__(self):
        var1 = np.zeros((1000,1000), dtype=np.uint8)


data = [Slot() for i in range(100000)]

input('Exit')

print(len(data))