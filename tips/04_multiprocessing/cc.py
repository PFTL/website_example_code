import multiprocessing as mp
import random

val = random.random()

def simple_func():
    print(val)


if __name__ == '__main__':
    print('Before multiprocessing: ')
    simple_func()
    print('After multiprocessing:')
    p = mp.Process(target=simple_func)
    p.start()
    p.join()