from time import sleep, time

import numpy as np
from multiprocessing import Process

import zmq


def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    num_data_frames = 1000
    data = np.random.randint(0, high=2 ** 8, size=(1024, 1024), dtype=np.uint8)
    sleep(2)
    print('Starting to publish data')
    publish_time = time()
    for _ in range(num_data_frames):
        socket.send_string('test', zmq.SNDMORE)
        socket.send_pyobj(data)
    publish_time = time() - publish_time

    socket.send_string('test', zmq.SNDMORE)
    socket.send_pyobj('stop')
    print(f'Published {num_data_frames} frames in {publish_time:2.2f} seconds')
    print(f'Which is equivalent to {num_data_frames*1048688/publish_time/1024/1024:.0f}MB/s')
    sleep(1)  # Gives enough time to the subscribers to update their status
    socket.close()


def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    sleep(1)  # Takes a while for TCP connections to propagate
    topic_filter = 'test'.encode('ascii')
    socket.setsockopt(zmq.SUBSCRIBE, topic_filter)
    i = 0
    t0 = time()
    print('Starting to listen')
    while True:
        topic = socket.recv_string()
        data = socket.recv_pyobj()
        if isinstance(data, str):
            break
        i += 1
    t_end = time()

    print(f'Received {i} frames in {t_end-t0:2.2f} seconds')
    print(f'This is equivalent to {i*1048688/(t_end-t0)/1024/1024:.0f}MB/s')


if __name__ == "__main__":
    pub = Process(target=publisher)
    pub.start()
    subs = Process(target=subscriber)
    subs.start()
    sub = Process(target=subscriber)
    sub.start()
    subss = Process(target=subscriber)
    subss.start()
    sleep(2)
    pub.join()
    subs.join()
    sub.join()
    subss.join()
