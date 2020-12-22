"""
Acquire an image
"""
import numpy as np
from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.StartGrabbing(1)
grab = camera.RetrieveResult(2000, pylon.TimeoutHandling_Return)
img = np.zeros(1)
if grab.GrabSucceeded():
    img = grab.GetArray()

print(f'Size of image: {img.shape}')
camera.Close()