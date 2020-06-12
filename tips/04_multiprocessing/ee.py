import multiprocessing as mp


class MyClass:
    def __init__(self, queue):
        self.queue = queue

    def simple_method(self):
        print('This is a simple method')

    def mp_simple_method(self):
        self.p = mp.Process(target=self.simple_method)
        self.p.start()

    def wait(self):
        self.p.join()


if __name__ == '__main__':
    queue = mp.Lock()
    my_class = MyClass(queue)
    my_class.mp_simple_method()
    my_class.wait()