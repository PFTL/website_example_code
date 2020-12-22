"""
Using Callbacks
"""
import time

from pypylon import pylon


class EventPrinter(pylon.ConfigurationEventHandler):
    def OnAttach(self, camera):
        print(f'Before attaching the camera {camera}')

    def OnAttached(self, camera):
        print(f'Attached: {camera.GetDeviceInfo()}')

    def OnOpen(self, camera):
        print('Before opening')

    def OnOpened(self, camera):
        print('After Opening')

    def OnDestroy(self, camera):
        print('Before destroying')

    def OnDestroyed(self, camera):
        print('After destroying')

    def OnClosed(self, camera):
        print('Camera Closed')

    def OnDetach(self, camera):
        print('Detaching')

    def OnGrabStarted(self, camera):
        print('Grab started')
        time.sleep(2)


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
camera.RegisterConfiguration(EventPrinter(), pylon.RegistrationMode_Append, pylon.Cleanup_Delete)

camera.Attach(tl_factory.CreateFirstDevice())

camera.Open()
camera.StartGrabbing(0)
camera.Close()
camera.DestroyDevice()