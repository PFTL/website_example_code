import multiprocessing as mp


class MyClass:
    def __init__(self, i):
        self.i = i
        self.file = open(f'{i}.txt', 'w')

    def simple_method(self):
        print('This is a simple method')
        print(f'The stored value is: {self.i}')

    def mp_simple_method(self):
        self.p = mp.Process(target=self.simple_method)
        self.p.start()

    def wait(self):
        self.p.join()
        self.file.close()


if __name__ == '__main__':
    mp.set_start_method('spawn')
    my_class = MyClass(1)
    my_class.mp_simple_method()
    my_class.wait()