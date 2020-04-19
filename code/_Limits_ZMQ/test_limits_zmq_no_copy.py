import random
import sys
from time import sleep, time

import numpy as np
from multiprocessing import Process

import zmq


def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")
    num_data_frames = 1000
    data = np.random.randint(0, high=2 ** 16, size=(1024, 1024), dtype=np.uint16)
    data_size = sys.getsizeof(data)
    sleep(3)
    print('Starting to publish data')
    for i in range(num_data_frames):
        t0 = time()
        socket.send_string('test', zmq.SNDMORE)
        md = dict(
            dtype=str(data.dtype),
            shape=data.shape,
            i=i,
        )
        socket.send_json(md, 0 | zmq.SNDMORE)
        socket.send(data, 0, copy=True, track=False)
        t = time()-t0
        if t<.001:
            sleep(.001-t)
        if i==0:
            publish_time = time()
        if int(i/1000) == i/1000:
            print('Published frames:', i)
    publish_time = time() - publish_time

    socket.send_string('test', zmq.SNDMORE)
    socket.send_json({'stop': True})
    socket.send_string('other', zmq.SNDMORE)
    socket.send_json({'stop': True})
    print(f'Published {num_data_frames} frames in {publish_time:2.2f} seconds')
    print(f'Which is equivalent to {num_data_frames*data_size/publish_time/1024/1024:.0f}MB/s')
    sleep(1)  # Gives enough time to the subscribers to update their status
    socket.close()


def subscriber(topic='test'):
    # delay = random.random()/1000
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    sleep(2)  # Takes a while for TCP connections to propagate
    topic_filter = topic.encode('ascii')
    socket.setsockopt(zmq.SUBSCRIBE, topic_filter)
    i = 0
    t0 = time()
    print('Starting to listen')
    old_i = 0
    skipped_frames = 0
    data_size = 0
    while True:
        topic = socket.recv_string()
        mdata = socket.recv_json(flags=0)
        if mdata.get('stop', None):
            break
        if mdata['i']-old_i>1:
            skipped_frames += mdata['i']-old_i
            sleep(.0001)
            print('Skipped frames', skipped_frames)
            if mdata['i']-old_i > 100:
                break
        old_i = mdata['i']
        if i == 0:
            t0 = time()
        msg = socket.recv(flags=0, copy=True, track=False)
        buf = memoryview(msg)
        data = np.frombuffer(buf, dtype=mdata['dtype'])
        data = data.reshape(mdata['shape']).copy()
        if i == 0:
            data_size = sys.getsizeof(data)
        i += 1
        if int(i/1000) == i/1000:
            print('Received frames:', i)
        # sleep(delay)
    t_end = time()

    print(f'Received {i} frames in {t_end-t0:2.2f} seconds')
    print(f'This is equivalent to {i*data_size/(t_end-t0)/1024/1024:.0f}MB/s')


if __name__ == "__main__":
    pub = Process(target=publisher)
    pub.start()
    sub = Process(target=subscriber)
    sub.start()
    # subs = Process(target=subscriber)
    # subs.start()
    subss = Process(target=subscriber, kwargs={'topic': 'other'})
    subss.start()
    sleep(2)
    pub.join()
    sub.join()
    # subs.join()
    subss.join()
