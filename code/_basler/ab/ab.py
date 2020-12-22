"""
Free Run
"""

import time
from threading import Thread

import pyqtgraph as pg
from pypylon import pylon

from PyQt5.QtWidgets import QApplication

app = QApplication([])
imv = pg.ImageView()
imv.show()


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.ExposureTime = 50000
camera.Gain = 0
camera.StartGrabbing(pylon.GrabStrategy_OneByOne)


def to_thread():
    i = 0
    print('Starting to acquire')
    t0 = time.time()
    while camera.IsGrabbing():
        for _ in range(camera.NumReadyBuffers.Value):
            grab = camera.RetrieveResult(100, pylon.TimeoutHandling_ThrowException)
            time.sleep(.01)
            if grab.GrabSucceeded():
                i += 1
                imv.setImage(grab.GetArray(), autoRange=False)
            if i == 10000:
                break
    print(f'Acquired {i} frames in {time.time()-t0:.0f} seconds')


thread = Thread(target=to_thread)
thread.start()
app.exec()

camera.Close()
