import time
from multiprocessing import Process, Event, Queue


class MyTestClass:
    def __init__(self, param1, param2, stop_event: Event, method_queue: Queue):
        self.param1 = param1
        self.param2 = param2
        self.stop_event = stop_event
        self.method_queue = method_queue
        self.run_til_stop()

    def run_til_stop(self):
        while not self.stop_event.is_set():
            if not self.method_queue.empty():
                data = self.method_queue.get()
                func = self.__getattribute__(data['method'])
                if 'args' in data:
                    if 'kwargs' in data:
                        func(*data['args'], **data['kwargs'])
                    else:
                        func(*data['args'])
                else:
                    func()

    def acquire(self):
        for i in range(self.param1):
            print(i)

    def __del__(self):
        print('Deleting the class')


class ProcessClass:
    def __init__(self, cls, stop_event, *args, **kwargs):
        self.cls = cls
        self.method_queue = Queue()
        if kwargs:
            kwargs.update({'stop_event': stop_event, 'method_queue': self.method_queue})
        else:
            kwargs = {'stop_event': stop_event, 'method_queue': self.method_queue}
        self.process = Process(target=self.cls, args=args, kwargs=kwargs)
        self.process.start()

    def __getattribute__(self, item):
        def empty_func():
            return
        try:
            return super().__getattribute__(item)
        except AttributeError:
            if hasattr(self.cls, item):
                func = getattr(self.cls, item)
                self.method_queue.put({'method': func.__name__})
                return empty_func
            raise


if __name__ == '__main__':
    stop_event = Event()
    stop_event.clear()
    method_queue = Queue()
    pc = ProcessClass(MyTestClass, stop_event, 50, 20)
    pc.acquire()
    for i in range(10):
        if pc.process.is_alive():
            time.sleep(.1)
    stop_event.set()
