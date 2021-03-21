"""
Using Callbacks
"""
import random
import sys
import time

from pypylon import pylon


class ImageEventPrinter(pylon.ImageEventHandler):
    def OnImagesSkipped(self, camera, countOfSkippedImages):
        print("OnImagesSkipped event for device ", camera.GetDeviceInfo().GetModelName())
        print(countOfSkippedImages, " images have been skipped.")
        print()

    def OnImageGrabbed(self, camera, grabResult):
        print("OnImageGrabbed event for device ", camera.GetDeviceInfo().GetModelName())

        # Image grabbed successfully?
        if grabResult.GrabSucceeded():
            print("SizeX: ", grabResult.GetWidth())
            print("SizeY: ", grabResult.GetHeight())
            img = grabResult.GetArray()
            print("Gray values of first row: ", img[0])
            print()
        else:
            print("Error: ", grabResult.GetErrorCode(), grabResult.GetErrorDescription())


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()

camera.RegisterImageEventHandler(ImageEventPrinter(), pylon.RegistrationMode_Append, pylon.Cleanup_Delete)
camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.ExposureTime = 100
camera.MaxNumBuffer = 2
camera.StartGrabbing(1000, pylon.GrabStrategy_LatestImages)
i = 0
while camera.IsGrabbing():
    grab = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
    if grab.GrabSucceeded():
        i += 1
        time.sleep(random.random()/5)

camera.Close()
print(f'Acquired {i} frames')