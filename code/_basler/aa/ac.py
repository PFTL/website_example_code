"""
Change a Parameter
"""
from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.ExposureTime.SetValue(50000.0)
camera.Close()