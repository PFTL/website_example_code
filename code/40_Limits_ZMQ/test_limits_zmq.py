from sys import getsizeof
from time import sleep, time

import numpy as np
from multiprocessing import Process, Queue

import zmq


def publisher(queue):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    sleep(2)
    print('Starting to publish data from the queue')
    i = 0
    publish_time = 0
    totaltime_0 = time()
    queue_time = 0
    while not queue.empty():
        q_t0 = time()
        data = queue.get()
        queue_time += time() - q_t0
        socket.send_string(data['topic'], zmq.SNDMORE)
        t0 = time()
        socket.send_pyobj(data['data'])
        publish_time += time()-t0
        i += 1
    totaltime_end = time()
    print(f'Published {i} frames in {totaltime_end-totaltime_0} total seconds, out of which {publish_time} were spent publishing data')
    print(f'Time spent dequeing: {queue_time}')
    print(f'Which is equivalent to {i*1048688/publish_time/1024/1024}MB/s')
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
    t0 = 0
    t_end = 0
    while True:
        topic = socket.recv_string()
        data = socket.recv_pyobj()
        if i == 0:
            t0 = time()
        if isinstance(data, str):
            t_end = time()
            break
        i += 1

    print(f'Received {i} frames in {t_end-t0} seconds')
    print(f'This is equivalent to {i*1048688/(t_end-t0)/1024/1024}MB/s')


if __name__ == "__main__":
    num_data_frames = 200

    data = np.random.randint(0, high=2 ** 8, size=(1024, 1024), dtype=np.uint8)
    print(getsizeof(data))

    q_send = Queue()
    while not q_send.empty():
        q_send.get()

    for _ in range(num_data_frames):
        q_send.put({'topic': 'test', 'data': data})

    q_send.put({'topic': 'test', 'data': 'stop'})

    pub = Process(target=publisher, args=(q_send, ))
    pub.start()
    subs = Process(target=subscriber)
    subs.start()
    sleep(2)
    pub.join()
    subs.join()
