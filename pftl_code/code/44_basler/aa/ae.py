"""
Check options of a parameter
"""
from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
print(camera.ExposureTime.GetUnit())
print(camera.ExposureTime.GetValue())
print(camera.ExposureTime.GetMin())
print(camera.ExposureTime.GetMax())
print(camera.ExposureTime.Unit)
print(camera.ExposureTime.Value)
print(camera.ExposureTime.Min)
print(camera.ExposureTime.Max)
camera.Close()

