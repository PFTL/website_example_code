"""
Change a parameter Python-style
"""
from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.ExposureTime = 50000
camera.Close()

