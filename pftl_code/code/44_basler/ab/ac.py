"""
Timeout exception
"""
import time

from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.ExposureTime = 105000
camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
for i in range(10):
    grab = camera.RetrieveResult(100, pylon.TimeoutHandling_Return)
    if grab and grab.GrabSucceeded():
        print('Grab succeded')

camera.Close()
